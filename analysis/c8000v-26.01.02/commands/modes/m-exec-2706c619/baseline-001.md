# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-000608

```text
(exec)# aaa tools memleak-detection-start <cr>
```

Handler ` RVA 0x1371EB80 `；selector ` 0 `；EOL ` RVA 0x35C0E758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3)

### path-000030

```text
(exec)# access-enable <cr>
```

Handler ` RVA 0xCEEEEA0 `；selector ` 0 `；EOL ` RVA 0x33D2ACF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15f718c9cfdd67e9](../../evidence/conditions-sets-009.md#c-15f718c9cfdd67e9)

### path-000032

```text
(exec)# access-profile <cr>
```

Handler ` RVA 0xDD24680 `；selector ` 0 `；EOL ` RVA 0x34043248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [状态效果 S-3b52e1e210114bb5](../../evidence/state_effects-sets-013.md#s-3b52e1e210114bb5)

### path-004742

```text
(exec)# access-session remote-device-notification mac <address> <cr>
```

Handler ` RVA 0xCADCD00 `；selector ` 0 `；EOL ` RVA 0x33B9B6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [参数 P-a31f1e1a4ace1062](../../evidence/parameters-sets-012.md#p-a31f1e1a4ace1062)

### path-008388

```text
(exec)# access-template <number:100..199> <string> any any <cr>
```

Handler ` RVA 0xCEEFAE0 `；selector ` 0 `；EOL ` RVA 0x33D2A758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP extended access list；` string ` Name of Temp. list within the access-list。

[条件 C-15f718c9cfdd67e9](../../evidence/conditions-sets-009.md#c-15f718c9cfdd67e9) · [参数 P-2160701221db188a](../../evidence/parameters-sets-003.md#p-2160701221db188a) · [状态效果 S-4f9d900153676c1a](../../evidence/state_effects-sets-017.md#s-4f9d900153676c1a)

### path-000075

```text
(exec)# acm confirm-commit <cr>
```

Handler ` RVA 0xDED7A40 `；selector ` 0 `；EOL ` RVA 0x34095218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [状态效果 S-636f06f8ded1777f](../../evidence/state_effects-sets-021.md#s-636f06f8ded1777f)

### path-000255

```text
(exec)# alps update-circuits <cr>
```

Handler ` RVA 0x11217A80 `；selector ` 0 `；EOL ` RVA 0x3541A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3)

### path-000212

```text
(exec)# analyze memory-leak <cr>
```

Handler ` RVA 0xE0942F0 `；selector ` 0 `；EOL ` RVA 0x341F0840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af772b1fda107ee7](../../evidence/conditions-sets-068.md#c-af772b1fda107ee7) · [状态效果 S-1d1e171a5be10cf3](../../evidence/state_effects-sets-007.md#s-1d1e171a5be10cf3)

### path-004979

```text
(exec)# analyze summary memory-leak update <cr>
```

Handler ` RVA 0xE0943B0 `；selector ` 0 `；EOL ` RVA 0x341F0540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06a8fd770c3ab8bc](../../evidence/conditions-sets-003.md#c-06a8fd770c3ab8bc) · [状态效果 S-d614aaa42f84bf2e](../../evidence/state_effects-sets-045.md#s-d614aaa42f84bf2e)

### path-000244

```text
(exec)# archive config <cr>
```

Handler ` RVA 0xDEDE440 `；selector ` 0 `；EOL ` RVA 0x3409A0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3)

### path-010979

```text
(exec)# archive log config add comment <string> <cr>
```

Handler ` RVA 0xDF0B3A0 `；selector ` 0 `；EOL ` RVA 0x340A35A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Comment (up to 128 characters)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [参数 P-3088f7718888ec37](../../evidence/parameters-sets-004.md#p-3088f7718888ec37)

### path-005269

```text
(exec)# archive tar /table <string> <cr>
```

Handler ` RVA 0xD663D40 `；selector ` 0 `；EOL ` RVA 0x33EBD5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tar filename。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [参数 P-2418664fd9d768d1](../../evidence/parameters-sets-003.md#p-2418664fd9d768d1) · [状态效果 S-56c66fc1463105e0](../../evidence/state_effects-sets-019.md#s-56c66fc1463105e0)

### path-001174

```text
(exec)# authentication display config-mode <cr>
```

Handler ` RVA 0xCB10230 `；selector ` 0 `；EOL ` RVA 0x33BB23E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3)

### path-001210

```text
(exec)# authentication display legacy <cr>
```

Handler ` RVA 0xCB102D0 `；selector ` 0 `；EOL ` RVA 0x33BB26C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-515e73018ff5161e](../../evidence/conditions-sets-032.md#c-515e73018ff5161e) · [状态效果 S-28919d55f08c93c3](../../evidence/state_effects-sets-009.md#s-28919d55f08c93c3)

### path-000095

```text
(exec)# auto secure <cr>
```

Handler ` RVA 0xB246A80 `；selector ` 0 `；EOL ` RVA 0x336D4B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f234e9012469242c](../../evidence/conditions-sets-093.md#c-f234e9012469242c) · [状态效果 S-2d9b3c4be3ba4402](../../evidence/state_effects-sets-010.md#s-2d9b3c4be3ba4402)

### path-001234

```text
(exec)# beep kill session <cr>
```

Handler ` RVA 0xEF60A30 `；selector ` 1 `；EOL ` RVA 0x3448C338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3)

### path-012451

```text
(exec)# bfe enter <interface> <cr>
```

Handler ` RVA 0x1061D550 `；selector ` 0 `；EOL ` RVA 0x34BD4738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bbbbbdd381d93856](../../evidence/conditions-sets-072.md#c-bbbbbdd381d93856) · [缺口 G-a7b2fa5813a1f1f4](../../evidence/gaps-sets-006.md#g-a7b2fa5813a1f1f4) · [参数 P-b4b1c28d41cf2bc8](../../evidence/parameters-sets-014.md#p-b4b1c28d41cf2bc8) · [状态效果 S-88f9dc359204c296](../../evidence/state_effects-sets-029.md#s-88f9dc359204c296)

### path-000224

```text
(exec)# bingd stop <cr>
```

Handler ` RVA 0xF2731C0 `；selector ` 0 `；EOL ` RVA 0x345DDD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12f2c408565c054a](../../evidence/conditions-sets-007.md#c-12f2c408565c054a)

### path-001308

```text
(exec)# bingd template <string> <cr>
```

Handler ` RVA 0xF272D80 `；selector ` 0 `；EOL ` RVA 0x345DD688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` beep template to be used。

[条件 C-4a5bc1b5058663c2](../../evidence/conditions-sets-029.md#c-4a5bc1b5058663c2) · [参数 P-74a8a6af26414404](../../evidence/parameters-sets-009.md#p-74a8a6af26414404)

### path-001334

```text
(exec)# bingng template <string> <cr>
```

Handler ` RVA 0xF272900 `；selector ` 0 `；EOL ` RVA 0x345DC9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` beep template to be used。

[条件 C-b7c0b7332be331ee](../../evidence/conditions-sets-071.md#c-b7c0b7332be331ee) · [参数 P-333ae3065c8daf82](../../evidence/parameters-sets-004.md#p-333ae3065c8daf82)

### path-012518

```text
(exec)# bounce interface <interface> <cr>
```

Handler ` RVA 0xE07CD50 `；selector ` 0 `；EOL ` RVA 0x341D0040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70e210a3deae1648](../../evidence/conditions-sets-044.md#c-70e210a3deae1648) · [缺口 G-740de3f492525849](../../evidence/gaps-sets-004.md#g-740de3f492525849) · [参数 P-01fd594d89cf5e6b](../../evidence/parameters-sets-001.md#p-01fd594d89cf5e6b)

### path-025333

```text
(exec)# bounce interface range <interface> - <number:dynamic> <cr>
```

Handler ` RVA 0xE07D150 `；selector ` 0 `；EOL ` RVA 0x341CFCE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` end interface number。

[条件 C-0b1fdfe547484e8e](../../evidence/conditions-sets-005.md#c-0b1fdfe547484e8e) · [缺口 G-7fc1b162065b8e15](../../evidence/gaps-sets-005.md#g-7fc1b162065b8e15) · [参数 P-40b0a409fdb1e23f](../../evidence/parameters-sets-005.md#p-40b0a409fdb1e23f)

### path-005351

```text
(exec)# bulkstat profile <string> disable <cr>
```

Handler ` RVA 0xBC6B6A0 `；selector ` 0 `；EOL ` RVA 0x338819A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of profile。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [参数 P-feb2bca4df1d2854](../../evidence/parameters-sets-019.md#p-feb2bca4df1d2854) · [状态效果 S-1a838c1d9854a0a6](../../evidence/state_effects-sets-006.md#s-1a838c1d9854a0a6)

### path-005352

```text
(exec)# bulkstat profile <string> enable repeat <number:1..4294967294> <cr>
```

Handler ` RVA 0xBC6B6A0 `；selector ` 3 `；EOL ` RVA 0x33881C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of profile；` unsigned_number ` Number of recurrences。

[条件 C-fc758e3af277807b](../../evidence/conditions-sets-097.md#c-fc758e3af277807b) · [参数 P-b7570e5ddb9c6525](../../evidence/parameters-sets-014.md#p-b7570e5ddb9c6525) · [状态效果 S-a6ec50584889e541](../../evidence/state_effects-sets-035.md#s-a6ec50584889e541)

### path-008338

```text
(exec)# call-home debug syslog-throttling timer <number:1..86400> <cr>
```

Handler ` RVA 0xB6D4AC0 `；selector ` 0 `；EOL ` RVA 0x337F1D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-5a021525448e8c5a](../../evidence/conditions-sets-035.md#c-5a021525448e8c5a) · [参数 P-4c50fed8d94ed394](../../evidence/parameters-sets-006.md#p-4c50fed8d94ed394)

### path-004660

```text
(exec)# call-home diagnostic-signature deinstall <number:1..99999999> <cr>
```

Handler ` RVA 0x128FF210 `；selector ` 0 `；EOL ` RVA 0x337F28E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-27036f714526483c](../../evidence/conditions-sets-015.md#c-27036f714526483c) · [参数 P-590f69f5c012b06f](../../evidence/parameters-sets-007.md#p-590f69f5c012b06f)

### path-004641

```text
(exec)# call-home diagnostic-signature deinstall all <cr>
```

Handler ` RVA 0x128FF210 `；selector ` 1 `；EOL ` RVA 0x337F2638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-27036f714526483c](../../evidence/conditions-sets-015.md#c-27036f714526483c)

### path-004645

```text
(exec)# call-home diagnostic-signature download <number:1..99999999> <cr>
```

Handler ` RVA 0x128FEFD0 `；selector ` 0 `；EOL ` RVA 0x337F2338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-27036f714526483c](../../evidence/conditions-sets-015.md#c-27036f714526483c) · [参数 P-40c651dff0cca626](../../evidence/parameters-sets-005.md#p-40c651dff0cca626)

### path-004628

```text
(exec)# call-home diagnostic-signature download all <cr>
```

Handler ` RVA 0x128FEFD0 `；selector ` 1 `；EOL ` RVA 0x337F2088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-27036f714526483c](../../evidence/conditions-sets-015.md#c-27036f714526483c)

### path-004654

```text
(exec)# call-home diagnostic-signature install <number:1..99999999> <cr>
```

Handler ` RVA 0x128FF0B0 `；selector ` 0 `；EOL ` RVA 0x337F2BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-27036f714526483c](../../evidence/conditions-sets-015.md#c-27036f714526483c) · [参数 P-1b6032225704560d](../../evidence/parameters-sets-003.md#p-1b6032225704560d)

### path-004668

```text
(exec)# call-home diagnostic-signature load <string> <cr>
```

Handler ` RVA 0x128FF300 `；selector ` 0 `；EOL ` RVA 0x337F2EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DS file name。

[条件 C-27036f714526483c](../../evidence/conditions-sets-015.md#c-27036f714526483c) · [参数 P-2bddbfb1f7b5c021](../../evidence/parameters-sets-004.md#p-2bddbfb1f7b5c021)

### path-008336

```text
(exec)# call-home request config-sanity profile <string> <cr>
```

Handler ` RVA 0xB6D4930 `；selector ` 0 `；EOL ` RVA 0x337F1150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile name to use for call-home request。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [参数 P-3109956af5f1aef4](../../evidence/parameters-sets-004.md#p-3109956af5f1aef4) · [状态效果 S-f2d1cede8df68825](../../evidence/state_effects-sets-051.md#s-f2d1cede8df68825)

### path-001015

```text
(exec)# call-home request registration-info <cr>
```

Handler ` RVA 0xB6D4B70 `；selector ` 0 `；EOL ` RVA 0x337F1820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c4495070a8a1449](../../evidence/conditions-sets-048.md#c-7c4495070a8a1449) · [状态效果 S-75cf7c4125f8b198](../../evidence/state_effects-sets-025.md#s-75cf7c4125f8b198)

### path-008356

```text
(exec)# call-home send <string> email <string> <cr>
```

Handler ` RVA 0xB6D4310 `；selector ` 0 `；EOL ` RVA 0x337F07A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IOS exec command；` string ` Receiver's email address。

[条件 C-00da6473f9b5d680](../../evidence/conditions-sets-001.md#c-00da6473f9b5d680) · [参数 P-f743d2b9800ce8a1](../../evidence/parameters-sets-018.md#p-f743d2b9800ce8a1)

### path-008429

```text
(exec)# call-home send <string> tac-service-request <string> <cr>
```

Handler ` RVA 0xB6D4310 `；selector ` 0 `；EOL ` RVA 0x337EF6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IOS exec CLIs list (1-127) characters, each CLI seperated by ';'.You must enclose your CLIs list in double quotes ；` string ` TAC service request number。

[条件 C-4c3c9424632ca9f0](../../evidence/conditions-sets-030.md#c-4c3c9424632ca9f0) · [参数 P-0700e2bf3f145040](../../evidence/parameters-sets-001.md#p-0700e2bf3f145040) · [状态效果 S-9998ac3579fce04c](../../evidence/state_effects-sets-033.md#s-9998ac3579fce04c)

### path-004598

```text
(exec)# call-home send alert-group configuration <cr>
```

Handler ` RVA 0xB6D39A0 `；selector ` 0 `；EOL ` RVA 0x337EEDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f807004fc988531a](../../evidence/conditions-sets-096.md#c-f807004fc988531a) · [状态效果 S-0457b6e5eb74e67f](../../evidence/state_effects-sets-001.md#s-0457b6e5eb74e67f)

### path-008318

```text
(exec)# call-home test <string> profile <string> <cr>
```

Handler ` RVA 0xB6D3760 `；selector ` 0 `；EOL ` RVA 0x337F0C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Test message；` string ` Profile name to use for test message。

[条件 C-a4a93543b68bb731](../../evidence/conditions-sets-063.md#c-a4a93543b68bb731) · [参数 P-a026819f0ca18f5e](../../evidence/parameters-sets-012.md#p-a026819f0ca18f5e)

### path-013115

```text
(exec)# call-home test profile <string> <cr>
```

Handler ` RVA 0xB6D3760 `；selector ` 0 `；EOL ` RVA 0x337F0C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Profile name to use for test message。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-1acdd4c6fa543ec0](../../evidence/gaps-sets-001.md#g-1acdd4c6fa543ec0) · [参数 P-5b870089180de464](../../evidence/parameters-sets-007.md#p-5b870089180de464) · [状态效果 S-c234d77bd94fcc8e](../../evidence/state_effects-sets-041.md#s-c234d77bd94fcc8e)

### path-000047

```text
(exec)# cd <cr>
```

Handler ` RVA 0xD657A00 `；selector ` 0 `；EOL ` RVA 0x33EB9078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3)

### path-012265

```text
(exec)# cd <url:dynamic> <cr>
```

Handler ` RVA 0xD657A00 `；selector ` 0 `；EOL ` RVA 0x33EB9078 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c13e036612d1bc74](../../evidence/conditions-sets-075.md#c-c13e036612d1bc74) · [缺口 G-0c74e5ac3f3f6ca7](../../evidence/gaps-sets-001.md#g-0c74e5ac3f3f6ca7) · [参数 P-84d72830efdf215e](../../evidence/parameters-sets-010.md#p-84d72830efdf215e)

### path-012267

```text
(exec)# chkflash <?url_prefix_action@55558940bb90> <cr>
```

Handler ` RVA 0xD65B3F0 `；selector ` 0 `；EOL ` RVA 0x33EB7BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-980cf402e260344f](../../evidence/conditions-sets-059.md#c-980cf402e260344f) · [缺口 G-4f5ace776156a6a4](../../evidence/gaps-sets-003.md#g-4f5ace776156a6a4) · [状态效果 S-37e1839782bc8aa2](../../evidence/state_effects-sets-012.md#s-37e1839782bc8aa2)

### path-000002

```text
(exec)# clear <cr>
```

Handler ` RVA 0xE0062B0 `；selector ` 0 `；EOL ` RVA 0x3411F6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c937182aef3c67a8](../../evidence/conditions-sets-078.md#c-c937182aef3c67a8)

### path-009139

```text
(exec)# clear aaa cache filterserver acl <cr>
```

Handler ` RVA 0xCD2A390 `；selector ` 0 `；EOL ` RVA 0x3404BE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011092

```text
(exec)# clear aaa cache group <string> all <cr>
```

Handler ` RVA 0xDDEF640 `；selector ` 0 `；EOL ` RVA 0x3404C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Server group being cleared。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-65a6b53edc5dd687](../../evidence/parameters-sets-008.md#p-65a6b53edc5dd687) · [状态效果 S-c301baa62ec27385](../../evidence/state_effects-sets-041.md#s-c301baa62ec27385)

### path-005700

```text
(exec)# clear aaa counters clients <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 16 `；EOL ` RVA 0x3404B4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-009134

```text
(exec)# clear aaa counters command handler <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 17 `；EOL ` RVA 0x3404B7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005715

```text
(exec)# clear aaa counters requests <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 25 `；EOL ` RVA 0x3404BA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-009146

```text
(exec)# clear aaa counters servers all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 15 `；EOL ` RVA 0x3404B0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-34f1436b600166f5](../../evidence/state_effects-sets-012.md#s-34f1436b600166f5)

### path-005692

```text
(exec)# clear aaa local statistics <cr>
```

Handler ` RVA 0xD507150 `；selector ` 0 `；EOL ` RVA 0x33E71FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011097

```text
(exec)# clear aaa local user blocked all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 7 `；EOL ` RVA 0x33E71C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2a2eddd4bceff2d](../../evidence/conditions-sets-081.md#c-d2a2eddd4bceff2d) · [状态效果 S-d1f3822684635a27](../../evidence/state_effects-sets-044.md#s-d1f3822684635a27)

### path-011088

```text
(exec)# clear aaa local user fail-attempts all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 4 `；EOL ` RVA 0x33E718E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-be128bad73f57739](../../evidence/state_effects-sets-040.md#s-be128bad73f57739)

### path-011085

```text
(exec)# clear aaa local user lockout all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 3 `；EOL ` RVA 0x33E71550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-96ddf802d8ae42f2](../../evidence/state_effects-sets-032.md#s-96ddf802d8ae42f2)

### path-005689

```text
(exec)# clear aaa tools memleak <cr>
```

Handler ` RVA 0x1371EAF0 `；selector ` 0 `；EOL ` RVA 0x35C0DDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000574

```text
(exec)# clear access-list counters <cr>
```

Handler ` RVA 0xE0AF0F0 `；selector ` 0 `；EOL ` RVA 0x341862A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92f6f0e0febcbaf1](../../evidence/conditions-sets-057.md#c-92f6f0e0febcbaf1)

### path-004290

```text
(exec)# clear access-list fqdn statistics <cr>
```

Handler ` RVA 0xCF1C1A0 `；selector ` 0 `；EOL ` RVA 0x33D662E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-010604

```text
(exec)# clear access-template <number:100..199> <string> any any <cr>
```

Handler ` RVA 0xCEEFED0 `；selector ` 0 `；EOL ` RVA 0x33D2CF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP extended access list；` string ` Dynamic Access-list name。

[条件 C-67ba89ba0d0e3b61](../../evidence/conditions-sets-040.md#c-67ba89ba0d0e3b61) · [参数 P-f1f333f2758db219](../../evidence/parameters-sets-018.md#p-f1f333f2758db219) · [状态效果 S-c27954fb8335bd08](../../evidence/state_effects-sets-041.md#s-c27954fb8335bd08)

### path-000147

```text
(exec)# clear adjacency <cr>
```

Handler ` RVA 0xB5519E0 `；selector ` 0 `；EOL ` RVA 0x3379B228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-002137

```text
(exec)# clear alps circuits <cr>
```

Handler ` RVA 0x11217960 `；selector ` 1 `；EOL ` RVA 0x3541CD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-3629e51c6eaa5db4](../../evidence/state_effects-sets-012.md#s-3629e51c6eaa5db4)

### path-002064

```text
(exec)# clear alps counters <cr>
```

Handler ` RVA 0x11217960 `；selector ` 0 `；EOL ` RVA 0x3541C9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-013008

```text
(exec)# clear ancp interface <interface> <cr>
```

Handler ` RVA 0xB263C90 `；selector ` 0 `；EOL ` RVA 0x336DAA30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-677ecca0f8a5a8e2](../../evidence/conditions-sets-040.md#c-677ecca0f8a5a8e2) · [缺口 G-d4e9a98473901bf3](../../evidence/gaps-sets-007.md#g-d4e9a98473901bf3) · [参数 P-96232a8e091cb3ab](../../evidence/parameters-sets-012.md#p-96232a8e091cb3ab)

### path-005718

```text
(exec)# clear archive log config <cr>
```

Handler ` RVA 0xDF0B450 `；selector ` 0 `；EOL ` RVA 0x340CDF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000590

```text
(exec)# clear arp-cache <address> <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 1 `；EOL ` RVA 0x33CD7ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address。

[条件 C-5aec5c57e8109645](../../evidence/conditions-sets-036.md#c-5aec5c57e8109645) · [参数 P-86bbb0bf087473ac](../../evidence/parameters-sets-010.md#p-86bbb0bf087473ac)

### path-000104

```text
(exec)# clear arp-cache <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 0 `；EOL ` RVA 0x33CD7B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c59e3d75d7c7e95](../../evidence/conditions-sets-023.md#c-3c59e3d75d7c7e95)

### path-012315

```text
(exec)# clear arp-cache <interface> <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 0 `；EOL ` RVA 0x33CD7B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4b4bb363f4dbbc9e](../../evidence/conditions-sets-030.md#c-4b4bb363f4dbbc9e) · [缺口 G-d7f15b655f85675d](../../evidence/gaps-sets-008.md#g-d7f15b655f85675d) · [参数 P-7f95961605bb9d9e](../../evidence/parameters-sets-010.md#p-7f95961605bb9d9e)

### path-004361

```text
(exec)# clear arp-cache counters ha <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 2 `；EOL ` RVA 0x33CD8210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef7358d728ee621b](../../evidence/conditions-sets-092.md#c-ef7358d728ee621b)

### path-001464

```text
(exec)# clear avc sd-service <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 50 `；EOL ` RVA 0x3527DE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005225

```text
(exec)# clear avc sd-service cmds <cr>
```

Handler ` RVA 0x10DCF240 `；selector ` 0 `；EOL ` RVA 0x3527D8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005193

```text
(exec)# clear avc sd-service device-health <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 54 `；EOL ` RVA 0x3527D350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005243

```text
(exec)# clear avc sd-service device-table <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 51 `；EOL ` RVA 0x3527DB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80e78ec0d2841b17](../../evidence/conditions-sets-050.md#c-80e78ec0d2841b17)

### path-005211

```text
(exec)# clear avc sd-service ent-export <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 55 `；EOL ` RVA 0x3527D5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005173

```text
(exec)# clear avc sd-service flow-counters <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 53 `；EOL ` RVA 0x3527D0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c027d7a055ec0b3c](../../evidence/conditions-sets-074.md#c-c027d7a055ec0b3c)

### path-008904

```text
(exec)# clear avc sd-service telemetry-table counters <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 52 `；EOL ` RVA 0x3527DE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e581fcbe75c4fdfa](../../evidence/conditions-sets-089.md#c-e581fcbe75c4fdfa) · [状态效果 S-74b0b4bf8b5c0833](../../evidence/state_effects-sets-025.md#s-74b0b4bf8b5c0833)

### path-001207

```text
(exec)# clear bfd counters <cr>
```

Handler ` RVA 0x10B36A30 `；selector ` 0 `；EOL ` RVA 0x34CAD5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-771029134ef3937c](../../evidence/state_effects-sets-025.md#s-771029134ef3937c)

### path-001221

```text
(exec)# clear bfd dampening <cr>
```

Handler ` RVA 0x10B36A30 `；selector ` 1 `；EOL ` RVA 0x34CADBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-d6d707e4896be89c](../../evidence/state_effects-sets-046.md#s-d6d707e4896be89c)

### path-017879

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> dampening <cr>
```

Handler ` RVA 0xF1CB1C0 `；selector ` 0 `；EOL ` RVA 0x344B0AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-845fcfd8a7e75fa6](../../evidence/conditions-sets-051.md#c-845fcfd8a7e75fa6) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-017925

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> dampening <cr>
```

Handler ` RVA 0xF1CB1C0 `；selector ` 0 `；EOL ` RVA 0x3552F300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9f127ee6b4475d8](../../evidence/conditions-sets-084.md#c-d9f127ee6b4475d8) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-023960

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> flap-statistics <address> <address> <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 3 `；EOL ` RVA 0x344B1898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Network to clear flap statistics；` address ` Network mask。

[条件 C-209b292a4fa10c04](../../evidence/conditions-sets-013.md#c-209b292a4fa10c04) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [参数 P-d01527e1a7d9b5b5](../../evidence/parameters-sets-016.md#p-d01527e1a7d9b5b5) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-017926

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 2 `；EOL ` RVA 0x344B0D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e6ab6b4e658811d](../../evidence/conditions-sets-049.md#c-7e6ab6b4e658811d) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-025346

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> flap-statistics <prefix:dynamic> <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 3 `；EOL ` RVA 0x3552F730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to clear flap statistics。

[条件 C-a724b34b0a0bbe87](../../evidence/conditions-sets-064.md#c-a724b34b0a0bbe87) · [缺口 G-83134054dac990b6](../../evidence/gaps-sets-005.md#g-83134054dac990b6) · [参数 P-4063490524d45b2e](../../evidence/parameters-sets-005.md#p-4063490524d45b2e) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-023964

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> flap-statistics filter-list <number:1..500> <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 5 `；EOL ` RVA 0x344B1E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Regular expression access list number。

[条件 C-7e6ab6b4e658811d](../../evidence/conditions-sets-049.md#c-7e6ab6b4e658811d) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [参数 P-9b8d7741a45051a5](../../evidence/parameters-sets-012.md#p-9b8d7741a45051a5) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-023962

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> flap-statistics regexp <string> <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 4 `；EOL ` RVA 0x344B1B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` A regular expression to match BGP AS paths. Use "ctrl-v ?" to enter "?"。

[条件 C-7e6ab6b4e658811d](../../evidence/conditions-sets-049.md#c-7e6ab6b4e658811d) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [参数 P-eac1b0155f42b74a](../../evidence/parameters-sets-018.md#p-eac1b0155f42b74a) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-017893

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> route-map-cache <cr>
```

Handler ` RVA 0xF1CA300 `；selector ` 0 `；EOL ` RVA 0x344B2418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4c98711ec57b88e](../../evidence/conditions-sets-094.md#c-f4c98711ec57b88e) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-025041

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> rpki server <address> port <number:1..65535> <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 10 `；EOL ` RVA 0x344B2870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` BGP IPv6 rpki cache server address to clear；` unsigned_number ` port number for peer to clear。

[条件 C-ec2d00094906ac4b](../../evidence/conditions-sets-091.md#c-ec2d00094906ac4b) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [参数 P-070a8c665f6684fe](../../evidence/parameters-sets-001.md#p-070a8c665f6684fe) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-021810

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> sso statistics <cr>
```

Handler ` RVA 0xF1CA380 `；selector ` 0 `；EOL ` RVA 0x344B2BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4722372d2b0a2713](../../evidence/conditions-sets-028.md#c-4722372d2b0a2713) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-017876

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> table-map <cr>
```

Handler ` RVA 0xF1CD4A0 `；selector ` 0 `；EOL ` RVA 0x344B2170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-713264a531747075](../../evidence/conditions-sets-044.md#c-713264a531747075) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-017920

```text
(exec)# clear bgp ipv4 <?bgp_as4_action@555589a05470> table-map <cr>
```

Handler ` RVA 0xF1CD4A0 `；selector ` 0 `；EOL ` RVA 0x3552FA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d60469266d835d3d](../../evidence/conditions-sets-083.md#c-d60469266d835d3d) · [缺口 G-91648cc69dad0461](../../evidence/gaps-sets-005.md#g-91648cc69dad0461) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-001574

```text
(exec)# clear bgp ipv4 <cr>
```

Handler ` RVA 0xF1C77B0 `；selector ` 0 `；EOL ` RVA 0x344AFD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be2007c7f39bee9a](../../evidence/conditions-sets-073.md#c-be2007c7f39bee9a) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-005317

```text
(exec)# clear bgp ipv4 cease <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 7 `；EOL ` RVA 0x344B0470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be2007c7f39bee9a](../../evidence/conditions-sets-073.md#c-be2007c7f39bee9a) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-005303

```text
(exec)# clear bgp ipv4 flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 6 `；EOL ` RVA 0x344B01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be2007c7f39bee9a](../../evidence/conditions-sets-073.md#c-be2007c7f39bee9a) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-005304

```text
(exec)# clear bgp ipv4 internal <cr>
```

Handler ` RVA 0xF1CD7B0 `；selector ` 0 `；EOL ` RVA 0x344B0730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d74e39cb8a6206ff](../../evidence/conditions-sets-083.md#c-d74e39cb8a6206ff) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-017825

```text
(exec)# clear bgp ipv4 update-group <?match_ipv6_addrinfo_action@555589a05410> <cr>
```

Handler ` RVA 0xF1CA660 `；selector ` 0 `；EOL ` RVA 0x344B1160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab817c3670e85d88](../../evidence/conditions-sets-066.md#c-ab817c3670e85d88) · [缺口 G-d6b149e1fab14424](../../evidence/gaps-sets-007.md#g-d6b149e1fab14424) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-008986

```text
(exec)# clear bgp ipv4 update-group <number:1..4294967295> <cr>
```

Handler ` RVA 0xF1CA660 `；selector ` 0 `；EOL ` RVA 0x344B1160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Clear peers in the update-group。

[条件 C-ab817c3670e85d88](../../evidence/conditions-sets-066.md#c-ab817c3670e85d88) · [参数 P-37ab67deed9369de](../../evidence/parameters-sets-005.md#p-37ab67deed9369de) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-011011

```text
(exec)# clear bgp ipv4 vrf <string> dampening <cr>
```

Handler ` RVA 0xF1CB1C0 `；selector ` 0 `；EOL ` RVA 0x344B0AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-327712bbfaf11255](../../evidence/conditions-sets-020.md#c-327712bbfaf11255) · [参数 P-cd1f6e9647c25601](../../evidence/parameters-sets-016.md#p-cd1f6e9647c25601) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-011023

```text
(exec)# clear bgp ipv4 vrf <string> flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 2 `；EOL ` RVA 0x344B0D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-327712bbfaf11255](../../evidence/conditions-sets-020.md#c-327712bbfaf11255) · [参数 P-cd1f6e9647c25601](../../evidence/parameters-sets-016.md#p-cd1f6e9647c25601) · [状态效果 S-995795d6611115a2](../../evidence/state_effects-sets-033.md#s-995795d6611115a2)

### path-000293

```text
(exec)# clear bridge <cr>
```

Handler ` RVA 0xF28A710 `；selector ` 0 `；EOL ` RVA 0x345E44D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c5de2225932f4b5](../../evidence/conditions-sets-017.md#c-2c5de2225932f4b5)

### path-004583

```text
(exec)# clear bridge-domain route stats <cr>
```

Handler ` RVA 0xBF37330 `；selector ` 0 `；EOL ` RVA 0x33953F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92b38d71c29d1433](../../evidence/conditions-sets-057.md#c-92b38d71c29d1433) · [状态效果 S-a01be88be1bc6dad](../../evidence/state_effects-sets-034.md#s-a01be88be1bc6dad)

### path-000299

```text
(exec)# clear bsc <cr>
```

Handler ` RVA 0x113C36A0 `；selector ` 0 `；EOL ` RVA 0x354B4B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000301

```text
(exec)# clear bstun <cr>
```

Handler ` RVA 0x113E1220 `；selector ` 0 `；EOL ` RVA 0x354BCA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005487

```text
(exec)# clear call admission statistics <cr>
```

Handler ` RVA 0xDEB0A00 `；selector ` 0 `；EOL ` RVA 0x3408CD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56aa479a35648f3f](../../evidence/conditions-sets-034.md#c-56aa479a35648f3f)

### path-004597

```text
(exec)# clear call-home diagnostic-signature statistics <cr>
```

Handler ` RVA 0x128FF400 `；selector ` 0 `；EOL ` RVA 0x337F4010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec7415f280a351e6](../../evidence/conditions-sets-091.md#c-ec7415f280a351e6)

### path-008291

```text
(exec)# clear call-home diagnostic-signature statistics download <cr>
```

Handler ` RVA 0x128FF460 `；selector ` 0 `；EOL ` RVA 0x337F3FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec7415f280a351e6](../../evidence/conditions-sets-091.md#c-ec7415f280a351e6)

### path-004585

```text
(exec)# clear call-home smart-licensing statistics <cr>
```

Handler ` RVA 0xB6D3710 `；selector ` 0 `；EOL ` RVA 0x337F4568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be0897ad66c8df96](../../evidence/conditions-sets-073.md#c-be0897ad66c8df96)

### path-000759

```text
(exec)# clear call-home statistics <cr>
```

Handler ` RVA 0xB6D36C0 `；selector ` 0 `；EOL ` RVA 0x337F3C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000925

```text
(exec)# clear cdp counters <cr>
```

Handler ` RVA 0xCDA98F0 `；selector ` 0 `；EOL ` RVA 0x33CE01A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000944

```text
(exec)# clear cdp table <cr>
```

Handler ` RVA 0xCDA9940 `；selector ` 0 `；EOL ` RVA 0x33CE0450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-016928

```text
(exec)# clear cef interface <interface> policy-statistics <cr>
```

Handler ` RVA 0xB3DDB50 `；selector ` 0 `；EOL ` RVA 0x337647B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa067c839156fd49](../../evidence/conditions-sets-066.md#c-aa067c839156fd49) · [缺口 G-84b5e0ed5a95c48a](../../evidence/gaps-sets-005.md#g-84b5e0ed5a95c48a) · [参数 P-b26c0c4700455946](../../evidence/parameters-sets-014.md#p-b26c0c4700455946) · [状态效果 S-a8a6879c08d75814](../../evidence/state_effects-sets-036.md#s-a8a6879c08d75814)

### path-004531

```text
(exec)# clear cef interface policy-statistics <cr>
```

Handler ` RVA 0xB3DDB50 `；selector ` 0 `；EOL ` RVA 0x337647B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23601dec894d9411](../../evidence/conditions-sets-014.md#c-23601dec894d9411) · [状态效果 S-a8a6879c08d75814](../../evidence/state_effects-sets-036.md#s-a8a6879c08d75814)

### path-000957

```text
(exec)# clear cef linecard <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 3 `；EOL ` RVA 0x33733770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cc76796786e1ff4](../../evidence/conditions-sets-024.md#c-3cc76796786e1ff4)

### path-013229

```text
(exec)# clear cef linecard <number:dynamic> <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 3 `；EOL ` RVA 0x33733770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-3246612c8f0362c2](../../evidence/conditions-sets-020.md#c-3246612c8f0362c2) · [缺口 G-570e4e488c09b474](../../evidence/gaps-sets-004.md#g-570e4e488c09b474) · [参数 P-696056a0b4964e1c](../../evidence/parameters-sets-008.md#p-696056a0b4964e1c) · [状态效果 S-84644e9efc7bb85e](../../evidence/state_effects-sets-028.md#s-84644e9efc7bb85e)

### path-017074

```text
(exec)# clear cef linecard <number:dynamic> Adjacency <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 2 `；EOL ` RVA 0x33733748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-3246612c8f0362c2](../../evidence/conditions-sets-020.md#c-3246612c8f0362c2) · [缺口 G-570e4e488c09b474](../../evidence/gaps-sets-004.md#g-570e4e488c09b474) · [参数 P-696056a0b4964e1c](../../evidence/parameters-sets-008.md#p-696056a0b4964e1c) · [状态效果 S-84644e9efc7bb85e](../../evidence/state_effects-sets-028.md#s-84644e9efc7bb85e)

### path-017057

```text
(exec)# clear cef linecard <number:dynamic> Interface <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 1 `；EOL ` RVA 0x337334A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-3246612c8f0362c2](../../evidence/conditions-sets-020.md#c-3246612c8f0362c2) · [缺口 G-570e4e488c09b474](../../evidence/gaps-sets-004.md#g-570e4e488c09b474) · [参数 P-696056a0b4964e1c](../../evidence/parameters-sets-008.md#p-696056a0b4964e1c) · [状态效果 S-84644e9efc7bb85e](../../evidence/state_effects-sets-028.md#s-84644e9efc7bb85e)

### path-017040

```text
(exec)# clear cef linecard <number:dynamic> Prefix <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 0 `；EOL ` RVA 0x337331F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-3246612c8f0362c2](../../evidence/conditions-sets-020.md#c-3246612c8f0362c2) · [缺口 G-570e4e488c09b474](../../evidence/gaps-sets-004.md#g-570e4e488c09b474) · [参数 P-696056a0b4964e1c](../../evidence/parameters-sets-008.md#p-696056a0b4964e1c) · [状态效果 S-84644e9efc7bb85e](../../evidence/state_effects-sets-028.md#s-84644e9efc7bb85e)

### path-004665

```text
(exec)# clear cef linecard Adjacency <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 2 `；EOL ` RVA 0x33733748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cc76796786e1ff4](../../evidence/conditions-sets-024.md#c-3cc76796786e1ff4)

### path-004650

```text
(exec)# clear cef linecard Interface <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 1 `；EOL ` RVA 0x337334A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cc76796786e1ff4](../../evidence/conditions-sets-024.md#c-3cc76796786e1ff4)

### path-004635

```text
(exec)# clear cef linecard Prefix <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 0 `；EOL ` RVA 0x337331F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cc76796786e1ff4](../../evidence/conditions-sets-024.md#c-3cc76796786e1ff4)

### path-004607

```text
(exec)# clear cef linecard events <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 4 `；EOL ` RVA 0x33732ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cc76796786e1ff4](../../evidence/conditions-sets-024.md#c-3cc76796786e1ff4)

### path-004506

```text
(exec)# clear cef load-balance statistics <cr>
```

Handler ` RVA 0xB3F90A0 `；selector ` 0 `；EOL ` RVA 0x33764AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-004639

```text
(exec)# clear cef table IPv4 <cr>
```

Handler ` RVA 0xB5C9AD0 `；selector ` 0 `；EOL ` RVA 0x337ADA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d57f3ad92681b33](../../evidence/conditions-sets-055.md#c-8d57f3ad92681b33) · [状态效果 S-8b27dcccd59b2ee1](../../evidence/state_effects-sets-030.md#s-8b27dcccd59b2ee1)

### path-008304

```text
(exec)# clear cef table IPv4 consistency-check <cr>
```

Handler ` RVA 0xB5C9A70 `；selector ` 0 `；EOL ` RVA 0x337AD630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec19cca086ff4535](../../evidence/conditions-sets-091.md#c-ec19cca086ff4535) · [状态效果 S-8b27dcccd59b2ee1](../../evidence/state_effects-sets-030.md#s-8b27dcccd59b2ee1)

### path-001236

```text
(exec)# clear cft stats <cr>
```

Handler ` RVA 0x12945F20 `；selector ` 1 `；EOL ` RVA 0x358FD9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-debd54453a963429](../../evidence/conditions-sets-086.md#c-debd54453a963429)

### path-000665

```text
(exec)# clear checkpoint clients <cr>
```

Handler ` RVA 0xCDB61A0 `；selector ` 0 `；EOL ` RVA 0x33CEE3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000653

```text
(exec)# clear checkpoint entities <cr>
```

Handler ` RVA 0xCDB63F0 `；selector ` 0 `；EOL ` RVA 0x33CEE138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000676

```text
(exec)# clear checkpoint statistics <cr>
```

Handler ` RVA 0xCDB6600 `；selector ` 0 `；EOL ` RVA 0x33CEE688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-017252

```text
(exec)# clear class-map control <?option@555589144230> all <cr>
```

Handler ` RVA 0xCB5B220 `；selector ` 0 `；EOL ` RVA 0x33BF02D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-da23afc4682de9e9](../../evidence/conditions-sets-084.md#c-da23afc4682de9e9) · [缺口 G-fc92469ed3690db1](../../evidence/gaps-sets-009.md#g-fc92469ed3690db1) · [状态效果 S-7072a84e7035ad75](../../evidence/state_effects-sets-024.md#s-7072a84e7035ad75)

### path-001192

```text
(exec)# clear class-map control <cr>
```

Handler ` RVA 0x10A5CC50 `；selector ` 0 `；EOL ` RVA 0x34C768B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6ef759a3bcd1981](../../evidence/conditions-sets-077.md#c-c6ef759a3bcd1981)

### path-001562

```text
(exec)# clear clns cache <cr>
```

Handler ` RVA 0x10592040 `；selector ` 1 `；EOL ` RVA 0x34B6B560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001592

```text
(exec)# clear clns es-neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 2 `；EOL ` RVA 0x34B6BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001602

```text
(exec)# clear clns is-neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 3 `；EOL ` RVA 0x34B6BD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001617

```text
(exec)# clear clns neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 4 `；EOL ` RVA 0x34B6C000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001579

```text
(exec)# clear clns route <cr>
```

Handler ` RVA 0x10592040 `；selector ` 5 `；EOL ` RVA 0x34B6B808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001635

```text
(exec)# clear clns traffic <cr>
```

Handler ` RVA 0x10592040 `；selector ` 6 `；EOL ` RVA 0x34B6C2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005877

```text
(exec)# clear cns config stats <cr>
```

Handler ` RVA 0xF31ED20 `；selector ` 0 `；EOL ` RVA 0x34609B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001997

```text
(exec)# clear cns counters <cr>
```

Handler ` RVA 0xF2FE680 `；selector ` 0 `；EOL ` RVA 0x346051C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005856

```text
(exec)# clear cns event stats <cr>
```

Handler ` RVA 0xF35DEC0 `；selector ` 0 `；EOL ` RVA 0x34617250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005935

```text
(exec)# clear cns image connections <cr>
```

Handler ` RVA 0xF36DAA0 `；selector ` 0 `；EOL ` RVA 0x3461C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005903

```text
(exec)# clear cns image status <cr>
```

Handler ` RVA 0xF36D980 `；selector ` 0 `；EOL ` RVA 0x3461BDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000528

```text
(exec)# clear configuration lock <cr>
```

Handler ` RVA 0xDF3AC00 `；selector ` 0 `；EOL ` RVA 0x340B6170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-012570

```text
(exec)# clear control-plane * <cr>
```

Handler ` RVA 0xE47F2B0 `；selector ` 0 `；EOL ` RVA 0x342C48C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d59dfb718242d33](../../evidence/conditions-sets-018.md#c-2d59dfb718242d33) · [缺口 G-438f4fbee9866d57](../../evidence/gaps-sets-003.md#g-438f4fbee9866d57)

### path-000287

```text
(exec)# clear control-plane <cr>
```

Handler ` RVA 0xE47F2B0 `；selector ` 0 `；EOL ` RVA 0x342C48C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-012348

```text
(exec)# clear controller <?controller_action@55558994af58> <cr>
```

Handler ` RVA 0xECFF830 `；selector ` 0 `；EOL ` RVA 0x343F76A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b715f0e21c92f4f0](../../evidence/conditions-sets-071.md#c-b715f0e21c92f4f0) · [缺口 G-25e0732cce9e0318](../../evidence/gaps-sets-002.md#g-25e0732cce9e0318)

### path-000588

```text
(exec)# clear controller all <cr>
```

Handler ` RVA 0xECFC750 `；selector ` 0 `；EOL ` RVA 0x343F6970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-62aad64ca365dc1f](../../evidence/conditions-sets-038.md#c-62aad64ca365dc1f)

### path-012894

```text
(exec)# clear controller hw-module <?slotcard_func_action@55558994ac18> <cr>
```

Handler ` RVA 0xECFC7D0 `；selector ` 0 `；EOL ` RVA 0x343F6C80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-62aad64ca365dc1f](../../evidence/conditions-sets-038.md#c-62aad64ca365dc1f) · [缺口 G-fdf826f0ac0ccb33](../../evidence/gaps-sets-009.md#g-fdf826f0ac0ccb33)

### path-000066

```text
(exec)# clear counters <cr>
```

Handler ` RVA 0xE40DC10 `；selector ` 0 `；EOL ` RVA 0x3411FD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22522dbe85960628](../../evidence/conditions-sets-013.md#c-22522dbe85960628)

### path-012284

```text
(exec)# clear counters <interface> <cr>
```

Handler ` RVA 0xE40DC10 `；selector ` 0 `；EOL ` RVA 0x3411FD38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7c366d42e3b6b208](../../evidence/conditions-sets-048.md#c-7c366d42e3b6b208) · [缺口 G-09e00ad83fe20fed](../../evidence/gaps-sets-001.md#g-09e00ad83fe20fed) · [参数 P-0ee8e4512bd3a472](../../evidence/parameters-sets-002.md#p-0ee8e4512bd3a472)

### path-005672

```text
(exec)# clear crypto autovpn session <cr>
```

Handler ` RVA 0x165EC340 `；selector ` 1 `；EOL ` RVA 0x35FA6D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011084

```text
(exec)# clear crypto autovpn session peer <number:1..2147483647> <cr>
```

Handler ` RVA 0x165EC340 `；selector ` 0 `；EOL ` RVA 0x35FA6DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peerno。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-5d2397c60ef477d4](../../evidence/parameters-sets-007.md#p-5d2397c60ef477d4)

### path-005657

```text
(exec)# clear crypto ceal statistics <cr>
```

Handler ` RVA 0x120E8990 `；selector ` 0 `；EOL ` RVA 0x3579FA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-9c37f78c7467f1c1](../../evidence/state_effects-sets-033.md#s-9c37f78c7467f1c1)

### path-021915

```text
(exec)# clear crypto engine accelerator counter <?slotcard_func_action@55558ace60a0> <cr>
```

Handler ` RVA 0x120CAC10 `；selector ` 0 `；EOL ` RVA 0x357920E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b3128fd50605a6a1](../../evidence/conditions-sets-069.md#c-b3128fd50605a6a1) · [缺口 G-2f46a787b46f453b](../../evidence/gaps-sets-002.md#g-2f46a787b46f453b)

### path-009140

```text
(exec)# clear crypto engine accelerator counter <cr>
```

Handler ` RVA 0x120CAC10 `；selector ` 0 `；EOL ` RVA 0x357920E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94a53424b4154ed5](../../evidence/conditions-sets-057.md#c-94a53424b4154ed5)

### path-005675

```text
(exec)# clear crypto ha statistics <cr>
```

Handler ` RVA 0x1924CF00 `；selector ` 0 `；EOL ` RVA 0x3697A7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84ebe2b240fdb7c2](../../evidence/conditions-sets-051.md#c-84ebe2b240fdb7c2)

### path-005634

```text
(exec)# clear crypto pki benchmarks <cr>
```

Handler ` RVA 0x120B7E10 `；selector ` 0 `；EOL ` RVA 0x35752EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005606

```text
(exec)# clear crypto pki counters <cr>
```

Handler ` RVA 0x11FC7870 `；selector ` 0 `；EOL ` RVA 0x35752C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005663

```text
(exec)# clear crypto pki crl <cr>
```

Handler ` RVA 0x11F2ECF0 `；selector ` 0 `；EOL ` RVA 0x35753188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001840

```text
(exec)# clear cts credentials <cr>
```

Handler ` RVA 0x13047780 `；selector ` 0 `；EOL ` RVA 0x35A1D248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06a42be64c2bfd77](../../evidence/conditions-sets-003.md#c-06a42be64c2bfd77) · [状态效果 S-19501804a603b27b](../../evidence/state_effects-sets-006.md#s-19501804a603b27b)

### path-021991

```text
(exec)# clear cts macsec counters interface <interface> <cr>
```

Handler ` RVA 0x16072240 `；selector ` 0 `；EOL ` RVA 0x35EADEA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f492d28be08982ac](../../evidence/conditions-sets-094.md#c-f492d28be08982ac) · [缺口 G-ca6df055b893597a](../../evidence/gaps-sets-007.md#g-ca6df055b893597a) · [参数 P-94b5c72b1be973e2](../../evidence/parameters-sets-011.md#p-94b5c72b1be973e2)

### path-006100

```text
(exec)# clear cts role-based counters <cr>
```

Handler ` RVA 0x141FE9C0 `；selector ` 0 `；EOL ` RVA 0x35CFE5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17b07a74b31aa441](../../evidence/conditions-sets-009.md#c-17b07a74b31aa441) · [状态效果 S-90f4a000888d346c](../../evidence/state_effects-sets-031.md#s-90f4a000888d346c)

### path-017928

```text
(exec)# clear device-tracking counters interface <interface> <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1023 `；EOL ` RVA 0x35BD7398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71111e15888e204e](../../evidence/conditions-sets-044.md#c-71111e15888e204e) · [缺口 G-37f8de854955c390](../../evidence/gaps-sets-002.md#g-37f8de854955c390) · [参数 P-d642a75acd880839](../../evidence/parameters-sets-016.md#p-d642a75acd880839) · [状态效果 S-b1124f8d7b9b70b6](../../evidence/state_effects-sets-038.md#s-b1124f8d7b9b70b6)

### path-009059

```text
(exec)# clear device-tracking database policy <string> <cr>
```

Handler ` RVA 0x136806D0 `；selector ` 1020 `；EOL ` RVA 0x35BD6BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Snooping Policy name to be cleared。

[条件 C-c8acded231f1ee98](../../evidence/conditions-sets-077.md#c-c8acded231f1ee98) · [参数 P-e868e12c898fe3d6](../../evidence/parameters-sets-017.md#p-e868e12c898fe3d6) · [状态效果 S-2ff2766492b1fc46](../../evidence/state_effects-sets-011.md#s-2ff2766492b1fc46)

### path-001670

```text
(exec)# clear device-tracking events <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1021 `；EOL ` RVA 0x35BD7808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8acded231f1ee98](../../evidence/conditions-sets-077.md#c-c8acded231f1ee98)

### path-017954

```text
(exec)# clear device-tracking internal dhcp-server-stats <?ipv4orv6_addr_action@55558b12bd98> <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1024 `；EOL ` RVA 0x35BD7DD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7996a6489ee805f8](../../evidence/conditions-sets-047.md#c-7996a6489ee805f8) · [缺口 G-d18744c1fa505787](../../evidence/gaps-sets-007.md#g-d18744c1fa505787)

### path-001692

```text
(exec)# clear device-tracking messages <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1022 `；EOL ` RVA 0x35BD7AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8acded231f1ee98](../../evidence/conditions-sets-077.md#c-c8acded231f1ee98)

### path-001632

```text
(exec)# clear dhcp-server-tracking database <cr>
```

Handler ` RVA 0x136A1FB0 `；selector ` 0 `；EOL ` RVA 0x35C01760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-002144

```text
(exec)# clear diagnostic event-log <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927497faab9c3532](../../evidence/conditions-sets-056.md#c-927497faab9c3532) · [状态效果 S-3bceb42f45fb4f54](../../evidence/state_effects-sets-013.md#s-3bceb42f45fb4f54)

### path-018496

```text
(exec)# clear diagnostic event-log slot <?option@5555898dce18> <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d1d441cc661227f](../../evidence/conditions-sets-018.md#c-2d1d441cc661227f) · [缺口 G-b9e008878621b54e](../../evidence/gaps-sets-007.md#g-b9e008878621b54e) · [状态效果 S-3821033864acbb8d](../../evidence/state_effects-sets-012.md#s-3821033864acbb8d)

### path-009267

```text
(exec)# clear diagnostic event-log slot all <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a2b56cc4054aac48](../../evidence/conditions-sets-063.md#c-a2b56cc4054aac48) · [状态效果 S-b0b19c66a11a3f61](../../evidence/state_effects-sets-037.md#s-b0b19c66a11a3f61)

### path-000111

```text
(exec)# clear dialer <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 0 `；EOL ` RVA 0x34666688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e91f66fb0a1433cf](../../evidence/conditions-sets-090.md#c-e91f66fb0a1433cf)

### path-012341

```text
(exec)# clear dialer <interface> <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 0 `；EOL ` RVA 0x34666688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-55ae41c4122977f9](../../evidence/conditions-sets-034.md#c-55ae41c4122977f9) · [缺口 G-95188e2e92b7e50b](../../evidence/gaps-sets-005.md#g-95188e2e92b7e50b) · [参数 P-ec3bdcfd7179c229](../../evidence/parameters-sets-018.md#p-ec3bdcfd7179c229)

### path-008162

```text
(exec)# clear dialer dnis group <string> <cr>
```

Handler ` RVA 0xF4E9360 `；selector ` 0 `；EOL ` RVA 0x34674518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS group name。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-05f42c525d7c2f8f](../../evidence/parameters-sets-001.md#p-05f42c525d7c2f8f)

### path-008145

```text
(exec)# clear dialer dnis number <string> <cr>
```

Handler ` RVA 0xF4E9130 `；selector ` 1 `；EOL ` RVA 0x34673F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS number。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-a6076225f83e98fc](../../evidence/parameters-sets-013.md#p-a6076225f83e98fc)

### path-010482

```text
(exec)# clear dialer dnis range <string> <string> <cr>
```

Handler ` RVA 0xF4E9130 `；selector ` 2 `；EOL ` RVA 0x34674258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS range start；` string ` DNIS range end。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-6ff2f7c7e2918e74](../../evidence/parameters-sets-009.md#p-6ff2f7c7e2918e74)

### path-000622

```text
(exec)# clear dialer sessions <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 1 `；EOL ` RVA 0x34673BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-006433

```text
(exec)# clear diameter gx statistics <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 22 `；EOL ` RVA 0x338ADE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf42b62376e3a30b](../../evidence/conditions-sets-074.md#c-bf42b62376e3a30b)

### path-009478

```text
(exec)# clear diameter peer connection all <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 34 `；EOL ` RVA 0x338AD2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf42b62376e3a30b](../../evidence/conditions-sets-074.md#c-bf42b62376e3a30b)

### path-011264

```text
(exec)# clear diameter peer connection name <string> <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 21 `；EOL ` RVA 0x338AD598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Peer name。

[条件 C-bf42b62376e3a30b](../../evidence/conditions-sets-074.md#c-bf42b62376e3a30b) · [参数 P-ac0b956092f2b047](../../evidence/parameters-sets-013.md#p-ac0b956092f2b047)

### path-009499

```text
(exec)# clear diameter peer statistics all <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 36 `；EOL ` RVA 0x338AD870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf42b62376e3a30b](../../evidence/conditions-sets-074.md#c-bf42b62376e3a30b)

### path-011271

```text
(exec)# clear diameter peer statistics name <string> <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 35 `；EOL ` RVA 0x338ADB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Peer name。

[条件 C-bf42b62376e3a30b](../../evidence/conditions-sets-074.md#c-bf42b62376e3a30b) · [参数 P-56d578d820d5ba55](../../evidence/parameters-sets-007.md#p-56d578d820d5ba55)

### path-018050

```text
(exec)# clear dlep client <interface> <number:1..2147483647> <cr>
```

Handler ` RVA 0x132D3330 `；selector ` 1 `；EOL ` RVA 0x35A59B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Peer ID。

[条件 C-f9cf0863f6645c4f](../../evidence/conditions-sets-096.md#c-f9cf0863f6645c4f) · [缺口 G-420e468b371e5b1d](../../evidence/gaps-sets-003.md#g-420e468b371e5b1d) · [参数 P-027f888b654eb87c](../../evidence/parameters-sets-001.md#p-027f888b654eb87c)

### path-001854

```text
(exec)# clear dlep counters <cr>
```

Handler ` RVA 0x132D3330 `；selector ` 3 `；EOL ` RVA 0x35A5A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05474243150ac9d0](../../evidence/conditions-sets-002.md#c-05474243150ac9d0)

### path-014153

```text
(exec)# clear dlep counters <interface> <cr>
```

Handler ` RVA 0x132D3330 `；selector ` 4 `；EOL ` RVA 0x35A5A2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e039c376ca57172b](../../evidence/conditions-sets-086.md#c-e039c376ca57172b) · [缺口 G-5227fd34b33e39df](../../evidence/gaps-sets-003.md#g-5227fd34b33e39df) · [参数 P-71f6efd962bcda1f](../../evidence/parameters-sets-009.md#p-71f6efd962bcda1f)

### path-018067

```text
(exec)# clear dlep neighbor <interface> <number:1..2147483647> <cr>
```

Handler ` RVA 0x132D3330 `；selector ` 2 `；EOL ` RVA 0x35A59F70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Session ID。

[条件 C-85868229cce54f28](../../evidence/conditions-sets-052.md#c-85868229cce54f28) · [缺口 G-4a729fef6780d9a0](../../evidence/gaps-sets-003.md#g-4a729fef6780d9a0) · [参数 P-abcf0b5b9afbcb72](../../evidence/parameters-sets-013.md#p-abcf0b5b9afbcb72)

### path-002188

```text
(exec)# clear dlsw reachability <cr>
```

Handler ` RVA 0x11421C60 `；selector ` 0 `；EOL ` RVA 0x354CC100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13819f00641bcb90](../../evidence/conditions-sets-008.md#c-13819f00641bcb90) · [状态效果 S-0aa73c65d4bc2b5c](../../evidence/state_effects-sets-003.md#s-0aa73c65d4bc2b5c)

### path-002140

```text
(exec)# clear dmvpn statistics <cr>
```

Handler ` RVA 0xF4F28F0 `；selector ` 0 `；EOL ` RVA 0x3467EC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7bbd3dcd9e8792a5](../../evidence/conditions-sets-048.md#c-7bbd3dcd9e8792a5) · [状态效果 S-1db7418f52ec63d8](../../evidence/state_effects-sets-007.md#s-1db7418f52ec63d8)

### path-002073

```text
(exec)# clear drip counters <cr>
```

Handler ` RVA 0x112B2F80 `；selector ` 1 `；EOL ` RVA 0x3544D280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000523

```text
(exec)# clear dspfarm statistics <cr>
```

Handler ` RVA 0x188BAB20 `；selector ` 0 `；EOL ` RVA 0x367F3F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-87c4ba360dc721e5](../../evidence/state_effects-sets-029.md#s-87c4ba360dc721e5)

### path-001313

```text
(exec)# clear dtp counter <cr>
```

Handler ` RVA 0x15F14E10 `；selector ` 0 `；EOL ` RVA 0x35E66F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-009078

```text
(exec)# clear eigrp address-family ipv4 events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346B5888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5a65ff0d4685a5f](../../evidence/conditions-sets-076.md#c-c5a65ff0d4685a5f) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-009073

```text
(exec)# clear eigrp address-family ipv4 logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346B55E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5a65ff0d4685a5f](../../evidence/conditions-sets-076.md#c-c5a65ff0d4685a5f) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-009091

```text
(exec)# clear eigrp address-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346B4A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f6c16a554eaaa2a](../../evidence/conditions-sets-049.md#c-7f6c16a554eaaa2a) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-021865

```text
(exec)# clear eigrp address-family ipv4 neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346B4A60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-96e3b3eb22bd72a5](../../evidence/conditions-sets-058.md#c-96e3b3eb22bd72a5) · [缺口 G-9942a434d849f583](../../evidence/gaps-sets-006.md#g-9942a434d849f583) · [参数 P-2f56401a63b121e6](../../evidence/parameters-sets-004.md#p-2f56401a63b121e6) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-009095

```text
(exec)# clear eigrp address-family ipv4 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 73 `；EOL ` RVA 0x346B5DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5a65ff0d4685a5f](../../evidence/conditions-sets-076.md#c-c5a65ff0d4685a5f) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-011783

```text
(exec)# clear eigrp address-family ipv4 topology <address> <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346B4EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-c5a65ff0d4685a5f](../../evidence/conditions-sets-076.md#c-c5a65ff0d4685a5f) · [参数 P-3fb9dae9bb0abdd4](../../evidence/parameters-sets-005.md#p-3fb9dae9bb0abdd4) · [状态效果 S-6bcc427703247f28](../../evidence/state_effects-sets-023.md#s-6bcc427703247f28)

### path-021875

```text
(exec)# clear eigrp address-family ipv4 topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346B4EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-2cdf6edc5f3cc504](../../evidence/conditions-sets-018.md#c-2cdf6edc5f3cc504) · [缺口 G-5d217aedceaccceb](../../evidence/gaps-sets-004.md#g-5d217aedceaccceb) · [参数 P-fde01b13da4c6a73](../../evidence/parameters-sets-019.md#p-fde01b13da4c6a73) · [状态效果 S-104eabb670cd0ae7](../../evidence/state_effects-sets-004.md#s-104eabb670cd0ae7)

### path-011070

```text
(exec)# clear eigrp address-family ipv4 topology active <cr>
```

Handler ` RVA 0xF573DF0 `；selector ` 69 `；EOL ` RVA 0x346B51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5a65ff0d4685a5f](../../evidence/conditions-sets-076.md#c-c5a65ff0d4685a5f) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-009088

```text
(exec)# clear eigrp address-family ipv4 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 70 `；EOL ` RVA 0x346B5B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c5a65ff0d4685a5f](../../evidence/conditions-sets-076.md#c-c5a65ff0d4685a5f) · [状态效果 S-6b6190cc49d04d91](../../evidence/state_effects-sets-023.md#s-6b6190cc49d04d91)

### path-009074

```text
(exec)# clear eigrp address-family ipv6 events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x35453F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f221ea2aa6b4a75](../../evidence/conditions-sets-024.md#c-3f221ea2aa6b4a75) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-009066

```text
(exec)# clear eigrp address-family ipv6 logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x35453C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f221ea2aa6b4a75](../../evidence/conditions-sets-024.md#c-3f221ea2aa6b4a75) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-009080

```text
(exec)# clear eigrp address-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35453180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5d3bed64ded0beb2](../../evidence/conditions-sets-036.md#c-5d3bed64ded0beb2) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-021856

```text
(exec)# clear eigrp address-family ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35453180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-45c333ad8858cb17](../../evidence/conditions-sets-027.md#c-45c333ad8858cb17) · [缺口 G-de10b3f6cddc8fbb](../../evidence/gaps-sets-008.md#g-de10b3f6cddc8fbb) · [参数 P-76dabc69c1f3ad87](../../evidence/parameters-sets-009.md#p-76dabc69c1f3ad87) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-009089

```text
(exec)# clear eigrp address-family ipv6 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 73 `；EOL ` RVA 0x35454478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f221ea2aa6b4a75](../../evidence/conditions-sets-024.md#c-3f221ea2aa6b4a75) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-021857

```text
(exec)# clear eigrp address-family ipv6 topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x35453600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to clear from topology。

[条件 C-4748cb16aba1fb2b](../../evidence/conditions-sets-028.md#c-4748cb16aba1fb2b) · [缺口 G-db7a19a034d8c915](../../evidence/gaps-sets-008.md#g-db7a19a034d8c915) · [参数 P-377578bc8d963cfc](../../evidence/parameters-sets-005.md#p-377578bc8d963cfc) · [状态效果 S-4175607beb5fb07a](../../evidence/state_effects-sets-014.md#s-4175607beb5fb07a)

### path-011061

```text
(exec)# clear eigrp address-family ipv6 topology active <cr>
```

Handler ` RVA 0xF573DF0 `；selector ` 69 `；EOL ` RVA 0x35453878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f221ea2aa6b4a75](../../evidence/conditions-sets-024.md#c-3f221ea2aa6b4a75) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-009079

```text
(exec)# clear eigrp address-family ipv6 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 70 `；EOL ` RVA 0x354541D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f221ea2aa6b4a75](../../evidence/conditions-sets-024.md#c-3f221ea2aa6b4a75) · [状态效果 S-98d95e2ee83f16eb](../../evidence/state_effects-sets-032.md#s-98d95e2ee83f16eb)

### path-009049

```text
(exec)# clear eigrp service-family external-client <string> <cr>
```

Handler ` RVA 0x104726A0 `；selector ` 41 `；EOL ` RVA 0x34B3AB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client Label。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-6e6d51b6eb7ccc0f](../../evidence/parameters-sets-009.md#p-6e6d51b6eb7ccc0f) · [状态效果 S-84c833b806eb99d2](../../evidence/state_effects-sets-028.md#s-84c833b806eb99d2)

### path-009077

```text
(exec)# clear eigrp service-family ipv4 events <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 71 `；EOL ` RVA 0x346EFFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4511e4ce718b5f5f](../../evidence/conditions-sets-027.md#c-4511e4ce718b5f5f) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-009072

```text
(exec)# clear eigrp service-family ipv4 logging <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 72 `；EOL ` RVA 0x346EFD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4511e4ce718b5f5f](../../evidence/conditions-sets-027.md#c-4511e4ce718b5f5f) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-009090

```text
(exec)# clear eigrp service-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x346EEFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af75949bc0622d83](../../evidence/conditions-sets-068.md#c-af75949bc0622d83) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-021864

```text
(exec)# clear eigrp service-family ipv4 neighbors <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x346EEFE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ef692ca430ec8d81](../../evidence/conditions-sets-092.md#c-ef692ca430ec8d81) · [缺口 G-9496c3a0ba2b429c](../../evidence/gaps-sets-005.md#g-9496c3a0ba2b429c) · [参数 P-084e102a1e8ab2f2](../../evidence/parameters-sets-001.md#p-084e102a1e8ab2f2) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-012208

```text
(exec)# clear eigrp service-family ipv4 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x346EF660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-e15d9eeec52de666](../../evidence/conditions-sets-087.md#c-e15d9eeec52de666) · [参数 P-981a610bcc4e38b2](../../evidence/parameters-sets-012.md#p-981a610bcc4e38b2) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-011065

```text
(exec)# clear eigrp service-family ipv4 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x346EF930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4511e4ce718b5f5f](../../evidence/conditions-sets-027.md#c-4511e4ce718b5f5f) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-009087

```text
(exec)# clear eigrp service-family ipv4 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x346F0288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4511e4ce718b5f5f](../../evidence/conditions-sets-027.md#c-4511e4ce718b5f5f) · [状态效果 S-b06366f4e0bd8683](../../evidence/state_effects-sets-037.md#s-b06366f4e0bd8683)

### path-009094

```text
(exec)# clear eigrp service-family ipv6 events <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 71 `；EOL ` RVA 0x35476980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f24fb0c4ccd81948](../../evidence/conditions-sets-094.md#c-f24fb0c4ccd81948) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-009086

```text
(exec)# clear eigrp service-family ipv6 logging <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 72 `；EOL ` RVA 0x354766D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f24fb0c4ccd81948](../../evidence/conditions-sets-094.md#c-f24fb0c4ccd81948) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-009103

```text
(exec)# clear eigrp service-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x35475988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4489464fcd644a28](../../evidence/conditions-sets-027.md#c-4489464fcd644a28) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-021880

```text
(exec)# clear eigrp service-family ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x35475988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a1f435c39236ae6b](../../evidence/conditions-sets-063.md#c-a1f435c39236ae6b) · [缺口 G-57fa5f4bc32a0961](../../evidence/gaps-sets-004.md#g-57fa5f4bc32a0961) · [参数 P-85069a83d9913ff2](../../evidence/parameters-sets-010.md#p-85069a83d9913ff2) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-012209

```text
(exec)# clear eigrp service-family ipv6 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x35476000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-88831771e0947da3](../../evidence/conditions-sets-053.md#c-88831771e0947da3) · [参数 P-b117aaae787be4fd](../../evidence/parameters-sets-013.md#p-b117aaae787be4fd) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-011074

```text
(exec)# clear eigrp service-family ipv6 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x354762D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f24fb0c4ccd81948](../../evidence/conditions-sets-094.md#c-f24fb0c4ccd81948) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-009101

```text
(exec)# clear eigrp service-family ipv6 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x35476C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f24fb0c4ccd81948](../../evidence/conditions-sets-094.md#c-f24fb0c4ccd81948) · [状态效果 S-e2023bb15acf622d](../../evidence/state_effects-sets-048.md#s-e2023bb15acf622d)

### path-000924

```text
(exec)# clear entry <number:0..256> <cr>
```

Handler ` RVA 0xCCF7FE0 `；selector ` 0 `；EOL ` RVA 0x33C66A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Queue entry number。

[条件 C-1710bd1a949ace27](../../evidence/conditions-sets-009.md#c-1710bd1a949ace27) · [参数 P-baff37d66d7bf69e](../../evidence/parameters-sets-014.md#p-baff37d66d7bf69e)

### path-001930

```text
(exec)# clear environment counters <cr>
```

Handler ` RVA 0xE123D20 `；selector ` 16 `；EOL ` RVA 0x3420AE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000650

```text
(exec)# clear eobc counters <cr>
```

Handler ` RVA 0xED896F0 `；selector ` 0 `；EOL ` RVA 0x3442E440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000663

```text
(exec)# clear eobc interface <cr>
```

Handler ` RVA 0xED897B0 `；selector ` 0 `；EOL ` RVA 0x3442E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-014711

```text
(exec)# clear errdisable <interface> recover-link <cr>
```

Handler ` RVA 0x15E5A980 `；selector ` 5 `；EOL ` RVA 0x35E2AE58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41af6f5a805196b7](../../evidence/conditions-sets-026.md#c-41af6f5a805196b7) · [缺口 G-3556a2d5e51e383c](../../evidence/gaps-sets-002.md#g-3556a2d5e51e383c) · [参数 P-3241337386bbc684](../../evidence/parameters-sets-004.md#p-3241337386bbc684) · [状态效果 S-3c85b7f06e78fcee](../../evidence/state_effects-sets-013.md#s-3c85b7f06e78fcee)

### path-014699

```text
(exec)# clear errdisable <interface> vlan <cr>
```

Handler ` RVA 0x15E5A980 `；selector ` 4 `；EOL ` RVA 0x35E2A958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfe2197936fa19c3](../../evidence/conditions-sets-074.md#c-bfe2197936fa19c3) · [缺口 G-3556a2d5e51e383c](../../evidence/gaps-sets-002.md#g-3556a2d5e51e383c) · [参数 P-3241337386bbc684](../../evidence/parameters-sets-004.md#p-3241337386bbc684)

### path-018796

```text
(exec)# clear errdisable <interface> vlan <string> <cr>
```

Handler ` RVA 0x15E5A980 `；selector ` 3 `；EOL ` RVA 0x35E2A930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` list of vlans to clear, or &lt;cr&gt; for all vlans。

[条件 C-bfe2197936fa19c3](../../evidence/conditions-sets-074.md#c-bfe2197936fa19c3) · [缺口 G-3556a2d5e51e383c](../../evidence/gaps-sets-002.md#g-3556a2d5e51e383c) · [参数 P-b9787b4f9341097c](../../evidence/parameters-sets-014.md#p-b9787b4f9341097c)

### path-012079

```text
(exec)# clear ethernet cfm ais domain <string> mpid <number:1..8191> port <cr>
```

Handler ` RVA 0xBDD3860 `；selector ` 0 `；EOL ` RVA 0x338CDFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-0a839349463db648](../../evidence/conditions-sets-004.md#c-0a839349463db648) · [参数 P-d12e398db42d71ec](../../evidence/parameters-sets-016.md#p-d12e398db42d71ec) · [状态效果 S-8d097997d0d9eabf](../../evidence/state_effects-sets-030.md#s-8d097997d0d9eabf)

### path-023378

```text
(exec)# clear ethernet cfm ais link-status Interface <interface> <cr>
```

Handler ` RVA 0xBDD3780 `；selector ` 0 `；EOL ` RVA 0x338CDB70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8ffedf50cb91b52f](../../evidence/conditions-sets-056.md#c-8ffedf50cb91b52f) · [缺口 G-f560e27589ff51cb](../../evidence/gaps-sets-008.md#g-f560e27589ff51cb) · [参数 P-878c009ee9041459](../../evidence/parameters-sets-010.md#p-878c009ee9041459)

### path-004618

```text
(exec)# clear ethernet cfm ccm-learning-database <cr>
```

Handler ` RVA 0xBDD3D70 `；selector ` 0 `；EOL ` RVA 0x338CF840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07dc1bc4e094be04](../../evidence/conditions-sets-003.md#c-07dc1bc4e094be04) · [状态效果 S-da65f5a80c2d75c5](../../evidence/state_effects-sets-046.md#s-da65f5a80c2d75c5)

### path-004526

```text
(exec)# clear ethernet cfm errors <cr>
```

Handler ` RVA 0xBDD2B30 `；selector ` 0 `；EOL ` RVA 0x338CE920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b79c681f496f0f95](../../evidence/conditions-sets-071.md#c-b79c681f496f0f95) · [状态效果 S-94f3d576eba05297](../../evidence/state_effects-sets-032.md#s-94f3d576eba05297)

### path-008242

```text
(exec)# clear ethernet cfm fast-timeout statistics <cr>
```

Handler ` RVA 0xBDD3CD0 `；selector ` 0 `；EOL ` RVA 0x338CF3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-534e0c1aee4b8763](../../evidence/conditions-sets-033.md#c-534e0c1aee4b8763)

### path-010510

```text
(exec)# clear ethernet cfm latching-loopback discover-phase mep <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 1 `；EOL ` RVA 0x338CD438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f) · [状态效果 S-f2467369201cd364](../../evidence/state_effects-sets-051.md#s-f2467369201cd364)

### path-010507

```text
(exec)# clear ethernet cfm latching-loopback discover-phase mip <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 2 `；EOL ` RVA 0x338CD6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f) · [状态效果 S-abe4a8f270f10b1d](../../evidence/state_effects-sets-036.md#s-abe4a8f270f10b1d)

### path-008169

```text
(exec)# clear ethernet cfm maintenance-points remote <cr>
```

Handler ` RVA 0xBDD28E0 `；selector ` 0 `；EOL ` RVA 0x338CC7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f)

### path-011599

```text
(exec)# clear ethernet cfm maintenance-points remote domain <string> <cr>
```

Handler ` RVA 0xBDD2A20 `；selector ` 0 `；EOL ` RVA 0x338CC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f) · [参数 P-b4f885fc792161b1](../../evidence/parameters-sets-014.md#p-b4f885fc792161b1)

### path-011603

```text
(exec)# clear ethernet cfm pm session db <number:0..8000> <cr>
```

Handler ` RVA 0xBE8C2A0 `；selector ` 0 `；EOL ` RVA 0x339155B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session Id。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f) · [参数 P-c0ee7e00d5a1eec9](../../evidence/parameters-sets-015.md#p-c0ee7e00d5a1eec9) · [状态效果 S-5ad2d32d22b2a548](../../evidence/state_effects-sets-020.md#s-5ad2d32d22b2a548)

### path-004439

```text
(exec)# clear ethernet cfm statistics <cr>
```

Handler ` RVA 0xBDD3070 `；selector ` 0 `；EOL ` RVA 0x338CD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f)

### path-004411

```text
(exec)# clear ethernet cfm traceroute-cache <cr>
```

Handler ` RVA 0xBDD3D20 `；selector ` 0 `；EOL ` RVA 0x338CCD08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f)

### path-004402

```text
(exec)# clear ethernet lmi statistics <cr>
```

Handler ` RVA 0xBEC38F0 `；selector ` 0 `；EOL ` RVA 0x339203E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da510826a0bbdec4](../../evidence/conditions-sets-084.md#c-da510826a0bbdec4)

### path-016809

```text
(exec)# clear ethernet lmi statistics <interface> <cr>
```

Handler ` RVA 0xBEC38F0 `；selector ` 0 `；EOL ` RVA 0x339203E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2291dd11fd2f7644](../../evidence/conditions-sets-014.md#c-2291dd11fd2f7644) · [缺口 G-8c4906c49f660d40](../../evidence/gaps-sets-005.md#g-8c4906c49f660d40) · [参数 P-711b12ab2ac057ea](../../evidence/parameters-sets-009.md#p-711b12ab2ac057ea)

### path-004399

```text
(exec)# clear ethernet oam statistics <cr>
```

Handler ` RVA 0xBEECC20 `；selector ` 44 `；EOL ` RVA 0x3392F790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f)

### path-020844

```text
(exec)# clear ethernet oam statistics interface <interface> <cr>
```

Handler ` RVA 0xBEECC20 `；selector ` 45 `；EOL ` RVA 0x3392F850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3475a508eddc7d03](../../evidence/conditions-sets-020.md#c-3475a508eddc7d03) · [缺口 G-4b6f91a8b7b837de](../../evidence/gaps-sets-003.md#g-4b6f91a8b7b837de) · [参数 P-973a347b471c3aa4](../../evidence/parameters-sets-012.md#p-973a347b471c3aa4)

### path-011613

```text
(exec)# clear ethernet service instance id <number:1..16384> mac-tunnel <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 1 `；EOL ` RVA 0x33979C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-36b096c0608ed5e8](../../evidence/conditions-sets-021.md#c-36b096c0608ed5e8) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-d094fad8d002c9da](../../evidence/state_effects-sets-044.md#s-d094fad8d002c9da)

### path-011953

```text
(exec)# clear ethernet service instance id <number:1..16384> mac-tunnel errdisable <cr>
```

Handler ` RVA 0xC0357A0 `；selector ` 3 `；EOL ` RVA 0x33985898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-dcdc180763ff5543](../../evidence/conditions-sets-085.md#c-dcdc180763ff5543) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-d094fad8d002c9da](../../evidence/state_effects-sets-044.md#s-d094fad8d002c9da)

### path-020947

```text
(exec)# clear ethernet service instance interface <interface> <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 1 `；EOL ` RVA 0x33979C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d15f1e23a381ff7](../../evidence/conditions-sets-024.md#c-3d15f1e23a381ff7) · [缺口 G-889d5e09ea647677](../../evidence/gaps-sets-005.md#g-889d5e09ea647677) · [参数 P-93b1a4af74db590d](../../evidence/parameters-sets-011.md#p-93b1a4af74db590d)

### path-023410

```text
(exec)# clear ethernet service instance interface <interface> errdisable <cr>
```

Handler ` RVA 0xC0357A0 `；selector ` 3 `；EOL ` RVA 0x33985898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-768769fa9404b8a5](../../evidence/conditions-sets-046.md#c-768769fa9404b8a5) · [缺口 G-889d5e09ea647677](../../evidence/gaps-sets-005.md#g-889d5e09ea647677) · [参数 P-93b1a4af74db590d](../../evidence/parameters-sets-011.md#p-93b1a4af74db590d)

### path-008182

```text
(exec)# clear ethernet service internal back-trace <cr>
```

Handler ` RVA 0xC013D80 `；selector ` 0 `；EOL ` RVA 0x3397BF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22df223187e2073f](../../evidence/conditions-sets-014.md#c-22df223187e2073f)

### path-008194

```text
(exec)# clear ethernet service ipc statistics <cr>
```

Handler ` RVA 0xBF920F0 `；selector ` 0 `；EOL ` RVA 0x33962C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ac23d5722e8034f](../../evidence/conditions-sets-036.md#c-5ac23d5722e8034f)

### path-016907

```text
(exec)# clear ethernet service mac-tunnel <number:dynamic> <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 2 `；EOL ` RVA 0x339796A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Mac-in-Mac tunnel identifier。

[条件 C-5a9a1a17b3431390](../../evidence/conditions-sets-035.md#c-5a9a1a17b3431390) · [缺口 G-aab5934e79e0b703](../../evidence/gaps-sets-006.md#g-aab5934e79e0b703) · [参数 P-ccf825a36f0ff1d1](../../evidence/parameters-sets-016.md#p-ccf825a36f0ff1d1) · [状态效果 S-79dbad8632cebeb4](../../evidence/state_effects-sets-026.md#s-79dbad8632cebeb4)

### path-009389

```text
(exec)# clear event manager detector counters <cr>
```

Handler ` RVA 0xC0CB550 `；selector ` 0 `；EOL ` RVA 0x339BCBB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011235

```text
(exec)# clear event manager detector rpc counters <cr>
```

Handler ` RVA 0xC0A29A0 `；selector ` 0 `；EOL ` RVA 0x3399C3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011246

```text
(exec)# clear event manager detector rpc sessions <cr>
```

Handler ` RVA 0xC0A2BA0 `；selector ` 0 `；EOL ` RVA 0x3399C698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-009377

```text
(exec)# clear event manager server counters <cr>
```

Handler ` RVA 0xC0CB5C0 `；selector ` 0 `；EOL ` RVA 0x339BC8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000101

```text
(exec)# clear facility-alarm <cr>
```

Handler ` RVA 0xC299EF0 `；selector ` 0 `；EOL ` RVA 0x33A28388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-000545

```text
(exec)# clear facility-alarm critical <cr>
```

Handler ` RVA 0xC299990 `；selector ` 0 `；EOL ` RVA 0x33A27F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-cf45e193332358a3](../../evidence/state_effects-sets-044.md#s-cf45e193332358a3)

### path-020809

```text
(exec)# clear facility-alarm hw-module slot <number:dynamic> oir <cr>
```

Handler ` RVA 0xC299D10 `；selector ` 0 `；EOL ` RVA 0x33A28508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` slot number。

[条件 C-f797ef730f2e1f4a](../../evidence/conditions-sets-096.md#c-f797ef730f2e1f4a) · [缺口 G-917e8cdd9748594d](../../evidence/gaps-sets-005.md#g-917e8cdd9748594d) · [参数 P-127131a92a3cda1a](../../evidence/parameters-sets-002.md#p-127131a92a3cda1a) · [状态效果 S-3ff1309ed387182d](../../evidence/state_effects-sets-014.md#s-3ff1309ed387182d)

### path-004605

```text
(exec)# clear flow exporter statistics <cr>
```

Handler ` RVA 0xC154D30 `；selector ` 0 `；EOL ` RVA 0x339E3370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-025297

```text
(exec)# clear flow monitor <?option@555588f41c90> <cr>
```

Handler ` RVA 0xC18F9D0 `；selector ` 0 `；EOL ` RVA 0x339EDE90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-62349631f0455efa](../../evidence/conditions-sets-038.md#c-62349631f0455efa) · [缺口 G-780ba3d830198b03](../../evidence/gaps-sets-005.md#g-780ba3d830198b03) · [状态效果 S-dc8c823d13e51773](../../evidence/state_effects-sets-047.md#s-dc8c823d13e51773)

### path-002324

```text
(exec)# clear flowspec afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 5 `；EOL ` RVA 0x35A98610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8386eee65c8fc25](../../evidence/conditions-sets-065.md#c-a8386eee65c8fc25) · [状态效果 S-c6c8b1cda0590c94](../../evidence/state_effects-sets-042.md#s-c6c8b1cda0590c94)

### path-018730

```text
(exec)# clear flowspec afi-all nlri <hex-data> <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 6 `；EOL ` RVA 0x35A98358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexdata ` Enter NLRI in hex。

[条件 C-5e7aa2e10f1771c4](../../evidence/conditions-sets-037.md#c-5e7aa2e10f1771c4) · [缺口 G-f7bf8992244e3522](../../evidence/gaps-sets-009.md#g-f7bf8992244e3522) · [参数 P-29e848b788832a0a](../../evidence/parameters-sets-004.md#p-29e848b788832a0a) · [状态效果 S-c6c8b1cda0590c94](../../evidence/state_effects-sets-042.md#s-c6c8b1cda0590c94)

### path-006187

```text
(exec)# clear flowspec counters afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 2 `；EOL ` RVA 0x35A97D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-451f8b0686c526a2](../../evidence/state_effects-sets-015.md#s-451f8b0686c526a2)

### path-006125

```text
(exec)# clear flowspec counters internal <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 4 `；EOL ` RVA 0x35A97918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-170841b0ad533f1a](../../evidence/state_effects-sets-005.md#s-170841b0ad533f1a)

### path-005438

```text
(exec)# clear fqdn packet statistics <cr>
```

Handler ` RVA 0xC2E0BF0 `；selector ` 0 `；EOL ` RVA 0x33A3CB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-cffa779f9f47ebe9](../../evidence/state_effects-sets-044.md#s-cffa779f9f47ebe9)

### path-001447

```text
(exec)# clear frame-relay counter <cr>
```

Handler ` RVA 0xF606570 `；selector ` 18 `；EOL ` RVA 0x34700850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001462

```text
(exec)# clear frame-relay inarp <cr>
```

Handler ` RVA 0xF62D080 `；selector ` 17 `；EOL ` RVA 0x3470EE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-001536

```text
(exec)# clear host <string> <cr>
```

Handler ` RVA 0xD128DD0 `；selector ` 0 `；EOL ` RVA 0x33D95930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname to delete (* for all entries)。

[条件 C-837278a6e26e6a6c](../../evidence/conditions-sets-051.md#c-837278a6e26e6a6c) · [参数 P-5fa77e3c3044d1c6](../../evidence/parameters-sets-008.md#p-5fa77e3c3044d1c6) · [状态效果 S-d45e3cc138980878](../../evidence/state_effects-sets-045.md#s-d45e3cc138980878)

### path-001385

```text
(exec)# clear icm statistics <cr>
```

Handler ` RVA 0xC2FAF60 `；selector ` 0 `；EOL ` RVA 0x33A40790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-7318fd1cb76dd9ef](../../evidence/state_effects-sets-024.md#s-7318fd1cb76dd9ef)

### path-012300

```text
(exec)# clear interface <interface> <cr>
```

Handler ` RVA 0xE002C40 `；selector ` 0 `；EOL ` RVA 0x341661E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bf2a4505c239ab1c](../../evidence/conditions-sets-074.md#c-bf2a4505c239ab1c) · [缺口 G-2840999d7791e4d2](../../evidence/gaps-sets-002.md#g-2840999d7791e4d2) · [参数 P-2f2c0b6b3666db1a](../../evidence/parameters-sets-004.md#p-2f2c0b6b3666db1a)

### path-025302

```text
(exec)# clear interface range <interface> <interface> <cr>
```

Handler ` RVA 0xE002F70 `；selector ` 0 `；EOL ` RVA 0x341664F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dc4108d2e8b2f868](../../evidence/conditions-sets-085.md#c-dc4108d2e8b2f868) · [缺口 G-41b79ce593cc13f4](../../evidence/gaps-sets-003.md#g-41b79ce593cc13f4) · [参数 P-dce3ddcd12794452](../../evidence/parameters-sets-017.md#p-dce3ddcd12794452)

### path-000312

```text
(exec)# clear iox <cr>
```

Handler ` RVA 0xEADA610 `；selector ` 0 `；EOL ` RVA 0x343A3698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-004830

```text
(exec)# clear ip access-list counters <cr>
```

Handler ` RVA 0xCEEDDF0 `；selector ` 0 `；EOL ` RVA 0x33D2D580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ea772d18ea88d05](../../evidence/conditions-sets-055.md#c-8ea772d18ea88d05)

### path-001435

```text
(exec)# clear ip accounting <cr>
```

Handler ` RVA 0xD17A5F0 `；selector ` 0 `；EOL ` RVA 0x33DA6DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-b1d55b4791ba1905](../../evidence/state_effects-sets-038.md#s-b1d55b4791ba1905)

### path-004688

```text
(exec)# clear ip arp <address> <cr>
```

Handler ` RVA 0xCF5FF90 `；selector ` 0 `；EOL ` RVA 0x33D1E250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of dynamic ARP entry。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-b690c2ce67487b89](../../evidence/parameters-sets-014.md#p-b690c2ce67487b89)

### path-008420

```text
(exec)# clear ip arp poll statistics <cr>
```

Handler ` RVA 0xCFE25A0 `；selector ` 0 `；EOL ` RVA 0x33D1E538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-013623

```text
(exec)# clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> <cr>
```

Handler ` RVA 0xF1C77B0 `；selector ` 0 `；EOL ` RVA 0x344AFD80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-585e3bf3848c0d22](../../evidence/conditions-sets-035.md#c-585e3bf3848c0d22) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-76570cce92dc5c6b](../../evidence/state_effects-sets-025.md#s-76570cce92dc5c6b)

### path-017502

```text
(exec)# clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> cease <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 7 `；EOL ` RVA 0x344B0470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03e83c542b699e01](../../evidence/conditions-sets-002.md#c-03e83c542b699e01) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-76570cce92dc5c6b](../../evidence/state_effects-sets-025.md#s-76570cce92dc5c6b)

### path-017487

```text
(exec)# clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 6 `；EOL ` RVA 0x344B01C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03e83c542b699e01](../../evidence/conditions-sets-002.md#c-03e83c542b699e01) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-76570cce92dc5c6b](../../evidence/state_effects-sets-025.md#s-76570cce92dc5c6b)

### path-017488

```text
(exec)# clear ip bgp <?match_ipv6_addrinfo_action@555589a037f0> internal <cr>
```

Handler ` RVA 0xF1CD7B0 `；selector ` 0 `；EOL ` RVA 0x344B0730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74e7cb9ab777a10f](../../evidence/conditions-sets-045.md#c-74e7cb9ab777a10f) · [缺口 G-14199b39249e3a2d](../../evidence/gaps-sets-001.md#g-14199b39249e3a2d) · [状态效果 S-76570cce92dc5c6b](../../evidence/state_effects-sets-025.md#s-76570cce92dc5c6b)

### path-001284

```text
(exec)# clear ip cache <cr>
```

Handler ` RVA 0xD49E510 `；selector ` 0 `；EOL ` RVA 0x33E54E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005160

```text
(exec)# clear ip casa counters <cr>
```

Handler ` RVA 0x1132C870 `；selector ` 0 `；EOL ` RVA 0x35499608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-017793

```text
(exec)# clear ip cef * prefix-statistics <cr>
```

Handler ` RVA 0xB61F7B0 `；selector ` 0 `；EOL ` RVA 0x337C4660 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98e029689acf8af5](../../evidence/conditions-sets-059.md#c-98e029689acf8af5) · [缺口 G-3491539c14800b04](../../evidence/gaps-sets-002.md#g-3491539c14800b04) · [状态效果 S-75da7ef9f77e48c6](../../evidence/state_effects-sets-025.md#s-75da7ef9f77e48c6)

### path-005254

```text
(exec)# clear ip cef event-log <cr>
```

Handler ` RVA 0xB5ECF20 `；selector ` 0 `；EOL ` RVA 0x337B4F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005242

```text
(exec)# clear ip cef inconsistency <cr>
```

Handler ` RVA 0xB5ECEE0 `；selector ` 0 `；EOL ` RVA 0x337B4CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005359

```text
(exec)# clear ip cef prefix-statistics <cr>
```

Handler ` RVA 0xB61F7B0 `；selector ` 0 `；EOL ` RVA 0x337C4660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ff3776d311dc981](../../evidence/conditions-sets-037.md#c-5ff3776d311dc981) · [状态效果 S-75da7ef9f77e48c6](../../evidence/state_effects-sets-025.md#s-75da7ef9f77e48c6)

### path-001285

```text
(exec)# clear ip cgmp <cr>
```

Handler ` RVA 0xF6779A0 `；selector ` 0 `；EOL ` RVA 0x34746408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-748df4bd6ac276c9](../../evidence/conditions-sets-045.md#c-748df4bd6ac276c9)

### path-013552

```text
(exec)# clear ip cgmp <interface> <cr>
```

Handler ` RVA 0xF6779A0 `；selector ` 0 `；EOL ` RVA 0x34746408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-12a828ad1b8d844d](../../evidence/conditions-sets-007.md#c-12a828ad1b8d844d) · [缺口 G-3fdf2da03149b692](../../evidence/gaps-sets-003.md#g-3fdf2da03149b692) · [参数 P-606ce1ff40b811af](../../evidence/parameters-sets-008.md#p-606ce1ff40b811af)

### path-017812

```text
(exec)# clear ip dhcp binding * <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 0 `；EOL ` RVA 0x33DE4238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c59c36a53c0de92](../../evidence/conditions-sets-005.md#c-0c59c36a53c0de92) · [缺口 G-34a6802e331f1db9](../../evidence/gaps-sets-002.md#g-34a6802e331f1db9)

### path-009009

```text
(exec)# clear ip dhcp binding <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 1 `；EOL ` RVA 0x33DE44E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Clear a specific binding。

[条件 C-7b5212d159042dff](../../evidence/conditions-sets-048.md#c-7b5212d159042dff) · [参数 P-701f423f9be8657b](../../evidence/parameters-sets-009.md#p-701f423f9be8657b)

### path-017838

```text
(exec)# clear ip dhcp conflict * <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 2 `；EOL ` RVA 0x33DE4900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-483da186762afad2](../../evidence/conditions-sets-028.md#c-483da186762afad2) · [缺口 G-de6621ce3918ea84](../../evidence/gaps-sets-008.md#g-de6621ce3918ea84)

### path-009021

```text
(exec)# clear ip dhcp conflict <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 3 `；EOL ` RVA 0x33DE4BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Clear a specific conflict。

[条件 C-255135ac04163554](../../evidence/conditions-sets-015.md#c-255135ac04163554) · [参数 P-98938e3b3a412be2](../../evidence/parameters-sets-012.md#p-98938e3b3a412be2)

### path-009035

```text
(exec)# clear ip dhcp limit lease <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 8 `；EOL ` RVA 0x33DE5590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f68ac6cdccb4710c](../../evidence/conditions-sets-095.md#c-f68ac6cdccb4710c)

### path-021786

```text
(exec)# clear ip dhcp limit lease <interface> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 7 `；EOL ` RVA 0x33DE5568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a82776ba016de036](../../evidence/conditions-sets-065.md#c-a82776ba016de036) · [缺口 G-02b924108f71f223](../../evidence/gaps-sets-001.md#g-02b924108f71f223) · [参数 P-bc74f852c8c1296f](../../evidence/parameters-sets-014.md#p-bc74f852c8c1296f)

### path-008965

```text
(exec)# clear ip dhcp server odap-statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 10 `；EOL ` RVA 0x33DE3E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d07aa454d913976f](../../evidence/conditions-sets-080.md#c-d07aa454d913976f)

### path-008981

```text
(exec)# clear ip dhcp server statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 4 `；EOL ` RVA 0x33DE3918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-260b138e4318e6fc](../../evidence/conditions-sets-015.md#c-260b138e4318e6fc)

### path-021719

```text
(exec)# clear ip dhcp server statistics <interface> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 9 `；EOL ` RVA 0x33DE38F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1debda0c549ff025](../../evidence/conditions-sets-012.md#c-1debda0c549ff025) · [缺口 G-97d7874488d4e0e1](../../evidence/gaps-sets-006.md#g-97d7874488d4e0e1) · [参数 P-9be37e5051587589](../../evidence/parameters-sets-012.md#p-9be37e5051587589)

### path-021708

```text
(exec)# clear ip dhcp snooping binding * <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 0 `；EOL ` RVA 0x35E818A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f78eb319b53a3ffb](../../evidence/conditions-sets-096.md#c-f78eb319b53a3ffb) · [缺口 G-51a56d3715830f1e](../../evidence/gaps-sets-003.md#g-51a56d3715830f1e)

### path-011017

```text
(exec)# clear ip dhcp snooping binding <address> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 1 `；EOL ` RVA 0x35E81B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Clear address specific bindings。

[条件 C-d07aa454d913976f](../../evidence/conditions-sets-080.md#c-d07aa454d913976f) · [参数 P-24a6453abfb0d28a](../../evidence/parameters-sets-003.md#p-24a6453abfb0d28a)

### path-021741

```text
(exec)# clear ip dhcp snooping binding <interface> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 2 `；EOL ` RVA 0x35E81E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7a2d2d4272fefcd](../../evidence/conditions-sets-089.md#c-e7a2d2d4272fefcd) · [缺口 G-4669f266a5c3f438](../../evidence/gaps-sets-003.md#g-4669f266a5c3f438) · [参数 P-06a696bd55f1f878](../../evidence/parameters-sets-001.md#p-06a696bd55f1f878)

### path-011779

```text
(exec)# clear ip dhcp snooping binding bridge-domain <string> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 3 `；EOL ` RVA 0x35E821D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DHCP Snooping bd range, example : 1,3-5,7,9-11。

[条件 C-a9d18010a3d034d1](../../evidence/conditions-sets-066.md#c-a9d18010a3d034d1) · [参数 P-cce908d8140214c8](../../evidence/parameters-sets-016.md#p-cce908d8140214c8)

### path-011014

```text
(exec)# clear ip dhcp snooping database statistics <cr>
```

Handler ` RVA 0x15FAA320 `；selector ` 0 `；EOL ` RVA 0x35E825B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d07aa454d913976f](../../evidence/conditions-sets-080.md#c-d07aa454d913976f)

### path-008977

```text
(exec)# clear ip dhcp snooping statistics <cr>
```

Handler ` RVA 0x15FA9590 `；selector ` 0 `；EOL ` RVA 0x35E82840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d07aa454d913976f](../../evidence/conditions-sets-080.md#c-d07aa454d913976f)

### path-017836

```text
(exec)# clear ip dhcp subnet * <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 6 `；EOL ` RVA 0x33DE4F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a3873ced7de2c97c](../../evidence/conditions-sets-063.md#c-a3873ced7de2c97c) · [缺口 G-a04ce115b4b6ed1d](../../evidence/gaps-sets-006.md#g-a04ce115b4b6ed1d)

### path-009019

```text
(exec)# clear ip dhcp subnet <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 5 `；EOL ` RVA 0x33DE51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Specify an address in the subnet to clear。

[条件 C-97f3ef56d6894b12](../../evidence/conditions-sets-059.md#c-97f3ef56d6894b12) · [参数 P-604821058269eb93](../../evidence/parameters-sets-008.md#p-604821058269eb93)

### path-017521

```text
(exec)# clear ip dns servers * <cr>
```

Handler ` RVA 0xD133B70 `；selector ` 0 `；EOL ` RVA 0x33D9B6E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f05760b341d1a543](../../evidence/conditions-sets-093.md#c-f05760b341d1a543) · [缺口 G-71508ff11bc3fd83](../../evidence/gaps-sets-004.md#g-71508ff11bc3fd83) · [状态效果 S-33d07e2eec0a0b7a](../../evidence/state_effects-sets-011.md#s-33d07e2eec0a0b7a)

### path-008687

```text
(exec)# clear ip dns servers <address> <cr>
```

Handler ` RVA 0xD133B70 `；selector ` 0 `；EOL ` RVA 0x33D9B6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPV4 Server Address。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-f3837ab8cf79a70e](../../evidence/parameters-sets-018.md#p-f3837ab8cf79a70e)

### path-001112

```text
(exec)# clear ip drp <cr>
```

Handler ` RVA 0xF4F0BA0 `；selector ` 0 `；EOL ` RVA 0x3467ADA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005183

```text
(exec)# clear ip eigrp events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346D9C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a633e88c1268bef](../../evidence/conditions-sets-041.md#c-6a633e88c1268bef) · [状态效果 S-32925ca5b2cb4299](../../evidence/state_effects-sets-011.md#s-32925ca5b2cb4299)

### path-005166

```text
(exec)# clear ip eigrp logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346D99B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a633e88c1268bef](../../evidence/conditions-sets-041.md#c-6a633e88c1268bef) · [状态效果 S-32925ca5b2cb4299](../../evidence/state_effects-sets-011.md#s-32925ca5b2cb4299)

### path-005206

```text
(exec)# clear ip eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346D92A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b50331938a240a1](../../evidence/conditions-sets-054.md#c-8b50331938a240a1) · [状态效果 S-32925ca5b2cb4299](../../evidence/state_effects-sets-011.md#s-32925ca5b2cb4299)

### path-017647

```text
(exec)# clear ip eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346D92A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ffa0a14f43cb60c6](../../evidence/conditions-sets-099.md#c-ffa0a14f43cb60c6) · [缺口 G-d088bfb99087ae2b](../../evidence/gaps-sets-007.md#g-d088bfb99087ae2b) · [参数 P-db885fec6df06f89](../../evidence/parameters-sets-017.md#p-db885fec6df06f89) · [状态效果 S-32925ca5b2cb4299](../../evidence/state_effects-sets-011.md#s-32925ca5b2cb4299)

### path-008820

```text
(exec)# clear ip eigrp topology <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346D96E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network to clear from topology。

[条件 C-6a633e88c1268bef](../../evidence/conditions-sets-041.md#c-6a633e88c1268bef) · [参数 P-c5c28ea144019d4d](../../evidence/parameters-sets-015.md#p-c5c28ea144019d4d) · [状态效果 S-32925ca5b2cb4299](../../evidence/state_effects-sets-011.md#s-32925ca5b2cb4299)

### path-017646

```text
(exec)# clear ip eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346D96E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-6e1f5d3dc8e729db](../../evidence/conditions-sets-043.md#c-6e1f5d3dc8e729db) · [缺口 G-fbb8fea18633edf3](../../evidence/gaps-sets-009.md#g-fbb8fea18633edf3) · [参数 P-f39852c340c83db0](../../evidence/parameters-sets-018.md#p-f39852c340c83db0) · [状态效果 S-1dbfa1e7aa5eadc0](../../evidence/state_effects-sets-007.md#s-1dbfa1e7aa5eadc0)

### path-010757

```text
(exec)# clear ip http client cache all <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 1 `；EOL ` RVA 0x33DB0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011685

```text
(exec)# clear ip http client cache session <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 2 `；EOL ` RVA 0x33DB0AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` session name。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-ba614fcf6b2daaef](../../evidence/parameters-sets-014.md#p-ba614fcf6b2daaef)

### path-011682

```text
(exec)# clear ip http client cache url <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 3 `；EOL ` RVA 0x33DB07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` url to clear。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-04caf09ff1ffb9ea](../../evidence/parameters-sets-001.md#p-04caf09ff1ffb9ea)

### path-008714

```text
(exec)# clear ip http client cookie <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 4 `；EOL ` RVA 0x33DB1618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011690

```text
(exec)# clear ip http client cookie domain <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 6 `；EOL ` RVA 0x33DB1370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client domain/host name。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-7ddae15590050dbb](../../evidence/parameters-sets-010.md#p-7ddae15590050dbb)

### path-011696

```text
(exec)# clear ip http client cookie name <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 7 `；EOL ` RVA 0x33DB1658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client cookie name。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-70e3f6d6b140bc15](../../evidence/parameters-sets-009.md#p-70e3f6d6b140bc15)

### path-011684

```text
(exec)# clear ip http client cookie session <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 5 `；EOL ` RVA 0x33DB1088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client session name。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-7dc08f985880508a](../../evidence/parameters-sets-010.md#p-7dc08f985880508a)

### path-004721

```text
(exec)# clear ip icmp rate-limit <cr>
```

Handler ` RVA 0xCFE5700 `；selector ` 0 `；EOL ` RVA 0x33D2B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83bafa6d7bb275ab](../../evidence/conditions-sets-051.md#c-83bafa6d7bb275ab)

### path-017106

```text
(exec)# clear ip icmp rate-limit <interface> <cr>
```

Handler ` RVA 0xCFE5700 `；selector ` 0 `；EOL ` RVA 0x33D2B198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f90de7ce786c8e6e](../../evidence/conditions-sets-096.md#c-f90de7ce786c8e6e) · [缺口 G-2bbf7fbb07f399cb](../../evidence/gaps-sets-002.md#g-2bbf7fbb07f399cb) · [参数 P-b03239b6c3606417](../../evidence/parameters-sets-013.md#p-b03239b6c3606417)

### path-005127

```text
(exec)# clear ip igmp group <cr>
```

Handler ` RVA 0xF6B26D0 `；selector ` 0 `；EOL ` RVA 0x34746DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84bc31fd40ffcf92](../../evidence/conditions-sets-051.md#c-84bc31fd40ffcf92) · [状态效果 S-be24368a56acba23](../../evidence/state_effects-sets-040.md#s-be24368a56acba23)

### path-017558

```text
(exec)# clear ip igmp group <interface> <cr>
```

Handler ` RVA 0xF6B26D0 `；selector ` 0 `；EOL ` RVA 0x34746DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7e2ee4719c6ced9b](../../evidence/conditions-sets-049.md#c-7e2ee4719c6ced9b) · [缺口 G-b30ec43a1c3b2e3e](../../evidence/gaps-sets-006.md#g-b30ec43a1c3b2e3e) · [参数 P-cece2de85eb2be27](../../evidence/parameters-sets-016.md#p-cece2de85eb2be27) · [状态效果 S-be24368a56acba23](../../evidence/state_effects-sets-040.md#s-be24368a56acba23)

### path-013355

```text
(exec)# clear ip interface <interface> <cr>
```

Handler ` RVA 0xCF0E720 `；selector ` 0 `；EOL ` RVA 0x33D2C780 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd236d5a9aeb7311](../../evidence/conditions-sets-073.md#c-bd236d5a9aeb7311) · [缺口 G-da3907552e4d8118](../../evidence/gaps-sets-008.md#g-da3907552e4d8118) · [参数 P-19b41cc50ccf0878](../../evidence/parameters-sets-002.md#p-19b41cc50ccf0878)

### path-017183

```text
(exec)# clear ip interface <interface> stats <cr>
```

Handler ` RVA 0xCF38F80 `；selector ` 0 `；EOL ` RVA 0x33D2C758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd236d5a9aeb7311](../../evidence/conditions-sets-073.md#c-bd236d5a9aeb7311) · [缺口 G-da3907552e4d8118](../../evidence/gaps-sets-008.md#g-da3907552e4d8118) · [参数 P-19b41cc50ccf0878](../../evidence/parameters-sets-002.md#p-19b41cc50ccf0878)

### path-023468

```text
(exec)# clear ip interface <interface> topology base stats <cr>
```

Handler ` RVA 0xCF38F10 `；selector ` 0 `；EOL ` RVA 0x33D2C3B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd236d5a9aeb7311](../../evidence/conditions-sets-073.md#c-bd236d5a9aeb7311) · [缺口 G-da3907552e4d8118](../../evidence/gaps-sets-008.md#g-da3907552e4d8118) · [参数 P-19b41cc50ccf0878](../../evidence/parameters-sets-002.md#p-19b41cc50ccf0878) · [状态效果 S-25fcbcc1f12c35ec](../../evidence/state_effects-sets-009.md#s-25fcbcc1f12c35ec)

### path-005233

```text
(exec)# clear ip mfib counters <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355B7700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8c1fa28769202dda](../../evidence/conditions-sets-054.md#c-8c1fa28769202dda) · [状态效果 S-1331375b9ac80dcc](../../evidence/state_effects-sets-004.md#s-1331375b9ac80dcc)

### path-017670

```text
(exec)# clear ip mfib counters <prefix:dynamic> <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355B7700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-6ce6af4a8eeb7b01](../../evidence/conditions-sets-042.md#c-6ce6af4a8eeb7b01) · [缺口 G-e0825a477ae95de3](../../evidence/gaps-sets-008.md#g-e0825a477ae95de3) · [参数 P-11932c0b949637f4](../../evidence/parameters-sets-002.md#p-11932c0b949637f4) · [状态效果 S-1331375b9ac80dcc](../../evidence/state_effects-sets-004.md#s-1331375b9ac80dcc)

### path-005096

```text
(exec)# clear ip mrm status-report <cr>
```

Handler ` RVA 0xF672250 `；selector ` 0 `；EOL ` RVA 0x3471F308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-013601

```text
(exec)# clear ip mroute * <cr>
```

Handler ` RVA 0xF74EC90 `；selector ` 0 `；EOL ` RVA 0x347468B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc401a5c2ce1fa13](../../evidence/conditions-sets-079.md#c-cc401a5c2ce1fa13) · [缺口 G-495214df7e16558b](../../evidence/gaps-sets-003.md#g-495214df7e16558b) · [状态效果 S-cf402c5053557ac9](../../evidence/state_effects-sets-044.md#s-cf402c5053557ac9)

### path-005098

```text
(exec)# clear ip mroute <address> <cr>
```

Handler ` RVA 0xF74EC90 `；selector ` 0 `；EOL ` RVA 0x347468B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP name or group address。

[条件 C-4e3a6e4a37b52b8e](../../evidence/conditions-sets-031.md#c-4e3a6e4a37b52b8e) · [参数 P-5526640d1cbfc478](../../evidence/parameters-sets-007.md#p-5526640d1cbfc478) · [状态效果 S-5bb55273fb86393f](../../evidence/state_effects-sets-020.md#s-5bb55273fb86393f)

### path-008617

```text
(exec)# clear ip msdp peer <address> <cr>
```

Handler ` RVA 0xF78ED70 `；selector ` 0 `；EOL ` RVA 0x34741B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [参数 P-9f44f2d1408a3f5d](../../evidence/parameters-sets-012.md#p-9f44f2d1408a3f5d)

### path-005003

```text
(exec)# clear ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78EA70 `；selector ` 0 `；EOL ` RVA 0x34741E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005021

```text
(exec)# clear ip msdp statistics <cr>
```

Handler ` RVA 0xF78EB10 `；selector ` 0 `；EOL ` RVA 0x34742130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005054

```text
(exec)# clear ip multicast limit <cr>
```

Handler ` RVA 0xF777FE0 `；selector ` 0 `；EOL ` RVA 0x34746048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44a3d5c7617ee39a](../../evidence/conditions-sets-027.md#c-44a3d5c7617ee39a)

### path-017457

```text
(exec)# clear ip multicast limit <interface> <cr>
```

Handler ` RVA 0xF777FE0 `；selector ` 0 `；EOL ` RVA 0x34746048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fa82d8840be52501](../../evidence/conditions-sets-097.md#c-fa82d8840be52501) · [缺口 G-6c2dd868b4a31c65](../../evidence/gaps-sets-004.md#g-6c2dd868b4a31c65) · [参数 P-b0899c18c843ca25](../../evidence/parameters-sets-013.md#p-b0899c18c843ca25)

### path-008730

```text
(exec)# clear ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD4712F0 `；selector ` 0 `；EOL ` RVA 0x33E525D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c01dc944e3def4f](../../evidence/conditions-sets-005.md#c-0c01dc944e3def4f)

### path-005037

```text
(exec)# clear ip multicast rsvp <cr>
```

Handler ` RVA 0xF6F1770 `；selector ` 0 `；EOL ` RVA 0x34745CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52c71dba6b9b8c0b](../../evidence/conditions-sets-032.md#c-52c71dba6b9b8c0b)

### path-017438

```text
(exec)# clear ip multicast rsvp <interface> <cr>
```

Handler ` RVA 0xF6F1770 `；selector ` 0 `；EOL ` RVA 0x34745CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-574d9a44526f360b](../../evidence/conditions-sets-034.md#c-574d9a44526f360b) · [缺口 G-d22044241edd3608](../../evidence/gaps-sets-007.md#g-d22044241edd3608) · [参数 P-bb819926b72a1e7d](../../evidence/parameters-sets-014.md#p-bb819926b72a1e7d)

### path-011991

```text
(exec)# clear ip multicast snooping limit vlan <number:1..4095> statistics <cr>
```

Handler ` RVA 0xC3568D0 `；selector ` 64 `；EOL ` RVA 0x33A5F240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-0c01dc944e3def4f](../../evidence/conditions-sets-005.md#c-0c01dc944e3def4f) · [参数 P-85cbffd05ab530a5](../../evidence/parameters-sets-010.md#p-85cbffd05ab530a5)

### path-005105

```text
(exec)# clear ip nat statistics <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 1 `；EOL ` RVA 0x347DD7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-017545

```text
(exec)# clear ip nat translation * <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 0 `；EOL ` RVA 0x347DCB40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a915bd16866829ed](../../evidence/conditions-sets-065.md#c-a915bd16866829ed) · [缺口 G-18ce86318758d554](../../evidence/gaps-sets-001.md#g-18ce86318758d554) · [状态效果 S-f8b80b77c56b2dd6](../../evidence/state_effects-sets-053.md#s-f8b80b77c56b2dd6)

### path-005222

```text
(exec)# clear ip nat translation <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 0 `；EOL ` RVA 0x347DCB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29c5259e20fc3e3e](../../evidence/conditions-sets-016.md#c-29c5259e20fc3e3e)

### path-001270

```text
(exec)# clear ip nbar <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 2 `；EOL ` RVA 0x3527C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfc53a51f2e8504e](../../evidence/conditions-sets-080.md#c-cfc53a51f2e8504e) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-011691

```text
(exec)# clear ip nbar classification auto-learn top-hosts restart <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 14 `；EOL ` RVA 0x3527B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-279eb39c18f526f0](../../evidence/conditions-sets-016.md#c-279eb39c18f526f0) · [状态效果 S-b6287b7099121533](../../evidence/state_effects-sets-039.md#s-b6287b7099121533)

### path-011683

```text
(exec)# clear ip nbar classification auto-learn top-hosts statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 13 `；EOL ` RVA 0x3527B5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-279eb39c18f526f0](../../evidence/conditions-sets-016.md#c-279eb39c18f526f0) · [状态效果 S-b6287b7099121533](../../evidence/state_effects-sets-039.md#s-b6287b7099121533)

### path-010752

```text
(exec)# clear ip nbar classification cache sync <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 12 `；EOL ` RVA 0x3527BBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-011693

```text
(exec)# clear ip nbar classification dns learning cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 47 `；EOL ` RVA 0x3527BF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-011700

```text
(exec)# clear ip nbar classification dns learning statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 49 `；EOL ` RVA 0x3527C1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-008708

```text
(exec)# clear ip nbar classification socket-cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 48 `；EOL ` RVA 0x3527C458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-005022

```text
(exec)# clear ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 34 `；EOL ` RVA 0x3527B048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1748a59eb20e5a92](../../evidence/conditions-sets-009.md#c-1748a59eb20e5a92) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-005031

```text
(exec)# clear ip nbar statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 7 `；EOL ` RVA 0x3527C748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5190528876f2b11](../../evidence/conditions-sets-064.md#c-a5190528876f2b11) · [状态效果 S-84a514e6952e3c95](../../evidence/state_effects-sets-028.md#s-84a514e6952e3c95)

### path-001423

```text
(exec)# clear ip nhrp <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 0 `；EOL ` RVA 0x347F2628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4672b3b843474434](../../evidence/conditions-sets-028.md#c-4672b3b843474434)

### path-013681

```text
(exec)# clear ip nhrp <interface> <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 0 `；EOL ` RVA 0x347F2628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-16cc392c7ef5e46a](../../evidence/conditions-sets-009.md#c-16cc392c7ef5e46a) · [缺口 G-33f69aa2e0415a4e](../../evidence/gaps-sets-002.md#g-33f69aa2e0415a4e) · [参数 P-57d8892cc9e461c1](../../evidence/parameters-sets-007.md#p-57d8892cc9e461c1)

### path-005218

```text
(exec)# clear ip nhrp counters <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 1 `；EOL ` RVA 0x347F29F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4672b3b843474434](../../evidence/conditions-sets-028.md#c-4672b3b843474434)

### path-005189

```text
(exec)# clear ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 0 `；EOL ` RVA 0x34BF9228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-f2e1edd85ab38b1a](../../evidence/state_effects-sets-051.md#s-f2e1edd85ab38b1a)

### path-021569

```text
(exec)# clear ip nhrp shortcut interface <interface> <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 1 `；EOL ` RVA 0x34BF92E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6ae67c6c000f5dc7](../../evidence/conditions-sets-041.md#c-6ae67c6c000f5dc7) · [缺口 G-32b151dc5831b823](../../evidence/gaps-sets-002.md#g-32b151dc5831b823) · [参数 P-b7cfd3b87c5b765b](../../evidence/parameters-sets-014.md#p-b7cfd3b87c5b765b) · [状态效果 S-f2e1edd85ab38b1a](../../evidence/state_effects-sets-051.md#s-f2e1edd85ab38b1a)

### path-005291

```text
(exec)# clear ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 2 `；EOL ` RVA 0x347F2F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3de47fbbee6785](../../evidence/conditions-sets-097.md#c-fb3de47fbbee6785)

### path-017729

```text
(exec)# clear ip nhrp stats <interface> <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 2 `；EOL ` RVA 0x347F2F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d907d5676cdcc78](../../evidence/conditions-sets-024.md#c-3d907d5676cdcc78) · [缺口 G-e4b9cff4886156ea](../../evidence/gaps-sets-008.md#g-e4b9cff4886156ea) · [参数 P-e74517d0446cc71b](../../evidence/parameters-sets-017.md#p-e74517d0446cc71b)

### path-005171

```text
(exec)# clear ip ospf counters <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 4 `；EOL ` RVA 0x348934D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005184

```text
(exec)# clear ip ospf events <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 6 `；EOL ` RVA 0x34893FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005121

```text
(exec)# clear ip ospf force-spf <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 0 `；EOL ` RVA 0x34892C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-011729

```text
(exec)# clear ip ospf lsa router <address> self <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 7 `；EOL ` RVA 0x34893A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF LSID in IP address format。

[条件 C-2713a37cfc99e412](../../evidence/conditions-sets-015.md#c-2713a37cfc99e412) · [参数 P-4bb4f15a3e4f951b](../../evidence/parameters-sets-006.md#p-4bb4f15a3e4f951b) · [状态效果 S-b6124f6531b57a13](../../evidence/state_effects-sets-039.md#s-b6124f6531b57a13)

### path-008747

```text
(exec)# clear ip ospf nsr statistics <cr>
```

Handler ` RVA 0xDACCB50 `；selector ` 20 `；EOL ` RVA 0x33FC88B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-f3676f0012c2c0c8](../../evidence/state_effects-sets-051.md#s-f3676f0012c2c0c8)

### path-005091

```text
(exec)# clear ip ospf process <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 3 `；EOL ` RVA 0x34892700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005071

```text
(exec)# clear ip ospf redistribution <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 2 `；EOL ` RVA 0x34892458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005108

```text
(exec)# clear ip ospf rib <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 1 `；EOL ` RVA 0x348929A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce)

### path-005190

```text
(exec)# clear ip ospf traffic <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 5 `；EOL ` RVA 0x34893080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b4cf5094c0c0c7b](../../evidence/conditions-sets-060.md#c-9b4cf5094c0c0c7b)

### path-017610

```text
(exec)# clear ip ospf traffic <interface> <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 5 `；EOL ` RVA 0x34893080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2229cb6345ebf70f](../../evidence/conditions-sets-013.md#c-2229cb6345ebf70f) · [缺口 G-431fff5b8a95e318](../../evidence/gaps-sets-003.md#g-431fff5b8a95e318) · [参数 P-319be4011d545c98](../../evidence/parameters-sets-004.md#p-319be4011d545c98)

### path-005038

```text
(exec)# clear ip pim df <cr>
```

Handler ` RVA 0xF7CB460 `；selector ` 0 `；EOL ` RVA 0x34771D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c01dc944e3def4f](../../evidence/conditions-sets-005.md#c-0c01dc944e3def4f)

### path-021401

```text
(exec)# clear ip pim interface <interface> count <cr>
```

Handler ` RVA 0xF827030 `；selector ` 0 `；EOL ` RVA 0x34772140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-27f7d15206f80ecb](../../evidence/conditions-sets-016.md#c-27f7d15206f80ecb) · [缺口 G-18a7425124d07066](../../evidence/gaps-sets-001.md#g-18a7425124d07066) · [参数 P-8e30251f47fbf72e](../../evidence/parameters-sets-011.md#p-8e30251f47fbf72e)

### path-008705

```text
(exec)# clear ip pim interface count <cr>
```

Handler ` RVA 0xF827030 `；selector ` 0 `；EOL ` RVA 0x34772140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff2f69d88f328578](../../evidence/conditions-sets-098.md#c-ff2f69d88f328578)

### path-008702

```text
(exec)# clear ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF8A2050 `；selector ` 0 `；EOL ` RVA 0x347726F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c01dc944e3def4f](../../evidence/conditions-sets-005.md#c-0c01dc944e3def4f)

### path-008683

```text
(exec)# clear ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF8A1FA0 `；selector ` 0 `；EOL ` RVA 0x34772450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c01dc944e3def4f](../../evidence/conditions-sets-005.md#c-0c01dc944e3def4f)

### path-005002

```text
(exec)# clear ip pim rp-mapping <cr>
```

Handler ` RVA 0xF7BE560 `；selector ` 0 `；EOL ` RVA 0x34771918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c01dc944e3def4f](../../evidence/conditions-sets-005.md#c-0c01dc944e3def4f)

### path-001421

```text
(exec)# clear ip prefix-list <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x34283CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-24702ac94b23aca3](../../evidence/state_effects-sets-008.md#s-24702ac94b23aca3)

### path-000993

```text
(exec)# clear ip redirect <cr>
```

Handler ` RVA 0xCF50BF0 `；selector ` 0 `；EOL ` RVA 0x33D2B468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e029b59c347a5ce](../../evidence/conditions-sets-006.md#c-0e029b59c347a5ce) · [状态效果 S-98de150b6ab5b43a](../../evidence/state_effects-sets-032.md#s-98de150b6ab5b43a)

### path-013724

```text
(exec)# clear ip reflexive-list * <cr>
```

Handler ` RVA 0xCEFCA00 `；selector ` 0 `；EOL ` RVA 0x3479AD88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2f2c90257b498e7](../../evidence/conditions-sets-087.md#c-e2f2c90257b498e7) · [缺口 G-1ed2d3717e2e43f4](../../evidence/gaps-sets-002.md#g-1ed2d3717e2e43f4) · [状态效果 S-1f319386bacccfe3](../../evidence/state_effects-sets-007.md#s-1f319386bacccfe3)

### path-005255

```text
(exec)# clear ip reflexive-list <string> <cr>
```

Handler ` RVA 0xCEFCA00 `；selector ` 0 `；EOL ` RVA 0x3479AD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Delete a specific reflexive ACL。

[条件 C-9eb1f86326aa8299](../../evidence/conditions-sets-061.md#c-9eb1f86326aa8299) · [参数 P-afb5c6d87d9e8de3](../../evidence/parameters-sets-013.md#p-afb5c6d87d9e8de3)

### path-013513

```text
(exec)# clear ip route * <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 1 `；EOL ` RVA 0x3422DF58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4133fe0b636c1103](../../evidence/conditions-sets-025.md#c-4133fe0b636c1103) · [缺口 G-e12c79afb36e567d](../../evidence/gaps-sets-008.md#g-e12c79afb36e567d) · [状态效果 S-7b5fc6c17bfd3a53](../../evidence/state_effects-sets-026.md#s-7b5fc6c17bfd3a53)

### path-004982

```text
(exec)# clear ip route <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 1 `；EOL ` RVA 0x3422DF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination network route to delete。

[条件 C-3f1b6b8860e1df45](../../evidence/conditions-sets-024.md#c-3f1b6b8860e1df45) · [参数 P-a606ea51f9247878](../../evidence/parameters-sets-013.md#p-a606ea51f9247878) · [状态效果 S-ae3714b54f82f3ae](../../evidence/state_effects-sets-037.md#s-ae3714b54f82f3ae)

### path-008619

```text
(exec)# clear ip route dhcp <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 2 `；EOL ` RVA 0x3422E240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination host route to delete。

[条件 C-3f1b6b8860e1df45](../../evidence/conditions-sets-024.md#c-3f1b6b8860e1df45) · [参数 P-f4e189f9e5e93c08](../../evidence/parameters-sets-018.md#p-f4e189f9e5e93c08) · [状态效果 S-7b5fc6c17bfd3a53](../../evidence/state_effects-sets-026.md#s-7b5fc6c17bfd3a53)

### path-017458

```text
(exec)# clear ip route download * <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 1 `；EOL ` RVA 0x3422E620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-81245142f77a0cc9](../../evidence/conditions-sets-050.md#c-81245142f77a0cc9) · [缺口 G-eaeda2c32a5e0a29](../../evidence/gaps-sets-008.md#g-eaeda2c32a5e0a29) · [状态效果 S-7b5fc6c17bfd3a53](../../evidence/state_effects-sets-026.md#s-7b5fc6c17bfd3a53)

### path-010771

```text
(exec)# clear ip route download <address> <address> <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 1 `；EOL ` RVA 0x3422E620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination network route to delete；` address ` Destination network mask。

[条件 C-be72fc6332dbfb81](../../evidence/conditions-sets-074.md#c-be72fc6332dbfb81) · [参数 P-405fcd062cfd9eeb](../../evidence/parameters-sets-005.md#p-405fcd062cfd9eeb) · [状态效果 S-beb9974a60f33101](../../evidence/state_effects-sets-040.md#s-beb9974a60f33101)

### path-008706

```text
(exec)# clear ip route download reload <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 2 `；EOL ` RVA 0x3422E8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be72fc6332dbfb81](../../evidence/conditions-sets-074.md#c-be72fc6332dbfb81) · [状态效果 S-7b5fc6c17bfd3a53](../../evidence/state_effects-sets-026.md#s-7b5fc6c17bfd3a53)

### path-005258

```text
(exec)# clear ip rsvp authentication <cr>
```

Handler ` RVA 0x100741B0 `；selector ` 0 `；EOL ` RVA 0x34A3D340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-005181

```text
(exec)# clear ip rsvp counters <cr>
```

Handler ` RVA 0x100B7230 `；selector ` 0 `；EOL ` RVA 0x34A3B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-010941

```text
(exec)# clear ip rsvp hello bfd lost-cnt <cr>
```

Handler ` RVA 0x10074420 `；selector ` 0 `；EOL ` RVA 0x34A3C3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-010960

```text
(exec)# clear ip rsvp hello bfd nbr-lost <cr>
```

Handler ` RVA 0x100744C0 `；selector ` 0 `；EOL ` RVA 0x34A3C678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-010945

```text
(exec)# clear ip rsvp hello instance counters <cr>
```

Handler ` RVA 0x1006F1F0 `；selector ` 0 `；EOL ` RVA 0x34A3C0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-010920

```text
(exec)# clear ip rsvp hello instance statistics <cr>
```

Handler ` RVA 0x1006F240 `；selector ` 0 `；EOL ` RVA 0x34A3BE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-008842

```text
(exec)# clear ip rsvp hello statistics <cr>
```

Handler ` RVA 0x1006F290 `；selector ` 0 `；EOL ` RVA 0x34A3BB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-008886

```text
(exec)# clear ip rsvp metadata interface <cr>
```

Handler ` RVA 0x10078C10 `；selector ` 0 `；EOL ` RVA 0x34A3D630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b27782dc9fc2a96a](../../evidence/conditions-sets-069.md#c-b27782dc9fc2a96a)

### path-008796

```text
(exec)# clear ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100B71E0 `；selector ` 0 `；EOL ` RVA 0x34A3AB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac6e6a792af1891e](../../evidence/conditions-sets-067.md#c-ac6e6a792af1891e)

### path-017628

```text
(exec)# clear ip rsvp reservation * <cr>
```

Handler ` RVA 0x1006F000 `；selector ` 0 `；EOL ` RVA 0x34A3B4F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-931e1b88e496b72a](../../evidence/conditions-sets-057.md#c-931e1b88e496b72a) · [缺口 G-6a53b8077a48b93b](../../evidence/gaps-sets-004.md#g-6a53b8077a48b93b)

### path-012111

```text
(exec)# clear ip rsvp reservation <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F000 `；selector ` 0 `；EOL ` RVA 0x34A3B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73) · [参数 P-bca9d63baab5c636](../../evidence/parameters-sets-014.md#p-bca9d63baab5c636) · [状态效果 S-9b2de1235da33a22](../../evidence/state_effects-sets-033.md#s-9b2de1235da33a22)

### path-017609

```text
(exec)# clear ip rsvp sender * <cr>
```

Handler ` RVA 0x1006ED80 `；selector ` 0 `；EOL ` RVA 0x34A3AFB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44fe56ae0225ec69](../../evidence/conditions-sets-027.md#c-44fe56ae0225ec69) · [缺口 G-ea5c953c425fce52](../../evidence/gaps-sets-008.md#g-ea5c953c425fce52)

### path-012109

```text
(exec)# clear ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x1006ED80 `；selector ` 0 `；EOL ` RVA 0x34A3AFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73) · [参数 P-6ed41e2ffa47e5cc](../../evidence/parameters-sets-009.md#p-6ed41e2ffa47e5cc) · [状态效果 S-4761e5fe1fdd3128](../../evidence/state_effects-sets-016.md#s-4761e5fe1fdd3128)

### path-010919

```text
(exec)# clear ip rsvp signalling fast-local-repair statistics <cr>
```

Handler ` RVA 0x100710E0 `；selector ` 0 `；EOL ` RVA 0x34A3CA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-008872

```text
(exec)# clear ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x10070F70 `；selector ` 0 `；EOL ` RVA 0x34A3CC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-010957

```text
(exec)# clear ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071080 `；selector ` 0 `；EOL ` RVA 0x34A3CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16d7f50998f61f73](../../evidence/conditions-sets-009.md#c-16d7f50998f61f73)

### path-004846

```text
(exec)# clear ip rtp header-compression <cr>
```

Handler ` RVA 0xD194840 `；selector ` 0 `；EOL ` RVA 0x33DAB158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d60b45cecd520cdc](../../evidence/conditions-sets-083.md#c-d60b45cecd520cdc)

