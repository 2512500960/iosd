# trunk-group · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008082

```text
(config-trunk-group)# capacity trunk-group update interval <number:10..3600> <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 1 `；EOL ` RVA 0x37900558 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` capacity update timer value。

[条件 C-a635baa8de2455b3](../../evidence/conditions-sets-064.md#c-a635baa8de2455b3) · [参数 P-402a0631023aabea](../../evidence/parameters-sets-005.md#p-402a0631023aabea) · [状态效果 S-8231a248993237ad](../../evidence/state_effects-sets-028.md#s-8231a248993237ad)

### observed_connections-008044

```text
(config-trunk-group)# carrier-id <string> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 12 `；EOL ` RVA 0x378FCC30 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Carrier identifier。

[条件 C-b6318cd1fd2e1b2c](../../evidence/conditions-sets-070.md#c-b6318cd1fd2e1b2c) · [参数 P-69c83c2a00e94bc8](../../evidence/parameters-sets-008.md#p-69c83c2a00e94bc8)

### observed_connections-008059

```text
(config-trunk-group)# carrier-id <string> cic <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 13 `；EOL ` RVA 0x378FCC98 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Carrier identifier。

[条件 C-b6318cd1fd2e1b2c](../../evidence/conditions-sets-070.md#c-b6318cd1fd2e1b2c) · [参数 P-69c83c2a00e94bc8](../../evidence/parameters-sets-008.md#p-69c83c2a00e94bc8)

### observed_connections-008083

```text
(config-trunk-group)# default capacity trunk-group update interval <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 1 `；EOL ` RVA 0x37900558 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7948850dd42b1bb2](../../evidence/conditions-sets-047.md#c-7948850dd42b1bb2) · [状态效果 S-86ec645451806eeb](../../evidence/state_effects-sets-029.md#s-86ec645451806eeb)

### observed_connections-008043

```text
(config-trunk-group)# default carrier-id <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 12 `；EOL ` RVA 0x378FCC30 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-09be91f53203e761](../../evidence/conditions-sets-004.md#c-09be91f53203e761) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008052

```text
(config-trunk-group)# default description <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 9 `；EOL ` RVA 0x378FEA30 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff7c53c1de79e6bc](../../evidence/conditions-sets-098.md#c-ff7c53c1de79e6bc) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008046

```text
(config-trunk-group)# default hunt-scheme <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 10 `；EOL ` RVA 0x378FD640 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83951da655986728](../../evidence/conditions-sets-051.md#c-83951da655986728) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008071

```text
(config-trunk-group)# default isdn supp-service tbct <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 11 `；EOL ` RVA 0x378FD2C0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9961f9d5ab3b24ae](../../evidence/state_effects-sets-033.md#s-9961f9d5ab3b24ae)

### observed_connections-008062

```text
(config-trunk-group)# default max-calls any <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 2 `；EOL ` RVA 0x378FE148 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8510e35c471bf37c](../../evidence/conditions-sets-051.md#c-8510e35c471bf37c) · [状态效果 S-3f1053b70feb4322](../../evidence/state_effects-sets-014.md#s-3f1053b70feb4322)

### observed_connections-008049

```text
(config-trunk-group)# default max-retry <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 8 `；EOL ` RVA 0x378FDD80 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bbd1c0aeaa6fb94](../../evidence/conditions-sets-054.md#c-8bbd1c0aeaa6fb94) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008068

```text
(config-trunk-group)# default preemption enable <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 17 `；EOL ` RVA 0x378FF100 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bac78deff780310d](../../evidence/conditions-sets-072.md#c-bac78deff780310d) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008080

```text
(config-trunk-group)# default preemption guard timer <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 19 `；EOL ` RVA 0x378FF7E8 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d02e03b1f2fc0f6a](../../evidence/conditions-sets-080.md#c-d02e03b1f2fc0f6a) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008077

```text
(config-trunk-group)# default preemption tone timer <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 18 `；EOL ` RVA 0x378FF470 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-86defa5d86391916](../../evidence/conditions-sets-052.md#c-86defa5d86391916) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008074

```text
(config-trunk-group)# default tgrep advertise trunk-group <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 0 `；EOL ` RVA 0x378FFC20 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-444db606c8d26fa3](../../evidence/conditions-sets-027.md#c-444db606c8d26fa3) · [状态效果 S-795ca6bb748c2a9b](../../evidence/state_effects-sets-026.md#s-795ca6bb748c2a9b)

### observed_connections-008058

```text
(config-trunk-group)# default translation-profile outgoing <cr>
```

Handler ` RVA 0x1E3BB950 `；selector ` 5 `；EOL ` RVA 0x378FC8A8 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6c1b6a34e2f0f5ee](../../evidence/conditions-sets-042.md#c-6c1b6a34e2f0f5ee) · [状态效果 S-457c6ffd811986e3](../../evidence/state_effects-sets-015.md#s-457c6ffd811986e3)

### observed_connections-008066

```text
(config-trunk-group)# default voice-class cause-code <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 16 `；EOL ` RVA 0x378FE6D0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4aa17ba11a64a0c](../../evidence/conditions-sets-076.md#c-c4aa17ba11a64a0c) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008054

```text
(config-trunk-group)# default xsvc <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 20 `；EOL ` RVA 0x378FED50 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aea60ac1153f76d4](../../evidence/conditions-sets-068.md#c-aea60ac1153f76d4) · [状态效果 S-54e96429e66aa238](../../evidence/state_effects-sets-018.md#s-54e96429e66aa238)

### observed_connections-008051

```text
(config-trunk-group)# description <string> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 9 `；EOL ` RVA 0x378FEA30 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Description for the trunk group。

[条件 C-18b8c8d21c55d683](../../evidence/conditions-sets-010.md#c-18b8c8d21c55d683) · [参数 P-c8ea012ce97f5a1d](../../evidence/parameters-sets-015.md#p-c8ea012ce97f5a1d)

### observed_connections-008041

```text
(config-trunk-group)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x379008E0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73dc94413bfe1f10](../../evidence/conditions-sets-045.md#c-73dc94413bfe1f10)

### observed_connections-008040

```text
(config-trunk-group)# hunt-scheme <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 10 `；EOL ` RVA 0x378FD640 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92f3e462b95eb911](../../evidence/conditions-sets-057.md#c-92f3e462b95eb911)

### observed_connections-008060

```text
(config-trunk-group)# isdn supp-service tbct <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 11 `；EOL ` RVA 0x378FD2C0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-5fd5986b9826570f](../../evidence/state_effects-sets-021.md#s-5fd5986b9826570f)

### observed_connections-008063

```text
(config-trunk-group)# max-calls any <number:0..1000> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 2 `；EOL ` RVA 0x378FE148 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify number of allowed calls。

[条件 C-e5e81c37c004772e](../../evidence/conditions-sets-089.md#c-e5e81c37c004772e) · [参数 P-613047f548ff0e80](../../evidence/parameters-sets-008.md#p-613047f548ff0e80) · [状态效果 S-5054630a91dde518](../../evidence/state_effects-sets-018.md#s-5054630a91dde518)

### observed_connections-008048

```text
(config-trunk-group)# max-retry <number:1..5> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 8 `；EOL ` RVA 0x378FDD80 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify number of outgoing attempts。

[条件 C-0378180b63774d8a](../../evidence/conditions-sets-002.md#c-0378180b63774d8a) · [参数 P-33e83e3aad92b55d](../../evidence/parameters-sets-004.md#p-33e83e3aad92b55d)

### observed_connections-008081

```text
(config-trunk-group)# no capacity trunk-group update interval <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 1 `；EOL ` RVA 0x37900558 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5d36d4e6e30b463](../../evidence/conditions-sets-082.md#c-d5d36d4e6e30b463) · [状态效果 S-2c750ed3ecb4ec98](../../evidence/state_effects-sets-010.md#s-2c750ed3ecb4ec98)

### observed_connections-008042

```text
(config-trunk-group)# no carrier-id <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 12 `；EOL ` RVA 0x378FCC30 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc7b635ec30c2149](../../evidence/conditions-sets-073.md#c-bc7b635ec30c2149) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008050

```text
(config-trunk-group)# no description <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 9 `；EOL ` RVA 0x378FEA30 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8ac827bc887aa5cc](../../evidence/conditions-sets-054.md#c-8ac827bc887aa5cc) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008045

```text
(config-trunk-group)# no hunt-scheme <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 10 `；EOL ` RVA 0x378FD640 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-801bdbef3836c559](../../evidence/conditions-sets-050.md#c-801bdbef3836c559) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008070

```text
(config-trunk-group)# no isdn supp-service tbct <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 11 `；EOL ` RVA 0x378FD2C0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-83f804bdf7f81dbd](../../evidence/state_effects-sets-028.md#s-83f804bdf7f81dbd)

### observed_connections-008061

```text
(config-trunk-group)# no max-calls any <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 2 `；EOL ` RVA 0x378FE148 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3f266a7ed1f6b66c](../../evidence/conditions-sets-024.md#c-3f266a7ed1f6b66c) · [状态效果 S-49f0744e24f268cd](../../evidence/state_effects-sets-016.md#s-49f0744e24f268cd)

### observed_connections-008047

```text
(config-trunk-group)# no max-retry <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 8 `；EOL ` RVA 0x378FDD80 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-894cd24b0c1b4a9b](../../evidence/conditions-sets-053.md#c-894cd24b0c1b4a9b) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008067

```text
(config-trunk-group)# no preemption enable <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 17 `；EOL ` RVA 0x378FF100 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1560fc82574099c](../../evidence/conditions-sets-075.md#c-c1560fc82574099c) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008078

```text
(config-trunk-group)# no preemption guard timer <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 19 `；EOL ` RVA 0x378FF7E8 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9cb3c53ba7401873](../../evidence/conditions-sets-061.md#c-9cb3c53ba7401873) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008075

```text
(config-trunk-group)# no preemption tone timer <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 18 `；EOL ` RVA 0x378FF470 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c45bc09657304e3b](../../evidence/conditions-sets-076.md#c-c45bc09657304e3b) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008072

```text
(config-trunk-group)# no tgrep advertise trunk-group <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 0 `；EOL ` RVA 0x378FFC20 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f142c273ca91b19b](../../evidence/conditions-sets-093.md#c-f142c273ca91b19b) · [状态效果 S-31f942afd8fc7f65](../../evidence/state_effects-sets-011.md#s-31f942afd8fc7f65)

### observed_connections-008056

```text
(config-trunk-group)# no translation-profile outgoing <cr>
```

Handler ` RVA 0x1E3BB950 `；selector ` 5 `；EOL ` RVA 0x378FC8A8 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-32ac91fd18165455](../../evidence/conditions-sets-020.md#c-32ac91fd18165455) · [状态效果 S-d59a92adc5b1a631](../../evidence/state_effects-sets-045.md#s-d59a92adc5b1a631)

### observed_connections-008064

```text
(config-trunk-group)# no voice-class cause-code <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 16 `；EOL ` RVA 0x378FE6D0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bcf4d9a775bd3073](../../evidence/conditions-sets-073.md#c-bcf4d9a775bd3073) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008053

```text
(config-trunk-group)# no xsvc <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 20 `；EOL ` RVA 0x378FED50 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6f4dac6e15a3d95b](../../evidence/conditions-sets-043.md#c-6f4dac6e15a3d95b) · [状态效果 S-95101b70895ddba3](../../evidence/state_effects-sets-032.md#s-95101b70895ddba3)

### observed_connections-008055

```text
(config-trunk-group)# preemption enable <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 17 `；EOL ` RVA 0x378FF100 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ddb79c3c65bec0a5](../../evidence/conditions-sets-085.md#c-ddb79c3c65bec0a5)

### observed_connections-008079

```text
(config-trunk-group)# preemption guard timer <number:60..500> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 19 `；EOL ` RVA 0x378FF7E8 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Preemption guard timer (in milliseconds)。

[条件 C-552263f133ef9e9b](../../evidence/conditions-sets-033.md#c-552263f133ef9e9b) · [参数 P-d9bcde443188728c](../../evidence/parameters-sets-016.md#p-d9bcde443188728c)

### observed_connections-008076

```text
(config-trunk-group)# preemption tone timer <number:4..30> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 18 `；EOL ` RVA 0x378FF470 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Preemption tone timer (in seconds)。

[条件 C-4198115210600c0d](../../evidence/conditions-sets-026.md#c-4198115210600c0d) · [参数 P-38f00c5b7414e721](../../evidence/parameters-sets-005.md#p-38f00c5b7414e721)

### observed_connections-008069

```text
(config-trunk-group)# tgrep advertise trunk-group <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 0 `；EOL ` RVA 0x378FFC20 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4d700ec3a9cff97](../../evidence/conditions-sets-070.md#c-b4d700ec3a9cff97) · [状态效果 S-81e4ba1b1d4508e2](../../evidence/state_effects-sets-028.md#s-81e4ba1b1d4508e2)

### observed_connections-008073

```text
(config-trunk-group)# tgrep advertise trunk-group disable <cr>
```

Handler ` RVA 0x1E3CBDE0 `；selector ` 2 `；EOL ` RVA 0x378FFC48 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4d700ec3a9cff97](../../evidence/conditions-sets-070.md#c-b4d700ec3a9cff97) · [状态效果 S-050389097a85fc6a](../../evidence/state_effects-sets-002.md#s-050389097a85fc6a)

### observed_connections-008057

```text
(config-trunk-group)# translation-profile outgoing <string> <cr>
```

Handler ` RVA 0x1E3BB950 `；selector ` 5 `；EOL ` RVA 0x378FC8A8 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile name。

[条件 C-6accc6b93ec4e8f6](../../evidence/conditions-sets-041.md#c-6accc6b93ec4e8f6) · [参数 P-2a37235baafd88f9](../../evidence/parameters-sets-004.md#p-2a37235baafd88f9) · [状态效果 S-d1fdf4e6552cd2bd](../../evidence/state_effects-sets-044.md#s-d1fdf4e6552cd2bd)

### observed_connections-008065

```text
(config-trunk-group)# voice-class cause-code <number:1..64> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 16 `；EOL ` RVA 0x378FE6D0 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Voice class cause code tag。

[条件 C-5310db5d7f5dbfa4](../../evidence/conditions-sets-032.md#c-5310db5d7f5dbfa4) · [参数 P-98137d3cbf222bc9](../../evidence/parameters-sets-012.md#p-98137d3cbf222bc9)

### observed_connections-008039

```text
(config-trunk-group)# xsvc <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 20 `；EOL ` RVA 0x378FED50 `。

模式根 ` RVA 0x378FC6A0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a9e4ac2c338e482](../../evidence/conditions-sets-010.md#c-1a9e4ac2c338e482)
