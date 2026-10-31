# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-034812

```text
(config)# no do-exec monitor elog calibrate <cr>
```

Handler ` RVA 0xDEADB20 `；selector ` 0 `；EOL ` RVA 0x3408A2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034769

```text
(config)# no do-exec monitor elog free <cr>
```

Handler ` RVA 0xDEAE090 `；selector ` 2 `；EOL ` RVA 0x3408A020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034476

```text
(config)# no do-exec monitor elog off <cr>
```

Handler ` RVA 0xDEAE210 `；selector ` 0 `；EOL ` RVA 0x340883C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034496

```text
(config)# no do-exec monitor elog on <cr>
```

Handler ` RVA 0xDEADF10 `；selector ` 2 `；EOL ` RVA 0x34087F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044230

```text
(config)# no do-exec monitor elog on <number:0..4294967295> <cr>
```

Handler ` RVA 0xDEADF10 `；selector ` 1 `；EOL ` RVA 0x34087ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Set of points to turn on。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-2c31303773e8b92b](../../evidence/parameters-sets-004.md#p-2c31303773e8b92b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056902

```text
(config)# no do-exec monitor elog patch <number:0..4294967295> <number:1..65535> <number:0..65535> <cr>
```

Handler ` RVA 0xDEAD430 `；selector ` 0 `；EOL ` RVA 0x34089258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Virtual address to patch, be careful or no supper!；` unsigned_number ` Event code；` unsigned_number ` Event datum。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-b84cdd056c22c188](../../evidence/parameters-sets-014.md#p-b84cdd056c22c188) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044296

```text
(config)# no do-exec monitor elog save <string> <cr>
```

Handler ` RVA 0xDEAE350 `；selector ` 0 `；EOL ` RVA 0x340886D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` URL to store event data。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-9b947e321167506a](../../evidence/parameters-sets-012.md#p-9b947e321167506a) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034685

```text
(config)# no do-exec monitor elog show-dynamic <cr>
```

Handler ` RVA 0xDEAD090 `；selector ` 0 `；EOL ` RVA 0x34089A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034856

```text
(config)# no do-exec monitor elog stats <cr>
```

Handler ` RVA 0xDEAE670 `；selector ` 0 `；EOL ` RVA 0x3408A570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034560

```text
(config)# no do-exec monitor elog test <cr>
```

Handler ` RVA 0xDEAE280 `；selector ` 0 `；EOL ` RVA 0x34088958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044745

```text
(config)# no do-exec monitor elog trigger clear <cr>
```

Handler ` RVA 0xDEAE900 `；selector ` 0 `；EOL ` RVA 0x3408B5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044661

```text
(config)# no do-exec monitor elog trigger on <cr>
```

Handler ` RVA 0xDEAE7A0 `；selector ` 3 `；EOL ` RVA 0x3408A8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052541

```text
(config)# no do-exec monitor elog trigger on <number:0..4294967295> <cr>
```

Handler ` RVA 0xDEAE7A0 `；selector ` 1 `；EOL ` RVA 0x3408A8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Set of start trigger points。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-7db90e5a9669575b](../../evidence/parameters-sets-010.md#p-7db90e5a9669575b) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052562

```text
(config)# no do-exec monitor elog trigger patch <number:0..4294967295> <cr>
```

Handler ` RVA 0xDEAE820 `；selector ` 0 `；EOL ` RVA 0x3408AE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Virtual address to patch -- be careful!。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-6198d949ef4ae0af](../../evidence/parameters-sets-008.md#p-6198d949ef4ae0af) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044756

```text
(config)# no do-exec monitor elog trigger position <cr>
```

Handler ` RVA 0xDEAE890 `；selector ` 0 `；EOL ` RVA 0x3408B130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052587

```text
(config)# no do-exec monitor elog trigger position <number:0..100> <cr>
```

Handler ` RVA 0xDEAE890 `；selector ` 1 `；EOL ` RVA 0x3408B108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Position of trigger in buffer (percent)。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-6bef0be9314c9617](../../evidence/parameters-sets-009.md#p-6bef0be9314c9617) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044410

```text
(config)# no do-exec monitor elog unpatch <number:0..4294967295> <cr>
```

Handler ` RVA 0xDEAD4B0 `；selector ` 0 `；EOL ` RVA 0x34089548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Virtual address to upatch。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-c21b71e2681f76a6](../../evidence/parameters-sets-015.md#p-c21b71e2681f76a6) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044450

```text
(config)# no do-exec monitor elog unpatch all <cr>
```

Handler ` RVA 0xDEAD760 `；selector ` 0 `；EOL ` RVA 0x340897F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-034977

```text
(config)# no do-exec monitor event-trace hw-api <cr>
```

Handler ` RVA 0xD2D0F80 `；selector ` 0 `；EOL ` RVA 0x33DF9D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1bfe4dbcc4e806cf](../../evidence/conditions-sets-011.md#c-1bfe4dbcc4e806cf) · [状态效果 S-2de68eb322bb5e7b](../../evidence/state_effects-sets-010.md#s-2de68eb322bb5e7b)

### path-052225

```text
(config)# no do-exec monitor processes cpu extended <number:1..2147483647> <cr>
```

Handler ` RVA 0xE087DB0 `；selector ` 0 `；EOL ` RVA 0x341DC5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Process Id。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-1aab3f592ba75926](../../evidence/parameters-sets-003.md#p-1aab3f592ba75926) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044492

```text
(config)# no do-exec monitor tdm-pcm-capture caplog <number:1..268435455> <cr>
```

Handler ` RVA 0x1DC26EE0 `；selector ` 34 `；EOL ` RVA 0x35F6B230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` PCM stream index in hex. Bit0:R_in=0x01 Bit1:S_in=0x02 Bit2:S_out=0x04。

[条件 C-8488c8d2a4732230](../../evidence/conditions-sets-051.md#c-8488c8d2a4732230) · [参数 P-001d649dfb887b01](../../evidence/parameters-sets-001.md#p-001d649dfb887b01) · [状态效果 S-800c84784e0e7d79](../../evidence/state_effects-sets-027.md#s-800c84784e0e7d79)

### path-034644

```text
(config)# no do-exec monitor tdm-pcm-capture disable <cr>
```

Handler ` RVA 0x1DC26EE0 `；selector ` 36 `；EOL ` RVA 0x35F6AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8488c8d2a4732230](../../evidence/conditions-sets-051.md#c-8488c8d2a4732230) · [状态效果 S-e3fb08a05e13535f](../../evidence/state_effects-sets-048.md#s-e3fb08a05e13535f)

### path-044322

```text
(config)# no do-exec monitor xcode-pcm-capture <number:1..10> disable <cr>
```

Handler ` RVA 0x183194E0 `；selector ` 8 `；EOL ` RVA 0x35F6A638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` tag number 1-10。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-67706cb4b859aa9f](../../evidence/parameters-sets-008.md#p-67706cb4b859aa9f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-060129

```text
(config)# no do-exec monitor xcode-pcm-capture <number:1..10> incoming-side call-id <number:0..2147483647> stream <number:1..268435455> duration <number:0..255> <cr>
```

Handler ` RVA 0x183194E0 `；selector ` 9 `；EOL ` RVA 0x35F6AAD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` tag number 1-10；` unsigned_number ` call-id value；` unsigned_number ` PCM stream bitmap in hex. Bit0:R_in=0x01 Bit1:S_in=0x02 Bit2:S_out=0x04；` unsigned_number ` PCM capture duration in sec. 0 is for entire call duration。

[条件 C-54ef6c11f67e9f15](../../evidence/conditions-sets-033.md#c-54ef6c11f67e9f15) · [参数 P-7b368569145f17ba](../../evidence/parameters-sets-010.md#p-7b368569145f17ba) · [状态效果 S-a9815aaafa25b604](../../evidence/state_effects-sets-036.md#s-a9815aaafa25b604)

### path-026976

```text
(config)# no do-exec mrinfo <cr>
```

Handler ` RVA 0xF6F4870 `；selector ` 0 `；EOL ` RVA 0x34744940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c173d79ad6215f39](../../evidence/conditions-sets-075.md#c-c173d79ad6215f39) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026999

```text
(config)# no do-exec mstat <cr>
```

Handler ` RVA 0xF6F4CF0 `；selector ` 0 `；EOL ` RVA 0x34744EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-210673a77948e3fd](../../evidence/conditions-sets-013.md#c-210673a77948e3fd) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026587

```text
(config)# no do-exec mtr <cr>
```

Handler ` RVA 0xE00F6A0 `；selector ` 0 `；EOL ` RVA 0x3415DA98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d7d13b70618a6c58](../../evidence/conditions-sets-083.md#c-d7d13b70618a6c58) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027023

```text
(config)# no do-exec mtrace <cr>
```

Handler ` RVA 0xF6F2690 `；selector ` 0 `；EOL ` RVA 0x34745358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d7a67922fd541da3](../../evidence/conditions-sets-083.md#c-d7a67922fd541da3) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026357

```text
(config)# no do-exec name-connection <cr>
```

Handler ` RVA 0xDE85F40 `；selector ` 0 `；EOL ` RVA 0x341871C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044849

```text
(config)# no do-exec nat64 map-e address register <cr>
```

Handler ` RVA 0xD5909F0 `；selector ` 0 `；EOL ` RVA 0x33E9A5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6c7125523a1cefc7](../../evidence/conditions-sets-042.md#c-6c7125523a1cefc7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-044807

```text
(config)# no do-exec nat64 map-e rule request <cr>
```

Handler ` RVA 0xD590920 `；selector ` 0 `；EOL ` RVA 0x33E9A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6c7125523a1cefc7](../../evidence/conditions-sets-042.md#c-6c7125523a1cefc7) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-059695

```text
(config)# no do-exec nat64 map-t ce address domain <number:1..10000> ipv4 <address> <cr>
```

Handler ` RVA 0xD59AD70 `；selector ` 0 `；EOL ` RVA 0x33E99FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` NAT64 map-t domain number；` address ` IPv4 address。

[条件 C-6c7125523a1cefc7](../../evidence/conditions-sets-042.md#c-6c7125523a1cefc7) · [参数 P-39c6b9846de25865](../../evidence/parameters-sets-005.md#p-39c6b9846de25865) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-030677

```text
(config)# no do-exec ncia start <cr>
```

Handler ` RVA 0x11B1D9F0 `；selector ` 2 `；EOL ` RVA 0x3562A660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-faf16677250df24a](../../evidence/state_effects-sets-053.md#s-faf16677250df24a)

### path-030698

```text
(config)# no do-exec ncia stop <cr>
```

Handler ` RVA 0x11B1D9F0 `；selector ` 1 `；EOL ` RVA 0x3562A928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-faf16677250df24a](../../evidence/state_effects-sets-053.md#s-faf16677250df24a)

### path-046129

```text
(config)# no do-exec onep stop session all <cr>
```

Handler ` RVA 0x13A808C0 `；selector ` 0 `；EOL ` RVA 0x35CB82D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-862920a1b9b74130](../../evidence/state_effects-sets-028.md#s-862920a1b9b74130)

### path-029962

```text
(config)# no do-exec pad <string> <cr>
```

Handler ` RVA 0xFE66070 `；selector ` 0 `；EOL ` RVA 0x349000D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` X121 address or name of a remote system。

[条件 C-ea38452536ef0111](../../evidence/conditions-sets-090.md#c-ea38452536ef0111) · [参数 P-fb40535bd46d1317](../../evidence/parameters-sets-019.md#p-fb40535bd46d1317) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026588

```text
(config)# no do-exec ping <cr>
```

Handler ` RVA 0xE010010 `；selector ` 0 `；EOL ` RVA 0x3415B4A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2097fc6287c05a10](../../evidence/conditions-sets-013.md#c-2097fc6287c05a10) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-050498

```text
(config)# no do-exec pnpa service abort-on-fault <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 67 `；EOL ` RVA 0x33B67E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable or disable abort-on-fault。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-00c44352ff5bf053](../../evidence/parameters-sets-001.md#p-00c44352ff5bf053) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050485

```text
(config)# no do-exec pnpa service act2-sudi <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 69 `；EOL ` RVA 0x33B67B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable or disable act2 sudi during device-auth。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-60cbb82cb3693034](../../evidence/parameters-sets-008.md#p-60cbb82cb3693034) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050469

```text
(config)# no do-exec pnpa service ap-extension <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 68 `；EOL ` RVA 0x33B67858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable or disable ap extension。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-377b4054c7c00a81](../../evidence/parameters-sets-005.md#p-377b4054c7c00a81) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050989

```text
(config)# no do-exec pnpa service backoff-reset <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 0 `；EOL ` RVA 0x33B72BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the profile name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-058304f630d6240e](../../evidence/parameters-sets-001.md#p-058304f630d6240e) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056352

```text
(config)# no do-exec pnpa service certify <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 2 `；EOL ` RVA 0x33B72520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the file URL；` string ` Specify the verify URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-49cc79f37c311cf3](../../evidence/parameters-sets-006.md#p-49cc79f37c311cf3) · [状态效果 S-e6693c2e31ec8e6f](../../evidence/state_effects-sets-049.md#s-e6693c2e31ec8e6f)

### path-056337

```text
(config)# no do-exec pnpa service check-server-id <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 3 `；EOL ` RVA 0x33B72180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the server id (hostname or ip)；` unsigned_number ` Specify the server port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d239d744d63a6987](../../evidence/parameters-sets-016.md#p-d239d744d63a6987) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056327

```text
(config)# no do-exec pnpa service check-ssl-handshake <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 4 `；EOL ` RVA 0x33B71E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the server id (hostname or ip)；` unsigned_number ` Specify the server port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b82d299d4798187f](../../evidence/parameters-sets-014.md#p-b82d299d4798187f) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050458

```text
(config)# no do-exec pnpa service config-control <number:0..3> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 70 `；EOL ` RVA 0x33B67568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` config-control level: 3-strict, 2-all-check, 1-basic-check, 0-none。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-35ffbdd0c7542d73](../../evidence/parameters-sets-005.md#p-35ffbdd0c7542d73) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050442

```text
(config)# no do-exec pnpa service config-monitor <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 71 `；EOL ` RVA 0x33B67278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable or disable config-monitor。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7e47f765fa9d8e62](../../evidence/parameters-sets-010.md#p-7e47f765fa9d8e62) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050428

```text
(config)# no do-exec pnpa service config-reserve <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 72 `；EOL ` RVA 0x33B66F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify profile to reserve。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cfbbd60413864266](../../evidence/parameters-sets-016.md#p-cfbbd60413864266) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056016

```text
(config)# no do-exec pnpa service config-retry <number:0..10000> <number:0..10000> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 73 `；EOL ` RVA 0x33B66CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Set config max retry；` unsigned_number ` Set config-retry interval in ms。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-f18c8e5fdb7e24ec](../../evidence/parameters-sets-018.md#p-f18c8e5fdb7e24ec) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050982

```text
(config)# no do-exec pnpa service config-upgrade <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 5 `；EOL ` RVA 0x33B71938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the config source file path。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3e7e69dbed315fde](../../evidence/parameters-sets-005.md#p-3e7e69dbed315fde) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050396

```text
(config)# no do-exec pnpa service connectivity-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 74 `；EOL ` RVA 0x33B66968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enforce connectivity: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-303a3e7c7e3edb16](../../evidence/parameters-sets-004.md#p-303a3e7c7e3edb16) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056365

```text
(config)# no do-exec pnpa service copy <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 1 `；EOL ` RVA 0x33B728E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the source file URL；` string ` Specify the destination file path。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a6f5c788bce058d4](../../evidence/parameters-sets-013.md#p-a6f5c788bce058d4) · [状态效果 S-487b9983ecd50818](../../evidence/state_effects-sets-016.md#s-487b9983ecd50818)

### path-050377

```text
(config)# no do-exec pnpa service correlator-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 75 `；EOL ` RVA 0x33B66678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Correlator check: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-4a9d32d3aa341999](../../evidence/parameters-sets-006.md#p-4a9d32d3aa341999) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050359

```text
(config)# no do-exec pnpa service device-id-cert <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 76 `；EOL ` RVA 0x33B66388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) device-id-cert。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bd8ddb0fee9cd6de](../../evidence/parameters-sets-014.md#p-bd8ddb0fee9cd6de) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050899

```text
(config)# no do-exec pnpa service diag <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 6 `；EOL ` RVA 0x33B71458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Diag level: 0-none, 1-all。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8ef001bbcd9e88c1](../../evidence/parameters-sets-011.md#p-8ef001bbcd9e88c1) · [状态效果 S-bf757b979855587f](../../evidence/state_effects-sets-040.md#s-bf757b979855587f)

### path-051190

```text
(config)# no do-exec pnpa service discovery abort-autoinstall <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 7 `；EOL ` RVA 0x33B71028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056480

```text
(config)# no do-exec pnpa service discovery bypass-auto-install <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 8 `；EOL ` RVA 0x33B70DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7f4f54823086e1ad](../../evidence/parameters-sets-010.md#p-7f4f54823086e1ad) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056473

```text
(config)# no do-exec pnpa service discovery bypass-cellular-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 9 `；EOL ` RVA 0x33B70AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass cellular-check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-6bfeb9065172b03e](../../evidence/parameters-sets-009.md#p-6bfeb9065172b03e) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056468

```text
(config)# no do-exec pnpa service discovery bypass-connectivity-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 10 `；EOL ` RVA 0x33B707C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass connectivity-check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d33d16eb50948d01](../../evidence/parameters-sets-016.md#p-d33d16eb50948d01) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056464

```text
(config)# no do-exec pnpa service discovery bypass-disc-summary <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 11 `；EOL ` RVA 0x33B704D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8b96e58952d2d5ff](../../evidence/parameters-sets-011.md#p-8b96e58952d2d5ff) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056457

```text
(config)# no do-exec pnpa service discovery bypass-dns-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 12 `；EOL ` RVA 0x33B701E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-421bea45088742c0](../../evidence/parameters-sets-006.md#p-421bea45088742c0) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056449

```text
(config)# no do-exec pnpa service discovery bypass-https-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 13 `；EOL ` RVA 0x33B6FEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass https-enforcement: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-78a3b7af483fb70c](../../evidence/parameters-sets-009.md#p-78a3b7af483fb70c) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056439

```text
(config)# no do-exec pnpa service discovery bypass-napp-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 14 `；EOL ` RVA 0x33B6FC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass napp check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7c9aff8094b54082](../../evidence/parameters-sets-010.md#p-7c9aff8094b54082) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056430

```text
(config)# no do-exec pnpa service discovery bypass-startup-config <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 15 `；EOL ` RVA 0x33B6F910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8fe566dc6aeaefb0](../../evidence/parameters-sets-011.md#p-8fe566dc6aeaefb0) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056420

```text
(config)# no do-exec pnpa service discovery bypass-webui-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 16 `；EOL ` RVA 0x33B6F620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass webui check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-005812e8002c86c7](../../evidence/parameters-sets-001.md#p-005812e8002c86c7) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056409

```text
(config)# no do-exec pnpa service discovery bypass-wizard-input <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 17 `；EOL ` RVA 0x33B6F330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Bypass wizard: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-823f4c048ce7250d](../../evidence/parameters-sets-010.md#p-823f4c048ce7250d) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-051068

```text
(config)# no do-exec pnpa service discovery clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 18 `；EOL ` RVA 0x33B6F020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058826

```text
(config)# no do-exec pnpa service discovery dhcp ipv4 <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 19 `；EOL ` RVA 0x33B6ED88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify a DHCP op43 string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b249e0108e8433a5](../../evidence/parameters-sets-014.md#p-b249e0108e8433a5) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058820

```text
(config)# no do-exec pnpa service discovery dhcp ipv6 <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 20 `；EOL ` RVA 0x33B6EAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify a DHCP op17 string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-797f0695c9572a5c](../../evidence/parameters-sets-009.md#p-797f0695c9572a5c) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-051054

```text
(config)# no do-exec pnpa service discovery dns-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 21 `；EOL ` RVA 0x33B6E750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056391

```text
(config)# no do-exec pnpa service discovery dns-set <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 22 `；EOL ` RVA 0x33B6E4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the DNS domain-name-cache。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-e8db970f70a49b74](../../evidence/parameters-sets-017.md#p-e8db970f70a49b74) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056386

```text
(config)# no do-exec pnpa service discovery method-disable <number:0..15> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 23 `；EOL ` RVA 0x33B6E1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` discovery method。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-932466822764f01b](../../evidence/parameters-sets-011.md#p-932466822764f01b) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056379

```text
(config)# no do-exec pnpa service discovery method-enable <number:0..15> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 24 `；EOL ` RVA 0x33B6DEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` discovery method。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-f8ffaac76d709e73](../../evidence/parameters-sets-019.md#p-f8ffaac76d709e73) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-051018

```text
(config)# no do-exec pnpa service discovery method-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 25 `；EOL ` RVA 0x33B6DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050996

```text
(config)# no do-exec pnpa service discovery no-shutdown <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 26 `；EOL ` RVA 0x33B6D938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056345

```text
(config)# no do-exec pnpa service discovery server-credential <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 27 `；EOL ` RVA 0x33B6D6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Server Credential: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-6fe7d1a6a6e7cd5c](../../evidence/parameters-sets-009.md#p-6fe7d1a6a6e7cd5c) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050965

```text
(config)# no do-exec pnpa service discovery setup-abort <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 28 `；EOL ` RVA 0x33B6D3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050949

```text
(config)# no do-exec pnpa service discovery shutdown <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 29 `；EOL ` RVA 0x33B6D0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050935

```text
(config)# no do-exec pnpa service discovery start <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 30 `；EOL ` RVA 0x33B6CE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050920

```text
(config)# no do-exec pnpa service discovery stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 31 `；EOL ` RVA 0x33B6CBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058793

```text
(config)# no do-exec pnpa service discovery terminate <number:0..11> <number:0..14> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 32 `；EOL ` RVA 0x33B6C920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Requested By；` unsigned_number ` Reason。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-18dd944bfc769b57](../../evidence/parameters-sets-002.md#p-18dd944bfc769b57) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056300

```text
(config)# no do-exec pnpa service discovery wait-for-stop <number:0..7200> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 33 `；EOL ` RVA 0x33B6C5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Max wait time in seconds。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-5100fe36e66f0cae](../../evidence/parameters-sets-007.md#p-5100fe36e66f0cae) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050875

```text
(config)# no do-exec pnpa service do-change-mode <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 34 `；EOL ` RVA 0x33B6C298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` node mode - autonomous, controller。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2bfc1edfe80ede81](../../evidence/parameters-sets-004.md#p-2bfc1edfe80ede81) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-042142

```text
(config)# no do-exec pnpa service do-write-erase <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 35 `；EOL ` RVA 0x33B6BF88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-042125

```text
(config)# no do-exec pnpa service do-write-memory <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 36 `；EOL ` RVA 0x33B6BCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050344

```text
(config)# no do-exec pnpa service eem-proxy <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 77 `；EOL ` RVA 0x33B66098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) eem-proxy。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-773136487d0b76af](../../evidence/parameters-sets-009.md#p-773136487d0b76af) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058756

```text
(config)# no do-exec pnpa service event-notify <number:0..29> <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 37 `；EOL ` RVA 0x33B6AEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` event to notify；` string ` notified by；` string ` notified reason。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-f5bb9b810c9641cc](../../evidence/parameters-sets-018.md#p-f5bb9b810c9641cc) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050325

```text
(config)# no do-exec pnpa service fault-control <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 78 `；EOL ` RVA 0x33B65A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` fault-control level: 1-strict, 0-none。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bbf3a30fd9ffe120](../../evidence/parameters-sets-014.md#p-bbf3a30fd9ffe120) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-059584

```text
(config)# no do-exec pnpa service hello <string> <string> <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 38 `；EOL ` RVA 0x33B6AB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the protocol；` string ` Specify the host, ipv4, or ipv6；` string ` Specify the host or ipaddr；` unsigned_number ` Specify the hello port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-4c01acc227679362](../../evidence/parameters-sets-006.md#p-4c01acc227679362) · [状态效果 S-3855bded4bf1ee0a](../../evidence/state_effects-sets-012.md#s-3855bded4bf1ee0a)

### path-050762

```text
(config)# no do-exec pnpa service image-install <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 39 `；EOL ` RVA 0x33B6A080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the Image source file path。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-756361a048212659](../../evidence/parameters-sets-009.md#p-756361a048212659) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-041953

```text
(config)# no do-exec pnpa service image-install-commit <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 41 `；EOL ` RVA 0x33B6A468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-041977

```text
(config)# no do-exec pnpa service image-remove-inactive <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 40 `；EOL ` RVA 0x33B6A710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-046935

```text
(config)# no do-exec pnpa service internal <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 79 `；EOL ` RVA 0x33B530C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` service-control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b3d83bc3bb62d34d](../../evidence/parameters-sets-014.md#p-b3d83bc3bb62d34d) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-055979

```text
(config)# no do-exec pnpa service location-tag <number:0..1> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 80 `；EOL ` RVA 0x33B65760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) location tag；` string ` Specify location tag。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3c6c42bcdf2c6780](../../evidence/parameters-sets-005.md#p-3c6c42bcdf2c6780) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050303

```text
(config)# no do-exec pnpa service lock-bypass <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 81 `；EOL ` RVA 0x33B65428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b2dd957f6c9ed270](../../evidence/parameters-sets-014.md#p-b2dd957f6c9ed270) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-041257

```text
(config)# no do-exec pnpa service lock-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 82 `；EOL ` RVA 0x33B65118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-041227

```text
(config)# no do-exec pnpa service lock-exec <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 83 `；EOL ` RVA 0x33B64E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050250

```text
(config)# no do-exec pnpa service monvar-diag <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 84 `；EOL ` RVA 0x33B64BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` diag monvar string (null to reset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fb47b9e711cb8226](../../evidence/parameters-sets-019.md#p-fb47b9e711cb8226) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050185

```text
(config)# no do-exec pnpa service must-ignore-config-reg <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 86 `；EOL ` RVA 0x33B64320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore config-reg: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-de80c47601a0703a](../../evidence/parameters-sets-017.md#p-de80c47601a0703a) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050209

```text
(config)# no do-exec pnpa service must-ignore-config-rollback <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 87 `；EOL ` RVA 0x33B64610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore config-rollback: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-82d10f2cdf8d90c8](../../evidence/parameters-sets-010.md#p-82d10f2cdf8d90c8) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050156

```text
(config)# no do-exec pnpa service must-ignore-dir-walk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 88 `；EOL ` RVA 0x33B64030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore dir-walk: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-e79ae40db74922a6](../../evidence/parameters-sets-017.md#p-e79ae40db74922a6) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050131

```text
(config)# no do-exec pnpa service must-ignore-ifs-walk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 89 `；EOL ` RVA 0x33B63D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore ifs-walk: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3e18d8cfbde56d01](../../evidence/parameters-sets-005.md#p-3e18d8cfbde56d01) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050096

```text
(config)# no do-exec pnpa service must-ignore-image-signature <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 90 `；EOL ` RVA 0x33B63A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore image-signature: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cba6357f2c967325](../../evidence/parameters-sets-015.md#p-cba6357f2c967325) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050065

```text
(config)# no do-exec pnpa service must-ignore-reload-info <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 91 `；EOL ` RVA 0x33B63760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore reload_info: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-901d0977f1754861](../../evidence/parameters-sets-011.md#p-901d0977f1754861) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050228

```text
(config)# no do-exec pnpa service must-ignore-reload-info <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 85 `；EOL ` RVA 0x33B64900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must block reload-info: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-75b90c2e33b7f873](../../evidence/parameters-sets-009.md#p-75b90c2e33b7f873) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050037

```text
(config)# no do-exec pnpa service must-ignore-save-tech <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 92 `；EOL ` RVA 0x33B63470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore save-tech: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-46b4ad70bc846593](../../evidence/parameters-sets-006.md#p-46b4ad70bc846593) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050019

```text
(config)# no do-exec pnpa service must-ignore-terminate-now <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 93 `；EOL ` RVA 0x33B63180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must ignore terminate now: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-df4cb64e4a88b1b6](../../evidence/parameters-sets-017.md#p-df4cb64e4a88b1b6) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049995

```text
(config)# no do-exec pnpa service must-keep-backup <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 94 `；EOL ` RVA 0x33B62E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Must keep backup: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-17d217b95f009eb6](../../evidence/parameters-sets-002.md#p-17d217b95f009eb6) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050002

```text
(config)# no do-exec pnpa service napp-client <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 95 `；EOL ` RVA 0x33B62BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` NAPP Client: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cf109c9cb28e456d](../../evidence/parameters-sets-016.md#p-cf109c9cb28e456d) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049976

```text
(config)# no do-exec pnpa service napp-connect <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 96 `；EOL ` RVA 0x33B62870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` device SN。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-00c5eff6a64f2197](../../evidence/parameters-sets-001.md#p-00c5eff6a64f2197) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-040812

```text
(config)# no do-exec pnpa service napp-http-server <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 97 `；EOL ` RVA 0x33B62540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049937

```text
(config)# no do-exec pnpa service napp-server <number:0..2> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 98 `；EOL ` RVA 0x33B62250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` NAPP Server: 2-enable-chunking, 1-enable-no-chunking, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bf25eff6457a3b12](../../evidence/parameters-sets-015.md#p-bf25eff6457a3b12) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-040719

```text
(config)# no do-exec pnpa service napp-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 99 `；EOL ` RVA 0x33B61EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049890

```text
(config)# no do-exec pnpa service napp-tag <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 100 `；EOL ` RVA 0x33B61C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` device SN。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8b528813987481c3](../../evidence/parameters-sets-011.md#p-8b528813987481c3) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050653

```text
(config)# no do-exec pnpa service notify-now <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 42 `；EOL ` RVA 0x33B69BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile to be notified。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-68f9ccd4c3539287](../../evidence/parameters-sets-008.md#p-68f9ccd4c3539287) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-059576

```text
(config)# no do-exec pnpa service notify-service <string> <string> <string> <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 43 `；EOL ` RVA 0x33B698B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the notification type: syslog, snmp；` string ` Specify the severity；` string ` Specify the recipient；` unsigned_number ` Notify control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-70161dd8932d3652](../../evidence/parameters-sets-009.md#p-70161dd8932d3652) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050611

```text
(config)# no do-exec pnpa service notify-state <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 44 `；EOL ` RVA 0x33B69510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` state msg to be notified。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d4291a2f9dc3d499](../../evidence/parameters-sets-016.md#p-d4291a2f9dc3d499) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049843

```text
(config)# no do-exec pnpa service post-reload-priv <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 101 `；EOL ` RVA 0x33B61948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Load(1) or save(0) post-reload-priv。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a9530d319e417cdb](../../evidence/parameters-sets-013.md#p-a9530d319e417cdb) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049850

```text
(config)# no do-exec pnpa service proxy-control <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 102 `；EOL ` RVA 0x33B61658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Proxy control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d5e8c07eed1f0020](../../evidence/parameters-sets-016.md#p-d5e8c07eed1f0020) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049800

```text
(config)# no do-exec pnpa service python-listener <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 111 `；EOL ` RVA 0x33B61320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Python Listener: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-c6f3c8aa68a370fd](../../evidence/parameters-sets-015.md#p-c6f3c8aa68a370fd) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-059912

```text
(config)# no do-exec pnpa service query-to-client <string> <string> <string> configlet <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 112 `；EOL ` RVA 0x33B61028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` napp version string；` string ` UDI string；` string ` transaction id string；` string ` configlet string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-0e1b8d2f679cba72](../../evidence/parameters-sets-002.md#p-0e1b8d2f679cba72) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058496

```text
(config)# no do-exec pnpa service query-to-server <string> <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 113 `；EOL ` RVA 0x33B60C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` napp version string；` string ` UDI string；` string ` transaction id string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fa2c7c877e60c096](../../evidence/parameters-sets-019.md#p-fa2c7c877e60c096) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056127

```text
(config)# no do-exec pnpa service redirect-backup <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 46 `；EOL ` RVA 0x33B69220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the redierction profile；` unsigned_number ` Specify redirection port (0 for as-is)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a45206e0307fbffc](../../evidence/parameters-sets-013.md#p-a45206e0307fbffc) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-056115

```text
(config)# no do-exec pnpa service redirect-primary <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 47 `；EOL ` RVA 0x33B68EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the redierction profile；` unsigned_number ` Specify redirection port (0 for as-is)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-194db4a6cc116691](../../evidence/parameters-sets-002.md#p-194db4a6cc116691) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050636

```text
(config)# no do-exec pnpa service reload cancel <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 48 `；EOL ` RVA 0x33B68928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-f9a41e76d1e2f92e](../../evidence/state_effects-sets-053.md#s-f9a41e76d1e2f92e)

### path-041426

```text
(config)# no do-exec pnpa service reset <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 45 `；EOL ` RVA 0x33B65D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049703

```text
(config)# no do-exec pnpa service resolve-discovery <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 114 `；EOL ` RVA 0x33B608A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` hostname string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-9752fb71a61bd149](../../evidence/parameters-sets-012.md#p-9752fb71a61bd149) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049659

```text
(config)# no do-exec pnpa service resolve-dns <number:0..4> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 115 `；EOL ` RVA 0x33B605B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Resolution: 0-default, 1-v4-only, 2-v6-only, 3-v4-first, 4-v6-first。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fecb2817928f3c6a](../../evidence/parameters-sets-019.md#p-fecb2817928f3c6a) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049677

```text
(config)# no do-exec pnpa service resolve-hostname <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 116 `；EOL ` RVA 0x33B602C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` hostname string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-82fa424a0db43254](../../evidence/parameters-sets-010.md#p-82fa424a0db43254) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-041771

```text
(config)# no do-exec pnpa service save-tech <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 49 `；EOL ` RVA 0x33B68520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050552

```text
(config)# no do-exec pnpa service script <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 50 `；EOL ` RVA 0x33B68190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Location of the script。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-588eb97ffa148d20](../../evidence/parameters-sets-007.md#p-588eb97ffa148d20) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-042055

```text
(config)# no do-exec pnpa service sdwan-ready <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 53 `；EOL ` RVA 0x33B6B4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050828

```text
(config)# no do-exec pnpa service sdwan-start <number:0..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 51 `；EOL ` RVA 0x33B6BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` sdwan use case。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-4916a1a60f87a02b](../../evidence/parameters-sets-006.md#p-4916a1a60f87a02b) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-042078

```text
(config)# no do-exec pnpa service sdwan-stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 52 `；EOL ` RVA 0x33B6B748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049581

```text
(config)# no do-exec pnpa service security-ending-max <number:1..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 117 `；EOL ` RVA 0x33B5FF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` security ending max length。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-e9119277ed6a8fe9](../../evidence/parameters-sets-017.md#p-e9119277ed6a8fe9) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049533

```text
(config)# no do-exec pnpa service security-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 118 `；EOL ` RVA 0x33B5FCA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enforce security: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-298e91827eac381c](../../evidence/parameters-sets-004.md#p-298e91827eac381c) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049269

```text
(config)# no do-exec pnpa service server-identity-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 124 `；EOL ` RVA 0x33B5E210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Server ID validation: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-da1cfe4bd7b3fe2c](../../evidence/parameters-sets-016.md#p-da1cfe4bd7b3fe2c) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049491

```text
(config)# no do-exec pnpa service show-file <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 54 `；EOL ` RVA 0x33B5F9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-ee232f3ef7c1c75f](../../evidence/parameters-sets-018.md#p-ee232f3ef7c1c75f) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-040342

```text
(config)# no do-exec pnpa service show-running-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 55 `；EOL ` RVA 0x33B5F6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-040306

```text
(config)# no do-exec pnpa service show-startup-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 56 `；EOL ` RVA 0x33B5F400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-055539

```text
(config)# no do-exec pnpa service sid auth-only <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 119 `；EOL ` RVA 0x33B5F138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` SID auth only: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-90477e5f166ab209](../../evidence/parameters-sets-011.md#p-90477e5f166ab209) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-055491

```text
(config)# no do-exec pnpa service sid must-renew <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 121 `；EOL ` RVA 0x33B5EB80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` SID must renew: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-32c2d63e16682f7f](../../evidence/parameters-sets-004.md#p-32c2d63e16682f7f) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-055518

```text
(config)# no do-exec pnpa service sid must-validate <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 120 `；EOL ` RVA 0x33B5EE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` SID must validate: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-12062fb47306577e](../../evidence/parameters-sets-002.md#p-12062fb47306577e) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058435

```text
(config)# no do-exec pnpa service sid update <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 122 `；EOL ` RVA 0x33B5E898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the new sid；` string ` Specify the profile。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-47ee00b12a0b4c47](../../evidence/parameters-sets-006.md#p-47ee00b12a0b4c47) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-055427

```text
(config)# no do-exec pnpa service sid validation <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 123 `；EOL ` RVA 0x33B5E568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` SID validation: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a88bef6bb1b4f758](../../evidence/parameters-sets-013.md#p-a88bef6bb1b4f758) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049218

```text
(config)# no do-exec pnpa service sleep-for <number:1..3600> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 125 `；EOL ` RVA 0x33B5DF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` sleep time in seconds (No ctrl-C)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7a7e08538b1b49a5](../../evidence/parameters-sets-010.md#p-7a7e08538b1b49a5) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-049169

```text
(config)# no do-exec pnpa service smu-task-activate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 57 `；EOL ` RVA 0x33B5DC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d1cb7f9bcdcf753d](../../evidence/parameters-sets-016.md#p-d1cb7f9bcdcf753d) · [状态效果 S-dadf007ba7c185ff](../../evidence/state_effects-sets-046.md#s-dadf007ba7c185ff)

### path-055346

```text
(config)# no do-exec pnpa service smu-task-add <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 58 `；EOL ` RVA 0x33B5D920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the bundle name；` string ` Specify the bundle URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3dbbe73eff66b8a0](../../evidence/parameters-sets-005.md#p-3dbbe73eff66b8a0) · [状态效果 S-77e0b3fe25105c34](../../evidence/state_effects-sets-025.md#s-77e0b3fe25105c34)

### path-040062

```text
(config)# no do-exec pnpa service smu-task-clear-all <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 59 `；EOL ` RVA 0x33B5D548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-b2ecdbad816cb5bc](../../evidence/state_effects-sets-038.md#s-b2ecdbad816cb5bc)

### path-040021

```text
(config)# no do-exec pnpa service smu-task-commit <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 60 `；EOL ` RVA 0x33B5D290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-3fec91a3d1f5153f](../../evidence/state_effects-sets-014.md#s-3fec91a3d1f5153f)

### path-048973

```text
(config)# no do-exec pnpa service smu-task-deactivate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 61 `；EOL ` RVA 0x33B5D010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-5b889fd0e2d4722a](../../evidence/parameters-sets-007.md#p-5b889fd0e2d4722a) · [状态效果 S-4e3b46f4db205725](../../evidence/state_effects-sets-017.md#s-4e3b46f4db205725)

### path-048903

```text
(config)# no do-exec pnpa service smu-task-remove <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 62 `；EOL ` RVA 0x33B5CD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-ee910b235e862416](../../evidence/parameters-sets-018.md#p-ee910b235e862416) · [状态效果 S-e279ca640843fad7](../../evidence/state_effects-sets-048.md#s-e279ca640843fad7)

### path-039862

```text
(config)# no do-exec pnpa service smu-task-run <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 63 `；EOL ` RVA 0x33B5C9E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-7c4b37d1f3773f9b](../../evidence/state_effects-sets-026.md#s-7c4b37d1f3773f9b)

### path-039813

```text
(config)# no do-exec pnpa service smu-task-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 64 `；EOL ` RVA 0x33B5C730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-00caa2932a795fd9](../../evidence/state_effects-sets-001.md#s-00caa2932a795fd9)

### path-048799

```text
(config)# no do-exec pnpa service smu-verify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 65 `；EOL ` RVA 0x33B5C490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cc0b46ba0581021b](../../evidence/parameters-sets-015.md#p-cc0b46ba0581021b) · [状态效果 S-9156e0ae534cd3a1](../../evidence/state_effects-sets-031.md#s-9156e0ae534cd3a1)

### path-048649

```text
(config)# no do-exec pnpa service snmp <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 126 `；EOL ` RVA 0x33B5C130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the request SNMP PDU in Base64。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-94473c5c84f29ce8](../../evidence/parameters-sets-011.md#p-94473c5c84f29ce8) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-058237

```text
(config)# no do-exec pnpa service snooping <number:0..1> <number:0..4094> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 127 `；EOL ` RVA 0x33B5BE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enforce snooping: 1-enable, 0-disable；` unsigned_number ` vlan id；` string ` Specify the dhcp option string (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d9f80e33b5e3a816](../../evidence/parameters-sets-016.md#p-d9f80e33b5e3a816) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048482

```text
(config)# no do-exec pnpa service stack-renumber <number:1..9> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 128 `；EOL ` RVA 0x33B5B7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Top of stack switch number: 1-9。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-1800deaa8355c918](../../evidence/parameters-sets-002.md#p-1800deaa8355c918) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048537

```text
(config)# no do-exec pnpa service stack-reorder <number:1..9> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 129 `；EOL ` RVA 0x33B5BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Top of stack switch number: 1-9。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a790aecbeed8eeb9](../../evidence/parameters-sets-013.md#p-a790aecbeed8eeb9) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-050798

```text
(config)# no do-exec pnpa service tls-tunnel-notify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 152 `；EOL ` RVA 0x33B6B218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` tls tunnel name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-1da18c2d26058ef1](../../evidence/parameters-sets-003.md#p-1da18c2d26058ef1) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048436

```text
(config)# no do-exec pnpa service token-auth-set <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 130 `；EOL ` RVA 0x33B5B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the token-auth string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7b905f8bac36bef9](../../evidence/parameters-sets-010.md#p-7b905f8bac36bef9) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-054521

```text
(config)# no do-exec pnpa service trustpoint-install <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 153 `；EOL ` RVA 0x33B57AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the trustpoint label；` string ` Specify the certificate URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d3f8cd0bf21cc6a9](../../evidence/parameters-sets-016.md#p-d3f8cd0bf21cc6a9) · [状态效果 S-61a13446ac8de98c](../../evidence/state_effects-sets-021.md#s-61a13446ac8de98c)

### path-047593

```text
(config)# no do-exec pnpa service trustpoint-uninstall <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 154 `；EOL ` RVA 0x33B57720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the trustpoint label。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fcbe95cdcfbd4544](../../evidence/parameters-sets-019.md#p-fcbe95cdcfbd4544) · [状态效果 S-b53c3a08ec841691](../../evidence/state_effects-sets-038.md#s-b53c3a08ec841691)

### path-047609

```text
(config)# no do-exec pnpa service trustpool-install <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 155 `；EOL ` RVA 0x33B57408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the bundle URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-043798f3537f3872](../../evidence/parameters-sets-001.md#p-043798f3537f3872) · [状态效果 S-89ebbd686611cbfa](../../evidence/state_effects-sets-029.md#s-89ebbd686611cbfa)

### path-038371

```text
(config)# no do-exec pnpa service trustpool-uninstall <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 156 `；EOL ` RVA 0x33B57070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-4da5848f9ed62ba1](../../evidence/state_effects-sets-017.md#s-4da5848f9ed62ba1)

### path-048380

```text
(config)# no do-exec pnpa service udi-checking <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 131 `；EOL ` RVA 0x33B5B200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enforce udi checking: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-47ae8fb6c02bac0d](../../evidence/parameters-sets-006.md#p-47ae8fb6c02bac0d) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-039371

```text
(config)# no do-exec pnpa service udi-refresh <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 132 `；EOL ` RVA 0x33B5AEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-039319

```text
(config)# no do-exec pnpa service unlock-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 133 `；EOL ` RVA 0x33B5AC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-039274

```text
(config)# no do-exec pnpa service unlock-exec <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 134 `；EOL ` RVA 0x33B5A9A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048211

```text
(config)# no do-exec pnpa service use-ntp-server <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 135 `；EOL ` RVA 0x33B5A720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the ntp server name (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-dd997acde6d6e31b](../../evidence/parameters-sets-017.md#p-dd997acde6d6e31b) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048170

```text
(config)# no do-exec pnpa service use-src-intf <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 136 `；EOL ` RVA 0x33B5A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the source interface name (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7b726c2f0dd3a7ec](../../evidence/parameters-sets-010.md#p-7b726c2f0dd3a7ec) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048125

```text
(config)# no do-exec pnpa service use-unix-disk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 137 `；EOL ` RVA 0x33B5A148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Use Unix disk: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2757a78edd0c9a69](../../evidence/parameters-sets-003.md#p-2757a78edd0c9a69) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-048086

```text
(config)# no do-exec pnpa service use-vrf <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 138 `；EOL ` RVA 0x33B59E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the vrf name (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-51080c07389089a0](../../evidence/parameters-sets-007.md#p-51080c07389089a0) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047557

```text
(config)# no do-exec pnpa service validate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 157 `；EOL ` RVA 0x33B56DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2cd423664f9b5606](../../evidence/parameters-sets-004.md#p-2cd423664f9b5606) · [状态效果 S-4ee665251c2baa66](../../evidence/state_effects-sets-017.md#s-4ee665251c2baa66)

### path-046962

```text
(config)# no do-exec pnpa service verbose <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 139 `；EOL ` RVA 0x33B533B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` verbose-control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-be51a107b43ad9ed](../../evidence/parameters-sets-014.md#p-be51a107b43ad9ed) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047525

```text
(config)# no do-exec pnpa service verify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 158 `；EOL ` RVA 0x33B56A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-24b3cb7039281dd9](../../evidence/parameters-sets-003.md#p-24b3cb7039281dd9) · [状态效果 S-1767ba77d3b17935](../../evidence/state_effects-sets-005.md#s-1767ba77d3b17935)

### path-047481

```text
(config)# no do-exec pnpa service wait-time <number:0..100> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 159 `；EOL ` RVA 0x33B566C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` wait type。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2cca3fb3c6cbf767](../../evidence/parameters-sets-004.md#p-2cca3fb3c6cbf767) · [状态效果 S-fbe6533c33512578](../../evidence/state_effects-sets-053.md#s-fbe6533c33512578)

### path-039079

```text
(config)# no do-exec pnpa service wakeup <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 140 `；EOL ` RVA 0x33B59B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038183

```text
(config)# no do-exec pnpa service watch-ack-notifications <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 160 `；EOL ` RVA 0x33B56338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038143

```text
(config)# no do-exec pnpa service watch-all <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 161 `；EOL ` RVA 0x33B56090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038100

```text
(config)# no do-exec pnpa service watch-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 162 `；EOL ` RVA 0x33B55DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038065

```text
(config)# no do-exec pnpa service watch-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 163 `；EOL ` RVA 0x33B55B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047314

```text
(config)# no do-exec pnpa service watch-default-action <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 164 `；EOL ` RVA 0x33B55810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` action to take - wakeup-pnp-server-now, notify-pnp-server-now, syslog, etc.。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-eb9e86917c1668d8](../../evidence/parameters-sets-018.md#p-eb9e86917c1668d8) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-054358

```text
(config)# no do-exec pnpa service watch-disable <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 165 `；EOL ` RVA 0x33B554C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` watch_id；` string ` event to unwatch。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bc901cb7b87b0261](../../evidence/parameters-sets-014.md#p-bc901cb7b87b0261) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-059848

```text
(config)# no do-exec pnpa service watch-enable <string> <string> <string> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 166 `；EOL ` RVA 0x33B550E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` watch_id；` string ` event to watch；` string ` event param str ("null" for default)；` unsigned_number ` event param value；` string ` action to take - wakeup-pnp-server-now, notify-pnp-server-now, syslog, etc.。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-eb5241440f036fd2](../../evidence/parameters-sets-018.md#p-eb5241440f036fd2) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-037926

```text
(config)# no do-exec pnpa service watch-pnp-profile <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 167 `；EOL ` RVA 0x33B54C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-037891

```text
(config)# no do-exec pnpa service watch-pnp-server <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 168 `；EOL ` RVA 0x33B549C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-037858

```text
(config)# no do-exec pnpa service watch-pnp-service <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 169 `；EOL ` RVA 0x33B54718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-037811

```text
(config)# no do-exec pnpa service watch-pnp-state <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 170 `；EOL ` RVA 0x33B54470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-037759

```text
(config)# no do-exec pnpa service watch-system <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 171 `；EOL ` RVA 0x33B541C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-037712

```text
(config)# no do-exec pnpa service watch-tls-tunnel <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 172 `；EOL ` RVA 0x33B53F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047044

```text
(config)# no do-exec pnpa service webui set <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 173 `；EOL ` RVA 0x33B53C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047012

```text
(config)# no do-exec pnpa service webui start <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 175 `；EOL ` RVA 0x33B53998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-046985

```text
(config)# no do-exec pnpa service webui stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 174 `；EOL ` RVA 0x33B536A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038973

```text
(config)# no do-exec pnpa service xep-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 141 `；EOL ` RVA 0x33B59868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047954

```text
(config)# no do-exec pnpa service xep-ignore-disconnect <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 142 `；EOL ` RVA 0x33B595E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Ignore Disconnect: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a80109c842869060](../../evidence/parameters-sets-013.md#p-a80109c842869060) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038878

```text
(config)# no do-exec pnpa service xep-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 143 `；EOL ` RVA 0x33B592D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047872

```text
(config)# no do-exec pnpa service xep-tracking <number:0..4> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 144 `；EOL ` RVA 0x33B59048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` xep-tracking: 0-none, 1-all, 2-Rx, 3-Tx, 4-Drop。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-869afff84899f879](../../evidence/parameters-sets-010.md#p-869afff84899f879) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038797

```text
(config)# no do-exec pnpa service xml-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 145 `；EOL ` RVA 0x33B58D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047783

```text
(config)# no do-exec pnpa service xml-process <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 146 `；EOL ` RVA 0x33B58AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the URL of a text file containing the XML message。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7a094047a2aab620](../../evidence/parameters-sets-010.md#p-7a094047a2aab620) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-059866

```text
(config)# no do-exec pnpa service xml-profile <string> <string> <string> <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 147 `；EOL ` RVA 0x33B587C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the profile for XML encoding；` string ` Specify the protocol；` string ` Specify the host, ipv4, or ipv6；` string ` Specify the host or ipaddr；` unsigned_number ` Specify the svc_xml_profile port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-0c96bbfdba221420](../../evidence/parameters-sets-001.md#p-0c96bbfdba221420) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-038633

```text
(config)# no do-exec pnpa service xml-replay <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 148 `；EOL ` RVA 0x33B583B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-047679

```text
(config)# no do-exec pnpa service xml-udi <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 149 `；EOL ` RVA 0x33B58138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the udi for XML encoding。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-75dab89d28d346c4](../../evidence/parameters-sets-009.md#p-75dab89d28d346c4) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-054538

```text
(config)# no do-exec pnpa service xml-usr <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 150 `；EOL ` RVA 0x33B57E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Specify the usr for XML encoding；` string ` Specify the pwd for XML encoding。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8a1bb1606a99457c](../../evidence/parameters-sets-011.md#p-8a1bb1606a99457c) · [状态效果 S-8b08fa74a390a4b1](../../evidence/state_effects-sets-030.md#s-8b08fa74a390a4b1)

### path-030711

```text
(config)# no do-exec pnpa summary <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 151 `；EOL ` RVA 0x33B52D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027945

```text
(config)# no do-exec profile hogs <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 4 `；EOL ` RVA 0x34122D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ff61e0a82c1c3c7](../../evidence/conditions-sets-012.md#c-1ff61e0a82c1c3c7) · [状态效果 S-b953b8ee42acd70c](../../evidence/state_effects-sets-039.md#s-b953b8ee42acd70c)

### path-027919

```text
(config)# no do-exec profile start <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 2 `；EOL ` RVA 0x34122848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ff61e0a82c1c3c7](../../evidence/conditions-sets-012.md#c-1ff61e0a82c1c3c7) · [状态效果 S-b953b8ee42acd70c](../../evidence/state_effects-sets-039.md#s-b953b8ee42acd70c)

### path-027930

```text
(config)# no do-exec profile stop <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 3 `；EOL ` RVA 0x34122AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ff61e0a82c1c3c7](../../evidence/conditions-sets-012.md#c-1ff61e0a82c1c3c7) · [状态效果 S-b953b8ee42acd70c](../../evidence/state_effects-sets-039.md#s-b953b8ee42acd70c)

### path-027439

```text
(config)# no do-exec pwd <cr>
```

Handler ` RVA 0xD6577A0 `；selector ` 0 `；EOL ` RVA 0x33EB9310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-056935

```text
(config)# no do-exec redundancy application reload group <number:1..2> peer <cr>
```

Handler ` RVA 0xCC27200 `；selector ` 0 `；EOL ` RVA 0x33C22148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group number。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [参数 P-1ea83a5be9f8743b](../../evidence/parameters-sets-003.md#p-1ea83a5be9f8743b) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-056962

```text
(config)# no do-exec redundancy application reload group <number:1..2> self <cr>
```

Handler ` RVA 0xCC27140 `；selector ` 0 `；EOL ` RVA 0x33C223F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` group number。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [参数 P-1ea83a5be9f8743b](../../evidence/parameters-sets-003.md#p-1ea83a5be9f8743b) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-044606

```text
(config)# no do-exec redundancy application test-client disable <cr>
```

Handler ` RVA 0xCC25820 `；selector ` 0 `；EOL ` RVA 0x33C21B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-044559

```text
(config)# no do-exec redundancy application test-client enable <cr>
```

Handler ` RVA 0xCC257D0 `；selector ` 0 `；EOL ` RVA 0x33C21870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-028862

```text
(config)# no do-exec redundancy force-switchover <cr>
```

Handler ` RVA 0xD527E60 `；selector ` 0 `；EOL ` RVA 0x33E7AA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-01ef9b57c5950e3d](../../evidence/conditions-sets-001.md#c-01ef9b57c5950e3d) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-034746

```text
(config)# no do-exec redundancy keepalive enable <cr>
```

Handler ` RVA 0xD527AA0 `；selector ` 0 `；EOL ` RVA 0x33E7A638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [状态效果 S-ffd9b72befff5b51](../../evidence/state_effects-sets-054.md#s-ffd9b72befff5b51)

### path-034675

```text
(config)# no do-exec redundancy reload peer <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 8 `；EOL ` RVA 0x33FDA628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d55ca44b6a1e097](../../evidence/conditions-sets-042.md#c-6d55ca44b6a1e097) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-034821

```text
(config)# no do-exec redundancy reload shelf <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 9 `；EOL ` RVA 0x33FDAA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-34d2e9539c53f5e4](../../evidence/conditions-sets-021.md#c-34d2e9539c53f5e4) · [状态效果 S-94f20dd0dc066eda](../../evidence/state_effects-sets-032.md#s-94f20dd0dc066eda)

### path-028560

```text
(config)# no do-exec redundancy switch-activity <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 6 `；EOL ` RVA 0x33FDA2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c9fa8d0bafacac50](../../evidence/conditions-sets-078.md#c-c9fa8d0bafacac50) · [状态效果 S-1a893be0346df143](../../evidence/state_effects-sets-006.md#s-1a893be0346df143)

### path-026607

```text
(config)# no do-exec reload <cr>
```

Handler ` RVA 0xE004870 `；selector ` 0 `；EOL ` RVA 0x341641B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88af6400836c226f](../../evidence/conditions-sets-053.md#c-88af6400836c226f) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-043975

```text
(config)# no do-exec request consent-token generate-challenge shell-access <cr>
```

Handler ` RVA 0x156982F0 `；selector ` 0 `；EOL ` RVA 0x35D7BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f7494206c386f65](../../evidence/conditions-sets-037.md#c-5f7494206c386f65) · [状态效果 S-603d5eb057829984](../../evidence/state_effects-sets-021.md#s-603d5eb057829984)

### path-034104

```text
(config)# no do-exec request license new-udi <cr>
```

Handler ` RVA 0xBB696E0 `；selector ` 0 `；EOL ` RVA 0x3386A530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d752cf956ddab6b](../../evidence/conditions-sets-042.md#c-6d752cf956ddab6b) · [状态效果 S-8e73c5f837dfc267](../../evidence/state_effects-sets-030.md#s-8e73c5f837dfc267)

### path-058885

```text
(config)# no do-exec request platform software netconf-yang key generate rsa <cr>
```

Handler ` RVA 0xE9DA2E0 `；selector ` 0 `；EOL ` RVA 0x34382DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-504957a3650c2448](../../evidence/conditions-sets-031.md#c-504957a3650c2448) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-028043

```text
(config)# no do-exec request tech-support <cr>
```

Handler ` RVA 0xEB1FF10 `；selector ` 0 `；EOL ` RVA 0x343B4048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d7673a4a02446503](../../evidence/conditions-sets-083.md#c-d7673a4a02446503) · [状态效果 S-240fad2905104852](../../evidence/state_effects-sets-008.md#s-240fad2905104852)

### path-026855

```text
(config)# no do-exec restart <cr>
```

Handler ` RVA 0xF43B510 `；selector ` 0 `；EOL ` RVA 0x34648EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ccb755ee6423829e](../../evidence/conditions-sets-079.md#c-ccb755ee6423829e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026477

```text
(config)# no do-exec resume <cr>
```

Handler ` RVA 0xDE857D0 `；selector ` 0 `；EOL ` RVA 0x341875E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-290b33e33c70fc4e](../../evidence/conditions-sets-016.md#c-290b33e33c70fc4e) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-027431

```text
(config)# no do-exec rmdir <cr>
```

Handler ` RVA 0xD658590 `；selector ` 0 `；EOL ` RVA 0x33EB8A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0bbc4036072e55c5](../../evidence/conditions-sets-005.md#c-0bbc4036072e55c5) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-035345

```text
(config)# no do-exec routing-context vrf global <cr>
```

Handler ` RVA 0xE24C600 `；selector ` 0 `；EOL ` RVA 0x34280D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb79c8341d670e8e](../../evidence/conditions-sets-097.md#c-fb79c8341d670e8e) · [状态效果 S-a8ee6f4363c8548e](../../evidence/state_effects-sets-036.md#s-a8ee6f4363c8548e)

### path-035064

```text
(config)# no do-exec rsh <string> <string> <cr>
```

Handler ` RVA 0xD004170 `；selector ` 0 `；EOL ` RVA 0x33D7B938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IP address or hostname of rsh server；` string ` Command to be executed remotely。

[条件 C-90ebb260ac291ec8](../../evidence/conditions-sets-056.md#c-90ebb260ac291ec8) · [参数 P-a830d8d1cbc4fe2c](../../evidence/parameters-sets-013.md#p-a830d8d1cbc4fe2c) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-052054

```text
(config)# no do-exec set memory debug incremental starting-time <cr>
```

Handler ` RVA 0xE08DB90 `；selector ` 0 `；EOL ` RVA 0x341E7B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2929b8a3861e6914](../../evidence/conditions-sets-016.md#c-2929b8a3861e6914) · [状态效果 S-c8993a407fadce7e](../../evidence/state_effects-sets-042.md#s-c8993a407fadce7e)

### path-026390

```text
(config)# no do-exec setup <cr>
```

Handler ` RVA 0xE006400 `；selector ` 0 `；EOL ` RVA 0x341657D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-53911967820a073d](../../evidence/conditions-sets-033.md#c-53911967820a073d) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-026181

```text
(config)# no do-exec show <cr>
```

Handler ` RVA 0xE006240 `；selector ` 0 `；EOL ` RVA 0x34123660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-1b13caa8f397e71a](../../evidence/state_effects-sets-006.md#s-1b13caa8f397e71a)

### path-043222

```text
(config)# no do-exec show aaa acct-stop-cache <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 22 `；EOL ` RVA 0x34049A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-becc03a3b9099e6b](../../evidence/state_effects-sets-040.md#s-becc03a3b9099e6b)

### path-042925

```text
(config)# no do-exec show aaa attributes <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 1 `；EOL ` RVA 0x34046A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056537

```text
(config)# no do-exec show aaa cache filterserver acl <cr>
```

Handler ` RVA 0xCD2A340 `；selector ` 0 `；EOL ` RVA 0x34045CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ce9ab917f0bc63ef](../../evidence/conditions-sets-080.md#c-ce9ab917f0bc63ef) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056545

```text
(config)# no do-exec show aaa cache filterserver pending <cr>
```

Handler ` RVA 0xCD2A2F0 `；selector ` 0 `；EOL ` RVA 0x34045F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ce9ab917f0bc63ef](../../evidence/conditions-sets-080.md#c-ce9ab917f0bc63ef) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058862

```text
(config)# no do-exec show aaa cache group <string> all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 13 `；EOL ` RVA 0x340462F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` AAA SG Cache。

[条件 C-ce9ab917f0bc63ef](../../evidence/conditions-sets-080.md#c-ce9ab917f0bc63ef) · [参数 P-3dca316610ef6909](../../evidence/parameters-sets-005.md#p-3dca316610ef6909) · [状态效果 S-979ba7cd4498e7f4](../../evidence/state_effects-sets-032.md#s-979ba7cd4498e7f4)

### path-043083

```text
(config)# no do-exec show aaa clients <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 10 `；EOL ` RVA 0x34048400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051538

```text
(config)# no do-exec show aaa command handler <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 11 `；EOL ` RVA 0x34048708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056558

```text
(config)# no do-exec show aaa common-criteria policy all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 23 `；EOL ` RVA 0x34046718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5a1bdbb74d45f98c](../../evidence/conditions-sets-035.md#c-5a1bdbb74d45f98c) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042846

```text
(config)# no do-exec show aaa counters <cr>
```

Handler ` RVA 0xDD43740 `；selector ` 0 `；EOL ` RVA 0x340455E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056617

```text
(config)# no do-exec show aaa dead-criteria radius <address> <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 18 `；EOL ` RVA 0x34047E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of the server。

[条件 C-1de3d9df4fc4acb6](../../evidence/conditions-sets-012.md#c-1de3d9df4fc4acb6) · [参数 P-78e08a15bf119a7a](../../evidence/parameters-sets-009.md#p-78e08a15bf119a7a) · [状态效果 S-36dd8a81cd25e271](../../evidence/state_effects-sets-012.md#s-36dd8a81cd25e271)

### path-043359

```text
(config)# no do-exec show aaa fqdn <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 26 `；EOL ` RVA 0x3404A668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d37179533b37c123](../../evidence/conditions-sets-082.md#c-d37179533b37c123) · [状态效果 S-bfd6343d162d2af5](../../evidence/state_effects-sets-041.md#s-bfd6343d162d2af5)

### path-043018

```text
(config)# no do-exec show aaa hash <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 4 `；EOL ` RVA 0x340477F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042786

```text
(config)# no do-exec show aaa idmgr <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 20 `；EOL ` RVA 0x340452D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058870

```text
(config)# no do-exec show aaa ipv6 tacacs source-interface global <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 27 `；EOL ` RVA 0x3404AB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-a01b9c00534bee86](../../evidence/state_effects-sets-034.md#s-a01b9c00534bee86)

### path-056543

```text
(config)# no do-exec show aaa local admin_user all <cr>
```

Handler ` RVA 0xDDDD5F0 `；selector ` 0 `；EOL ` RVA 0x33E70E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-510cdccc6fb71311](../../evidence/conditions-sets-032.md#c-510cdccc6fb71311) · [状态效果 S-71a532521cf687a6](../../evidence/state_effects-sets-024.md#s-71a532521cf687a6)

### path-051344

```text
(config)# no do-exec show aaa local statistics <cr>
```

Handler ` RVA 0xD5070E0 `；selector ` 0 `；EOL ` RVA 0x33E70AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056540

```text
(config)# no do-exec show aaa local user blocked <cr>
```

Handler ` RVA 0xD505370 `；selector ` 6 `；EOL ` RVA 0x33E70818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-502313fa57050bd0](../../evidence/conditions-sets-031.md#c-502313fa57050bd0) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056524

```text
(config)# no do-exec show aaa local user lockout <cr>
```

Handler ` RVA 0xD505370 `；selector ` 2 `；EOL ` RVA 0x33E70530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043302

```text
(config)# no do-exec show aaa memory <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 19 `；EOL ` RVA 0x34049E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-202b001507e20552](../../evidence/state_effects-sets-007.md#s-202b001507e20552)

### path-056631

```text
(config)# no do-exec show aaa memory stats all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 21 `；EOL ` RVA 0x3404A148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-58463691d37f558f](../../evidence/state_effects-sets-019.md#s-58463691d37f558f)

### path-051401

```text
(config)# no do-exec show aaa method-lists authentication <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 2 `；EOL ` RVA 0x34046D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-705d3b0624c2dd77](../../evidence/state_effects-sets-024.md#s-705d3b0624c2dd77)

### path-051441

```text
(config)# no do-exec show aaa requests statistics <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 24 `；EOL ` RVA 0x34047500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043152

```text
(config)# no do-exec show aaa server-private <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 9 `；EOL ` RVA 0x34048E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-becc03a3b9099e6b](../../evidence/state_effects-sets-040.md#s-becc03a3b9099e6b)

### path-043187

```text
(config)# no do-exec show aaa servers <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 8 `；EOL ` RVA 0x34048AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-9ca7606f838abec9](../../evidence/state_effects-sets-033.md#s-9ca7606f838abec9)

### path-043199

```text
(config)# no do-exec show aaa service-profiles <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 6 `；EOL ` RVA 0x34049798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-becc03a3b9099e6b](../../evidence/state_effects-sets-040.md#s-becc03a3b9099e6b)

### path-043168

```text
(config)# no do-exec show aaa sessions <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 5 `；EOL ` RVA 0x340490D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-becc03a3b9099e6b](../../evidence/state_effects-sets-040.md#s-becc03a3b9099e6b)

### path-051622

```text
(config)# no do-exec show aaa sp-cache all-list <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 7 `；EOL ` RVA 0x34049458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-d203e3c5bbf7e056](../../evidence/state_effects-sets-044.md#s-d203e3c5bbf7e056)

### path-051385

```text
(config)# no do-exec show aaa subscriber profile <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 14 `；EOL ` RVA 0x34045958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b7ebb0b463d465ec](../../evidence/conditions-sets-071.md#c-b7ebb0b463d465ec) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-056532

```text
(config)# no do-exec show aaa tools memleak statistics <cr>
```

Handler ` RVA 0x1371D720 `；selector ` 0 `；EOL ` RVA 0x35C0D690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-605dc55b517c534e](../../evidence/state_effects-sets-021.md#s-605dc55b517c534e)

### path-043016

```text
(config)# no do-exec show aaa tracebacks <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 12 `；EOL ` RVA 0x34047A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051421

```text
(config)# no do-exec show aaa user <number:1..4294967295> <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 3 `；EOL ` RVA 0x340471B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Unique Id for a single user。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [参数 P-1b01084d2bf088cf](../../evidence/parameters-sets-003.md#p-1b01084d2bf088cf) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-033562

```text
(config)# no do-exec show access-expression <cr>
```

Handler ` RVA 0x1E3FDC10 `；selector ` 0 `；EOL ` RVA 0x345E8370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-755f3c0916a9e689](../../evidence/conditions-sets-046.md#c-755f3c0916a9e689) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-028956

```text
(config)# no do-exec show access-lists <cr>
```

Handler ` RVA 0xE0AE9A0 `；selector ` 0 `；EOL ` RVA 0x34185F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0855b1d6143262fb](../../evidence/conditions-sets-004.md#c-0855b1d6143262fb) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-035167

```text
(config)# no do-exec show access-lists acl-limit <cr>
```

Handler ` RVA 0xE0AEF10 `；selector ` 0 `；EOL ` RVA 0x34CEF048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-044844

```text
(config)# no do-exec show access-lists fqdn client <cr>
```

Handler ` RVA 0xCF22230 `；selector ` 0 `；EOL ` RVA 0x33D65A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c0e0131cb51b9276](../../evidence/state_effects-sets-041.md#s-c0e0131cb51b9276)

### path-044781

```text
(config)# no do-exec show access-lists fqdn pending-mappings <cr>
```

Handler ` RVA 0xCF24260 `；selector ` 0 `；EOL ` RVA 0x33D65CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c0e0131cb51b9276](../../evidence/state_effects-sets-041.md#s-c0e0131cb51b9276)

### path-044878

```text
(config)# no do-exec show access-lists fqdn statistics <cr>
```

Handler ` RVA 0xCF1BE90 `；selector ` 0 `；EOL ` RVA 0x33D65FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c0e0131cb51b9276](../../evidence/state_effects-sets-041.md#s-c0e0131cb51b9276)

### path-034997

```text
(config)# no do-exec show access-lists ipc <cr>
```

Handler ` RVA 0xCF05960 `；selector ` 0 `；EOL ` RVA 0x33D63E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-035180

```text
(config)# no do-exec show access-lists rate-limit <cr>
```

Handler ` RVA 0x10C68E60 `；selector ` 0 `；EOL ` RVA 0x34CEED88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-044866

```text
(config)# no do-exec show access-lists template summary <cr>
```

Handler ` RVA 0xEBB9030 `；selector ` 0 `；EOL ` RVA 0x343D13B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3464939f8c60a665](../../evidence/conditions-sets-020.md#c-3464939f8c60a665) · [状态效果 S-aa7b2e8b327bce41](../../evidence/state_effects-sets-036.md#s-aa7b2e8b327bce41)

### path-055776

```text
(config)# no do-exec show access-session limit profile details <cr>
```

Handler ` RVA 0xCAD3890 `；selector ` 0 `；EOL ` RVA 0x33B961C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4ee3d35e56eaffb9](../../evidence/conditions-sets-031.md#c-4ee3d35e56eaffb9) · [状态效果 S-461f4face6f35cb4](../../evidence/state_effects-sets-015.md#s-461f4face6f35cb4)

### path-041487

```text
(config)# no do-exec show accounting group <cr>
```

Handler ` RVA 0x10D141B0 `；selector ` 1 `；EOL ` RVA 0x34D10A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050370

```text
(config)# no do-exec show accounting group <string> <cr>
```

Handler ` RVA 0x10D141B0 `；selector ` 2 `；EOL ` RVA 0x34D10A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Group name。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [参数 P-0cff7b130b46abb3](../../evidence/parameters-sets-001.md#p-0cff7b130b46abb3) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041533

```text
(config)# no do-exec show accounting session <cr>
```

Handler ` RVA 0x10D15B60 `；selector ` 3 `；EOL ` RVA 0x34D10F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050388

```text
(config)# no do-exec show accounting session <number:1..100000> <cr>
```

Handler ` RVA 0x10D15B60 `；selector ` 4 `；EOL ` RVA 0x34D10F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Session id。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [参数 P-fe468869032ecf3b](../../evidence/parameters-sets-019.md#p-fe468869032ecf3b) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-034712

```text
(config)# no do-exec show acm rules <cr>
```

Handler ` RVA 0xDECF5D0 `；selector ` 0 `；EOL ` RVA 0x340C69D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-030803

```text
(config)# no do-exec show adjacency <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 1 `；EOL ` RVA 0x3379D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-48322428610b04c9](../../evidence/conditions-sets-028.md#c-48322428610b04c9) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037305

```text
(config)# no do-exec show adjacency connid-mgr <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 2 `；EOL ` RVA 0x3379C200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037432

```text
(config)# no do-exec show adjacency summary <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 0 `；EOL ` RVA 0x3379C5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7f655aa64276ff61](../../evidence/conditions-sets-049.md#c-7f655aa64276ff61) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037700

```text
(config)# no do-exec show alg sip <cr>
```

Handler ` RVA 0xCD3D500 `；selector ` 0 `；EOL ` RVA 0x33CD4600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-029492

```text
(config)# no do-exec show alignment <cr>
```

Handler ` RVA 0xE8F39E0 `；selector ` 0 `；EOL ` RVA 0x3433E688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043495

```text
(config)# no do-exec show alps ascu <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 2 `；EOL ` RVA 0x3541B4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-881910bb7a44a5a4](../../evidence/conditions-sets-053.md#c-881910bb7a44a5a4) · [状态效果 S-d0974a7c4d970e18](../../evidence/state_effects-sets-044.md#s-d0974a7c4d970e18)

### path-043456

```text
(config)# no do-exec show alps circuits <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 1 `；EOL ` RVA 0x3541B060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043418

```text
(config)# no do-exec show alps peers <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 0 `；EOL ` RVA 0x3541AC50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-046895

```text
(config)# no do-exec show ancp an-port summary <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 8 `；EOL ` RVA 0x336DA170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3ff1f6a9178625b3](../../evidence/state_effects-sets-014.md#s-3ff1f6a9178625b3)

### path-037608

```text
(config)# no do-exec show ancp neighbor <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 7 `；EOL ` RVA 0x336D8FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-dc2e52923ecc43e3](../../evidence/state_effects-sets-047.md#s-dc2e52923ecc43e3)

### path-046768

```text
(config)# no do-exec show ancp neighbor brief <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 1 `；EOL ` RVA 0x336D8B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-da63671dff04a25d](../../evidence/state_effects-sets-046.md#s-da63671dff04a25d)

### path-037434

```text
(config)# no do-exec show ancp port <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 3 `；EOL ` RVA 0x336D86D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a602d1be8f2a9bab](../../evidence/conditions-sets-064.md#c-a602d1be8f2a9bab) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037433

```text
(config)# no do-exec show ancp session <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 4 `；EOL ` RVA 0x336D9690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037355

```text
(config)# no do-exec show ancp statistics <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 5 `；EOL ` RVA 0x336D9A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-037465

```text
(config)# no do-exec show ancp status <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 6 `；EOL ` RVA 0x336D9DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8968d7fbd30f19b7](../../evidence/conditions-sets-053.md#c-8968d7fbd30f19b7) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050714

```text
(config)# no do-exec show application ha statistics <cr>
```

Handler ` RVA 0x12802A90 `；selector ` 0 `；EOL ` RVA 0x358D9A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1bccf2487d5955e5](../../evidence/conditions-sets-011.md#c-1bccf2487d5955e5) · [状态效果 S-da7a561e938e8dfd](../../evidence/state_effects-sets-046.md#s-da7a561e938e8dfd)

### path-050780

```text
(config)# no do-exec show application ip route <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 5 `；EOL ` RVA 0x358DAC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7a4815c79326b1a6](../../evidence/conditions-sets-047.md#c-7a4815c79326b1a6) · [状态效果 S-455c4cd93f7046ab](../../evidence/state_effects-sets-015.md#s-455c4cd93f7046ab)

### path-059578

```text
(config)# no do-exec show application ip route application <string> summary <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 2 `；EOL ` RVA 0x358DA6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Application name。

[条件 C-680144e3598ff1f5](../../evidence/conditions-sets-040.md#c-680144e3598ff1f5) · [参数 P-a7b5cfc24129c4ef](../../evidence/parameters-sets-013.md#p-a7b5cfc24129c4ef) · [状态效果 S-455c4cd93f7046ab](../../evidence/state_effects-sets-015.md#s-455c4cd93f7046ab)

### path-041757

```text
(config)# no do-exec show application summary <cr>
```

Handler ` RVA 0x1280F4C0 `；selector ` 0 `；EOL ` RVA 0x358DA110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-033397

```text
(config)# no do-exec show archive <cr>
```

Handler ` RVA 0xDECC9F0 `；selector ` 0 `；EOL ` RVA 0x3409C008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-051456

```text
(config)# no do-exec show archive config differences <cr>
```

Handler ` RVA 0xDFDC970 `；selector ` 0 `；EOL ` RVA 0x340CD168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-41eda4e0e14ce222](../../evidence/state_effects-sets-014.md#s-41eda4e0e14ce222)

### path-056571

```text
(config)# no do-exec show archive config rollback timer <cr>
```

Handler ` RVA 0xDFDCFE0 `；selector ` 0 `；EOL ` RVA 0x340CD868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058864

```text
(config)# no do-exec show archive log config all persistent <cr>
```

Handler ` RVA 0xDF14700 `；selector ` 0 `；EOL ` RVA 0x340A2B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9cbb4b4153436f12](../../evidence/state_effects-sets-033.md#s-9cbb4b4153436f12)

### path-056564

```text
(config)# no do-exec show archive log config statistics <cr>
```

Handler ` RVA 0xDF0B2B0 `；selector ` 0 `；EOL ` RVA 0x340A27D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-948b796c1d2e09af](../../evidence/state_effects-sets-031.md#s-948b796c1d2e09af)

### path-031284

```text
(config)# no do-exec show arp <cr>
```

Handler ` RVA 0xCD4CF60 `；selector ` 0 `；EOL ` RVA 0x33D29978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-650a0de43e577f20](../../evidence/conditions-sets-039.md#c-650a0de43e577f20) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-033902

```text
(config)# no do-exec show asp <cr>
```

Handler ` RVA 0x113A1300 `；selector ` 0 `；EOL ` RVA 0x354A39B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041241

```text
(config)# no do-exec show async bootp <cr>
```

Handler ` RVA 0xD3448C0 `；selector ` 0 `；EOL ` RVA 0x349343F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041279

```text
(config)# no do-exec show async status <cr>
```

Handler ` RVA 0xFF3FE50 `；selector ` 0 `；EOL ` RVA 0x349346A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043980

```text
(config)# no do-exec show auto install status <cr>
```

Handler ` RVA 0xFFA8E70 `；selector ` 0 `；EOL ` RVA 0x349433F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-044001

```text
(config)# no do-exec show auto install tech-support <cr>
```

Handler ` RVA 0xFFAE9B0 `；selector ` 0 `；EOL ` RVA 0x34943698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-044023

```text
(config)# no do-exec show auto install trace <cr>
```

Handler ` RVA 0xFFAE910 `；selector ` 0 `；EOL ` RVA 0x34943940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-043964

```text
(config)# no do-exec show auto secure config <cr>
```

Handler ` RVA 0xB246B10 `；selector ` 0 `；EOL ` RVA 0x336D4EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-041903

```text
(config)# no do-exec show autoip status <cr>
```

Handler ` RVA 0xB286210 `；selector ` 0 `；EOL ` RVA 0x3372CA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-050626

```text
(config)# no do-exec show autoip status detail <cr>
```

Handler ` RVA 0xB286260 `；selector ` 0 `；EOL ` RVA 0x3372CA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-032056

```text
(config)# no do-exec show avc <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 89 `；EOL ` RVA 0x35254938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f267040d57d4ceb6](../../evidence/conditions-sets-094.md#c-f267040d57d4ceb6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055640

```text
(config)# no do-exec show avc sd-service info cmds <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 87 `；EOL ` RVA 0x3524EA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058483

```text
(config)# no do-exec show avc sd-service info cmds config <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 86 `；EOL ` RVA 0x3524EA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058473

```text
(config)# no do-exec show avc sd-service info cmds status <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 88 `；EOL ` RVA 0x3524E798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-055602

```text
(config)# no do-exec show avc sd-service info detailed <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 61 `；EOL ` RVA 0x3524EF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-80508a6a03e99bb1](../../evidence/state_effects-sets-027.md#s-80508a6a03e99bb1)

### path-055863

```text
(config)# no do-exec show avc sd-service info ent <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 66 `；EOL ` RVA 0x35253A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058562

```text
(config)# no do-exec show avc sd-service info ent config <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 72 `；EOL ` RVA 0x35252720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059540

```text
(config)# no do-exec show avc sd-service info ent device-health db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 75 `；EOL ` RVA 0x35253FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059921

```text
(config)# no do-exec show avc sd-service info ent device-health export last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 76 `；EOL ` RVA 0x35253D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059918

```text
(config)# no do-exec show avc sd-service info ent device-health export stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 77 `；EOL ` RVA 0x35253AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059546

```text
(config)# no do-exec show avc sd-service info ent device-health interfaces <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 74 `；EOL ` RVA 0x35254298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058632

```text
(config)# no do-exec show avc sd-service info ent export <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 70 `；EOL ` RVA 0x352534F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059532

```text
(config)# no do-exec show avc sd-service info ent export current <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 68 `；EOL ` RVA 0x35252F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059541

```text
(config)# no do-exec show avc sd-service info ent export keys-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 73 `；EOL ` RVA 0x352534D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e75e7c5f49467991](../../evidence/conditions-sets-089.md#c-e75e7c5f49467991) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059536

```text
(config)# no do-exec show avc sd-service info ent export last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 69 `；EOL ` RVA 0x35253228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058578

```text
(config)# no do-exec show avc sd-service info ent fields-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 71 `；EOL ` RVA 0x352529C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-408faba1da1d990a](../../evidence/conditions-sets-025.md#c-408faba1da1d990a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058591

```text
(config)# no do-exec show avc sd-service info ent symbol-table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 67 `；EOL ` RVA 0x35252C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8bde9d2728f9f1a](../../evidence/conditions-sets-077.md#c-c8bde9d2728f9f1a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058555

```text
(config)# no do-exec show avc sd-service info export flow-counters <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 63 `；EOL ` RVA 0x35250B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b12b55aa16da627d](../../evidence/conditions-sets-068.md#c-b12b55aa16da627d) · [状态效果 S-77f324a65483b312](../../evidence/state_effects-sets-025.md#s-77f324a65483b312)

### path-058557

```text
(config)# no do-exec show avc sd-service info export l3-cache <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 55 `；EOL ` RVA 0x3524FF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-77f324a65483b312](../../evidence/state_effects-sets-025.md#s-77f324a65483b312)

### path-058545

```text
(config)# no do-exec show avc sd-service info export npc-info <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 62 `；EOL ` RVA 0x35250880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a32f3f16c88a2c74](../../evidence/conditions-sets-063.md#c-a32f3f16c88a2c74) · [状态效果 S-77f324a65483b312](../../evidence/state_effects-sets-025.md#s-77f324a65483b312)

### path-058584

```text
(config)# no do-exec show avc sd-service info export socket-cache <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 56 `；EOL ` RVA 0x352505A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-77f324a65483b312](../../evidence/state_effects-sets-025.md#s-77f324a65483b312)

### path-058538

```text
(config)# no do-exec show avc sd-service info import dump <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-80bfabfb380b920e](../../evidence/state_effects-sets-027.md#s-80bfabfb380b920e)

### path-059514

```text
(config)# no do-exec show avc sd-service info import dump l3-rules <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-1a59ff567cc653a4](../../evidence/state_effects-sets-006.md#s-1a59ff567cc653a4)

### path-059518

```text
(config)# no do-exec show avc sd-service info import dump l4-rules <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0468ff64ee7f1c47](../../evidence/state_effects-sets-001.md#s-0468ff64ee7f1c47)

### path-058564

```text
(config)# no do-exec show avc sd-service info tls-fp clear-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 85 `；EOL ` RVA 0x35251648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a281251bbcdf2caf](../../evidence/conditions-sets-063.md#c-a281251bbcdf2caf) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058603

```text
(config)# no do-exec show avc sd-service info tls-fp clear-stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 82 `；EOL ` RVA 0x352523F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57e0a4ed47b4aa96](../../evidence/conditions-sets-034.md#c-57e0a4ed47b4aa96) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058567

```text
(config)# no do-exec show avc sd-service info tls-fp dump-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 83 `；EOL ` RVA 0x35251178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-08f104f9e5675f7a](../../evidence/conditions-sets-004.md#c-08f104f9e5675f7a) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059521

```text
(config)# no do-exec show avc sd-service info tls-fp dump-db detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 84 `；EOL ` RVA 0x35251150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2a19795555946921](../../evidence/conditions-sets-016.md#c-2a19795555946921) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059537

```text
(config)# no do-exec show avc sd-service info tls-fp fingerprint-db dump <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 80 `；EOL ` RVA 0x35251F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9f5a3c9b6d75e25f](../../evidence/conditions-sets-062.md#c-9f5a3c9b6d75e25f) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059917

```text
(config)# no do-exec show avc sd-service info tls-fp fingerprint-db dump detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 81 `；EOL ` RVA 0x35251EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dad1ba29aa9615e1](../../evidence/conditions-sets-084.md#c-dad1ba29aa9615e1) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-059529

```text
(config)# no do-exec show avc sd-service info tls-fp fingerprint-db info <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 79 `；EOL ` RVA 0x35251C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-818143645fa9c448](../../evidence/conditions-sets-050.md#c-818143645fa9c448) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-058579

```text
(config)# no do-exec show avc sd-service info tls-fp show-stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 78 `；EOL ` RVA 0x352518F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6d0955a494ab5957](../../evidence/conditions-sets-042.md#c-6d0955a494ab5957) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-029599

```text
(config)# no do-exec show backup <cr>
```

Handler ` RVA 0xEF363F0 `；selector ` 0 `；EOL ` RVA 0x34483370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-034642

```text
(config)# no do-exec show banner login <cr>
```

Handler ` RVA 0xDEFB260 `；selector ` 0 `；EOL ` RVA 0x340C5CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-7bb5a8a0e44633fe](../../evidence/state_effects-sets-026.md#s-7bb5a8a0e44633fe)

### path-042151

```text
(config)# no do-exec show beep blocked <cr>
```

Handler ` RVA 0xEF60FC0 `；selector ` 1 `；EOL ` RVA 0x3448BFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-289de11ffdfbb361](../../evidence/conditions-sets-016.md#c-289de11ffdfbb361) · [状态效果 S-371cc526d24b92b2](../../evidence/state_effects-sets-012.md#s-371cc526d24b92b2)

### path-042181

```text
(config)# no do-exec show beep session <cr>
```

Handler ` RVA 0xEF60FC0 `；selector ` 3 `；EOL ` RVA 0x3448BD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-289de11ffdfbb361](../../evidence/conditions-sets-016.md#c-289de11ffdfbb361) · [状态效果 S-e9335913cf19ee7f](../../evidence/state_effects-sets-049.md#s-e9335913cf19ee7f)

### path-039277

```text
(config)# no do-exec show bfd clients <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 1 `；EOL ` RVA 0x34CB4440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039311

```text
(config)# no do-exec show bfd drops <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 4 `；EOL ` RVA 0x34CB49E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039525

```text
(config)# no do-exec show bfd fast-timers-on-slow-int <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 8 `；EOL ` RVA 0x34CB54E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039326

```text
(config)# no do-exec show bfd hardware <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 5 `；EOL ` RVA 0x34CB4748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039419

```text
(config)# no do-exec show bfd idbs <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 13 `；EOL ` RVA 0x34CB4F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039363

```text
(config)# no do-exec show bfd interface <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 2 `；EOL ` RVA 0x34CB4C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039171

```text
(config)# no do-exec show bfd internal <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 0 `；EOL ` RVA 0x34CB2A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b6cf434966e05a7a](../../evidence/state_effects-sets-039.md#s-b6cf434966e05a7a)

### path-039534

```text
(config)# no do-exec show bfd map <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 6 `；EOL ` RVA 0x34CB5248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-039146

```text
(config)# no do-exec show bfd summary <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 3 `；EOL ` RVA 0x34CB21C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0601ab9e9bf2f4bf](../../evidence/state_effects-sets-002.md#s-0601ab9e9bf2f4bf)

### path-048533

```text
(config)# no do-exec show bfd target-identifier all <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 9 `；EOL ` RVA 0x34CB57D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-048713

```text
(config)# no do-exec show bfd target-identifier interface <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 12 `；EOL ` RVA 0x34CB5FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-accf9c8dabd2c0cb](../../evidence/conditions-sets-067.md#c-accf9c8dabd2c0cb) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-048600

```text
(config)# no do-exec show bfd target-identifier local <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 10 `；EOL ` RVA 0x34CB5A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-048658

```text
(config)# no do-exec show bfd target-identifier remote <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 11 `；EOL ` RVA 0x34CB5D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2ca547d4d4c45c81](../../evidence/state_effects-sets-010.md#s-2ca547d4d4c45c81)

### path-056120

```text
(config)# no do-exec show bgp <address> <address> longer-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 5 `；EOL ` RVA 0x344C3548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network in the BGP routing table to display；` address ` Network mask。

[条件 C-b3f268d634b7ef44](../../evidence/conditions-sets-070.md#c-b3f268d634b7ef44) · [参数 P-54d2e655ff68d058](../../evidence/parameters-sets-007.md#p-54d2e655ff68d058) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-056133

```text
(config)# no do-exec show bgp <address> <address> shorter-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 18 `；EOL ` RVA 0x344C3850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network in the BGP routing table to display；` address ` Network mask。

[条件 C-b3f268d634b7ef44](../../evidence/conditions-sets-070.md#c-b3f268d634b7ef44) · [参数 P-54d2e655ff68d058](../../evidence/parameters-sets-007.md#p-54d2e655ff68d058) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041011

```text
(config)# no do-exec show bgp <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344C6070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Display route-type 2 with specified MAC Address (H.H.H or HH:HH:HH:HH:HH:HH)。

[条件 C-9d2b0dee5c3e0a48](../../evidence/conditions-sets-061.md#c-9d2b0dee5c3e0a48) · [参数 P-176896aa62ac74b6](../../evidence/parameters-sets-002.md#p-176896aa62ac74b6) · [状态效果 S-683167b5cdd33856](../../evidence/state_effects-sets-022.md#s-683167b5cdd33856)

### path-041908

```text
(config)# no do-exec show bgp <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 1 `；EOL ` RVA 0x344C3B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network in the BGP routing table to display。

[条件 C-b3f268d634b7ef44](../../evidence/conditions-sets-070.md#c-b3f268d634b7ef44) · [参数 P-3d2613e00c71652f](../../evidence/parameters-sets-005.md#p-3d2613e00c71652f) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-056175

```text
(config)# no do-exec show bgp <address> internal pathext <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 43 `；EOL ` RVA 0x344C3F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network in the BGP routing table to display。

[条件 C-b3f268d634b7ef44](../../evidence/conditions-sets-070.md#c-b3f268d634b7ef44) · [参数 P-3d2613e00c71652f](../../evidence/parameters-sets-005.md#p-3d2613e00c71652f) · [状态效果 S-ac842766358d1ded](../../evidence/state_effects-sets-036.md#s-ac842766358d1ded)

### path-032314

```text
(config)# no do-exec show bgp <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 0 `；EOL ` RVA 0x344CA860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2fd4743bb6cd1b93](../../evidence/conditions-sets-019.md#c-2fd4743bb6cd1b93) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-032774

```text
(config)# no do-exec show bgp <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 13 `；EOL ` RVA 0x34500CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ce82cfece7c8b403](../../evidence/conditions-sets-080.md#c-ce82cfece7c8b403) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-058599

```text
(config)# no do-exec show bgp all route-type <number:1..7> <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344C8570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Multicast VPN NLRI route-type；` address ` Route-type 1 originator ID。

[条件 C-4f7b36f51ae999be](../../evidence/conditions-sets-031.md#c-4f7b36f51ae999be) · [参数 P-1b8a4dec5fa285d3](../../evidence/parameters-sets-003.md#p-1b8a4dec5fa285d3) · [状态效果 S-114a3370c6425681](../../evidence/state_effects-sets-004.md#s-114a3370c6425681)

### path-058611

```text
(config)# no do-exec show bgp all route-type <number:1..7> <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344CB0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Multicast VPN NLRI route-type；` address ` Route-type 1 originator ID。

[条件 C-a16c8bc03ffd3fc5](../../evidence/conditions-sets-062.md#c-a16c8bc03ffd3fc5) · [参数 P-fe3de206dc5b3918](../../evidence/parameters-sets-019.md#p-fe3de206dc5b3918) · [状态效果 S-b8e408a794eb362f](../../evidence/state_effects-sets-039.md#s-b8e408a794eb362f)

### path-050276

```text
(config)# no do-exec show bgp aspath hash <cr>
```

Handler ` RVA 0xF1723F0 `；selector ` 0 `；EOL ` RVA 0x344BE710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b585fc4d04add1cd](../../evidence/conditions-sets-070.md#c-b585fc4d04add1cd) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050257

```text
(config)# no do-exec show bgp attr hash <cr>
```

Handler ` RVA 0xF1729B0 `；selector ` 0 `；EOL ` RVA 0x344BDC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3fd6796db48e491a](../../evidence/conditions-sets-025.md#c-3fd6796db48e491a) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050277

```text
(config)# no do-exec show bgp attr nexthop <cr>
```

Handler ` RVA 0xF172000 `；selector ` 0 `；EOL ` RVA 0x344BDF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3329a332a6a38952](../../evidence/conditions-sets-020.md#c-3329a332a6a38952) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-040932

```text
(config)# no do-exec show bgp binding-sid <cr>
```

Handler ` RVA 0xF1CFDA0 `；selector ` 0 `；EOL ` RVA 0x344BC410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3ff8002708bc146c](../../evidence/conditions-sets-025.md#c-3ff8002708bc146c) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041670

```text
(config)# no do-exec show bgp cidr-only <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 4 `；EOL ` RVA 0x344C25B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b9897bd9b94129e4](../../evidence/conditions-sets-072.md#c-b9897bd9b94129e4) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041454

```text
(config)# no do-exec show bgp cluster-ids <cr>
```

Handler ` RVA 0xF185F30 `；selector ` 39 `；EOL ` RVA 0x344C0470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-26d87fb8dedcfee6](../../evidence/conditions-sets-015.md#c-26d87fb8dedcfee6) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050357

```text
(config)# no do-exec show bgp cluster-ids internal <cr>
```

Handler ` RVA 0xF185F30 `；selector ` 38 `；EOL ` RVA 0x344C0448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ff9a17c60121fb93](../../evidence/conditions-sets-099.md#c-ff9a17c60121fb93) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-042020

```text
(config)# no do-exec show bgp community <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 7 `；EOL ` RVA 0x34501500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b179f58b165a509](../../evidence/conditions-sets-054.md#c-8b179f58b165a509) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050640

```text
(config)# no do-exec show bgp community-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 8 `；EOL ` RVA 0x34501A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` community-list number。

[条件 C-9b305abbaac9a019](../../evidence/conditions-sets-060.md#c-9b305abbaac9a019) · [参数 P-a5a54df05ee65623](../../evidence/parameters-sets-013.md#p-a5a54df05ee65623) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041531

```text
(config)# no do-exec show bgp dampened-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 12 `；EOL ` RVA 0x344C1470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-468b463167f2c58d](../../evidence/conditions-sets-028.md#c-468b463167f2c58d) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050394

```text
(config)# no do-exec show bgp dampening parameters <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 14 `；EOL ` RVA 0x344C11C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-26d87fb8dedcfee6](../../evidence/conditions-sets-015.md#c-26d87fb8dedcfee6) · [状态效果 S-7f0a12199bbb1679](../../evidence/state_effects-sets-027.md#s-7f0a12199bbb1679)

### path-040811

```text
(config)# no do-exec show bgp default <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 32 `；EOL ` RVA 0x344C5448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e60788873c187c26](../../evidence/conditions-sets-089.md#c-e60788873c187c26) · [状态效果 S-9549e77a603cb914](../../evidence/state_effects-sets-032.md#s-9549e77a603cb914)

### path-040934

```text
(config)# no do-exec show bgp detail <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 44 `；EOL ` RVA 0x344C8F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8dbb839227eb7f25](../../evidence/conditions-sets-055.md#c-8dbb839227eb7f25) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050049

```text
(config)# no do-exec show bgp detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 52 `；EOL ` RVA 0x344C8F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` L2VPN EVPN Route。

[条件 C-8dbb839227eb7f25](../../evidence/conditions-sets-055.md#c-8dbb839227eb7f25) · [参数 P-faf666212ecfdfb5](../../evidence/parameters-sets-019.md#p-faf666212ecfdfb5) · [状态效果 S-d59142d60ad9d23a](../../evidence/state_effects-sets-045.md#s-d59142d60ad9d23a)

### path-050080

```text
(config)# no do-exec show bgp detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 53 `；EOL ` RVA 0x344C94F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IPv4 MVPN Route。

[条件 C-29a7e5d1c554a45f](../../evidence/conditions-sets-016.md#c-29a7e5d1c554a45f) · [参数 P-f14d7edbc095e8f7](../../evidence/parameters-sets-018.md#p-f14d7edbc095e8f7) · [状态效果 S-036fe727ff5ddfa9](../../evidence/state_effects-sets-001.md#s-036fe727ff5ddfa9)

### path-050112

```text
(config)# no do-exec show bgp detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 54 `；EOL ` RVA 0x344C9810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` IPv6 MVPN Route。

[条件 C-d4c0f54b7e28c78a](../../evidence/conditions-sets-082.md#c-d4c0f54b7e28c78a) · [参数 P-8e299cbbeb9d5d4c](../../evidence/parameters-sets-011.md#p-8e299cbbeb9d5d4c) · [状态效果 S-c086e23734bc59ce](../../evidence/state_effects-sets-041.md#s-c086e23734bc59ce)

### path-049864

```text
(config)# no do-exec show bgp evi context <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 47 `；EOL ` RVA 0x344C5C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9d2b0dee5c3e0a48](../../evidence/conditions-sets-061.md#c-9d2b0dee5c3e0a48) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050698

```text
(config)# no do-exec show bgp extcommunity-list <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 11 `；EOL ` RVA 0x34502620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` extcommunity-list name。

[条件 C-0340ce5884c66dff](../../evidence/conditions-sets-002.md#c-0340ce5884c66dff) · [参数 P-16c46cd5a4132de6](../../evidence/parameters-sets-002.md#p-16c46cd5a4132de6) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050482

```text
(config)# no do-exec show bgp filter-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 2 `；EOL ` RVA 0x34500058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Regular expression access list number。

[条件 C-26d87fb8dedcfee6](../../evidence/conditions-sets-015.md#c-26d87fb8dedcfee6) · [参数 P-2d3e3d354ed0b984](../../evidence/parameters-sets-004.md#p-2d3e3d354ed0b984) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041742

```text
(config)# no do-exec show bgp import <cr>
```

Handler ` RVA 0xF171AC0 `；selector ` 0 `；EOL ` RVA 0x344C2260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae9966d71ffdcca3](../../evidence/conditions-sets-067.md#c-ae9966d71ffdcca3) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050496

```text
(config)# no do-exec show bgp inconsistency nexthop-label <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 20 `；EOL ` RVA 0x344C2908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4fa666e1e7f45cd1](../../evidence/conditions-sets-031.md#c-4fa666e1e7f45cd1) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050542

```text
(config)# no do-exec show bgp inconsistency nexthop-label <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 20 `；EOL ` RVA 0x3552E078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-da7ffe34765aca6e](../../evidence/conditions-sets-084.md#c-da7ffe34765aca6e) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041794

```text
(config)# no do-exec show bgp inconsistent-as <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 6 `；EOL ` RVA 0x34500F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9b305abbaac9a019](../../evidence/conditions-sets-060.md#c-9b305abbaac9a019) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041715

```text
(config)# no do-exec show bgp injected-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 17 `；EOL ` RVA 0x344C2BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-04c97389bc083ccc](../../evidence/conditions-sets-002.md#c-04c97389bc083ccc) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041768

```text
(config)# no do-exec show bgp injected-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 17 `；EOL ` RVA 0x3552E308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-da7ffe34765aca6e](../../evidence/conditions-sets-084.md#c-da7ffe34765aca6e) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041542

```text
(config)# no do-exec show bgp internal <cr>
```

Handler ` RVA 0xF184450 `；selector ` 35 `；EOL ` RVA 0x344C0C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-afbde34b0ad2f78d](../../evidence/conditions-sets-068.md#c-afbde34b0ad2f78d) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050399

```text
(config)# no do-exec show bgp internal stat <cr>
```

Handler ` RVA 0xF184450 `；selector ` 36 `；EOL ` RVA 0x344C0C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-40570ab14841f95f](../../evidence/conditions-sets-025.md#c-40570ab14841f95f) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050375

```text
(config)# no do-exec show bgp internal task <cr>
```

Handler ` RVA 0xF184450 `；selector ` 37 `；EOL ` RVA 0x344C09A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2dbe429f29f14acf](../../evidence/conditions-sets-018.md#c-2dbe429f29f14acf) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-040994

```text
(config)# no do-exec show bgp labels <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 16 `；EOL ` RVA 0x344C9DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d38c63946e23893b](../../evidence/conditions-sets-082.md#c-d38c63946e23893b) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041104

```text
(config)# no do-exec show bgp labels <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 16 `；EOL ` RVA 0x344CA838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-522678a3a994b617](../../evidence/conditions-sets-032.md#c-522678a3a994b617) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-041649

```text
(config)# no do-exec show bgp labels <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 16 `；EOL ` RVA 0x344C1810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae9966d71ffdcca3](../../evidence/conditions-sets-067.md#c-ae9966d71ffdcca3) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)

### path-050682

```text
(config)# no do-exec show bgp largecommunity-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 10 `；EOL ` RVA 0x34502278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` community-list number。

[条件 C-9b305abbaac9a019](../../evidence/conditions-sets-060.md#c-9b305abbaac9a019) · [参数 P-73dcc5a2cab3ca61](../../evidence/parameters-sets-009.md#p-73dcc5a2cab3ca61) · [状态效果 S-ba89b633700ca70a](../../evidence/state_effects-sets-039.md#s-ba89b633700ca70a)
