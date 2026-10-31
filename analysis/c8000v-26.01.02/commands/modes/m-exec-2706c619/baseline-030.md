# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-014743

```text
(exec)# do-exec show subscriber session <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 0 `；EOL ` RVA 0x34BFE688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9092ae85c31952d1](../../evidence/state_effects-sets-031.md#s-9092ae85c31952d1)

### path-022116

```text
(exec)# do-exec show subscriber session queuing display <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 1 `；EOL ` RVA 0x34BFEEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-95f993e58bf16eb5](../../evidence/state_effects-sets-032.md#s-95f993e58bf16eb5)

### path-024123

```text
(exec)# do-exec show subscriber session queuing enable <number:0..4294967295> <cr>
```

Handler ` RVA 0x10A1CB50 `；selector ` 2 `；EOL ` RVA 0x34BFF280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Subscriber session Unique ID。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d8fc5bf063c7793b](../../evidence/parameters-sets-016.md#p-d8fc5bf063c7793b) · [状态效果 S-5345ee1c960ace7d](../../evidence/state_effects-sets-018.md#s-5345ee1c960ace7d)

### path-014500

```text
(exec)# do-exec show subscriber statistics <cr>
```

Handler ` RVA 0x10A1DBA0 `；selector ` 0 `；EOL ` RVA 0x34C39980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3cf531e304245269](../../evidence/state_effects-sets-013.md#s-3cf531e304245269)

### path-014429

```text
(exec)# do-exec show subscriber tech-support <cr>
```

Handler ` RVA 0x10A2A830 `；selector ` 0 `；EOL ` RVA 0x34BFC528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014553

```text
(exec)# do-exec show subscriber template <cr>
```

Handler ` RVA 0x10A24180 `；selector ` 0 `；EOL ` RVA 0x34BFD3E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018528

```text
(exec)# do-exec show subscriber template active <cr>
```

Handler ` RVA 0x10A242B0 `；selector ` 0 `；EOL ` RVA 0x34BFCE70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022079

```text
(exec)# do-exec show subscriber template id <number:1..30500> <cr>
```

Handler ` RVA 0x10A24240 `；selector ` 0 `；EOL ` RVA 0x34BFD428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Template Id。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-52180e6f7d2d8585](../../evidence/parameters-sets-007.md#p-52180e6f7d2d8585) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024062

```text
(exec)# do-exec show subscriber template key tmpl_id <number:1..30500> <cr>
```

Handler ` RVA 0x10A24720 `；selector ` 0 `；EOL ` RVA 0x34BFCBD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Template Id。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-08c72fd3e4c76054](../../evidence/parameters-sets-001.md#p-08c72fd3e4c76054) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018555

```text
(exec)# do-exec show subscriber template state <cr>
```

Handler ` RVA 0x10A241E0 `；selector ` 0 `；EOL ` RVA 0x34BFD118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012766

```text
(exec)# do-exec show subscriber-policy <cr>
```

Handler ` RVA 0xF282120 `；selector ` 0 `；EOL ` RVA 0x345E7448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012759

```text
(exec)# do-exec show subsys <cr>
```

Handler ` RVA 0xE0898A0 `；selector ` 0 `；EOL ` RVA 0x34177930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-052699c885fd8715](../../evidence/state_effects-sets-002.md#s-052699c885fd8715)

### path-016280

```text
(exec)# do-exec show subsys boottime <cr>
```

Handler ` RVA 0xE04C950 `；selector ` 0 `；EOL ` RVA 0x341764F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020380

```text
(exec)# do-exec show subsys boottime class <cr>
```

Handler ` RVA 0xE04C8F0 `；selector ` 0 `；EOL ` RVA 0x341764C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020361

```text
(exec)# do-exec show subsys boottime init <cr>
```

Handler ` RVA 0xE04C8A0 `；selector ` 0 `；EOL ` RVA 0x34176220 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020377

```text
(exec)# do-exec show subsys class kernel <cr>
```

Handler ` RVA 0xE089910 `；selector ` 0 `；EOL ` RVA 0x34176A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-067122fbc3a1ee32](../../evidence/state_effects-sets-002.md#s-067122fbc3a1ee32)

### path-016297

```text
(exec)# do-exec show subsys memory <cr>
```

Handler ` RVA 0xE04CA60 `；selector ` 0 `；EOL ` RVA 0x34177458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020406

```text
(exec)# do-exec show subsys memory class <cr>
```

Handler ` RVA 0xE04CA00 `；selector ` 0 `；EOL ` RVA 0x34177430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020391

```text
(exec)# do-exec show subsys memory init <cr>
```

Handler ` RVA 0xE04C9B0 `；selector ` 0 `；EOL ` RVA 0x34177188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020345

```text
(exec)# do-exec show subsys name <string> <cr>
```

Handler ` RVA 0xE0898A0 `；selector ` 0 `；EOL ` RVA 0x34175F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Subsystem to list; trailing * is a wildcard。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-421db8a73cf5a5ea](../../evidence/parameters-sets-006.md#p-421db8a73cf5a5ea) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012333

```text
(exec)# do-exec show sum <cr>
```

Handler ` RVA 0xD7C05F0 `；selector ` 0 `；EOL ` RVA 0x34126EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019961

```text
(exec)# do-exec show system insecure configuration <cr>
```

Handler ` RVA 0xE030B60 `；selector ` 0 `；EOL ` RVA 0x3416F2E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019974

```text
(exec)# do-exec show system insecure profile <cr>
```

Handler ` RVA 0xE030E30 `；selector ` 0 `；EOL ` RVA 0x3416F588 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019973

```text
(exec)# do-exec show system security mode <cr>
```

Handler ` RVA 0xE031A40 `；selector ` 0 `；EOL ` RVA 0x3416F860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012665

```text
(exec)# do-exec show table-map <cr>
```

Handler ` RVA 0xDA4A5C0 `；selector ` 2 `；EOL ` RVA 0x33FB4538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0d5d7fb9d5f5a66](../../evidence/conditions-sets-093.md#c-f0d5d7fb9d5f5a66) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012667

```text
(exec)# do-exec show table-map <cr>
```

Handler ` RVA 0xDA4A5C0 `；selector ` 1 `；EOL ` RVA 0x33FB47E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3feeb789eac329cf](../../evidence/conditions-sets-025.md#c-3feeb789eac329cf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015519

```text
(exec)# do-exec show table-map enabled <cr>
```

Handler ` RVA 0xDA4A5C0 `；selector ` 3 `；EOL ` RVA 0x33FB2FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-faf3bc4baf16d13c](../../evidence/conditions-sets-097.md#c-faf3bc4baf16d13c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-89497211cfe7f77c](../../evidence/state_effects-sets-029.md#s-89497211cfe7f77c)

### path-019267

```text
(exec)# do-exec show tableid ha statistics <cr>
```

Handler ` RVA 0x123AFC60 `；selector ` 0 `；EOL ` RVA 0x35842D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b600e66db91dd563](../../evidence/conditions-sets-070.md#c-b600e66db91dd563) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012699

```text
(exec)# do-exec show tacacs <cr>
```

Handler ` RVA 0xDBA8B50 `；selector ` 0 `；EOL ` RVA 0x33FFBC08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae6b025fb75f7085](../../evidence/state_effects-sets-037.md#s-ae6b025fb75f7085)

### path-015884

```text
(exec)# do-exec show tcl mem <cr>
```

Handler ` RVA 0x11144430 `；selector ` 0 `；EOL ` RVA 0x3540C060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2369f6e147b9a59c](../../evidence/conditions-sets-014.md#c-2369f6e147b9a59c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020062

```text
(exec)# do-exec show tcl mem contents <cr>
```

Handler ` RVA 0x11143D30 `；selector ` 0 `；EOL ` RVA 0x3540C038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-23af8f40761813f9](../../evidence/conditions-sets-014.md#c-23af8f40761813f9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014928

```text
(exec)# do-exec show tcp statistics <cr>
```

Handler ` RVA 0xCE261A0 `；selector ` 0 `；EOL ` RVA 0x33CF6230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019241

```text
(exec)# do-exec show tcp statistics ingress <cr>
```

Handler ` RVA 0xCE27BF0 `；selector ` 0 `；EOL ` RVA 0x33CF6208 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-52004cb46631456e](../../evidence/conditions-sets-032.md#c-52004cb46631456e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d006a54b471996d](../../evidence/state_effects-sets-020.md#s-5d006a54b471996d)

### path-021333

```text
(exec)# do-exec show tdm connections aim <number:0..4294967295> <cr>
```

Handler ` RVA 0x15B0E440 `；selector ` 0 `；EOL ` RVA 0x35DECD60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` AIM slot number。

[条件 C-922c95f608bb94da](../../evidence/conditions-sets-056.md#c-922c95f608bb94da) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-aa2ea22ca29461eb](../../evidence/parameters-sets-013.md#p-aa2ea22ca29461eb) · [状态效果 S-bdfb9918b8b74ff1](../../evidence/state_effects-sets-040.md#s-bdfb9918b8b74ff1)

### path-012752

```text
(exec)# do-exec show tech-support <cr>
```

Handler ` RVA 0xDE9E120 `；selector ` 0 `；EOL ` RVA 0x34086880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b46f279ac5855ff](../../evidence/conditions-sets-023.md#c-3b46f279ac5855ff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020604

```text
(exec)# do-exec show tech-support mfib ipv4 <cr>
```

Handler ` RVA 0x1197EB10 `；selector ` 0 `；EOL ` RVA 0x355C02B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b46f279ac5855ff](../../evidence/conditions-sets-023.md#c-3b46f279ac5855ff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b4acdd4698a2c18](../../evidence/state_effects-sets-013.md#s-3b4acdd4698a2c18)

### path-020601

```text
(exec)# do-exec show tech-support mfib ipv6 <cr>
```

Handler ` RVA 0x1197E970 `；selector ` 0 `；EOL ` RVA 0x355C0570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b46f279ac5855ff](../../evidence/conditions-sets-023.md#c-3b46f279ac5855ff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-41c68c51399c5d05](../../evidence/state_effects-sets-014.md#s-41c68c51399c5d05)

### path-020582

```text
(exec)# do-exec show tech-support vrrp ipv4 <cr>
```

Handler ` RVA 0x133CAB60 `；selector ` 0 `；EOL ` RVA 0x35A85C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b46f279ac5855ff](../../evidence/conditions-sets-023.md#c-3b46f279ac5855ff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-be92540a37183e90](../../evidence/state_effects-sets-040.md#s-be92540a37183e90)

### path-020588

```text
(exec)# do-exec show tech-support vrrp ipv6 <cr>
```

Handler ` RVA 0x133CADF0 `；selector ` 0 `；EOL ` RVA 0x35A85EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b46f279ac5855ff](../../evidence/conditions-sets-023.md#c-3b46f279ac5855ff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e779b19609737385](../../evidence/state_effects-sets-049.md#s-e779b19609737385)

### path-012707

```text
(exec)# do-exec show template <cr>
```

Handler ` RVA 0xD6D2EC0 `；selector ` 0 `；EOL ` RVA 0x33ED7618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a873eb590143c5d0](../../evidence/conditions-sets-065.md#c-a873eb590143c5d0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022955

```text
(exec)# do-exec show template binding target interface_global <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 10 `；EOL ` RVA 0x33ED6FB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015767

```text
(exec)# do-exec show template brief <cr>
```

Handler ` RVA 0xD6D2EC0 `；selector ` 16 `；EOL ` RVA 0x33ED6968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015792

```text
(exec)# do-exec show template detail <cr>
```

Handler ` RVA 0xD6D2EC0 `；selector ` 3 `；EOL ` RVA 0x33ED6C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b4fa2c8f4bada93](../../evidence/conditions-sets-036.md#c-5b4fa2c8f4bada93) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015820

```text
(exec)# do-exec show template global <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 0 `；EOL ` RVA 0x33ED3688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e8fe36844b033c92](../../evidence/conditions-sets-090.md#c-e8fe36844b033c92) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019945

```text
(exec)# do-exec show template global all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 25 `；EOL ` RVA 0x33ED21D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022942

```text
(exec)# do-exec show template global binding all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 23 `；EOL ` RVA 0x33ED3010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019932

```text
(exec)# do-exec show template global brief <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 22 `；EOL ` RVA 0x33ED1F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019991

```text
(exec)# do-exec show template global detail <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 24 `；EOL ` RVA 0x33ED33B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-01cd464c29c55dce](../../evidence/conditions-sets-001.md#c-01cd464c29c55dce) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024439

```text
(exec)# do-exec show template global source built-in all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 26 `；EOL ` RVA 0x33ED28B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024903

```text
(exec)# do-exec show template global source built-in original all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 27 `；EOL ` RVA 0x33ED2BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024435

```text
(exec)# do-exec show template global source user all <cr>
```

Handler ` RVA 0xD6DC3B0 `；selector ` 28 `；EOL ` RVA 0x33ED2548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019977

```text
(exec)# do-exec show template interface all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 7 `；EOL ` RVA 0x33ED5198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022933

```text
(exec)# do-exec show template interface binding all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 4 `；EOL ` RVA 0x33ED4088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024430

```text
(exec)# do-exec show template interface binding target interface_global <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 10 `；EOL ` RVA 0x33ED3A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019953

```text
(exec)# do-exec show template interface brief <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 2 `；EOL ` RVA 0x33ED43C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024902

```text
(exec)# do-exec show template interface source built-in Original all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 19 `；EOL ` RVA 0x33ED4B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024449

```text
(exec)# do-exec show template interface source built-in all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 5 `；EOL ` RVA 0x33ED4E48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024437

```text
(exec)# do-exec show template interface source user all <cr>
```

Handler ` RVA 0xD6D3670 `；selector ` 6 `；EOL ` RVA 0x33ED4740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019964

```text
(exec)# do-exec show template service all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 15 `；EOL ` RVA 0x33ED5FF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019986

```text
(exec)# do-exec show template service brief <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 14 `；EOL ` RVA 0x33ED66B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024434

```text
(exec)# do-exec show template service source aaa all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 13 `；EOL ` RVA 0x33ED55A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024443

```text
(exec)# do-exec show template service source built-in all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 11 `；EOL ` RVA 0x33ED5CA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024438

```text
(exec)# do-exec show template service source user all <cr>
```

Handler ` RVA 0xD6D44E0 `；selector ` 12 `；EOL ` RVA 0x33ED5938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015594

```text
(exec)# do-exec show tenant all <cr>
```

Handler ` RVA 0x123E0800 `；selector ` 0 `；EOL ` RVA 0x35847D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-58a28dae1c8290da](../../evidence/conditions-sets-035.md#c-58a28dae1c8290da) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019836

```text
(exec)# do-exec show tenant mapping table <cr>
```

Handler ` RVA 0x123DFFF0 `；selector ` 0 `；EOL ` RVA 0x35848020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-58a28dae1c8290da](../../evidence/conditions-sets-035.md#c-58a28dae1c8290da) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012821

```text
(exec)# do-exec show terminal <cr>
```

Handler ` RVA 0xE2CE600 `；selector ` 0 `；EOL ` RVA 0x3417D680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016032

```text
(exec)# do-exec show test_rib_access get_all_ipv4_protos <cr>
```

Handler ` RVA 0xDC10DD0 `；selector ` 1 `；EOL ` RVA 0x34010958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024908

```text
(exec)# do-exec show test_rib_access get_proto_pdb <string> <number:1..2> <number:0..1> <string> <cr>
```

Handler ` RVA 0xDC10B50 `；selector ` 1 `；EOL ` RVA 0x34010640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` router protocol name；` unsigned_number `  Protocol Type 1:IP 2:OSI ；` unsigned_number `  Address Family 0:IPv4 1:IPv6 ；` string ` Topology name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7afb3a264d306520](../../evidence/parameters-sets-010.md#p-7afb3a264d306520) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025237

```text
(exec)# do-exec show test_rib_access get_route <address> <number:0..6> <number:0..128> <string> <number:0..2> <number:0..65535> <number:0..65535> exact <cr>
```

Handler ` RVA 0xDC0FD90 `；selector ` 0 `；EOL ` RVA 0x3400F6A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of prefix；` unsigned_number `  Address Family 0:IPv4 6:IPv4Mcast ；` unsigned_number `  prefix len；` string ` Topology name；` unsigned_number `  NH Type 0:ANY 1:DEF  2:ALT；` unsigned_number `  NH Include Flter 0:No Incl Filter；` unsigned_number `  NH Exclude Flter 0:No Excl Fltr。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2565c5ac010af90c](../../evidence/parameters-sets-003.md#p-2565c5ac010af90c) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025238

```text
(exec)# do-exec show test_rib_access get_route <address> <number:0..6> <number:0..128> <string> <number:0..2> <number:0..65535> <number:0..65535> long <cr>
```

Handler ` RVA 0xDC0FD90 `；selector ` 1 `；EOL ` RVA 0x3400F9B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of prefix；` unsigned_number `  Address Family 0:IPv4 6:IPv4Mcast ；` unsigned_number `  prefix len；` string ` Topology name；` unsigned_number `  NH Type 0:ANY 1:DEF  2:ALT；` unsigned_number `  NH Include Flter 0:No Incl Filter；` unsigned_number `  NH Exclude Flter 0:No Excl Fltr。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2565c5ac010af90c](../../evidence/parameters-sets-003.md#p-2565c5ac010af90c) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025246

```text
(exec)# do-exec show test_rib_access get_route <address> <number:0..6> <number:0..128> <string> <number:0..2> <number:0..65535> <number:0..65535> long del_nh <cr>
```

Handler ` RVA 0xDC0FD90 `；selector ` 2 `；EOL ` RVA 0x3400F988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of prefix；` unsigned_number `  Address Family 0:IPv4 6:IPv4Mcast ；` unsigned_number `  prefix len；` string ` Topology name；` unsigned_number `  NH Type 0:ANY 1:DEF  2:ALT；` unsigned_number `  NH Include Flter 0:No Incl Filter；` unsigned_number `  NH Exclude Flter 0:No Excl Fltr。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2565c5ac010af90c](../../evidence/parameters-sets-003.md#p-2565c5ac010af90c) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023081

```text
(exec)# do-exec show test_rib_access walk_rib <number:0..7> <string> <cr>
```

Handler ` RVA 0xDC10910 `；selector ` 1 `；EOL ` RVA 0x340100A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number `  Address Family 0:IPv4 1:IPv6 6:IPv4Mcast 7:IPv6Mcast；` string ` Topology name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-97593609663d590a](../../evidence/parameters-sets-012.md#p-97593609663d590a) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012700

```text
(exec)# do-exec show time-range <cr>
```

Handler ` RVA 0xDBCCA30 `；selector ` 0 `；EOL ` RVA 0x33FFE8D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-198f7e7ecea01c8f](../../evidence/conditions-sets-010.md#c-198f7e7ecea01c8f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015755

```text
(exec)# do-exec show time-range ipc <cr>
```

Handler ` RVA 0xDBCA310 `；selector ` 0 `；EOL ` RVA 0x33FFE5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012410

```text
(exec)# do-exec show timers <cr>
```

Handler ` RVA 0xDE91470 `；selector ` 0 `；EOL ` RVA 0x34175290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012573

```text
(exec)# do-exec show topology <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 14 `；EOL ` RVA 0x33FE09D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f731c54b45c8f77e](../../evidence/conditions-sets-095.md#c-f731c54b45c8f77e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012574

```text
(exec)# do-exec show topology <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 0 `；EOL ` RVA 0x33FE0C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea35c2bac3de2dec](../../evidence/conditions-sets-090.md#c-ea35c2bac3de2dec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014283

```text
(exec)# do-exec show topology clients <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 10 `；EOL ` RVA 0x33FE11F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014316

```text
(exec)# do-exec show topology ha <cr>
```

Handler ` RVA 0xDB67370 `；selector ` 9 `；EOL ` RVA 0x33FE14E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-605f5fc5b4f8eb94](../../evidence/conditions-sets-037.md#c-605f5fc5b4f8eb94) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012586

```text
(exec)# do-exec show track <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 1 `；EOL ` RVA 0x34214690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8aba489d1eed4539](../../evidence/conditions-sets-054.md#c-8aba489d1eed4539) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018475

```text
(exec)# do-exec show track <number:1..32767> map <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 11 `；EOL ` RVA 0x342159B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-9c1477298c8524bd](../../evidence/conditions-sets-060.md#c-9c1477298c8524bd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c147d1fcc7a3b437](../../evidence/parameters-sets-015.md#p-c147d1fcc7a3b437) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014299

```text
(exec)# do-exec show track map <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 11 `；EOL ` RVA 0x34215278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014322

```text
(exec)# do-exec show track resolution <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 3 `；EOL ` RVA 0x34214F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c76b22ddafae8411](../../evidence/conditions-sets-077.md#c-c76b22ddafae8411) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014260

```text
(exec)# do-exec show track summary <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 9 `；EOL ` RVA 0x34214C28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014242

```text
(exec)# do-exec show track timers <cr>
```

Handler ` RVA 0xE14F330 `；selector ` 2 `；EOL ` RVA 0x34214980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013308

```text
(exec)# do-exec show transport-map all <cr>
```

Handler ` RVA 0xDBDB160 `；selector ` 0 `；EOL ` RVA 0x34003AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6a76f6f85fbb69f4](../../evidence/conditions-sets-041.md#c-6a76f6f85fbb69f4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017180

```text
(exec)# do-exec show transport-map name <string> <cr>
```

Handler ` RVA 0xDBDB160 `；selector ` 1 `；EOL ` RVA 0x34003DC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Transport map name。

[条件 C-6a76f6f85fbb69f4](../../evidence/conditions-sets-041.md#c-6a76f6f85fbb69f4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a22277e8b6222397](../../evidence/parameters-sets-012.md#p-a22277e8b6222397) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017210

```text
(exec)# do-exec show transport-map type console <cr>
```

Handler ` RVA 0xDBDB160 `；selector ` 2 `；EOL ` RVA 0x340040C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51cff2e89eecb64b](../../evidence/conditions-sets-032.md#c-51cff2e89eecb64b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c438dc11c2525be4](../../evidence/state_effects-sets-042.md#s-c438dc11c2525be4)

### path-020581

```text
(exec)# do-exec show tunnel bgp host-addr <cr>
```

Handler ` RVA 0x1436C2A0 `；selector ` 0 `；EOL ` RVA 0x35D49618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa6109a75a305a86](../../evidence/state_effects-sets-053.md#s-fa6109a75a305a86)

### path-016505

```text
(exec)# do-exec show tunnel groups <cr>
```

Handler ` RVA 0xB50F790 `；selector ` 0 `；EOL ` RVA 0x3483DEE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-048887e6b430b357](../../evidence/state_effects-sets-001.md#s-048887e6b430b357)

### path-016595

```text
(exec)# do-exec show tunnel tunnel-to <cr>
```

Handler ` RVA 0xB51A1B0 `；selector ` 0 `；EOL ` RVA 0x33793B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2b9383d7c7282738](../../evidence/conditions-sets-017.md#c-2b9383d7c7282738) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dc413e8e0018168c](../../evidence/state_effects-sets-047.md#s-dc413e8e0018168c)

### path-012779

```text
(exec)# do-exec show udf <cr>
```

Handler ` RVA 0xF9FDE00 `；selector ` 0 `；EOL ` RVA 0x347B8B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012554

```text
(exec)# do-exec show udp <cr>
```

Handler ` RVA 0xCE472D0 `；selector ` 0 `；EOL ` RVA 0x33D07AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016586

```text
(exec)# do-exec show uidp statistics <cr>
```

Handler ` RVA 0x1599CF10 `；selector ` 0 `；EOL ` RVA 0x35DCFE58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2320f1e09d0e8c76](../../evidence/state_effects-sets-008.md#s-2320f1e09d0e8c76)

### path-016598

```text
(exec)# do-exec show usb-devices summary <cr>
```

Handler ` RVA 0x1581A670 `；selector ` 0 `；EOL ` RVA 0x3435D8A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012453

```text
(exec)# do-exec show users <cr>
```

Handler ` RVA 0xDFE03B0 `；selector ` 0 `；EOL ` RVA 0x3415C2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018691

```text
(exec)# do-exec show vasi pair status <cr>
```

Handler ` RVA 0x1243B640 `；selector ` 0 `；EOL ` RVA 0x358694C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022114

```text
(exec)# do-exec show vasi pair status <number:1..2000> <cr>
```

Handler ` RVA 0x1243B640 `；selector ` 1 `；EOL ` RVA 0x35869498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` VASI pair number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-81163eb070625975](../../evidence/parameters-sets-010.md#p-81163eb070625975) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012446

```text
(exec)# do-exec show version <cr>
```

Handler ` RVA 0xE0065E0 `；selector ` 0 `；EOL ` RVA 0x341644A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8237cd43d4724294](../../evidence/conditions-sets-050.md#c-8237cd43d4724294) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012823

```text
(exec)# do-exec show virtual-service <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 1 `；EOL ` RVA 0x35DBD988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-016634

```text
(exec)# do-exec show virtual-service detail <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 3 `；EOL ` RVA 0x35DBB840 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-016630

```text
(exec)# do-exec show virtual-service list <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 2 `；EOL ` RVA 0x35DBB4C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-023293

```text
(exec)# do-exec show virtual-service profile name <string> <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 4 `；EOL ` RVA 0x35DBBC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the appliance。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0e8111368fd0d6e2](../../evidence/parameters-sets-002.md#p-0e8111368fd0d6e2) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-023297

```text
(exec)# do-exec show virtual-service storage pool list <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 8 `；EOL ` RVA 0x35DBCAF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-024909

```text
(exec)# do-exec show virtual-service storage volume detail volume-name <string> <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 10 `；EOL ` RVA 0x35DBD128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the Storage volume。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6e223a80f24a1d3d](../../evidence/parameters-sets-009.md#p-6e223a80f24a1d3d) · [状态效果 S-8ba25cef7a824fe4](../../evidence/state_effects-sets-030.md#s-8ba25cef7a824fe4)

### path-023299

```text
(exec)# do-exec show virtual-service storage volume list <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 9 `；EOL ` RVA 0x35DBCDC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-016642

```text
(exec)# do-exec show virtual-service tech-support <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 11 `；EOL ` RVA 0x35DBD3E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-020699

```text
(exec)# do-exec show virtual-service trace message <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 12 `；EOL ` RVA 0x35DBD6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-023292

```text
(exec)# do-exec show virtual-service utilization name <string> <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 5 `；EOL ` RVA 0x35DBBFE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the appliance。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d0cc9b246329dddd](../../evidence/parameters-sets-016.md#p-d0cc9b246329dddd) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-023296

```text
(exec)# do-exec show virtual-service utilization statistics CPU <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 6 `；EOL ` RVA 0x35DBC2A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5d6033a1a75099e0](../../evidence/conditions-sets-036.md#c-5d6033a1a75099e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-020697

```text
(exec)# do-exec show virtual-service version installed <cr>
```

Handler ` RVA 0x1590BC10 `；selector ` 7 `；EOL ` RVA 0x35DBC700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b6ce2c920851d74](../../evidence/state_effects-sets-017.md#s-4b6ce2c920851d74)

### path-012623

```text
(exec)# do-exec show vlan <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 0 `；EOL ` RVA 0x35E03988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9d5945e6411a5f0](../../evidence/conditions-sets-084.md#c-d9d5945e6411a5f0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014808

```text
(exec)# do-exec show vlan brief <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 3 `；EOL ` RVA 0x35DFBB58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014876

```text
(exec)# do-exec show vlan counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 12 `；EOL ` RVA 0x35DFCA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5d242a61f73e39c7](../../evidence/conditions-sets-036.md#c-5d242a61f73e39c7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022598

```text
(exec)# do-exec show vlan dot1q tag native <cr>
```

Handler ` RVA 0x15FEB9E0 `；selector ` 3 `；EOL ` RVA 0x35E93C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9d5945e6411a5f0](../../evidence/conditions-sets-084.md#c-d9d5945e6411a5f0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014981

```text
(exec)# do-exec show vlan group <cr>
```

Handler ` RVA 0x15EB6910 `；selector ` 0 `；EOL ` RVA 0x35E60DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9d5945e6411a5f0](../../evidence/conditions-sets-084.md#c-d9d5945e6411a5f0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022609

```text
(exec)# do-exec show vlan group group-name <string> <cr>
```

Handler ` RVA 0x15EB6910 `；selector ` 1 `；EOL ` RVA 0x35E60E78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VLAN group name。

[条件 C-d9d5945e6411a5f0](../../evidence/conditions-sets-084.md#c-d9d5945e6411a5f0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b285a6d56a666287](../../evidence/parameters-sets-014.md#p-b285a6d56a666287) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024297

```text
(exec)# do-exec show vlan group group-name <string> user-count <cr>
```

Handler ` RVA 0x15EB6910 `；selector ` 2 `；EOL ` RVA 0x35E60E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VLAN group name。

[条件 C-d9d5945e6411a5f0](../../evidence/conditions-sets-084.md#c-d9d5945e6411a5f0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b285a6d56a666287](../../evidence/parameters-sets-014.md#p-b285a6d56a666287) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019313

```text
(exec)# do-exec show vlan id <string> <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 2 `；EOL ` RVA 0x35DFC568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` ISL VLAN IDs 1-1005。

[条件 C-70643951d19125a9](../../evidence/conditions-sets-043.md#c-70643951d19125a9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cf337acc24838790](../../evidence/parameters-sets-016.md#p-cf337acc24838790) · [状态效果 S-c729272576154263](../../evidence/state_effects-sets-042.md#s-c729272576154263)

### path-022470

```text
(exec)# do-exec show vlan id <string> counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 11 `；EOL ` RVA 0x35DFC248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` ISL VLAN IDs 1-1005。

[条件 C-ebdf4ed3b5ef4713](../../evidence/conditions-sets-091.md#c-ebdf4ed3b5ef4713) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cf337acc24838790](../../evidence/parameters-sets-016.md#p-cf337acc24838790) · [状态效果 S-c729272576154263](../../evidence/state_effects-sets-042.md#s-c729272576154263)

### path-014925

```text
(exec)# do-exec show vlan ifindex <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 9 `；EOL ` RVA 0x35DFDB58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-286f023a852b3e17](../../evidence/conditions-sets-016.md#c-286f023a852b3e17) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019363

```text
(exec)# do-exec show vlan internal usage <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 13 `；EOL ` RVA 0x35DFE1A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ae75d984a7e7c1d0](../../evidence/conditions-sets-067.md#c-ae75d984a7e7c1d0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014828

```text
(exec)# do-exec show vlan mtu <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 19 `；EOL ` RVA 0x35DFBE00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019260

```text
(exec)# do-exec show vlan name <string> <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 1 `；EOL ` RVA 0x35DFCE40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` A VTP VLAN name。

[条件 C-40c90bf4fa382200](../../evidence/conditions-sets-025.md#c-40c90bf4fa382200) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-453f1d4b5b291239](../../evidence/parameters-sets-006.md#p-453f1d4b5b291239) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014915

```text
(exec)# do-exec show vlan private-vlan <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 8 `；EOL ` RVA 0x35DFD288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d74234984df77224](../../evidence/conditions-sets-083.md#c-d74234984df77224) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014911

```text
(exec)# do-exec show vlan remote-span <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 14 `；EOL ` RVA 0x35DFD568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-497afb4cf5502b83](../../evidence/conditions-sets-029.md#c-497afb4cf5502b83) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014946

```text
(exec)# do-exec show vlan summary <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 10 `；EOL ` RVA 0x35DFDE40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb6639ea672d84d7](../../evidence/conditions-sets-072.md#c-bb6639ea672d84d7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014938

```text
(exec)# do-exec show vlan uni-vlan <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 20 `；EOL ` RVA 0x35DFD8B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e6276929eaee084](../../evidence/conditions-sets-055.md#c-8e6276929eaee084) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014509

```text
(exec)# do-exec show vlan-autoconfig access-interface <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 2 `；EOL ` RVA 0x3544F380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014462

```text
(exec)# do-exec show vlan-autoconfig error-history <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 3 `；EOL ` RVA 0x3544EE30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014485

```text
(exec)# do-exec show vlan-autoconfig statistics <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 5 `；EOL ` RVA 0x3544F0D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014441

```text
(exec)# do-exec show vlan-autoconfig summary <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 4 `；EOL ` RVA 0x3544EB88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014590

```text
(exec)# do-exec show vlan-autoconfig vlan-interface <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 1 `；EOL ` RVA 0x3544F9B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-09bf7cb4a18f66d4](../../evidence/conditions-sets-004.md#c-09bf7cb4a18f66d4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018572

```text
(exec)# do-exec show vlan-autoconfig vlan-interface detailed <cr>
```

Handler ` RVA 0x112BC900 `；selector ` 6 `；EOL ` RVA 0x3544F668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012589

```text
(exec)# do-exec show vlan-range <cr>
```

Handler ` RVA 0x11D3AEA0 `；selector ` 11 `；EOL ` RVA 0x356D3F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012593

```text
(exec)# do-exec show vlans <cr>
```

Handler ` RVA 0x11D205F0 `；selector ` 0 `；EOL ` RVA 0x356CFDF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014542

```text
(exec)# do-exec show vlans summary <cr>
```

Handler ` RVA 0x11D1F260 `；selector ` 0 `；EOL ` RVA 0x356CF5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014558

```text
(exec)# do-exec show vlans tokenring <cr>
```

Handler ` RVA 0x11D1F1E0 `；selector ` 0 `；EOL ` RVA 0x356CF880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014575

```text
(exec)# do-exec show vlans tr-isl <cr>
```

Handler ` RVA 0x11D1ED50 `；selector ` 0 `；EOL ` RVA 0x356CFB28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012693

```text
(exec)# do-exec show vnet <cr>
```

Handler ` RVA 0x12467AB0 `；selector ` 0 `；EOL ` RVA 0x358759D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5bdfae59fd17b6db](../../evidence/conditions-sets-036.md#c-5bdfae59fd17b6db) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a2b46f7247f39448](../../evidence/state_effects-sets-034.md#s-a2b46f7247f39448)

### path-019891

```text
(exec)# do-exec show vpdn dead-cache all <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 1 `；EOL ` RVA 0x3570B978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-874b55779c117b7c](../../evidence/state_effects-sets-029.md#s-874b55779c117b7c)

### path-022889

```text
(exec)# do-exec show vpdn dead-cache group <string> <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 2 `；EOL ` RVA 0x3570B6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ab5305a87287f44c](../../evidence/parameters-sets-013.md#p-ab5305a87287f44c) · [状态效果 S-874b55779c117b7c](../../evidence/state_effects-sets-029.md#s-874b55779c117b7c)

### path-015609

```text
(exec)# do-exec show vpdn domain <cr>
```

Handler ` RVA 0x11D45010 `；selector ` 0 `；EOL ` RVA 0x3570AB50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015618

```text
(exec)# do-exec show vpdn group <cr>
```

Handler ` RVA 0x11DB8260 `；selector ` 0 `；EOL ` RVA 0x3570A128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019852

```text
(exec)# do-exec show vpdn group <string> <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 20 `；EOL ` RVA 0x3570A438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022850

```text
(exec)# do-exec show vpdn group <string> domain <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 22 `；EOL ` RVA 0x3570A410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022840

```text
(exec)# do-exec show vpdn group <string> endpoint <cr>
```

Handler ` RVA 0x11DB9580 `；selector ` 21 `；EOL ` RVA 0x3570A168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-aaf221e0011cb9dd](../../evidence/parameters-sets-013.md#p-aaf221e0011cb9dd) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019918

```text
(exec)# do-exec show vpdn group-select Default <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 138 `；EOL ` RVA 0x3570CC18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3da7336a77d5c288](../../evidence/conditions-sets-024.md#c-3da7336a77d5c288) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019900

```text
(exec)# do-exec show vpdn group-select Summary <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 139 `；EOL ` RVA 0x3570C970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3da7336a77d5c288](../../evidence/conditions-sets-024.md#c-3da7336a77d5c288) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025079

```text
(exec)# do-exec show vpdn group-select keys hostname <string> source-ip <address> <cr>
```

Handler ` RVA 0x11DBAB80 `；selector ` 140 `；EOL ` RVA 0x3570D028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Hostname of user；` address ` Source IP of user。

[条件 C-3da7336a77d5c288](../../evidence/conditions-sets-024.md#c-3da7336a77d5c288) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9c6a85d6ffef3c2d](../../evidence/parameters-sets-012.md#p-9c6a85d6ffef3c2d) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019833

```text
(exec)# do-exec show vpdn history failure <cr>
```

Handler ` RVA 0x11DC0FF0 `；selector ` 0 `；EOL ` RVA 0x35709B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019829

```text
(exec)# do-exec show vpdn history fsm <cr>
```

Handler ` RVA 0x11D81400 `；selector ` 0 `；EOL ` RVA 0x35709E00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019905

```text
(exec)# do-exec show vpdn lsg all <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 1 `；EOL ` RVA 0x3570BF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fc645306706dc4c4](../../evidence/state_effects-sets-053.md#s-fc645306706dc4c4)

### path-022900

```text
(exec)# do-exec show vpdn lsg group <string> <cr>
```

Handler ` RVA 0x11DB8630 `；selector ` 2 `；EOL ` RVA 0x3570BD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of VPDN group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c7153b712117ee31](../../evidence/parameters-sets-015.md#p-c7153b712117ee31) · [状态效果 S-fc645306706dc4c4](../../evidence/state_effects-sets-053.md#s-fc645306706dc4c4)

### path-015638

```text
(exec)# do-exec show vpdn multilink <cr>
```

Handler ` RVA 0x11DB8470 `；selector ` 0 `；EOL ` RVA 0x3570B0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015624

```text
(exec)# do-exec show vpdn redirect <cr>
```

Handler ` RVA 0x11DB8520 `；selector ` 0 `；EOL ` RVA 0x3570ADF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015746

```text
(exec)# do-exec show vpdn redundancy <cr>
```

Handler ` RVA 0x11DC5470 `；selector ` 1 `；EOL ` RVA 0x3570C378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b1934f11cffdf231](../../evidence/conditions-sets-069.md#c-b1934f11cffdf231) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019917

```text
(exec)# do-exec show vpdn redundancy all <cr>
```

Handler ` RVA 0x11DC5470 `；selector ` 4 `；EOL ` RVA 0x3570C410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b1934f11cffdf231](../../evidence/conditions-sets-069.md#c-b1934f11cffdf231) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fd5e87bdcfd64e1d](../../evidence/state_effects-sets-054.md#s-fd5e87bdcfd64e1d)

### path-015651

```text
(exec)# do-exec show vpdn scalability <cr>
```

Handler ` RVA 0x11DE4800 `；selector ` 0 `；EOL ` RVA 0x3570B348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c15c4e5ca41196c](../../evidence/conditions-sets-011.md#c-1c15c4e5ca41196c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022821

```text
(exec)# do-exec show vpdn statistics call fsm <cr>
```

Handler ` RVA 0x11D9C160 `；selector ` 0 `；EOL ` RVA 0x357091F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022829

```text
(exec)# do-exec show vpdn statistics mgr fsm <cr>
```

Handler ` RVA 0x11DA0AF0 `；selector ` 0 `；EOL ` RVA 0x357094C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022827

```text
(exec)# do-exec show vpdn subscriber statistics fsm <cr>
```

Handler ` RVA 0x11E16260 `；selector ` 0 `；EOL ` RVA 0x35709818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012632

```text
(exec)# do-exec show vrf <cr>
```

Handler ` RVA 0xDC3F530 `；selector ` 0 `；EOL ` RVA 0x34014230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ae303442ee1ad78a](../../evidence/conditions-sets-067.md#c-ae303442ee1ad78a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e2c1a2ddba224664](../../evidence/state_effects-sets-048.md#s-e2c1a2ddba224664)

### path-015103

```text
(exec)# do-exec show vrf list <cr>
```

Handler ` RVA 0x12465980 `；selector ` 0 `；EOL ` RVA 0x35872DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-111318d033eddc67](../../evidence/conditions-sets-007.md#c-111318d033eddc67) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e2c1a2ddba224664](../../evidence/state_effects-sets-048.md#s-e2c1a2ddba224664)

### path-015034

```text
(exec)# do-exec show vrf select <cr>
```

Handler ` RVA 0xFADE7A0 `；selector ` 0 `；EOL ` RVA 0x34808200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9f657977d009fe62](../../evidence/conditions-sets-062.md#c-9f657977d009fe62) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e2c1a2ddba224664](../../evidence/state_effects-sets-048.md#s-e2c1a2ddba224664)

### path-012618

```text
(exec)# do-exec show vrrp <cr>
```

Handler ` RVA 0x133C8FB0 `；selector ` 0 `；EOL ` RVA 0x35A80120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71d6cdf48c75ad95](../../evidence/conditions-sets-044.md#c-71d6cdf48c75ad95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6c659c9c22ab0f12](../../evidence/state_effects-sets-023.md#s-6c659c9c22ab0f12)

### path-014286

```text
(exec)# do-exec show vrrs accounting <cr>
```

Handler ` RVA 0xE2FD270 `；selector ` 0 `；EOL ` RVA 0x342A3250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8a528432043a29e](../../evidence/conditions-sets-077.md#c-c8a528432043a29e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-50096ed8271412e0](../../evidence/state_effects-sets-017.md#s-50096ed8271412e0)

### path-014821

```text
(exec)# do-exec show vrrs client <cr>
```

Handler ` RVA 0x133F9730 `；selector ` 0 `；EOL ` RVA 0x35A8A930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-933083c625dafcbb](../../evidence/conditions-sets-057.md#c-933083c625dafcbb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-651ee5fcd693aea8](../../evidence/state_effects-sets-022.md#s-651ee5fcd693aea8)

### path-014274

```text
(exec)# do-exec show vrrs clients <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 1 `；EOL ` RVA 0x3429FE60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-30419cbda49bc5eb](../../evidence/conditions-sets-019.md#c-30419cbda49bc5eb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4336ffc8f1a33b46](../../evidence/state_effects-sets-015.md#s-4336ffc8f1a33b46)

### path-014287

```text
(exec)# do-exec show vrrs group <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 2 `；EOL ` RVA 0x3429FBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-30419cbda49bc5eb](../../evidence/conditions-sets-019.md#c-30419cbda49bc5eb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4336ffc8f1a33b46](../../evidence/state_effects-sets-015.md#s-4336ffc8f1a33b46)

### path-014319

```text
(exec)# do-exec show vrrs internal <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 4 `；EOL ` RVA 0x342A0148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e925b254ea6f39e5](../../evidence/conditions-sets-090.md#c-e925b254ea6f39e5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4336ffc8f1a33b46](../../evidence/state_effects-sets-015.md#s-4336ffc8f1a33b46)

### path-019097

```text
(exec)# do-exec show vrrs pathway address <cr>
```

Handler ` RVA 0x133F9490 `；selector ` 0 `；EOL ` RVA 0x35A8B460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9f6ff7c13de89ea](../../evidence/conditions-sets-084.md#c-d9f6ff7c13de89ea) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-651ee5fcd693aea8](../../evidence/state_effects-sets-022.md#s-651ee5fcd693aea8)

### path-016852

```text
(exec)# do-exec show vrrs plugin database <cr>
```

Handler ` RVA 0xE2FEDD0 `；selector ` 2 `；EOL ` RVA 0x342A6228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-19b0552d619d65bf](../../evidence/conditions-sets-010.md#c-19b0552d619d65bf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cdc8969c53bd6b9b](../../evidence/state_effects-sets-044.md#s-cdc8969c53bd6b9b)

### path-014851

```text
(exec)# do-exec show vrrs server <cr>
```

Handler ` RVA 0x133F97D0 `；selector ` 0 `；EOL ` RVA 0x35A8ADD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2e8e4709a85735dc](../../evidence/conditions-sets-018.md#c-2e8e4709a85735dc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4defd4b4c4c6b40d](../../evidence/state_effects-sets-017.md#s-4defd4b4c4c6b40d)

### path-014238

```text
(exec)# do-exec show vrrs summary <cr>
```

Handler ` RVA 0xE2F9FA0 `；selector ` 3 `；EOL ` RVA 0x3429F8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-30419cbda49bc5eb](../../evidence/conditions-sets-019.md#c-30419cbda49bc5eb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4336ffc8f1a33b46](../../evidence/state_effects-sets-015.md#s-4336ffc8f1a33b46)

### path-014770

```text
(exec)# do-exec show vrrs tag <cr>
```

Handler ` RVA 0x133F9880 `；selector ` 0 `；EOL ` RVA 0x35A8A648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2e8e4709a85735dc](../../evidence/conditions-sets-018.md#c-2e8e4709a85735dc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-651ee5fcd693aea8](../../evidence/state_effects-sets-022.md#s-651ee5fcd693aea8)

### path-015868

```text
(exec)# do-exec show vtemplate queue <cr>
```

Handler ` RVA 0x105C73D0 `；selector ` 1 `；EOL ` RVA 0x34BB14D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-26a28aa87ff105af](../../evidence/conditions-sets-015.md#c-26a28aa87ff105af) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014830

```text
(exec)# do-exec show vtp counters <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 4 `；EOL ` RVA 0x35DFAAE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014862

```text
(exec)# do-exec show vtp devices <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 17 `；EOL ` RVA 0x35DFAE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019115

```text
(exec)# do-exec show vtp devices conflicts <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 18 `；EOL ` RVA 0x35DFADF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014857

```text
(exec)# do-exec show vtp password <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 15 `；EOL ` RVA 0x35DFB2F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014818

```text
(exec)# do-exec show vtp status <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 7 `；EOL ` RVA 0x35E03BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014895

```text
(exec)# do-exec show vtp trunks <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 5 `；EOL ` RVA 0x35DFB600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019163

```text
(exec)# do-exec show vtp trunks all <cr>
```

Handler ` RVA 0x15C743A0 `；selector ` 6 `；EOL ` RVA 0x35DFB5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012591

```text
(exec)# do-exec show wccp <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 0 `；EOL ` RVA 0x34C9FC18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c10d5c462556faf](../../evidence/conditions-sets-017.md#c-2c10d5c462556faf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-014517

```text
(exec)# do-exec show wccp capabilities <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 14 `；EOL ` RVA 0x34C9D3D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ef59ad3ae260f50](../../evidence/conditions-sets-037.md#c-5ef59ad3ae260f50) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018593

```text
(exec)# do-exec show wccp capabilities internal <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 15 `；EOL ` RVA 0x34C9D440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a63ba3df2f8a3a46](../../evidence/conditions-sets-064.md#c-a63ba3df2f8a3a46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-022065

```text
(exec)# do-exec show wccp capabilities internal data <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 16 `；EOL ` RVA 0x34C9D418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-47f742cc9e7a9700](../../evidence/conditions-sets-028.md#c-47f742cc9e7a9700) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018515

```text
(exec)# do-exec show wccp global counters <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 3 `；EOL ` RVA 0x34C9C2E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018444

```text
(exec)# do-exec show wccp global internal <cr>
```

Handler ` RVA 0x10AB5B50 `；selector ` 0 `；EOL ` RVA 0x34C9BFD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9954f77c47576dc9](../../evidence/conditions-sets-059.md#c-9954f77c47576dc9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-014519

```text
(exec)# do-exec show wccp interfaces <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 10 `；EOL ` RVA 0x34C9CB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018531

```text
(exec)# do-exec show wccp interfaces cef <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 13 `；EOL ` RVA 0x34C9CB50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018502

```text
(exec)# do-exec show wccp interfaces counts <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 12 `；EOL ` RVA 0x34C9C8A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018472

```text
(exec)# do-exec show wccp interfaces detail <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 11 `；EOL ` RVA 0x34C9C600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-014468

```text
(exec)# do-exec show wccp summary <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 17 `；EOL ` RVA 0x34C9D060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-16f0c44478eefb74](../../evidence/state_effects-sets-005.md#s-16f0c44478eefb74)

### path-018755

```text
(exec)# do-exec show wccp web-cache assignment <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9E3D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018657

```text
(exec)# do-exec show wccp web-cache buckets <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9DDF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018878

```text
(exec)# do-exec show wccp web-cache clients <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 2 `；EOL ` RVA 0x34C9F370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018887

```text
(exec)# do-exec show wccp web-cache counters <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 4 `；EOL ` RVA 0x34C9F0D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018963

```text
(exec)# do-exec show wccp web-cache detail <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 1 `；EOL ` RVA 0x34C9F6A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-025060

```text
(exec)# do-exec show wccp web-cache hash <address> <address> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 7 `；EOL ` RVA 0x34C9E7E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Destination IPv4 address；` address ` Source IPv4 address；` unsigned_number ` Destination port；` unsigned_number ` Source Port。

[条件 C-df0193e56ad7fe86](../../evidence/conditions-sets-086.md#c-df0193e56ad7fe86) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-32263aafb6e585c0](../../evidence/parameters-sets-004.md#p-32263aafb6e585c0) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018949

```text
(exec)# do-exec show wccp web-cache internal <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 5 `；EOL ` RVA 0x34C9F948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5c5dc8593ba7e814](../../evidence/conditions-sets-036.md#c-5c5dc8593ba7e814) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018677

```text
(exec)# do-exec show wccp web-cache mask-acl <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 18 `；EOL ` RVA 0x34C9E0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018991

```text
(exec)# do-exec show wccp web-cache merged-acl <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 9 `；EOL ` RVA 0x34C9FBF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018782

```text
(exec)# do-exec show wccp web-cache service <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 8 `；EOL ` RVA 0x34C9EAF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-018820

```text
(exec)# do-exec show wccp web-cache view <cr>
```

Handler ` RVA 0x10AD36D0 `；selector ` 6 `；EOL ` RVA 0x34C9ED98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e8f22e8a56f108e](../../evidence/conditions-sets-043.md#c-6e8f22e8a56f108e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f3af7929dca8c374](../../evidence/state_effects-sets-052.md#s-f3af7929dca8c374)

### path-013738

```text
(exec)# do-exec show wrr-queue bandwidth <cr>
```

Handler ` RVA 0x15F29A20 `；selector ` 0 `；EOL ` RVA 0x35E6D2A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013755

```text
(exec)# do-exec show wrr-queue cos-map <cr>
```

Handler ` RVA 0x15F29700 `；selector ` 0 `；EOL ` RVA 0x35E6D550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020530

```text
(exec)# do-exec show wsma agent counters <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463A978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c0493eebdbe4af34](../../evidence/state_effects-sets-041.md#s-c0493eebdbe4af34)

### path-020540

```text
(exec)# do-exec show wsma agent profiles <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463AC30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0f1ae763f8ce2408](../../evidence/state_effects-sets-004.md#s-0f1ae763f8ce2408)

### path-020551

```text
(exec)# do-exec show wsma agent schema <cr>
```

Handler ` RVA 0xF3E9DD0 `；selector ` 0 `；EOL ` RVA 0x3463AEE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bc033162bedfe2a9](../../evidence/state_effects-sets-040.md#s-bc033162bedfe2a9)

### path-016394

```text
(exec)# do-exec show wsma history <cr>
```

Handler ` RVA 0xF3EBEA0 `；selector ` 0 `；EOL ` RVA 0x3463B2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016378

```text
(exec)# do-exec show wsma id <cr>
```

Handler ` RVA 0xF403170 `；selector ` 0 `；EOL ` RVA 0x3463A5F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020547

```text
(exec)# do-exec show wsma profile connections <cr>
```

Handler ` RVA 0xF3D6160 `；selector ` 0 `；EOL ` RVA 0x3462DC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7ae4aa993a4df958](../../evidence/state_effects-sets-026.md#s-7ae4aa993a4df958)

### path-016404

```text
(exec)# do-exec show wsma summary <cr>
```

Handler ` RVA 0xF3EC0F0 `；selector ` 0 `；EOL ` RVA 0x3463B5A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016418

```text
(exec)# do-exec show wsma tech-support <cr>
```

Handler ` RVA 0xF3EC200 `；selector ` 0 `；EOL ` RVA 0x3463B848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012729

```text
(exec)# do-exec show x25 <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 8 `；EOL ` RVA 0x34BC8BF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-897f90db81b13c1b](../../evidence/conditions-sets-053.md#c-897f90db81b13c1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015937

```text
(exec)# do-exec show x25 context <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 10 `；EOL ` RVA 0x34BC7228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fddf4f7bdf7bd4a0](../../evidence/conditions-sets-098.md#c-fddf4f7bdf7bd4a0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020090

```text
(exec)# do-exec show x25 context xot <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 7 `；EOL ` RVA 0x34BC6ED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020145

```text
(exec)# do-exec show x25 cug local-cug <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 11 `；EOL ` RVA 0x34BC8860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-897f90db81b13c1b](../../evidence/conditions-sets-053.md#c-897f90db81b13c1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0a8d6849d8bb7079](../../evidence/state_effects-sets-003.md#s-0a8d6849d8bb7079)

### path-015898

```text
(exec)# do-exec show x25 hunt-group <cr>
```

Handler ` RVA 0x10618C60 `；selector ` 12 `；EOL ` RVA 0x34BC6948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015872

```text
(exec)# do-exec show x25 map <cr>
```

Handler ` RVA 0x105F30D0 `；selector ` 1 `；EOL ` RVA 0x34BC6638 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015952

```text
(exec)# do-exec show x25 profile <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 9 `；EOL ` RVA 0x34BC7D38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-897f90db81b13c1b](../../evidence/conditions-sets-053.md#c-897f90db81b13c1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016003

```text
(exec)# do-exec show x25 remote-red <cr>
```

Handler ` RVA 0x1061D4F0 `；selector ` 0 `；EOL ` RVA 0x34BD4A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-897f90db81b13c1b](../../evidence/conditions-sets-053.md#c-897f90db81b13c1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015890

```text
(exec)# do-exec show x25 route <cr>
```

Handler ` RVA 0x1060FFA0 `；selector ` 3 `；EOL ` RVA 0x34BC6BC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015978

```text
(exec)# do-exec show x25 xot <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 5 `；EOL ` RVA 0x34BC8450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-897f90db81b13c1b](../../evidence/conditions-sets-053.md#c-897f90db81b13c1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020128

```text
(exec)# do-exec show x25 xot access-group <cr>
```

Handler ` RVA 0x105F32F0 `；selector ` 6 `；EOL ` RVA 0x34BC8088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-897f90db81b13c1b](../../evidence/conditions-sets-053.md#c-897f90db81b13c1b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015382

```text
(exec)# do-exec show x28 hunt-group <cr>
```

Handler ` RVA 0xFE6C310 `；selector ` 0 `；EOL ` RVA 0x34900498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-11f85fd974927194](../../evidence/state_effects-sets-004.md#s-11f85fd974927194)

### path-015377

```text
(exec)# do-exec show x29 access-lists <cr>
```

Handler ` RVA 0xFE717E0 `；selector ` 0 `；EOL ` RVA 0x349007E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019211

```text
(exec)# do-exec show xdr client all <cr>
```

Handler ` RVA 0x10C95110 `；selector ` 0 `；EOL ` RVA 0x34CF50F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7727a5be25974bff](../../evidence/state_effects-sets-025.md#s-7727a5be25974bff)

### path-014904

```text
(exec)# do-exec show xdr memory <cr>
```

Handler ` RVA 0x10C96910 `；selector ` 0 `；EOL ` RVA 0x34CF56C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014861

```text
(exec)# do-exec show xdr multicast-group <cr>
```

Handler ` RVA 0x10C95720 `；selector ` 0 `；EOL ` RVA 0x34CF4D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019162

```text
(exec)# do-exec show xdr statistics timers <cr>
```

Handler ` RVA 0xB319600 `；selector ` 0 `；EOL ` RVA 0x33738C60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-36f70731b3eb85b8](../../evidence/state_effects-sets-012.md#s-36f70731b3eb85b8)

### path-014873

```text
(exec)# do-exec show xdr timers <cr>
```

Handler ` RVA 0x10C96830 `；selector ` 0 `；EOL ` RVA 0x34CF53D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020616

```text
(exec)# do-exec show xmpp profile connections <cr>
```

Handler ` RVA 0x12618B60 `；selector ` 0 `；EOL ` RVA 0x358C6178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-88d4a5a64836516a](../../evidence/conditions-sets-053.md#c-88d4a5a64836516a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6829eab1eca164f6](../../evidence/state_effects-sets-022.md#s-6829eab1eca164f6)

### path-012748

```text
(exec)# do-exec show xos <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 12 `；EOL ` RVA 0x340254E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016142

```text
(exec)# do-exec show xos errors <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 2 `；EOL ` RVA 0x34023508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020306

```text
(exec)# do-exec show xos info xdm <cr>
```

Handler ` RVA 0xDCA7840 `；selector ` 0 `；EOL ` RVA 0x34026700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016268

```text
(exec)# do-exec show xos traces <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 1 `；EOL ` RVA 0x34025028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020342

```text
(exec)# do-exec show xos traces address <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 8 `；EOL ` RVA 0x34024AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020356

```text
(exec)# do-exec show xos traces interface <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 7 `；EOL ` RVA 0x34024D58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020262

```text
(exec)# do-exec show xos traces ipc <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 4 `；EOL ` RVA 0x34023818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020278

```text
(exec)# do-exec show xos traces mgd <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 5 `；EOL ` RVA 0x34023AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020314

```text
(exec)# do-exec show xos traces packet <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 11 `；EOL ` RVA 0x340242B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020323

```text
(exec)# do-exec show xos traces policy <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 10 `；EOL ` RVA 0x34024560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020332

```text
(exec)# do-exec show xos traces routing <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 9 `；EOL ` RVA 0x34024808 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020294

```text
(exec)# do-exec show xos traces time <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 6 `；EOL ` RVA 0x34023D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020307

```text
(exec)# do-exec show xos traces utils <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 3 `；EOL ` RVA 0x34024010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020373

```text
(exec)# do-exec show xos traces xdm <cr>
```

Handler ` RVA 0xDC718E0 `；selector ` 13 `；EOL ` RVA 0x34025000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020503

```text
(exec)# do-exec show xsd-format cli <string> <cr>
```

Handler ` RVA 0xF414F30 `；selector ` 0 `；EOL ` RVA 0x34641B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Enter the fully expanded command to display。

[条件 C-4ff4d432f11f727b](../../evidence/conditions-sets-031.md#c-4ff4d432f11f727b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5385741c6a902cd0](../../evidence/parameters-sets-007.md#p-5385741c6a902cd0) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012256

```text
(exec)# do-exec slip <cr>
```

Handler ` RVA 0xFF404B0 `；selector ` 0 `；EOL ` RVA 0x34933EE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024766

```text
(exec)# do-exec snmp get-next v1 <string> <string> oid <string> <cr>
```

Handler ` RVA 0x10527C60 `；selector ` 0 `；EOL ` RVA 0x34B535A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP/IPv6 address or hostname of SNMP destination；` string ` SNMP community string；` string ` Object identifier value。

[条件 C-caa70df812422fbf](../../evidence/conditions-sets-078.md#c-caa70df812422fbf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a202ce2166e2659e](../../evidence/parameters-sets-012.md#p-a202ce2166e2659e) · [状态效果 S-acb159491540ed39](../../evidence/state_effects-sets-037.md#s-acb159491540ed39)

### path-012485

```text
(exec)# do-exec ssh <string> <cr>
```

Handler ` RVA 0x1239B530 `；selector ` 0 `；EOL ` RVA 0x35829648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-3aebf023e080e4a7](../../evidence/conditions-sets-023.md#c-3aebf023e080e4a7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4f9aee87c0358682](../../evidence/parameters-sets-007.md#p-4f9aee87c0358682) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012231

```text
(exec)# do-exec systat <cr>
```

Handler ` RVA 0xDFE03B0 `；selector ` 0 `；EOL ` RVA 0x3415D448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dbe5b845c03dfc65](../../evidence/conditions-sets-085.md#c-dbe5b845c03dfc65) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012277

```text
(exec)# do-exec system kexecreload <cr>
```

Handler ` RVA 0xEA264C0 `；selector ` 0 `；EOL ` RVA 0x34391FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0cc3c97117eb99d4](../../evidence/conditions-sets-005.md#c-0cc3c97117eb99d4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6f430b24bfd1be41](../../evidence/state_effects-sets-024.md#s-6f430b24bfd1be41)

### path-012257

```text
(exec)# do-exec tclquit <cr>
```

Handler ` RVA 0x11148A70 `；selector ` 0 `；EOL ` RVA 0x3540BD00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012258

```text
(exec)# do-exec tclsh <cr>
```

Handler ` RVA 0x11148210 `；selector ` 0 `；EOL ` RVA 0x3540BA48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012250

```text
(exec)# do-exec telnet <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 1 `；EOL ` RVA 0x33CF53F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d7a1c4ba34f8e917](../../evidence/conditions-sets-083.md#c-d7a1c4ba34f8e917) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b2515e0616ab9a57](../../evidence/state_effects-sets-038.md#s-b2515e0616ab9a57)

### path-012251

```text
(exec)# do-exec telnet <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33CF56B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8fbf36f6a2be8a91](../../evidence/conditions-sets-056.md#c-8fbf36f6a2be8a91) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b2515e0616ab9a57](../../evidence/state_effects-sets-038.md#s-b2515e0616ab9a57)

### path-012252

```text
(exec)# do-exec telnet <cr>
```

Handler ` RVA 0xCE631F0 `；selector ` 0 `；EOL ` RVA 0x33CF56E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2f0197d110a9ac4e](../../evidence/conditions-sets-018.md#c-2f0197d110a9ac4e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b2515e0616ab9a57](../../evidence/state_effects-sets-038.md#s-b2515e0616ab9a57)

### path-012396

```text
(exec)# do-exec terminal absolute-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-adc842fa92a9252e](../../evidence/conditions-sets-067.md#c-adc842fa92a9252e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012881

```text
(exec)# do-exec terminal access-class out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f1d651ddbe3e416a](../../evidence/conditions-sets-093.md#c-f1d651ddbe3e416a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0941bae25b9c051c](../../evidence/state_effects-sets-002.md#s-0941bae25b9c051c)

### path-013068

```text
(exec)# do-exec terminal accounting resource <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce2c17d3e0e7ac4f](../../evidence/conditions-sets-079.md#c-ce2c17d3e0e7ac4f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bd1097378be18a46](../../evidence/state_effects-sets-040.md#s-bd1097378be18a46)

### path-013045

```text
(exec)# do-exec terminal authorization reverse-access <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71663b0ebfeab1b3](../../evidence/conditions-sets-044.md#c-71663b0ebfeab1b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-50fa17d428f6744e](../../evidence/state_effects-sets-018.md#s-50fa17d428f6744e)

### path-012387

```text
(exec)# do-exec terminal autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11c2ac2669f5dae7](../../evidence/conditions-sets-007.md#c-11c2ac2669f5dae7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4483e3d89b4d6742](../../evidence/state_effects-sets-015.md#s-4483e3d89b4d6742)

### path-012418

```text
(exec)# do-exec terminal autocommand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94c1ec6bbba03858](../../evidence/conditions-sets-058.md#c-94c1ec6bbba03858) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012424

```text
(exec)# do-exec terminal autocommand-options <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2a79d96e3bd180b7](../../evidence/conditions-sets-017.md#c-2a79d96e3bd180b7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012395

```text
(exec)# do-exec terminal autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013030

```text
(exec)# do-exec terminal autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012399

```text
(exec)# do-exec terminal autohost <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fadfedbcadec8af](../../evidence/conditions-sets-043.md#c-6fadfedbcadec8af) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012414

```text
(exec)# do-exec terminal autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012995

```text
(exec)# do-exec terminal autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8f1561d246d4d237](../../evidence/state_effects-sets-030.md#s-8f1561d246d4d237)

### path-012233

```text
(exec)# do-exec terminal buffer-length <number:16..1536> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` buffer length in bytes。

[条件 C-595bdfb2c3980f29](../../evidence/conditions-sets-035.md#c-595bdfb2c3980f29) · [缺口 G-8bed86c2c1ce685d](../../evidence/gaps-sets-005.md#g-8bed86c2c1ce685d) · [参数 P-c1be88f0a8e29c00](../../evidence/parameters-sets-015.md#p-c1be88f0a8e29c00) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012219

```text
(exec)# do-exec terminal data-character-bits <number:7..8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bits per character。

[条件 C-e68bf37f9a7efad2](../../evidence/conditions-sets-089.md#c-e68bf37f9a7efad2) · [缺口 G-9d45fed12e416da7](../../evidence/gaps-sets-006.md#g-9d45fed12e416da7) · [参数 P-8925e9101d554722](../../evidence/parameters-sets-011.md#p-8925e9101d554722) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012420

```text
(exec)# do-exec terminal databits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d7ede26f2e138fdf](../../evidence/conditions-sets-083.md#c-d7ede26f2e138fdf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c6fde689a0fb5bc5](../../evidence/state_effects-sets-042.md#s-c6fde689a0fb5bc5)

### path-012411

```text
(exec)# do-exec terminal dispatch-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9bb77263a3177667](../../evidence/conditions-sets-060.md#c-9bb77263a3177667) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012368

```text
(exec)# do-exec terminal dispatch-machine <cr>
```

Handler ` RVA 0xDE9D520 `；selector ` 0 `；EOL ` RVA 0x33C63168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e29172beefbec5d0](../../evidence/conditions-sets-087.md#c-e29172beefbec5d0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012242

```text
(exec)# do-exec terminal dispatch-timeout <number:0..4294967294> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 114 `；EOL ` RVA 0x33C61B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Dispatch timer in milliseconds。

[条件 C-1e4399f518a7859d](../../evidence/conditions-sets-012.md#c-1e4399f518a7859d) · [缺口 G-425ef43b62092ab7](../../evidence/gaps-sets-003.md#g-425ef43b62092ab7) · [参数 P-8d68e5fe16a5b7d4](../../evidence/parameters-sets-011.md#p-8d68e5fe16a5b7d4) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012318

```text
(exec)# do-exec terminal domain-lookup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 2 `；EOL ` RVA 0x34128800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012306

```text
(exec)# do-exec terminal download <cr>
```

Handler ` RVA 0xE05E330 `；selector ` 138 `；EOL ` RVA 0x3417D940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-172c6c5ca92c98ca](../../evidence/conditions-sets-009.md#c-172c6c5ca92c98ca) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012343

```text
(exec)# do-exec terminal editing <cr>
```

Handler ` RVA 0xE059390 `；selector ` 137 `；EOL ` RVA 0x3412A1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012398

```text
(exec)# do-exec terminal escape-character <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 5 `；EOL ` RVA 0x341607F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c7c4c06b61bcac67](../../evidence/conditions-sets-077.md#c-c7c4c06b61bcac67) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013056

```text
(exec)# do-exec terminal escape-character BREAK <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 30 `；EOL ` RVA 0x34160818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f448d80a12a76c73](../../evidence/conditions-sets-094.md#c-f448d80a12a76c73) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013126

```text
(exec)# do-exec terminal escape-character DEFAULT <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 32 `；EOL ` RVA 0x34160DF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f2a2f5d595c26b1c](../../evidence/conditions-sets-094.md#c-f2a2f5d595c26b1c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013077

```text
(exec)# do-exec terminal escape-character NONE <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 31 `；EOL ` RVA 0x34160AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f448d80a12a76c73](../../evidence/conditions-sets-094.md#c-f448d80a12a76c73) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012329

```text
(exec)# do-exec terminal exec <cr>
```

Handler ` RVA 0xE059390 `；selector ` 125 `；EOL ` RVA 0x34129088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc130bdaa6ac021e](../../evidence/conditions-sets-097.md#c-fc130bdaa6ac021e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016747

```text
(exec)# do-exec terminal exec prompt expand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 40 `；EOL ` RVA 0x34128B48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016761

```text
(exec)# do-exec terminal exec prompt timestamp <cr>
```

Handler ` RVA 0xE059390 `；selector ` 38 `；EOL ` RVA 0x34128DF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012307

```text
(exec)# do-exec terminal exec-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 11 `；EOL ` RVA 0x3412B998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012313

```text
(exec)# do-exec terminal exec-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 134 `；EOL ` RVA 0x34128270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e255767253b1ee7f](../../evidence/conditions-sets-087.md#c-e255767253b1ee7f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012324

```text
(exec)# do-exec terminal exec-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 13 `；EOL ` RVA 0x3412BD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ffcb4ec917b86ba7](../../evidence/conditions-sets-099.md#c-ffcb4ec917b86ba7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012332

```text
(exec)# do-exec terminal exit <cr>
```

Handler ` RVA 0xE059390 `；selector ` 14 `；EOL ` RVA 0x3412C3B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-de78bf454b325f5a](../../evidence/conditions-sets-086.md#c-de78bf454b325f5a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012353

```text
(exec)# do-exec terminal flush-at-activation <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 164 `；EOL ` RVA 0x33C62DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012352

```text
(exec)# do-exec terminal full-help <cr>
```

Handler ` RVA 0xE059390 `；selector ` 139 `；EOL ` RVA 0x3412A748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012345

```text
(exec)# do-exec terminal history <cr>
```

Handler ` RVA 0xE059390 `；selector ` 135 `；EOL ` RVA 0x34129D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012337

```text
(exec)# do-exec terminal history size <number:0..256> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 136 `；EOL ` RVA 0x34129CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Size of history buffer。

[条件 C-ceb03ddb2533a9c5](../../evidence/conditions-sets-080.md#c-ceb03ddb2533a9c5) · [缺口 G-a8c2b7d393d2b218](../../evidence/gaps-sets-006.md#g-a8c2b7d393d2b218) · [参数 P-4058fcc1fd27a275](../../evidence/parameters-sets-005.md#p-4058fcc1fd27a275) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012409

```text
(exec)# do-exec terminal insecure <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 22 `；EOL ` RVA 0x33C65158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012347

```text
(exec)# do-exec terminal international <cr>
```

Handler ` RVA 0xE059390 `；selector ` 36 `；EOL ` RVA 0x3412A4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016911

```text
(exec)# do-exec terminal ip netmask-format hexadecimal <cr>
```

Handler ` RVA 0xE059390 `；selector ` 33 `；EOL ` RVA 0x33D406C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b7903e0a1ffcd0b8](../../evidence/state_effects-sets-039.md#s-b7903e0a1ffcd0b8)

### path-013034

```text
(exec)# do-exec terminal ip tcp input-coalesce-threshold <number:5..255> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 35 `；EOL ` RVA 0x33D40A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of packets。

[条件 C-a898712e93cf6dc2](../../evidence/conditions-sets-065.md#c-a898712e93cf6dc2) · [缺口 G-46feb337f9717573](../../evidence/gaps-sets-003.md#g-46feb337f9717573) · [参数 P-cdd49c8a2d98adbd](../../evidence/parameters-sets-016.md#p-cdd49c8a2d98adbd) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020902

```text
(exec)# do-exec terminal ipv6 access-class <string> out <cr>
```

Handler ` RVA 0x12165730 `；selector ` 0 `；EOL ` RVA 0x357AFFD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Access-list name。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2f4c08e17f96c869](../../evidence/parameters-sets-004.md#p-2f4c08e17f96c869) · [状态效果 S-b73aaf60fb12189c](../../evidence/state_effects-sets-039.md#s-b73aaf60fb12189c)

### path-016736

```text
(exec)# do-exec terminal ipv6 format scoped_help-string <cr>
```

Handler ` RVA 0x12321A90 `；selector ` 0 `；EOL ` RVA 0x3580DEF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-172c6c5ca92c98ca](../../evidence/conditions-sets-009.md#c-172c6c5ca92c98ca) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-341149f5d87111ee](../../evidence/state_effects-sets-012.md#s-341149f5d87111ee)

### path-012340

```text
(exec)# do-exec terminal length <cr>
```

Handler ` RVA 0xE059390 `；selector ` 0 `；EOL ` RVA 0x34129408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d445eeb2d3807d0](../../evidence/conditions-sets-042.md#c-6d445eeb2d3807d0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9313e4e0d3c0d8d9](../../evidence/state_effects-sets-031.md#s-9313e4e0d3c0d8d9)

### path-012302

```text
(exec)# do-exec terminal location <cr>
```

Handler ` RVA 0xE059390 `；selector ` 15 `；EOL ` RVA 0x3412AF60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c5979aba5cdcdea](../../evidence/conditions-sets-054.md#c-8c5979aba5cdcdea) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012372

```text
(exec)# do-exec terminal lockable <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 116 `；EOL ` RVA 0x33C63AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013023

```text
(exec)# do-exec terminal logging synchronous <cr>
```

Handler ` RVA 0xE054FE0 `；selector ` 0 `；EOL ` RVA 0x3417DD40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-da0bc18fb547c863](../../evidence/conditions-sets-084.md#c-da0bc18fb547c863) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012401

```text
(exec)# do-exec terminal login <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 16 `；EOL ` RVA 0x3417EA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3523a0f5fa113069](../../evidence/conditions-sets-021.md#c-3523a0f5fa113069) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3f506306b3828609](../../evidence/state_effects-sets-014.md#s-3f506306b3828609)

### path-013086

```text
(exec)# do-exec terminal login authentication <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 26 `；EOL ` RVA 0x3417E628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-39e2487ef71f74ed](../../evidence/conditions-sets-022.md#c-39e2487ef71f74ed) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012391

```text
(exec)# do-exec terminal logout-warning <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 141 `；EOL ` RVA 0x33C63E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-87c4f93f1bebd352](../../evidence/conditions-sets-053.md#c-87c4f93f1bebd352) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013138

```text
(exec)# do-exec terminal modem answer-timeout <cr>
```

Handler ` RVA 0xDE8F510 `；selector ` 0 `；EOL ` RVA 0x3417F1B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f35ca67024ca7c6a](../../evidence/conditions-sets-094.md#c-f35ca67024ca7c6a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-0932500779138833](../../evidence/state_effects-sets-002.md#s-0932500779138833)

### path-013371

```text
(exec)# do-exec terminal modem autoconfigure <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB820 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6a340ffbf25caba8](../../evidence/conditions-sets-041.md#c-6a340ffbf25caba8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-982f4a75f07798af](../../evidence/state_effects-sets-032.md#s-982f4a75f07798af)

### path-017265

```text
(exec)# do-exec terminal modem autoconfigure discovery <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f71e30c87984a71a](../../evidence/conditions-sets-095.md#c-f71e30c87984a71a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7241d2a518ce5a7e](../../evidence/state_effects-sets-024.md#s-7241d2a518ce5a7e)

### path-013339

```text
(exec)# do-exec terminal modem busyout <cr>
```

Handler ` RVA 0xFDCEDB0 `；selector ` 162 `；EOL ` RVA 0x348DBB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e701247629a51dc4](../../evidence/conditions-sets-089.md#c-e701247629a51dc4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-982f4a75f07798af](../../evidence/state_effects-sets-032.md#s-982f4a75f07798af)

### path-013121

```text
(exec)# do-exec terminal modem callin <cr>
```

Handler ` RVA 0xDE8F920 `；selector ` 105 `；EOL ` RVA 0x3417F7E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9384f5b556fdec02](../../evidence/state_effects-sets-031.md#s-9384f5b556fdec02)

### path-013133

```text
(exec)# do-exec terminal modem dtr-delay <cr>
```

Handler ` RVA 0xDE8F710 `；selector ` 0 `；EOL ` RVA 0x3417F528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-00dbff7684b84d05](../../evidence/conditions-sets-001.md#c-00dbff7684b84d05) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b6c5f0b787712f2b](../../evidence/state_effects-sets-039.md#s-b6c5f0b787712f2b)

### path-012362

```text
(exec)# do-exec terminal monitor <cr>
```

Handler ` RVA 0xE060540 `；selector ` 4 `；EOL ` RVA 0x3418FDC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012308

```text
(exec)# do-exec terminal motd-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 12 `；EOL ` RVA 0x3412CA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-841860a8a67fa61a](../../evidence/conditions-sets-051.md#c-841860a8a67fa61a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013044

```text
(exec)# do-exec terminal no absolute-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-96e029d559d97375](../../evidence/conditions-sets-058.md#c-96e029d559d97375) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016755

```text
(exec)# do-exec terminal no access-class out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-89b09379a07d4356](../../evidence/conditions-sets-053.md#c-89b09379a07d4356) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1b5e8a637079689c](../../evidence/state_effects-sets-006.md#s-1b5e8a637079689c)

### path-016941

```text
(exec)# do-exec terminal no accounting resource <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-63e2b227269dfdb3](../../evidence/conditions-sets-039.md#c-63e2b227269dfdb3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-755ca38e65c39ad0](../../evidence/state_effects-sets-025.md#s-755ca38e65c39ad0)

### path-012969

```text
(exec)# do-exec terminal no activation-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 110 `；EOL ` RVA 0x33C634C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3ec6d0d0434cfe32](../../evidence/conditions-sets-024.md#c-3ec6d0d0434cfe32) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016926

```text
(exec)# do-exec terminal no authorization reverse-access <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-8d489952ef91b06d](../../evidence/conditions-sets-055.md#c-8d489952ef91b06d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4dcfb07a03b83453](../../evidence/state_effects-sets-017.md#s-4dcfb07a03b83453)

### path-013006

```text
(exec)# do-exec terminal no autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-11c2ac2669f5dae7](../../evidence/conditions-sets-007.md#c-11c2ac2669f5dae7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-405729c30519b117](../../evidence/state_effects-sets-014.md#s-405729c30519b117)

### path-013136

```text
(exec)# do-exec terminal no autocommand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fead61d5d281aa46](../../evidence/conditions-sets-098.md#c-fead61d5d281aa46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013153

```text
(exec)# do-exec terminal no autocommand-options <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fd3a98c3c809a87c](../../evidence/conditions-sets-098.md#c-fd3a98c3c809a87c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013041

```text
(exec)# do-exec terminal no autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016916

```text
(exec)# do-exec terminal no autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013066

```text
(exec)# do-exec terminal no autohost <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-5a05ccf55b35fd32](../../evidence/conditions-sets-035.md#c-5a05ccf55b35fd32) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013114

```text
(exec)# do-exec terminal no autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016890

```text
(exec)# do-exec terminal no autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a52aa4d606841e77](../../evidence/state_effects-sets-035.md#s-a52aa4d606841e77)

### path-012346

```text
(exec)# do-exec terminal no buffer-length <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c4f49d5bafe2b83d](../../evidence/conditions-sets-076.md#c-c4f49d5bafe2b83d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012295

```text
(exec)# do-exec terminal no data-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-246bf77538cbb785](../../evidence/conditions-sets-014.md#c-246bf77538cbb785) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013139

```text
(exec)# do-exec terminal no databits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fe2bf307679439bf](../../evidence/conditions-sets-098.md#c-fe2bf307679439bf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3f9f33c6b8a4a013](../../evidence/state_effects-sets-014.md#s-3f9f33c6b8a4a013)

### path-012983

```text
(exec)# do-exec terminal no disconnect-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 113 `；EOL ` RVA 0x33C63810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-ccd994643e7c8bfc](../../evidence/conditions-sets-079.md#c-ccd994643e7c8bfc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013111

```text
(exec)# do-exec terminal no dispatch-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-9bb77263a3177667](../../evidence/conditions-sets-060.md#c-9bb77263a3177667) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012970

```text
(exec)# do-exec terminal no dispatch-machine <cr>
```

Handler ` RVA 0xDE9D520 `；selector ` 0 `；EOL ` RVA 0x33C63168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-4a25ed96a8bf2b42](../../evidence/conditions-sets-029.md#c-4a25ed96a8bf2b42) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012393

```text
(exec)# do-exec terminal no dispatch-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 114 `；EOL ` RVA 0x33C61B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-7a8f5a7074dc6dad](../../evidence/conditions-sets-048.md#c-7a8f5a7074dc6dad) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012872

```text
(exec)# do-exec terminal no domain-lookup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 2 `；EOL ` RVA 0x34128800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012858

```text
(exec)# do-exec terminal no download <cr>
```

Handler ` RVA 0xE05E330 `；selector ` 138 `；EOL ` RVA 0x3417D940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-172c6c5ca92c98ca](../../evidence/conditions-sets-009.md#c-172c6c5ca92c98ca) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012907

```text
(exec)# do-exec terminal no editing <cr>
```

Handler ` RVA 0xE059390 `；selector ` 137 `；EOL ` RVA 0x3412A1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013046

```text
(exec)# do-exec terminal no escape-character <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 5 `；EOL ` RVA 0x341607F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d2350bd1e29cee23](../../evidence/conditions-sets-081.md#c-d2350bd1e29cee23) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012883

```text
(exec)# do-exec terminal no exec <cr>
```

Handler ` RVA 0xE059390 `；selector ` 125 `；EOL ` RVA 0x34129088 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fc130bdaa6ac021e](../../evidence/conditions-sets-097.md#c-fc130bdaa6ac021e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-020768

```text
(exec)# do-exec terminal no exec prompt expand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 40 `；EOL ` RVA 0x34128B48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-020778

```text
(exec)# do-exec terminal no exec prompt timestamp <cr>
```

Handler ` RVA 0xE059390 `；selector ` 38 `；EOL ` RVA 0x34128DF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012859

```text
(exec)# do-exec terminal no exec-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 11 `；EOL ` RVA 0x3412B998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012867

```text
(exec)# do-exec terminal no exec-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 134 `；EOL ` RVA 0x34128270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-0417a3871cf8c37b](../../evidence/conditions-sets-002.md#c-0417a3871cf8c37b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012878

```text
(exec)# do-exec terminal no exec-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 13 `；EOL ` RVA 0x3412BD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-9fd8492a667f4b4a](../../evidence/conditions-sets-062.md#c-9fd8492a667f4b4a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-017159

```text
(exec)# do-exec terminal no flowcontrol software <cr>
```

Handler ` RVA 0xE056390 `；selector ` 104 `；EOL ` RVA 0x34183DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b7e586ad882939e0](../../evidence/conditions-sets-071.md#c-b7e586ad882939e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-20928669cfa2a0e8](../../evidence/state_effects-sets-007.md#s-20928669cfa2a0e8)

### path-012924

```text
(exec)# do-exec terminal no flush-at-activation <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 164 `；EOL ` RVA 0x33C62DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012923

```text
(exec)# do-exec terminal no full-help <cr>
```

Handler ` RVA 0xE059390 `；selector ` 139 `；EOL ` RVA 0x3412A748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012908

```text
(exec)# do-exec terminal no history <cr>
```

Handler ` RVA 0xE059390 `；selector ` 135 `；EOL ` RVA 0x34129D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012898

```text
(exec)# do-exec terminal no history size <cr>
```

Handler ` RVA 0xE059390 `；selector ` 136 `；EOL ` RVA 0x34129CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3c3aba14b83f38a3](../../evidence/conditions-sets-023.md#c-3c3aba14b83f38a3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013134

```text
(exec)# do-exec terminal no hold-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 122 `；EOL ` RVA 0x33C62820 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-ad3a35431b877450](../../evidence/conditions-sets-067.md#c-ad3a35431b877450) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013106

```text
(exec)# do-exec terminal no insecure <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 22 `；EOL ` RVA 0x33C65158 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012913

```text
(exec)# do-exec terminal no international <cr>
```

Handler ` RVA 0xE059390 `；selector ` 36 `；EOL ` RVA 0x3412A4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-020916

```text
(exec)# do-exec terminal no ip netmask-format hexadecimal <cr>
```

Handler ` RVA 0xE059390 `；selector ` 33 `；EOL ` RVA 0x33D406C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-715a224697126734](../../evidence/state_effects-sets-024.md#s-715a224697126734)

### path-016921

```text
(exec)# do-exec terminal no ip tcp input-coalesce-threshold <cr>
```

Handler ` RVA 0xE059390 `；selector ` 35 `；EOL ` RVA 0x33D40A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-ac39f41cf8ffd2b5](../../evidence/conditions-sets-067.md#c-ac39f41cf8ffd2b5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-023365

```text
(exec)# do-exec terminal no ipv6 access-class <string> out <cr>
```

Handler ` RVA 0x12165730 `；selector ` 0 `；EOL ` RVA 0x357AFFD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Access-list name。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2f4c08e17f96c869](../../evidence/parameters-sets-004.md#p-2f4c08e17f96c869) · [状态效果 S-76b04e230e79a01c](../../evidence/state_effects-sets-025.md#s-76b04e230e79a01c)

### path-020760

```text
(exec)# do-exec terminal no ipv6 format scoped_help-string <cr>
```

Handler ` RVA 0x12321A90 `；selector ` 0 `；EOL ` RVA 0x3580DEF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-172c6c5ca92c98ca](../../evidence/conditions-sets-009.md#c-172c6c5ca92c98ca) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2f52b3a4457e7eed](../../evidence/state_effects-sets-010.md#s-2f52b3a4457e7eed)

### path-012900

```text
(exec)# do-exec terminal no length <cr>
```

Handler ` RVA 0xE059390 `；selector ` 0 `；EOL ` RVA 0x34129408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-257750283bc5dd49](../../evidence/conditions-sets-015.md#c-257750283bc5dd49) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b63e1b9bbd0d55b3](../../evidence/state_effects-sets-039.md#s-b63e1b9bbd0d55b3)

### path-012849

```text
(exec)# do-exec terminal no location <cr>
```

Handler ` RVA 0xE059390 `；selector ` 15 `；EOL ` RVA 0x3412AF60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-147875c3256f512f](../../evidence/conditions-sets-008.md#c-147875c3256f512f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012979

```text
(exec)# do-exec terminal no lockable <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 116 `；EOL ` RVA 0x33C63AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016908

```text
(exec)# do-exec terminal no logging synchronous <cr>
```

Handler ` RVA 0xE054FE0 `；selector ` 0 `；EOL ` RVA 0x3417DD40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b6f7f53864bd3759](../../evidence/conditions-sets-071.md#c-b6f7f53864bd3759) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013069

```text
(exec)# do-exec terminal no login <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 16 `；EOL ` RVA 0x3417EA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3523a0f5fa113069](../../evidence/conditions-sets-021.md#c-3523a0f5fa113069) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c4eac1f5975e633b](../../evidence/state_effects-sets-042.md#s-c4eac1f5975e633b)

### path-016953

```text
(exec)# do-exec terminal no login authentication <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 26 `；EOL ` RVA 0x3417E628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d2114ff5097a9b5e](../../evidence/conditions-sets-081.md#c-d2114ff5097a9b5e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013027

```text
(exec)# do-exec terminal no logout-warning <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 141 `；EOL ` RVA 0x33C63E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-da0a8b2b48e445b8](../../evidence/conditions-sets-084.md#c-da0a8b2b48e445b8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016985

```text
(exec)# do-exec terminal no modem answer-timeout <cr>
```

Handler ` RVA 0xDE8F510 `；selector ` 0 `；EOL ` RVA 0x3417F1B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b08998b40ccd016f](../../evidence/conditions-sets-068.md#c-b08998b40ccd016f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-02e89a634f8ee5a5](../../evidence/state_effects-sets-001.md#s-02e89a634f8ee5a5)

### path-017208

```text
(exec)# do-exec terminal no modem autoconfigure <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB820 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-043b3e26448ca420](../../evidence/conditions-sets-002.md#c-043b3e26448ca420) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-af4940de8695e8b4](../../evidence/state_effects-sets-037.md#s-af4940de8695e8b4)

### path-017176

```text
(exec)# do-exec terminal no modem busyout <cr>
```

Handler ` RVA 0xFDCEDB0 `；selector ` 162 `；EOL ` RVA 0x348DBB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-e701247629a51dc4](../../evidence/conditions-sets-089.md#c-e701247629a51dc4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-af4940de8695e8b4](../../evidence/state_effects-sets-037.md#s-af4940de8695e8b4)

### path-016980

```text
(exec)# do-exec terminal no modem callin <cr>
```

Handler ` RVA 0xDE8F920 `；selector ` 105 `；EOL ` RVA 0x3417F7E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dd89d66b5d566cc5](../../evidence/state_effects-sets-047.md#s-dd89d66b5d566cc5)

### path-016984

```text
(exec)# do-exec terminal no modem dtr-delay <cr>
```

Handler ` RVA 0xDE8F710 `；selector ` 0 `；EOL ` RVA 0x3417F528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-9ae53470a8b59a75](../../evidence/conditions-sets-060.md#c-9ae53470a8b59a75) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c9eabf9ab9c70884](../../evidence/state_effects-sets-043.md#s-c9eabf9ab9c70884)

### path-012956

```text
(exec)# do-exec terminal no monitor <cr>
```

Handler ` RVA 0xE060540 `；selector ` 4 `；EOL ` RVA 0x3418FDC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012860

```text
(exec)# do-exec terminal no motd-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 12 `；EOL ` RVA 0x3412CA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-841860a8a67fa61a](../../evidence/conditions-sets-051.md#c-841860a8a67fa61a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-012889

```text
(exec)# do-exec terminal no notify <cr>
```

Handler ` RVA 0xE059390 `；selector ` 7 `；EOL ` RVA 0x341299F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016897

```text
(exec)# do-exec terminal no ntp pps-discipline <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 1 `；EOL ` RVA 0x348FB6C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-01de1c8237b0afa3](../../evidence/conditions-sets-001.md#c-01de1c8237b0afa3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-17088c9d8fd4ca1e](../../evidence/state_effects-sets-005.md#s-17088c9d8fd4ca1e)

### path-016835

```text
(exec)# do-exec terminal no ntp refclock <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 0 `；EOL ` RVA 0x348FA9E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-5340ad5c1862748b](../../evidence/conditions-sets-033.md#c-5340ad5c1862748b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013135

```text
(exec)# do-exec terminal no parity <cr>
```

Handler ` RVA 0xE059390 `；selector ` 101 `；EOL ` RVA 0x34182320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-daf1a1a899d96d95](../../evidence/conditions-sets-084.md#c-daf1a1a899d96d95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a3f4572cc8b0ef70](../../evidence/state_effects-sets-035.md#s-a3f4572cc8b0ef70)

### path-012925

```text
(exec)# do-exec terminal no password <cr>
```

Handler ` RVA 0xDDD7F60 `；selector ` 18 `；EOL ` RVA 0x34198A68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b50ee6b2c181d844](../../evidence/conditions-sets-070.md#c-b50ee6b2c181d844) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016714

```text
(exec)# do-exec terminal no prc expose <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 0 `；EOL ` RVA 0x341279C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-016721

```text
(exec)# do-exec terminal no prc hide <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 1 `；EOL ` RVA 0x34127C68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)

### path-013084

```text
(exec)# do-exec terminal no private <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 115 `；EOL ` RVA 0x33C64EB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-459e116bff0d6485](../../evidence/conditions-sets-027.md#c-459e116bff0d6485) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d1b285c2b299052c](../../evidence/state_effects-sets-044.md#s-d1b285c2b299052c)
