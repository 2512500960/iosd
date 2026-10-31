# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-031042

```text
(config)# no cts policy-server username <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 1 `；EOL ` RVA 0x359F7198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-62878993964623c7](../../evidence/conditions-sets-038.md#c-62878993964623c7) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029179

```text
(config)# no cts role-based enforcement <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 0 `；EOL ` RVA 0x35CFA6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3c2a529e2ab1a1fd](../../evidence/conditions-sets-023.md#c-3c2a529e2ab1a1fd) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-044974

```text
(config)# no cts role-based enforcement logging-interval <number:5..86400> <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 14 `；EOL ` RVA 0x35CFA6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enter logging interval in seconds。

[条件 C-e8be9f72014ed63c](../../evidence/conditions-sets-090.md#c-e8be9f72014ed63c) · [参数 P-ab0334442b8cbc0d](../../evidence/parameters-sets-013.md#p-ab0334442b8cbc0d) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-028878

```text
(config)# no cts role-based ipv6-copy <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 6 `；EOL ` RVA 0x35CE8948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-32732e14c3f77d59](../../evidence/conditions-sets-020.md#c-32732e14c3f77d59) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-035092

```text
(config)# no cts role-based monitor all <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 12 `；EOL ` RVA 0x35CFB810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-14caee070928983d](../../evidence/conditions-sets-008.md#c-14caee070928983d) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-035272

```text
(config)# no cts role-based policy priority-static <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 13 `；EOL ` RVA 0x35CFAC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e9f606d272b51a89](../../evidence/conditions-sets-090.md#c-e9f606d272b51a89) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029184

```text
(config)# no cts role-based sgt-caching <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 8 `；EOL ` RVA 0x35CF8668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1452a1125e391c7](../../evidence/conditions-sets-081.md#c-d1452a1125e391c7) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-035206

```text
(config)# no cts role-based sgt-caching with-enforcement <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 7 `；EOL ` RVA 0x35CF8358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cbaf825484834ab9](../../evidence/conditions-sets-078.md#c-cbaf825484834ab9) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-035282

```text
(config)# no cts role-based sgt-map <address> <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 2 `；EOL ` RVA 0x35CE72E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 host address。

[条件 C-d5b58e781740419c](../../evidence/conditions-sets-082.md#c-d5b58e781740419c) · [参数 P-4d4a85f27ad2348e](../../evidence/parameters-sets-006.md#p-4d4a85f27ad2348e) · [状态效果 S-95323df5f54b3711](../../evidence/state_effects-sets-032.md#s-95323df5f54b3711)

### path-030799

```text
(config)# no cts server load-balance <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 4 `；EOL ` RVA 0x35A15D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2947ce6db8859635](../../evidence/conditions-sets-016.md#c-2947ce6db8859635) · [状态效果 S-d3ebd2b2c3b5e6df](../../evidence/state_effects-sets-045.md#s-d3ebd2b2c3b5e6df)

### path-027480

```text
(config)# no cts sgt <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 0 `；EOL ` RVA 0x35A161B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-56a6ab370fff158e](../../evidence/conditions-sets-034.md#c-56a6ab370fff158e) · [状态效果 S-11d7481c62894a2a](../../evidence/state_effects-sets-004.md#s-11d7481c62894a2a)

### path-030992

```text
(config)# no cts sxp enable <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 49 `；EOL ` RVA 0x35A4D6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [状态效果 S-98b0ef7f5679f067](../../evidence/state_effects-sets-032.md#s-98b0ef7f5679f067)

### path-037988

```text
(config)# no cts sxp import-list <string> <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 50 `；EOL ` RVA 0x35A4DA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Import-list name。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-edc86fdb67e73efe](../../evidence/parameters-sets-018.md#p-edc86fdb67e73efe) · [状态效果 S-631f4eaa0ac89ea8](../../evidence/state_effects-sets-021.md#s-631f4eaa0ac89ea8)

### path-054421

```text
(config)# no cts sxp limit export peer-sequence-nodes <number:2..64> <cr>
```

Handler ` RVA 0x1322A0D0 `；selector ` 0 `；EOL ` RVA 0x35A4E358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enter number of nodes。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-d8786f70be9cbf6b](../../evidence/parameters-sets-016.md#p-d8786f70be9cbf6b) · [状态效果 S-cc40d2eabe5cfeda](../../evidence/state_effects-sets-043.md#s-cc40d2eabe5cfeda)

### path-027334

```text
(config)# no cwmp agent <cr>
```

Handler ` RVA 0x164722D0 `；selector ` 0 `；EOL ` RVA 0x35F8A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-025895

```text
(config)# no default-value data-character-bits <cr>
```

Handler ` RVA 0xE001B50 `；selector ` 1 `；EOL ` RVA 0x3411D2D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-df2e63ece91c6f59](../../evidence/conditions-sets-086.md#c-df2e63ece91c6f59) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-025881

```text
(config)# no default-value exec-character-bits <cr>
```

Handler ` RVA 0xE001B50 `；selector ` 3 `；EOL ` RVA 0x3411CFC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ca6d25d9e2b87aa1](../../evidence/conditions-sets-078.md#c-ca6d25d9e2b87aa1) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-025888

```text
(config)# no default-value special-character-bits <cr>
```

Handler ` RVA 0xE001B50 `；selector ` 2 `；EOL ` RVA 0x3411D038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7bfe861c4bbbbd98](../../evidence/conditions-sets-048.md#c-7bfe861c4bbbbd98) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-028039

```text
(config)# no define interface-range <string> <cr>
```

Handler ` RVA 0xE42FB80 `；selector ` 0 `；EOL ` RVA 0x3411B348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` macro definition。

[条件 C-25baea4e64042e23](../../evidence/conditions-sets-015.md#c-25baea4e64042e23) · [参数 P-589ed71e5b1ca069](../../evidence/parameters-sets-007.md#p-589ed71e5b1ca069) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-025933

```text
(config)# no device-tracking <cr>
```

Handler ` RVA 0x1368AFF0 `；selector ` 1123 `；EOL ` RVA 0x35BEACB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3172ce485a803527](../../evidence/conditions-sets-019.md#c-3172ce485a803527) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030566

```text
(config)# no device-tracking export oper-data <cr>
```

Handler ` RVA 0x13686E40 `；selector ` 0 `；EOL ` RVA 0x35BE6BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-071df3ba17dfca49](../../evidence/conditions-sets-003.md#c-071df3ba17dfca49) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027387

```text
(config)# no device-tracking full-proxy <cr>
```

Handler ` RVA 0x1367FFE0 `；selector ` 0 `；EOL ` RVA 0x35BE5D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e7f8492f656fd719](../../evidence/conditions-sets-090.md#c-e7f8492f656fd719) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-037252

```text
(config)# no device-tracking history ip disable <cr>
```

Handler ` RVA 0x13687A40 `；selector ` 0 `；EOL ` RVA 0x35BE6558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-532f9aa651754443](../../evidence/conditions-sets-033.md#c-532f9aa651754443) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-037292

```text
(config)# no device-tracking history ip length <cr>
```

Handler ` RVA 0x13687950 `；selector ` 0 `；EOL ` RVA 0x35BE6860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-77f068e582f284e8](../../evidence/conditions-sets-047.md#c-77f068e582f284e8) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027416

```text
(config)# no device-tracking logging <cr>
```

Handler ` RVA 0x136800A0 `；selector ` 0 `；EOL ` RVA 0x35BE60D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4dc32716f5ca3606](../../evidence/conditions-sets-030.md#c-4dc32716f5ca3606) · [状态效果 S-cccad28655412ef6](../../evidence/state_effects-sets-043.md#s-cccad28655412ef6)

### path-030529

```text
(config)# no device-tracking policy <string> <cr>
```

Handler ` RVA 0x1368A1D0 `；selector ` 1100 `；EOL ` RVA 0x35BEA990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of the device-tracking policy。

[条件 C-42d6ea33c1b6ae7c](../../evidence/conditions-sets-026.md#c-42d6ea33c1b6ae7c) · [参数 P-d4137a6cee565ff9](../../evidence/parameters-sets-016.md#p-d4137a6cee565ff9) · [状态效果 S-c59139bd4c380353](../../evidence/state_effects-sets-042.md#s-c59139bd4c380353)

### path-037376

```text
(config)# no device-tracking service-support device-tracking-layer3 <number:0..7> <cr>
```

Handler ` RVA 0x13687B10 `；selector ` 0 `；EOL ` RVA 0x35BE7A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Support (0: none, 1:port, 2:vlan, 4:box, 7: all, ...)。

[条件 C-0eb82648614b7620](../../evidence/conditions-sets-006.md#c-0eb82648614b7620) · [参数 P-144d9d62b7320cef](../../evidence/parameters-sets-002.md#p-144d9d62b7320cef) · [状态效果 S-b3d701d028ce032a](../../evidence/state_effects-sets-038.md#s-b3d701d028ce032a)

### path-030590

```text
(config)# no device-tracking tdl dhcp-stats <cr>
```

Handler ` RVA 0x13687530 `；selector ` 0 `；EOL ` RVA 0x35BE6F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4dc32716f5ca3606](../../evidence/conditions-sets-030.md#c-4dc32716f5ca3606) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-037371

```text
(config)# no device-tracking tdl disable dhcp-faults <cr>
```

Handler ` RVA 0x13687350 `；selector ` 0 `；EOL ` RVA 0x35BE7338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6aebcd79d377a1b2](../../evidence/conditions-sets-041.md#c-6aebcd79d377a1b2) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027377

```text
(config)# no device-tracking tracking <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1005 `；EOL ` RVA 0x35BE9FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4770cd6da8bbd6fd](../../evidence/conditions-sets-028.md#c-4770cd6da8bbd6fd) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030484

```text
(config)# no device-tracking tracking auto-source <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1010 `；EOL ` RVA 0x35BE9C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3603958eee98073f](../../evidence/conditions-sets-021.md#c-3603958eee98073f) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030509

```text
(config)# no device-tracking tracking retry-interval <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1006 `；EOL ` RVA 0x35BEA050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-018e5e959d5ba8ea](../../evidence/conditions-sets-001.md#c-018e5e959d5ba8ea) · [状态效果 S-93636dd84f46ed4d](../../evidence/state_effects-sets-031.md#s-93636dd84f46ed4d)

### path-030450

```text
(config)# no device-tracking unit-test bulk-sync <cr>
```

Handler ` RVA 0x13685F80 `；selector ` 0 `；EOL ` RVA 0x35BDDD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-054059

```text
(config)# no device-tracking unit-test check-reach vlan <number:0..4096> <address> <cr>
```

Handler ` RVA 0x136868D0 `；selector ` 0 `；EOL ` RVA 0x35BDF0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number；` address ` IPv6 address。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-eda4c24d6d5d3762](../../evidence/parameters-sets-018.md#p-eda4c24d6d5d3762) · [状态效果 S-821ae497ff07cfe1](../../evidence/state_effects-sets-028.md#s-821ae497ff07cfe1)

### path-030961

```text
(config)# no device-tracking unit-test disable-cli-sync <cr>
```

Handler ` RVA 0x13686B70 `；selector ` 0 `；EOL ` RVA 0x35BE4D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-046900

```text
(config)# no device-tracking unit-test dna vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685460 `；selector ` 0 `；EOL ` RVA 0x35BDFF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-20d6f79d28b3e5cb](../../evidence/parameters-sets-003.md#p-20d6f79d28b3e5cb) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-057956

```text
(config)# no device-tracking unit-test ha-sync-msg msg-type bt-entry action enable <cr>
```

Handler ` RVA 0x13686A80 `；selector ` 0 `；EOL ` RVA 0x35BE4560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-b2378ef6408024dc](../../evidence/state_effects-sets-038.md#s-b2378ef6408024dc)

### path-046906

```text
(config)# no device-tracking unit-test ip-dhcp-snooping vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13684D10 `；selector ` 0 `；EOL ` RVA 0x35BE1310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-90e7043ba98afd5f](../../evidence/parameters-sets-011.md#p-90e7043ba98afd5f) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-046977

```text
(config)# no device-tracking unit-test lisp-dt vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13681C10 `；selector ` 0 `；EOL ` RVA 0x35BE16C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-10f24bfd0d125ead](../../evidence/parameters-sets-002.md#p-10f24bfd0d125ead) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030733

```text
(config)# no device-tracking unit-test pgm <cr>
```

Handler ` RVA 0x13680F90 `；selector ` 0 `；EOL ` RVA 0x35BE0538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-046845

```text
(config)# no device-tracking unit-test profile vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13680F50 `；selector ` 0 `；EOL ` RVA 0x35BE0A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-efdb3cde321c553e](../../evidence/parameters-sets-018.md#p-efdb3cde321c553e) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-047178

```text
(config)# no device-tracking unit-test reapply-filters vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685FF0 `；selector ` 0 `；EOL ` RVA 0x35BE49E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-139592a46b415c0d](../../evidence/parameters-sets-002.md#p-139592a46b415c0d) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-059836

```text
(config)# no device-tracking unit-test replace-policy vlan <number:1..4096> old <string> new <string> <cr>
```

Handler ` RVA 0x13685820 `；selector ` 0 `；EOL ` RVA 0x35BDF9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number；` string ` old Policy name；` string ` new Policy name。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-38fe206d4babd853](../../evidence/parameters-sets-005.md#p-38fe206d4babd853) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030752

```text
(config)# no device-tracking unit-test upgm <cr>
```

Handler ` RVA 0x13680B60 `；selector ` 0 `；EOL ` RVA 0x35BE0EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-037345

```text
(config)# no device-tracking unlock policy <string> <cr>
```

Handler ` RVA 0x1368B2C0 `；selector ` 0 `；EOL ` RVA 0x35BE76A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Policy name。

[条件 C-2c4ff5fbef360ca7](../../evidence/conditions-sets-017.md#c-2c4ff5fbef360ca7) · [参数 P-df524c1964bb3064](../../evidence/parameters-sets-017.md#p-df524c1964bb3064) · [状态效果 S-f6a257851a98b2d1](../../evidence/state_effects-sets-052.md#s-f6a257851a98b2d1)

### path-027374

```text
(config)# no device-tracking upgrade-cli <cr>
```

Handler ` RVA 0x13689E20 `；selector ` 0 `；EOL ` RVA 0x35BEA5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4770cd6da8bbd6fd](../../evidence/conditions-sets-028.md#c-4770cd6da8bbd6fd) · [状态效果 S-504297964d434465](../../evidence/state_effects-sets-018.md#s-504297964d434465)

### path-031277

```text
(config)# no diagnostic cns publish <cr>
```

Handler ` RVA 0x159C30A0 `；selector ` 1 `；EOL ` RVA 0x35DD3758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-48d534200a9a2250](../../evidence/conditions-sets-029.md#c-48d534200a9a2250) · [状态效果 S-618c6f71b8b15306](../../evidence/state_effects-sets-021.md#s-618c6f71b8b15306)

### path-031139

```text
(config)# no diagnostic event-log size <cr>
```

Handler ` RVA 0xEB6AA60 `；selector ` 0 `；EOL ` RVA 0x343BC1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4297bee1dc906336](../../evidence/conditions-sets-026.md#c-4297bee1dc906336) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027553

```text
(config)# no diagnostic level <cr>
```

Handler ` RVA 0xEB67CD0 `；selector ` 0 `；EOL ` RVA 0x343BC690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f51b74bc2cf1888a](../../evidence/conditions-sets-095.md#c-f51b74bc2cf1888a) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-031253

```text
(config)# no diagnostic monitor global <cr>
```

Handler ` RVA 0xEB68B30 `；selector ` 16 `；EOL ` RVA 0x343BCE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-349bfff1b788f2e1](../../evidence/conditions-sets-020.md#c-349bfff1b788f2e1) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-031188

```text
(config)# no diagnostic monitor syslog <cr>
```

Handler ` RVA 0xEB67E60 `；selector ` 8 `；EOL ` RVA 0x343BCAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-35826832df598b30](../../evidence/conditions-sets-021.md#c-35826832df598b30) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-031120

```text
(config)# no diagnostic soft-error recovery <cr>
```

Handler ` RVA 0xEB6AB70 `；selector ` 0 `；EOL ` RVA 0x343BBD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6bce88cfca175c7e](../../evidence/conditions-sets-042.md#c-6bce88cfca175c7e) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-036474

```text
(config)# no diameter attribute list <number:0..99> <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 6 `；EOL ` RVA 0x338A66E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` attribute list number。

[条件 C-9a117866ea358fbe](../../evidence/conditions-sets-060.md#c-9a117866ea358fbe) · [参数 P-356573e8ba146437](../../evidence/parameters-sets-005.md#p-356573e8ba146437) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030327

```text
(config)# no diameter gx retransmit <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 32 `；EOL ` RVA 0x338A8160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9dba353a642939aa](../../evidence/conditions-sets-061.md#c-9dba353a642939aa) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030371

```text
(config)# no diameter gx subscription-id-type <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 37 `；EOL ` RVA 0x338A87D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb662ac050e0ec56](../../evidence/conditions-sets-097.md#c-fb662ac050e0ec56) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030353

```text
(config)# no diameter gx tx-timer <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 33 `；EOL ` RVA 0x338A84B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6281cca5ba2d0881](../../evidence/conditions-sets-038.md#c-6281cca5ba2d0881) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030232

```text
(config)# no diameter origin host <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 0 `；EOL ` RVA 0x338A7230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a3d08e0dd17f39c4](../../evidence/conditions-sets-063.md#c-a3d08e0dd17f39c4) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030195

```text
(config)# no diameter origin realm <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 1 `；EOL ` RVA 0x338A6F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bd2ade63c64b17e4](../../evidence/conditions-sets-073.md#c-bd2ade63c64b17e4) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030249

```text
(config)# no diameter peer <string> <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 4 `；EOL ` RVA 0x338A7DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name for the diameter peer configuration。

[条件 C-79108cf80a05c775](../../evidence/conditions-sets-047.md#c-79108cf80a05c775) · [参数 P-00e60acb19f32338](../../evidence/parameters-sets-001.md#p-00e60acb19f32338) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027192

```text
(config)# no diameter redundancy <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 24 `；EOL ` RVA 0x338A6388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-79108cf80a05c775](../../evidence/conditions-sets-047.md#c-79108cf80a05c775) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-030155

```text
(config)# no diameter timer connection <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 3 `；EOL ` RVA 0x338A6AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-96b29e997a15b9ea](../../evidence/conditions-sets-058.md#c-96b29e997a15b9ea) · [状态效果 S-8c5429013467c20f](../../evidence/state_effects-sets-030.md#s-8c5429013467c20f)

### path-036678

```text
(config)# no diameter vendor supported vodafone <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 15 `；EOL ` RVA 0x338A79D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-79108cf80a05c775](../../evidence/conditions-sets-047.md#c-79108cf80a05c775) · [状态效果 S-8d331211ad8d797b](../../evidence/state_effects-sets-030.md#s-8d331211ad8d797b)

### path-026892

```text
(config)# no dlsw allroute-netbios <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 6 `；EOL ` RVA 0x354D7A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026863

```text
(config)# no dlsw allroute-sna <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 5 `；EOL ` RVA 0x354D7798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029283

```text
(config)# no dlsw bridge-group <number:1..255> <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 8 `；EOL ` RVA 0x354D6BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Assign a Bridge Group to be assigned to DLSw。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [参数 P-69e4dfacabd25d76](../../evidence/parameters-sets-008.md#p-69e4dfacabd25d76) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026766

```text
(config)# no dlsw cache-ignore-netbios-datagram <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 12 `；EOL ` RVA 0x354D49F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026966

```text
(config)# no dlsw circuit-keepalives <cr>
```

Handler ` RVA 0x11453220 `；selector ` 0 `；EOL ` RVA 0x354D92D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026931

```text
(config)# no dlsw disable <cr>
```

Handler ` RVA 0x11421B20 `；selector ` 0 `；EOL ` RVA 0x354D8B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026598

```text
(config)# no dlsw duplicate-path-bias <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 0 `；EOL ` RVA 0x354D01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-11b987fae4e10b42](../../evidence/conditions-sets-007.md#c-11b987fae4e10b42) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029153

```text
(config)# no dlsw explorerQ-depth <number:10..1000> <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 1 `；EOL ` RVA 0x354D4DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Maximum Depth of explorer queue in packets。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [参数 P-21aea01164806436](../../evidence/parameters-sets-003.md#p-21aea01164806436) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026492

```text
(config)# no dlsw fast-hpr-support <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 10 `；EOL ` RVA 0x354CDD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029766

```text
(config)# no dlsw group-cache disable <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 8 `；EOL ` RVA 0x354DAE08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029830

```text
(config)# no dlsw group-cache enable <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 9 `；EOL ` RVA 0x354DB0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027147

```text
(config)# no dlsw group-cache max-entries <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 10 `；EOL ` RVA 0x354DB0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8aea76509648bd56](../../evidence/conditions-sets-054.md#c-8aea76509648bd56) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026993

```text
(config)# no dlsw history-log <cr>
```

Handler ` RVA 0x11421E20 `；selector ` 0 `；EOL ` RVA 0x354D8EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a917368bc28a3c33](../../evidence/conditions-sets-065.md#c-a917368bc28a3c33) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-028701

```text
(config)# no dlsw icanreach mac-exclusive <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 3 `；EOL ` RVA 0x354D2E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-67a40f4ca4c01f53](../../evidence/state_effects-sets-022.md#s-67a40f4ca4c01f53)

### path-029721

```text
(config)# no dlsw llc2 nornr <cr>
```

Handler ` RVA 0x11421D80 `；selector ` 1 `；EOL ` RVA 0x354DAB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026642

```text
(config)# no dlsw load-balance <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 0 `；EOL ` RVA 0x354D0530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a480a1fbe2169e64](../../evidence/conditions-sets-063.md#c-a480a1fbe2169e64) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026425

```text
(config)# no dlsw local-peer <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 0 `；EOL ` RVA 0x354CC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-59802ca74bb6b1b9](../../evidence/conditions-sets-035.md#c-59802ca74bb6b1b9) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-044900

```text
(config)# no dlsw mac-addr <address> ring <number:0..4095> <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 3 `；EOL ` RVA 0x354D52C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` MAC Address；` unsigned_number ` Ring number。

[条件 C-7e7058e191dfb0f0](../../evidence/conditions-sets-049.md#c-7e7058e191dfb0f0) · [参数 P-ea4dae8e32906a28](../../evidence/parameters-sets-018.md#p-ea4dae8e32906a28) · [状态效果 S-e271f85798594160](../../evidence/state_effects-sets-048.md#s-e271f85798594160)

### path-044901

```text
(config)# no dlsw mac-addr <address> ring <number:0..4095> <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 4 `；EOL ` RVA 0x354D52E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` MAC Address；` unsigned_number ` Ring number。

[条件 C-ecade62fa96a3043](../../evidence/conditions-sets-091.md#c-ecade62fa96a3043) · [参数 P-ea4dae8e32906a28](../../evidence/parameters-sets-018.md#p-ea4dae8e32906a28) · [状态效果 S-e271f85798594160](../../evidence/state_effects-sets-048.md#s-e271f85798594160)

### path-025727

```text
(config)# no dlsw max-multiple-rifs <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 11 `；EOL ` RVA 0x354D3A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f433582e61a5f755](../../evidence/conditions-sets-094.md#c-f433582e61a5f755) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027099

```text
(config)# no dlsw multicast <cr>
```

Handler ` RVA 0x11418A50 `；selector ` 0 `；EOL ` RVA 0x354DA828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026449

```text
(config)# no dlsw netbios-cache-length <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 11 `；EOL ` RVA 0x354CD710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4342ded10172eb9c](../../evidence/conditions-sets-026.md#c-4342ded10172eb9c) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027010

```text
(config)# no dlsw netbios-keepalive-filter <cr>
```

Handler ` RVA 0x11418A90 `；selector ` 1 `；EOL ` RVA 0x354D9820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026754

```text
(config)# no dlsw peer-log-changes <cr>
```

Handler ` RVA 0x11418C10 `；selector ` 0 `；EOL ` RVA 0x354D41D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-97a5428e46aa381d](../../evidence/conditions-sets-059.md#c-97a5428e46aa381d) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026875

```text
(config)# no dlsw peer-on-demand-defaults <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 5 `；EOL ` RVA 0x354D5C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e4cb71c32645845e](../../evidence/conditions-sets-088.md#c-e4cb71c32645845e) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026952

```text
(config)# no dlsw prom-peer-defaults <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 9 `；EOL ` RVA 0x354D7DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-82c284d1e515d2df](../../evidence/conditions-sets-051.md#c-82c284d1e515d2df) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026713

```text
(config)# no dlsw redundant-rings <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 13 `；EOL ` RVA 0x354D3AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49272d0dd3d382bc](../../evidence/conditions-sets-029.md#c-49272d0dd3d382bc) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-044520

```text
(config)# no dlsw remote-peer <number:0..4095> tcp <address> <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 1 `；EOL ` RVA 0x354D0A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Remote peer ring group list；` address ` Remote peer IP address。

[条件 C-a287739b99cf5238](../../evidence/conditions-sets-063.md#c-a287739b99cf5238) · [参数 P-4abb61377bb7ea27](../../evidence/parameters-sets-006.md#p-4abb61377bb7ea27) · [状态效果 S-02fc834db3551208](../../evidence/state_effects-sets-001.md#s-02fc834db3551208)

### path-026603

```text
(config)# no dlsw rsvp <cr>
```

Handler ` RVA 0x114938E0 `；selector ` 0 `；EOL ` RVA 0x354CFDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-002371138019fa6c](../../evidence/conditions-sets-001.md#c-002371138019fa6c) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026443

```text
(config)# no dlsw snmp-traps-extended <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 12 `；EOL ` RVA 0x354CDA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026722

```text
(config)# no dlsw tbridge-maxmtu-4472 <cr>
```

Handler ` RVA 0x11418B90 `；selector ` 0 `；EOL ` RVA 0x354D44A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-028505

```text
(config)# no dlsw timer sna-explorer-timeout <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 2 `；EOL ` RVA 0x354CF0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-564e4b402515b7b2](../../evidence/conditions-sets-034.md#c-564e4b402515b7b2) · [状态效果 S-cda75aa5657ea979](../../evidence/state_effects-sets-044.md#s-cda75aa5657ea979)

### path-029579

```text
(config)# no dlsw tos disable <cr>
```

Handler ` RVA 0x11418AD0 `；selector ` 0 `；EOL ` RVA 0x354D9B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-029748

```text
(config)# no dlsw tos map <cr>
```

Handler ` RVA 0x11418AD0 `；selector ` 1 `；EOL ` RVA 0x354D9E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7dc396bca06e06e1](../../evidence/conditions-sets-049.md#c-7dc396bca06e06e1) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-027046

```text
(config)# no dlsw tos-disable <cr>
```

Handler ` RVA 0x11418AD0 `；selector ` 2 `；EOL ` RVA 0x354DA4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-028532

```text
(config)# no dlsw touch-timer touch-nb-cache-timeout <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 7 `；EOL ` RVA 0x354CF9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-79527f3c75096a8e](../../evidence/conditions-sets-047.md#c-79527f3c75096a8e) · [状态效果 S-5cda7f6d75181adc](../../evidence/state_effects-sets-020.md#s-5cda7f6d75181adc)

### path-029820

```text
(config)# no dlsw transparent switch-support <cr>
```

Handler ` RVA 0x11418B10 `；selector ` 1 `；EOL ` RVA 0x354DB638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026989

```text
(config)# no dlsw udp-disable <cr>
```

Handler ` RVA 0x11418B50 `；selector ` 0 `；EOL ` RVA 0x354D9578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026743

```text
(config)# no dlsw xid-modify-tws <cr>
```

Handler ` RVA 0x11418BD0 `；selector ` 0 `；EOL ` RVA 0x354D4750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-026899

```text
(config)# no dnsix-dmdp retries <cr>
```

Handler ` RVA 0xD4A1FB0 `；selector ` 0 `；EOL ` RVA 0x33E567E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6b9db6e372ac4d0d](../../evidence/conditions-sets-042.md#c-6b9db6e372ac4d0d) · [状态效果 S-619cafda8e71ce11](../../evidence/state_effects-sets-021.md#s-619cafda8e71ce11)

### path-026921

```text
(config)# no dnsix-nat source <cr>
```

Handler ` RVA 0xD4A31F0 `；selector ` 0 `；EOL ` RVA 0x33E56B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4efb8ba594ef957d](../../evidence/conditions-sets-031.md#c-4efb8ba594ef957d) · [状态效果 S-877114362551788d](../../evidence/state_effects-sets-029.md#s-877114362551788d)

### path-026358

```text
(config)# no do-exec <number:1..99> <cr>
```

Handler ` RVA 0xDE857D0 `；selector ` 1 `；EOL ` RVA 0x34186F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Session number to resume。

[条件 C-389cecc55b15fe86](../../evidence/conditions-sets-022.md#c-389cecc55b15fe86) · [参数 P-5a2136bf20667e61](../../evidence/parameters-sets-007.md#p-5a2136bf20667e61) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-025994

```text
(config)# no do-exec <string> <cr>
```

Handler ` RVA 0xDEF32B0 `；selector ` 0 `；EOL ` RVA 0x340BB4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Exec Command。

[条件 C-41fd7b67705d8a48](../../evidence/conditions-sets-026.md#c-41fd7b67705d8a48) · [参数 P-bf6e24cec82cb154](../../evidence/parameters-sets-015.md#p-bf6e24cec82cb154) · [状态效果 S-111c9a6e5266b334](../../evidence/state_effects-sets-004.md#s-111c9a6e5266b334)

### path-034329

```text
(config)# no do-exec aaa tools memleak-detection-start <cr>
```

Handler ` RVA 0x1371EB80 `；selector ` 0 `；EOL ` RVA 0x35C0E758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026807

```text
(config)# no do-exec access-enable <cr>
```

Handler ` RVA 0xCEEEEA0 `；selector ` 0 `；EOL ` RVA 0x33D2ACF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fe511de0c1967cce](../../evidence/conditions-sets-098.md#c-fe511de0c1967cce) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026834

```text
(config)# no do-exec access-profile <cr>
```

Handler ` RVA 0xDD24680 `；selector ` 0 `；EOL ` RVA 0x34043248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-7bdbd391cdc8586d](../../evidence/state_effects-sets-026.md#s-7bdbd391cdc8586d)

### path-045046

```text
(config)# no do-exec access-session remote-device-notification mac <address> <cr>
```

Handler ` RVA 0xCADCD00 `；selector ` 0 `；EOL ` RVA 0x33B9B6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` MAC address。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a31f1e1a4ace1062](../../evidence/parameters-sets-012.md#p-a31f1e1a4ace1062) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052676

```text
(config)# no do-exec access-template <number:100..199> <string> any any <cr>
```

Handler ` RVA 0xCEEFAE0 `；selector ` 0 `；EOL ` RVA 0x33D2A758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IP extended access list；` string ` Name of Temp. list within the access-list。

[条件 C-fe511de0c1967cce](../../evidence/conditions-sets-098.md#c-fe511de0c1967cce) · [参数 P-2160701221db188a](../../evidence/parameters-sets-003.md#p-2160701221db188a) · [状态效果 S-5e439e36412f2c46](../../evidence/state_effects-sets-020.md#s-5e439e36412f2c46)

### path-028136

```text
(config)# no do-exec acm confirm-commit <cr>
```

Handler ` RVA 0xDED7A40 `；selector ` 0 `；EOL ` RVA 0x34095218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-6dd86e8b30065ae4](../../evidence/state_effects-sets-023.md#s-6dd86e8b30065ae4)

### path-030611

```text
(config)# no do-exec alps update-circuits <cr>
```

Handler ` RVA 0x11217A80 `；selector ` 0 `；EOL ` RVA 0x3541A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-030504

```text
(config)# no do-exec archive config <cr>
```

Handler ` RVA 0xDEDE440 `；selector ` 0 `；EOL ` RVA 0x3409A0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057769

```text
(config)# no do-exec archive log config add comment <string> <cr>
```

Handler ` RVA 0xDF0B3A0 `；selector ` 0 `；EOL ` RVA 0x340A35A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Comment (up to 128 characters)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3088f7718888ec37](../../evidence/parameters-sets-004.md#p-3088f7718888ec37) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046659

```text
(config)# no do-exec archive tar /table <string> <cr>
```

Handler ` RVA 0xD663D40 `；selector ` 0 `；EOL ` RVA 0x33EBD5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Tar filename。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2418664fd9d768d1](../../evidence/parameters-sets-003.md#p-2418664fd9d768d1) · [状态效果 S-6df01b162a0319fd](../../evidence/state_effects-sets-023.md#s-6df01b162a0319fd)

### path-036068

```text
(config)# no do-exec authentication display config-mode <cr>
```

Handler ` RVA 0xCB10230 `；selector ` 0 `；EOL ` RVA 0x33BB23E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036229

```text
(config)# no do-exec authentication display legacy <cr>
```

Handler ` RVA 0xCB102D0 `；selector ` 0 `；EOL ` RVA 0x33BB26C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-66ac7ba3aad392f3](../../evidence/conditions-sets-040.md#c-66ac7ba3aad392f3) · [状态效果 S-16bdee2bd832b32d](../../evidence/state_effects-sets-005.md#s-16bdee2bd832b32d)

### path-028243

```text
(config)# no do-exec auto secure <cr>
```

Handler ` RVA 0xB246A80 `；selector ` 0 `；EOL ` RVA 0x336D4B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8b2890c9b18dd7a](../../evidence/conditions-sets-077.md#c-c8b2890c9b18dd7a) · [状态效果 S-4980fd65ba7cd8c7](../../evidence/state_effects-sets-016.md#s-4980fd65ba7cd8c7)

### path-036344

```text
(config)# no do-exec beep kill session <cr>
```

Handler ` RVA 0xEF60A30 `；selector ` 1 `；EOL ` RVA 0x3448C338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-030189

```text
(config)# no do-exec bingd stop <cr>
```

Handler ` RVA 0xF2731C0 `；selector ` 0 `；EOL ` RVA 0x345DDD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a43a5a94eb877d2](../../evidence/conditions-sets-004.md#c-0a43a5a94eb877d2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036663

```text
(config)# no do-exec bingd template <string> <cr>
```

Handler ` RVA 0xF272D80 `；selector ` 0 `；EOL ` RVA 0x345DD688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` beep template to be used。

[条件 C-958be3c8e13e9651](../../evidence/conditions-sets-058.md#c-958be3c8e13e9651) · [参数 P-74a8a6af26414404](../../evidence/parameters-sets-009.md#p-74a8a6af26414404) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036759

```text
(config)# no do-exec bingng template <string> <cr>
```

Handler ` RVA 0xF272900 `；selector ` 0 `；EOL ` RVA 0x345DC9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` beep template to be used。

[条件 C-4738ea267c8b20c5](../../evidence/conditions-sets-028.md#c-4738ea267c8b20c5) · [参数 P-333ae3065c8daf82](../../evidence/parameters-sets-004.md#p-333ae3065c8daf82) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046897

```text
(config)# no do-exec bulkstat profile <string> disable <cr>
```

Handler ` RVA 0xBC6B6A0 `；selector ` 0 `；EOL ` RVA 0x338819A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of profile。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-feb2bca4df1d2854](../../evidence/parameters-sets-019.md#p-feb2bca4df1d2854) · [状态效果 S-5a99f626c7546901](../../evidence/state_effects-sets-020.md#s-5a99f626c7546901)

### path-046899

```text
(config)# no do-exec bulkstat profile <string> enable repeat <number:1..4294967294> <cr>
```

Handler ` RVA 0xBC6B6A0 `；selector ` 3 `；EOL ` RVA 0x33881C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of profile；` unsigned_number ` Number of recurrences。

[条件 C-2c55ea67ecdfc4f2](../../evidence/conditions-sets-017.md#c-2c55ea67ecdfc4f2) · [参数 P-b7570e5ddb9c6525](../../evidence/parameters-sets-014.md#p-b7570e5ddb9c6525) · [状态效果 S-6d4ea24ff75485ce](../../evidence/state_effects-sets-023.md#s-6d4ea24ff75485ce)

### path-052583

```text
(config)# no do-exec call-home debug syslog-throttling timer <number:1..86400> <cr>
```

Handler ` RVA 0xB6D4AC0 `；selector ` 0 `；EOL ` RVA 0x337F1D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-241964126de341c2](../../evidence/conditions-sets-014.md#c-241964126de341c2) · [参数 P-4c50fed8d94ed394](../../evidence/parameters-sets-006.md#p-4c50fed8d94ed394) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044826

```text
(config)# no do-exec call-home diagnostic-signature deinstall <number:1..99999999> <cr>
```

Handler ` RVA 0x128FF210 `；selector ` 0 `；EOL ` RVA 0x337F28E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-590f69f5c012b06f](../../evidence/parameters-sets-007.md#p-590f69f5c012b06f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044770

```text
(config)# no do-exec call-home diagnostic-signature deinstall all <cr>
```

Handler ` RVA 0x128FF210 `；selector ` 1 `；EOL ` RVA 0x337F2638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044779

```text
(config)# no do-exec call-home diagnostic-signature download <number:1..99999999> <cr>
```

Handler ` RVA 0x128FEFD0 `；selector ` 0 `；EOL ` RVA 0x337F2338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-40c651dff0cca626](../../evidence/parameters-sets-005.md#p-40c651dff0cca626) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044720

```text
(config)# no do-exec call-home diagnostic-signature download all <cr>
```

Handler ` RVA 0x128FEFD0 `；selector ` 1 `；EOL ` RVA 0x337F2088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044814

```text
(config)# no do-exec call-home diagnostic-signature install <number:1..99999999> <cr>
```

Handler ` RVA 0x128FF0B0 `；selector ` 0 `；EOL ` RVA 0x337F2BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-1b6032225704560d](../../evidence/parameters-sets-003.md#p-1b6032225704560d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044854

```text
(config)# no do-exec call-home diagnostic-signature load <string> <cr>
```

Handler ` RVA 0x128FF300 `；selector ` 0 `；EOL ` RVA 0x337F2EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` DS file name。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-2bddbfb1f7b5c021](../../evidence/parameters-sets-004.md#p-2bddbfb1f7b5c021) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052577

```text
(config)# no do-exec call-home request config-sanity profile <string> <cr>
```

Handler ` RVA 0xB6D4930 `；selector ` 0 `；EOL ` RVA 0x337F1150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile name to use for call-home request。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3109956af5f1aef4](../../evidence/parameters-sets-004.md#p-3109956af5f1aef4) · [状态效果 S-4478411e25530b87](../../evidence/state_effects-sets-015.md#s-4478411e25530b87)

### path-035396

```text
(config)# no do-exec call-home request registration-info <cr>
```

Handler ` RVA 0xB6D4B70 `；selector ` 0 `；EOL ` RVA 0x337F1820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-59f5c9434bb9c973](../../evidence/conditions-sets-035.md#c-59f5c9434bb9c973) · [状态效果 S-b9157093094901b1](../../evidence/state_effects-sets-039.md#s-b9157093094901b1)

### path-052612

```text
(config)# no do-exec call-home send <string> email <string> <cr>
```

Handler ` RVA 0xB6D4310 `；selector ` 0 `；EOL ` RVA 0x337F07A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IOS exec command；` string ` Receiver's email address。

[条件 C-27805f0d3d956c98](../../evidence/conditions-sets-016.md#c-27805f0d3d956c98) · [参数 P-f743d2b9800ce8a1](../../evidence/parameters-sets-018.md#p-f743d2b9800ce8a1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052748

```text
(config)# no do-exec call-home send <string> tac-service-request <string> <cr>
```

Handler ` RVA 0xB6D4310 `；selector ` 0 `；EOL ` RVA 0x337EF6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IOS exec CLIs list (1-127) characters, each CLI seperated by ';'.You must enclose your CLIs list in double quotes ；` string ` TAC service request number。

[条件 C-d3ed586eb9b5a8aa](../../evidence/conditions-sets-082.md#c-d3ed586eb9b5a8aa) · [参数 P-0700e2bf3f145040](../../evidence/parameters-sets-001.md#p-0700e2bf3f145040) · [状态效果 S-506207a55aa80c00](../../evidence/state_effects-sets-018.md#s-506207a55aa80c00)

### path-044622

```text
(config)# no do-exec call-home send alert-group configuration <cr>
```

Handler ` RVA 0xB6D39A0 `；selector ` 0 `；EOL ` RVA 0x337EEDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-821c1b18aa47637b](../../evidence/conditions-sets-050.md#c-821c1b18aa47637b) · [状态效果 S-c3b9b11c4883e5bd](../../evidence/state_effects-sets-041.md#s-c3b9b11c4883e5bd)

### path-052557

```text
(config)# no do-exec call-home test <string> profile <string> <cr>
```

Handler ` RVA 0xB6D3760 `；selector ` 0 `；EOL ` RVA 0x337F0C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Test message；` string ` Profile name to use for test message。

[条件 C-5ec21721dc9f537c](../../evidence/conditions-sets-037.md#c-5ec21721dc9f537c) · [参数 P-a026819f0ca18f5e](../../evidence/parameters-sets-012.md#p-a026819f0ca18f5e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027443

```text
(config)# no do-exec cd <cr>
```

Handler ` RVA 0xD657A00 `；selector ` 0 `；EOL ` RVA 0x33EB9078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026078

```text
(config)# no do-exec clear <cr>
```

Handler ` RVA 0xE0062B0 `；selector ` 0 `；EOL ` RVA 0x3411F6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-13c9a48981117953](../../evidence/conditions-sets-008.md#c-13c9a48981117953) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054488

```text
(config)# no do-exec clear aaa cache filterserver acl <cr>
```

Handler ` RVA 0xCD2A390 `；selector ` 0 `；EOL ` RVA 0x3404BE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058045

```text
(config)# no do-exec clear aaa cache group <string> all <cr>
```

Handler ` RVA 0xDDEF640 `；selector ` 0 `；EOL ` RVA 0x3404C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Server group being cleared。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-65a6b53edc5dd687](../../evidence/parameters-sets-008.md#p-65a6b53edc5dd687) · [状态效果 S-9df0ebc5c40a9b19](../../evidence/state_effects-sets-034.md#s-9df0ebc5c40a9b19)

### path-047577

```text
(config)# no do-exec clear aaa counters clients <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 16 `；EOL ` RVA 0x3404B4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054484

```text
(config)# no do-exec clear aaa counters command handler <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 17 `；EOL ` RVA 0x3404B7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047600

```text
(config)# no do-exec clear aaa counters requests <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 25 `；EOL ` RVA 0x3404BA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054499

```text
(config)# no do-exec clear aaa counters servers all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 15 `；EOL ` RVA 0x3404B0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-f6cceb082ed6565d](../../evidence/state_effects-sets-052.md#s-f6cceb082ed6565d)

### path-047567

```text
(config)# no do-exec clear aaa local statistics <cr>
```

Handler ` RVA 0xD507150 `；selector ` 0 `；EOL ` RVA 0x33E71FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058049

```text
(config)# no do-exec clear aaa local user blocked all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 7 `；EOL ` RVA 0x33E71C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-65d9f93750302bbc](../../evidence/conditions-sets-039.md#c-65d9f93750302bbc) · [状态效果 S-2cfaaba3fa73c610](../../evidence/state_effects-sets-010.md#s-2cfaaba3fa73c610)

### path-058040

```text
(config)# no do-exec clear aaa local user fail-attempts all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 4 `；EOL ` RVA 0x33E718E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-0a78f72a6c41dca2](../../evidence/state_effects-sets-003.md#s-0a78f72a6c41dca2)

### path-058035

```text
(config)# no do-exec clear aaa local user lockout all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 3 `；EOL ` RVA 0x33E71550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5e6478d392b869f9](../../evidence/state_effects-sets-020.md#s-5e6478d392b869f9)

### path-047562

```text
(config)# no do-exec clear aaa tools memleak <cr>
```

Handler ` RVA 0x1371EAF0 `；selector ` 0 `；EOL ` RVA 0x35C0DDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034213

```text
(config)# no do-exec clear access-list counters <cr>
```

Handler ` RVA 0xE0AF0F0 `；selector ` 0 `；EOL ` RVA 0x341862A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dcbf105ca1b565dd](../../evidence/conditions-sets-085.md#c-dcbf105ca1b565dd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-043965

```text
(config)# no do-exec clear access-list fqdn statistics <cr>
```

Handler ` RVA 0xCF1C1A0 `；selector ` 0 `；EOL ` RVA 0x33D662E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057104

```text
(config)# no do-exec clear access-template <number:100..199> <string> any any <cr>
```

Handler ` RVA 0xCEEFED0 `；selector ` 0 `；EOL ` RVA 0x33D2CF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IP extended access list；` string ` Dynamic Access-list name。

[条件 C-8bc23a2a6ab20b85](../../evidence/conditions-sets-054.md#c-8bc23a2a6ab20b85) · [参数 P-f1f333f2758db219](../../evidence/parameters-sets-018.md#p-f1f333f2758db219) · [状态效果 S-8a0c5ccab48a2134](../../evidence/state_effects-sets-029.md#s-8a0c5ccab48a2134)

### path-028630

```text
(config)# no do-exec clear adjacency <cr>
```

Handler ` RVA 0xB5519E0 `；selector ` 0 `；EOL ` RVA 0x3379B228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039034

```text
(config)# no do-exec clear alps circuits <cr>
```

Handler ` RVA 0x11217960 `；selector ` 1 `；EOL ` RVA 0x3541CD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-e5aecac669036cfb](../../evidence/state_effects-sets-049.md#s-e5aecac669036cfb)

### path-038809

```text
(config)# no do-exec clear alps counters <cr>
```

Handler ` RVA 0x11217960 `；selector ` 0 `；EOL ` RVA 0x3541C9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047608

```text
(config)# no do-exec clear archive log config <cr>
```

Handler ` RVA 0xDF0B450 `；selector ` 0 `；EOL ` RVA 0x340CDF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034283

```text
(config)# no do-exec clear arp-cache <address> <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 1 `；EOL ` RVA 0x33CD7ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address。

[条件 C-bcdb9394ba16e4b9](../../evidence/conditions-sets-073.md#c-bcdb9394ba16e4b9) · [参数 P-86bbb0bf087473ac](../../evidence/parameters-sets-010.md#p-86bbb0bf087473ac) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028314

```text
(config)# no do-exec clear arp-cache <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 0 `；EOL ` RVA 0x33CD7B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3ecf6bdba30521bc](../../evidence/conditions-sets-024.md#c-3ecf6bdba30521bc) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044142

```text
(config)# no do-exec clear arp-cache counters ha <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 2 `；EOL ` RVA 0x33CD8210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-193872d6b0f1a2e9](../../evidence/conditions-sets-010.md#c-193872d6b0f1a2e9) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037217

```text
(config)# no do-exec clear avc sd-service <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 50 `；EOL ` RVA 0x3527DE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046493

```text
(config)# no do-exec clear avc sd-service cmds <cr>
```

Handler ` RVA 0x10DCF240 `；selector ` 0 `；EOL ` RVA 0x3527D8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046384

```text
(config)# no do-exec clear avc sd-service device-health <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 54 `；EOL ` RVA 0x3527D350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046547

```text
(config)# no do-exec clear avc sd-service device-table <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 51 `；EOL ` RVA 0x3527DB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9f2933ed5b542c9f](../../evidence/conditions-sets-062.md#c-9f2933ed5b542c9f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046444

```text
(config)# no do-exec clear avc sd-service ent-export <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 55 `；EOL ` RVA 0x3527D5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046314

```text
(config)# no do-exec clear avc sd-service flow-counters <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 53 `；EOL ` RVA 0x3527D0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a584d0e2cac5b048](../../evidence/conditions-sets-064.md#c-a584d0e2cac5b048) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053937

```text
(config)# no do-exec clear avc sd-service telemetry-table counters <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 52 `；EOL ` RVA 0x3527DE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-624c814ea19fcff8](../../evidence/conditions-sets-038.md#c-624c814ea19fcff8) · [状态效果 S-e34f2b7463f61422](../../evidence/state_effects-sets-048.md#s-e34f2b7463f61422)

### path-036213

```text
(config)# no do-exec clear bfd counters <cr>
```

Handler ` RVA 0x10B36A30 `；selector ` 0 `；EOL ` RVA 0x34CAD5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-865673e01ba891ba](../../evidence/state_effects-sets-028.md#s-865673e01ba891ba)

### path-036277

```text
(config)# no do-exec clear bfd dampening <cr>
```

Handler ` RVA 0x10B36A30 `；selector ` 1 `；EOL ` RVA 0x34CADBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-f61f2ec55017d68b](../../evidence/state_effects-sets-052.md#s-f61f2ec55017d68b)

### path-037511

```text
(config)# no do-exec clear bgp ipv4 <cr>
```

Handler ` RVA 0xF1C77B0 `；selector ` 0 `；EOL ` RVA 0x344AFD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0b3fb836298cfcdc](../../evidence/conditions-sets-005.md#c-0b3fb836298cfcdc) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-046778

```text
(config)# no do-exec clear bgp ipv4 cease <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 7 `；EOL ` RVA 0x344B0470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0b3fb836298cfcdc](../../evidence/conditions-sets-005.md#c-0b3fb836298cfcdc) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-046728

```text
(config)# no do-exec clear bgp ipv4 flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 6 `；EOL ` RVA 0x344B01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0b3fb836298cfcdc](../../evidence/conditions-sets-005.md#c-0b3fb836298cfcdc) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-046729

```text
(config)# no do-exec clear bgp ipv4 internal <cr>
```

Handler ` RVA 0xF1CD7B0 `；selector ` 0 `；EOL ` RVA 0x344B0730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9b8c1491af3eddcf](../../evidence/conditions-sets-060.md#c-9b8c1491af3eddcf) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-054161

```text
(config)# no do-exec clear bgp ipv4 update-group <number:1..4294967295> <cr>
```

Handler ` RVA 0xF1CA660 `；selector ` 0 `；EOL ` RVA 0x344B1160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Clear peers in the update-group。

[条件 C-020ae5108c3293f9](../../evidence/conditions-sets-001.md#c-020ae5108c3293f9) · [参数 P-37ab67deed9369de](../../evidence/parameters-sets-005.md#p-37ab67deed9369de) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-057843

```text
(config)# no do-exec clear bgp ipv4 vrf <string> dampening <cr>
```

Handler ` RVA 0xF1CB1C0 `；selector ` 0 `；EOL ` RVA 0x344B0AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-4acfc8da0ddc4619](../../evidence/conditions-sets-029.md#c-4acfc8da0ddc4619) · [参数 P-cd1f6e9647c25601](../../evidence/parameters-sets-016.md#p-cd1f6e9647c25601) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-057866

```text
(config)# no do-exec clear bgp ipv4 vrf <string> flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 2 `；EOL ` RVA 0x344B0D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-4acfc8da0ddc4619](../../evidence/conditions-sets-029.md#c-4acfc8da0ddc4619) · [参数 P-cd1f6e9647c25601](../../evidence/parameters-sets-016.md#p-cd1f6e9647c25601) · [状态效果 S-2f8e9ce21d3e78fd](../../evidence/state_effects-sets-011.md#s-2f8e9ce21d3e78fd)

### path-031396

```text
(config)# no do-exec clear bridge <cr>
```

Handler ` RVA 0xF28A710 `；selector ` 0 `；EOL ` RVA 0x345E44D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-697ee8398e2334de](../../evidence/conditions-sets-041.md#c-697ee8398e2334de) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044594

```text
(config)# no do-exec clear bridge-domain route stats <cr>
```

Handler ` RVA 0xBF37330 `；selector ` 0 `；EOL ` RVA 0x33953F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a78fd5ad38c3eaf9](../../evidence/conditions-sets-065.md#c-a78fd5ad38c3eaf9) · [状态效果 S-8176fc61823fe30e](../../evidence/state_effects-sets-027.md#s-8176fc61823fe30e)

### path-031520

```text
(config)# no do-exec clear bsc <cr>
```

Handler ` RVA 0x113C36A0 `；selector ` 0 `；EOL ` RVA 0x354B4B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-031552

```text
(config)# no do-exec clear bstun <cr>
```

Handler ` RVA 0x113E1220 `；selector ` 0 `；EOL ` RVA 0x354BCA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047212

```text
(config)# no do-exec clear call admission statistics <cr>
```

Handler ` RVA 0xDEB0A00 `；selector ` 0 `；EOL ` RVA 0x3408CD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5770bff7e45873f3](../../evidence/conditions-sets-034.md#c-5770bff7e45873f3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044621

```text
(config)# no do-exec clear call-home diagnostic-signature statistics <cr>
```

Handler ` RVA 0x128FF400 `；selector ` 0 `；EOL ` RVA 0x337F4010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-695d490b0b391d16](../../evidence/conditions-sets-041.md#c-695d490b0b391d16) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052512

```text
(config)# no do-exec clear call-home diagnostic-signature statistics download <cr>
```

Handler ` RVA 0x128FF460 `；selector ` 0 `；EOL ` RVA 0x337F3FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-695d490b0b391d16](../../evidence/conditions-sets-041.md#c-695d490b0b391d16) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044597

```text
(config)# no do-exec clear call-home smart-licensing statistics <cr>
```

Handler ` RVA 0xB6D3710 `；selector ` 0 `；EOL ` RVA 0x337F4568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-797a43e59bd3b809](../../evidence/conditions-sets-047.md#c-797a43e59bd3b809) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034754

```text
(config)# no do-exec clear call-home statistics <cr>
```

Handler ` RVA 0xB6D36C0 `；selector ` 0 `；EOL ` RVA 0x337F3C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035097

```text
(config)# no do-exec clear cdp counters <cr>
```

Handler ` RVA 0xCDA98F0 `；selector ` 0 `；EOL ` RVA 0x33CE01A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035159

```text
(config)# no do-exec clear cdp table <cr>
```

Handler ` RVA 0xCDA9940 `；selector ` 0 `；EOL ` RVA 0x33CE0450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044512

```text
(config)# no do-exec clear cef interface policy-statistics <cr>
```

Handler ` RVA 0xB3DDB50 `；selector ` 0 `；EOL ` RVA 0x337647B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-edbdbf9af3b2d05d](../../evidence/conditions-sets-092.md#c-edbdbf9af3b2d05d) · [状态效果 S-e91c1d231ed9fec3](../../evidence/state_effects-sets-049.md#s-e91c1d231ed9fec3)

### path-035188

```text
(config)# no do-exec clear cef linecard <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 3 `；EOL ` RVA 0x33733770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044839

```text
(config)# no do-exec clear cef linecard Adjacency <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 2 `；EOL ` RVA 0x33733748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044790

```text
(config)# no do-exec clear cef linecard Interface <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 1 `；EOL ` RVA 0x337334A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044741

```text
(config)# no do-exec clear cef linecard Prefix <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 0 `；EOL ` RVA 0x337331F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044638

```text
(config)# no do-exec clear cef linecard events <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 4 `；EOL ` RVA 0x33732ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044469

```text
(config)# no do-exec clear cef load-balance statistics <cr>
```

Handler ` RVA 0xB3F90A0 `；selector ` 0 `；EOL ` RVA 0x33764AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044760

```text
(config)# no do-exec clear cef table IPv4 <cr>
```

Handler ` RVA 0xB5C9AD0 `；selector ` 0 `；EOL ` RVA 0x337ADA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f9c385ba10038d1](../../evidence/conditions-sets-006.md#c-0f9c385ba10038d1) · [状态效果 S-e6b22e32e9505517](../../evidence/state_effects-sets-049.md#s-e6b22e32e9505517)

### path-052538

```text
(config)# no do-exec clear cef table IPv4 consistency-check <cr>
```

Handler ` RVA 0xB5C9A70 `；selector ` 0 `；EOL ` RVA 0x337AD630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7e2805c08fbc4fe8](../../evidence/conditions-sets-049.md#c-7e2805c08fbc4fe8) · [状态效果 S-e6b22e32e9505517](../../evidence/state_effects-sets-049.md#s-e6b22e32e9505517)

### path-036353

```text
(config)# no do-exec clear cft stats <cr>
```

Handler ` RVA 0x12945F20 `；selector ` 1 `；EOL ` RVA 0x358FD9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1632491c2ff8b76](../../evidence/conditions-sets-081.md#c-d1632491c2ff8b76) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034528

```text
(config)# no do-exec clear checkpoint clients <cr>
```

Handler ` RVA 0xCDB61A0 `；selector ` 0 `；EOL ` RVA 0x33CEE3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034480

```text
(config)# no do-exec clear checkpoint entities <cr>
```

Handler ` RVA 0xCDB63F0 `；selector ` 0 `；EOL ` RVA 0x33CEE138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034562

```text
(config)# no do-exec clear checkpoint statistics <cr>
```

Handler ` RVA 0xCDB6600 `；selector ` 0 `；EOL ` RVA 0x33CEE688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036140

```text
(config)# no do-exec clear class-map control <cr>
```

Handler ` RVA 0x10A5CC50 `；selector ` 0 `；EOL ` RVA 0x34C768B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e89804328378fef3](../../evidence/conditions-sets-090.md#c-e89804328378fef3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037476

```text
(config)# no do-exec clear clns cache <cr>
```

Handler ` RVA 0x10592040 `；selector ` 1 `；EOL ` RVA 0x34B6B560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037562

```text
(config)# no do-exec clear clns es-neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 2 `；EOL ` RVA 0x34B6BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037589

```text
(config)# no do-exec clear clns is-neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 3 `；EOL ` RVA 0x34B6BD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037631

```text
(config)# no do-exec clear clns neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 4 `；EOL ` RVA 0x34B6C000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037524

```text
(config)# no do-exec clear clns route <cr>
```

Handler ` RVA 0x10592040 `；selector ` 5 `；EOL ` RVA 0x34B6B808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037674

```text
(config)# no do-exec clear clns traffic <cr>
```

Handler ` RVA 0x10592040 `；selector ` 6 `；EOL ` RVA 0x34B6C2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047868

```text
(config)# no do-exec clear cns config stats <cr>
```

Handler ` RVA 0xF31ED20 `；selector ` 0 `；EOL ` RVA 0x34609B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038610

```text
(config)# no do-exec clear cns counters <cr>
```

Handler ` RVA 0xF2FE680 `；selector ` 0 `；EOL ` RVA 0x346051C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047820

```text
(config)# no do-exec clear cns event stats <cr>
```

Handler ` RVA 0xF35DEC0 `；selector ` 0 `；EOL ` RVA 0x34617250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047957

```text
(config)# no do-exec clear cns image connections <cr>
```

Handler ` RVA 0xF36DAA0 `；selector ` 0 `；EOL ` RVA 0x3461C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047904

```text
(config)# no do-exec clear cns image status <cr>
```

Handler ` RVA 0xF36D980 `；selector ` 0 `；EOL ` RVA 0x3461BDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034099

```text
(config)# no do-exec clear configuration lock <cr>
```

Handler ` RVA 0xDF3AC00 `；selector ` 0 `；EOL ` RVA 0x340B6170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-031308

```text
(config)# no do-exec clear control-plane <cr>
```

Handler ` RVA 0xE47F2B0 `；selector ` 0 `；EOL ` RVA 0x342C48C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034273

```text
(config)# no do-exec clear controller all <cr>
```

Handler ` RVA 0xECFC750 `；selector ` 0 `；EOL ` RVA 0x343F6970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-246b4b7c76529398](../../evidence/conditions-sets-014.md#c-246b4b7c76529398) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027961

```text
(config)# no do-exec clear counters <cr>
```

Handler ` RVA 0xE40DC10 `；selector ` 0 `；EOL ` RVA 0x3411FD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a24e4f16969ee72](../../evidence/conditions-sets-029.md#c-4a24e4f16969ee72) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047523

```text
(config)# no do-exec clear crypto autovpn session <cr>
```

Handler ` RVA 0x165EC340 `；selector ` 1 `；EOL ` RVA 0x35FA6D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058024

```text
(config)# no do-exec clear crypto autovpn session peer <number:1..2147483647> <cr>
```

Handler ` RVA 0x165EC340 `；selector ` 0 `；EOL ` RVA 0x35FA6DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Peerno。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-5d2397c60ef477d4](../../evidence/parameters-sets-007.md#p-5d2397c60ef477d4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047493

```text
(config)# no do-exec clear crypto ceal statistics <cr>
```

Handler ` RVA 0x120E8990 `；selector ` 0 `；EOL ` RVA 0x3579FA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-4c0b168c9344273e](../../evidence/state_effects-sets-017.md#s-4c0b168c9344273e)

### path-054489

```text
(config)# no do-exec clear crypto engine accelerator counter <cr>
```

Handler ` RVA 0x120CAC10 `；selector ` 0 `；EOL ` RVA 0x357920E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a8e49c9039b54cd7](../../evidence/conditions-sets-065.md#c-a8e49c9039b54cd7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047536

```text
(config)# no do-exec clear crypto ha statistics <cr>
```

Handler ` RVA 0x1924CF00 `；selector ` 0 `；EOL ` RVA 0x3697A7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-125918ebee950010](../../evidence/conditions-sets-007.md#c-125918ebee950010) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047460

```text
(config)# no do-exec clear crypto pki benchmarks <cr>
```

Handler ` RVA 0x120B7E10 `；selector ` 0 `；EOL ` RVA 0x35752EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047411

```text
(config)# no do-exec clear crypto pki counters <cr>
```

Handler ` RVA 0x11FC7870 `；selector ` 0 `；EOL ` RVA 0x35752C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-047505

```text
(config)# no do-exec clear crypto pki crl <cr>
```

Handler ` RVA 0x11F2ECF0 `；selector ` 0 `；EOL ` RVA 0x35753188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038200

```text
(config)# no do-exec clear cts credentials <cr>
```

Handler ` RVA 0x13047780 `；selector ` 0 `；EOL ` RVA 0x35A1D248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0648da1944570fa8](../../evidence/conditions-sets-003.md#c-0648da1944570fa8) · [状态效果 S-0866631b7e122be2](../../evidence/state_effects-sets-002.md#s-0866631b7e122be2)

### path-048244

```text
(config)# no do-exec clear cts role-based counters <cr>
```

Handler ` RVA 0x141FE9C0 `；selector ` 0 `；EOL ` RVA 0x35CFE5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-34ee87a193a0a00e](../../evidence/conditions-sets-021.md#c-34ee87a193a0a00e) · [状态效果 S-71538632f25eb588](../../evidence/state_effects-sets-024.md#s-71538632f25eb588)

### path-054320

```text
(config)# no do-exec clear device-tracking database policy <string> <cr>
```

Handler ` RVA 0x136806D0 `；selector ` 1020 `；EOL ` RVA 0x35BD6BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Snooping Policy name to be cleared。

[条件 C-3798f376b9381e80](../../evidence/conditions-sets-022.md#c-3798f376b9381e80) · [参数 P-e868e12c898fe3d6](../../evidence/parameters-sets-017.md#p-e868e12c898fe3d6) · [状态效果 S-0b22e94f6f6126b3](../../evidence/state_effects-sets-003.md#s-0b22e94f6f6126b3)

### path-037752

```text
(config)# no do-exec clear device-tracking events <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1021 `；EOL ` RVA 0x35BD7808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3798f376b9381e80](../../evidence/conditions-sets-022.md#c-3798f376b9381e80) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037805

```text
(config)# no do-exec clear device-tracking messages <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1022 `；EOL ` RVA 0x35BD7AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3798f376b9381e80](../../evidence/conditions-sets-022.md#c-3798f376b9381e80) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037659

```text
(config)# no do-exec clear dhcp-server-tracking database <cr>
```

Handler ` RVA 0x136A1FB0 `；selector ` 0 `；EOL ` RVA 0x35C01760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039041

```text
(config)# no do-exec clear diagnostic event-log <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cc2706f2b049ba7](../../evidence/conditions-sets-018.md#c-2cc2706f2b049ba7) · [状态效果 S-11a5bd9cdab40a50](../../evidence/state_effects-sets-004.md#s-11a5bd9cdab40a50)

### path-054679

```text
(config)# no do-exec clear diagnostic event-log slot all <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1b21cdc38c280145](../../evidence/conditions-sets-011.md#c-1b21cdc38c280145) · [状态效果 S-df584dce587d1898](../../evidence/state_effects-sets-047.md#s-df584dce587d1898)

### path-028370

```text
(config)# no do-exec clear dialer <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 0 `；EOL ` RVA 0x34666688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7630f1e5c0c96cbe](../../evidence/conditions-sets-046.md#c-7630f1e5c0c96cbe) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052264

```text
(config)# no do-exec clear dialer dnis group <string> <cr>
```

Handler ` RVA 0xF4E9360 `；selector ` 0 `；EOL ` RVA 0x34674518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` DNIS group name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-05f42c525d7c2f8f](../../evidence/parameters-sets-001.md#p-05f42c525d7c2f8f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052208

```text
(config)# no do-exec clear dialer dnis number <string> <cr>
```

Handler ` RVA 0xF4E9130 `；selector ` 1 `；EOL ` RVA 0x34673F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` DNIS number。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-a6076225f83e98fc](../../evidence/parameters-sets-013.md#p-a6076225f83e98fc) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056834

```text
(config)# no do-exec clear dialer dnis range <string> <string> <cr>
```

Handler ` RVA 0xF4E9130 `；selector ` 2 `；EOL ` RVA 0x34674258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` DNIS range start；` string ` DNIS range end。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-6ff2f7c7e2918e74](../../evidence/parameters-sets-009.md#p-6ff2f7c7e2918e74) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034375

```text
(config)# no do-exec clear dialer sessions <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 1 `；EOL ` RVA 0x34673BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-048825

```text
(config)# no do-exec clear diameter gx statistics <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 22 `；EOL ` RVA 0x338ADE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055062

```text
(config)# no do-exec clear diameter peer connection all <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 34 `；EOL ` RVA 0x338AD2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058307

```text
(config)# no do-exec clear diameter peer connection name <string> <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 21 `；EOL ` RVA 0x338AD598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Peer name。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [参数 P-ac0b956092f2b047](../../evidence/parameters-sets-013.md#p-ac0b956092f2b047) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-055099

```text
(config)# no do-exec clear diameter peer statistics all <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 36 `；EOL ` RVA 0x338AD870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058325

```text
(config)# no do-exec clear diameter peer statistics name <string> <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 35 `；EOL ` RVA 0x338ADB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Peer name。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [参数 P-56d578d820d5ba55](../../evidence/parameters-sets-007.md#p-56d578d820d5ba55) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038231

```text
(config)# no do-exec clear dlep counters <cr>
```

Handler ` RVA 0x132D3330 `；selector ` 3 `；EOL ` RVA 0x35A5A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d01143ef4c108a3f](../../evidence/conditions-sets-080.md#c-d01143ef4c108a3f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039157

```text
(config)# no do-exec clear dlsw reachability <cr>
```

Handler ` RVA 0x11421C60 `；selector ` 0 `；EOL ` RVA 0x354CC100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0af2364a1a48bd94](../../evidence/conditions-sets-005.md#c-0af2364a1a48bd94) · [状态效果 S-8be0a91af861e49b](../../evidence/state_effects-sets-030.md#s-8be0a91af861e49b)

### path-039038

```text
(config)# no do-exec clear dmvpn statistics <cr>
```

Handler ` RVA 0xF4F28F0 `；selector ` 0 `；EOL ` RVA 0x3467EC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-22f4bc6d1acce73a](../../evidence/conditions-sets-014.md#c-22f4bc6d1acce73a) · [状态效果 S-242b7122920c829c](../../evidence/state_effects-sets-008.md#s-242b7122920c829c)

### path-038855

```text
(config)# no do-exec clear drip counters <cr>
```

Handler ` RVA 0x112B2F80 `；selector ` 1 `；EOL ` RVA 0x3544D280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034046

```text
(config)# no do-exec clear dspfarm statistics <cr>
```

Handler ` RVA 0x188BAB20 `；selector ` 0 `；EOL ` RVA 0x367F3F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-2f60b2d00e5489fc](../../evidence/state_effects-sets-011.md#s-2f60b2d00e5489fc)

### path-036677

```text
(config)# no do-exec clear dtp counter <cr>
```

Handler ` RVA 0x15F14E10 `；selector ` 0 `；EOL ` RVA 0x35E66F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054372

```text
(config)# no do-exec clear eigrp address-family ipv4 events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346B5888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-6310d78446d19d82](../../evidence/state_effects-sets-021.md#s-6310d78446d19d82)

### path-054352

```text
(config)# no do-exec clear eigrp address-family ipv4 logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346B55E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-6310d78446d19d82](../../evidence/state_effects-sets-021.md#s-6310d78446d19d82)

### path-054397

```text
(config)# no do-exec clear eigrp address-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346B4A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-47089db8aeb7e60d](../../evidence/conditions-sets-028.md#c-47089db8aeb7e60d) · [状态效果 S-6310d78446d19d82](../../evidence/state_effects-sets-021.md#s-6310d78446d19d82)

### path-054413

```text
(config)# no do-exec clear eigrp address-family ipv4 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 73 `；EOL ` RVA 0x346B5DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-6310d78446d19d82](../../evidence/state_effects-sets-021.md#s-6310d78446d19d82)

### path-059344

```text
(config)# no do-exec clear eigrp address-family ipv4 topology <address> <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346B4EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [参数 P-3fb9dae9bb0abdd4](../../evidence/parameters-sets-005.md#p-3fb9dae9bb0abdd4) · [状态效果 S-11ea8a6680527f14](../../evidence/state_effects-sets-004.md#s-11ea8a6680527f14)

### path-057982

```text
(config)# no do-exec clear eigrp address-family ipv4 topology active <cr>
```

Handler ` RVA 0xF573DF0 `；selector ` 69 `；EOL ` RVA 0x346B51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-6310d78446d19d82](../../evidence/state_effects-sets-021.md#s-6310d78446d19d82)

### path-054392

```text
(config)# no do-exec clear eigrp address-family ipv4 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 70 `；EOL ` RVA 0x346B5B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-6310d78446d19d82](../../evidence/state_effects-sets-021.md#s-6310d78446d19d82)

### path-054353

```text
(config)# no do-exec clear eigrp address-family ipv6 events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x35453F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-13f0d2c511e74adb](../../evidence/state_effects-sets-005.md#s-13f0d2c511e74adb)

### path-054339

```text
(config)# no do-exec clear eigrp address-family ipv6 logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x35453C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-13f0d2c511e74adb](../../evidence/state_effects-sets-005.md#s-13f0d2c511e74adb)

### path-054376

```text
(config)# no do-exec clear eigrp address-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35453180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c543cb4cc0b7c573](../../evidence/conditions-sets-076.md#c-c543cb4cc0b7c573) · [状态效果 S-13f0d2c511e74adb](../../evidence/state_effects-sets-005.md#s-13f0d2c511e74adb)

### path-054393

```text
(config)# no do-exec clear eigrp address-family ipv6 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 73 `；EOL ` RVA 0x35454478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-13f0d2c511e74adb](../../evidence/state_effects-sets-005.md#s-13f0d2c511e74adb)

### path-057967

```text
(config)# no do-exec clear eigrp address-family ipv6 topology active <cr>
```

Handler ` RVA 0xF573DF0 `；selector ` 69 `；EOL ` RVA 0x35453878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-13f0d2c511e74adb](../../evidence/state_effects-sets-005.md#s-13f0d2c511e74adb)

### path-054373

```text
(config)# no do-exec clear eigrp address-family ipv6 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 70 `；EOL ` RVA 0x354541D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-13f0d2c511e74adb](../../evidence/state_effects-sets-005.md#s-13f0d2c511e74adb)

### path-054290

```text
(config)# no do-exec clear eigrp service-family external-client <string> <cr>
```

Handler ` RVA 0x104726A0 `；selector ` 41 `；EOL ` RVA 0x34B3AB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Client Label。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-6e6d51b6eb7ccc0f](../../evidence/parameters-sets-009.md#p-6e6d51b6eb7ccc0f) · [状态效果 S-894668ff6e14fc40](../../evidence/state_effects-sets-029.md#s-894668ff6e14fc40)

### path-054371

```text
(config)# no do-exec clear eigrp service-family ipv4 events <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 71 `；EOL ` RVA 0x346EFFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-a520e7e7464c4348](../../evidence/state_effects-sets-035.md#s-a520e7e7464c4348)

### path-054351

```text
(config)# no do-exec clear eigrp service-family ipv4 logging <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 72 `；EOL ` RVA 0x346EFD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-a520e7e7464c4348](../../evidence/state_effects-sets-035.md#s-a520e7e7464c4348)

### path-054396

```text
(config)# no do-exec clear eigrp service-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x346EEFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c4aebcafa3efb865](../../evidence/conditions-sets-076.md#c-c4aebcafa3efb865) · [状态效果 S-a520e7e7464c4348](../../evidence/state_effects-sets-035.md#s-a520e7e7464c4348)

### path-060261

```text
(config)# no do-exec clear eigrp service-family ipv4 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x346EF660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-1c902772e46b736b](../../evidence/conditions-sets-011.md#c-1c902772e46b736b) · [参数 P-981a610bcc4e38b2](../../evidence/parameters-sets-012.md#p-981a610bcc4e38b2) · [状态效果 S-a520e7e7464c4348](../../evidence/state_effects-sets-035.md#s-a520e7e7464c4348)

### path-057974

```text
(config)# no do-exec clear eigrp service-family ipv4 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x346EF930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-a520e7e7464c4348](../../evidence/state_effects-sets-035.md#s-a520e7e7464c4348)

### path-054391

```text
(config)# no do-exec clear eigrp service-family ipv4 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x346F0288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-a520e7e7464c4348](../../evidence/state_effects-sets-035.md#s-a520e7e7464c4348)

### path-054409

```text
(config)# no do-exec clear eigrp service-family ipv6 events <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 71 `；EOL ` RVA 0x35476980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-e57231e8185e63e6](../../evidence/state_effects-sets-049.md#s-e57231e8185e63e6)

### path-054387

```text
(config)# no do-exec clear eigrp service-family ipv6 logging <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 72 `；EOL ` RVA 0x354766D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-e57231e8185e63e6](../../evidence/state_effects-sets-049.md#s-e57231e8185e63e6)

### path-054429

```text
(config)# no do-exec clear eigrp service-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x35475988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5079892e533d3ab0](../../evidence/conditions-sets-031.md#c-5079892e533d3ab0) · [状态效果 S-e57231e8185e63e6](../../evidence/state_effects-sets-049.md#s-e57231e8185e63e6)

### path-060263

```text
(config)# no do-exec clear eigrp service-family ipv6 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x35476000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-1993d4bf841bf125](../../evidence/conditions-sets-010.md#c-1993d4bf841bf125) · [参数 P-b117aaae787be4fd](../../evidence/parameters-sets-013.md#p-b117aaae787be4fd) · [状态效果 S-e57231e8185e63e6](../../evidence/state_effects-sets-049.md#s-e57231e8185e63e6)

### path-057988

```text
(config)# no do-exec clear eigrp service-family ipv6 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x354762D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-e57231e8185e63e6](../../evidence/state_effects-sets-049.md#s-e57231e8185e63e6)

### path-054425

```text
(config)# no do-exec clear eigrp service-family ipv6 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x35476C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-e57231e8185e63e6](../../evidence/state_effects-sets-049.md#s-e57231e8185e63e6)

### path-035096

```text
(config)# no do-exec clear entry <number:0..256> <cr>
```

Handler ` RVA 0xCCF7FE0 `；selector ` 0 `；EOL ` RVA 0x33C66A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Queue entry number。

[条件 C-ae130bfe4f93ffb9](../../evidence/conditions-sets-067.md#c-ae130bfe4f93ffb9) · [参数 P-baff37d66d7bf69e](../../evidence/parameters-sets-014.md#p-baff37d66d7bf69e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-038435

```text
(config)# no do-exec clear environment counters <cr>
```

Handler ` RVA 0xE123D20 `；selector ` 16 `；EOL ` RVA 0x3420AE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034473

```text
(config)# no do-exec clear eobc counters <cr>
```

Handler ` RVA 0xED896F0 `；selector ` 0 `；EOL ` RVA 0x3442E440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034525

```text
(config)# no do-exec clear eobc interface <cr>
```

Handler ` RVA 0xED897B0 `；selector ` 0 `；EOL ` RVA 0x3442E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059970

```text
(config)# no do-exec clear ethernet cfm ais domain <string> mpid <number:1..8191> port <cr>
```

Handler ` RVA 0xBDD3860 `；selector ` 0 `；EOL ` RVA 0x338CDFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-334f7c49a7ede4e3](../../evidence/conditions-sets-020.md#c-334f7c49a7ede4e3) · [参数 P-d12e398db42d71ec](../../evidence/parameters-sets-016.md#p-d12e398db42d71ec) · [状态效果 S-47aac09ac446dce2](../../evidence/state_effects-sets-016.md#s-47aac09ac446dce2)

### path-044669

```text
(config)# no do-exec clear ethernet cfm ccm-learning-database <cr>
```

Handler ` RVA 0xBDD3D70 `；selector ` 0 `；EOL ` RVA 0x338CF840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6babdf68d76558b8](../../evidence/conditions-sets-042.md#c-6babdf68d76558b8) · [状态效果 S-32301fcd2e9962d7](../../evidence/state_effects-sets-011.md#s-32301fcd2e9962d7)

### path-044496

```text
(config)# no do-exec clear ethernet cfm errors <cr>
```

Handler ` RVA 0xBDD2B30 `；selector ` 0 `；EOL ` RVA 0x338CE920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6645a68419d2583e](../../evidence/conditions-sets-040.md#c-6645a68419d2583e) · [状态效果 S-3e9d498cbe01ad58](../../evidence/state_effects-sets-014.md#s-3e9d498cbe01ad58)

### path-052413

```text
(config)# no do-exec clear ethernet cfm fast-timeout statistics <cr>
```

Handler ` RVA 0xBDD3CD0 `；selector ` 0 `；EOL ` RVA 0x338CF3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49fdd367145abd42](../../evidence/conditions-sets-029.md#c-49fdd367145abd42) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056899

```text
(config)# no do-exec clear ethernet cfm latching-loopback discover-phase mep <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 1 `；EOL ` RVA 0x338CD438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-7ad99689e0a79606](../../evidence/state_effects-sets-026.md#s-7ad99689e0a79606)

### path-056894

```text
(config)# no do-exec clear ethernet cfm latching-loopback discover-phase mip <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 2 `；EOL ` RVA 0x338CD6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-db4b9b7412d01b81](../../evidence/state_effects-sets-046.md#s-db4b9b7412d01b81)

### path-052277

```text
(config)# no do-exec clear ethernet cfm maintenance-points remote <cr>
```

Handler ` RVA 0xBDD28E0 `；selector ` 0 `；EOL ` RVA 0x338CC7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058921

```text
(config)# no do-exec clear ethernet cfm maintenance-points remote domain <string> <cr>
```

Handler ` RVA 0xBDD2A20 `；selector ` 0 `；EOL ` RVA 0x338CC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [参数 P-b4f885fc792161b1](../../evidence/parameters-sets-014.md#p-b4f885fc792161b1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058931

```text
(config)# no do-exec clear ethernet cfm pm session db <number:0..8000> <cr>
```

Handler ` RVA 0xBE8C2A0 `；selector ` 0 `；EOL ` RVA 0x339155B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Session Id。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [参数 P-c0ee7e00d5a1eec9](../../evidence/parameters-sets-015.md#p-c0ee7e00d5a1eec9) · [状态效果 S-d98a24fd76d12639](../../evidence/state_effects-sets-046.md#s-d98a24fd76d12639)

### path-044343

```text
(config)# no do-exec clear ethernet cfm statistics <cr>
```

Handler ` RVA 0xBDD3070 `；selector ` 0 `；EOL ` RVA 0x338CD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044275

```text
(config)# no do-exec clear ethernet cfm traceroute-cache <cr>
```

Handler ` RVA 0xBDD3D20 `；selector ` 0 `；EOL ` RVA 0x338CCD08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044258

```text
(config)# no do-exec clear ethernet lmi statistics <cr>
```

Handler ` RVA 0xBEC38F0 `；selector ` 0 `；EOL ` RVA 0x339203E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e252cf8c35d4f1d1](../../evidence/conditions-sets-087.md#c-e252cf8c35d4f1d1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044255

```text
(config)# no do-exec clear ethernet oam statistics <cr>
```

Handler ` RVA 0xBEECC20 `；selector ` 44 `；EOL ` RVA 0x3392F790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058959

```text
(config)# no do-exec clear ethernet service instance id <number:1..16384> mac-tunnel <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 1 `；EOL ` RVA 0x33979C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-ea732fa9e043fe11](../../evidence/conditions-sets-091.md#c-ea732fa9e043fe11) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-76f309547e209f54](../../evidence/state_effects-sets-025.md#s-76f309547e209f54)

### path-059671

```text
(config)# no do-exec clear ethernet service instance id <number:1..16384> mac-tunnel errdisable <cr>
```

Handler ` RVA 0xC0357A0 `；selector ` 3 `；EOL ` RVA 0x33985898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-6966d62b8dc7328d](../../evidence/conditions-sets-041.md#c-6966d62b8dc7328d) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-76f309547e209f54](../../evidence/state_effects-sets-025.md#s-76f309547e209f54)

### path-052306

```text
(config)# no do-exec clear ethernet service internal back-trace <cr>
```

Handler ` RVA 0xC013D80 `；selector ` 0 `；EOL ` RVA 0x3397BF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-59b07fa78c1ec760](../../evidence/conditions-sets-035.md#c-59b07fa78c1ec760) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052329

```text
(config)# no do-exec clear ethernet service ipc statistics <cr>
```

Handler ` RVA 0xBF920F0 `；selector ` 0 `；EOL ` RVA 0x33962C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054908

```text
(config)# no do-exec clear event manager detector counters <cr>
```

Handler ` RVA 0xC0CB550 `；selector ` 0 `；EOL ` RVA 0x339BCBB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058257

```text
(config)# no do-exec clear event manager detector rpc counters <cr>
```

Handler ` RVA 0xC0A29A0 `；selector ` 0 `；EOL ` RVA 0x3399C3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-058278

```text
(config)# no do-exec clear event manager detector rpc sessions <cr>
```

Handler ` RVA 0xC0A2BA0 `；selector ` 0 `；EOL ` RVA 0x3399C698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054880

```text
(config)# no do-exec clear event manager server counters <cr>
```

Handler ` RVA 0xC0CB5C0 `；selector ` 0 `；EOL ` RVA 0x339BC8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028282

```text
(config)# no do-exec clear facility-alarm <cr>
```

Handler ` RVA 0xC299EF0 `；selector ` 0 `；EOL ` RVA 0x33A28388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034140

```text
(config)# no do-exec clear facility-alarm critical <cr>
```

Handler ` RVA 0xC299990 `；selector ` 0 `；EOL ` RVA 0x33A27F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-11cf8f04477e7437](../../evidence/state_effects-sets-004.md#s-11cf8f04477e7437)

### path-044634

```text
(config)# no do-exec clear flow exporter statistics <cr>
```

Handler ` RVA 0xC154D30 `；selector ` 0 `；EOL ` RVA 0x339E3370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-039537

```text
(config)# no do-exec clear flowspec afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 5 `；EOL ` RVA 0x35A98610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a0a86034b1ad4591](../../evidence/conditions-sets-062.md#c-a0a86034b1ad4591) · [状态效果 S-3432b835ca3330a6](../../evidence/state_effects-sets-012.md#s-3432b835ca3330a6)

### path-048390

```text
(config)# no do-exec clear flowspec counters afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 2 `；EOL ` RVA 0x35A97D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-af27c26833ea6b92](../../evidence/state_effects-sets-037.md#s-af27c26833ea6b92)

### path-048281

```text
(config)# no do-exec clear flowspec counters internal <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 4 `；EOL ` RVA 0x35A97918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-c0d0e665d397e418](../../evidence/state_effects-sets-041.md#s-c0d0e665d397e418)

### path-047099

```text
(config)# no do-exec clear fqdn packet statistics <cr>
```

Handler ` RVA 0xC2E0BF0 `；selector ` 0 `；EOL ` RVA 0x33A3CB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-48d060cc9d3e01ae](../../evidence/state_effects-sets-016.md#s-48d060cc9d3e01ae)

### path-037161

```text
(config)# no do-exec clear frame-relay counter <cr>
```

Handler ` RVA 0xF606570 `；selector ` 18 `；EOL ` RVA 0x34700850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037205

```text
(config)# no do-exec clear frame-relay inarp <cr>
```

Handler ` RVA 0xF62D080 `；selector ` 17 `；EOL ` RVA 0x3470EE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037430

```text
(config)# no do-exec clear host <string> <cr>
```

Handler ` RVA 0xD128DD0 `；selector ` 0 `；EOL ` RVA 0x33D95930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Hostname to delete (* for all entries)。

[条件 C-7cd4fea57bafbb25](../../evidence/conditions-sets-048.md#c-7cd4fea57bafbb25) · [参数 P-5fa77e3c3044d1c6](../../evidence/parameters-sets-008.md#p-5fa77e3c3044d1c6) · [状态效果 S-326286e4bf908453](../../evidence/state_effects-sets-011.md#s-326286e4bf908453)

### path-036956

```text
(config)# no do-exec clear icm statistics <cr>
```

Handler ` RVA 0xC2FAF60 `；selector ` 0 `；EOL ` RVA 0x33A40790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-80413ff659693bfa](../../evidence/state_effects-sets-027.md#s-80413ff659693bfa)

### path-031746

```text
(config)# no do-exec clear iox <cr>
```

Handler ` RVA 0xEADA610 `；selector ` 0 `；EOL ` RVA 0x343A3698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045324

```text
(config)# no do-exec clear ip access-list counters <cr>
```

Handler ` RVA 0xCEEDDF0 `；selector ` 0 `；EOL ` RVA 0x33D2D580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-29b5b928497ba869](../../evidence/conditions-sets-016.md#c-29b5b928497ba869) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037119

```text
(config)# no do-exec clear ip accounting <cr>
```

Handler ` RVA 0xD17A5F0 `；selector ` 0 `；EOL ` RVA 0x33DA6DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-06830b0bd2ae672e](../../evidence/state_effects-sets-002.md#s-06830b0bd2ae672e)

### path-044919

```text
(config)# no do-exec clear ip arp <address> <cr>
```

Handler ` RVA 0xCF5FF90 `；selector ` 0 `；EOL ` RVA 0x33D1E250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of dynamic ARP entry。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-b690c2ce67487b89](../../evidence/parameters-sets-014.md#p-b690c2ce67487b89) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052730

```text
(config)# no do-exec clear ip arp poll statistics <cr>
```

Handler ` RVA 0xCFE25A0 `；selector ` 0 `；EOL ` RVA 0x33D1E538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036564

```text
(config)# no do-exec clear ip cache <cr>
```

Handler ` RVA 0xD49E510 `；selector ` 0 `；EOL ` RVA 0x33E54E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046281

```text
(config)# no do-exec clear ip casa counters <cr>
```

Handler ` RVA 0x1132C870 `；selector ` 0 `；EOL ` RVA 0x35499608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046596

```text
(config)# no do-exec clear ip cef event-log <cr>
```

Handler ` RVA 0xB5ECF20 `；selector ` 0 `；EOL ` RVA 0x337B4F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046533

```text
(config)# no do-exec clear ip cef inconsistency <cr>
```

Handler ` RVA 0xB5ECEE0 `；selector ` 0 `；EOL ` RVA 0x337B4CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046925

```text
(config)# no do-exec clear ip cef prefix-statistics <cr>
```

Handler ` RVA 0xB61F7B0 `；selector ` 0 `；EOL ` RVA 0x337C4660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5f42d62acdf9713](../../evidence/conditions-sets-083.md#c-d5f42d62acdf9713) · [状态效果 S-2f074ac839ff8cb8](../../evidence/state_effects-sets-010.md#s-2f074ac839ff8cb8)

### path-036571

```text
(config)# no do-exec clear ip cgmp <cr>
```

Handler ` RVA 0xF6779A0 `；selector ` 0 `；EOL ` RVA 0x34746408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-15c8fb31734caa71](../../evidence/conditions-sets-009.md#c-15c8fb31734caa71) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054206

```text
(config)# no do-exec clear ip dhcp binding <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 1 `；EOL ` RVA 0x33DE44E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Clear a specific binding。

[条件 C-915a8514a34f7b53](../../evidence/conditions-sets-056.md#c-915a8514a34f7b53) · [参数 P-701f423f9be8657b](../../evidence/parameters-sets-009.md#p-701f423f9be8657b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054236

```text
(config)# no do-exec clear ip dhcp conflict <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 3 `；EOL ` RVA 0x33DE4BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Clear a specific conflict。

[条件 C-1ef20701edbe572d](../../evidence/conditions-sets-012.md#c-1ef20701edbe572d) · [参数 P-98938e3b3a412be2](../../evidence/parameters-sets-012.md#p-98938e3b3a412be2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054264

```text
(config)# no do-exec clear ip dhcp limit lease <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 8 `；EOL ` RVA 0x33DE5590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2498161afb0903f2](../../evidence/conditions-sets-014.md#c-2498161afb0903f2) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054115

```text
(config)# no do-exec clear ip dhcp server odap-statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 10 `；EOL ` RVA 0x33DE3E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054147

```text
(config)# no do-exec clear ip dhcp server statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 4 `；EOL ` RVA 0x33DE3918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b7107639c9a89805](../../evidence/conditions-sets-071.md#c-b7107639c9a89805) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057851

```text
(config)# no do-exec clear ip dhcp snooping binding <address> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 1 `；EOL ` RVA 0x35E81B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Clear address specific bindings。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [参数 P-24a6453abfb0d28a](../../evidence/parameters-sets-003.md#p-24a6453abfb0d28a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059328

```text
(config)# no do-exec clear ip dhcp snooping binding bridge-domain <string> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 3 `；EOL ` RVA 0x35E821D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` DHCP Snooping bd range, example : 1,3-5,7,9-11。

[条件 C-75fcf496af8704d2](../../evidence/conditions-sets-046.md#c-75fcf496af8704d2) · [参数 P-cce908d8140214c8](../../evidence/parameters-sets-016.md#p-cce908d8140214c8) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057847

```text
(config)# no do-exec clear ip dhcp snooping database statistics <cr>
```

Handler ` RVA 0x15FAA320 `；selector ` 0 `；EOL ` RVA 0x35E825B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054141

```text
(config)# no do-exec clear ip dhcp snooping statistics <cr>
```

Handler ` RVA 0x15FA9590 `；selector ` 0 `；EOL ` RVA 0x35E82840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-054232

```text
(config)# no do-exec clear ip dhcp subnet <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 5 `；EOL ` RVA 0x33DE51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Specify an address in the subnet to clear。

[条件 C-8127a4d438972794](../../evidence/conditions-sets-050.md#c-8127a4d438972794) · [参数 P-604821058269eb93](../../evidence/parameters-sets-008.md#p-604821058269eb93) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053360

```text
(config)# no do-exec clear ip dns servers <address> <cr>
```

Handler ` RVA 0xD133B70 `；selector ` 0 `；EOL ` RVA 0x33D9B6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPV4 Server Address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-f3837ab8cf79a70e](../../evidence/parameters-sets-018.md#p-f3837ab8cf79a70e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035758

```text
(config)# no do-exec clear ip drp <cr>
```

Handler ` RVA 0xF4F0BA0 `；selector ` 0 `；EOL ` RVA 0x3467ADA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046341

```text
(config)# no do-exec clear ip eigrp events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346D9C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [状态效果 S-2f88ed09164449b8](../../evidence/state_effects-sets-011.md#s-2f88ed09164449b8)

### path-046294

```text
(config)# no do-exec clear ip eigrp logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346D99B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [状态效果 S-2f88ed09164449b8](../../evidence/state_effects-sets-011.md#s-2f88ed09164449b8)

### path-046422

```text
(config)# no do-exec clear ip eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346D92A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-753308e3327070a9](../../evidence/conditions-sets-045.md#c-753308e3327070a9) · [状态效果 S-2f88ed09164449b8](../../evidence/state_effects-sets-011.md#s-2f88ed09164449b8)

### path-053719

```text
(config)# no do-exec clear ip eigrp topology <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346D96E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network to clear from topology。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [参数 P-c5c28ea144019d4d](../../evidence/parameters-sets-015.md#p-c5c28ea144019d4d) · [状态效果 S-2f88ed09164449b8](../../evidence/state_effects-sets-011.md#s-2f88ed09164449b8)

### path-057394

```text
(config)# no do-exec clear ip http client cache all <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 1 `；EOL ` RVA 0x33DB0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059143

```text
(config)# no do-exec clear ip http client cache session <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 2 `；EOL ` RVA 0x33DB0AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` session name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-ba614fcf6b2daaef](../../evidence/parameters-sets-014.md#p-ba614fcf6b2daaef) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059133

```text
(config)# no do-exec clear ip http client cache url <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 3 `；EOL ` RVA 0x33DB07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` url to clear。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-04caf09ff1ffb9ea](../../evidence/parameters-sets-001.md#p-04caf09ff1ffb9ea) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053436

```text
(config)# no do-exec clear ip http client cookie <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 4 `；EOL ` RVA 0x33DB1618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059150

```text
(config)# no do-exec clear ip http client cookie domain <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 6 `；EOL ` RVA 0x33DB1370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Client domain/host name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-7ddae15590050dbb](../../evidence/parameters-sets-010.md#p-7ddae15590050dbb) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059161

```text
(config)# no do-exec clear ip http client cookie name <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 7 `；EOL ` RVA 0x33DB1658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Client cookie name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-70e3f6d6b140bc15](../../evidence/parameters-sets-009.md#p-70e3f6d6b140bc15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059142

```text
(config)# no do-exec clear ip http client cookie session <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 5 `；EOL ` RVA 0x33DB1088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Client session name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-7dc08f985880508a](../../evidence/parameters-sets-010.md#p-7dc08f985880508a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044998

```text
(config)# no do-exec clear ip icmp rate-limit <cr>
```

Handler ` RVA 0xCFE5700 `；selector ` 0 `；EOL ` RVA 0x33D2B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d149a0ed9e1c68ff](../../evidence/conditions-sets-081.md#c-d149a0ed9e1c68ff) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046206

```text
(config)# no do-exec clear ip igmp group <cr>
```

Handler ` RVA 0xF6B26D0 `；selector ` 0 `；EOL ` RVA 0x34746DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5b415668ee6ea98d](../../evidence/conditions-sets-036.md#c-5b415668ee6ea98d) · [状态效果 S-93b3e7dd2aa27365](../../evidence/state_effects-sets-031.md#s-93b3e7dd2aa27365)

### path-046512

```text
(config)# no do-exec clear ip mfib counters <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355B7700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f808427ebefa84e5](../../evidence/conditions-sets-096.md#c-f808427ebefa84e5) · [状态效果 S-bfe2544fa4418299](../../evidence/state_effects-sets-041.md#s-bfe2544fa4418299)

### path-046099

```text
(config)# no do-exec clear ip mrm status-report <cr>
```

Handler ` RVA 0xF672250 `；selector ` 0 `；EOL ` RVA 0x3471F308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046110

```text
(config)# no do-exec clear ip mroute <address> <cr>
```

Handler ` RVA 0xF74EC90 `；selector ` 0 `；EOL ` RVA 0x347468B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP name or group address。

[条件 C-be25b0dc514ae992](../../evidence/conditions-sets-073.md#c-be25b0dc514ae992) · [参数 P-5526640d1cbfc478](../../evidence/parameters-sets-007.md#p-5526640d1cbfc478) · [状态效果 S-aed97c4a5c2c00b5](../../evidence/state_effects-sets-037.md#s-aed97c4a5c2c00b5)

### path-053183

```text
(config)# no do-exec clear ip msdp peer <address> <cr>
```

Handler ` RVA 0xF78ED70 `；selector ` 0 `；EOL ` RVA 0x34741B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-9f44f2d1408a3f5d](../../evidence/parameters-sets-012.md#p-9f44f2d1408a3f5d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045820

```text
(config)# no do-exec clear ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78EA70 `；selector ` 0 `；EOL ` RVA 0x34741E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045875

```text
(config)# no do-exec clear ip msdp statistics <cr>
```

Handler ` RVA 0xF78EB10 `；selector ` 0 `；EOL ` RVA 0x34742130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045980

```text
(config)# no do-exec clear ip multicast limit <cr>
```

Handler ` RVA 0xF777FE0 `；selector ` 0 `；EOL ` RVA 0x34746048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5aff361b478776d](../../evidence/conditions-sets-082.md#c-d5aff361b478776d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053487

```text
(config)# no do-exec clear ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD4712F0 `；selector ` 0 `；EOL ` RVA 0x33E525D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045933

```text
(config)# no do-exec clear ip multicast rsvp <cr>
```

Handler ` RVA 0xF6F1770 `；selector ` 0 `；EOL ` RVA 0x34745CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e532f6e964361ea1](../../evidence/conditions-sets-088.md#c-e532f6e964361ea1) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059773

```text
(config)# no do-exec clear ip multicast snooping limit vlan <number:1..4095> statistics <cr>
```

Handler ` RVA 0xC3568D0 `；selector ` 64 `；EOL ` RVA 0x33A5F240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [参数 P-85cbffd05ab530a5](../../evidence/parameters-sets-010.md#p-85cbffd05ab530a5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046132

```text
(config)# no do-exec clear ip nat statistics <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 1 `；EOL ` RVA 0x347DD7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046474

```text
(config)# no do-exec clear ip nat translation <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 0 `；EOL ` RVA 0x347DCB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a1cc54701c6ed739](../../evidence/conditions-sets-062.md#c-a1cc54701c6ed739) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-036513

```text
(config)# no do-exec clear ip nbar <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 2 `；EOL ` RVA 0x3527C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ce4cc5e5f2365570](../../evidence/conditions-sets-079.md#c-ce4cc5e5f2365570) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-059153

```text
(config)# no do-exec clear ip nbar classification auto-learn top-hosts restart <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 14 `；EOL ` RVA 0x3527B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a8d94fa5b85f8d8a](../../evidence/conditions-sets-065.md#c-a8d94fa5b85f8d8a) · [状态效果 S-13e8a749227f62b7](../../evidence/state_effects-sets-005.md#s-13e8a749227f62b7)

### path-059141

```text
(config)# no do-exec clear ip nbar classification auto-learn top-hosts statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 13 `；EOL ` RVA 0x3527B5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a8d94fa5b85f8d8a](../../evidence/conditions-sets-065.md#c-a8d94fa5b85f8d8a) · [状态效果 S-13e8a749227f62b7](../../evidence/state_effects-sets-005.md#s-13e8a749227f62b7)

### path-057387

```text
(config)# no do-exec clear ip nbar classification cache sync <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 12 `；EOL ` RVA 0x3527BBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-059156

```text
(config)# no do-exec clear ip nbar classification dns learning cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 47 `；EOL ` RVA 0x3527BF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-059175

```text
(config)# no do-exec clear ip nbar classification dns learning statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 49 `；EOL ` RVA 0x3527C1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-053417

```text
(config)# no do-exec clear ip nbar classification socket-cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 48 `；EOL ` RVA 0x3527C458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-045882

```text
(config)# no do-exec clear ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 34 `；EOL ` RVA 0x3527B048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cd1aff9592498208](../../evidence/conditions-sets-079.md#c-cd1aff9592498208) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-045910

```text
(config)# no do-exec clear ip nbar statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 7 `；EOL ` RVA 0x3527C748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-71e0524c2117ffd7](../../evidence/conditions-sets-044.md#c-71e0524c2117ffd7) · [状态效果 S-ac334b784f8942f9](../../evidence/state_effects-sets-036.md#s-ac334b784f8942f9)

### path-037085

```text
(config)# no do-exec clear ip nhrp <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 0 `；EOL ` RVA 0x347F2628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046464

```text
(config)# no do-exec clear ip nhrp counters <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 1 `；EOL ` RVA 0x347F29F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046356

```text
(config)# no do-exec clear ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 0 `；EOL ` RVA 0x34BF9228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1734e8712ed94573](../../evidence/state_effects-sets-005.md#s-1734e8712ed94573)

### path-046705

```text
(config)# no do-exec clear ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 2 `；EOL ` RVA 0x347F2F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-72d46b46a297f481](../../evidence/conditions-sets-044.md#c-72d46b46a297f481) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046305

```text
(config)# no do-exec clear ip ospf counters <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 4 `；EOL ` RVA 0x348934D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046344

```text
(config)# no do-exec clear ip ospf events <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 6 `；EOL ` RVA 0x34893FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046196

```text
(config)# no do-exec clear ip ospf force-spf <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 0 `；EOL ` RVA 0x34892C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059228

```text
(config)# no do-exec clear ip ospf lsa router <address> self <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 7 `；EOL ` RVA 0x34893A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF LSID in IP address format。

[条件 C-a52f305b1c8c11f0](../../evidence/conditions-sets-064.md#c-a52f305b1c8c11f0) · [参数 P-4bb4f15a3e4f951b](../../evidence/parameters-sets-006.md#p-4bb4f15a3e4f951b) · [状态效果 S-5818d98ec9f863c1](../../evidence/state_effects-sets-019.md#s-5818d98ec9f863c1)

### path-053523

```text
(config)# no do-exec clear ip ospf nsr statistics <cr>
```

Handler ` RVA 0xDACCB50 `；selector ` 20 `；EOL ` RVA 0x33FC88B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5dbe502c3acf75ff](../../evidence/state_effects-sets-020.md#s-5dbe502c3acf75ff)

### path-046090

```text
(config)# no do-exec clear ip ospf process <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 3 `；EOL ` RVA 0x34892700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046044

```text
(config)# no do-exec clear ip ospf redistribution <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 2 `；EOL ` RVA 0x34892458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046147

```text
(config)# no do-exec clear ip ospf rib <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 1 `；EOL ` RVA 0x348929A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046363

```text
(config)# no do-exec clear ip ospf traffic <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 5 `；EOL ` RVA 0x34893080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9481ef008e1de97f](../../evidence/conditions-sets-057.md#c-9481ef008e1de97f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045935

```text
(config)# no do-exec clear ip pim df <cr>
```

Handler ` RVA 0xF7CB460 `；selector ` 0 `；EOL ` RVA 0x34771D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053413

```text
(config)# no do-exec clear ip pim interface count <cr>
```

Handler ` RVA 0xF827030 `；selector ` 0 `；EOL ` RVA 0x34772140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d0cc604d16d7fbbd](../../evidence/conditions-sets-080.md#c-d0cc604d16d7fbbd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053408

```text
(config)# no do-exec clear ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF8A2050 `；selector ` 0 `；EOL ` RVA 0x347726F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053356

```text
(config)# no do-exec clear ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF8A1FA0 `；selector ` 0 `；EOL ` RVA 0x34772450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045819

```text
(config)# no do-exec clear ip pim rp-mapping <cr>
```

Handler ` RVA 0xF7BE560 `；selector ` 0 `；EOL ` RVA 0x34771918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-037078

```text
(config)# no do-exec clear ip prefix-list <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x34283CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5cdf8c3f2be1a50f](../../evidence/state_effects-sets-020.md#s-5cdf8c3f2be1a50f)

### path-035314

```text
(config)# no do-exec clear ip redirect <cr>
```

Handler ` RVA 0xCF50BF0 `；selector ` 0 `；EOL ` RVA 0x33D2B468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-b026e02836d84298](../../evidence/state_effects-sets-037.md#s-b026e02836d84298)

### path-046601

```text
(config)# no do-exec clear ip reflexive-list <string> <cr>
```

Handler ` RVA 0xCEFCA00 `；selector ` 0 `；EOL ` RVA 0x3479AD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Delete a specific reflexive ACL。

[条件 C-94a4629f79b58d64](../../evidence/conditions-sets-057.md#c-94a4629f79b58d64) · [参数 P-afb5c6d87d9e8de3](../../evidence/parameters-sets-013.md#p-afb5c6d87d9e8de3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-045773

```text
(config)# no do-exec clear ip route <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 1 `；EOL ` RVA 0x3422DF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination network route to delete。

[条件 C-3ef1add5b3f1b32e](../../evidence/conditions-sets-024.md#c-3ef1add5b3f1b32e) · [参数 P-a606ea51f9247878](../../evidence/parameters-sets-013.md#p-a606ea51f9247878) · [状态效果 S-fa2843ac24cd5850](../../evidence/state_effects-sets-053.md#s-fa2843ac24cd5850)

### path-053191

```text
(config)# no do-exec clear ip route dhcp <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 2 `；EOL ` RVA 0x3422E240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination host route to delete。

[条件 C-3ef1add5b3f1b32e](../../evidence/conditions-sets-024.md#c-3ef1add5b3f1b32e) · [参数 P-f4e189f9e5e93c08](../../evidence/parameters-sets-018.md#p-f4e189f9e5e93c08) · [状态效果 S-a651c8d33431e2ee](../../evidence/state_effects-sets-035.md#s-a651c8d33431e2ee)

### path-057415

```text
(config)# no do-exec clear ip route download <address> <address> <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 1 `；EOL ` RVA 0x3422E620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Destination network route to delete；` address ` Destination network mask。

[条件 C-3c5166292a75cfac](../../evidence/conditions-sets-023.md#c-3c5166292a75cfac) · [参数 P-405fcd062cfd9eeb](../../evidence/parameters-sets-005.md#p-405fcd062cfd9eeb) · [状态效果 S-cb71abe1e90c7feb](../../evidence/state_effects-sets-043.md#s-cb71abe1e90c7feb)

### path-053414

```text
(config)# no do-exec clear ip route download reload <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 2 `；EOL ` RVA 0x3422E8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3c5166292a75cfac](../../evidence/conditions-sets-023.md#c-3c5166292a75cfac) · [状态效果 S-a651c8d33431e2ee](../../evidence/state_effects-sets-035.md#s-a651c8d33431e2ee)

### path-046615

```text
(config)# no do-exec clear ip rsvp authentication <cr>
```

Handler ` RVA 0x100741B0 `；selector ` 0 `；EOL ` RVA 0x34A3D340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-046335

```text
(config)# no do-exec clear ip rsvp counters <cr>
```

Handler ` RVA 0x100B7230 `；selector ` 0 `；EOL ` RVA 0x34A3B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057687

```text
(config)# no do-exec clear ip rsvp hello bfd lost-cnt <cr>
```

Handler ` RVA 0x10074420 `；selector ` 0 `；EOL ` RVA 0x34A3C3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057729

```text
(config)# no do-exec clear ip rsvp hello bfd nbr-lost <cr>
```

Handler ` RVA 0x100744C0 `；selector ` 0 `；EOL ` RVA 0x34A3C678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057693

```text
(config)# no do-exec clear ip rsvp hello instance counters <cr>
```

Handler ` RVA 0x1006F1F0 `；selector ` 0 `；EOL ` RVA 0x34A3C0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-057656

```text
(config)# no do-exec clear ip rsvp hello instance statistics <cr>
```

Handler ` RVA 0x1006F240 `；selector ` 0 `；EOL ` RVA 0x34A3BE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053771

```text
(config)# no do-exec clear ip rsvp hello statistics <cr>
```

Handler ` RVA 0x1006F290 `；selector ` 0 `；EOL ` RVA 0x34A3BB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-053893

```text
(config)# no do-exec clear ip rsvp metadata interface <cr>
```

Handler ` RVA 0x10078C10 `；selector ` 0 `；EOL ` RVA 0x34A3D630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-577970e4f2d7b997](../../evidence/conditions-sets-034.md#c-577970e4f2d7b997) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

