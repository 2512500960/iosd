# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-011865

```text
(exec)# show ip nbar resources status freebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 27 `；EOL ` RVA 0x3524C410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [参数 P-911a5d92236ca3a7](../../evidence/parameters-sets-011.md#p-911a5d92236ca3a7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006553

```text
(exec)# show ip nbar statistics <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 27 `；EOL ` RVA 0x3524B6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-86effce09d7ececf](../../evidence/conditions-sets-052.md#c-86effce09d7ececf) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006516

```text
(exec)# show ip nbar version <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 1 `；EOL ` RVA 0x3524B3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002793

```text
(exec)# show ip nhrp <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 0 `；EOL ` RVA 0x347F2000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd8f561271462713](../../evidence/conditions-sets-073.md#c-bd8f561271462713) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015121

```text
(exec)# show ip nhrp <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 0 `；EOL ` RVA 0x347F2000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be592514c50f9624](../../evidence/conditions-sets-073.md#c-be592514c50f9624) · [缺口 G-11cf64e66bf8bcc9](../../evidence/gaps-sets-001.md#g-11cf64e66bf8bcc9) · [参数 P-25d6d38100e7fadc](../../evidence/parameters-sets-003.md#p-25d6d38100e7fadc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006661

```text
(exec)# show ip nhrp attribute <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 16 `；EOL ` RVA 0x347F5C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006713

```text
(exec)# show ip nhrp instances <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 20 `；EOL ` RVA 0x347F5F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-acc11270165a94e0](../../evidence/conditions-sets-067.md#c-acc11270165a94e0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006693

```text
(exec)# show ip nhrp map <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 17 `；EOL ` RVA 0x347F5968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-793ea800b9965343](../../evidence/conditions-sets-047.md#c-793ea800b9965343) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019218

```text
(exec)# show ip nhrp map <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 17 `；EOL ` RVA 0x347F5968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3365664df88f7e95](../../evidence/conditions-sets-020.md#c-3365664df88f7e95) · [缺口 G-3a69137f05319b89](../../evidence/gaps-sets-003.md#g-3a69137f05319b89) · [参数 P-6568a812c93047c0](../../evidence/parameters-sets-008.md#p-6568a812c93047c0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006736

```text
(exec)# show ip nhrp multicast <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 4 `；EOL ` RVA 0x347F5548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7635dfc1b5add799](../../evidence/conditions-sets-046.md#c-7635dfc1b5add799) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019230

```text
(exec)# show ip nhrp multicast <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 4 `；EOL ` RVA 0x347F5548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-454c84fe1fab7f80](../../evidence/conditions-sets-027.md#c-454c84fe1fab7f80) · [缺口 G-b697487bd462b620](../../evidence/gaps-sets-006.md#g-b697487bd462b620) · [参数 P-1396d9b0340a62ea](../../evidence/parameters-sets-002.md#p-1396d9b0340a62ea) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006697

```text
(exec)# show ip nhrp nhs <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 3 `；EOL ` RVA 0x347F4350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee6f229a43b075c8](../../evidence/conditions-sets-092.md#c-ee6f229a43b075c8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019236

```text
(exec)# show ip nhrp nhs <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 3 `；EOL ` RVA 0x347F4350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f6aedc99dd58fbd3](../../evidence/conditions-sets-095.md#c-f6aedc99dd58fbd3) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022550

```text
(exec)# show ip nhrp nhs <interface> redundancy <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 10 `；EOL ` RVA 0x347F4EB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f6aedc99dd58fbd3](../../evidence/conditions-sets-095.md#c-f6aedc99dd58fbd3) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024857

```text
(exec)# show ip nhrp nhs <interface> redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 14 `；EOL ` RVA 0x347F4958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-f6aedc99dd58fbd3](../../evidence/conditions-sets-095.md#c-f6aedc99dd58fbd3) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-2f94580451c4bcf7](../../evidence/parameters-sets-004.md#p-2f94580451c4bcf7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024277

```text
(exec)# show ip nhrp nhs <interface> redundancy preempted <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 12 `；EOL ` RVA 0x347F4BE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f6aedc99dd58fbd3](../../evidence/conditions-sets-095.md#c-f6aedc99dd58fbd3) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024266

```text
(exec)# show ip nhrp nhs <interface> redundancy running <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 11 `；EOL ` RVA 0x347F4648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f6aedc99dd58fbd3](../../evidence/conditions-sets-095.md#c-f6aedc99dd58fbd3) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024283

```text
(exec)# show ip nhrp nhs <interface> redundancy waiting <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 13 `；EOL ` RVA 0x347F4E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f6aedc99dd58fbd3](../../evidence/conditions-sets-095.md#c-f6aedc99dd58fbd3) · [缺口 G-a24c209c1f029862](../../evidence/gaps-sets-006.md#g-a24c209c1f029862) · [参数 P-f4bbc780f0b0bf6a](../../evidence/parameters-sets-018.md#p-f4bbc780f0b0bf6a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009762

```text
(exec)# show ip nhrp nhs redundancy <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 10 `；EOL ` RVA 0x347F4EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee6f229a43b075c8](../../evidence/conditions-sets-092.md#c-ee6f229a43b075c8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011870

```text
(exec)# show ip nhrp nhs redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 14 `；EOL ` RVA 0x347F4958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-ee6f229a43b075c8](../../evidence/conditions-sets-092.md#c-ee6f229a43b075c8) · [参数 P-133a9e4b186bdac7](../../evidence/parameters-sets-002.md#p-133a9e4b186bdac7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011343

```text
(exec)# show ip nhrp nhs redundancy preempted <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 12 `；EOL ` RVA 0x347F4BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee6f229a43b075c8](../../evidence/conditions-sets-092.md#c-ee6f229a43b075c8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011334

```text
(exec)# show ip nhrp nhs redundancy running <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 11 `；EOL ` RVA 0x347F4648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee6f229a43b075c8](../../evidence/conditions-sets-092.md#c-ee6f229a43b075c8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011346

```text
(exec)# show ip nhrp nhs redundancy waiting <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 13 `；EOL ` RVA 0x347F4E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee6f229a43b075c8](../../evidence/conditions-sets-092.md#c-ee6f229a43b075c8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006571

```text
(exec)# show ip nhrp purge <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 2 `；EOL ` RVA 0x347F3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006785

```text
(exec)# show ip nhrp redirect <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 6 `；EOL ` RVA 0x347F1958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009764

```text
(exec)# show ip nhrp redirect statistics <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 7 `；EOL ` RVA 0x347F1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006779

```text
(exec)# show ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE580 `；selector ` 0 `；EOL ` RVA 0x34BF8EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-eeecbc59dec838c0](../../evidence/state_effects-sets-050.md#s-eeecbc59dec838c0)

### path-006701

```text
(exec)# show ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 18 `；EOL ` RVA 0x347F3B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80969c21d05cb775](../../evidence/conditions-sets-050.md#c-80969c21d05cb775) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019237

```text
(exec)# show ip nhrp stats <interface> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 18 `；EOL ` RVA 0x347F3B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d7b693b43aaa7f7b](../../evidence/conditions-sets-083.md#c-d7b693b43aaa7f7b) · [缺口 G-2438a1dc2685beb5](../../evidence/gaps-sets-002.md#g-2438a1dc2685beb5) · [参数 P-b3ec1b1c3984c82d](../../evidence/parameters-sets-014.md#p-b3ec1b1c3984c82d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006602

```text
(exec)# show ip nhrp traffic <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 1 `；EOL ` RVA 0x347F3670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002794

```text
(exec)# show ip ospf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 7 `；EOL ` RVA 0x34892168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9fe8519482ec89e](../../evidence/conditions-sets-090.md#c-e9fe8519482ec89e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006402

```text
(exec)# show ip ospf bad-checksum <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 1 `；EOL ` RVA 0x3487AD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006696

```text
(exec)# show ip ospf border-routers <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 17 `；EOL ` RVA 0x348788A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006977

```text
(exec)# show ip ospf database <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 58 `；EOL ` RVA 0x34895630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e68542957fd6318b](../../evidence/conditions-sets-089.md#c-e68542957fd6318b) · [状态效果 S-cc91860de1df0769](../../evidence/state_effects-sets-043.md#s-cc91860de1df0769)

### path-009891

```text
(exec)# show ip ospf database database-summary <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 60 `；EOL ` RVA 0x34896290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-03510c5a0f8b69a0](../../evidence/conditions-sets-002.md#c-03510c5a0f8b69a0) · [状态效果 S-cc91860de1df0769](../../evidence/state_effects-sets-043.md#s-cc91860de1df0769)

### path-011418

```text
(exec)# show ip ospf database database-summary detail <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 54 `；EOL ` RVA 0x348965B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b5be62908a105171](../../evidence/conditions-sets-070.md#c-b5be62908a105171) · [状态效果 S-ad8d12eda9a8abaf](../../evidence/state_effects-sets-037.md#s-ad8d12eda9a8abaf)

### path-006805

```text
(exec)# show ip ospf delete-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 57 `；EOL ` RVA 0x34876370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019032

```text
(exec)# show ip ospf events <?option@555589dca990> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 16 `；EOL ` RVA 0x348769F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd512c17107faa03](../../evidence/conditions-sets-085.md#c-dd512c17107faa03) · [缺口 G-01e125fbb768b747](../../evidence/gaps-sets-001.md#g-01e125fbb768b747) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006490

```text
(exec)# show ip ospf events <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 16 `；EOL ` RVA 0x348769F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b07ceb988da204ca](../../evidence/conditions-sets-068.md#c-b07ceb988da204ca) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006884

```text
(exec)# show ip ospf flood-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 66 `；EOL ` RVA 0x34890B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d562acd02ea27da6](../../evidence/conditions-sets-082.md#c-d562acd02ea27da6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019444

```text
(exec)# show ip ospf flood-list <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 66 `；EOL ` RVA 0x34890B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a326ca4071735d36](../../evidence/conditions-sets-063.md#c-a326ca4071735d36) · [缺口 G-c41d3ddccf01d0ea](../../evidence/gaps-sets-007.md#g-c41d3ddccf01d0ea) · [参数 P-559bdfbb17cb41ba](../../evidence/parameters-sets-007.md#p-559bdfbb17cb41ba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006898

```text
(exec)# show ip ospf interface <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 65 `；EOL ` RVA 0x3488FEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-40a5d5639a8d1a3c](../../evidence/conditions-sets-025.md#c-40a5d5639a8d1a3c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019432

```text
(exec)# show ip ospf interface <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 65 `；EOL ` RVA 0x3488FEC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08370333012f05f6](../../evidence/conditions-sets-004.md#c-08370333012f05f6) · [缺口 G-4ae8073d2450ae27](../../evidence/gaps-sets-003.md#g-4ae8073d2450ae27) · [参数 P-7d4580ce235b9ca9](../../evidence/parameters-sets-010.md#p-7d4580ce235b9ca9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009882

```text
(exec)# show ip ospf internal forwarding-addresses <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 23 `；EOL ` RVA 0x34891EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011399

```text
(exec)# show ip ospf internal memory cache <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 2 `；EOL ` RVA 0x34891C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006732

```text
(exec)# show ip ospf max-metric <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 10 `；EOL ` RVA 0x34879EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006708

```text
(exec)# show ip ospf maxage-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 9 `；EOL ` RVA 0x3487A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011376

```text
(exec)# show ip ospf mpls traffic-eng link <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 61 `；EOL ` RVA 0x3488F830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-4ca9cdb25b834938](../../evidence/state_effects-sets-017.md#s-4ca9cdb25b834938)

### path-006551

```text
(exec)# show ip ospf multi-area <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 68 `；EOL ` RVA 0x348775F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b3359216e563a7c](../../evidence/conditions-sets-011.md#c-1b3359216e563a7c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006960

```text
(exec)# show ip ospf neighbor <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 71 `；EOL ` RVA 0x34890EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f1c4a8423418580](../../evidence/conditions-sets-031.md#c-4f1c4a8423418580) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019535

```text
(exec)# show ip ospf neighbor <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 71 `；EOL ` RVA 0x34890EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-87a21bb6cd917e5e](../../evidence/conditions-sets-052.md#c-87a21bb6cd917e5e) · [缺口 G-f00c520c112f9683](../../evidence/gaps-sets-008.md#g-f00c520c112f9683) · [参数 P-0f45569dc916688e](../../evidence/parameters-sets-002.md#p-0f45569dc916688e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006580

```text
(exec)# show ip ospf nsf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 14 `；EOL ` RVA 0x34877900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006817

```text
(exec)# show ip ospf nsr <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 20 `；EOL ` RVA 0x33FC8EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009777

```text
(exec)# show ip ospf nsr objects <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 21 `；EOL ` RVA 0x33FC8C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009793

```text
(exec)# show ip ospf nsr statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 22 `；EOL ` RVA 0x33FC8EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006927

```text
(exec)# show ip ospf request-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 73 `；EOL ` RVA 0x34891878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12365064d015748a](../../evidence/conditions-sets-007.md#c-12365064d015748a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019493

```text
(exec)# show ip ospf request-list <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 73 `；EOL ` RVA 0x34891878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c0eb55b4ba54d470](../../evidence/conditions-sets-074.md#c-c0eb55b4ba54d470) · [缺口 G-5ee5d435e7b117a7](../../evidence/gaps-sets-004.md#g-5ee5d435e7b117a7) · [参数 P-61af90c3cc0c36a7](../../evidence/parameters-sets-008.md#p-61af90c3cc0c36a7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006914

```text
(exec)# show ip ospf retransmission-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 72 `；EOL ` RVA 0x34891490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61d1a2f11bb98e61](../../evidence/conditions-sets-038.md#c-61d1a2f11bb98e61) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019486

```text
(exec)# show ip ospf retransmission-list <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 72 `；EOL ` RVA 0x34891490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfddac48a97bfcc6](../../evidence/conditions-sets-074.md#c-bfddac48a97bfcc6) · [缺口 G-ddf5cad6f7926983](../../evidence/gaps-sets-008.md#g-ddf5cad6f7926983) · [参数 P-d0c7091b8167d658](../../evidence/parameters-sets-016.md#p-d0c7091b8167d658) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006773

```text
(exec)# show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 19 `；EOL ` RVA 0x34879088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b9c1ae9fb507ea7](../../evidence/conditions-sets-017.md#c-2b9c1ae9fb507ea7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006774

```text
(exec)# show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 18 `；EOL ` RVA 0x34879308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f699ed62843313b6](../../evidence/conditions-sets-095.md#c-f699ed62843313b6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006511

```text
(exec)# show ip ospf sham-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 6 `；EOL ` RVA 0x34877308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006735

```text
(exec)# show ip ospf statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 11 `；EOL ` RVA 0x34879890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006652

```text
(exec)# show ip ospf summary-address <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 8 `；EOL ` RVA 0x34878228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009600

```text
(exec)# show ip ospf timers lsa-group <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 12 `；EOL ` RVA 0x34877C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009623

```text
(exec)# show ip ospf timers rate-limit <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 13 `；EOL ` RVA 0x34877EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006771

```text
(exec)# show ip ospf topology-info <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 15 `；EOL ` RVA 0x3487A778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2bdf75d04d89e48](../../evidence/conditions-sets-087.md#c-e2bdf75d04d89e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006886

```text
(exec)# show ip ospf traffic <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 67 `；EOL ` RVA 0x34890680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c1785290badd949](../../evidence/conditions-sets-060.md#c-9c1785290badd949) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019445

```text
(exec)# show ip ospf traffic <interface> <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 67 `；EOL ` RVA 0x34890680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-666ede9f6afa56d2](../../evidence/conditions-sets-040.md#c-666ede9f6afa56d2) · [缺口 G-b924082425b71df1](../../evidence/gaps-sets-007.md#g-b924082425b71df1) · [参数 P-4087e195c55a7fdd](../../evidence/parameters-sets-005.md#p-4087e195c55a7fdd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006539

```text
(exec)# show ip ospf virtual-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 5 `；EOL ` RVA 0x34876DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006377

```text
(exec)# show ip pim autorp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 46 `；EOL ` RVA 0x34753198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024286

```text
(exec)# show ip pim bfd neighbor <interface> inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9C0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eb407461248fb9c5](../../evidence/conditions-sets-091.md#c-eb407461248fb9c5) · [缺口 G-3b711376ed9c33c3](../../evidence/gaps-sets-003.md#g-3b711376ed9c33c3) · [参数 P-f19137e773a21890](../../evidence/parameters-sets-018.md#p-f19137e773a21890) · [状态效果 S-7d1c8893f6dcece4](../../evidence/state_effects-sets-027.md#s-7d1c8893f6dcece4)

### path-011352

```text
(exec)# show ip pim bfd neighbor inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9C0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-60c9173e4021057e](../../evidence/conditions-sets-038.md#c-60c9173e4021057e) · [状态效果 S-7d1c8893f6dcece4](../../evidence/state_effects-sets-027.md#s-7d1c8893f6dcece4)

### path-024852

```text
(exec)# show ip pim boundary <interface> <address> <address> in <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 60 `；EOL ` RVA 0x34755E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` src address；` address ` grp address。

[条件 C-16fa597b50b4e3f0](../../evidence/conditions-sets-009.md#c-16fa597b50b4e3f0) · [缺口 G-e12737a4ff7112ee](../../evidence/gaps-sets-008.md#g-e12737a4ff7112ee) · [参数 P-1424b188ff35c0d2](../../evidence/parameters-sets-002.md#p-1424b188ff35c0d2) · [状态效果 S-a9a356ff05e4339a](../../evidence/state_effects-sets-036.md#s-a9a356ff05e4339a)

### path-006407

```text
(exec)# show ip pim bsr-router <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 20 `；EOL ` RVA 0x34753440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009592

```text
(exec)# show ip pim drlb gdr-candidates <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 79 `；EOL ` RVA 0x34754128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c52a521fba4dbc3](../../evidence/conditions-sets-048.md#c-7c52a521fba4dbc3) · [状态效果 S-2a9e5c59bcea3318](../../evidence/state_effects-sets-010.md#s-2a9e5c59bcea3318)

### path-022358

```text
(exec)# show ip pim drlb gdr-candidates <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 79 `；EOL ` RVA 0x34754128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-642ec2034020c5ac](../../evidence/conditions-sets-039.md#c-642ec2034020c5ac) · [缺口 G-3e32c0ce1ee57818](../../evidence/gaps-sets-003.md#g-3e32c0ce1ee57818) · [参数 P-564edbb49c380db8](../../evidence/parameters-sets-007.md#p-564edbb49c380db8) · [状态效果 S-2a9e5c59bcea3318](../../evidence/state_effects-sets-010.md#s-2a9e5c59bcea3318)

### path-006641

```text
(exec)# show ip pim gir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 87 `；EOL ` RVA 0x34756200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce96bb5284c01d1b](../../evidence/conditions-sets-080.md#c-ce96bb5284c01d1b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006760

```text
(exec)# show ip pim interface <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 12 `；EOL ` RVA 0x347558F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4ee1b9708d8d1a4](../../evidence/conditions-sets-064.md#c-a4ee1b9708d8d1a4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019312

```text
(exec)# show ip pim interface <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 12 `；EOL ` RVA 0x347558F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f3e72f51b6119ec9](../../evidence/conditions-sets-094.md#c-f3e72f51b6119ec9) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022593

```text
(exec)# show ip pim interface <interface> bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9C488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e54e3d4f4f939cba](../../evidence/conditions-sets-088.md#c-e54e3d4f4f939cba) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-f466552f04688273](../../evidence/state_effects-sets-052.md#s-f466552f04688273)

### path-022445

```text
(exec)# show ip pim interface <interface> detail <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 39 `；EOL ` RVA 0x34755648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f3e72f51b6119ec9](../../evidence/conditions-sets-094.md#c-f3e72f51b6119ec9) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022415

```text
(exec)# show ip pim interface <interface> traffic <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 96 `；EOL ` RVA 0x347553A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f3e72f51b6119ec9](../../evidence/conditions-sets-094.md#c-f3e72f51b6119ec9) · [缺口 G-351f84834239c90a](../../evidence/gaps-sets-002.md#g-351f84834239c90a) · [参数 P-463e276a391bd8c0](../../evidence/parameters-sets-006.md#p-463e276a391bd8c0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009801

```text
(exec)# show ip pim interface bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9C488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d6feea30e8dc65a](../../evidence/conditions-sets-011.md#c-1d6feea30e8dc65a) · [状态效果 S-f466552f04688273](../../evidence/state_effects-sets-052.md#s-f466552f04688273)

### path-009675

```text
(exec)# show ip pim interface detail <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 39 `；EOL ` RVA 0x34755648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4ee1b9708d8d1a4](../../evidence/conditions-sets-064.md#c-a4ee1b9708d8d1a4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009652

```text
(exec)# show ip pim interface traffic <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 96 `；EOL ` RVA 0x347553A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4ee1b9708d8d1a4](../../evidence/conditions-sets-064.md#c-a4ee1b9708d8d1a4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006839

```text
(exec)# show ip pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478DCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-009843

```text
(exec)# show ip pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x3478BB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011373

```text
(exec)# show ip pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x3478B838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e6a5239a8b5178ac](../../evidence/conditions-sets-089.md#c-e6a5239a8b5178ac) · [状态效果 S-c1cee01a3266053c](../../evidence/state_effects-sets-041.md#s-c1cee01a3266053c)

### path-011873

```text
(exec)# show ip pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x3478B440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [参数 P-e84d14ee7ea2ba12](../../evidence/parameters-sets-017.md#p-e84d14ee7ea2ba12) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011377

```text
(exec)# show ip pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x3478C440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-569f850f86fa2022](../../evidence/conditions-sets-034.md#c-569f850f86fa2022) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011387

```text
(exec)# show ip pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x3478CEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58ee3c52929f8ea3](../../evidence/conditions-sets-035.md#c-58ee3c52929f8ea3) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011372

```text
(exec)# show ip pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x3478C198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ec3d6e0a578a4fe](../../evidence/conditions-sets-049.md#c-7ec3d6e0a578a4fe) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011379

```text
(exec)# show ip pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x3478C6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7dc1a8cf35506de](../../evidence/conditions-sets-096.md#c-f7dc1a8cf35506de) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011381

```text
(exec)# show ip pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x3478C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b11f70c10deefc58](../../evidence/conditions-sets-068.md#c-b11f70c10deefc58) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011384

```text
(exec)# show ip pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x3478CC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9453f6b2fcd7239c](../../evidence/conditions-sets-057.md#c-9453f6b2fcd7239c) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011406

```text
(exec)# show ip pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x3478D498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3ca488222807f62](../../evidence/conditions-sets-088.md#c-e3ca488222807f62) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011880

```text
(exec)# show ip pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478D740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-345401d56829090e](../../evidence/conditions-sets-020.md#c-345401d56829090e) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011394

```text
(exec)# show ip pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x3478D188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-40847ec47738af2d](../../evidence/conditions-sets-025.md#c-40847ec47738af2d) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011404

```text
(exec)# show ip pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478D9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0b68bae7bdef907](../../evidence/conditions-sets-086.md#c-e0b68bae7bdef907) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011365

```text
(exec)# show ip pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x3478BEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cea9280e3f95214b](../../evidence/conditions-sets-080.md#c-cea9280e3f95214b) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-009786

```text
(exec)# show ip pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x3478AEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-011353

```text
(exec)# show ip pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x3478AEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-009758

```text
(exec)# show ip pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x3478AB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cebace0dbd709755](../../evidence/conditions-sets-080.md#c-cebace0dbd709755) · [状态效果 S-3dc7c5024f0010af](../../evidence/state_effects-sets-014.md#s-3dc7c5024f0010af)

### path-006630

```text
(exec)# show ip pim mvpn <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 52 `；EOL ` RVA 0x34752B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009610

```text
(exec)# show ip pim mvpn bier <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 89 `；EOL ` RVA 0x34752840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009490

```text
(exec)# show ip pim mvpn crt <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 70 `；EOL ` RVA 0x34751850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009590

```text
(exec)# show ip pim mvpn gre <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 90 `；EOL ` RVA 0x34752598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009574

```text
(exec)# show ip pim mvpn ir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 91 `；EOL ` RVA 0x347522F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009535

```text
(exec)# show ip pim mvpn leaf-ad <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 92 `；EOL ` RVA 0x34751DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009443

```text
(exec)# show ip pim mvpn mldp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 68 `；EOL ` RVA 0x34751300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009466

```text
(exec)# show ip pim mvpn pe <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 69 `；EOL ` RVA 0x347515A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009511

```text
(exec)# show ip pim mvpn replication <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 93 `；EOL ` RVA 0x34751AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009556

```text
(exec)# show ip pim mvpn srv6 <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 97 `；EOL ` RVA 0x34752048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009632

```text
(exec)# show ip pim mvpn tdb <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 94 `；EOL ` RVA 0x34752AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009420

```text
(exec)# show ip pim mvpn vxlan <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 95 `；EOL ` RVA 0x34751058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006462

```text
(exec)# show ip pim neighbor <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 10 `；EOL ` RVA 0x347710F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-837c4cd2b0205972](../../evidence/conditions-sets-051.md#c-837c4cd2b0205972) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018953

```text
(exec)# show ip pim neighbor <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 10 `；EOL ` RVA 0x347710F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-67910b2191a66944](../../evidence/conditions-sets-040.md#c-67910b2191a66944) · [缺口 G-5bde90dd26461a6c](../../evidence/gaps-sets-004.md#g-5bde90dd26461a6c) · [参数 P-78ff02a4e0cf0889](../../evidence/parameters-sets-009.md#p-78ff02a4e0cf0889) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009528

```text
(exec)# show ip pim pfp-sa announcements <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 83 `；EOL ` RVA 0x34753790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4beb10443808ceb9](../../evidence/conditions-sets-030.md#c-4beb10443808ceb9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009572

```text
(exec)# show ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 86 `；EOL ` RVA 0x34753CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4beb10443808ceb9](../../evidence/conditions-sets-030.md#c-4beb10443808ceb9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009552

```text
(exec)# show ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 84 `；EOL ` RVA 0x34753A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4beb10443808ceb9](../../evidence/conditions-sets-030.md#c-4beb10443808ceb9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006627

```text
(exec)# show ip pim rp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 11 `；EOL ` RVA 0x34754BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61b5669da132f85e](../../evidence/conditions-sets-038.md#c-61b5669da132f85e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009581

```text
(exec)# show ip pim rp-hash <address> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 22 `；EOL ` RVA 0x34754FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` group address。

[条件 C-4c782013125a0eb7](../../evidence/conditions-sets-030.md#c-4c782013125a0eb7) · [参数 P-c66d3e1e0ed7b695](../../evidence/parameters-sets-015.md#p-c66d3e1e0ed7b695) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006625

```text
(exec)# show ip pim tunnel <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 55 `；EOL ` RVA 0x347547A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66e49a4e60daab77](../../evidence/conditions-sets-040.md#c-66e49a4e60daab77) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019158

```text
(exec)# show ip pim tunnel <interface> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 55 `；EOL ` RVA 0x347547A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e026bbb28e0154c](../../evidence/conditions-sets-061.md#c-9e026bbb28e0154c) · [缺口 G-684fdf37951a3f07](../../evidence/gaps-sets-004.md#g-684fdf37951a3f07) · [参数 P-a42cd1aca99fb473](../../evidence/parameters-sets-013.md#p-a42cd1aca99fb473) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002503

```text
(exec)# show ip policy <cr>
```

Handler ` RVA 0xFAD9620 `；selector ` 0 `；EOL ` RVA 0x34804A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006543

```text
(exec)# show ip policy adj-subblock <cr>
```

Handler ` RVA 0xFAD9440 `；selector ` 0 `；EOL ` RVA 0x34804A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002200

```text
(exec)# show ip policy-list <cr>
```

Handler ` RVA 0xE218540 `；selector ` 0 `；EOL ` RVA 0x344BABE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011830

```text
(exec)# show ip portbundle ip <address> bundle <number:1..65535> <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 0 `；EOL ` RVA 0x356A5148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Portbundle IP address；` unsigned_number ` Portbundle bundle number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-81af61e5ba4224a6](../../evidence/parameters-sets-010.md#p-81af61e5ba4224a6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005922

```text
(exec)# show ip portbundle status <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 1 `；EOL ` RVA 0x356A4DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009208

```text
(exec)# show ip portbundle status free <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 2 `；EOL ` RVA 0x356A4B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-494ccd6919bccd9e](../../evidence/state_effects-sets-016.md#s-494ccd6919bccd9e)

### path-005987

```text
(exec)# show ip ports all <cr>
```

Handler ` RVA 0xCE51730 `；selector ` 0 `；EOL ` RVA 0x33CF6FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005961

```text
(exec)# show ip ports ephemeral-max <cr>
```

Handler ` RVA 0xCDEFA80 `；selector ` 0 `；EOL ` RVA 0x33CF6D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006014

```text
(exec)# show ip ports reservation <cr>
```

Handler ` RVA 0xCE518D0 `；selector ` 0 `；EOL ` RVA 0x33CF7250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c005c5fcde583d9f](../../evidence/conditions-sets-074.md#c-c005c5fcde583d9f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002675

```text
(exec)# show ip prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x342832B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88a2248132632179](../../evidence/conditions-sets-053.md#c-88a2248132632179) · [状态效果 S-143379868d088606](../../evidence/state_effects-sets-005.md#s-143379868d088606)

### path-019430

```text
(exec)# show ip prefix-list <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 4 `；EOL ` RVA 0x34283688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 10.0.0.0/8。

[条件 C-d21ede582614ea22](../../evidence/conditions-sets-081.md#c-d21ede582614ea22) · [缺口 G-2196acf0a1478dd3](../../evidence/gaps-sets-002.md#g-2196acf0a1478dd3) · [参数 P-89e89425649c4718](../../evidence/parameters-sets-011.md#p-89e89425649c4718) · [状态效果 S-143379868d088606](../../evidence/state_effects-sets-005.md#s-143379868d088606)

### path-011371

```text
(exec)# show ip prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x34283358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-88a2248132632179](../../evidence/conditions-sets-053.md#c-88a2248132632179) · [参数 P-0d71bd8044f6fc2b](../../evidence/parameters-sets-001.md#p-0d71bd8044f6fc2b) · [状态效果 S-143379868d088606](../../evidence/state_effects-sets-005.md#s-143379868d088606)

### path-006813

```text
(exec)# show ip prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x34282FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-143379868d088606](../../evidence/state_effects-sets-005.md#s-143379868d088606)

### path-006802

```text
(exec)# show ip prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x34282CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-143379868d088606](../../evidence/state_effects-sets-005.md#s-143379868d088606)

### path-002216

```text
(exec)# show ip protocols <cr>
```

Handler ` RVA 0xE1F60E0 `；selector ` 0 `；EOL ` RVA 0x3422FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44f485a1fcd2161c](../../evidence/conditions-sets-027.md#c-44f485a1fcd2161c) · [状态效果 S-23b47a0474303467](../../evidence/state_effects-sets-008.md#s-23b47a0474303467)

### path-006065

```text
(exec)# show ip protocols summary <cr>
```

Handler ` RVA 0xE1F5DF0 `；selector ` 0 `；EOL ` RVA 0x3422FA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44f485a1fcd2161c](../../evidence/conditions-sets-027.md#c-44f485a1fcd2161c) · [状态效果 S-23b47a0474303467](../../evidence/state_effects-sets-008.md#s-23b47a0474303467)

### path-015010

```text
(exec)# show ip reassembly <interface> <cr>
```

Handler ` RVA 0xC78EA70 `；selector ` 0 `；EOL ` RVA 0x33AECED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e510e2b1b66dd9c](../../evidence/conditions-sets-049.md#c-7e510e2b1b66dd9c) · [缺口 G-e7f0c28428edc901](../../evidence/gaps-sets-008.md#g-e7f0c28428edc901) · [参数 P-0e83b0412d60a526](../../evidence/parameters-sets-002.md#p-0e83b0412d60a526) · [状态效果 S-6021cbe4dcd1c564](../../evidence/state_effects-sets-021.md#s-6021cbe4dcd1c564)

### path-001800

```text
(exec)# show ip redirects <cr>
```

Handler ` RVA 0xCF509C0 `；selector ` 0 `；EOL ` RVA 0x33D31570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006096

```text
(exec)# show ip rib database <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 1 `；EOL ` RVA 0x3422F578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9fa81fb0d1adae9](../../evidence/conditions-sets-090.md#c-e9fa81fb0d1adae9) · [状态效果 S-848a96ba9e5b62a9](../../evidence/state_effects-sets-028.md#s-848a96ba9e5b62a9)

### path-018547

```text
(exec)# show ip rib route <?router_action_proc_vpn@555589783268> <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 2 `；EOL ` RVA 0x3422F2D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e9fa81fb0d1adae9](../../evidence/conditions-sets-090.md#c-e9fa81fb0d1adae9) · [缺口 G-95f60b11cd716043](../../evidence/gaps-sets-005.md#g-95f60b11cd716043) · [状态效果 S-848a96ba9e5b62a9](../../evidence/state_effects-sets-028.md#s-848a96ba9e5b62a9)

### path-006651

```text
(exec)# show ip rip database <cr>
```

Handler ` RVA 0xFB73AB0 `；selector ` 0 `；EOL ` RVA 0x34822820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-265b4c12aa8f3553](../../evidence/conditions-sets-015.md#c-265b4c12aa8f3553) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006637

```text
(exec)# show ip rip neighbors <cr>
```

Handler ` RVA 0xFB52AC0 `；selector ` 0 `；EOL ` RVA 0x34822B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4cf46f000210ac4](../../evidence/conditions-sets-064.md#c-a4cf46f000210ac4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006567

```text
(exec)# show ip rip timers <cr>
```

Handler ` RVA 0xFB56CB0 `；selector ` 0 `；EOL ` RVA 0x34822428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025402

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> <address> getnext <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 8 `；EOL ` RVA 0x34233BA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-f2e2f142f8200e4d](../../evidence/conditions-sets-094.md#c-f2e2f142f8200e4d) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-025403

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> <address> getprev <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 9 `；EOL ` RVA 0x34233E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-f2e2f142f8200e4d](../../evidence/conditions-sets-094.md#c-f2e2f142f8200e4d) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-025404

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> <address> longer-prefixes <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 7 `；EOL ` RVA 0x342340F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-f2e2f142f8200e4d](../../evidence/conditions-sets-094.md#c-f2e2f142f8200e4d) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-025401

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> <address> resolve <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 10 `；EOL ` RVA 0x34233900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to display information about or hostname。

[条件 C-f2e2f142f8200e4d](../../evidence/conditions-sets-094.md#c-f2e2f142f8200e4d) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [参数 P-2f6a56dcc94741bf](../../evidence/parameters-sets-004.md#p-2f6a56dcc94741bf) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-025385

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 0 `；EOL ` RVA 0x34231710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6cbedcbc3816e3b8](../../evidence/conditions-sets-042.md#c-6cbedcbc3816e3b8) · [缺口 G-7a24ab141841f0e8](../../evidence/gaps-sets-005.md#g-7a24ab141841f0e8) · [状态效果 S-b4db3e11669db65b](../../evidence/state_effects-sets-038.md#s-b4db3e11669db65b)

### path-025391

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> cidr <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 6 `；EOL ` RVA 0x34233298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cad7ac9b250b6f61](../../evidence/conditions-sets-078.md#c-cad7ac9b250b6f61) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-025392

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> dhcp <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 13 `；EOL ` RVA 0x342335A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cad7ac9b250b6f61](../../evidence/conditions-sets-078.md#c-cad7ac9b250b6f61) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-025388

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> download <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 3 `；EOL ` RVA 0x342319E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b2e076adf03265d](../../evidence/conditions-sets-023.md#c-3b2e076adf03265d) · [缺口 G-7a24ab141841f0e8](../../evidence/gaps-sets-005.md#g-7a24ab141841f0e8) · [状态效果 S-b4db3e11669db65b](../../evidence/state_effects-sets-038.md#s-b4db3e11669db65b)

### path-018768

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> loops <cr>
```

Handler ` RVA 0xDBE99E0 `；selector ` 0 `；EOL ` RVA 0x34231F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-025389

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> majornets-only <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 5 `；EOL ` RVA 0x34232D48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cad7ac9b250b6f61](../../evidence/conditions-sets-078.md#c-cad7ac9b250b6f61) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-018733

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> profile <cr>
```

Handler ` RVA 0xE1ADBE0 `；selector ` 0 `；EOL ` RVA 0x34231C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-018910

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> replicate <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 11 `；EOL ` RVA 0x342329C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-018872

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> static-table <cr>
```

Handler ` RVA 0xE2A4BF0 `；selector ` 0 `；EOL ` RVA 0x34232710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-018812

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> summary <cr>
```

Handler ` RVA 0xE1D59C0 `；selector ` 0 `；EOL ` RVA 0x342321C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-025390

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> supernets-only <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 4 `；EOL ` RVA 0x34232FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cad7ac9b250b6f61](../../evidence/conditions-sets-078.md#c-cad7ac9b250b6f61) · [缺口 G-a88c03ded52cad18](../../evidence/gaps-sets-006.md#g-a88c03ded52cad18) · [状态效果 S-d3a2e0bb0e84ced3](../../evidence/state_effects-sets-045.md#s-d3a2e0bb0e84ced3)

### path-018845

```text
(exec)# show ip route <?router_action_no_proc_vpn@5555897853d8> track-table <cr>
```

Handler ` RVA 0xD4A59D0 `；selector ` 0 `；EOL ` RVA 0x34232468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [缺口 G-03c6795a1cd09c6e](../../evidence/gaps-sets-001.md#g-03c6795a1cd09c6e) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-009332

```text
(exec)# show ip route list <number:1..199> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 12 `；EOL ` RVA 0x34230C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [参数 P-6f46a0106e78d96b](../../evidence/parameters-sets-009.md#p-6f46a0106e78d96b) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-009367

```text
(exec)# show ip route omp-tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 15 `；EOL ` RVA 0x34231420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Management Protocol (OMP) Tag value。

[条件 C-1029b62c92a1bba7](../../evidence/conditions-sets-006.md#c-1029b62c92a1bba7) · [参数 P-1586b2be9da07e52](../../evidence/parameters-sets-002.md#p-1586b2be9da07e52) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-009366

```text
(exec)# show ip route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 14 `；EOL ` RVA 0x34231000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-a81cf38b82e83ad7](../../evidence/conditions-sets-065.md#c-a81cf38b82e83ad7) · [参数 P-e0210763947c7838](../../evidence/parameters-sets-017.md#p-e0210763947c7838) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-011173

```text
(exec)# show ip route tree <address> <address> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 3 `；EOL ` RVA 0x34230700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [参数 P-3c5f288fee4ae5f4](../../evidence/parameters-sets-005.md#p-3c5f288fee4ae5f4) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-006174

```text
(exec)# show ip route tree <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 1 `；EOL ` RVA 0x342306C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-009318

```text
(exec)# show ip route tree summary <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 2 `；EOL ` RVA 0x342303F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a197f9d2cce68e9](../../evidence/conditions-sets-041.md#c-6a197f9d2cce68e9) · [状态效果 S-c741586d7675b6f3](../../evidence/state_effects-sets-042.md#s-c741586d7675b6f3)

### path-006260

```text
(exec)# show ip rpf queued <cr>
```

Handler ` RVA 0xF740240 `；selector ` 0 `；EOL ` RVA 0x34750190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3704729e48e38e9e](../../evidence/conditions-sets-021.md#c-3704729e48e38e9e) · [状态效果 S-2f44bd4b711a0e9a](../../evidence/state_effects-sets-010.md#s-2f44bd4b711a0e9a)

### path-002843

```text
(exec)# show ip rsvp <cr>
```

Handler ` RVA 0x10073190 `；selector ` 0 `；EOL ` RVA 0x34A3A428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3da5c90fec893b04](../../evidence/conditions-sets-024.md#c-3da5c90fec893b04) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009761

```text
(exec)# show ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C49F0 `；selector ` 0 `；EOL ` RVA 0x34A69C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011369

```text
(exec)# show ip rsvp aggregation ip endpoints <cr>
```

Handler ` RVA 0x101C42E0 `；selector ` 0 `；EOL ` RVA 0x34A69F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011356

```text
(exec)# show ip rsvp aggregation ip interface <cr>
```

Handler ` RVA 0x101C4050 `；selector ` 0 `；EOL ` RVA 0x34A69970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19aa28bcb7fef7cd](../../evidence/conditions-sets-010.md#c-19aa28bcb7fef7cd) · [状态效果 S-347ad4479a62767c](../../evidence/state_effects-sets-012.md#s-347ad4479a62767c)

### path-024285

```text
(exec)# show ip rsvp aggregation ip interface <interface> <cr>
```

Handler ` RVA 0x101C4050 `；selector ` 0 `；EOL ` RVA 0x34A69970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-75805e17968cb4c3](../../evidence/conditions-sets-046.md#c-75805e17968cb4c3) · [缺口 G-671688814f471f27](../../evidence/gaps-sets-004.md#g-671688814f471f27) · [参数 P-473b7f2b6b9040ec](../../evidence/parameters-sets-006.md#p-473b7f2b6b9040ec) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011339

```text
(exec)# show ip rsvp aggregation ip map <cr>
```

Handler ` RVA 0x101C3C20 `；selector ` 0 `；EOL ` RVA 0x34A691B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011344

```text
(exec)# show ip rsvp aggregation ip reservation <cr>
```

Handler ` RVA 0x101C3DE0 `；selector ` 0 `；EOL ` RVA 0x34A694F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006913

```text
(exec)# show ip rsvp atm-peak-rate-limit <cr>
```

Handler ` RVA 0x100542A0 `；selector ` 0 `；EOL ` RVA 0x34A34388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-467a0f7f31acbbdb](../../evidence/conditions-sets-028.md#c-467a0f7f31acbbdb) · [状态效果 S-5bfb3e162565a65c](../../evidence/state_effects-sets-020.md#s-5bfb3e162565a65c)

### path-019471

```text
(exec)# show ip rsvp atm-peak-rate-limit <interface> <cr>
```

Handler ` RVA 0x100542A0 `；selector ` 0 `；EOL ` RVA 0x34A34388 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab10da391cc6a41c](../../evidence/conditions-sets-066.md#c-ab10da391cc6a41c) · [缺口 G-46cd77eaafbe8a37](../../evidence/gaps-sets-003.md#g-46cd77eaafbe8a37) · [参数 P-bd7fb8c43148e967](../../evidence/parameters-sets-014.md#p-bd7fb8c43148e967) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006734

```text
(exec)# show ip rsvp authentication <cr>
```

Handler ` RVA 0x10073FB0 `；selector ` 0 `；EOL ` RVA 0x34A2FFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006976

```text
(exec)# show ip rsvp counters <cr>
```

Handler ` RVA 0x100B61F0 `；selector ` 0 `；EOL ` RVA 0x34A35FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [状态效果 S-48756a84414a8391](../../evidence/state_effects-sets-016.md#s-48756a84414a8391)

### path-006883

```text
(exec)# show ip rsvp handles <cr>
```

Handler ` RVA 0x10070450 `；selector ` 0 `；EOL ` RVA 0x34A34000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c38057bdf21f780](../../evidence/conditions-sets-030.md#c-4c38057bdf21f780) · [状态效果 S-1c44d546c05af888](../../evidence/state_effects-sets-006.md#s-1c44d546c05af888)

### path-007003

```text
(exec)# show ip rsvp hello <cr>
```

Handler ` RVA 0x10072260 `；selector ` 0 `；EOL ` RVA 0x34A38728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e2f8ef65d50037b1](../../evidence/conditions-sets-087.md#c-e2f8ef65d50037b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011437

```text
(exec)# show ip rsvp hello bfd nbr <cr>
```

Handler ` RVA 0x10076740 `；selector ` 0 `；EOL ` RVA 0x34A37650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7df6317d844a4a33](../../evidence/conditions-sets-049.md#c-7df6317d844a4a33) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011892

```text
(exec)# show ip rsvp hello bfd nbr detail <cr>
```

Handler ` RVA 0x10076940 `；selector ` 0 `；EOL ` RVA 0x34A37348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7df6317d844a4a33](../../evidence/conditions-sets-049.md#c-7df6317d844a4a33) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011895

```text
(exec)# show ip rsvp hello client lsp detail <cr>
```

Handler ` RVA 0x10076EA0 `；selector ` 0 `；EOL ` RVA 0x34A38108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011894

```text
(exec)# show ip rsvp hello client lsp summary <cr>
```

Handler ` RVA 0x10076D20 `；selector ` 0 `；EOL ` RVA 0x34A38410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011440

```text
(exec)# show ip rsvp hello client nbr <cr>
```

Handler ` RVA 0x10076A40 `；selector ` 0 `；EOL ` RVA 0x34A37DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011893

```text
(exec)# show ip rsvp hello client nbr detail <cr>
```

Handler ` RVA 0x10076C10 `；selector ` 0 `；EOL ` RVA 0x34A37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74faadc013aa600c](../../evidence/conditions-sets-045.md#c-74faadc013aa600c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009938

```text
(exec)# show ip rsvp hello graceful-restart <cr>
```

Handler ` RVA 0x10073050 `；selector ` 0 `；EOL ` RVA 0x34A38700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef5ed1a666ba4748](../../evidence/conditions-sets-092.md#c-ef5ed1a666ba4748) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011425

```text
(exec)# show ip rsvp hello instance internal <cr>
```

Handler ` RVA 0x10076620 `；selector ` 0 `；EOL ` RVA 0x34A368E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-692987fefc2d91e8](../../evidence/conditions-sets-041.md#c-692987fefc2d91e8) · [状态效果 S-866e184185c15e19](../../evidence/state_effects-sets-029.md#s-866e184185c15e19)

### path-011428

```text
(exec)# show ip rsvp hello instance summary <cr>
```

Handler ` RVA 0x10076290 `；selector ` 0 `；EOL ` RVA 0x34A36C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-692987fefc2d91e8](../../evidence/conditions-sets-041.md#c-692987fefc2d91e8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009910

```text
(exec)# show ip rsvp hello statistics <cr>
```

Handler ` RVA 0x100761D0 `；selector ` 0 `；EOL ` RVA 0x34A36F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76d6906fdad99132](../../evidence/conditions-sets-046.md#c-76d6906fdad99132) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009915

```text
(exec)# show ip rsvp host receivers <cr>
```

Handler ` RVA 0x1006D010 `；selector ` 0 `；EOL ` RVA 0x34A35B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [状态效果 S-531107af0d7c08d8](../../evidence/state_effects-sets-018.md#s-531107af0d7c08d8)

### path-009904

```text
(exec)# show ip rsvp host senders <cr>
```

Handler ` RVA 0x1006D750 `；selector ` 0 `；EOL ` RVA 0x34A358A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [状态效果 S-74a8dfed59f610b4](../../evidence/state_effects-sets-025.md#s-74a8dfed59f610b4)

### path-006906

```text
(exec)# show ip rsvp installed <cr>
```

Handler ` RVA 0x1006B120 `；selector ` 0 `；EOL ` RVA 0x34A33858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad975350c846c2db](../../evidence/conditions-sets-067.md#c-ad975350c846c2db) · [状态效果 S-75c419c1298053d8](../../evidence/state_effects-sets-025.md#s-75c419c1298053d8)

### path-019460

```text
(exec)# show ip rsvp installed <interface> <cr>
```

Handler ` RVA 0x1006B120 `；selector ` 0 `；EOL ` RVA 0x34A33858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6f5e0c5d88b99a69](../../evidence/conditions-sets-043.md#c-6f5e0c5d88b99a69) · [缺口 G-b48897c36abff7d8](../../evidence/gaps-sets-006.md#g-b48897c36abff7d8) · [参数 P-09a4bace1c71e068](../../evidence/parameters-sets-001.md#p-09a4bace1c71e068) · [状态效果 S-6c5ba43a4d4775ae](../../evidence/state_effects-sets-023.md#s-6c5ba43a4d4775ae)

### path-006887

```text
(exec)# show ip rsvp interface <cr>
```

Handler ` RVA 0x1006B3E0 `；selector ` 0 `；EOL ` RVA 0x34A33020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f103c8fc8ddea53](../../evidence/conditions-sets-006.md#c-0f103c8fc8ddea53) · [状态效果 S-d0891f12c9bdd4cc](../../evidence/state_effects-sets-044.md#s-d0891f12c9bdd4cc)

### path-019461

```text
(exec)# show ip rsvp interface <interface> <cr>
```

Handler ` RVA 0x1006B3E0 `；selector ` 0 `；EOL ` RVA 0x34A33020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-547a24757922e9c9](../../evidence/conditions-sets-033.md#c-547a24757922e9c9) · [缺口 G-25245a7ad1610a00](../../evidence/gaps-sets-002.md#g-25245a7ad1610a00) · [参数 P-454cfd4a7bebbc08](../../evidence/parameters-sets-006.md#p-454cfd4a7bebbc08) · [状态效果 S-f2270b26de429cb4](../../evidence/state_effects-sets-051.md#s-f2270b26de429cb4)

### path-009916

```text
(exec)# show ip rsvp listeners <address> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 6 `；EOL ` RVA 0x34A35008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [参数 P-559a5e35800d3230](../../evidence/parameters-sets-007.md#p-559a5e35800d3230) · [状态效果 S-de956d77c4fb4b50](../../evidence/state_effects-sets-047.md#s-de956d77c4fb4b50)

### path-011420

```text
(exec)# show ip rsvp listeners <address> <number:0..255> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 4 `；EOL ` RVA 0x34A34CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [参数 P-c1d702e7762de23b](../../evidence/parameters-sets-015.md#p-c1d702e7762de23b) · [状态效果 S-de956d77c4fb4b50](../../evidence/state_effects-sets-047.md#s-de956d77c4fb4b50)

### path-011881

```text
(exec)# show ip rsvp listeners <address> <number:0..255> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 0 `；EOL ` RVA 0x34A34A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [参数 P-eeed49378aa0252c](../../evidence/parameters-sets-018.md#p-eeed49378aa0252c) · [状态效果 S-de956d77c4fb4b50](../../evidence/state_effects-sets-047.md#s-de956d77c4fb4b50)

### path-006940

```text
(exec)# show ip rsvp listeners <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 7 `；EOL ` RVA 0x34A352C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d421029802e57df](../../evidence/conditions-sets-024.md#c-3d421029802e57df) · [状态效果 S-de956d77c4fb4b50](../../evidence/state_effects-sets-047.md#s-de956d77c4fb4b50)

### path-006828

```text
(exec)# show ip rsvp metadata <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A32250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [状态效果 S-479e32249d9834b1](../../evidence/state_effects-sets-016.md#s-479e32249d9834b1)

### path-006807

```text
(exec)# show ip rsvp neighbor <cr>
```

Handler ` RVA 0x1006DCE0 `；selector ` 0 `；EOL ` RVA 0x34A309B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [状态效果 S-672b4219abdfc209](../../evidence/state_effects-sets-022.md#s-672b4219abdfc209)

### path-009785

```text
(exec)# show ip rsvp neighbor queues <cr>
```

Handler ` RVA 0x1006DB00 `；selector ` 0 `；EOL ` RVA 0x34A30C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d435423850cf954c](../../evidence/conditions-sets-082.md#c-d435423850cf954c) · [状态效果 S-672b4219abdfc209](../../evidence/state_effects-sets-022.md#s-672b4219abdfc209)

### path-009688

```text
(exec)# show ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100723C0 `；selector ` 0 `；EOL ` RVA 0x34A2FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-494c6a7983e46592](../../evidence/conditions-sets-029.md#c-494c6a7983e46592) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009908

```text
(exec)# show ip rsvp p2mp counters <cr>
```

Handler ` RVA 0x101A72E0 `；selector ` 0 `；EOL ` RVA 0x34A3A468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7604b9b3a99a26db](../../evidence/conditions-sets-046.md#c-7604b9b3a99a26db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006715

```text
(exec)# show ip rsvp policy <cr>
```

Handler ` RVA 0x10113110 `；selector ` 0 `；EOL ` RVA 0x34A40A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c293d3779bede94](../../evidence/conditions-sets-048.md#c-7c293d3779bede94) · [状态效果 S-e64319c64501dd19](../../evidence/state_effects-sets-049.md#s-e64319c64501dd19)

### path-009747

```text
(exec)# show ip rsvp policy cops <cr>
```

Handler ` RVA 0x10113110 `；selector ` 8 `；EOL ` RVA 0x34A40AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5327ead3e239c79d](../../evidence/conditions-sets-033.md#c-5327ead3e239c79d) · [状态效果 S-e64319c64501dd19](../../evidence/state_effects-sets-049.md#s-e64319c64501dd19)

### path-009700

```text
(exec)# show ip rsvp policy identity <cr>
```

Handler ` RVA 0x10112D90 `；selector ` 0 `；EOL ` RVA 0x34A40020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-e64319c64501dd19](../../evidence/state_effects-sets-049.md#s-e64319c64501dd19)

### path-009836

```text
(exec)# show ip rsvp policy local <cr>
```

Handler ` RVA 0x10113110 `；selector ` 1 `；EOL ` RVA 0x34A40490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-51577c374a7c4e5c](../../evidence/conditions-sets-032.md#c-51577c374a7c4e5c) · [状态效果 S-d7c2a0215756558f](../../evidence/state_effects-sets-046.md#s-d7c2a0215756558f)

### path-022633

```text
(exec)# show ip rsvp policy local <interface> <cr>
```

Handler ` RVA 0x10113110 `；selector ` 1 `；EOL ` RVA 0x34A40490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9cfe8061cf8539c1](../../evidence/conditions-sets-061.md#c-9cfe8061cf8539c1) · [缺口 G-e0769badd0fd20ea](../../evidence/gaps-sets-008.md#g-e0769badd0fd20ea) · [参数 P-0536a22aeae684e2](../../evidence/parameters-sets-001.md#p-0536a22aeae684e2) · [状态效果 S-d7c2a0215756558f](../../evidence/state_effects-sets-046.md#s-d7c2a0215756558f)

### path-006885

```text
(exec)# show ip rsvp precedence <cr>
```

Handler ` RVA 0x10054510 `；selector ` 0 `；EOL ` RVA 0x34A33C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-681e33341befcb82](../../evidence/conditions-sets-040.md#c-681e33341befcb82) · [状态效果 S-aba20e85a50dd835](../../evidence/state_effects-sets-036.md#s-aba20e85a50dd835)

### path-019431

```text
(exec)# show ip rsvp precedence <interface> <cr>
```

Handler ` RVA 0x10054510 `；selector ` 0 `；EOL ` RVA 0x34A33C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-084c2c572b6ca4f7](../../evidence/conditions-sets-004.md#c-084c2c572b6ca4f7) · [缺口 G-2b3145c2709f6e6e](../../evidence/gaps-sets-002.md#g-2b3145c2709f6e6e) · [参数 P-9d56f06581e454ae](../../evidence/parameters-sets-012.md#p-9d56f06581e454ae) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006772

```text
(exec)# show ip rsvp sbm <cr>
```

Handler ` RVA 0x1006E490 `；selector ` 0 `；EOL ` RVA 0x34A303A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c48cdebf9fa1305](../../evidence/conditions-sets-023.md#c-3c48cdebf9fa1305) · [状态效果 S-43f950155cf076a4](../../evidence/state_effects-sets-015.md#s-43f950155cf076a4)

### path-019285

```text
(exec)# show ip rsvp sbm <interface> <cr>
```

Handler ` RVA 0x1006E490 `；selector ` 0 `；EOL ` RVA 0x34A303A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be004c6a6200f04b](../../evidence/conditions-sets-073.md#c-be004c6a6200f04b) · [缺口 G-6567d1442ce4917d](../../evidence/gaps-sets-004.md#g-6567d1442ce4917d) · [参数 P-4ee747faa40a2997](../../evidence/parameters-sets-006.md#p-4ee747faa40a2997) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006831

```text
(exec)# show ip rsvp sender <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A315A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [状态效果 S-befa65d92cd8e2e6](../../evidence/state_effects-sets-040.md#s-befa65d92cd8e2e6)

### path-009963

```text
(exec)# show ip rsvp signalling blockade <cr>
```

Handler ` RVA 0x10067C20 `；selector ` 0 `；EOL ` RVA 0x34A3A0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be699b557581bc06](../../evidence/conditions-sets-073.md#c-be699b557581bc06) · [状态效果 S-fc96c8de58727379](../../evidence/state_effects-sets-053.md#s-fc96c8de58727379)

### path-009902

```text
(exec)# show ip rsvp signalling fast-local-repair <cr>
```

Handler ` RVA 0x100713E0 `；selector ` 0 `；EOL ` RVA 0x34A38D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009899

```text
(exec)# show ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x100712D0 `；selector ` 0 `；EOL ` RVA 0x34A38FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011432

```text
(exec)# show ip rsvp signalling refresh interval <cr>
```

Handler ` RVA 0x10071130 `；selector ` 0 `；EOL ` RVA 0x34A39858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011435

```text
(exec)# show ip rsvp signalling refresh misses <cr>
```

Handler ` RVA 0x100711A0 `；selector ` 0 `；EOL ` RVA 0x34A39B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011427

```text
(exec)# show ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071210 `；selector ` 0 `；EOL ` RVA 0x34A395B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009911

```text
(exec)# show ip rsvp signalling session-timers <cr>
```

Handler ` RVA 0x10072130 `；selector ` 0 `；EOL ` RVA 0x34A392A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31bbd11c2e970ff0](../../evidence/conditions-sets-019.md#c-31bbd11c2e970ff0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009768

```text
(exec)# show ip rsvp transport clients <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A31E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c3c055753ffd7df](../../evidence/conditions-sets-017.md#c-2c3c055753ffd7df) · [状态效果 S-9541c6d06e4dac3a](../../evidence/state_effects-sets-032.md#s-9541c6d06e4dac3a)

### path-005798

```text
(exec)# show ip rtp header-compression <cr>
```

Handler ` RVA 0xD194110 `；selector ` 0 `；EOL ` RVA 0x33DAABA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7513642931f3ef25](../../evidence/conditions-sets-045.md#c-7513642931f3ef25) · [状态效果 S-a8da9e5c5b7ea87b](../../evidence/state_effects-sets-036.md#s-a8da9e5c5b7ea87b)

### path-009467

```text
(exec)# show ip sctp association list <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 2 `；EOL ` RVA 0x33D0DFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011233

```text
(exec)# show ip sctp association parameters <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 3 `；EOL ` RVA 0x33D0DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-d2fce9ec1de3fa16](../../evidence/parameters-sets-016.md#p-d2fce9ec1de3fa16) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011222

```text
(exec)# show ip sctp association statistics <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 4 `；EOL ` RVA 0x33D0DA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-39686869c9f42ad0](../../evidence/parameters-sets-005.md#p-39686869c9f42ad0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006280

```text
(exec)# show ip sctp errors <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 6 `；EOL ` RVA 0x33D0D6F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006339

```text
(exec)# show ip sctp instances <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 1 `；EOL ` RVA 0x33D0E288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006238

```text
(exec)# show ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 5 `；EOL ` RVA 0x33D0D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002310

```text
(exec)# show ip sdr <cr>
```

Handler ` RVA 0xF87E5A0 `；selector ` 0 `；EOL ` RVA 0x3474E828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-172ce32b53a9055e](../../evidence/conditions-sets-009.md#c-172ce32b53a9055e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006985

```text
(exec)# show ip sla application <cr>
```

Handler ` RVA 0x102DD0E0 `；selector ` 0 `；EOL ` RVA 0x34A99F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006843

```text
(exec)# show ip sla authentication <cr>
```

Handler ` RVA 0x101DA830 `；selector ` 0 `；EOL ` RVA 0x34A6E750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009894

```text
(exec)# show ip sla auto discovery <cr>
```

Handler ` RVA 0x10241B90 `；selector ` 0 `；EOL ` RVA 0x34A7ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009892

```text
(exec)# show ip sla auto group <cr>
```

Handler ` RVA 0x10240F70 `；selector ` 0 `；EOL ` RVA 0x34A7A360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2f57912147037d69](../../evidence/state_effects-sets-010.md#s-2f57912147037d69)

### path-009890

```text
(exec)# show ip sla auto schedule <cr>
```

Handler ` RVA 0x10241510 `；selector ` 0 `；EOL ` RVA 0x34A7A6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012138

```text
(exec)# show ip sla auto summary-statistics group type ip <string> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 2 `；EOL ` RVA 0x34A7B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-d6d0e6165020b7f4](../../evidence/state_effects-sets-046.md#s-d6d0e6165020b7f4)

### path-012199

```text
(exec)# show ip sla auto summary-statistics group type ip <string> ip-address <address> port <number:0..64000> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 3 `；EOL ` RVA 0x34A7B2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name；` address ` destination ip address；` unsigned_number ` destination port。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-8528621cf3b47973](../../evidence/parameters-sets-010.md#p-8528621cf3b47973) · [状态效果 S-d6d0e6165020b7f4](../../evidence/state_effects-sets-046.md#s-d6d0e6165020b7f4)

### path-012173

```text
(exec)# show ip sla auto summary-statistics group type ip <string> ip-address <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 1 `；EOL ` RVA 0x34A7B248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-d6d0e6165020b7f4](../../evidence/state_effects-sets-046.md#s-d6d0e6165020b7f4)

### path-009903

```text
(exec)# show ip sla auto template <cr>
```

Handler ` RVA 0x102415E0 `；selector ` 0 `；EOL ` RVA 0x34A7AAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-a46f0a7f6101243f](../../evidence/state_effects-sets-035.md#s-a46f0a7f6101243f)

### path-006937

```text
(exec)# show ip sla collection-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 0 `；EOL ` RVA 0x34A97478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006860

```text
(exec)# show ip sla configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 14 `；EOL ` RVA 0x34A95AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006989

```text
(exec)# show ip sla distribution-statistics <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009909

```text
(exec)# show ip sla distribution-statistics full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 1 `；EOL ` RVA 0x34A97A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009898

```text
(exec)# show ip sla distribution-statistics raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 3 `；EOL ` RVA 0x34A977B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009922

```text
(exec)# show ip sla distribution-statistics tabular <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007050

```text
(exec)# show ip sla endpoint-list <cr>
```

Handler ` RVA 0x10241300 `；selector ` 0 `；EOL ` RVA 0x34A9A980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-05a7aec2970dd70e](../../evidence/state_effects-sets-002.md#s-05a7aec2970dd70e)

### path-009914

```text
(exec)# show ip sla enhanced-history distribution-statistics <cr>
```

Handler ` RVA 0x102DD570 `；selector ` 0 `；EOL ` RVA 0x34A98318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-5376ef44472f0d80](../../evidence/state_effects-sets-018.md#s-5376ef44472f0d80)

### path-009896

```text
(exec)# show ip sla ethernet-monitor configuration <cr>
```

Handler ` RVA 0x103C1120 `；selector ` 0 `；EOL ` RVA 0x34B09AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009877

```text
(exec)# show ip sla ethernet-monitor responder <cr>
```

Handler ` RVA 0x103C1230 `；selector ` 0 `；EOL ` RVA 0x34B09800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006872

```text
(exec)# show ip sla event-publisher <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 1 `；EOL ` RVA 0x34A890E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009852

```text
(exec)# show ip sla event-publisher detail <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 2 `；EOL ` RVA 0x34A890C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009884

```text
(exec)# show ip sla group schedule <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 0 `；EOL ` RVA 0x34A96958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011402

```text
(exec)# show ip sla group schedule details <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 28 `；EOL ` RVA 0x34A96930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007028

```text
(exec)# show ip sla history <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009930

```text
(exec)# show ip sla history full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 5 `；EOL ` RVA 0x34A989A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009944

```text
(exec)# show ip sla history interval-statistics <cr>
```

Handler ` RVA 0x102DDA40 `；selector ` 45 `；EOL ` RVA 0x34A98EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009921

```text
(exec)# show ip sla history raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 7 `；EOL ` RVA 0x34A98700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009937

```text
(exec)# show ip sla history tabular <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006911

```text
(exec)# show ip sla operational-state <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 16 `；EOL ` RVA 0x34A96E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015060

```text
(exec)# show ip sla periodic hostname summary <cr>
```

Handler ` RVA 0x102DDC20 `；selector ` 0 `；EOL ` RVA 0x34A962F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1a1a81b796538511](../../evidence/conditions-sets-010.md#c-1a1a81b796538511) · [缺口 G-e795325d219eadad](../../evidence/gaps-sets-008.md#g-e795325d219eadad) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007026

```text
(exec)# show ip sla reaction-configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 17 `；EOL ` RVA 0x34A9A568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007015

```text
(exec)# show ip sla reaction-trigger <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 12 `；EOL ` RVA 0x34A9A278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006869

```text
(exec)# show ip sla responder <cr>
```

Handler ` RVA 0x101FD080 `；selector ` 0 `；EOL ` RVA 0x34A719E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015078

```text
(exec)# show ip sla schedule backup tree summary <cr>
```

Handler ` RVA 0x102DDB30 `；selector ` 0 `；EOL ` RVA 0x34A96598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f8ae634dec6b4cb](../../evidence/conditions-sets-031.md#c-4f8ae634dec6b4cb) · [缺口 G-44211bc20d700a18](../../evidence/gaps-sets-003.md#g-44211bc20d700a18) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007017

```text
(exec)# show ip sla statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 18 `；EOL ` RVA 0x34A99A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009940

```text
(exec)# show ip sla statistics aggregated <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 25 `；EOL ` RVA 0x34A99550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011431

```text
(exec)# show ip sla statistics aggregated details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 26 `；EOL ` RVA 0x34A99528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009936

```text
(exec)# show ip sla statistics details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 22 `；EOL ` RVA 0x34A99A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006871

```text
(exec)# show ip sla summary <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 46 `；EOL ` RVA 0x34A95DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022663

```text
(exec)# show ip sla summary destination <?ipv4orv6_addr_action@555589fe9db8> <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 47 `；EOL ` RVA 0x34A95E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-60a10f2f63731b25](../../evidence/gaps-sets-004.md#g-60a10f2f63731b25) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006923

```text
(exec)# show ip sla totals-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 4 `；EOL ` RVA 0x34A97188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011412

```text
(exec)# show ip sla twamp connection requests <cr>
```

Handler ` RVA 0x1021EB60 `；selector ` 0 `；EOL ` RVA 0x34A73EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-eeb5d1a6f1bcd000](../../evidence/state_effects-sets-050.md#s-eeb5d1a6f1bcd000)

### path-009874

```text
(exec)# show ip sla twamp session <cr>
```

Handler ` RVA 0x10238810 `；selector ` 0 `；EOL ` RVA 0x34A76DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-ad9f2baeb05b2db3](../../evidence/state_effects-sets-037.md#s-ad9f2baeb05b2db3)

### path-009864

```text
(exec)# show ip sla twamp standards <cr>
```

Handler ` RVA 0x10238750 `；selector ` 0 `；EOL ` RVA 0x34A770A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009885

```text
(exec)# show ip sla twamp-light session <cr>
```

Handler ` RVA 0x1023AE80 `；selector ` 0 `；EOL ` RVA 0x34A79728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2e8dda49162d24bd](../../evidence/state_effects-sets-010.md#s-2e8dda49162d24bd)

### path-015277

```text
(exec)# show ip sla udp zero checksum hash <cr>
```

Handler ` RVA 0x101D8B00 `；selector ` 0 `；EOL ` RVA 0x34A9AC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d53c10bc3c8654b4](../../evidence/conditions-sets-082.md#c-d53c10bc3c8654b4) · [缺口 G-ed49a896157802de](../../evidence/gaps-sets-008.md#g-ed49a896157802de) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001814

```text
(exec)# show ip sockets <cr>
```

Handler ` RVA 0xCE441C0 `；selector ` 0 `；EOL ` RVA 0x33D31858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006928

```text
(exec)# show ip source binding <cr>
```

Handler ` RVA 0x15FA8BF0 `；selector ` 0 `；EOL ` RVA 0x35E7DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f93d0b7b9a074084](../../evidence/conditions-sets-096.md#c-f93d0b7b9a074084) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001808

```text
(exec)# show ip spd <cr>
```

Handler ` RVA 0xCF78E90 `；selector ` 0 `；EOL ` RVA 0x33D31AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002605

```text
(exec)# show ip ssh <cr>
```

Handler ` RVA 0x12360610 `；selector ` 0 `；EOL ` RVA 0x35828848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019176

```text
(exec)# show ip static route <?ipaddrmask_action@5555897e3ec8> <cr>
```

Handler ` RVA 0xE2A5A00 `；selector ` 0 `；EOL ` RVA 0x3428FF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a22fbb0601ca6162](../../evidence/conditions-sets-063.md#c-a22fbb0601ca6162) · [缺口 G-950b75415e4673aa](../../evidence/gaps-sets-005.md#g-950b75415e4673aa) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009637

```text
(exec)# show ip static route bfd <cr>
```

Handler ` RVA 0xE2A6F50 `；selector ` 0 `；EOL ` RVA 0x3428F298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-68817baa1e6a4f6a](../../evidence/conditions-sets-040.md#c-68817baa1e6a4f6a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022388

```text
(exec)# show ip static route bfd <interface> <cr>
```

Handler ` RVA 0xE2A6F50 `；selector ` 0 `；EOL ` RVA 0x3428F298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-07fd8d79af472922](../../evidence/conditions-sets-003.md#c-07fd8d79af472922) · [缺口 G-7a1928abc187d8ba](../../evidence/gaps-sets-005.md#g-7a1928abc187d8ba) · [参数 P-0be9fd4c5fb45e31](../../evidence/parameters-sets-001.md#p-0be9fd4c5fb45e31) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009555

```text
(exec)# show ip static route rwatch-rib <cr>
```

Handler ` RVA 0xE2A7940 `；selector ` 0 `；EOL ` RVA 0x3428F850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5aa975823e16c479](../../evidence/conditions-sets-036.md#c-5aa975823e16c479) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009589

```text
(exec)# show ip static route sr-polices <cr>
```

Handler ` RVA 0xE2A79D0 `；selector ` 0 `；EOL ` RVA 0x3428FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd5e5ad91a8d2392](../../evidence/conditions-sets-085.md#c-dd5e5ad91a8d2392) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009505

```text
(exec)# show ip static route summary <cr>
```

Handler ` RVA 0xE2A7770 `；selector ` 0 `；EOL ` RVA 0x3428EE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002721

```text
(exec)# show ip subscriber <cr>
```

Handler ` RVA 0x11A37870 `；selector ` 0 `；EOL ` RVA 0x355CDAE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-01825996c42519f8](../../evidence/state_effects-sets-001.md#s-01825996c42519f8)

### path-022052

```text
(exec)# show ip tcp adjust stats <interface> <cr>
```

Handler ` RVA 0xCDEFC60 `；selector ` 0 `；EOL ` RVA 0x33CF7668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c23b1ff4eb1a833a](../../evidence/conditions-sets-075.md#c-c23b1ff4eb1a833a) · [缺口 G-15b09437b8a1a52b](../../evidence/gaps-sets-001.md#g-15b09437b8a1a52b) · [参数 P-9e78a61ab5cdd5f3](../../evidence/parameters-sets-012.md#p-9e78a61ab5cdd5f3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005828

```text
(exec)# show ip tcp header-compression <cr>
```

Handler ` RVA 0xD194400 `；selector ` 0 `；EOL ` RVA 0x33DAB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7df4d3139ca6c380](../../evidence/conditions-sets-049.md#c-7df4d3139ca6c380) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006007

```text
(exec)# show ip telnet status <cr>
```

Handler ` RVA 0xCDEFBC0 `；selector ` 0 `；EOL ` RVA 0x33D02090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001855

```text
(exec)# show ip traffic <cr>
```

Handler ` RVA 0xCECF560 `；selector ` 0 `；EOL ` RVA 0x33D32270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018109

```text
(exec)# show ip traffic interface <interface> <cr>
```

Handler ` RVA 0xCECF4F0 `；selector ` 0 `；EOL ` RVA 0x33D32330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8a70382186606eea](../../evidence/conditions-sets-054.md#c-8a70382186606eea) · [缺口 G-3907641989e8551e](../../evidence/gaps-sets-002.md#g-3907641989e8551e) · [参数 P-71065a26c2012cdf](../../evidence/parameters-sets-009.md#p-71065a26c2012cdf) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009104

```text
(exec)# show ip traffic topology base <cr>
```

Handler ` RVA 0xCF0ED10 `；selector ` 0 `；EOL ` RVA 0x33D31E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-d35c863a9870ef53](../../evidence/state_effects-sets-045.md#s-d35c863a9870ef53)

### path-002538

```text
(exec)# show ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 2 `；EOL ` RVA 0x34B5A698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002687

```text
(exec)# show ip virtual-reassembly <cr>
```

Handler ` RVA 0xC78EA70 `；selector ` 0 `；EOL ` RVA 0x33AECED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e6681981681a3ac1](../../evidence/conditions-sets-089.md#c-e6681981681a3ac1) · [状态效果 S-beebc4278db75a17](../../evidence/state_effects-sets-040.md#s-beebc4278db75a17)

### path-001728

```text
(exec)# show ipam counts <cr>
```

Handler ` RVA 0xCEA9220 `；selector ` 0 `；EOL ` RVA 0x33D1B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001720

```text
(exec)# show ipam pool <cr>
```

Handler ` RVA 0xCEA02D0 `；selector ` 0 `；EOL ` RVA 0x33D1B340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001737

```text
(exec)# show ipam queues <cr>
```

Handler ` RVA 0xCEA9160 `；selector ` 0 `；EOL ` RVA 0x33D1B5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001760

```text
(exec)# show ipam status <cr>
```

Handler ` RVA 0xCE9D6D0 `；selector ` 0 `；EOL ` RVA 0x33D1B890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001065

```text
(exec)# show ipc all <cr>
```

Handler ` RVA 0xD3B9630 `；selector ` 0 `；EOL ` RVA 0x33E2A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-0c6b627abf0ef196](../../evidence/state_effects-sets-003.md#s-0c6b627abf0ef196)

### path-001185

```text
(exec)# show ipc app <cr>
```

Handler ` RVA 0xD3BE590 `；selector ` 0 `；EOL ` RVA 0x33E2D5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001199

```text
(exec)# show ipc buffer <cr>
```

Handler ` RVA 0xD39FCA0 `；selector ` 0 `；EOL ` RVA 0x33E2D858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008464

```text
(exec)# show ipc cli <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xD38B220 `；selector ` 0 `；EOL ` RVA 0x33E2AAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPC Seatid (in hex)；` string ` Remote command string。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-d04ece3d584907a5](../../evidence/parameters-sets-016.md#p-d04ece3d584907a5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001152

```text
(exec)# show ipc delayed <cr>
```

Handler ` RVA 0xD3A24C0 `；selector ` 0 `；EOL ` RVA 0x33E2D018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001005

```text
(exec)# show ipc fc <cr>
```

Handler ` RVA 0xD3B96E0 `；selector ` 0 `；EOL ` RVA 0x33E29FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001191

```text
(exec)# show ipc fragment <cr>
```

Handler ` RVA 0xD3BE5F0 `；selector ` 0 `；EOL ` RVA 0x33E2CD28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-b49acf8445135827](../../evidence/state_effects-sets-038.md#s-b49acf8445135827)

### path-001128

```text
(exec)# show ipc hog-info <cr>
```

Handler ` RVA 0xD3B8FB0 `；selector ` 0 `；EOL ` RVA 0x33E2C938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005008

```text
(exec)# show ipc keepalive tx <cr>
```

Handler ` RVA 0xD3B8EC0 `；selector ` 0 `；EOL ` RVA 0x33E2E360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-8642788651b38c1d](../../evidence/state_effects-sets-028.md#s-8642788651b38c1d)

### path-004786

```text
(exec)# show ipc mcast appclass <cr>
```

Handler ` RVA 0xD408040 `；selector ` 0 `；EOL ` RVA 0x33E42858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-1b7f6b8044941919](../../evidence/state_effects-sets-006.md#s-1b7f6b8044941919)

### path-004818

```text
(exec)# show ipc mcast groups <cr>
```

Handler ` RVA 0xD407F80 `；selector ` 0 `；EOL ` RVA 0x33E42C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-f559c30818c54ad0](../../evidence/state_effects-sets-052.md#s-f559c30818c54ad0)

### path-008484

```text
(exec)# show ipc mcast groups <number:1..4294967295> <cr>
```

Handler ` RVA 0xD407F10 `；selector ` 0 `；EOL ` RVA 0x33E42F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-6d276200dc0ed569](../../evidence/parameters-sets-009.md#p-6d276200dc0ed569) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004865

```text
(exec)# show ipc mcast sessions <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 0 `；EOL ` RVA 0x33E43368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-830e3f25330873e3](../../evidence/state_effects-sets-028.md#s-830e3f25330873e3)

### path-008541

```text
(exec)# show ipc mcast sessions verbose <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 1 `；EOL ` RVA 0x33E43340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-830e3f25330873e3](../../evidence/state_effects-sets-028.md#s-830e3f25330873e3)

### path-004770

```text
(exec)# show ipc mcast status <cr>
```

Handler ` RVA 0xD408100 `；selector ` 0 `；EOL ` RVA 0x33E42480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-c1877ac617f4a871](../../evidence/state_effects-sets-041.md#s-c1877ac617f4a871)

### path-001094

```text
(exec)# show ipc nodes <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 0 `；EOL ` RVA 0x33E2A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-778b28694736f957](../../evidence/state_effects-sets-025.md#s-778b28694736f957)

### path-004826

```text
(exec)# show ipc nodes capabilities <cr>
```

Handler ` RVA 0xD45A9C0 `；selector ` 0 `；EOL ` RVA 0x33E489F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-778b28694736f957](../../evidence/state_effects-sets-025.md#s-778b28694736f957)

### path-004812

```text
(exec)# show ipc nodes issu <cr>
```

Handler ` RVA 0xD45ADB0 `；selector ` 0 `；EOL ` RVA 0x33E48750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-778b28694736f957](../../evidence/state_effects-sets-025.md#s-778b28694736f957)

### path-004827

```text
(exec)# show ipc nodes verbose <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 1 `；EOL ` RVA 0x33E27958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-778b28694736f957](../../evidence/state_effects-sets-025.md#s-778b28694736f957)

### path-001145

```text
(exec)# show ipc ports <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 0 `；EOL ` RVA 0x33E2B120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-6b7666b4b626273a](../../evidence/state_effects-sets-023.md#s-6b7666b4b626273a)

### path-004841

```text
(exec)# show ipc ports verbose <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 1 `；EOL ` RVA 0x33E2B3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-6b7666b4b626273a](../../evidence/state_effects-sets-023.md#s-6b7666b4b626273a)

### path-000989

```text
(exec)# show ipc queue <cr>
```

Handler ` RVA 0xD3B91C0 `；selector ` 0 `；EOL ` RVA 0x33E29D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004771

```text
(exec)# show ipc rmi all <cr>
```

Handler ` RVA 0xD3FE890 `；selector ` 0 `；EOL ` RVA 0x33E3F8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-c4fd546d6072c4de](../../evidence/state_effects-sets-042.md#s-c4fd546d6072c4de)

### path-010607

```text
(exec)# show ipc rmi thresholds ru <string> <cr>
```

Handler ` RVA 0xD3FE9F0 `；selector ` 0 `；EOL ` RVA 0x33E401F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU id(in hex)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-1f71f90238213b0b](../../evidence/parameters-sets-003.md#p-1f71f90238213b0b) · [状态效果 S-87cf824cb90e1851](../../evidence/state_effects-sets-029.md#s-87cf824cb90e1851)

### path-001309

```text
(exec)# show ipc rpc <cr>
```

Handler ` RVA 0xD3B90F0 `；selector ` 0 `；EOL ` RVA 0x33E2E7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-42782220810b9eba](../../evidence/state_effects-sets-015.md#s-42782220810b9eba)

### path-001229

```text
(exec)# show ipc sess-ack <cr>
```

Handler ` RVA 0xD3B92E0 `；selector ` 0 `；EOL ` RVA 0x33E2DDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004861

```text
(exec)# show ipc session all <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 0 `；EOL ` RVA 0x33E2B898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-d9e038ec241e5a3a](../../evidence/state_effects-sets-046.md#s-d9e038ec241e5a3a)

### path-008538

```text
(exec)# show ipc session all verbose <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 1 `；EOL ` RVA 0x33E2B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-d9e038ec241e5a3a](../../evidence/state_effects-sets-046.md#s-d9e038ec241e5a3a)

### path-004886

```text
(exec)# show ipc session tx <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 0 `；EOL ` RVA 0x33E2BF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-a9b4648ac32344ed](../../evidence/state_effects-sets-036.md#s-a9b4648ac32344ed)

### path-008551

```text
(exec)# show ipc session tx verbose <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 1 `；EOL ` RVA 0x33E2BF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-a9b4648ac32344ed](../../evidence/state_effects-sets-036.md#s-a9b4648ac32344ed)

### path-001172

```text
(exec)# show ipc status <cr>
```

Handler ` RVA 0xD3B8DA0 `；selector ` 0 `；EOL ` RVA 0x33E2C640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-67e45b372d2202db](../../evidence/state_effects-sets-022.md#s-67e45b372d2202db)

### path-001216

```text
(exec)# show ipc thread-stats <cr>
```

Handler ` RVA 0xD3985A0 `；selector ` 0 `；EOL ` RVA 0x33E2DB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004892

```text
(exec)# show ipc trace <number:1..3> <cr>
```

Handler ` RVA 0xD3B9000 `；selector ` 0 `；EOL ` RVA 0x33E2D328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type of buffer(1. event 2. debug 3. error)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-8efb61522b8c3136](../../evidence/parameters-sets-011.md#p-8efb61522b8c3136) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001281

```text
(exec)# show ipc util <cr>
```

Handler ` RVA 0xD3BC620 `；selector ` 0 `；EOL ` RVA 0x33E2EA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001241

```text
(exec)# show ipc watermark <cr>
```

Handler ` RVA 0xD3B8F20 `；selector ` 0 `；EOL ` RVA 0x33E2E050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001070

```text
(exec)# show ipc zones <cr>
```

Handler ` RVA 0xD3BC120 `；selector ` 0 `；EOL ` RVA 0x33E2AD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002648

```text
(exec)# show ipv6 access-list <cr>
```

Handler ` RVA 0x1217F2C0 `；selector ` 0 `；EOL ` RVA 0x357B0418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15ba82e1b1af0acd](../../evidence/conditions-sets-009.md#c-15ba82e1b1af0acd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009806

```text
(exec)# show ipv6 access-list <string> dump-og-database <cr>
```

Handler ` RVA 0x1217F470 `；selector ` 0 `；EOL ` RVA 0x357B04A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User selected string identifying this access list。

[条件 C-47044ba01fe6dceb](../../evidence/conditions-sets-028.md#c-47044ba01fe6dceb) · [参数 P-4019a6f8b247af69](../../evidence/parameters-sets-005.md#p-4019a6f8b247af69) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015045

```text
(exec)# show ipv6 address <?match_ipv6_addrinfo_action@55558ad32ea0> <cr>
```

Handler ` RVA 0x12300550 `；selector ` 0 `；EOL ` RVA 0x357DEED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b33983ba79cffae](../../evidence/conditions-sets-011.md#c-1b33983ba79cffae) · [缺口 G-f79b1e5aa4785a98](../../evidence/gaps-sets-009.md#g-f79b1e5aa4785a98) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002707

```text
(exec)# show ipv6 alias <cr>
```

Handler ` RVA 0x12303F00 `；selector ` 0 `；EOL ` RVA 0x357DF538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003130

```text
(exec)# show ipv6 cef <cr>
```

Handler ` RVA 0xB662E40 `；selector ` 0 `；EOL ` RVA 0x337CDBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d33b24b2607b50b8](../../evidence/conditions-sets-081.md#c-d33b24b2607b50b8) · [状态效果 S-3f50e4a564b11b87](../../evidence/state_effects-sets-014.md#s-3f50e4a564b11b87)

### path-015455

```text
(exec)# show ipv6 cef <interface> <cr>
```

Handler ` RVA 0xB662E40 `；selector ` 0 `；EOL ` RVA 0x337CDBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-752603bb68d1ada2](../../evidence/conditions-sets-045.md#c-752603bb68d1ada2) · [缺口 G-1eb3993852c66ed8](../../evidence/gaps-sets-002.md#g-1eb3993852c66ed8) · [参数 P-a0c8755f7921148b](../../evidence/parameters-sets-012.md#p-a0c8755f7921148b) · [状态效果 S-3f50e4a564b11b87](../../evidence/state_effects-sets-014.md#s-3f50e4a564b11b87)

### path-007052

```text
(exec)# show ipv6 cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337CE290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fea93fa3a2ba2841](../../evidence/conditions-sets-098.md#c-fea93fa3a2ba2841) · [状态效果 S-2ca05be849ece704](../../evidence/state_effects-sets-010.md#s-2ca05be849ece704)

### path-011410

```text
(exec)# show ipv6 cef neighbor discovery throttling <cr>
```

Handler ` RVA 0xB671710 `；selector ` 0 `；EOL ` RVA 0x337CD4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c63cf6e327e36988](../../evidence/conditions-sets-076.md#c-c63cf6e327e36988) · [状态效果 S-3f50e4a564b11b87](../../evidence/state_effects-sets-014.md#s-3f50e4a564b11b87)

### path-006868

```text
(exec)# show ipv6 cef protocol-discard <cr>
```

Handler ` RVA 0xB5C2EB0 `；selector ` 73 `；EOL ` RVA 0x337D89C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006894

```text
(exec)# show ipv6 cef summary <cr>
```

Handler ` RVA 0xB670E30 `；selector ` 1 `；EOL ` RVA 0x337CD130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c63cf6e327e36988](../../evidence/conditions-sets-076.md#c-c63cf6e327e36988) · [状态效果 S-3f50e4a564b11b87](../../evidence/state_effects-sets-014.md#s-3f50e4a564b11b87)

### path-009913

```text
(exec)# show ipv6 cef switching statistics <cr>
```

Handler ` RVA 0xB66E5F0 `；selector ` 0 `；EOL ` RVA 0x337CDF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fea93fa3a2ba2841](../../evidence/conditions-sets-098.md#c-fea93fa3a2ba2841) · [状态效果 S-3f50e4a564b11b87](../../evidence/state_effects-sets-014.md#s-3f50e4a564b11b87)

### path-009918

```text
(exec)# show ipv6 cef traffic prefix-length <cr>
```

Handler ` RVA 0xB671680 `；selector ` 0 `；EOL ` RVA 0x337CE7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fea93fa3a2ba2841](../../evidence/conditions-sets-098.md#c-fea93fa3a2ba2841) · [状态效果 S-93538d4e61d28cdf](../../evidence/state_effects-sets-031.md#s-93538d4e61d28cdf)

### path-006938

```text
(exec)# show ipv6 cef tree <cr>
```

Handler ` RVA 0xB670D30 `；selector ` 0 `；EOL ` RVA 0x337CD7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c63cf6e327e36988](../../evidence/conditions-sets-076.md#c-c63cf6e327e36988) · [状态效果 S-3f50e4a564b11b87](../../evidence/state_effects-sets-014.md#s-3f50e4a564b11b87)

### path-006728

```text
(exec)# show ipv6 destination-guard policy <cr>
```

Handler ` RVA 0x136B13F0 `；selector ` 0 `；EOL ` RVA 0x35C02EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002596

```text
(exec)# show ipv6 dhcp <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 0 `；EOL ` RVA 0x357C0EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006826

```text
(exec)# show ipv6 dhcp binding <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 0 `；EOL ` RVA 0x357C6450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006846

```text
(exec)# show ipv6 dhcp conflict <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 3 `；EOL ` RVA 0x357C6D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006784

```text
(exec)# show ipv6 dhcp database <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 2 `；EOL ` RVA 0x357C5C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006714

```text
(exec)# show ipv6 dhcp interface <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 1 `；EOL ` RVA 0x357C0868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c99ec8ddb5b8125f](../../evidence/conditions-sets-078.md#c-c99ec8ddb5b8125f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019240

```text
(exec)# show ipv6 dhcp interface <interface> <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 1 `；EOL ` RVA 0x357C0868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f227b54e9ca2fd51](../../evidence/conditions-sets-093.md#c-f227b54e9ca2fd51) · [缺口 G-3ada891ce285a646](../../evidence/gaps-sets-003.md#g-3ada891ce285a646) · [参数 P-1cb93ec109cdb36a](../../evidence/parameters-sets-003.md#p-1cb93ec109cdb36a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011877

```text
(exec)# show ipv6 dhcp mac-hash-table dump pool <string> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 8 `；EOL ` RVA 0x357C7158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pool name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-c08b972a2d83bb8c](../../evidence/parameters-sets-015.md#p-c08b972a2d83bb8c) · [状态效果 S-1a98627041372137](../../evidence/state_effects-sets-006.md#s-1a98627041372137)

### path-012135

```text
(exec)# show ipv6 dhcp mac-hash-table dump pool <string> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 7 `；EOL ` RVA 0x357C71A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pool name；` unsigned_number ` Lower bound of index range；` unsigned_number ` Upper bound of index range。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-6b881825297e6ab3](../../evidence/parameters-sets-008.md#p-6b881825297e6ab3) · [状态效果 S-1a98627041372137](../../evidence/state_effects-sets-006.md#s-1a98627041372137)

### path-009819

```text
(exec)# show ipv6 dhcp packet statistics <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 6 `；EOL ` RVA 0x357C6A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006825

```text
(exec)# show ipv6 dhcp pool <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 1 `；EOL ` RVA 0x357C6748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009772

```text
(exec)# show ipv6 dhcp relay binding <cr>
```

Handler ` RVA 0x121B3460 `；selector ` 1 `；EOL ` RVA 0x357C33B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009809

```text
(exec)# show ipv6 dhcp route <address> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 5 `；EOL ` RVA 0x357C6040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-bed6f5b93ba7ce08](../../evidence/parameters-sets-014.md#p-bed6f5b93ba7ce08) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019362

```text
(exec)# show ipv6 dhcp route <prefix:dynamic> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 5 `；EOL ` RVA 0x357C6040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-fce2cf06cd24f38d](../../evidence/conditions-sets-098.md#c-fce2cf06cd24f38d) · [缺口 G-d33d5530b555eb71](../../evidence/gaps-sets-007.md#g-d33d5530b555eb71) · [参数 P-ad5c34686bcdd5f9](../../evidence/parameters-sets-013.md#p-ad5c34686bcdd5f9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006677

```text
(exec)# show ipv6 dhcp statistics <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 2 `；EOL ` RVA 0x357C0B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006682

```text
(exec)# show ipv6 eigrp accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x35467758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-006672

```text
(exec)# show ipv6 eigrp interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35466788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-393ef9f399668c49](../../evidence/conditions-sets-022.md#c-393ef9f399668c49) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-019190

```text
(exec)# show ipv6 eigrp interfaces <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35466788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80867c0ed77021d5](../../evidence/conditions-sets-050.md#c-80867c0ed77021d5) · [缺口 G-5e739b92576e1d69](../../evidence/gaps-sets-004.md#g-5e739b92576e1d69) · [参数 P-2a0afa2702cab971](../../evidence/parameters-sets-004.md#p-2a0afa2702cab971) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-006699

```text
(exec)# show ipv6 eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35466290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a524b2dba15c5b9](../../evidence/conditions-sets-023.md#c-3a524b2dba15c5b9) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-019219

```text
(exec)# show ipv6 eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35466290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-039dc33d5cd480fb](../../evidence/conditions-sets-002.md#c-039dc33d5cd480fb) · [缺口 G-3ad65496b0f12ccd](../../evidence/gaps-sets-003.md#g-3ad65496b0f12ccd) · [参数 P-a97c2d21c62dc44f](../../evidence/parameters-sets-013.md#p-a97c2d21c62dc44f) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-006730

```text
(exec)# show ipv6 eigrp sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-15591320d0d38a6d](../../evidence/state_effects-sets-005.md#s-15591320d0d38a6d)

### path-006769

```text
(exec)# show ipv6 eigrp sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-de49fbe88c6e0978](../../evidence/state_effects-sets-047.md#s-de49fbe88c6e0978)

### path-006613

```text
(exec)# show ipv6 eigrp timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x35466A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-006832

```text
(exec)# show ipv6 eigrp topology <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x354670B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f76acb445fba1c4](../../evidence/conditions-sets-031.md#c-4f76acb445fba1c4) · [状态效果 S-fbdd11ede981f163](../../evidence/state_effects-sets-053.md#s-fbdd11ede981f163)

### path-019279

```text
(exec)# show ipv6 eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x354670B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to display information about。

[条件 C-9a5d83e0daa114a4](../../evidence/conditions-sets-060.md#c-9a5d83e0daa114a4) · [缺口 G-9ae72f2157cab30a](../../evidence/gaps-sets-006.md#g-9ae72f2157cab30a) · [参数 P-c610da5717347127](../../evidence/parameters-sets-015.md#p-c610da5717347127) · [状态效果 S-42049565837fc22c](../../evidence/state_effects-sets-014.md#s-42049565837fc22c)

### path-006639

```text
(exec)# show ipv6 eigrp traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x35466D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-dd73c02a9286bfe0](../../evidence/state_effects-sets-047.md#s-dd73c02a9286bfe0)

### path-002718

```text
(exec)# show ipv6 enablement <cr>
```

Handler ` RVA 0x123003B0 `；selector ` 0 `；EOL ` RVA 0x357DF7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002248

```text
(exec)# show ipv6 errors-internal <cr>
```

Handler ` RVA 0x12304EF0 `；selector ` 0 `；EOL ` RVA 0x357E3398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4606ca718ceaf8b](../../evidence/conditions-sets-082.md#c-d4606ca718ceaf8b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006206

```text
(exec)# show ipv6 features global <cr>
```

Handler ` RVA 0x123058C0 `；selector ` 0 `；EOL ` RVA 0x357E5868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002696

```text
(exec)# show ipv6 general-prefix <cr>
```

Handler ` RVA 0x12303340 `；selector ` 0 `；EOL ` RVA 0x357DF290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006428

```text
(exec)# show ipv6 local pool <cr>
```

Handler ` RVA 0x1232CA00 `；selector ` 0 `；EOL ` RVA 0x358110E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-efaa3f25c33856a1](../../evidence/conditions-sets-093.md#c-efaa3f25c33856a1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002722

```text
(exec)# show ipv6 mfib <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca7cba7852ec64d8](../../evidence/conditions-sets-078.md#c-ca7cba7852ec64d8) · [状态效果 S-5a8b976e30a4a2aa](../../evidence/state_effects-sets-020.md#s-5a8b976e30a4a2aa)

### path-006604

```text
(exec)# show ipv6 mfib cable <cr>
```

Handler ` RVA 0x1197DD40 `；selector ` 0 `；EOL ` RVA 0x355B8E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3efb59728ac9f437](../../evidence/state_effects-sets-014.md#s-3efb59728ac9f437)

### path-006654

```text
(exec)# show ipv6 mfib interface <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B9DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8bf5a5acdfcd7d48](../../evidence/conditions-sets-054.md#c-8bf5a5acdfcd7d48) · [状态效果 S-7661feb179cf3d37](../../evidence/state_effects-sets-025.md#s-7661feb179cf3d37)

### path-009547

```text
(exec)# show ipv6 mfib internal fibidb <cr>
```

Handler ` RVA 0x1197DE80 `；selector ` 0 `；EOL ` RVA 0x355B92A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-83989142fb267824](../../evidence/state_effects-sets-028.md#s-83989142fb267824)

### path-009704

```text
(exec)# show ipv6 mfib internal mem <cr>
```

Handler ` RVA 0x1197DF50 `；selector ` 0 `；EOL ` RVA 0x355B95E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-c3704fa322e2650d](../../evidence/state_effects-sets-041.md#s-c3704fa322e2650d)

### path-006683

```text
(exec)# show ipv6 mfib rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f188dcc50cbdf27](../../evidence/conditions-sets-055.md#c-8f188dcc50cbdf27) · [状态效果 S-86dd72cbd3dc51bf](../../evidence/state_effects-sets-029.md#s-86dd72cbd3dc51bf)

### path-006532

```text
(exec)# show ipv6 mfib status <cr>
```

Handler ` RVA 0x1197C470 `；selector ` 0 `；EOL ` RVA 0x355B99F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-83989142fb267824](../../evidence/state_effects-sets-028.md#s-83989142fb267824)

### path-006662

```text
(exec)# show ipv6 mld acl-db <cr>
```

Handler ` RVA 0x11625660 `；selector ` 6 `；EOL ` RVA 0x3554A6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a72383b5b9871bd](../../evidence/conditions-sets-060.md#c-9a72383b5b9871bd) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-009619

```text
(exec)# show ipv6 mld all-vrfs traffic <cr>
```

Handler ` RVA 0x11625660 `；selector ` 4 `；EOL ` RVA 0x3554B100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76db2ed043998d11](../../evidence/conditions-sets-046.md#c-76db2ed043998d11) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-006725

```text
(exec)# show ipv6 mld gir <cr>
```

Handler ` RVA 0x11625660 `；selector ` 7 `；EOL ` RVA 0x3554ADE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c040cde0ca3b9d9d](../../evidence/conditions-sets-074.md#c-c040cde0ca3b9d9d) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-006739

```text
(exec)# show ipv6 mld groups <cr>
```

Handler ` RVA 0x11625660 `；selector ` 2 `；EOL ` RVA 0x35549A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfe40ee549809224](../../evidence/conditions-sets-080.md#c-cfe40ee549809224) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-019281

```text
(exec)# show ipv6 mld groups <interface> <cr>
```

Handler ` RVA 0x11625660 `；selector ` 2 `；EOL ` RVA 0x35549A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d5f6cbb5d22bce7](../../evidence/conditions-sets-024.md#c-3d5f6cbb5d22bce7) · [缺口 G-5f9d1fc2c61a7a71](../../evidence/gaps-sets-004.md#g-5f9d1fc2c61a7a71) · [参数 P-59e4dd46c32aac7c](../../evidence/parameters-sets-007.md#p-59e4dd46c32aac7c) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-006624

```text
(exec)# show ipv6 mld interface <cr>
```

Handler ` RVA 0x11625660 `；selector ` 1 `；EOL ` RVA 0x35549758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aa7c6afece46123](../../evidence/conditions-sets-048.md#c-7aa7c6afece46123) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-019144

```text
(exec)# show ipv6 mld interface <interface> <cr>
```

Handler ` RVA 0x11625660 `；selector ` 1 `；EOL ` RVA 0x35549758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1571cb67af4b6bce](../../evidence/conditions-sets-008.md#c-1571cb67af4b6bce) · [缺口 G-6abf17a64776ca89](../../evidence/gaps-sets-004.md#g-6abf17a64776ca89) · [参数 P-8c7a70ffd3f9558f](../../evidence/parameters-sets-011.md#p-8c7a70ffd3f9558f) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-006754

```text
(exec)# show ipv6 mld internal <cr>
```

Handler ` RVA 0x11628960 `；selector ` 0 `；EOL ` RVA 0x3554AA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-724059e95b80d9bb](../../evidence/conditions-sets-044.md#c-724059e95b80d9bb) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-019265

```text
(exec)# show ipv6 mld internal <interface> <cr>
```

Handler ` RVA 0x11628960 `；selector ` 0 `；EOL ` RVA 0x3554AA88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9d4830dfbe5ecf37](../../evidence/conditions-sets-061.md#c-9d4830dfbe5ecf37) · [缺口 G-0c173f1f9e8f09e3](../../evidence/gaps-sets-001.md#g-0c173f1f9e8f09e3) · [参数 P-760749805b4d6073](../../evidence/parameters-sets-009.md#p-760749805b4d6073) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

