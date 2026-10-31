# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-026920

```text
(config)# default dnsix-dmdp retries <cr>
```

Handler ` RVA 0xD4A1FB0 `；selector ` 0 `；EOL ` RVA 0x33E567E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-291b80c8eea077a4](../../evidence/conditions-sets-016.md#c-291b80c8eea077a4) · [状态效果 S-e7571194ff2a0299](../../evidence/state_effects-sets-049.md#s-e7571194ff2a0299)

### path-026933

```text
(config)# default dnsix-nat source <cr>
```

Handler ` RVA 0xD4A31F0 `；selector ` 0 `；EOL ` RVA 0x33E56B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a24908b0a0fe821e](../../evidence/conditions-sets-063.md#c-a24908b0a0fe821e) · [状态效果 S-9537739ecfd9ff39](../../evidence/state_effects-sets-032.md#s-9537739ecfd9ff39)

### path-026376

```text
(config)# default do-exec <number:1..99> <cr>
```

Handler ` RVA 0xDE857D0 `；selector ` 1 `；EOL ` RVA 0x34186F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Session number to resume。

[条件 C-389cecc55b15fe86](../../evidence/conditions-sets-022.md#c-389cecc55b15fe86) · [参数 P-5a2136bf20667e61](../../evidence/parameters-sets-007.md#p-5a2136bf20667e61) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-025996

```text
(config)# default do-exec <string> <cr>
```

Handler ` RVA 0xDEF32B0 `；selector ` 0 `；EOL ` RVA 0x340BB4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Exec Command。

[条件 C-41fd7b67705d8a48](../../evidence/conditions-sets-026.md#c-41fd7b67705d8a48) · [参数 P-bf6e24cec82cb154](../../evidence/parameters-sets-015.md#p-bf6e24cec82cb154) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034361

```text
(config)# default do-exec aaa tools memleak-detection-start <cr>
```

Handler ` RVA 0x1371EB80 `；selector ` 0 `；EOL ` RVA 0x35C0E758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-026822

```text
(config)# default do-exec access-enable <cr>
```

Handler ` RVA 0xCEEEEA0 `；selector ` 0 `；EOL ` RVA 0x33D2ACF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fe511de0c1967cce](../../evidence/conditions-sets-098.md#c-fe511de0c1967cce) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-026854

```text
(config)# default do-exec access-profile <cr>
```

Handler ` RVA 0xDD24680 `；selector ` 0 `；EOL ` RVA 0x34043248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-02e517ecdb8eb284](../../evidence/state_effects-sets-001.md#s-02e517ecdb8eb284)

### path-045083

```text
(config)# default do-exec access-session remote-device-notification mac <address> <cr>
```

Handler ` RVA 0xCADCD00 `；selector ` 0 `；EOL ` RVA 0x33B9B6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MAC address。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a31f1e1a4ace1062](../../evidence/parameters-sets-012.md#p-a31f1e1a4ace1062) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052693

```text
(config)# default do-exec access-template <number:100..199> <string> any any <cr>
```

Handler ` RVA 0xCEEFAE0 `；selector ` 0 `；EOL ` RVA 0x33D2A758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IP extended access list；` string ` Name of Temp. list within the access-list。

[条件 C-fe511de0c1967cce](../../evidence/conditions-sets-098.md#c-fe511de0c1967cce) · [参数 P-2160701221db188a](../../evidence/parameters-sets-003.md#p-2160701221db188a) · [状态效果 S-26afdbeb75374c7a](../../evidence/state_effects-sets-009.md#s-26afdbeb75374c7a)

### path-028161

```text
(config)# default do-exec acm confirm-commit <cr>
```

Handler ` RVA 0xDED7A40 `；selector ` 0 `；EOL ` RVA 0x34095218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-f34a73400682af91](../../evidence/state_effects-sets-051.md#s-f34a73400682af91)

### path-030631

```text
(config)# default do-exec alps update-circuits <cr>
```

Handler ` RVA 0x11217A80 `；selector ` 0 `；EOL ` RVA 0x3541A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-030010

```text
(config)# default do-exec analyze memory-leak <cr>
```

Handler ` RVA 0xE0942F0 `；selector ` 0 `；EOL ` RVA 0x341F0840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,1,0] `。

[条件 C-6deb2dda4d2778bd](../../evidence/conditions-sets-043.md#c-6deb2dda4d2778bd) · [状态效果 S-ea0b729a810b58f0](../../evidence/state_effects-sets-050.md#s-ea0b729a810b58f0)

### path-045817

```text
(config)# default do-exec analyze summary memory-leak update <cr>
```

Handler ` RVA 0xE0943B0 `；selector ` 0 `；EOL ` RVA 0x341F0540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,1,0] `。

[条件 C-3d030a0ab787851c](../../evidence/conditions-sets-024.md#c-3d030a0ab787851c) · [状态效果 S-774114a57e7ab8ee](../../evidence/state_effects-sets-025.md#s-774114a57e7ab8ee)

### path-030533

```text
(config)# default do-exec archive config <cr>
```

Handler ` RVA 0xDEDE440 `；selector ` 0 `；EOL ` RVA 0x3409A0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057793

```text
(config)# default do-exec archive log config add comment <string> <cr>
```

Handler ` RVA 0xDF0B3A0 `；selector ` 0 `；EOL ` RVA 0x340A35A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Comment (up to 128 characters)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3088f7718888ec37](../../evidence/parameters-sets-004.md#p-3088f7718888ec37) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046698

```text
(config)# default do-exec archive tar /table <string> <cr>
```

Handler ` RVA 0xD663D40 `；selector ` 0 `；EOL ` RVA 0x33EBD5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tar filename。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2418664fd9d768d1](../../evidence/parameters-sets-003.md#p-2418664fd9d768d1) · [状态效果 S-b5925f316af730ba](../../evidence/state_effects-sets-038.md#s-b5925f316af730ba)

### path-036142

```text
(config)# default do-exec authentication display config-mode <cr>
```

Handler ` RVA 0xCB10230 `；selector ` 0 `；EOL ` RVA 0x33BB23E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036294

```text
(config)# default do-exec authentication display legacy <cr>
```

Handler ` RVA 0xCB102D0 `；selector ` 0 `；EOL ` RVA 0x33BB26C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66ac7ba3aad392f3](../../evidence/conditions-sets-040.md#c-66ac7ba3aad392f3) · [状态效果 S-6767a91a75f1b057](../../evidence/state_effects-sets-022.md#s-6767a91a75f1b057)

### path-028280

```text
(config)# default do-exec auto secure <cr>
```

Handler ` RVA 0xB246A80 `；selector ` 0 `；EOL ` RVA 0x336D4B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c8b2890c9b18dd7a](../../evidence/conditions-sets-077.md#c-c8b2890c9b18dd7a) · [状态效果 S-e9e85f397f3866f6](../../evidence/state_effects-sets-049.md#s-e9e85f397f3866f6)

### path-036403

```text
(config)# default do-exec beep kill session <cr>
```

Handler ` RVA 0xEF60A30 `；selector ` 1 `；EOL ` RVA 0x3448C338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-030224

```text
(config)# default do-exec bingd stop <cr>
```

Handler ` RVA 0xF2731C0 `；selector ` 0 `；EOL ` RVA 0x345DDD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a43a5a94eb877d2](../../evidence/conditions-sets-004.md#c-0a43a5a94eb877d2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036713

```text
(config)# default do-exec bingd template <string> <cr>
```

Handler ` RVA 0xF272D80 `；selector ` 0 `；EOL ` RVA 0x345DD688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` beep template to be used。

[条件 C-958be3c8e13e9651](../../evidence/conditions-sets-058.md#c-958be3c8e13e9651) · [参数 P-74a8a6af26414404](../../evidence/parameters-sets-009.md#p-74a8a6af26414404) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036803

```text
(config)# default do-exec bingng template <string> <cr>
```

Handler ` RVA 0xF272900 `；selector ` 0 `；EOL ` RVA 0x345DC9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` beep template to be used。

[条件 C-4738ea267c8b20c5](../../evidence/conditions-sets-028.md#c-4738ea267c8b20c5) · [参数 P-333ae3065c8daf82](../../evidence/parameters-sets-004.md#p-333ae3065c8daf82) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046930

```text
(config)# default do-exec bulkstat profile <string> disable <cr>
```

Handler ` RVA 0xBC6B6A0 `；selector ` 0 `；EOL ` RVA 0x338819A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of profile。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-feb2bca4df1d2854](../../evidence/parameters-sets-019.md#p-feb2bca4df1d2854) · [状态效果 S-2dfdb701f32c3095](../../evidence/state_effects-sets-010.md#s-2dfdb701f32c3095)

### path-046931

```text
(config)# default do-exec bulkstat profile <string> enable repeat <number:1..4294967294> <cr>
```

Handler ` RVA 0xBC6B6A0 `；selector ` 3 `；EOL ` RVA 0x33881C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of profile；` unsigned_number ` Number of recurrences。

[条件 C-2c55ea67ecdfc4f2](../../evidence/conditions-sets-017.md#c-2c55ea67ecdfc4f2) · [参数 P-b7570e5ddb9c6525](../../evidence/parameters-sets-014.md#p-b7570e5ddb9c6525) · [状态效果 S-e18b8e0b4bf6e696](../../evidence/state_effects-sets-048.md#s-e18b8e0b4bf6e696)

### path-052617

```text
(config)# default do-exec call-home debug syslog-throttling timer <number:1..86400> <cr>
```

Handler ` RVA 0xB6D4AC0 `；selector ` 0 `；EOL ` RVA 0x337F1D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-241964126de341c2](../../evidence/conditions-sets-014.md#c-241964126de341c2) · [参数 P-4c50fed8d94ed394](../../evidence/parameters-sets-006.md#p-4c50fed8d94ed394) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044862

```text
(config)# default do-exec call-home diagnostic-signature deinstall <number:1..99999999> <cr>
```

Handler ` RVA 0x128FF210 `；selector ` 0 `；EOL ` RVA 0x337F28E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-590f69f5c012b06f](../../evidence/parameters-sets-007.md#p-590f69f5c012b06f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044812

```text
(config)# default do-exec call-home diagnostic-signature deinstall all <cr>
```

Handler ` RVA 0x128FF210 `；selector ` 1 `；EOL ` RVA 0x337F2638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044824

```text
(config)# default do-exec call-home diagnostic-signature download <number:1..99999999> <cr>
```

Handler ` RVA 0x128FEFD0 `；selector ` 0 `；EOL ` RVA 0x337F2338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-40c651dff0cca626](../../evidence/parameters-sets-005.md#p-40c651dff0cca626) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044766

```text
(config)# default do-exec call-home diagnostic-signature download all <cr>
```

Handler ` RVA 0x128FEFD0 `；selector ` 1 `；EOL ` RVA 0x337F2088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044850

```text
(config)# default do-exec call-home diagnostic-signature install <number:1..99999999> <cr>
```

Handler ` RVA 0x128FF0B0 `；selector ` 0 `；EOL ` RVA 0x337F2BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-1b6032225704560d](../../evidence/parameters-sets-003.md#p-1b6032225704560d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044884

```text
(config)# default do-exec call-home diagnostic-signature load <string> <cr>
```

Handler ` RVA 0x128FF300 `；selector ` 0 `；EOL ` RVA 0x337F2EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DS file name。

[条件 C-be85881e849a6173](../../evidence/conditions-sets-074.md#c-be85881e849a6173) · [参数 P-2bddbfb1f7b5c021](../../evidence/parameters-sets-004.md#p-2bddbfb1f7b5c021) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052611

```text
(config)# default do-exec call-home request config-sanity profile <string> <cr>
```

Handler ` RVA 0xB6D4930 `；selector ` 0 `；EOL ` RVA 0x337F1150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Profile name to use for call-home request。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3109956af5f1aef4](../../evidence/parameters-sets-004.md#p-3109956af5f1aef4) · [状态效果 S-0f78ce7b7b11e67e](../../evidence/state_effects-sets-004.md#s-0f78ce7b7b11e67e)

### path-035447

```text
(config)# default do-exec call-home request registration-info <cr>
```

Handler ` RVA 0xB6D4B70 `；selector ` 0 `；EOL ` RVA 0x337F1820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59f5c9434bb9c973](../../evidence/conditions-sets-035.md#c-59f5c9434bb9c973) · [状态效果 S-d5243367ae6155fd](../../evidence/state_effects-sets-045.md#s-d5243367ae6155fd)

### path-052637

```text
(config)# default do-exec call-home send <string> email <string> <cr>
```

Handler ` RVA 0xB6D4310 `；selector ` 0 `；EOL ` RVA 0x337F07A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` IOS exec command；` string ` Receiver's email address。

[条件 C-27805f0d3d956c98](../../evidence/conditions-sets-016.md#c-27805f0d3d956c98) · [参数 P-f743d2b9800ce8a1](../../evidence/parameters-sets-018.md#p-f743d2b9800ce8a1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052771

```text
(config)# default do-exec call-home send <string> tac-service-request <string> <cr>
```

Handler ` RVA 0xB6D4310 `；selector ` 0 `；EOL ` RVA 0x337EF6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` IOS exec CLIs list (1-127) characters, each CLI seperated by ';'.You must enclose your CLIs list in double quotes ；` string ` TAC service request number。

[条件 C-d3ed586eb9b5a8aa](../../evidence/conditions-sets-082.md#c-d3ed586eb9b5a8aa) · [参数 P-0700e2bf3f145040](../../evidence/parameters-sets-001.md#p-0700e2bf3f145040) · [状态效果 S-08068a52455e1df9](../../evidence/state_effects-sets-002.md#s-08068a52455e1df9)

### path-044662

```text
(config)# default do-exec call-home send alert-group configuration <cr>
```

Handler ` RVA 0xB6D39A0 `；selector ` 0 `；EOL ` RVA 0x337EEDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-821c1b18aa47637b](../../evidence/conditions-sets-050.md#c-821c1b18aa47637b) · [状态效果 S-074f0beb480f1600](../../evidence/state_effects-sets-002.md#s-074f0beb480f1600)

### path-052584

```text
(config)# default do-exec call-home test <string> profile <string> <cr>
```

Handler ` RVA 0xB6D3760 `；selector ` 0 `；EOL ` RVA 0x337F0C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Test message；` string ` Profile name to use for test message。

[条件 C-5ec21721dc9f537c](../../evidence/conditions-sets-037.md#c-5ec21721dc9f537c) · [参数 P-a026819f0ca18f5e](../../evidence/parameters-sets-012.md#p-a026819f0ca18f5e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-027456

```text
(config)# default do-exec cd <cr>
```

Handler ` RVA 0xD657A00 `；selector ` 0 `；EOL ` RVA 0x33EB9078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-026089

```text
(config)# default do-exec clear <cr>
```

Handler ` RVA 0xE0062B0 `；selector ` 0 `；EOL ` RVA 0x3411F6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13c9a48981117953](../../evidence/conditions-sets-008.md#c-13c9a48981117953) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054501

```text
(config)# default do-exec clear aaa cache filterserver acl <cr>
```

Handler ` RVA 0xCD2A390 `；selector ` 0 `；EOL ` RVA 0x3404BE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058051

```text
(config)# default do-exec clear aaa cache group <string> all <cr>
```

Handler ` RVA 0xDDEF640 `；selector ` 0 `；EOL ` RVA 0x3404C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Server group being cleared。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-65a6b53edc5dd687](../../evidence/parameters-sets-008.md#p-65a6b53edc5dd687) · [状态效果 S-66b6b0955c02f0d5](../../evidence/state_effects-sets-022.md#s-66b6b0955c02f0d5)

### path-047610

```text
(config)# default do-exec clear aaa counters clients <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 16 `；EOL ` RVA 0x3404B4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054493

```text
(config)# default do-exec clear aaa counters command handler <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 17 `；EOL ` RVA 0x3404B7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047636

```text
(config)# default do-exec clear aaa counters requests <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 25 `；EOL ` RVA 0x3404BA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054512

```text
(config)# default do-exec clear aaa counters servers all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 15 `；EOL ` RVA 0x3404B0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-f265f668ca02fb99](../../evidence/state_effects-sets-051.md#s-f265f668ca02fb99)

### path-047595

```text
(config)# default do-exec clear aaa local statistics <cr>
```

Handler ` RVA 0xD507150 `；selector ` 0 `；EOL ` RVA 0x33E71FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058056

```text
(config)# default do-exec clear aaa local user blocked all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 7 `；EOL ` RVA 0x33E71C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-65d9f93750302bbc](../../evidence/conditions-sets-039.md#c-65d9f93750302bbc) · [状态效果 S-8c36cdd38f28860a](../../evidence/state_effects-sets-030.md#s-8c36cdd38f28860a)

### path-058043

```text
(config)# default do-exec clear aaa local user fail-attempts all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 4 `；EOL ` RVA 0x33E718E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-37da05aae38a4175](../../evidence/state_effects-sets-012.md#s-37da05aae38a4175)

### path-058038

```text
(config)# default do-exec clear aaa local user lockout all <cr>
```

Handler ` RVA 0xD505370 `；selector ` 3 `；EOL ` RVA 0x33E71550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-4de10adb32db7bfe](../../evidence/state_effects-sets-017.md#s-4de10adb32db7bfe)

### path-047588

```text
(config)# default do-exec clear aaa tools memleak <cr>
```

Handler ` RVA 0x1371EAF0 `；selector ` 0 `；EOL ` RVA 0x35C0DDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034234

```text
(config)# default do-exec clear access-list counters <cr>
```

Handler ` RVA 0xE0AF0F0 `；selector ` 0 `；EOL ` RVA 0x341862A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dcbf105ca1b565dd](../../evidence/conditions-sets-085.md#c-dcbf105ca1b565dd) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-043979

```text
(config)# default do-exec clear access-list fqdn statistics <cr>
```

Handler ` RVA 0xCF1C1A0 `；selector ` 0 `；EOL ` RVA 0x33D662E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057120

```text
(config)# default do-exec clear access-template <number:100..199> <string> any any <cr>
```

Handler ` RVA 0xCEEFED0 `；selector ` 0 `；EOL ` RVA 0x33D2CF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IP extended access list；` string ` Dynamic Access-list name。

[条件 C-8bc23a2a6ab20b85](../../evidence/conditions-sets-054.md#c-8bc23a2a6ab20b85) · [参数 P-f1f333f2758db219](../../evidence/parameters-sets-018.md#p-f1f333f2758db219) · [状态效果 S-a074347f4c02ddee](../../evidence/state_effects-sets-034.md#s-a074347f4c02ddee)

### path-028664

```text
(config)# default do-exec clear adjacency <cr>
```

Handler ` RVA 0xB5519E0 `；selector ` 0 `；EOL ` RVA 0x3379B228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039082

```text
(config)# default do-exec clear alps circuits <cr>
```

Handler ` RVA 0x11217960 `；selector ` 1 `；EOL ` RVA 0x3541CD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-df9258ed267f8311](../../evidence/state_effects-sets-047.md#s-df9258ed267f8311)

### path-038854

```text
(config)# default do-exec clear alps counters <cr>
```

Handler ` RVA 0x11217960 `；selector ` 0 `；EOL ` RVA 0x3541C9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047639

```text
(config)# default do-exec clear archive log config <cr>
```

Handler ` RVA 0xDF0B450 `；selector ` 0 `；EOL ` RVA 0x340CDF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034314

```text
(config)# default do-exec clear arp-cache <address> <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 1 `；EOL ` RVA 0x33CD7ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address。

[条件 C-bcdb9394ba16e4b9](../../evidence/conditions-sets-073.md#c-bcdb9394ba16e4b9) · [参数 P-86bbb0bf087473ac](../../evidence/parameters-sets-010.md#p-86bbb0bf087473ac) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-028346

```text
(config)# default do-exec clear arp-cache <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 0 `；EOL ` RVA 0x33CD7B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3ecf6bdba30521bc](../../evidence/conditions-sets-024.md#c-3ecf6bdba30521bc) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044174

```text
(config)# default do-exec clear arp-cache counters ha <cr>
```

Handler ` RVA 0xCD417B0 `；selector ` 2 `；EOL ` RVA 0x33CD8210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-193872d6b0f1a2e9](../../evidence/conditions-sets-010.md#c-193872d6b0f1a2e9) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037255

```text
(config)# default do-exec clear avc sd-service <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 50 `；EOL ` RVA 0x3527DE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046545

```text
(config)# default do-exec clear avc sd-service cmds <cr>
```

Handler ` RVA 0x10DCF240 `；selector ` 0 `；EOL ` RVA 0x3527D8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046436

```text
(config)# default do-exec clear avc sd-service device-health <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 54 `；EOL ` RVA 0x3527D350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046605

```text
(config)# default do-exec clear avc sd-service device-table <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 51 `；EOL ` RVA 0x3527DB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9f2933ed5b542c9f](../../evidence/conditions-sets-062.md#c-9f2933ed5b542c9f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046491

```text
(config)# default do-exec clear avc sd-service ent-export <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 55 `；EOL ` RVA 0x3527D5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046368

```text
(config)# default do-exec clear avc sd-service flow-counters <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 53 `；EOL ` RVA 0x3527D0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a584d0e2cac5b048](../../evidence/conditions-sets-064.md#c-a584d0e2cac5b048) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053986

```text
(config)# default do-exec clear avc sd-service telemetry-table counters <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 52 `；EOL ` RVA 0x3527DE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-624c814ea19fcff8](../../evidence/conditions-sets-038.md#c-624c814ea19fcff8) · [状态效果 S-32759303323ed133](../../evidence/state_effects-sets-011.md#s-32759303323ed133)

### path-036276

```text
(config)# default do-exec clear bfd counters <cr>
```

Handler ` RVA 0x10B36A30 `；selector ` 0 `；EOL ` RVA 0x34CAD5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-a95283eff89bc6fc](../../evidence/state_effects-sets-036.md#s-a95283eff89bc6fc)

### path-036338

```text
(config)# default do-exec clear bfd dampening <cr>
```

Handler ` RVA 0x10B36A30 `；selector ` 1 `；EOL ` RVA 0x34CADBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-5b18fb17e8fb2c3f](../../evidence/state_effects-sets-020.md#s-5b18fb17e8fb2c3f)

### path-037544

```text
(config)# default do-exec clear bgp ipv4 <cr>
```

Handler ` RVA 0xF1C77B0 `；selector ` 0 `；EOL ` RVA 0x344AFD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0b3fb836298cfcdc](../../evidence/conditions-sets-005.md#c-0b3fb836298cfcdc) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-046809

```text
(config)# default do-exec clear bgp ipv4 cease <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 7 `；EOL ` RVA 0x344B0470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0b3fb836298cfcdc](../../evidence/conditions-sets-005.md#c-0b3fb836298cfcdc) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-046776

```text
(config)# default do-exec clear bgp ipv4 flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 6 `；EOL ` RVA 0x344B01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0b3fb836298cfcdc](../../evidence/conditions-sets-005.md#c-0b3fb836298cfcdc) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-046777

```text
(config)# default do-exec clear bgp ipv4 internal <cr>
```

Handler ` RVA 0xF1CD7B0 `；selector ` 0 `；EOL ` RVA 0x344B0730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b8c1491af3eddcf](../../evidence/conditions-sets-060.md#c-9b8c1491af3eddcf) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-054184

```text
(config)# default do-exec clear bgp ipv4 update-group <number:1..4294967295> <cr>
```

Handler ` RVA 0xF1CA660 `；selector ` 0 `；EOL ` RVA 0x344B1160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Clear peers in the update-group。

[条件 C-020ae5108c3293f9](../../evidence/conditions-sets-001.md#c-020ae5108c3293f9) · [参数 P-37ab67deed9369de](../../evidence/parameters-sets-005.md#p-37ab67deed9369de) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-057859

```text
(config)# default do-exec clear bgp ipv4 vrf <string> dampening <cr>
```

Handler ` RVA 0xF1CB1C0 `；selector ` 0 `；EOL ` RVA 0x344B0AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-4acfc8da0ddc4619](../../evidence/conditions-sets-029.md#c-4acfc8da0ddc4619) · [参数 P-cd1f6e9647c25601](../../evidence/parameters-sets-016.md#p-cd1f6e9647c25601) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-057881

```text
(config)# default do-exec clear bgp ipv4 vrf <string> flap-statistics <cr>
```

Handler ` RVA 0xF1CC180 `；selector ` 2 `；EOL ` RVA 0x344B0D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-4acfc8da0ddc4619](../../evidence/conditions-sets-029.md#c-4acfc8da0ddc4619) · [参数 P-cd1f6e9647c25601](../../evidence/parameters-sets-016.md#p-cd1f6e9647c25601) · [状态效果 S-a4a94bf41d0cc069](../../evidence/state_effects-sets-035.md#s-a4a94bf41d0cc069)

### path-031417

```text
(config)# default do-exec clear bridge <cr>
```

Handler ` RVA 0xF28A710 `；selector ` 0 `；EOL ` RVA 0x345E44D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-697ee8398e2334de](../../evidence/conditions-sets-041.md#c-697ee8398e2334de) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044633

```text
(config)# default do-exec clear bridge-domain route stats <cr>
```

Handler ` RVA 0xBF37330 `；selector ` 0 `；EOL ` RVA 0x33953F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a78fd5ad38c3eaf9](../../evidence/conditions-sets-065.md#c-a78fd5ad38c3eaf9) · [状态效果 S-066fa853094acc06](../../evidence/state_effects-sets-002.md#s-066fa853094acc06)

### path-031551

```text
(config)# default do-exec clear bsc <cr>
```

Handler ` RVA 0x113C36A0 `；selector ` 0 `；EOL ` RVA 0x354B4B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-031573

```text
(config)# default do-exec clear bstun <cr>
```

Handler ` RVA 0x113E1220 `；selector ` 0 `；EOL ` RVA 0x354BCA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047231

```text
(config)# default do-exec clear call admission statistics <cr>
```

Handler ` RVA 0xDEB0A00 `；selector ` 0 `；EOL ` RVA 0x3408CD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5770bff7e45873f3](../../evidence/conditions-sets-034.md#c-5770bff7e45873f3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044660

```text
(config)# default do-exec clear call-home diagnostic-signature statistics <cr>
```

Handler ` RVA 0x128FF400 `；selector ` 0 `；EOL ` RVA 0x337F4010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-695d490b0b391d16](../../evidence/conditions-sets-041.md#c-695d490b0b391d16) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052537

```text
(config)# default do-exec clear call-home diagnostic-signature statistics download <cr>
```

Handler ` RVA 0x128FF460 `；selector ` 0 `；EOL ` RVA 0x337F3FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-695d490b0b391d16](../../evidence/conditions-sets-041.md#c-695d490b0b391d16) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044636

```text
(config)# default do-exec clear call-home smart-licensing statistics <cr>
```

Handler ` RVA 0xB6D3710 `；selector ` 0 `；EOL ` RVA 0x337F4568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-797a43e59bd3b809](../../evidence/conditions-sets-047.md#c-797a43e59bd3b809) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034795

```text
(config)# default do-exec clear call-home statistics <cr>
```

Handler ` RVA 0xB6D36C0 `；selector ` 0 `；EOL ` RVA 0x337F3C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-035150

```text
(config)# default do-exec clear cdp counters <cr>
```

Handler ` RVA 0xCDA98F0 `；selector ` 0 `；EOL ` RVA 0x33CE01A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-035204

```text
(config)# default do-exec clear cdp table <cr>
```

Handler ` RVA 0xCDA9940 `；selector ` 0 `；EOL ` RVA 0x33CE0450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044541

```text
(config)# default do-exec clear cef interface policy-statistics <cr>
```

Handler ` RVA 0xB3DDB50 `；selector ` 0 `；EOL ` RVA 0x337647B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-edbdbf9af3b2d05d](../../evidence/conditions-sets-092.md#c-edbdbf9af3b2d05d) · [状态效果 S-d0d9872c86afdb24](../../evidence/state_effects-sets-044.md#s-d0d9872c86afdb24)

### path-035235

```text
(config)# default do-exec clear cef linecard <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 3 `；EOL ` RVA 0x33733770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044874

```text
(config)# default do-exec clear cef linecard Adjacency <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 2 `；EOL ` RVA 0x33733748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044837

```text
(config)# default do-exec clear cef linecard Interface <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 1 `；EOL ` RVA 0x337334A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044786

```text
(config)# default do-exec clear cef linecard Prefix <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 0 `；EOL ` RVA 0x337331F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044682

```text
(config)# default do-exec clear cef linecard events <cr>
```

Handler ` RVA 0xB2C6700 `；selector ` 4 `；EOL ` RVA 0x33732ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89c15b7b43dab9e3](../../evidence/conditions-sets-053.md#c-89c15b7b43dab9e3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044498

```text
(config)# default do-exec clear cef load-balance statistics <cr>
```

Handler ` RVA 0xB3F90A0 `；selector ` 0 `；EOL ` RVA 0x33764AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044802

```text
(config)# default do-exec clear cef table IPv4 <cr>
```

Handler ` RVA 0xB5C9AD0 `；selector ` 0 `；EOL ` RVA 0x337ADA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f9c385ba10038d1](../../evidence/conditions-sets-006.md#c-0f9c385ba10038d1) · [状态效果 S-fa7c4b3cad648af4](../../evidence/state_effects-sets-053.md#s-fa7c4b3cad648af4)

### path-052559

```text
(config)# default do-exec clear cef table IPv4 consistency-check <cr>
```

Handler ` RVA 0xB5C9A70 `；selector ` 0 `；EOL ` RVA 0x337AD630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7e2805c08fbc4fe8](../../evidence/conditions-sets-049.md#c-7e2805c08fbc4fe8) · [状态效果 S-fa7c4b3cad648af4](../../evidence/state_effects-sets-053.md#s-fa7c4b3cad648af4)

### path-036418

```text
(config)# default do-exec clear cft stats <cr>
```

Handler ` RVA 0x12945F20 `；selector ` 1 `；EOL ` RVA 0x358FD9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1632491c2ff8b76](../../evidence/conditions-sets-081.md#c-d1632491c2ff8b76) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034558

```text
(config)# default do-exec clear checkpoint clients <cr>
```

Handler ` RVA 0xCDB61A0 `；selector ` 0 `；EOL ` RVA 0x33CEE3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034524

```text
(config)# default do-exec clear checkpoint entities <cr>
```

Handler ` RVA 0xCDB63F0 `；selector ` 0 `；EOL ` RVA 0x33CEE138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034587

```text
(config)# default do-exec clear checkpoint statistics <cr>
```

Handler ` RVA 0xCDB6600 `；selector ` 0 `；EOL ` RVA 0x33CEE688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036214

```text
(config)# default do-exec clear class-map control <cr>
```

Handler ` RVA 0x10A5CC50 `；selector ` 0 `；EOL ` RVA 0x34C768B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e89804328378fef3](../../evidence/conditions-sets-090.md#c-e89804328378fef3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037520

```text
(config)# default do-exec clear clns cache <cr>
```

Handler ` RVA 0x10592040 `；selector ` 1 `；EOL ` RVA 0x34B6B560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037587

```text
(config)# default do-exec clear clns es-neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 2 `；EOL ` RVA 0x34B6BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037629

```text
(config)# default do-exec clear clns is-neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 3 `；EOL ` RVA 0x34B6BD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037671

```text
(config)# default do-exec clear clns neighbors <cr>
```

Handler ` RVA 0x10592040 `；selector ` 4 `；EOL ` RVA 0x34B6C000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037559

```text
(config)# default do-exec clear clns route <cr>
```

Handler ` RVA 0x10592040 `；selector ` 5 `；EOL ` RVA 0x34B6B808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037714

```text
(config)# default do-exec clear clns traffic <cr>
```

Handler ` RVA 0x10592040 `；selector ` 6 `；EOL ` RVA 0x34B6C2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047902

```text
(config)# default do-exec clear cns config stats <cr>
```

Handler ` RVA 0xF31ED20 `；selector ` 0 `；EOL ` RVA 0x34609B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038656

```text
(config)# default do-exec clear cns counters <cr>
```

Handler ` RVA 0xF2FE680 `；selector ` 0 `；EOL ` RVA 0x346051C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047867

```text
(config)# default do-exec clear cns event stats <cr>
```

Handler ` RVA 0xF35DEC0 `；selector ` 0 `；EOL ` RVA 0x34617250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048005

```text
(config)# default do-exec clear cns image connections <cr>
```

Handler ` RVA 0xF36DAA0 `；selector ` 0 `；EOL ` RVA 0x3461C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047946

```text
(config)# default do-exec clear cns image status <cr>
```

Handler ` RVA 0xF36D980 `；selector ` 0 `；EOL ` RVA 0x3461BDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034113

```text
(config)# default do-exec clear configuration lock <cr>
```

Handler ` RVA 0xDF3AC00 `；selector ` 0 `；EOL ` RVA 0x340B6170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-031325

```text
(config)# default do-exec clear control-plane <cr>
```

Handler ` RVA 0xE47F2B0 `；selector ` 0 `；EOL ` RVA 0x342C48C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034303

```text
(config)# default do-exec clear controller all <cr>
```

Handler ` RVA 0xECFC750 `；selector ` 0 `；EOL ` RVA 0x343F6970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-246b4b7c76529398](../../evidence/conditions-sets-014.md#c-246b4b7c76529398) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-027974

```text
(config)# default do-exec clear counters <cr>
```

Handler ` RVA 0xE40DC10 `；selector ` 0 `；EOL ` RVA 0x3411FD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a24e4f16969ee72](../../evidence/conditions-sets-029.md#c-4a24e4f16969ee72) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047555

```text
(config)# default do-exec clear crypto autovpn session <cr>
```

Handler ` RVA 0x165EC340 `；selector ` 1 `；EOL ` RVA 0x35FA6D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058031

```text
(config)# default do-exec clear crypto autovpn session peer <number:1..2147483647> <cr>
```

Handler ` RVA 0x165EC340 `；selector ` 0 `；EOL ` RVA 0x35FA6DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Peerno。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-5d2397c60ef477d4](../../evidence/parameters-sets-007.md#p-5d2397c60ef477d4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047535

```text
(config)# default do-exec clear crypto ceal statistics <cr>
```

Handler ` RVA 0x120E8990 `；selector ` 0 `；EOL ` RVA 0x3579FA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-6eb6c481a0195541](../../evidence/state_effects-sets-024.md#s-6eb6c481a0195541)

### path-054502

```text
(config)# default do-exec clear crypto engine accelerator counter <cr>
```

Handler ` RVA 0x120CAC10 `；selector ` 0 `；EOL ` RVA 0x357920E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a8e49c9039b54cd7](../../evidence/conditions-sets-065.md#c-a8e49c9039b54cd7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047564

```text
(config)# default do-exec clear crypto ha statistics <cr>
```

Handler ` RVA 0x1924CF00 `；selector ` 0 `；EOL ` RVA 0x3697A7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-125918ebee950010](../../evidence/conditions-sets-007.md#c-125918ebee950010) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047499

```text
(config)# default do-exec clear crypto pki benchmarks <cr>
```

Handler ` RVA 0x120B7E10 `；selector ` 0 `；EOL ` RVA 0x35752EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047450

```text
(config)# default do-exec clear crypto pki counters <cr>
```

Handler ` RVA 0x11FC7870 `；selector ` 0 `；EOL ` RVA 0x35752C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047545

```text
(config)# default do-exec clear crypto pki crl <cr>
```

Handler ` RVA 0x11F2ECF0 `；selector ` 0 `；EOL ` RVA 0x35753188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038243

```text
(config)# default do-exec clear cts credentials <cr>
```

Handler ` RVA 0x13047780 `；selector ` 0 `；EOL ` RVA 0x35A1D248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0648da1944570fa8](../../evidence/conditions-sets-003.md#c-0648da1944570fa8) · [状态效果 S-50e1ae9af67ae8a2](../../evidence/state_effects-sets-018.md#s-50e1ae9af67ae8a2)

### path-048279

```text
(config)# default do-exec clear cts role-based counters <cr>
```

Handler ` RVA 0x141FE9C0 `；selector ` 0 `；EOL ` RVA 0x35CFE5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34ee87a193a0a00e](../../evidence/conditions-sets-021.md#c-34ee87a193a0a00e) · [状态效果 S-a33d115748d63265](../../evidence/state_effects-sets-035.md#s-a33d115748d63265)

### path-054327

```text
(config)# default do-exec clear device-tracking database policy <string> <cr>
```

Handler ` RVA 0x136806D0 `；selector ` 1020 `；EOL ` RVA 0x35BD6BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Snooping Policy name to be cleared。

[条件 C-3798f376b9381e80](../../evidence/conditions-sets-022.md#c-3798f376b9381e80) · [参数 P-e868e12c898fe3d6](../../evidence/parameters-sets-017.md#p-e868e12c898fe3d6) · [状态效果 S-f4c013a7c17fa0cd](../../evidence/state_effects-sets-052.md#s-f4c013a7c17fa0cd)

### path-037804

```text
(config)# default do-exec clear device-tracking events <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1021 `；EOL ` RVA 0x35BD7808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3798f376b9381e80](../../evidence/conditions-sets-022.md#c-3798f376b9381e80) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037850

```text
(config)# default do-exec clear device-tracking messages <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1022 `；EOL ` RVA 0x35BD7AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3798f376b9381e80](../../evidence/conditions-sets-022.md#c-3798f376b9381e80) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037702

```text
(config)# default do-exec clear dhcp-server-tracking database <cr>
```

Handler ` RVA 0x136A1FB0 `；selector ` 0 `；EOL ` RVA 0x35C01760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039091

```text
(config)# default do-exec clear diagnostic event-log <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cc2706f2b049ba7](../../evidence/conditions-sets-018.md#c-2cc2706f2b049ba7) · [状态效果 S-518726d224b05ab5](../../evidence/state_effects-sets-018.md#s-518726d224b05ab5)

### path-054701

```text
(config)# default do-exec clear diagnostic event-log slot all <cr>
```

Handler ` RVA 0xEB6AF80 `；selector ` 1 `；EOL ` RVA 0x343C8708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1b21cdc38c280145](../../evidence/conditions-sets-011.md#c-1b21cdc38c280145) · [状态效果 S-647aa3b74e1f84e7](../../evidence/state_effects-sets-021.md#s-647aa3b74e1f84e7)

### path-028407

```text
(config)# default do-exec clear dialer <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 0 `；EOL ` RVA 0x34666688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7630f1e5c0c96cbe](../../evidence/conditions-sets-046.md#c-7630f1e5c0c96cbe) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052283

```text
(config)# default do-exec clear dialer dnis group <string> <cr>
```

Handler ` RVA 0xF4E9360 `；selector ` 0 `；EOL ` RVA 0x34674518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS group name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-05f42c525d7c2f8f](../../evidence/parameters-sets-001.md#p-05f42c525d7c2f8f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052234

```text
(config)# default do-exec clear dialer dnis number <string> <cr>
```

Handler ` RVA 0xF4E9130 `；selector ` 1 `；EOL ` RVA 0x34673F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS number。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-a6076225f83e98fc](../../evidence/parameters-sets-013.md#p-a6076225f83e98fc) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056848

```text
(config)# default do-exec clear dialer dnis range <string> <string> <cr>
```

Handler ` RVA 0xF4E9130 `；selector ` 2 `；EOL ` RVA 0x34674258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS range start；` string ` DNIS range end。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-6ff2f7c7e2918e74](../../evidence/parameters-sets-009.md#p-6ff2f7c7e2918e74) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034406

```text
(config)# default do-exec clear dialer sessions <cr>
```

Handler ` RVA 0xF4CD050 `；selector ` 1 `；EOL ` RVA 0x34673BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048894

```text
(config)# default do-exec clear diameter gx statistics <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 22 `；EOL ` RVA 0x338ADE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-055096

```text
(config)# default do-exec clear diameter peer connection all <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 34 `；EOL ` RVA 0x338AD2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058324

```text
(config)# default do-exec clear diameter peer connection name <string> <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 21 `；EOL ` RVA 0x338AD598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Peer name。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [参数 P-ac0b956092f2b047](../../evidence/parameters-sets-013.md#p-ac0b956092f2b047) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-055140

```text
(config)# default do-exec clear diameter peer statistics all <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 36 `；EOL ` RVA 0x338AD870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058335

```text
(config)# default do-exec clear diameter peer statistics name <string> <cr>
```

Handler ` RVA 0xBD05EE0 `；selector ` 35 `；EOL ` RVA 0x338ADB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Peer name。

[条件 C-548a47bb2d94eead](../../evidence/conditions-sets-033.md#c-548a47bb2d94eead) · [参数 P-56d578d820d5ba55](../../evidence/parameters-sets-007.md#p-56d578d820d5ba55) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038279

```text
(config)# default do-exec clear dlep counters <cr>
```

Handler ` RVA 0x132D3330 `；selector ` 3 `；EOL ` RVA 0x35A5A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d01143ef4c108a3f](../../evidence/conditions-sets-080.md#c-d01143ef4c108a3f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039207

```text
(config)# default do-exec clear dlsw reachability <cr>
```

Handler ` RVA 0x11421C60 `；selector ` 0 `；EOL ` RVA 0x354CC100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0af2364a1a48bd94](../../evidence/conditions-sets-005.md#c-0af2364a1a48bd94) · [状态效果 S-f75e4c8232a9360f](../../evidence/state_effects-sets-052.md#s-f75e4c8232a9360f)

### path-039087

```text
(config)# default do-exec clear dmvpn statistics <cr>
```

Handler ` RVA 0xF4F28F0 `；selector ` 0 `；EOL ` RVA 0x3467EC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-22f4bc6d1acce73a](../../evidence/conditions-sets-014.md#c-22f4bc6d1acce73a) · [状态效果 S-2bfcd4d9ffb84204](../../evidence/state_effects-sets-010.md#s-2bfcd4d9ffb84204)

### path-038892

```text
(config)# default do-exec clear drip counters <cr>
```

Handler ` RVA 0x112B2F80 `；selector ` 1 `；EOL ` RVA 0x3544D280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034053

```text
(config)# default do-exec clear dspfarm statistics <cr>
```

Handler ` RVA 0x188BAB20 `；selector ` 0 `；EOL ` RVA 0x367F3F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-96f10969fdc2e8a7](../../evidence/state_effects-sets-032.md#s-96f10969fdc2e8a7)

### path-036726

```text
(config)# default do-exec clear dtp counter <cr>
```

Handler ` RVA 0x15F14E10 `；selector ` 0 `；EOL ` RVA 0x35E66F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054389

```text
(config)# default do-exec clear eigrp address-family ipv4 events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346B5888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-14e69e2812516d38](../../evidence/state_effects-sets-005.md#s-14e69e2812516d38)

### path-054369

```text
(config)# default do-exec clear eigrp address-family ipv4 logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346B55E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-14e69e2812516d38](../../evidence/state_effects-sets-005.md#s-14e69e2812516d38)

### path-054417

```text
(config)# default do-exec clear eigrp address-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346B4A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47089db8aeb7e60d](../../evidence/conditions-sets-028.md#c-47089db8aeb7e60d) · [状态效果 S-14e69e2812516d38](../../evidence/state_effects-sets-005.md#s-14e69e2812516d38)

### path-054426

```text
(config)# default do-exec clear eigrp address-family ipv4 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 73 `；EOL ` RVA 0x346B5DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-14e69e2812516d38](../../evidence/state_effects-sets-005.md#s-14e69e2812516d38)

### path-059345

```text
(config)# default do-exec clear eigrp address-family ipv4 topology <address> <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346B4EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [参数 P-3fb9dae9bb0abdd4](../../evidence/parameters-sets-005.md#p-3fb9dae9bb0abdd4) · [状态效果 S-35f4fc5853b2c20a](../../evidence/state_effects-sets-012.md#s-35f4fc5853b2c20a)

### path-057990

```text
(config)# default do-exec clear eigrp address-family ipv4 topology active <cr>
```

Handler ` RVA 0xF573DF0 `；selector ` 69 `；EOL ` RVA 0x346B51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-14e69e2812516d38](../../evidence/state_effects-sets-005.md#s-14e69e2812516d38)

### path-054411

```text
(config)# default do-exec clear eigrp address-family ipv4 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 70 `；EOL ` RVA 0x346B5B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-605a4913a4ab8136](../../evidence/conditions-sets-037.md#c-605a4913a4ab8136) · [状态效果 S-14e69e2812516d38](../../evidence/state_effects-sets-005.md#s-14e69e2812516d38)

### path-054370

```text
(config)# default do-exec clear eigrp address-family ipv6 events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x35453F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-4f39a8105cc23a75](../../evidence/state_effects-sets-017.md#s-4f39a8105cc23a75)

### path-054350

```text
(config)# default do-exec clear eigrp address-family ipv6 logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x35453C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-4f39a8105cc23a75](../../evidence/state_effects-sets-017.md#s-4f39a8105cc23a75)

### path-054395

```text
(config)# default do-exec clear eigrp address-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35453180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c543cb4cc0b7c573](../../evidence/conditions-sets-076.md#c-c543cb4cc0b7c573) · [状态效果 S-4f39a8105cc23a75](../../evidence/state_effects-sets-017.md#s-4f39a8105cc23a75)

### path-054412

```text
(config)# default do-exec clear eigrp address-family ipv6 perf-stats <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 73 `；EOL ` RVA 0x35454478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-4f39a8105cc23a75](../../evidence/state_effects-sets-017.md#s-4f39a8105cc23a75)

### path-057973

```text
(config)# default do-exec clear eigrp address-family ipv6 topology active <cr>
```

Handler ` RVA 0xF573DF0 `；selector ` 69 `；EOL ` RVA 0x35453878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-4f39a8105cc23a75](../../evidence/state_effects-sets-017.md#s-4f39a8105cc23a75)

### path-054390

```text
(config)# default do-exec clear eigrp address-family ipv6 traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 70 `；EOL ` RVA 0x354541D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-87339d49ac7f31cd](../../evidence/conditions-sets-052.md#c-87339d49ac7f31cd) · [状态效果 S-4f39a8105cc23a75](../../evidence/state_effects-sets-017.md#s-4f39a8105cc23a75)

### path-054306

```text
(config)# default do-exec clear eigrp service-family external-client <string> <cr>
```

Handler ` RVA 0x104726A0 `；selector ` 41 `；EOL ` RVA 0x34B3AB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client Label。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-6e6d51b6eb7ccc0f](../../evidence/parameters-sets-009.md#p-6e6d51b6eb7ccc0f) · [状态效果 S-3db077244428fd33](../../evidence/state_effects-sets-014.md#s-3db077244428fd33)

### path-054388

```text
(config)# default do-exec clear eigrp service-family ipv4 events <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 71 `；EOL ` RVA 0x346EFFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-3daab5328f0765ac](../../evidence/state_effects-sets-014.md#s-3daab5328f0765ac)

### path-054368

```text
(config)# default do-exec clear eigrp service-family ipv4 logging <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 72 `；EOL ` RVA 0x346EFD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-3daab5328f0765ac](../../evidence/state_effects-sets-014.md#s-3daab5328f0765ac)

### path-054416

```text
(config)# default do-exec clear eigrp service-family ipv4 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x346EEFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4aebcafa3efb865](../../evidence/conditions-sets-076.md#c-c4aebcafa3efb865) · [状态效果 S-3daab5328f0765ac](../../evidence/state_effects-sets-014.md#s-3daab5328f0765ac)

### path-060262

```text
(config)# default do-exec clear eigrp service-family ipv4 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x346EF660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-1c902772e46b736b](../../evidence/conditions-sets-011.md#c-1c902772e46b736b) · [参数 P-981a610bcc4e38b2](../../evidence/parameters-sets-012.md#p-981a610bcc4e38b2) · [状态效果 S-3daab5328f0765ac](../../evidence/state_effects-sets-014.md#s-3daab5328f0765ac)

### path-057980

```text
(config)# default do-exec clear eigrp service-family ipv4 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x346EF930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-3daab5328f0765ac](../../evidence/state_effects-sets-014.md#s-3daab5328f0765ac)

### path-054410

```text
(config)# default do-exec clear eigrp service-family ipv4 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x346F0288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4480588a626db709](../../evidence/conditions-sets-027.md#c-4480588a626db709) · [状态效果 S-3daab5328f0765ac](../../evidence/state_effects-sets-014.md#s-3daab5328f0765ac)

### path-054424

```text
(config)# default do-exec clear eigrp service-family ipv6 events <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 71 `；EOL ` RVA 0x35476980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-898e5a62382af681](../../evidence/state_effects-sets-029.md#s-898e5a62382af681)

### path-054408

```text
(config)# default do-exec clear eigrp service-family ipv6 logging <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 72 `；EOL ` RVA 0x354766D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-898e5a62382af681](../../evidence/state_effects-sets-029.md#s-898e5a62382af681)

### path-054440

```text
(config)# default do-exec clear eigrp service-family ipv6 neighbors <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 67 `；EOL ` RVA 0x35475988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5079892e533d3ab0](../../evidence/conditions-sets-031.md#c-5079892e533d3ab0) · [状态效果 S-898e5a62382af681](../../evidence/state_effects-sets-029.md#s-898e5a62382af681)

### path-060264

```text
(config)# default do-exec clear eigrp service-family ipv6 topology <number:1..65535> : <number:1..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 68 `；EOL ` RVA 0x35476000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance；` unsigned_number ` Service:Sub-Service:Instance.Instance.Instance.Instance。

[条件 C-1993d4bf841bf125](../../evidence/conditions-sets-010.md#c-1993d4bf841bf125) · [参数 P-b117aaae787be4fd](../../evidence/parameters-sets-013.md#p-b117aaae787be4fd) · [状态效果 S-898e5a62382af681](../../evidence/state_effects-sets-029.md#s-898e5a62382af681)

### path-057996

```text
(config)# default do-exec clear eigrp service-family ipv6 topology active <cr>
```

Handler ` RVA 0xF593530 `；selector ` 69 `；EOL ` RVA 0x354762D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-898e5a62382af681](../../evidence/state_effects-sets-029.md#s-898e5a62382af681)

### path-054438

```text
(config)# default do-exec clear eigrp service-family ipv6 traffic <cr>
```

Handler ` RVA 0xF5933F0 `；selector ` 70 `；EOL ` RVA 0x35476C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-619ec423152a32a8](../../evidence/conditions-sets-038.md#c-619ec423152a32a8) · [状态效果 S-898e5a62382af681](../../evidence/state_effects-sets-029.md#s-898e5a62382af681)

### path-035149

```text
(config)# default do-exec clear entry <number:0..256> <cr>
```

Handler ` RVA 0xCCF7FE0 `；selector ` 0 `；EOL ` RVA 0x33C66A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Queue entry number。

[条件 C-ae130bfe4f93ffb9](../../evidence/conditions-sets-067.md#c-ae130bfe4f93ffb9) · [参数 P-baff37d66d7bf69e](../../evidence/parameters-sets-014.md#p-baff37d66d7bf69e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038477

```text
(config)# default do-exec clear environment counters <cr>
```

Handler ` RVA 0xE123D20 `；selector ` 16 `；EOL ` RVA 0x3420AE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034518

```text
(config)# default do-exec clear eobc counters <cr>
```

Handler ` RVA 0xED896F0 `；selector ` 0 `；EOL ` RVA 0x3442E440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034554

```text
(config)# default do-exec clear eobc interface <cr>
```

Handler ` RVA 0xED897B0 `；selector ` 0 `；EOL ` RVA 0x3442E6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059971

```text
(config)# default do-exec clear ethernet cfm ais domain <string> mpid <number:1..8191> port <cr>
```

Handler ` RVA 0xBDD3860 `；selector ` 0 `；EOL ` RVA 0x338CDFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` maintenance domain name；` unsigned_number ` Maintenance End Point Identifier。

[条件 C-334f7c49a7ede4e3](../../evidence/conditions-sets-020.md#c-334f7c49a7ede4e3) · [参数 P-d12e398db42d71ec](../../evidence/parameters-sets-016.md#p-d12e398db42d71ec) · [状态效果 S-37ad95ba7d396802](../../evidence/state_effects-sets-012.md#s-37ad95ba7d396802)

### path-044716

```text
(config)# default do-exec clear ethernet cfm ccm-learning-database <cr>
```

Handler ` RVA 0xBDD3D70 `；selector ` 0 `；EOL ` RVA 0x338CF840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6babdf68d76558b8](../../evidence/conditions-sets-042.md#c-6babdf68d76558b8) · [状态效果 S-d48117d61bad52cf](../../evidence/state_effects-sets-045.md#s-d48117d61bad52cf)

### path-044525

```text
(config)# default do-exec clear ethernet cfm errors <cr>
```

Handler ` RVA 0xBDD2B30 `；selector ` 0 `；EOL ` RVA 0x338CE920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6645a68419d2583e](../../evidence/conditions-sets-040.md#c-6645a68419d2583e) · [状态效果 S-278530bab82c1c38](../../evidence/state_effects-sets-009.md#s-278530bab82c1c38)

### path-052440

```text
(config)# default do-exec clear ethernet cfm fast-timeout statistics <cr>
```

Handler ` RVA 0xBDD3CD0 `；selector ` 0 `；EOL ` RVA 0x338CF3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49fdd367145abd42](../../evidence/conditions-sets-029.md#c-49fdd367145abd42) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056910

```text
(config)# default do-exec clear ethernet cfm latching-loopback discover-phase mep <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 1 `；EOL ` RVA 0x338CD438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-03fda3c4f0a09dd2](../../evidence/state_effects-sets-001.md#s-03fda3c4f0a09dd2)

### path-056905

```text
(config)# default do-exec clear ethernet cfm latching-loopback discover-phase mip <cr>
```

Handler ` RVA 0xBDD3360 `；selector ` 2 `；EOL ` RVA 0x338CD6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-d87c524692309d76](../../evidence/state_effects-sets-046.md#s-d87c524692309d76)

### path-052298

```text
(config)# default do-exec clear ethernet cfm maintenance-points remote <cr>
```

Handler ` RVA 0xBDD28E0 `；selector ` 0 `；EOL ` RVA 0x338CC7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058926

```text
(config)# default do-exec clear ethernet cfm maintenance-points remote domain <string> <cr>
```

Handler ` RVA 0xBDD2A20 `；selector ` 0 `；EOL ` RVA 0x338CC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` maintenance domain name。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [参数 P-b4f885fc792161b1](../../evidence/parameters-sets-014.md#p-b4f885fc792161b1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058938

```text
(config)# default do-exec clear ethernet cfm pm session db <number:0..8000> <cr>
```

Handler ` RVA 0xBE8C2A0 `；selector ` 0 `；EOL ` RVA 0x339155B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Session Id。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [参数 P-c0ee7e00d5a1eec9](../../evidence/parameters-sets-015.md#p-c0ee7e00d5a1eec9) · [状态效果 S-d46b6a865cc87a95](../../evidence/state_effects-sets-045.md#s-d46b6a865cc87a95)

### path-044372

```text
(config)# default do-exec clear ethernet cfm statistics <cr>
```

Handler ` RVA 0xBDD3070 `；selector ` 0 `；EOL ` RVA 0x338CD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044305

```text
(config)# default do-exec clear ethernet cfm traceroute-cache <cr>
```

Handler ` RVA 0xBDD3D20 `；selector ` 0 `；EOL ` RVA 0x338CCD08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044287

```text
(config)# default do-exec clear ethernet lmi statistics <cr>
```

Handler ` RVA 0xBEC38F0 `；selector ` 0 `；EOL ` RVA 0x339203E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e252cf8c35d4f1d1](../../evidence/conditions-sets-087.md#c-e252cf8c35d4f1d1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044284

```text
(config)# default do-exec clear ethernet oam statistics <cr>
```

Handler ` RVA 0xBEECC20 `；selector ` 44 `；EOL ` RVA 0x3392F790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058967

```text
(config)# default do-exec clear ethernet service instance id <number:1..16384> mac-tunnel <cr>
```

Handler ` RVA 0xC0188D0 `；selector ` 1 `；EOL ` RVA 0x33979C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-ea732fa9e043fe11](../../evidence/conditions-sets-091.md#c-ea732fa9e043fe11) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-2a2f78bc3e16e530](../../evidence/state_effects-sets-009.md#s-2a2f78bc3e16e530)

### path-059673

```text
(config)# default do-exec clear ethernet service instance id <number:1..16384> mac-tunnel errdisable <cr>
```

Handler ` RVA 0xC0357A0 `；selector ` 3 `；EOL ` RVA 0x33985898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-6966d62b8dc7328d](../../evidence/conditions-sets-041.md#c-6966d62b8dc7328d) · [参数 P-1dc6a57d8cba6c9f](../../evidence/parameters-sets-003.md#p-1dc6a57d8cba6c9f) · [状态效果 S-2a2f78bc3e16e530](../../evidence/state_effects-sets-009.md#s-2a2f78bc3e16e530)

### path-052328

```text
(config)# default do-exec clear ethernet service internal back-trace <cr>
```

Handler ` RVA 0xC013D80 `；selector ` 0 `；EOL ` RVA 0x3397BF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-59b07fa78c1ec760](../../evidence/conditions-sets-035.md#c-59b07fa78c1ec760) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052352

```text
(config)# default do-exec clear ethernet service ipc statistics <cr>
```

Handler ` RVA 0xBF920F0 `；selector ` 0 `；EOL ` RVA 0x33962C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace8b6fac2666806](../../evidence/conditions-sets-067.md#c-ace8b6fac2666806) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054930

```text
(config)# default do-exec clear event manager detector counters <cr>
```

Handler ` RVA 0xC0CB550 `；selector ` 0 `；EOL ` RVA 0x339BCBB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058273

```text
(config)# default do-exec clear event manager detector rpc counters <cr>
```

Handler ` RVA 0xC0A29A0 `；selector ` 0 `；EOL ` RVA 0x3399C3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058291

```text
(config)# default do-exec clear event manager detector rpc sessions <cr>
```

Handler ` RVA 0xC0A2BA0 `；selector ` 0 `；EOL ` RVA 0x3399C698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054903

```text
(config)# default do-exec clear event manager server counters <cr>
```

Handler ` RVA 0xC0CB5C0 `；selector ` 0 `；EOL ` RVA 0x339BC8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-028315

```text
(config)# default do-exec clear facility-alarm <cr>
```

Handler ` RVA 0xC299EF0 `；selector ` 0 `；EOL ` RVA 0x33A28388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034163

```text
(config)# default do-exec clear facility-alarm critical <cr>
```

Handler ` RVA 0xC299990 `；selector ` 0 `；EOL ` RVA 0x33A27F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-58bde938de3478f4](../../evidence/state_effects-sets-019.md#s-58bde938de3478f4)

### path-044680

```text
(config)# default do-exec clear flow exporter statistics <cr>
```

Handler ` RVA 0xC154D30 `；selector ` 0 `；EOL ` RVA 0x339E3370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039594

```text
(config)# default do-exec clear flowspec afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 5 `；EOL ` RVA 0x35A98610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a0a86034b1ad4591](../../evidence/conditions-sets-062.md#c-a0a86034b1ad4591) · [状态效果 S-230834bdf0c56b53](../../evidence/state_effects-sets-008.md#s-230834bdf0c56b53)

### path-048444

```text
(config)# default do-exec clear flowspec counters afi-all <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 2 `；EOL ` RVA 0x35A97D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-b618c8b63603f795](../../evidence/state_effects-sets-039.md#s-b618c8b63603f795)

### path-048322

```text
(config)# default do-exec clear flowspec counters internal <cr>
```

Handler ` RVA 0x1344A810 `；selector ` 4 `；EOL ` RVA 0x35A97918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-2629d6c624653b55](../../evidence/state_effects-sets-009.md#s-2629d6c624653b55)

### path-047129

```text
(config)# default do-exec clear fqdn packet statistics <cr>
```

Handler ` RVA 0xC2E0BF0 `；selector ` 0 `；EOL ` RVA 0x33A3CB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-dce0c27cfebbdb43](../../evidence/state_effects-sets-047.md#s-dce0c27cfebbdb43)

### path-037203

```text
(config)# default do-exec clear frame-relay counter <cr>
```

Handler ` RVA 0xF606570 `；selector ` 18 `；EOL ` RVA 0x34700850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037247

```text
(config)# default do-exec clear frame-relay inarp <cr>
```

Handler ` RVA 0xF62D080 `；selector ` 17 `；EOL ` RVA 0x3470EE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037463

```text
(config)# default do-exec clear host <string> <cr>
```

Handler ` RVA 0xD128DD0 `；selector ` 0 `；EOL ` RVA 0x33D95930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Hostname to delete (* for all entries)。

[条件 C-7cd4fea57bafbb25](../../evidence/conditions-sets-048.md#c-7cd4fea57bafbb25) · [参数 P-5fa77e3c3044d1c6](../../evidence/parameters-sets-008.md#p-5fa77e3c3044d1c6) · [状态效果 S-7abd10a278d6ebda](../../evidence/state_effects-sets-026.md#s-7abd10a278d6ebda)

### path-037005

```text
(config)# default do-exec clear icm statistics <cr>
```

Handler ` RVA 0xC2FAF60 `；selector ` 0 `；EOL ` RVA 0x33A40790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ef0635c7c3dab4e9](../../evidence/state_effects-sets-051.md#s-ef0635c7c3dab4e9)

### path-031766

```text
(config)# default do-exec clear iox <cr>
```

Handler ` RVA 0xEADA610 `；selector ` 0 `；EOL ` RVA 0x343A3698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045381

```text
(config)# default do-exec clear ip access-list counters <cr>
```

Handler ` RVA 0xCEEDDF0 `；selector ` 0 `；EOL ` RVA 0x33D2D580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-29b5b928497ba869](../../evidence/conditions-sets-016.md#c-29b5b928497ba869) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037167

```text
(config)# default do-exec clear ip accounting <cr>
```

Handler ` RVA 0xD17A5F0 `；selector ` 0 `；EOL ` RVA 0x33DA6DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ab77f82289980efb](../../evidence/state_effects-sets-036.md#s-ab77f82289980efb)

### path-044947

```text
(config)# default do-exec clear ip arp <address> <cr>
```

Handler ` RVA 0xCF5FF90 `；selector ` 0 `；EOL ` RVA 0x33D1E250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of dynamic ARP entry。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-b690c2ce67487b89](../../evidence/parameters-sets-014.md#p-b690c2ce67487b89) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052755

```text
(config)# default do-exec clear ip arp poll statistics <cr>
```

Handler ` RVA 0xCFE25A0 `；selector ` 0 `；EOL ` RVA 0x33D1E538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036614

```text
(config)# default do-exec clear ip cache <cr>
```

Handler ` RVA 0xD49E510 `；selector ` 0 `；EOL ` RVA 0x33E54E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046322

```text
(config)# default do-exec clear ip casa counters <cr>
```

Handler ` RVA 0x1132C870 `；selector ` 0 `；EOL ` RVA 0x35499608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046640

```text
(config)# default do-exec clear ip cef event-log <cr>
```

Handler ` RVA 0xB5ECF20 `；selector ` 0 `；EOL ` RVA 0x337B4F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046587

```text
(config)# default do-exec clear ip cef inconsistency <cr>
```

Handler ` RVA 0xB5ECEE0 `；selector ` 0 `；EOL ` RVA 0x337B4CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046954

```text
(config)# default do-exec clear ip cef prefix-statistics <cr>
```

Handler ` RVA 0xB61F7B0 `；selector ` 0 `；EOL ` RVA 0x337C4660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d5f42d62acdf9713](../../evidence/conditions-sets-083.md#c-d5f42d62acdf9713) · [状态效果 S-6ff746b1d5a8d41a](../../evidence/state_effects-sets-024.md#s-6ff746b1d5a8d41a)

### path-036619

```text
(config)# default do-exec clear ip cgmp <cr>
```

Handler ` RVA 0xF6779A0 `；selector ` 0 `；EOL ` RVA 0x34746408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15c8fb31734caa71](../../evidence/conditions-sets-009.md#c-15c8fb31734caa71) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054223

```text
(config)# default do-exec clear ip dhcp binding <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 1 `；EOL ` RVA 0x33DE44E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Clear a specific binding。

[条件 C-915a8514a34f7b53](../../evidence/conditions-sets-056.md#c-915a8514a34f7b53) · [参数 P-701f423f9be8657b](../../evidence/parameters-sets-009.md#p-701f423f9be8657b) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054249

```text
(config)# default do-exec clear ip dhcp conflict <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 3 `；EOL ` RVA 0x33DE4BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Clear a specific conflict。

[条件 C-1ef20701edbe572d](../../evidence/conditions-sets-012.md#c-1ef20701edbe572d) · [参数 P-98938e3b3a412be2](../../evidence/parameters-sets-012.md#p-98938e3b3a412be2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054275

```text
(config)# default do-exec clear ip dhcp limit lease <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 8 `；EOL ` RVA 0x33DE5590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2498161afb0903f2](../../evidence/conditions-sets-014.md#c-2498161afb0903f2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054138

```text
(config)# default do-exec clear ip dhcp server odap-statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 10 `；EOL ` RVA 0x33DE3E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054171

```text
(config)# default do-exec clear ip dhcp server statistics <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 4 `；EOL ` RVA 0x33DE3918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b7107639c9a89805](../../evidence/conditions-sets-071.md#c-b7107639c9a89805) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057867

```text
(config)# default do-exec clear ip dhcp snooping binding <address> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 1 `；EOL ` RVA 0x35E81B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Clear address specific bindings。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [参数 P-24a6453abfb0d28a](../../evidence/parameters-sets-003.md#p-24a6453abfb0d28a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059332

```text
(config)# default do-exec clear ip dhcp snooping binding bridge-domain <string> <cr>
```

Handler ` RVA 0x15FA9260 `；selector ` 3 `；EOL ` RVA 0x35E821D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DHCP Snooping bd range, example : 1,3-5,7,9-11。

[条件 C-75fcf496af8704d2](../../evidence/conditions-sets-046.md#c-75fcf496af8704d2) · [参数 P-cce908d8140214c8](../../evidence/parameters-sets-016.md#p-cce908d8140214c8) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057862

```text
(config)# default do-exec clear ip dhcp snooping database statistics <cr>
```

Handler ` RVA 0x15FAA320 `；selector ` 0 `；EOL ` RVA 0x35E825B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054165

```text
(config)# default do-exec clear ip dhcp snooping statistics <cr>
```

Handler ` RVA 0x15FA9590 `；selector ` 0 `；EOL ` RVA 0x35E82840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88701873d8528f78](../../evidence/conditions-sets-053.md#c-88701873d8528f78) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054247

```text
(config)# default do-exec clear ip dhcp subnet <address> <cr>
```

Handler ` RVA 0xD29A1F0 `；selector ` 5 `；EOL ` RVA 0x33DE51D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Specify an address in the subnet to clear。

[条件 C-8127a4d438972794](../../evidence/conditions-sets-050.md#c-8127a4d438972794) · [参数 P-604821058269eb93](../../evidence/parameters-sets-008.md#p-604821058269eb93) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053406

```text
(config)# default do-exec clear ip dns servers <address> <cr>
```

Handler ` RVA 0xD133B70 `；selector ` 0 `；EOL ` RVA 0x33D9B6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPV4 Server Address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-f3837ab8cf79a70e](../../evidence/parameters-sets-018.md#p-f3837ab8cf79a70e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-035827

```text
(config)# default do-exec clear ip drp <cr>
```

Handler ` RVA 0xF4F0BA0 `；selector ` 0 `；EOL ` RVA 0x3467ADA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046403

```text
(config)# default do-exec clear ip eigrp events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x346D9C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [状态效果 S-1cf882bffaee6845](../../evidence/state_effects-sets-007.md#s-1cf882bffaee6845)

### path-046340

```text
(config)# default do-exec clear ip eigrp logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x346D99B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [状态效果 S-1cf882bffaee6845](../../evidence/state_effects-sets-007.md#s-1cf882bffaee6845)

### path-046471

```text
(config)# default do-exec clear ip eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x346D92A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-753308e3327070a9](../../evidence/conditions-sets-045.md#c-753308e3327070a9) · [状态效果 S-1cf882bffaee6845](../../evidence/state_effects-sets-007.md#s-1cf882bffaee6845)

### path-053758

```text
(config)# default do-exec clear ip eigrp topology <address> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 68 `；EOL ` RVA 0x346D96E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Network to clear from topology。

[条件 C-3d6bbdb71e02be33](../../evidence/conditions-sets-024.md#c-3d6bbdb71e02be33) · [参数 P-c5c28ea144019d4d](../../evidence/parameters-sets-015.md#p-c5c28ea144019d4d) · [状态效果 S-1cf882bffaee6845](../../evidence/state_effects-sets-007.md#s-1cf882bffaee6845)

### path-057420

```text
(config)# default do-exec clear ip http client cache all <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 1 `；EOL ` RVA 0x33DB0D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059149

```text
(config)# default do-exec clear ip http client cache session <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 2 `；EOL ` RVA 0x33DB0AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` session name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-ba614fcf6b2daaef](../../evidence/parameters-sets-014.md#p-ba614fcf6b2daaef) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059140

```text
(config)# default do-exec clear ip http client cache url <string> <cr>
```

Handler ` RVA 0xD1D2220 `；selector ` 3 `；EOL ` RVA 0x33DB07D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` url to clear。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-04caf09ff1ffb9ea](../../evidence/parameters-sets-001.md#p-04caf09ff1ffb9ea) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053476

```text
(config)# default do-exec clear ip http client cookie <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 4 `；EOL ` RVA 0x33DB1618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059160

```text
(config)# default do-exec clear ip http client cookie domain <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 6 `；EOL ` RVA 0x33DB1370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client domain/host name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-7ddae15590050dbb](../../evidence/parameters-sets-010.md#p-7ddae15590050dbb) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059172

```text
(config)# default do-exec clear ip http client cookie name <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 7 `；EOL ` RVA 0x33DB1658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client cookie name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-70e3f6d6b140bc15](../../evidence/parameters-sets-009.md#p-70e3f6d6b140bc15) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059146

```text
(config)# default do-exec clear ip http client cookie session <string> <cr>
```

Handler ` RVA 0xD1D23A0 `；selector ` 5 `；EOL ` RVA 0x33DB1088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client session name。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-7dc08f985880508a](../../evidence/parameters-sets-010.md#p-7dc08f985880508a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045043

```text
(config)# default do-exec clear ip icmp rate-limit <cr>
```

Handler ` RVA 0xCFE5700 `；selector ` 0 `；EOL ` RVA 0x33D2B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d149a0ed9e1c68ff](../../evidence/conditions-sets-081.md#c-d149a0ed9e1c68ff) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046239

```text
(config)# default do-exec clear ip igmp group <cr>
```

Handler ` RVA 0xF6B26D0 `；selector ` 0 `；EOL ` RVA 0x34746DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5b415668ee6ea98d](../../evidence/conditions-sets-036.md#c-5b415668ee6ea98d) · [状态效果 S-849a104ea1b5c8f3](../../evidence/state_effects-sets-028.md#s-849a104ea1b5c8f3)

### path-046563

```text
(config)# default do-exec clear ip mfib counters <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355B7700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f808427ebefa84e5](../../evidence/conditions-sets-096.md#c-f808427ebefa84e5) · [状态效果 S-ec6c2beb7cc987bc](../../evidence/state_effects-sets-050.md#s-ec6c2beb7cc987bc)

### path-046153

```text
(config)# default do-exec clear ip mrm status-report <cr>
```

Handler ` RVA 0xF672250 `；selector ` 0 `；EOL ` RVA 0x3471F308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046163

```text
(config)# default do-exec clear ip mroute <address> <cr>
```

Handler ` RVA 0xF74EC90 `；selector ` 0 `；EOL ` RVA 0x347468B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP name or group address。

[条件 C-be25b0dc514ae992](../../evidence/conditions-sets-073.md#c-be25b0dc514ae992) · [参数 P-5526640d1cbfc478](../../evidence/parameters-sets-007.md#p-5526640d1cbfc478) · [状态效果 S-bfc9eafae8955fbd](../../evidence/state_effects-sets-041.md#s-bfc9eafae8955fbd)

### path-053233

```text
(config)# default do-exec clear ip msdp peer <address> <cr>
```

Handler ` RVA 0xF78ED70 `；selector ` 0 `；EOL ` RVA 0x34741B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Peer name or address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-9f44f2d1408a3f5d](../../evidence/parameters-sets-012.md#p-9f44f2d1408a3f5d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045873

```text
(config)# default do-exec clear ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78EA70 `；selector ` 0 `；EOL ` RVA 0x34741E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045925

```text
(config)# default do-exec clear ip msdp statistics <cr>
```

Handler ` RVA 0xF78EB10 `；selector ` 0 `；EOL ` RVA 0x34742130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046026

```text
(config)# default do-exec clear ip multicast limit <cr>
```

Handler ` RVA 0xF777FE0 `；selector ` 0 `；EOL ` RVA 0x34746048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d5aff361b478776d](../../evidence/conditions-sets-082.md#c-d5aff361b478776d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053525

```text
(config)# default do-exec clear ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD4712F0 `；selector ` 0 `；EOL ` RVA 0x33E525D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045978

```text
(config)# default do-exec clear ip multicast rsvp <cr>
```

Handler ` RVA 0xF6F1770 `；selector ` 0 `；EOL ` RVA 0x34745CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e532f6e964361ea1](../../evidence/conditions-sets-088.md#c-e532f6e964361ea1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059778

```text
(config)# default do-exec clear ip multicast snooping limit vlan <number:1..4095> statistics <cr>
```

Handler ` RVA 0xC3568D0 `；selector ` 64 `；EOL ` RVA 0x33A5F240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [参数 P-85cbffd05ab530a5](../../evidence/parameters-sets-010.md#p-85cbffd05ab530a5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046179

```text
(config)# default do-exec clear ip nat statistics <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 1 `；EOL ` RVA 0x347DD7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046520

```text
(config)# default do-exec clear ip nat translation <cr>
```

Handler ` RVA 0xFA0A1A0 `；selector ` 0 `；EOL ` RVA 0x347DCB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1cc54701c6ed739](../../evidence/conditions-sets-062.md#c-a1cc54701c6ed739) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036573

```text
(config)# default do-exec clear ip nbar <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 2 `；EOL ` RVA 0x3527C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce4cc5e5f2365570](../../evidence/conditions-sets-079.md#c-ce4cc5e5f2365570) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-059163

```text
(config)# default do-exec clear ip nbar classification auto-learn top-hosts restart <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 14 `；EOL ` RVA 0x3527B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a8d94fa5b85f8d8a](../../evidence/conditions-sets-065.md#c-a8d94fa5b85f8d8a) · [状态效果 S-cb4b3a374ada9cdd](../../evidence/state_effects-sets-043.md#s-cb4b3a374ada9cdd)

### path-059145

```text
(config)# default do-exec clear ip nbar classification auto-learn top-hosts statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 13 `；EOL ` RVA 0x3527B5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a8d94fa5b85f8d8a](../../evidence/conditions-sets-065.md#c-a8d94fa5b85f8d8a) · [状态效果 S-cb4b3a374ada9cdd](../../evidence/state_effects-sets-043.md#s-cb4b3a374ada9cdd)

### path-057411

```text
(config)# default do-exec clear ip nbar classification cache sync <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 12 `；EOL ` RVA 0x3527BBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-059169

```text
(config)# default do-exec clear ip nbar classification dns learning cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 47 `；EOL ` RVA 0x3527BF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-059180

```text
(config)# default do-exec clear ip nbar classification dns learning statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 49 `；EOL ` RVA 0x3527C1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-053462

```text
(config)# default do-exec clear ip nbar classification socket-cache <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 48 `；EOL ` RVA 0x3527C458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-045932

```text
(config)# default do-exec clear ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 34 `；EOL ` RVA 0x3527B048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd1aff9592498208](../../evidence/conditions-sets-079.md#c-cd1aff9592498208) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-045963

```text
(config)# default do-exec clear ip nbar statistics <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 7 `；EOL ` RVA 0x3527C748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-71e0524c2117ffd7](../../evidence/conditions-sets-044.md#c-71e0524c2117ffd7) · [状态效果 S-8263d2f41f62e67b](../../evidence/state_effects-sets-028.md#s-8263d2f41f62e67b)

### path-037138

```text
(config)# default do-exec clear ip nhrp <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 0 `；EOL ` RVA 0x347F2628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046509

```text
(config)# default do-exec clear ip nhrp counters <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 1 `；EOL ` RVA 0x347F29F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27b8c2ad606f4640](../../evidence/conditions-sets-016.md#c-27b8c2ad606f4640) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046413

```text
(config)# default do-exec clear ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE760 `；selector ` 0 `；EOL ` RVA 0x34BF9228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-63cc602f242942a2](../../evidence/state_effects-sets-021.md#s-63cc602f242942a2)

### path-046747

```text
(config)# default do-exec clear ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4540 `；selector ` 2 `；EOL ` RVA 0x347F2F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-72d46b46a297f481](../../evidence/conditions-sets-044.md#c-72d46b46a297f481) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046359

```text
(config)# default do-exec clear ip ospf counters <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 4 `；EOL ` RVA 0x348934D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046404

```text
(config)# default do-exec clear ip ospf events <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 6 `；EOL ` RVA 0x34893FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046227

```text
(config)# default do-exec clear ip ospf force-spf <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 0 `；EOL ` RVA 0x34892C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059233

```text
(config)# default do-exec clear ip ospf lsa router <address> self <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 7 `；EOL ` RVA 0x34893A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF LSID in IP address format。

[条件 C-a52f305b1c8c11f0](../../evidence/conditions-sets-064.md#c-a52f305b1c8c11f0) · [参数 P-4bb4f15a3e4f951b](../../evidence/parameters-sets-006.md#p-4bb4f15a3e4f951b) · [状态效果 S-f24edec4e596ca3e](../../evidence/state_effects-sets-051.md#s-f24edec4e596ca3e)

### path-053569

```text
(config)# default do-exec clear ip ospf nsr statistics <cr>
```

Handler ` RVA 0xDACCB50 `；selector ` 20 `；EOL ` RVA 0x33FC88B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-0684a14882edbdf9](../../evidence/state_effects-sets-002.md#s-0684a14882edbdf9)

### path-046143

```text
(config)# default do-exec clear ip ospf process <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 3 `；EOL ` RVA 0x34892700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046087

```text
(config)# default do-exec clear ip ospf redistribution <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 2 `；EOL ` RVA 0x34892458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046192

```text
(config)# default do-exec clear ip ospf rib <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 1 `；EOL ` RVA 0x348929A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046421

```text
(config)# default do-exec clear ip ospf traffic <cr>
```

Handler ` RVA 0xFCD4210 `；selector ` 5 `；EOL ` RVA 0x34893080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9481ef008e1de97f](../../evidence/conditions-sets-057.md#c-9481ef008e1de97f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045981

```text
(config)# default do-exec clear ip pim df <cr>
```

Handler ` RVA 0xF7CB460 `；selector ` 0 `；EOL ` RVA 0x34771D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053458

```text
(config)# default do-exec clear ip pim interface count <cr>
```

Handler ` RVA 0xF827030 `；selector ` 0 `；EOL ` RVA 0x34772140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d0cc604d16d7fbbd](../../evidence/conditions-sets-080.md#c-d0cc604d16d7fbbd) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053452

```text
(config)# default do-exec clear ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF8A2050 `；selector ` 0 `；EOL ` RVA 0x347726F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053399

```text
(config)# default do-exec clear ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF8A1FA0 `；selector ` 0 `；EOL ` RVA 0x34772450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045872

```text
(config)# default do-exec clear ip pim rp-mapping <cr>
```

Handler ` RVA 0xF7BE560 `；selector ` 0 `；EOL ` RVA 0x34771918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e51874697090e566](../../evidence/conditions-sets-088.md#c-e51874697090e566) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037130

```text
(config)# default do-exec clear ip prefix-list <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x34283CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-7b4c65669cf93938](../../evidence/state_effects-sets-026.md#s-7b4c65669cf93938)

### path-035370

```text
(config)# default do-exec clear ip redirect <cr>
```

Handler ` RVA 0xCF50BF0 `；selector ` 0 `；EOL ` RVA 0x33D2B468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-40cb41e4acbcc6cc](../../evidence/state_effects-sets-014.md#s-40cb41e4acbcc6cc)

### path-046646

```text
(config)# default do-exec clear ip reflexive-list <string> <cr>
```

Handler ` RVA 0xCEFCA00 `；selector ` 0 `；EOL ` RVA 0x3479AD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Delete a specific reflexive ACL。

[条件 C-94a4629f79b58d64](../../evidence/conditions-sets-057.md#c-94a4629f79b58d64) · [参数 P-afb5c6d87d9e8de3](../../evidence/parameters-sets-013.md#p-afb5c6d87d9e8de3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045829

```text
(config)# default do-exec clear ip route <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 1 `；EOL ` RVA 0x3422DF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination network route to delete。

[条件 C-3ef1add5b3f1b32e](../../evidence/conditions-sets-024.md#c-3ef1add5b3f1b32e) · [参数 P-a606ea51f9247878](../../evidence/parameters-sets-013.md#p-a606ea51f9247878) · [状态效果 S-911efe3d041a3f62](../../evidence/state_effects-sets-031.md#s-911efe3d041a3f62)

### path-053239

```text
(config)# default do-exec clear ip route dhcp <address> <cr>
```

Handler ` RVA 0xE1F84C0 `；selector ` 2 `；EOL ` RVA 0x3422E240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination host route to delete。

[条件 C-3ef1add5b3f1b32e](../../evidence/conditions-sets-024.md#c-3ef1add5b3f1b32e) · [参数 P-f4e189f9e5e93c08](../../evidence/parameters-sets-018.md#p-f4e189f9e5e93c08) · [状态效果 S-381bc86825266c18](../../evidence/state_effects-sets-012.md#s-381bc86825266c18)

### path-057449

```text
(config)# default do-exec clear ip route download <address> <address> <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 1 `；EOL ` RVA 0x3422E620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination network route to delete；` address ` Destination network mask。

[条件 C-3c5166292a75cfac](../../evidence/conditions-sets-023.md#c-3c5166292a75cfac) · [参数 P-405fcd062cfd9eeb](../../evidence/parameters-sets-005.md#p-405fcd062cfd9eeb) · [状态效果 S-419b75a93facbd0a](../../evidence/state_effects-sets-014.md#s-419b75a93facbd0a)

### path-053460

```text
(config)# default do-exec clear ip route download reload <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 2 `；EOL ` RVA 0x3422E8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c5166292a75cfac](../../evidence/conditions-sets-023.md#c-3c5166292a75cfac) · [状态效果 S-381bc86825266c18](../../evidence/state_effects-sets-012.md#s-381bc86825266c18)

### path-046662

```text
(config)# default do-exec clear ip rsvp authentication <cr>
```

Handler ` RVA 0x100741B0 `；selector ` 0 `；EOL ` RVA 0x34A3D340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046397

```text
(config)# default do-exec clear ip rsvp counters <cr>
```

Handler ` RVA 0x100B7230 `；selector ` 0 `；EOL ` RVA 0x34A3B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057719

```text
(config)# default do-exec clear ip rsvp hello bfd lost-cnt <cr>
```

Handler ` RVA 0x10074420 `；selector ` 0 `；EOL ` RVA 0x34A3C3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057752

```text
(config)# default do-exec clear ip rsvp hello bfd nbr-lost <cr>
```

Handler ` RVA 0x100744C0 `；selector ` 0 `；EOL ` RVA 0x34A3C678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057727

```text
(config)# default do-exec clear ip rsvp hello instance counters <cr>
```

Handler ` RVA 0x1006F1F0 `；selector ` 0 `；EOL ` RVA 0x34A3C0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057684

```text
(config)# default do-exec clear ip rsvp hello instance statistics <cr>
```

Handler ` RVA 0x1006F240 `；selector ` 0 `；EOL ` RVA 0x34A3BE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053805

```text
(config)# default do-exec clear ip rsvp hello statistics <cr>
```

Handler ` RVA 0x1006F290 `；selector ` 0 `；EOL ` RVA 0x34A3BB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053940

```text
(config)# default do-exec clear ip rsvp metadata interface <cr>
```

Handler ` RVA 0x10078C10 `；selector ` 0 `；EOL ` RVA 0x34A3D630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-577970e4f2d7b997](../../evidence/conditions-sets-034.md#c-577970e4f2d7b997) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053698

```text
(config)# default do-exec clear ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100B71E0 `；selector ` 0 `；EOL ` RVA 0x34A3AB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-628bdccceb1356de](../../evidence/conditions-sets-038.md#c-628bdccceb1356de) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060049

```text
(config)# default do-exec clear ip rsvp reservation <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F000 `；selector ` 0 `；EOL ` RVA 0x34A3B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [参数 P-bca9d63baab5c636](../../evidence/parameters-sets-014.md#p-bca9d63baab5c636) · [状态效果 S-b6e2f04f63207b6a](../../evidence/state_effects-sets-039.md#s-b6e2f04f63207b6a)

### path-060046

```text
(config)# default do-exec clear ip rsvp sender <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x1006ED80 `；selector ` 0 `；EOL ` RVA 0x34A3AFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [参数 P-6ed41e2ffa47e5cc](../../evidence/parameters-sets-009.md#p-6ed41e2ffa47e5cc) · [状态效果 S-ad8e25b1b6f22b34](../../evidence/state_effects-sets-037.md#s-ad8e25b1b6f22b34)

### path-057683

```text
(config)# default do-exec clear ip rsvp signalling fast-local-repair statistics <cr>
```

Handler ` RVA 0x100710E0 `；selector ` 0 `；EOL ` RVA 0x34A3CA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053905

```text
(config)# default do-exec clear ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x10070F70 `；selector ` 0 `；EOL ` RVA 0x34A3CC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057749

```text
(config)# default do-exec clear ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071080 `；selector ` 0 `；EOL ` RVA 0x34A3CF80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb980b4a4b3feec7](../../evidence/conditions-sets-097.md#c-fb980b4a4b3feec7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045435

```text
(config)# default do-exec clear ip rtp header-compression <cr>
```

Handler ` RVA 0xD194840 `；selector ` 0 `；EOL ` RVA 0x33DAB158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8acdee18c18ec765](../../evidence/conditions-sets-054.md#c-8acdee18c18ec765) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045847

```text
(config)# default do-exec clear ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FD20 `；selector ` 0 `；EOL ` RVA 0x33D0AAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036512

```text
(config)# default do-exec clear ip sdr <cr>
```

Handler ` RVA 0xF87F070 `；selector ` 0 `；EOL ` RVA 0x34745820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4899a50427063fad](../../evidence/conditions-sets-028.md#c-4899a50427063fad) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037333

```text
(config)# default do-exec clear ip subscriber <cr>
```

Handler ` RVA 0x11A39570 `；selector ` 0 `；EOL ` RVA 0x355CE968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-f9a1c2d5502aa9ea](../../evidence/state_effects-sets-053.md#s-f9a1c2d5502aa9ea)

### path-045482

```text
(config)# default do-exec clear ip tcp header-compression <cr>
```

Handler ` RVA 0xD194AE0 `；selector ` 0 `；EOL ` RVA 0x33DABAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e1f32afed43d6d4c](../../evidence/conditions-sets-087.md#c-e1f32afed43d6d4c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-035556

```text
(config)# default do-exec clear ip traffic <cr>
```

Handler ` RVA 0xCECF5C0 `；selector ` 0 `；EOL ` RVA 0x33D2BBF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052774

```text
(config)# default do-exec clear ip traffic topology base <cr>
```

Handler ` RVA 0xCF0EE20 `；selector ` 0 `；EOL ` RVA 0x33D2B7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9af39dcf3099e2c3](../../evidence/state_effects-sets-033.md#s-9af39dcf3099e2c3)

### path-036868

```text
(config)# default do-exec clear ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 3 `；EOL ` RVA 0x34B5AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-035197

```text
(config)# default do-exec clear ipam counts <cr>
```

Handler ` RVA 0xCEA9040 `；selector ` 0 `；EOL ` RVA 0x33D1BBC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-035253

```text
(config)# default do-exec clear ipam queues <cr>
```

Handler ` RVA 0xCEA90F0 `；selector ` 0 `；EOL ` RVA 0x33D1BE68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044154

```text
(config)# default do-exec clear ipc statistics peak <cr>
```

Handler ` RVA 0xD3B9920 `；selector ` 0 `；EOL ` RVA 0x33E272C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-ad2b8fc1bc7b41e0](../../evidence/state_effects-sets-037.md#s-ad2b8fc1bc7b41e0)

### path-044058

```text
(config)# default do-exec clear ipc statistics queue <cr>
```

Handler ` RVA 0xD3B9F70 `；selector ` 0 `；EOL ` RVA 0x33E26F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044163

```text
(config)# default do-exec clear ipc statistics zone <cr>
```

Handler ` RVA 0xD3B9FC0 `；selector ` 0 `；EOL ` RVA 0x33E27570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037166

```text
(config)# default do-exec clear ipv6 access-list <cr>
```

Handler ` RVA 0x1217F700 `；selector ` 0 `；EOL ` RVA 0x357B0A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046921

```text
(config)# default do-exec clear ipv6 cef prefix-statistics <cr>
```

Handler ` RVA 0xB684240 `；selector ` 0 `；EOL ` RVA 0x337D8618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a9b9f48e3754b1f2](../../evidence/conditions-sets-065.md#c-a9b9f48e3754b1f2) · [状态效果 S-d662ead62712e61f](../../evidence/state_effects-sets-045.md#s-d662ead62712e61f)

### path-054036

```text
(config)# default do-exec clear ipv6 dhcp binding <address> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 0 `；EOL ` RVA 0x357C7BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Client IPv6 address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-5cdfea9b76c9ff77](../../evidence/parameters-sets-007.md#p-5cdfea9b76c9ff77) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054094

```text
(config)# default do-exec clear ipv6 dhcp conflict <address> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 2 `；EOL ` RVA 0x357C85C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-88dca45322fc40b3](../../evidence/parameters-sets-011.md#p-88dca45322fc40b3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057806

```text
(config)# default do-exec clear ipv6 dhcp relay binding <address> <cr>
```

Handler ` RVA 0x121B39B0 `；selector ` 1 `；EOL ` RVA 0x357C37A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-2ed5ae9a7eacd364](../../evidence/parameters-sets-004.md#p-2ed5ae9a7eacd364) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054095

```text
(config)# default do-exec clear ipv6 dhcp route <address> <cr>
```

Handler ` RVA 0x121D09B0 `；selector ` 3 `；EOL ` RVA 0x357C81E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-b71caea3e07a6894](../../evidence/conditions-sets-071.md#c-b71caea3e07a6894) · [参数 P-ed6dcf58eee13906](../../evidence/parameters-sets-018.md#p-ed6dcf58eee13906) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046452

```text
(config)# default do-exec clear ipv6 eigrp events <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 71 `；EOL ` RVA 0x354657B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-22f3a07d866d2198](../../evidence/state_effects-sets-008.md#s-22f3a07d866d2198)

### path-046399

```text
(config)# default do-exec clear ipv6 eigrp logging <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 72 `；EOL ` RVA 0x35465510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-22f3a07d866d2198](../../evidence/state_effects-sets-008.md#s-22f3a07d866d2198)

### path-046568

```text
(config)# default do-exec clear ipv6 eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 67 `；EOL ` RVA 0x35465198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47d7b69e2f177ee8](../../evidence/conditions-sets-028.md#c-47d7b69e2f177ee8) · [状态效果 S-22f3a07d866d2198](../../evidence/state_effects-sets-008.md#s-22f3a07d866d2198)

### path-036154

```text
(config)# default do-exec clear ipv6 errors-internal <cr>
```

Handler ` RVA 0x12304FE0 `；selector ` 0 `；EOL ` RVA 0x357E36C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4454cce5585dae44](../../evidence/conditions-sets-027.md#c-4454cce5585dae44) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046307

```text
(config)# default do-exec clear ipv6 mfib counters <cr>
```

Handler ` RVA 0x1197D5A0 `；selector ` 0 `；EOL ` RVA 0x355BC008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a9cce6ac4cd81e3](../../evidence/conditions-sets-010.md#c-1a9cce6ac4cd81e3) · [状态效果 S-0f2075c4f87dd897](../../evidence/state_effects-sets-004.md#s-0f2075c4f87dd897)

### path-053736

```text
(config)# default do-exec clear ipv6 mld all-vrfs traffic <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 2 `；EOL ` RVA 0x3554C180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34b717c56dbdfb70](../../evidence/conditions-sets-020.md#c-34b717c56dbdfb70) · [状态效果 S-ff1da3febe6bb495](../../evidence/state_effects-sets-054.md#s-ff1da3febe6bb495)

### path-046467

```text
(config)# default do-exec clear ipv6 mld counters <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 3 `；EOL ` RVA 0x3554B900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2b6b77bb1f2c1093](../../evidence/conditions-sets-017.md#c-2b6b77bb1f2c1093) · [状态效果 S-ff1da3febe6bb495](../../evidence/state_effects-sets-054.md#s-ff1da3febe6bb495)

### path-046618

```text
(config)# default do-exec clear ipv6 mld group <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 4 `；EOL ` RVA 0x3554BD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-76b249d987d749b4](../../evidence/conditions-sets-046.md#c-76b249d987d749b4) · [状态效果 S-ff1da3febe6bb495](../../evidence/state_effects-sets-054.md#s-ff1da3febe6bb495)

### path-046291

```text
(config)# default do-exec clear ipv6 mld traffic <cr>
```

Handler ` RVA 0x115D9690 `；selector ` 1 `；EOL ` RVA 0x3554B570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a522572a98f7b12a](../../evidence/conditions-sets-064.md#c-a522572a98f7b12a) · [状态效果 S-ff1da3febe6bb495](../../evidence/state_effects-sets-054.md#s-ff1da3febe6bb495)

### path-036366

```text
(config)# default do-exec clear ipv6 mtu <cr>
```

Handler ` RVA 0x123069A0 `；selector ` 0 `；EOL ` RVA 0x357E5B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054080

```text
(config)# default do-exec clear ipv6 multicast aaa authorization <cr>
```

Handler ` RVA 0xC49F810 `；selector ` 1001 `；EOL ` RVA 0x35534C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a73dfb09fd12da18](../../evidence/conditions-sets-065.md#c-a73dfb09fd12da18) · [状态效果 S-7f016747ab4641f4](../../evidence/state_effects-sets-027.md#s-7f016747ab4641f4)

### path-059777

```text
(config)# default do-exec clear ipv6 multicast snooping limit vlan <number:1..4095> statistics <cr>
```

Handler ` RVA 0xC3568D0 `；selector ` 65 `；EOL ` RVA 0x33A5F660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-5b0920e26311c92a](../../evidence/parameters-sets-007.md#p-5b0920e26311c92a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046101

```text
(config)# default do-exec clear ipv6 nd destination <cr>
```

Handler ` RVA 0x1231A7C0 `；selector ` 0 `；EOL ` RVA 0x358056A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053507

```text
(config)# default do-exec clear ipv6 nd on-link prefix <cr>
```

Handler ` RVA 0x1231A3B0 `；selector ` 0 `；EOL ` RVA 0x35805358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046156

```text
(config)# default do-exec clear ipv6 nd router <cr>
```

Handler ` RVA 0x1231A8D0 `；selector ` 0 `；EOL ` RVA 0x358059B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036845

```text
(config)# default do-exec clear ipv6 neighbors <cr>
```

Handler ` RVA 0x12312B50 `；selector ` 0 `；EOL ` RVA 0x35802BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4d41c4b0ffea9641](../../evidence/conditions-sets-030.md#c-4d41c4b0ffea9641) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057591

```text
(config)# default do-exec clear ipv6 neighbors binding policy <string> <cr>
```

Handler ` RVA 0x136806D0 `；selector ` 1020 `；EOL ` RVA 0x35BF63A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Snooping Policy name to be cleared。

[条件 C-1909215f3ec7ca4b](../../evidence/conditions-sets-010.md#c-1909215f3ec7ca4b) · [参数 P-44ff88cb184b8e62](../../evidence/parameters-sets-006.md#p-44ff88cb184b8e62) · [状态效果 S-8f3849d5c8c279a1](../../evidence/state_effects-sets-030.md#s-8f3849d5c8c279a1)

### path-053484

```text
(config)# default do-exec clear ipv6 neighbors ha statistics <cr>
```

Handler ` RVA 0x12312A70 `；selector ` 0 `；EOL ` RVA 0x35803088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-88857cab8ffcc69c](../../evidence/state_effects-sets-029.md#s-88857cab8ffcc69c)

### path-037218

```text
(config)# default do-exec clear ipv6 nhrp <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 0 `；EOL ` RVA 0x35575280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046610

```text
(config)# default do-exec clear ipv6 nhrp counters <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 1 `；EOL ` RVA 0x35575678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046658

```text
(config)# default do-exec clear ipv6 nhrp shortcut <cr>
```

Handler ` RVA 0x1186E410 `；selector ` 0 `；EOL ` RVA 0x35575A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b222251f03aeb996](../../evidence/conditions-sets-069.md#c-b222251f03aeb996) · [状态效果 S-e2f9b991bbc97487](../../evidence/state_effects-sets-048.md#s-e2f9b991bbc97487)

### path-046517

```text
(config)# default do-exec clear ipv6 nhrp stats <cr>
```

Handler ` RVA 0x1186E480 `；selector ` 2 `；EOL ` RVA 0x35574D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-82b4309de47f4ee2](../../evidence/conditions-sets-051.md#c-82b4309de47f4ee2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053770

```text
(config)# default do-exec clear ipv6 pim all-vrfs traffic <cr>
```

Handler ` RVA 0x11725630 `；selector ` 3 `；EOL ` RVA 0x35563230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61aa384bdfdaf4b0](../../evidence/conditions-sets-038.md#c-61aa384bdfdaf4b0) · [状态效果 S-6cdb8b51c6cd75f9](../../evidence/state_effects-sets-023.md#s-6cdb8b51c6cd75f9)

### path-046565

```text
(config)# default do-exec clear ipv6 pim limit <cr>
```

Handler ` RVA 0x11725630 `；selector ` 4 `；EOL ` RVA 0x355626C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c792dc2853bbd0dc](../../evidence/conditions-sets-077.md#c-c792dc2853bbd0dc) · [状态效果 S-6cdb8b51c6cd75f9](../../evidence/state_effects-sets-023.md#s-6cdb8b51c6cd75f9)

### path-053956

```text
(config)# default do-exec clear ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x11725630 `；selector ` 6 `；EOL ` RVA 0x35562F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-6cdb8b51c6cd75f9](../../evidence/state_effects-sets-023.md#s-6cdb8b51c6cd75f9)

### path-053892

```text
(config)# default do-exec clear ipv6 pim pfp-sa originator <cr>
```

Handler ` RVA 0x11725630 `；selector ` 5 `；EOL ` RVA 0x35562C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-6cdb8b51c6cd75f9](../../evidence/state_effects-sets-023.md#s-6cdb8b51c6cd75f9)

### path-046396

```text
(config)# default do-exec clear ipv6 pim reset <cr>
```

Handler ` RVA 0x11725630 `；selector ` 1 `；EOL ` RVA 0x355622F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-2b032db3a1cf99f4](../../evidence/state_effects-sets-010.md#s-2b032db3a1cf99f4)

### path-046500

```text
(config)# default do-exec clear ipv6 pim traffic <cr>
```

Handler ` RVA 0x11725630 `；selector ` 2 `；EOL ` RVA 0x35562988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c123bc221e8796d](../../evidence/conditions-sets-023.md#c-3c123bc221e8796d) · [状态效果 S-6cdb8b51c6cd75f9](../../evidence/state_effects-sets-023.md#s-6cdb8b51c6cd75f9)

### path-037173

```text
(config)# default do-exec clear ipv6 prefix-list <cr>
```

Handler ` RVA 0xE21FCB0 `；selector ` 0 `；EOL ` RVA 0x3557FB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-eced2a81c16fc1aa](../../evidence/state_effects-sets-050.md#s-eced2a81c16fc1aa)

### path-036993

```text
(config)# default do-exec clear ipv6 rip <cr>
```

Handler ` RVA 0x118A6380 `；selector ` 0 `；EOL ` RVA 0x3557C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7a8b1a79f7ff80b2](../../evidence/conditions-sets-048.md#c-7a8b1a79f7ff80b2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046008

```text
(config)# default do-exec clear ipv6 route <address> <cr>
```

Handler ` RVA 0x123075A0 `；selector ` 0 `；EOL ` RVA 0x357EBFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 address。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [参数 P-80c04b2fec363bf8](../../evidence/parameters-sets-010.md#p-80c04b2fec363bf8) · [状态效果 S-0b01080dbb9779ed](../../evidence/state_effects-sets-003.md#s-0b01080dbb9779ed)

### path-046735

```text
(config)# default do-exec clear ipv6 snooping counters <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1023 `；EOL ` RVA 0x35BF5768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a95c6c5f538488c4](../../evidence/conditions-sets-065.md#c-a95c6c5f538488c4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046726

```text
(config)# default do-exec clear ipv6 snooping events <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1021 `；EOL ` RVA 0x35BF5AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a95c6c5f538488c4](../../evidence/conditions-sets-065.md#c-a95c6c5f538488c4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046775

```text
(config)# default do-exec clear ipv6 snooping messages <cr>
```

Handler ` RVA 0x13686600 `；selector ` 1022 `；EOL ` RVA 0x35BF5D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a95c6c5f538488c4](../../evidence/conditions-sets-065.md#c-a95c6c5f538488c4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037200

```text
(config)# default do-exec clear ipv6 spd <cr>
```

Handler ` RVA 0x12328050 `；selector ` 0 `；EOL ` RVA 0x35810460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036613

```text
(config)# default do-exec clear ipv6 traffic <cr>
```

Handler ` RVA 0x1231FC30 `；selector ` 0 `；EOL ` RVA 0x3580BA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046065

```text
(config)# default do-exec clear ipv6 traffic interface <cr>
```

Handler ` RVA 0x1231FC30 `；selector ` 1 `；EOL ` RVA 0x3580BAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dde915198ac38d0d](../../evidence/conditions-sets-085.md#c-dde915198ac38d0d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037673

```text
(config)# default do-exec clear isis lsp-fast-flooding <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x34B6ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-218458ab656157cb](../../evidence/state_effects-sets-008.md#s-218458ab656157cb)

### path-037561

```text
(config)# default do-exec clear isis lspfull <cr>
```

Handler ` RVA 0xFD360F0 `；selector ` 0 `；EOL ` RVA 0x34B6A818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-a85a7f82e198466e](../../evidence/state_effects-sets-036.md#s-a85a7f82e198466e)

### path-034989

```text
(config)# default do-exec clear kerberos creds <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 6 `；EOL ` RVA 0x33A6B2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044722

```text
(config)# default do-exec clear l2fib statistics all <cr>
```

Handler ` RVA 0xC7C4460 `；selector ` 0 `；EOL ` RVA 0x33AF8A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039652

```text
(config)# default do-exec clear l2protocol-forward counters <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 30 `；EOL ` RVA 0x35E8F288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dbb01e28bf8488ae](../../evidence/conditions-sets-085.md#c-dbb01e28bf8488ae) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039592

```text
(config)# default do-exec clear l2protocol-tunnel counters <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 15 `；EOL ` RVA 0x35E8EEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-028407bd9bcef226](../../evidence/conditions-sets-001.md#c-028407bd9bcef226) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053243

```text
(config)# default do-exec clear l2rib counters client producers <cr>
```

Handler ` RVA 0x125685C0 `；selector ` 0 `；EOL ` RVA 0x358B4CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fd9dbe61bf3884a](../../evidence/conditions-sets-050.md#c-7fd9dbe61bf3884a) · [状态效果 S-908930fed8104f81](../../evidence/state_effects-sets-031.md#s-908930fed8104f81)

### path-053302

```text
(config)# default do-exec clear l2rib test <string> msg-buffer <cr>
```

Handler ` RVA 0x125CDA60 `；selector ` 0 `；EOL ` RVA 0x358BF500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client name。

[条件 C-5e015be4c4cf5293](../../evidence/conditions-sets-037.md#c-5e015be4c4cf5293) · [参数 P-6491247b4d38c173](../../evidence/parameters-sets-008.md#p-6491247b4d38c173) · [状态效果 S-46e4e7be5e649c00](../../evidence/state_effects-sets-016.md#s-46e4e7be5e649c00)

### path-039678

```text
(config)# default do-exec clear lacp counters <cr>
```

Handler ` RVA 0xC8D3130 `；selector ` 0 `；EOL ` RVA 0x33B13D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047377

```text
(config)# default do-exec clear ldap server <string> <cr>
```

Handler ` RVA 0x11ABB2B0 `；selector ` 21 `；EOL ` RVA 0x3560CEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Server name。

[条件 C-b439acb4a73e550d](../../evidence/conditions-sets-070.md#c-b439acb4a73e550d) · [参数 P-4ad9af8e953ad328](../../evidence/parameters-sets-006.md#p-4ad9af8e953ad328) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034261

```text
(config)# default do-exec clear line async-queue <cr>
```

Handler ` RVA 0xCCFAD80 `；selector ` 0 `；EOL ` RVA 0x33C680A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-3ef2e69f03472daa](../../evidence/state_effects-sets-014.md#s-3ef2e69f03472daa)

### path-036580

```text
(config)# default do-exec clear lldp counters <cr>
```

Handler ` RVA 0x158A1C40 `；selector ` 0 `；EOL ` RVA 0x35D9E640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036633

```text
(config)# default do-exec clear lldp table <cr>
```

Handler ` RVA 0x158A1DB0 `；selector ` 0 `；EOL ` RVA 0x35D9E8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-028115

```text
(config)# default do-exec clear logging <cr>
```

Handler ` RVA 0xE073AF0 `；selector ` 0 `；EOL ` RVA 0x34191218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034154

```text
(config)# default do-exec clear logging persistent <cr>
```

Handler ` RVA 0xE06AAF0 `；selector ` 0 `；EOL ` RVA 0x34191280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034111

```text
(config)# default do-exec clear logging xml <cr>
```

Handler ` RVA 0xE073A20 `；selector ` 0 `；EOL ` RVA 0x34190F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048820

```text
(config)# default do-exec clear mac address-table dynamic <cr>
```

Handler ` RVA 0x15E779F0 `；selector ` 7 `；EOL ` RVA 0x35E52FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036781

```text
(config)# default do-exec clear mdns-sd query-db <cr>
```

Handler ` RVA 0x142A3750 `；selector ` 0 `；EOL ` RVA 0x35D0FFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-07a7cff2fe96286d](../../evidence/conditions-sets-003.md#c-07a7cff2fe96286d) · [状态效果 S-410a47cc58c537a5](../../evidence/state_effects-sets-014.md#s-410a47cc58c537a5)

### path-038532

```text
(config)# default do-exec clear memory events <cr>
```

Handler ` RVA 0xE0914B0 `；selector ` 0 `；EOL ` RVA 0x341E5930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84dc18100e4fe16f](../../evidence/conditions-sets-051.md#c-84dc18100e4fe16f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038434

```text
(config)# default do-exec clear memory low-water-mark <cr>
```

Handler ` RVA 0xE0403F0 `；selector ` 0 `；EOL ` RVA 0x341E5648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037825

```text
(config)# default do-exec clear mfib linecard <cr>
```

Handler ` RVA 0x11667DB0 `；selector ` 0 `；EOL ` RVA 0x35524F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dbcfe4717b43cd3b](../../evidence/conditions-sets-085.md#c-dbcfe4717b43cd3b) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037598

```text
(config)# default do-exec clear mfib table <cr>
```

Handler ` RVA 0x118FAD20 `；selector ` 0 `；EOL ` RVA 0x355A6B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88896570ce88308c](../../evidence/conditions-sets-053.md#c-88896570ce88308c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039724

```text
(config)# default do-exec clear mka all <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 1 `；EOL ` RVA 0x35EB59A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039979

```text
(config)# default do-exec clear mka sessions <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 2 `；EOL ` RVA 0x35EAFDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-040031

```text
(config)# default do-exec clear mka statistics <cr>
```

Handler ` RVA 0x160776D0 `；selector ` 7 `；EOL ` RVA 0x35EB02C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046739

```text
(config)# default do-exec clear mlrib layer2 statistics <cr>
```

Handler ` RVA 0xC88D760 `；selector ` 0 `；EOL ` RVA 0x33B09E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb46cf23a65ec1af](../../evidence/conditions-sets-097.md#c-fb46cf23a65ec1af) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037170

```text
(config)# default do-exec clear mvr counters <cr>
```

Handler ` RVA 0xC3B5C20 `；selector ` 0 `；EOL ` RVA 0x33A64008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045088

```text
(config)# default do-exec clear nat64 ha statistics <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 1 `；EOL ` RVA 0x33E928B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5b9a28e1fef1b188](../../evidence/conditions-sets-036.md#c-5b9a28e1fef1b188) · [状态效果 S-8697abf920cf98b4](../../evidence/state_effects-sets-029.md#s-8697abf920cf98b4)

### path-052870

```text
(config)# default do-exec clear nat64 map-e rule running <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 3 `；EOL ` RVA 0x33E93370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49d82582f10f1ef6](../../evidence/conditions-sets-029.md#c-49d82582f10f1ef6) · [状态效果 S-47e564249d9ecbdc](../../evidence/state_effects-sets-016.md#s-47e564249d9ecbdc)

### path-035848

```text
(config)# default do-exec clear nat64 statistics <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 0 `；EOL ` RVA 0x33E92028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63556c9dc475bf87](../../evidence/conditions-sets-038.md#c-63556c9dc475bf87) · [状态效果 S-f8f90c47cf63d1c3](../../evidence/state_effects-sets-053.md#s-f8f90c47cf63d1c3)

### path-045187

```text
(config)# default do-exec clear nat64 translations all <cr>
```

Handler ` RVA 0xD58DBC0 `；selector ` 2 `；EOL ` RVA 0x33E92C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1440cf250c18609a](../../evidence/conditions-sets-008.md#c-1440cf250c18609a) · [状态效果 S-f9f49daf0bf4ab8b](../../evidence/state_effects-sets-053.md#s-f9f49daf0bf4ab8b)

### path-035788

```text
(config)# default do-exec clear nat66 statistics <cr>
```

Handler ` RVA 0xD612DA0 `；selector ` 0 `；EOL ` RVA 0x33EAD460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c04533ad125be8a7](../../evidence/conditions-sets-074.md#c-c04533ad125be8a7) · [状态效果 S-b053658021c0d5a9](../../evidence/state_effects-sets-037.md#s-b053658021c0d5a9)

### path-039328

```text
(config)# default do-exec clear ncia circuits <cr>
```

Handler ` RVA 0x11B1D2B0 `；selector ` 0 `；EOL ` RVA 0x3562BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-3fe127a9afd1ce3d](../../evidence/state_effects-sets-014.md#s-3fe127a9afd1ce3d)

### path-031569

```text
(config)# default do-exec clear netbios-cache <cr>
```

Handler ` RVA 0x114B22B0 `；selector ` 0 `；EOL ` RVA 0x354F4B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038708

```text
(config)# default do-exec clear netconf counters <cr>
```

Handler ` RVA 0xF3C94B0 `；selector ` 0 `；EOL ` RVA 0x3462A498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-038769

```text
(config)# default do-exec clear netconf sessions <cr>
```

Handler ` RVA 0xF3C9770 `；selector ` 0 `；EOL ` RVA 0x3462A740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad55c29aef494ae4](../../evidence/conditions-sets-067.md#c-ad55c29aef494ae4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037510

```text
(config)# default do-exec clear nhrp stats <cr>
```

Handler ` RVA 0x10886440 `；selector ` 2 `；EOL ` RVA 0x34BEA778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-634a40b52d15d14f](../../evidence/conditions-sets-038.md#c-634a40b52d15d14f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)
