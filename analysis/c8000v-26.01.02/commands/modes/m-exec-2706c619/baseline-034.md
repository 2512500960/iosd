# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-024743

```text
(exec)# do-exec test tunnel tun-to <number:0..9> feature enable pre-decap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 10 `；EOL ` RVA 0x33796EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-b73c4a3a62cee5ae](../../evidence/state_effects-sets-039.md#s-b73c4a3a62cee5ae)

### path-024728

```text
(exec)# do-exec test tunnel tun-to <number:0..9> gre key disable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 8 `；EOL ` RVA 0x33796538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-b4c948f9a7dbbb93](../../evidence/state_effects-sets-038.md#s-b4c948f9a7dbbb93)

### path-024720

```text
(exec)# do-exec test tunnel tun-to <number:0..9> payload ipv4 enable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 11 `；EOL ` RVA 0x33795DD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-d139ea25f94f0916](../../evidence/conditions-sets-081.md#c-d139ea25f94f0916) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-69cc7260867861f7](../../evidence/state_effects-sets-023.md#s-69cc7260867861f7)

### path-025025

```text
(exec)# do-exec test tunnel tun-to <number:0..9> payload ipv4 mtu default <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 12 `；EOL ` RVA 0x337960C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-d139ea25f94f0916](../../evidence/conditions-sets-081.md#c-d139ea25f94f0916) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-d32ce91a6df9f4b2](../../evidence/state_effects-sets-045.md#s-d32ce91a6df9f4b2)

### path-023816

```text
(exec)# do-exec test tunnel tun-to <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 3 `；EOL ` RVA 0x33794948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b5fd48203094e8df](../../evidence/parameters-sets-014.md#p-b5fd48203094e8df) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014806

```text
(exec)# do-exec test uninstall <string> <cr>
```

Handler ` RVA 0x15A6CC70 `；selector ` 0 `；EOL ` RVA 0x35DE37F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-e0e7243124538125](../../evidence/conditions-sets-087.md#c-e0e7243124538125) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b9316c0493b1273](../../evidence/parameters-sets-010.md#p-7b9316c0493b1273) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023527

```text
(exec)# do-exec test vrrs client add <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 9 `；EOL ` RVA 0x342A0CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c1faf0a01590e7c1](../../evidence/parameters-sets-015.md#p-c1faf0a01590e7c1) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-021265

```text
(exec)# do-exec test vrrs client register <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 11 `；EOL ` RVA 0x342A0678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-dfe2be5a59cb5d99](../../evidence/parameters-sets-017.md#p-dfe2be5a59cb5d99) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-023541

```text
(exec)# do-exec test vrrs client remove <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 8 `；EOL ` RVA 0x342A0FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-912dcfafa5af0bac](../../evidence/parameters-sets-011.md#p-912dcfafa5af0bac) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-021238

```text
(exec)# do-exec test vrrs client unregister <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 10 `；EOL ` RVA 0x342A0988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e7f6bd64325acaf4](../../evidence/parameters-sets-017.md#p-e7f6bd64325acaf4) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-023641

```text
(exec)# do-exec test vrrs pathway name <string> disconnect <cr>
```

Handler ` RVA 0x133F9580 `；selector ` 0 `；EOL ` RVA 0x35A8B960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the VRRS tag associated with pathways。

[条件 C-463a0f267f49a4f6](../../evidence/conditions-sets-027.md#c-463a0f267f49a4f6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b55499403f5cacac](../../evidence/parameters-sets-014.md#p-b55499403f5cacac) · [状态效果 S-c53cdbaf97b1a6cd](../../evidence/state_effects-sets-042.md#s-c53cdbaf97b1a6cd)

### path-016728

```text
(exec)# do-exec test vrrs plugin server <cr>
```

Handler ` RVA 0xE2FF4F0 `；selector ` 0 `；EOL ` RVA 0x342A69C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4877c057cb96702c](../../evidence/conditions-sets-028.md#c-4877c057cb96702c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6eb9c0c7b613d93d](../../evidence/state_effects-sets-024.md#s-6eb9c0c7b613d93d)

### path-024644

```text
(exec)# do-exec test vrrs server add <string> vip <address> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 7 `；EOL ` RVA 0x342A15D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name string；` address ` VRRP group's virtual address。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1c35fd9c9703b522](../../evidence/parameters-sets-003.md#p-1c35fd9c9703b522) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-021269

```text
(exec)# do-exec test vrrs server delete <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 5 `；EOL ` RVA 0x342A1F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3c862bfbe3046baa](../../evidence/parameters-sets-005.md#p-3c862bfbe3046baa) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-021329

```text
(exec)# do-exec test vrrs server update <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 6 `；EOL ` RVA 0x342A1BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6c0f2e263c8af654](../../evidence/parameters-sets-009.md#p-6c0f2e263c8af654) · [状态效果 S-3c98636ba5cedb2d](../../evidence/state_effects-sets-013.md#s-3c98636ba5cedb2d)

### path-023667

```text
(exec)# do-exec test wccp ip web-cache assignment hash <cr>
```

Handler ` RVA 0x10AE0FA0 `；selector ` 0 `；EOL ` RVA 0x34CA15E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ab6f89db78e80bdb](../../evidence/conditions-sets-066.md#c-ab6f89db78e80bdb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-134770d293c4361f](../../evidence/state_effects-sets-005.md#s-134770d293c4361f)

### path-021452

```text
(exec)# do-exec test wccp ip web-cache capabilities <cr>
```

Handler ` RVA 0x10AE0C00 `；selector ` 0 `；EOL ` RVA 0x34CA11B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-af97d057c7bd2c8a](../../evidence/conditions-sets-068.md#c-af97d057c7bd2c8a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ac9672fcce16ac2b](../../evidence/state_effects-sets-036.md#s-ac9672fcce16ac2b)

### path-024989

```text
(exec)# do-exec test wccp ip web-cache service <number:0..255> <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10AE0A90 `；selector ` 0 `；EOL ` RVA 0x34CA1C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` WCCP service priority；` unsigned_number ` WCCP service protocol；` unsigned_number ` WCCP service flags。

[条件 C-4caa14063efcbaa3](../../evidence/conditions-sets-030.md#c-4caa14063efcbaa3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-71b77f6b738f2f59](../../evidence/parameters-sets-009.md#p-71b77f6b738f2f59) · [状态效果 S-ac9672fcce16ac2b](../../evidence/state_effects-sets-036.md#s-ac9672fcce16ac2b)

### path-014614

```text
(exec)# do-exec test wsma history <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 1 `；EOL ` RVA 0x3463D0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018763

```text
(exec)# do-exec test wsma listener <string> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 2 `；EOL ` RVA 0x3463D6A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the transport。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9f474f72af6c782b](../../evidence/parameters-sets-012.md#p-9f474f72af6c782b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-018798

```text
(exec)# do-exec test wsma max-priv-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 4 `；EOL ` RVA 0x3463D960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enforce max priv or not。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d3faea102e025dae](../../evidence/parameters-sets-016.md#p-d3faea102e025dae) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-014636

```text
(exec)# do-exec test wsma summary <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 3 `；EOL ` RVA 0x3463D390 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017253

```text
(exec)# do-exec test x25 dbit <number:0..1000> <cr>
```

Handler ` RVA 0x1061D5B0 `；selector ` 0 `；EOL ` RVA 0x34BD4DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` D-bit interval (packets)。

[条件 C-24513ddd0c676292](../../evidence/conditions-sets-014.md#c-24513ddd0c676292) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f4144dc0d3cc9c91](../../evidence/parameters-sets-018.md#p-f4144dc0d3cc9c91) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017634

```text
(exec)# do-exec test xdr create-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7830 `；selector ` 0 `；EOL ` RVA 0x34CFDE40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` ID of test stream to create。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d155c8fe88eef6d1](../../evidence/parameters-sets-016.md#p-d155c8fe88eef6d1) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017613

```text
(exec)# do-exec test xdr destroy-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7890 `；selector ` 0 `；EOL ` RVA 0x34CFDB50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` ID of test stream to destroy。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c2413738ef352aaf](../../evidence/parameters-sets-015.md#p-c2413738ef352aaf) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013572

```text
(exec)# do-exec test xdr disable <cr>
```

Handler ` RVA 0x10C75EA0 `；selector ` 0 `；EOL ` RVA 0x34CF46D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-88f99a190082320b](../../evidence/conditions-sets-053.md#c-88f99a190082320b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013573

```text
(exec)# do-exec test xdr enable <cr>
```

Handler ` RVA 0x10C75E20 `；selector ` 0 `；EOL ` RVA 0x34CF4988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e4c3b7ef72defc89](../../evidence/conditions-sets-088.md#c-e4c3b7ef72defc89) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023913

```text
(exec)# do-exec test xdr fragment <number:1..1000000> to_slots High-queue <cr>
```

Handler ` RVA 0x10CA78F0 `；selector ` 0 `；EOL ` RVA 0x34CFEF00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` fragment size (in Bytes)。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7258ec243930115d](../../evidence/parameters-sets-009.md#p-7258ec243930115d) · [状态效果 S-94ff783c875ee954](../../evidence/state_effects-sets-032.md#s-94ff783c875ee954)

### path-023781

```text
(exec)# do-exec test xdr ping to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA7E20 `；selector ` 0 `；EOL ` RVA 0x34CFD028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b75cb2e4c5728f3a](../../evidence/parameters-sets-014.md#p-b75cb2e4c5728f3a) · [状态效果 S-3a1ddd10e3d473e9](../../evidence/state_effects-sets-013.md#s-3a1ddd10e3d473e9)

### path-017674

```text
(exec)# do-exec test xdr push start <cr>
```

Handler ` RVA 0x10CA7B40 `；selector ` 0 `；EOL ` RVA 0x34CFE3D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-025212

```text
(exec)# do-exec test xdr push stream <number:1..20> count <number:0..200000> to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA75D0 `；selector ` 0 `；EOL ` RVA 0x34CFE818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-92fc2dc68416fcec](../../evidence/parameters-sets-011.md#p-92fc2dc68416fcec) · [状态效果 S-05e8f3865a6693d0](../../evidence/state_effects-sets-002.md#s-05e8f3865a6693d0)

### path-013703

```text
(exec)# do-exec test xdr show-streams <cr>
```

Handler ` RVA 0x10CA76F0 `；selector ` 0 `；EOL ` RVA 0x34CFE0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-017596

```text
(exec)# do-exec test xdr split allow <cr>
```

Handler ` RVA 0x10CA7D50 `；selector ` 0 `；EOL ` RVA 0x34CFD7F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4f92ce86913c4d91](../../evidence/state_effects-sets-017.md#s-4f92ce86913c4d91)

### path-025011

```text
(exec)# do-exec test xdr statistics client test-stats-1 create <number:1..1000000> <number:1..6000> <cr>
```

Handler ` RVA 0xB315AB0 `；selector ` 0 `；EOL ` RVA 0x33737890 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Num counters for this client；` unsigned_number ` Update interval for this client (s)。

[条件 C-9e8d2f8ada02ca9c](../../evidence/conditions-sets-061.md#c-9e8d2f8ada02ca9c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-022205fef7e7929e](../../evidence/parameters-sets-001.md#p-022205fef7e7929e) · [状态效果 S-928ae4ada456afff](../../evidence/state_effects-sets-031.md#s-928ae4ada456afff)

### path-023825

```text
(exec)# do-exec test xdr statistics client test-stats-1 req-stats <cr>
```

Handler ` RVA 0xB2B2B70 `；selector ` 0 `；EOL ` RVA 0x3372F4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-55f1bb7516490603](../../evidence/conditions-sets-034.md#c-55f1bb7516490603) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e9be7afa9825a3e4](../../evidence/state_effects-sets-049.md#s-e9be7afa9825a3e4)

### path-023846

```text
(exec)# do-exec test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB3157E0 `；selector ` 0 `；EOL ` RVA 0x33737E18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e8d2f8ada02ca9c](../../evidence/conditions-sets-061.md#c-9e8d2f8ada02ca9c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fe8a00d85da513a0](../../evidence/state_effects-sets-054.md#s-fe8a00d85da513a0)

### path-023867

```text
(exec)# do-exec test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB2B2770 `；selector ` 0 `；EOL ` RVA 0x3372FCE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-55f1bb7516490603](../../evidence/conditions-sets-034.md#c-55f1bb7516490603) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e3f6fd3e26247bca](../../evidence/state_effects-sets-048.md#s-e3f6fd3e26247bca)

### path-021587

```text
(exec)# do-exec test xdr statistics selftest <number:0..64> <cr>
```

Handler ` RVA 0xB2B3280 `；selector ` 0 `；EOL ` RVA 0x33730148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` slot_id。

[条件 C-6c74c69bb8bd70de](../../evidence/conditions-sets-042.md#c-6c74c69bb8bd70de) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a26de8620aef734b](../../evidence/parameters-sets-012.md#p-a26de8620aef734b) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012595

```text
(exec)# do-exec test xtf-policy-shim <cr>
```

Handler ` RVA 0x128866D0 `；selector ` 0 `；EOL ` RVA 0x358F6488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012244

```text
(exec)# do-exec traceroute <cr>
```

Handler ` RVA 0xE00FAA0 `；selector ` 0 `；EOL ` RVA 0x3415C008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e14ec55b45eaf509](../../evidence/conditions-sets-087.md#c-e14ec55b45eaf509) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023439

```text
(exec)# do-exec traceroute ethernet <address> domain <string> port <cr>
```

Handler ` RVA 0xBD664C0 `；selector ` 0 `；EOL ` RVA 0x338E2680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Remote Maintenance Point MAC Address；` string ` maintenance domain name。

[条件 C-929c3c6ad592ed8c](../../evidence/conditions-sets-057.md#c-929c3c6ad592ed8c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-938128e39050e564](../../evidence/parameters-sets-011.md#p-938128e39050e564) · [状态效果 S-daccc04e6e683ae1](../../evidence/state_effects-sets-046.md#s-daccc04e6e683ae1)

### path-012275

```text
(exec)# do-exec trigger <string> <cr>
```

Handler ` RVA 0xDF79070 `；selector ` 0 `；EOL ` RVA 0x340B8D08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trigger identifier for the trigger to be created or executed。

[条件 C-dba12bc9c2f286c9](../../evidence/conditions-sets-085.md#c-dba12bc9c2f286c9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8105354b13a9d4eb](../../evidence/parameters-sets-010.md#p-8105354b13a9d4eb) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012436

```text
(exec)# do-exec tunnel <string> <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33D2A1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Address or hostname of a remote system。

[条件 C-30b0899d435cd28f](../../evidence/conditions-sets-019.md#c-30b0899d435cd28f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4279d2faf8428569](../../evidence/parameters-sets-006.md#p-4279d2faf8428569) · [状态效果 S-8aae32d087724e9f](../../evidence/state_effects-sets-029.md#s-8aae32d087724e9f)

### path-012951

```text
(exec)# do-exec undebug ACM all <cr>
```

Handler ` RVA 0xDEDBDB0 `；selector ` 0 `；EOL ` RVA 0x34096D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-04a540f29f717c3a](../../evidence/state_effects-sets-001.md#s-04a540f29f717c3a)

### path-012926

```text
(exec)# do-exec undebug ACM error <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 1 `；EOL ` RVA 0x340967E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-04a540f29f717c3a](../../evidence/state_effects-sets-001.md#s-04a540f29f717c3a)

### path-012937

```text
(exec)# do-exec undebug ACM event <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 0 `；EOL ` RVA 0x34096A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-04a540f29f717c3a](../../evidence/state_effects-sets-001.md#s-04a540f29f717c3a)

### path-015833

```text
(exec)# do-exec undebug LDAP all <cr>
```

Handler ` RVA 0x11AC30E0 `；selector ` 0 `；EOL ` RVA 0x3560CAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5fb14ca4de4ef854](../../evidence/state_effects-sets-021.md#s-5fb14ca4de4ef854)

### path-015797

```text
(exec)# do-exec undebug LDAP error <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 1 `；EOL ` RVA 0x3560C2C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5fb14ca4de4ef854](../../evidence/state_effects-sets-021.md#s-5fb14ca4de4ef854)

### path-015810

```text
(exec)# do-exec undebug LDAP event <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 0 `；EOL ` RVA 0x3560C568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5fb14ca4de4ef854](../../evidence/state_effects-sets-021.md#s-5fb14ca4de4ef854)

### path-015822

```text
(exec)# do-exec undebug LDAP legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3560C810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5fb14ca4de4ef854](../../evidence/state_effects-sets-021.md#s-5fb14ca4de4ef854)

### path-015785

```text
(exec)# do-exec undebug LDAP packet <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 2 `；EOL ` RVA 0x3560C018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5fb14ca4de4ef854](../../evidence/state_effects-sets-021.md#s-5fb14ca4de4ef854)

### path-013220

```text
(exec)# do-exec undebug aaa accounting <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 16 `；EOL ` RVA 0x341B80C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013235

```text
(exec)# do-exec undebug aaa administrative <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 17 `；EOL ` RVA 0x341B8368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013547

```text
(exec)# do-exec undebug aaa api <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 35 `；EOL ` RVA 0x341BC6A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017424

```text
(exec)# do-exec undebug aaa api attr <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 36 `；EOL ` RVA 0x341BC680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013525

```text
(exec)# do-exec undebug aaa attr <cr>
```

Handler ` RVA 0xDD3A410 `；selector ` 26 `；EOL ` RVA 0x341BB120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017345

```text
(exec)# do-exec undebug aaa attr add <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 30 `；EOL ` RVA 0x341BABA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017323

```text
(exec)# do-exec undebug aaa attr alloc-free <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 31 `；EOL ` RVA 0x341BA900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017294

```text
(exec)# do-exec undebug aaa attr error <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 32 `；EOL ` RVA 0x341BA658 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017271

```text
(exec)# do-exec undebug aaa attr handle <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 27 `；EOL ` RVA 0x341BA3B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017391

```text
(exec)# do-exec undebug aaa attr info <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 28 `；EOL ` RVA 0x341BB0F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017366

```text
(exec)# do-exec undebug aaa attr update <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 29 `；EOL ` RVA 0x341BAE50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013187

```text
(exec)# do-exec undebug aaa authentication <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 12 `；EOL ` RVA 0x341B7B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013205

```text
(exec)# do-exec undebug aaa authorization <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 15 `；EOL ` RVA 0x341B7E18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013252

```text
(exec)# do-exec undebug aaa boundary <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 56 `；EOL ` RVA 0x341B8610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017007

```text
(exec)# do-exec undebug aaa cache filterserver <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 50 `；EOL ` RVA 0x341B7040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017028

```text
(exec)# do-exec undebug aaa cache group <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 51 `；EOL ` RVA 0x341B72E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013272

```text
(exec)# do-exec undebug aaa cca <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 57 `；EOL ` RVA 0x341B88B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013365

```text
(exec)# do-exec undebug aaa coa <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 25 `；EOL ` RVA 0x341B98A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013622

```text
(exec)# do-exec undebug aaa common-criteria <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 55 `；EOL ` RVA 0x341BD9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-179869b93942c777](../../evidence/conditions-sets-009.md#c-179869b93942c777) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013473

```text
(exec)# do-exec undebug aaa db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 38 `；EOL ` RVA 0x341BBB78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017462

```text
(exec)# do-exec undebug aaa dead-criteria transaction <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 42 `；EOL ` RVA 0x341BD188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013633

```text
(exec)# do-exec undebug aaa green <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 69 `；EOL ` RVA 0x341BDC90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-198ff8ab84026fa0](../../evidence/conditions-sets-010.md#c-198ff8ab84026fa0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013509

```text
(exec)# do-exec undebug aaa id <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 37 `；EOL ` RVA 0x341BC0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013438

```text
(exec)# do-exec undebug aaa ipc <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 33 `；EOL ` RVA 0x341BB628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013415

```text
(exec)# do-exec undebug aaa memory <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 13 `；EOL ` RVA 0x341BA0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013302

```text
(exec)# do-exec undebug aaa mlist-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 44 `；EOL ` RVA 0x341B8E08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013597

```text
(exec)# do-exec undebug aaa mlist-state <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 45 `；EOL ` RVA 0x341BD6C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013350

```text
(exec)# do-exec undebug aaa per-user <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 18 `；EOL ` RVA 0x341B9600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013382

```text
(exec)# do-exec undebug aaa pod <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 24 `；EOL ` RVA 0x341B9B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017037

```text
(exec)# do-exec undebug aaa profile db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 52 `；EOL ` RVA 0x341B78E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017442

```text
(exec)# do-exec undebug aaa protocol local <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 40 `；EOL ` RVA 0x341BCBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017465

```text
(exec)# do-exec undebug aaa protocol radius <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 41 `；EOL ` RVA 0x341BCE88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013396

```text
(exec)# do-exec undebug aaa proxy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 23 `；EOL ` RVA 0x341B9DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013634

```text
(exec)# do-exec undebug aaa redundancy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 54 `；EOL ` RVA 0x341BDF38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-8acdae59c3d89d4d](../../evidence/conditions-sets-054.md#c-8acdae59c3d89d4d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013337

```text
(exec)# do-exec undebug aaa server-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 46 `；EOL ` RVA 0x341B9358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013317

```text
(exec)# do-exec undebug aaa sg-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 47 `；EOL ` RVA 0x341B90B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013287

```text
(exec)# do-exec undebug aaa sg-server-selection <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 48 `；EOL ` RVA 0x341B8B60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017026

```text
(exec)# do-exec undebug aaa subscriber profile <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 53 `；EOL ` RVA 0x341B75E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013453

```text
(exec)# do-exec undebug aaa subsys <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 34 `；EOL ` RVA 0x341BB8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013582

```text
(exec)# do-exec undebug aaa testing <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 43 `；EOL ` RVA 0x341BD418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-017027

```text
(exec)# do-exec undebug aaa tools memleak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35C0DA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f9c237e8e402fff7](../../evidence/state_effects-sets-053.md#s-f9c237e8e402fff7)

### path-013523

```text
(exec)# do-exec undebug aaa traceback <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 14 `；EOL ` RVA 0x341BC370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-013491

```text
(exec)# do-exec undebug aaa userdb <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 39 `；EOL ` RVA 0x341BBE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-de16adc7d8264aa4](../../evidence/state_effects-sets-047.md#s-de16adc7d8264aa4)

### path-012747

```text
(exec)# do-exec undebug access-expression <cr>
```

Handler ` RVA 0xF2A3970 `；selector ` 0 `；EOL ` RVA 0x345E4A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8fe8d45cddfc1f71](../../evidence/state_effects-sets-031.md#s-8fe8d45cddfc1f71)

### path-016016

```text
(exec)# do-exec undebug access-session all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 4 `；EOL ` RVA 0x33BAEA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d213197f6d2fe2e0](../../evidence/conditions-sets-081.md#c-d213197f6d2fe2e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-39167546f48e7101](../../evidence/state_effects-sets-013.md#s-39167546f48e7101)

### path-016007

```text
(exec)# do-exec undebug access-session detail <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 2 `；EOL ` RVA 0x33BAE7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d213197f6d2fe2e0](../../evidence/conditions-sets-081.md#c-d213197f6d2fe2e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-39167546f48e7101](../../evidence/state_effects-sets-013.md#s-39167546f48e7101)

### path-015992

```text
(exec)# do-exec undebug access-session errors <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 0 `；EOL ` RVA 0x33BAE258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d213197f6d2fe2e0](../../evidence/conditions-sets-081.md#c-d213197f6d2fe2e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-39167546f48e7101](../../evidence/state_effects-sets-013.md#s-39167546f48e7101)

### path-016000

```text
(exec)# do-exec undebug access-session events <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 1 `；EOL ` RVA 0x33BAE500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d213197f6d2fe2e0](../../evidence/conditions-sets-081.md#c-d213197f6d2fe2e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-39167546f48e7101](../../evidence/state_effects-sets-013.md#s-39167546f48e7101)

### path-020146

```text
(exec)# do-exec undebug access-session feature all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 5 `；EOL ` RVA 0x33BAF118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d213197f6d2fe2e0](../../evidence/conditions-sets-081.md#c-d213197f6d2fe2e0) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-39167546f48e7101](../../evidence/state_effects-sets-013.md#s-39167546f48e7101)

### path-020219

```text
(exec)# do-exec undebug access-session rcl_server all <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 3 `；EOL ` RVA 0x33BAD888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-78917b02c5b173ec](../../evidence/conditions-sets-047.md#c-78917b02c5b173ec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-898eafa35178970b](../../evidence/state_effects-sets-029.md#s-898eafa35178970b)

### path-020214

```text
(exec)# do-exec undebug access-session rcl_server detail <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 2 `；EOL ` RVA 0x33BAD5E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-78917b02c5b173ec](../../evidence/conditions-sets-047.md#c-78917b02c5b173ec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-898eafa35178970b](../../evidence/state_effects-sets-029.md#s-898eafa35178970b)

### path-020208

```text
(exec)# do-exec undebug access-session rcl_server error <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 0 `；EOL ` RVA 0x33BAD338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-78917b02c5b173ec](../../evidence/conditions-sets-047.md#c-78917b02c5b173ec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-898eafa35178970b](../../evidence/state_effects-sets-029.md#s-898eafa35178970b)

### path-020199

```text
(exec)# do-exec undebug access-session rcl_server event <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 1 `；EOL ` RVA 0x33BAD090 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-78917b02c5b173ec](../../evidence/conditions-sets-047.md#c-78917b02c5b173ec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-898eafa35178970b](../../evidence/state_effects-sets-029.md#s-898eafa35178970b)

### path-016033

```text
(exec)# do-exec undebug access-session sync <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 3 `；EOL ` RVA 0x33BAED38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-78917b02c5b173ec](../../evidence/conditions-sets-047.md#c-78917b02c5b173ec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-39167546f48e7101](../../evidence/state_effects-sets-013.md#s-39167546f48e7101)

### path-018015

```text
(exec)# do-exec undebug acl cca error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3447D290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d32a9bc32302aa2b](../../evidence/state_effects-sets-045.md#s-d32a9bc32302aa2b)

### path-018032

```text
(exec)# do-exec undebug acl cca event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3447D538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d32a9bc32302aa2b](../../evidence/state_effects-sets-045.md#s-d32a9bc32302aa2b)

### path-012526

```text
(exec)# do-exec undebug adjacency <cr>
```

Handler ` RVA 0xB559CD0 `；selector ` 0 `；EOL ` RVA 0x3379B6B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c6d69296f92bba73](../../evidence/conditions-sets-077.md#c-c6d69296f92bba73) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e37673d079cf6843](../../evidence/state_effects-sets-048.md#s-e37673d079cf6843)

### path-013839

```text
(exec)# do-exec undebug alg all <cr>
```

Handler ` RVA 0xCD3BF50 `；selector ` 1 `；EOL ` RVA 0x33CD4910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-77d28278bfac1c96](../../evidence/state_effects-sets-025.md#s-77d28278bfac1c96)

### path-013895

```text
(exec)# do-exec undebug alg info <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD5108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-77d28278bfac1c96](../../evidence/state_effects-sets-025.md#s-77d28278bfac1c96)

### path-013880

```text
(exec)# do-exec undebug alg trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD4E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-77d28278bfac1c96](../../evidence/state_effects-sets-025.md#s-77d28278bfac1c96)

### path-013861

```text
(exec)# do-exec undebug alg warn <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CD4BB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-77d28278bfac1c96](../../evidence/state_effects-sets-025.md#s-77d28278bfac1c96)

### path-012301

```text
(exec)# do-exec undebug all <cr>
```

Handler ` RVA 0xE002630 `；selector ` 0 `；EOL ` RVA 0x34121818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-020456

```text
(exec)# do-exec undebug alps ascu event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 3 `；EOL ` RVA 0x3541C160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-55bcd9f5396d3d0a](../../evidence/conditions-sets-034.md#c-55bcd9f5396d3d0a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9a5327367f33ff38](../../evidence/state_effects-sets-033.md#s-9a5327367f33ff38)

### path-020428

```text
(exec)# do-exec undebug alps circuit event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 2 `；EOL ` RVA 0x3541BCD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7a5835a83e59b06e](../../evidence/state_effects-sets-026.md#s-7a5835a83e59b06e)

### path-020429

```text
(exec)# do-exec undebug alps peer event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 1 `；EOL ` RVA 0x3541B960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ec56ebeafac8e39d](../../evidence/state_effects-sets-050.md#s-ec56ebeafac8e39d)

### path-016315

```text
(exec)# do-exec undebug alps snmp <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 4 `；EOL ` RVA 0x3541C6A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015607

```text
(exec)# do-exec undebug analyze memory-leak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x341F0BE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-f91cbebe6e08d199](../../evidence/conditions-sets-096.md#c-f91cbebe6e08d199) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-311933826def7513](../../evidence/state_effects-sets-011.md#s-311933826def7513)

### path-013626

```text
(exec)# do-exec undebug ancp adjacency <cr>
```

Handler ` RVA 0xB258990 `；selector ` 0 `；EOL ` RVA 0x336D7DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-29131bf24112be74](../../evidence/state_effects-sets-009.md#s-29131bf24112be74)

### path-015441

```text
(exec)# do-exec undebug application db <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 7 `；EOL ` RVA 0x358DCD80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015464

```text
(exec)# do-exec undebug application detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 2 `；EOL ` RVA 0x358DD028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015414

```text
(exec)# do-exec undebug application event <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 5 `；EOL ` RVA 0x358DC578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015529

```text
(exec)# do-exec undebug application ha <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 8 `；EOL ` RVA 0x358DD660 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-019756

```text
(exec)# do-exec undebug application ha detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 9 `；EOL ` RVA 0x358DD638 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-022809

```text
(exec)# do-exec undebug application route <address> <address> <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 1 `；EOL ` RVA 0x358DD378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` Destination prefix；` address ` Destination prefix mask。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3fadc80999e697ce](../../evidence/parameters-sets-005.md#p-3fadc80999e697ce) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015444

```text
(exec)# do-exec undebug application rwatch <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 3 `；EOL ` RVA 0x358DC8B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-019704

```text
(exec)# do-exec undebug application rwatch rib <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 4 `；EOL ` RVA 0x358DC888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015403

```text
(exec)# do-exec undebug application summary <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 6 `；EOL ` RVA 0x358DC2D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-020212

```text
(exec)# do-exec undebug archive config differences <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-53c81f7971d7e870](../../evidence/state_effects-sets-018.md#s-53c81f7971d7e870)

### path-020223

```text
(exec)# do-exec undebug archive config ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ad51bf5a7ba87d9d](../../evidence/state_effects-sets-037.md#s-ad51bf5a7ba87d9d)

### path-020217

```text
(exec)# do-exec undebug archive config timestamp <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D318 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3b7272f83c7f87](../../evidence/state_effects-sets-053.md#s-fb3b7272f83c7f87)

### path-023088

```text
(exec)# do-exec undebug archive log config persistent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3409A520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f7397e0be9c8927e](../../evidence/state_effects-sets-052.md#s-f7397e0be9c8927e)

### path-016084

```text
(exec)# do-exec undebug archive versioning <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 0 `；EOL ` RVA 0x3409CB40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f608e5a5ad42fd95](../../evidence/state_effects-sets-052.md#s-f608e5a5ad42fd95)

### path-020206

```text
(exec)# do-exec undebug archive versioning ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 0 `；EOL ` RVA 0x3409CB18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bb2c678c737a52c4](../../evidence/state_effects-sets-040.md#s-bb2c678c737a52c4)

### path-012449

```text
(exec)# do-exec undebug arp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CDA618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-4b0aae330b573300](../../evidence/conditions-sets-029.md#c-4b0aae330b573300) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013011

```text
(exec)# do-exec undebug arp adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD8580 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013033

```text
(exec)# do-exec undebug arp application <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD8828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013189

```text
(exec)# do-exec undebug arp database <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33CD9D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013054

```text
(exec)# do-exec undebug arp dynamic <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x33CD8AD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013161

```text
(exec)# do-exec undebug arp error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 13 `；EOL ` RVA 0x33CD9818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013075

```text
(exec)# do-exec undebug arp ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x33CD8D78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013097

```text
(exec)# do-exec undebug arp interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33CD9020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013239

```text
(exec)# do-exec undebug arp retry <cr>
```

Handler ` RVA 0xE002120 `；selector ` 12 `；EOL ` RVA 0x33CDA2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d63fe8dad8228058](../../evidence/conditions-sets-083.md#c-d63fe8dad8228058) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013125

```text
(exec)# do-exec undebug arp static <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33CD92C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013147

```text
(exec)# do-exec undebug arp subblocking <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33CD9570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013177

```text
(exec)# do-exec undebug arp table <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33CD9AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-013207

```text
(exec)# do-exec undebug arp timer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33CDA010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e72234839a0f3b74](../../evidence/state_effects-sets-049.md#s-e72234839a0f3b74)

### path-016545

```text
(exec)# do-exec undebug aspp event <cr>
```

Handler ` RVA 0x113A0AC0 `；selector ` 0 `；EOL ` RVA 0x354A3338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7165c33256d0b0b8](../../evidence/state_effects-sets-024.md#s-7165c33256d0b0b8)

### path-016564

```text
(exec)# do-exec undebug aspp packet <cr>
```

Handler ` RVA 0x113A0AC0 `；selector ` 1 `；EOL ` RVA 0x354A3668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7165c33256d0b0b8](../../evidence/state_effects-sets-024.md#s-7165c33256d0b0b8)

### path-015225

```text
(exec)# do-exec undebug async async-queue <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34935440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-73c998cc952a162b](../../evidence/state_effects-sets-025.md#s-73c998cc952a162b)

### path-015173

```text
(exec)# do-exec undebug async framing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34934C48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-73c998cc952a162b](../../evidence/state_effects-sets-025.md#s-73c998cc952a162b)

### path-015191

```text
(exec)# do-exec undebug async packet <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34934EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-73c998cc952a162b](../../evidence/state_effects-sets-025.md#s-73c998cc952a162b)

### path-015210

```text
(exec)# do-exec undebug async state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34935198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-73c998cc952a162b](../../evidence/state_effects-sets-025.md#s-73c998cc952a162b)

### path-015035

```text
(exec)# do-exec undebug atm ilmi <cr>
```

Handler ` RVA 0xCCCAC00 `；selector ` 24 `；EOL ` RVA 0x33C52E30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b2b561f747a737b3](../../evidence/conditions-sets-069.md#c-b2b561f747a737b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-019409

```text
(exec)# do-exec undebug atm ilmi red <cr>
```

Handler ` RVA 0xCCCAC00 `；selector ` 29 `；EOL ` RVA 0x33C530D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b2b561f747a737b3](../../evidence/conditions-sets-069.md#c-b2b561f747a737b3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-012781

```text
(exec)# do-exec undebug atomic-config <cr>
```

Handler ` RVA 0x165754F0 `；selector ` 0 `；EOL ` RVA 0x35FA2C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-f18347b1d2aef086](../../evidence/conditions-sets-093.md#c-f18347b1d2aef086) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-015458

```text
(exec)# do-exec undebug autoip event <cr>
```

Handler ` RVA 0xB286740 `；selector ` 0 `；EOL ` RVA 0x3372B5B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cb5a4a603e0941d3](../../evidence/state_effects-sets-043.md#s-cb5a4a603e0941d3)

### path-012433

```text
(exec)# do-exec undebug backup <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34481E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ac18de5e4a306d1d](../../evidence/state_effects-sets-036.md#s-ac18de5e4a306d1d)

### path-015671

```text
(exec)# do-exec undebug beep concurrency <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 3 `；EOL ` RVA 0x3448B2A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c800164d199af0cc](../../evidence/conditions-sets-077.md#c-c800164d199af0cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f137ad7a8cc7cec9](../../evidence/state_effects-sets-051.md#s-f137ad7a8cc7cec9)

### path-015706

```text
(exec)# do-exec undebug beep profile <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 1 `；EOL ` RVA 0x3448B950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c800164d199af0cc](../../evidence/conditions-sets-077.md#c-c800164d199af0cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f137ad7a8cc7cec9](../../evidence/state_effects-sets-051.md#s-f137ad7a8cc7cec9)

### path-015718

```text
(exec)# do-exec undebug beep session <cr>
```

Handler ` RVA 0xEF60830 `；selector ` 2 `；EOL ` RVA 0x3448B5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-6dd9b56d49bf1aaa](../../evidence/conditions-sets-042.md#c-6dd9b56d49bf1aaa) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f137ad7a8cc7cec9](../../evidence/state_effects-sets-051.md#s-f137ad7a8cc7cec9)

### path-014333

```text
(exec)# do-exec undebug bfd dampening <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 3 `；EOL ` RVA 0x34CAD060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-014389

```text
(exec)# do-exec undebug bfd event <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 1 `；EOL ` RVA 0x34CAC8B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b63851fd03b40697](../../evidence/state_effects-sets-039.md#s-b63851fd03b40697)

### path-014294

```text
(exec)# do-exec undebug bfd ha <cr>
```

Handler ` RVA 0x10B663D0 `；selector ` 0 `；EOL ` RVA 0x34CBEF70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a10be9bfc9fad242](../../evidence/state_effects-sets-034.md#s-a10be9bfc9fad242)

### path-014376

```text
(exec)# do-exec undebug bfd packet <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 0 `；EOL ` RVA 0x34CAC2A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-10701656fa1b0291](../../evidence/state_effects-sets-004.md#s-10701656fa1b0291)

### path-014311

```text
(exec)# do-exec undebug bfd stub <cr>
```

Handler ` RVA 0x10B3D630 `；selector ` 2 `；EOL ` RVA 0x34CACDB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-019042

```text
(exec)# do-exec undebug bgp telemetry enable <cr>
```

Handler ` RVA 0xF047BD0 `；selector ` 1 `；EOL ` RVA 0x344F9690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d680ae433447c28f](../../evidence/state_effects-sets-045.md#s-d680ae433447c28f)

### path-014984

```text
(exec)# do-exec undebug bidb errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 67 `；EOL ` RVA 0x33BF93F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-51d66036d279c926](../../evidence/state_effects-sets-018.md#s-51d66036d279c926)

### path-014971

```text
(exec)# do-exec undebug bidb events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 66 `；EOL ` RVA 0x33BF9150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-51d66036d279c926](../../evidence/state_effects-sets-018.md#s-51d66036d279c926)

### path-015000

```text
(exec)# do-exec undebug bidb verbose <cr>
```

Handler ` RVA 0xE002120 `；selector ` 68 `；EOL ` RVA 0x33BF96A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-51d66036d279c926](../../evidence/state_effects-sets-018.md#s-51d66036d279c926)

### path-012684

```text
(exec)# do-exec undebug bing <cr>
```

Handler ` RVA 0xF277B80 `；selector ` 0 `；EOL ` RVA 0x345DE0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-175bf21506ea2010](../../evidence/state_effects-sets-005.md#s-175bf21506ea2010)

### path-015672

```text
(exec)# do-exec undebug bing detail <cr>
```

Handler ` RVA 0xF277B80 `；selector ` 1 `；EOL ` RVA 0x345DE0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-175bf21506ea2010](../../evidence/state_effects-sets-005.md#s-175bf21506ea2010)

### path-017654

```text
(exec)# do-exec undebug bridge-domain client api <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x33950710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017630

```text
(exec)# do-exec undebug bridge-domain client errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x33950468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-013698

```text
(exec)# do-exec undebug bridge-domain configuration <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x339509A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-013713

```text
(exec)# do-exec undebug bridge-domain errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33950C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-013728

```text
(exec)# do-exec undebug bridge-domain ipc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33950EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017758

```text
(exec)# do-exec undebug bridge-domain l2fib errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x339522E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-942d1030078d3fe5](../../evidence/conditions-sets-057.md#c-942d1030078d3fe5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017739

```text
(exec)# do-exec undebug bridge-domain l2fib events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x33952040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-942d1030078d3fe5](../../evidence/conditions-sets-057.md#c-942d1030078d3fe5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-013743

```text
(exec)# do-exec undebug bridge-domain linkfault <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x339511A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017742

```text
(exec)# do-exec undebug bridge-domain route errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x33951798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3af045e7e6a0d9c1](../../evidence/conditions-sets-023.md#c-3af045e7e6a0d9c1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017724

```text
(exec)# do-exec undebug bridge-domain route events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x339514F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3af045e7e6a0d9c1](../../evidence/conditions-sets-023.md#c-3af045e7e6a0d9c1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017775

```text
(exec)# do-exec undebug bridge-domain route flow-control <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x33951CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3af045e7e6a0d9c1](../../evidence/conditions-sets-023.md#c-3af045e7e6a0d9c1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-017761

```text
(exec)# do-exec undebug bridge-domain route messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33951A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3af045e7e6a0d9c1](../../evidence/conditions-sets-023.md#c-3af045e7e6a0d9c1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5d09339ae8ee0b2e](../../evidence/state_effects-sets-020.md#s-5d09339ae8ee0b2e)

### path-016334

```text
(exec)# do-exec undebug bsc diagnostic <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 2 `；EOL ` RVA 0x354B4EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c1d6bfc04655b7b8](../../evidence/state_effects-sets-041.md#s-c1d6bfc04655b7b8)

### path-016341

```text
(exec)# do-exec undebug bsc event <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 0 `；EOL ` RVA 0x354B51E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c1d6bfc04655b7b8](../../evidence/state_effects-sets-041.md#s-c1d6bfc04655b7b8)

### path-016356

```text
(exec)# do-exec undebug bsc packet <cr>
```

Handler ` RVA 0x113C3860 `；selector ` 1 `；EOL ` RVA 0x354B5510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c1d6bfc04655b7b8](../../evidence/state_effects-sets-041.md#s-c1d6bfc04655b7b8)

### path-016340

```text
(exec)# do-exec undebug bstun event <cr>
```

Handler ` RVA 0x113E6740 `；selector ` 1 `；EOL ` RVA 0x354BBF48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c25c78c01f860567](../../evidence/state_effects-sets-041.md#s-c25c78c01f860567)

### path-016355

```text
(exec)# do-exec undebug bstun packet <cr>
```

Handler ` RVA 0x113E6740 `；selector ` 2 `；EOL ` RVA 0x354BC278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c25c78c01f860567](../../evidence/state_effects-sets-041.md#s-c25c78c01f860567)

### path-012745

```text
(exec)# do-exec undebug buffer <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x342BC530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86c1df744520e837](../../evidence/state_effects-sets-029.md#s-86c1df744520e837)

### path-016128

```text
(exec)# do-exec undebug buffer failures <cr>
```

Handler ` RVA 0xE002120 `；selector ` 22 `；EOL ` RVA 0x342BC508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86c1df744520e837](../../evidence/state_effects-sets-029.md#s-86c1df744520e837)

### path-020563

```text
(exec)# do-exec undebug bulkstat client all <cr>
```

Handler ` RVA 0xBC6CE30 `；selector ` 2 `；EOL ` RVA 0x33888E78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-020545

```text
(exec)# do-exec undebug bulkstat client error <cr>
```

Handler ` RVA 0xBC6CCA0 `；selector ` 0 `；EOL ` RVA 0x33888908 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1302b8d529ae3a48](../../evidence/state_effects-sets-004.md#s-1302b8d529ae3a48)

### path-020554

```text
(exec)# do-exec undebug bulkstat client info <cr>
```

Handler ` RVA 0xBC6CCA0 `；selector ` 1 `；EOL ` RVA 0x33888BC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3da317711cd49647](../../evidence/state_effects-sets-014.md#s-3da317711cd49647)

### path-020555

```text
(exec)# do-exec undebug bulkstat file all <cr>
```

Handler ` RVA 0xBC6CE30 `；selector ` 1 `；EOL ` RVA 0x33888620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-020535

```text
(exec)# do-exec undebug bulkstat file error <cr>
```

Handler ` RVA 0xBC6CB70 `；selector ` 0 `；EOL ` RVA 0x338880B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ff90f53e727d39f7](../../evidence/state_effects-sets-054.md#s-ff90f53e727d39f7)

### path-020546

```text
(exec)# do-exec undebug bulkstat file info <cr>
```

Handler ` RVA 0xBC6CB70 `；selector ` 1 `；EOL ` RVA 0x33888368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-92dd813d0daa4d08](../../evidence/state_effects-sets-031.md#s-92dd813d0daa4d08)

### path-020578

```text
(exec)# do-exec undebug bulkstat processing all <cr>
```

Handler ` RVA 0xBC88F60 `；selector ` 0 `；EOL ` RVA 0x338984B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-020573

```text
(exec)# do-exec undebug bulkstat processing error <cr>
```

Handler ` RVA 0xBC88E60 `；selector ` 0 `；EOL ` RVA 0x338981F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-709f1797e629b688](../../evidence/state_effects-sets-024.md#s-709f1797e629b688)

### path-020567

```text
(exec)# do-exec undebug bulkstat processing info <cr>
```

Handler ` RVA 0xBC88E60 `；selector ` 1 `；EOL ` RVA 0x33897F40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8b2ae3ffe5c451e4](../../evidence/state_effects-sets-030.md#s-8b2ae3ffe5c451e4)

### path-014987

```text
(exec)# do-exec undebug caaa accounting <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 4 `；EOL ` RVA 0x33BB3A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-015066

```text
(exec)# do-exec undebug caaa all <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 0 `；EOL ` RVA 0x33BB4A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-015002

```text
(exec)# do-exec undebug caaa authentication <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 2 `；EOL ` RVA 0x33BB3D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-015016

```text
(exec)# do-exec undebug caaa authorization <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 3 `；EOL ` RVA 0x33BB3FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-014963

```text
(exec)# do-exec undebug caaa command-handler <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 6 `；EOL ` RVA 0x33BB3538 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-015030

```text
(exec)# do-exec undebug caaa error <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 1 `；EOL ` RVA 0x33BB4280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-014953

```text
(exec)# do-exec undebug caaa ha <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 7 `；EOL ` RVA 0x33BB3290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-014975

```text
(exec)# do-exec undebug caaa service <cr>
```

Handler ` RVA 0xCB23BA0 `；selector ` 5 `；EOL ` RVA 0x33BB37E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6b3d273e3a0f4d2a](../../evidence/state_effects-sets-023.md#s-6b3d273e3a0f4d2a)

### path-019889

```text
(exec)# do-exec undebug call filter detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3605B290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c9c541cc1ecf8fcf](../../evidence/conditions-sets-078.md#c-c9c541cc1ecf8fcf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6a2db415bbc6410a](../../evidence/state_effects-sets-023.md#s-6a2db415bbc6410a)

### path-019877

```text
(exec)# do-exec undebug call filter inout <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3605AFD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c9c541cc1ecf8fcf](../../evidence/conditions-sets-078.md#c-c9c541cc1ecf8fcf) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c77818e2fde58087](../../evidence/state_effects-sets-042.md#s-c77818e2fde58087)

### path-015921

```text
(exec)# do-exec undebug call-admission elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3408F7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a6ec8b8feba74786](../../evidence/state_effects-sets-035.md#s-a6ec8b8feba74786)

### path-015931

```text
(exec)# do-exec undebug call-admission trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3408FA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a6ec8b8feba74786](../../evidence/state_effects-sets-035.md#s-a6ec8b8feba74786)

### path-013730

```text
(exec)# do-exec undebug call-home all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 14 `；EOL ` RVA 0x337F5370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-013670

```text
(exec)# do-exec undebug call-home detail <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 2 `；EOL ` RVA 0x337F48D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017762

```text
(exec)# do-exec undebug call-home diagnostic-signature action <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 6 `；EOL ` RVA 0x337F61B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017817

```text
(exec)# do-exec undebug call-home diagnostic-signature all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 15 `；EOL ` RVA 0x337F6EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017788

```text
(exec)# do-exec undebug call-home diagnostic-signature api <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 8 `；EOL ` RVA 0x337F6700 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017798

```text
(exec)# do-exec undebug call-home diagnostic-signature cli <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 10 `；EOL ` RVA 0x337F69A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017776

```text
(exec)# do-exec undebug call-home diagnostic-signature download <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 7 `；EOL ` RVA 0x337F6458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017806

```text
(exec)# do-exec undebug call-home diagnostic-signature error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 9 `；EOL ` RVA 0x337F6C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017743

```text
(exec)# do-exec undebug call-home diagnostic-signature event-registration <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 5 `；EOL ` RVA 0x337F5F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017725

```text
(exec)# do-exec undebug call-home diagnostic-signature parsing <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 4 `；EOL ` RVA 0x337F5C60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2272dfeaa5744c90](../../evidence/conditions-sets-013.md#c-2272dfeaa5744c90) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-013700

```text
(exec)# do-exec undebug call-home error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 1 `；EOL ` RVA 0x337F4E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-013683

```text
(exec)# do-exec undebug call-home mail <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 3 `；EOL ` RVA 0x337F4B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-013761

```text
(exec)# do-exec undebug call-home message-content <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 13 `；EOL ` RVA 0x337F56A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-021636

```text
(exec)# do-exec undebug call-home message-content profile <string> <cr>
```

Handler ` RVA 0xB6C71B0 `；selector ` 0 `；EOL ` RVA 0x337F56E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Profile name。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e516ecaeeb5cb103](../../evidence/parameters-sets-017.md#p-e516ecaeeb5cb103) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017774

```text
(exec)# do-exec undebug call-home smart-licensing all <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 16 `；EOL ` RVA 0x337F77A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-1cf5b395f1fcdb5f](../../evidence/conditions-sets-011.md#c-1cf5b395f1fcdb5f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017760

```text
(exec)# do-exec undebug call-home smart-licensing error <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 12 `；EOL ` RVA 0x337F7500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-1cf5b395f1fcdb5f](../../evidence/conditions-sets-011.md#c-1cf5b395f1fcdb5f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-017740

```text
(exec)# do-exec undebug call-home smart-licensing trace <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 11 `；EOL ` RVA 0x337F7258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-1cf5b395f1fcdb5f](../../evidence/conditions-sets-011.md#c-1cf5b395f1fcdb5f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-013716

```text
(exec)# do-exec undebug call-home trace <cr>
```

Handler ` RVA 0xB6C6E20 `；selector ` 0 `；EOL ` RVA 0x337F50C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-78372d39ee933b03](../../evidence/state_effects-sets-026.md#s-78372d39ee933b03)

### path-012685

```text
(exec)# do-exec undebug callback <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x346049D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fa932c0a305a71e5](../../evidence/state_effects-sets-053.md#s-fa932c0a305a71e5)

### path-012366

```text
(exec)# do-exec undebug cca <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33EDDF58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-196bca3b56eb7c8f](../../evidence/state_effects-sets-006.md#s-196bca3b56eb7c8f)

### path-014031

```text
(exec)# do-exec undebug cce cp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x340387A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2efe99927d850108](../../evidence/state_effects-sets-010.md#s-2efe99927d850108)

### path-021822

```text
(exec)# do-exec undebug cce cp filter balance <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34038DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2efe99927d850108](../../evidence/state_effects-sets-010.md#s-2efe99927d850108)

### path-014114

```text
(exec)# do-exec undebug cce cpdp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3403BB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1dd7536f725412a9](../../evidence/state_effects-sets-007.md#s-1dd7536f725412a9)

### path-017998

```text
(exec)# do-exec undebug cce cpdp elog <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3403BB68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1dd7536f725412a9](../../evidence/state_effects-sets-007.md#s-1dd7536f725412a9)

### path-018006

```text
(exec)# do-exec undebug cce cpdp events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3403B698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1dd7536f725412a9](../../evidence/state_effects-sets-007.md#s-1dd7536f725412a9)

### path-021847

```text
(exec)# do-exec undebug cce cpdp events detailed <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3403B670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1dd7536f725412a9](../../evidence/state_effects-sets-007.md#s-1dd7536f725412a9)

### path-014115

```text
(exec)# do-exec undebug cce ha <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CDECF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae06d633c2bb01a5](../../evidence/state_effects-sets-037.md#s-ae06d633c2bb01a5)

### path-017982

```text
(exec)# do-exec undebug cce ha event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CDEA20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae06d633c2bb01a5](../../evidence/state_effects-sets-037.md#s-ae06d633c2bb01a5)

### path-017999

```text
(exec)# do-exec undebug cce ha issu <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CDECC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ae06d633c2bb01a5](../../evidence/state_effects-sets-037.md#s-ae06d633c2bb01a5)

### path-015857

```text
(exec)# do-exec undebug cdapi detail <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x35F0C540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-18556f93a521fe5a](../../evidence/state_effects-sets-006.md#s-18556f93a521fe5a)

### path-015849

```text
(exec)# do-exec undebug cdapi events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35F0C298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-18556f93a521fe5a](../../evidence/state_effects-sets-006.md#s-18556f93a521fe5a)

### path-013894

```text
(exec)# do-exec undebug cdp adjacency <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 2 `；EOL ` RVA 0x33CE0CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-013878

```text
(exec)# do-exec undebug cdp events <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 1 `；EOL ` RVA 0x33CE0A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-013951

```text
(exec)# do-exec undebug cdp ilp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x33CE1760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-013907

```text
(exec)# do-exec undebug cdp ip <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 3 `；EOL ` RVA 0x33CE0F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-013917

```text
(exec)# do-exec undebug cdp location-server <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 4 `；EOL ` RVA 0x33CE1210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-013859

```text
(exec)# do-exec undebug cdp packets <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 0 `；EOL ` RVA 0x33CE0770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-013932

```text
(exec)# do-exec undebug cdp test <cr>
```

Handler ` RVA 0xCDB4000 `；selector ` 5 `；EOL ` RVA 0x33CE14B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fb3bc4eeab970eff](../../evidence/state_effects-sets-053.md#s-fb3bc4eeab970eff)

### path-017664

```text
(exec)# do-exec undebug cef filter fib <cr>
```

Handler ` RVA 0xB384EB0 `；selector ` 0 `；EOL ` RVA 0x337431A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-226a906dd4c702c4](../../evidence/conditions-sets-013.md#c-226a906dd4c702c4) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-021688

```text
(exec)# do-exec undebug cef filter hardware notifications <cr>
```

Handler ` RVA 0xB4F8820 `；selector ` 0 `；EOL ` RVA 0x33743D70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d27e4e123a5ddc59](../../evidence/conditions-sets-081.md#c-d27e4e123a5ddc59) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-017698

```text
(exec)# do-exec undebug cef filter path <cr>
```

Handler ` RVA 0xB422A80 `；selector ` 0 `；EOL ` RVA 0x33742A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-09156bc660596dd3](../../evidence/conditions-sets-004.md#c-09156bc660596dd3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1552cf4b358eab10](../../evidence/state_effects-sets-005.md#s-1552cf4b358eab10)

### path-023792

```text
(exec)# do-exec undebug cef filter subtree context client <cr>
```

Handler ` RVA 0xB4537D0 `；selector ` 0 `；EOL ` RVA 0x33742120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-506088898de2a6e6](../../evidence/conditions-sets-031.md#c-506088898de2a6e6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-017683

```text
(exec)# do-exec undebug cef filter table <cr>
```

Handler ` RVA 0xB45B0A0 `；selector ` 0 `；EOL ` RVA 0x33743680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c657d12afb2385e3](../../evidence/conditions-sets-076.md#c-c657d12afb2385e3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-021563

```text
(exec)# do-exec undebug cef filter uid key <cr>
```

Handler ` RVA 0xB4B72F0 `；selector ` 0 `；EOL ` RVA 0x337424F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-69c768ab9a5c0e41](../../evidence/conditions-sets-041.md#c-69c768ab9a5c0e41) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e66113d76d78bb6e](../../evidence/state_effects-sets-049.md#s-e66113d76d78bb6e)

### path-017694

```text
(exec)# do-exec undebug cef filter vrf <cr>
```

Handler ` RVA 0xB4863B0 `；selector ` 0 `；EOL ` RVA 0x337439F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-8d27fdf7f57e7b02](../../evidence/conditions-sets-055.md#c-8d27fdf7f57e7b02) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-013691

```text
(exec)# do-exec undebug cef table <cr>
```

Handler ` RVA 0xB37CB40 `；selector ` 0 `；EOL ` RVA 0x33744360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-39f7f1da205a5af9](../../evidence/conditions-sets-022.md#c-39f7f1da205a5af9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-07d46cc13a15f5d7](../../evidence/state_effects-sets-002.md#s-07d46cc13a15f5d7)

### path-012367

```text
(exec)# do-exec undebug cfgdiff <cr>
```

Handler ` RVA 0xDFDE3D0 `；selector ` 1 `；EOL ` RVA 0x34113FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-710227b1f9b2a180](../../evidence/state_effects-sets-024.md#s-710227b1f9b2a180)

### path-012959

```text
(exec)# do-exec undebug cfgdiff timestamp <cr>
```

Handler ` RVA 0xDFDE3D0 `；selector ` 2 `；EOL ` RVA 0x34113F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-710227b1f9b2a180](../../evidence/state_effects-sets-024.md#s-710227b1f9b2a180)

### path-012590

```text
(exec)# do-exec undebug cft <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 6 `；EOL ` RVA 0x358FF988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-3cf153fb0af73622](../../evidence/conditions-sets-024.md#c-3cf153fb0af73622) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-014461

```text
(exec)# do-exec undebug cft ager <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 4 `；EOL ` RVA 0x358FEEC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b55e428601917f9a](../../evidence/conditions-sets-070.md#c-b55e428601917f9a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-014508

```text
(exec)# do-exec undebug cft engine <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 0 `；EOL ` RVA 0x358FF410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-6dd854677eb26d58](../../evidence/conditions-sets-042.md#c-6dd854677eb26d58) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-014529

```text
(exec)# do-exec undebug cft fe <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 3 `；EOL ` RVA 0x358FF6B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-210fb24a4c1dead2](../../evidence/conditions-sets-013.md#c-210fb24a4c1dead2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-014440

```text
(exec)# do-exec undebug cft flow <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 5 `；EOL ` RVA 0x358FEC18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-4d0a754f1862ca4d](../../evidence/conditions-sets-030.md#c-4d0a754f1862ca4d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-014548

```text
(exec)# do-exec undebug cft l4 <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 2 `；EOL ` RVA 0x358FF960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-f189bb838cb9df60](../../evidence/conditions-sets-093.md#c-f189bb838cb9df60) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-014484

```text
(exec)# do-exec undebug cft memory <cr>
```

Handler ` RVA 0x1294A410 `；selector ` 1 `；EOL ` RVA 0x358FF168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-79918c30ee53c888](../../evidence/conditions-sets-047.md#c-79918c30ee53c888) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-21605e916a10d4b7](../../evidence/state_effects-sets-008.md#s-21605e916a10d4b7)

### path-012689

```text
(exec)# do-exec undebug chat <cr>
```

Handler ` RVA 0xF2F58D0 `；selector ` 0 `；EOL ` RVA 0x346038B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b58cc52b9f0c7cf](../../evidence/state_effects-sets-016.md#s-4b58cc52b9f0c7cf)

### path-013416

```text
(exec)# do-exec undebug checkpoint timers <cr>
```

Handler ` RVA 0xCDBA680 `；selector ` 0 `；EOL ` RVA 0x33CECC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ffa3c76202fd5721](../../evidence/state_effects-sets-054.md#s-ffa3c76202fd5721)

### path-015321

```text
(exec)# do-exec undebug clns cache <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x34B6DC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-019547

```text
(exec)# do-exec undebug clns esis events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x34B6C768 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-019565

```text
(exec)# do-exec undebug clns esis packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x34B6CA10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015223

```text
(exec)# do-exec undebug clns events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34B6CCA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015303

```text
(exec)# do-exec undebug clns filters <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x34B6D9F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015270

```text
(exec)# do-exec undebug clns igrp-adjacency <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34B6D4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015237

```text
(exec)# do-exec undebug clns igrp-events <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34B6CF50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015257

```text
(exec)# do-exec undebug clns igrp-packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34B6D1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015286

```text
(exec)# do-exec undebug clns packets <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34B6D748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015343

```text
(exec)# do-exec undebug clns routing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34B6DF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9cb7efeb20f6358c](../../evidence/state_effects-sets-033.md#s-9cb7efeb20f6358c)

### path-015295

```text
(exec)# do-exec undebug cls errors <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x354C1F30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-015371

```text
(exec)# do-exec undebug cls flow-control <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x354C29D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-015389

```text
(exec)# do-exec undebug cls hpr <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x354C2C78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-015314

```text
(exec)# do-exec undebug cls messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x354C21D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-015336

```text
(exec)# do-exec undebug cls sdlc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x354C2480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-015278

```text
(exec)# do-exec undebug cls state <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x354C1C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-015355

```text
(exec)# do-exec undebug cls vdlc <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x354C2728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-120df649303be920](../../evidence/state_effects-sets-004.md#s-120df649303be920)

### path-016292

```text
(exec)# do-exec undebug cns aaa <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x340E7338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7377576952b954da](../../evidence/state_effects-sets-025.md#s-7377576952b954da)

### path-016333

```text
(exec)# do-exec undebug cns all <cr>
```

Handler ` RVA 0xDFA8FB0 `；selector ` 0 `；EOL ` RVA 0x340E8680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016255

```text
(exec)# do-exec undebug cns config <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3460F7F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-007a68198d603bf2](../../evidence/state_effects-sets-001.md#s-007a68198d603bf2)

### path-020434

```text
(exec)# do-exec undebug cns config all <cr>
```

Handler ` RVA 0xF314C20 `；selector ` 0 `；EOL ` RVA 0x3460F518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020411

```text
(exec)# do-exec undebug cns config apply <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3460ED20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020420

```text
(exec)# do-exec undebug cns config decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x3460EFC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020398

```text
(exec)# do-exec undebug cns config initial <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3460EA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020365

```text
(exec)# do-exec undebug cns config interface <cr>
```

Handler ` RVA 0xE002120 `；selector ` 6 `；EOL ` RVA 0x3460E528 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020427

```text
(exec)# do-exec undebug cns config messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x3460F270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-023192

```text
(exec)# do-exec undebug cns config notify all <cr>
```

Handler ` RVA 0xF32E760 `；selector ` 0 `；EOL ` RVA 0x34611C20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-023178

```text
(exec)# do-exec undebug cns config notify eventing <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x34610C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-023188

```text
(exec)# do-exec undebug cns config notify expand <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34611978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-023183

```text
(exec)# do-exec undebug cns config notify generation <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x34611180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-023186

```text
(exec)# do-exec undebug cns config notify modes <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x346116D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-023180

```text
(exec)# do-exec undebug cns config notify nvgen <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x34610ED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-023185

```text
(exec)# do-exec undebug cns config notify xml <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34611428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4afb26d209dbb05e](../../evidence/state_effects-sets-016.md#s-4afb26d209dbb05e)

### path-020383

```text
(exec)# do-exec undebug cns config partial <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3460E7D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020346

```text
(exec)# do-exec undebug cns config retrieve <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3460E280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-35253583b900d210](../../evidence/state_effects-sets-012.md#s-35253583b900d210)

### path-020350

```text
(exec)# do-exec undebug cns event agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34617F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dc8a363927fb5f1e](../../evidence/state_effects-sets-047.md#s-dc8a363927fb5f1e)

### path-020386

```text
(exec)# do-exec undebug cns event all <cr>
```

Handler ` RVA 0xF35D580 `；selector ` 0 `；EOL ` RVA 0x346184C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dc8a363927fb5f1e](../../evidence/state_effects-sets-047.md#s-dc8a363927fb5f1e)

### path-020335

```text
(exec)# do-exec undebug cns event connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34617CD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dc8a363927fb5f1e](../../evidence/state_effects-sets-047.md#s-dc8a363927fb5f1e)

### path-020368

```text
(exec)# do-exec undebug cns event subscriber <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34618220 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dc8a363927fb5f1e](../../evidence/state_effects-sets-047.md#s-dc8a363927fb5f1e)

### path-020362

```text
(exec)# do-exec undebug cns exec agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x346198D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1c952d928f792e6b](../../evidence/state_effects-sets-007.md#s-1c952d928f792e6b)

### path-020409

```text
(exec)# do-exec undebug cns exec all <cr>
```

Handler ` RVA 0xF369750 `；selector ` 0 `；EOL ` RVA 0x3461A0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1c952d928f792e6b](../../evidence/state_effects-sets-007.md#s-1c952d928f792e6b)

### path-020396

```text
(exec)# do-exec undebug cns exec decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x34619E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1c952d928f792e6b](../../evidence/state_effects-sets-007.md#s-1c952d928f792e6b)

### path-020381

```text
(exec)# do-exec undebug cns exec messages <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34619B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1c952d928f792e6b](../../evidence/state_effects-sets-007.md#s-1c952d928f792e6b)

### path-016304

```text
(exec)# do-exec undebug cns format <cr>
```

Handler ` RVA 0xE002120 `；selector ` 5 `；EOL ` RVA 0x340E75F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6d6d8904cc8fbbf8](../../evidence/state_effects-sets-023.md#s-6d6d8904cc8fbbf8)

### path-016283

```text
(exec)# do-exec undebug cns framework <cr>
```

Handler ` RVA 0xE002120 `；selector ` 4 `；EOL ` RVA 0x340E7080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-67fe72d59a8bb0a4](../../evidence/state_effects-sets-022.md#s-67fe72d59a8bb0a4)

### path-016316

```text
(exec)# do-exec undebug cns http <cr>
```

Handler ` RVA 0xE002120 `；selector ` 7 `；EOL ` RVA 0x340E78A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-88b475f9f6fa29e1](../../evidence/state_effects-sets-029.md#s-88b475f9f6fa29e1)

### path-020394

```text
(exec)# do-exec undebug cns image agent <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3461CC78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2bc790ee4b78c798](../../evidence/state_effects-sets-010.md#s-2bc790ee4b78c798)

### path-020418

```text
(exec)# do-exec undebug cns image all <cr>
```

Handler ` RVA 0xF36F680 `；selector ` 0 `；EOL ` RVA 0x3461D1C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2bc790ee4b78c798](../../evidence/state_effects-sets-010.md#s-2bc790ee4b78c798)

### path-020378

```text
(exec)# do-exec undebug cns image connection <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3461C9D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2bc790ee4b78c798](../../evidence/state_effects-sets-010.md#s-2bc790ee4b78c798)

### path-020408

```text
(exec)# do-exec undebug cns image error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x3461CF20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2bc790ee4b78c798](../../evidence/state_effects-sets-010.md#s-2bc790ee4b78c798)

### path-016246

```text
(exec)# do-exec undebug cns io <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x340E65A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b01d649490bf5bf4](../../evidence/state_effects-sets-037.md#s-b01d649490bf5bf4)

### path-016254

```text
(exec)# do-exec undebug cns lock <cr>
```

Handler ` RVA 0xE002120 `；selector ` 11 `；EOL ` RVA 0x340E6858 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dda0fb489ff19158](../../evidence/state_effects-sets-047.md#s-dda0fb489ff19158)

### path-016298

```text
(exec)# do-exec undebug cns management <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3461E430 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3e98b46f7234aaa5](../../evidence/state_effects-sets-014.md#s-3e98b46f7234aaa5)

### path-016273

```text
(exec)# do-exec undebug cns ssl <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x340E6DC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3eb947e30cd30c05](../../evidence/state_effects-sets-014.md#s-3eb947e30cd30c05)

### path-016262

```text
(exec)# do-exec undebug cns transport <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x340E6B10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-140b24574d5b0698](../../evidence/state_effects-sets-005.md#s-140b24574d5b0698)

### path-020461

```text
(exec)# do-exec undebug cns xml all <cr>
```

Handler ` RVA 0xDFA91E0 `；selector ` 0 `；EOL ` RVA 0x340E83D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b63f3ca3dab76d4d](../../evidence/state_effects-sets-039.md#s-b63f3ca3dab76d4d)

### path-020453

```text
(exec)# do-exec undebug cns xml decode <cr>
```

Handler ` RVA 0xE002120 `；selector ` 8 `；EOL ` RVA 0x340E8128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b63f3ca3dab76d4d](../../evidence/state_effects-sets-039.md#s-b63f3ca3dab76d4d)

### path-020437

```text
(exec)# do-exec undebug cns xml dom <cr>
```

Handler ` RVA 0xE002120 `；selector ` 9 `；EOL ` RVA 0x340E7BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b63f3ca3dab76d4d](../../evidence/state_effects-sets-039.md#s-b63f3ca3dab76d4d)

### path-020444

```text
(exec)# do-exec undebug cns xml parser <cr>
```

Handler ` RVA 0xE002120 `；selector ` 10 `；EOL ` RVA 0x340E7E80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d73e24ed4cef32cc](../../evidence/conditions-sets-083.md#c-d73e24ed4cef32cc) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b63f3ca3dab76d4d](../../evidence/state_effects-sets-039.md#s-b63f3ca3dab76d4d)

### path-012441

```text
(exec)# do-exec undebug compress <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34646F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-10d6ac3336e1acd7](../../evidence/state_effects-sets-004.md#s-10d6ac3336e1acd7)

### path-013197

```text
(exec)# do-exec undebug compress detailed <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34646F00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-10d6ac3336e1acd7](../../evidence/state_effects-sets-004.md#s-10d6ac3336e1acd7)

### path-012886

```text
(exec)# do-exec undebug condition <number:1..1000> <cr>
```

Handler ` RVA 0xE0124E0 `；selector ` 0 `；EOL ` RVA 0x341680A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Condition identifier。

[条件 C-a819487b214fec44](../../evidence/conditions-sets-065.md#c-a819487b214fec44) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e091cf22db6c4c81](../../evidence/parameters-sets-017.md#p-e091cf22db6c4c81) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-012895

```text
(exec)# do-exec undebug condition all <cr>
```

Handler ` RVA 0xE0124E0 `；selector ` 1 `；EOL ` RVA 0x34168358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a819487b214fec44](../../evidence/conditions-sets-065.md#c-a819487b214fec44) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016828

```text
(exec)# do-exec undebug condition called <string> <cr>
```

Handler ` RVA 0xE015F70 `；selector ` 0 `；EOL ` RVA 0x3416C040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Called number。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-583c5beadceb4dd1](../../evidence/parameters-sets-007.md#p-583c5beadceb4dd1) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016841

```text
(exec)# do-exec undebug condition calling <string> <cr>
```

Handler ` RVA 0xE016010 `；selector ` 0 `；EOL ` RVA 0x3416C360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Calling number。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-26077f9ec3339f62](../../evidence/parameters-sets-003.md#p-26077f9ec3339f62) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-021073

```text
(exec)# do-exec undebug condition cpl class-map <string> <cr>
```

Handler ` RVA 0xD8A8990 `；selector ` 0 `；EOL ` RVA 0x33F2ABB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Name of class。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ee5f9e90a0333755](../../evidence/parameters-sets-018.md#p-ee5f9e90a0333755) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-021086

```text
(exec)# do-exec undebug condition cpl policy-map <string> <cr>
```

Handler ` RVA 0xD8A8A80 `；selector ` 0 `；EOL ` RVA 0x33F2AED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Name of policy。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6da79a5792f6ebb6](../../evidence/parameters-sets-009.md#p-6da79a5792f6ebb6) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-021024

```text
(exec)# do-exec undebug condition cts peer-id <string> <cr>
```

Handler ` RVA 0x1315A430 `；selector ` 0 `；EOL ` RVA 0x35A4B878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Peer-id for debug filtering。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ff8ab1abf14164b9](../../evidence/parameters-sets-019.md#p-ff8ab1abf14164b9) · [状态效果 S-2b5aa24c3f65a711](../../evidence/state_effects-sets-010.md#s-2b5aa24c3f65a711)

### path-016889

```text
(exec)# do-exec undebug condition domain <string> <cr>
```

Handler ` RVA 0xE016820 `；selector ` 0 `；EOL ` RVA 0x34169038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Domain Name for debug filtering。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3db3ad0c087c65b9](../../evidence/parameters-sets-005.md#p-3db3ad0c087c65b9) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016892

```text
(exec)# do-exec undebug condition ip <address> <cr>
```

Handler ` RVA 0xE016440 `；selector ` 0 `；EOL ` RVA 0x3416CD88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` IP address。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ba6c1e5afebebf7a](../../evidence/parameters-sets-014.md#p-ba6c1e5afebebf7a) · [状态效果 S-f2f0e7a0753ac4b8](../../evidence/state_effects-sets-051.md#s-f2f0e7a0753ac4b8)

### path-024959

```text
(exec)# do-exec undebug condition ip nat inside destination list <number:1..2699> <cr>
```

Handler ` RVA 0xFAA60B0 `；selector ` 4 `；EOL ` RVA 0x347ECA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-c0eb11561ae7bd99](../../evidence/conditions-sets-074.md#c-c0eb11561ae7bd99) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-56fb8c865d84d520](../../evidence/parameters-sets-007.md#p-56fb8c865d84d520) · [状态效果 S-ed011f62140fc4ee](../../evidence/state_effects-sets-050.md#s-ed011f62140fc4ee)

### path-023425

```text
(exec)# do-exec undebug condition ip nat inside source <cr>
```

Handler ` RVA 0xFAA60B0 `；selector ` 2 `；EOL ` RVA 0x347EB908 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-ab89f2eec0ffd742](../../evidence/conditions-sets-066.md#c-ab89f2eec0ffd742) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ff293d2b3adbc88b](../../evidence/state_effects-sets-054.md#s-ff293d2b3adbc88b)

### path-025116

```text
(exec)# do-exec undebug condition ip nat inside source static <address> <address> <cr>
```

Handler ` RVA 0xFAA5CE0 `；selector ` 2 `；EOL ` RVA 0x347EBEE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-2f2a74ebd736009a](../../evidence/conditions-sets-018.md#c-2f2a74ebd736009a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-23b933c6ddbc3ea6](../../evidence/parameters-sets-003.md#p-23b933c6ddbc3ea6) · [状态效果 S-ff293d2b3adbc88b](../../evidence/state_effects-sets-054.md#s-ff293d2b3adbc88b)

### path-024962

```text
(exec)# do-exec undebug condition ip nat outside source list <number:1..2699> <cr>
```

Handler ` RVA 0xFAA60B0 `；selector ` 3 `；EOL ` RVA 0x347ECF30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-b43ab5bdc600e5e2](../../evidence/conditions-sets-070.md#c-b43ab5bdc600e5e2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e0d06491e8ac96e8](../../evidence/parameters-sets-017.md#p-e0d06491e8ac96e8) · [状态效果 S-4f0c401ca1ad8323](../../evidence/state_effects-sets-017.md#s-4f0c401ca1ad8323)

### path-025114

```text
(exec)# do-exec undebug condition ip nat outside source static <address> <address> <cr>
```

Handler ` RVA 0xFAA5CE0 `；selector ` 3 `；EOL ` RVA 0x347ED450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-b43ab5bdc600e5e2](../../evidence/conditions-sets-070.md#c-b43ab5bdc600e5e2) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a6b2b8043c5b7bf2](../../evidence/parameters-sets-013.md#p-a6b2b8043c5b7bf2) · [状态效果 S-4f0c401ca1ad8323](../../evidence/state_effects-sets-017.md#s-4f0c401ca1ad8323)

### path-023423

```text
(exec)# do-exec undebug condition ip nat pool <string> <cr>
```

Handler ` RVA 0xFAA5BC0 `；selector ` 0 `；EOL ` RVA 0x347EDA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Name of address pool。

[条件 C-99f2610478e09b3e](../../evidence/conditions-sets-060.md#c-99f2610478e09b3e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-316716d9bd87b796](../../evidence/parameters-sets-004.md#p-316716d9bd87b796) · [状态效果 S-f2f0e7a0753ac4b8](../../evidence/state_effects-sets-051.md#s-f2f0e7a0753ac4b8)

### path-016868

```text
(exec)# do-exec undebug condition mac-address <address> <cr>
```

Handler ` RVA 0xE016320 `；selector ` 0 `；EOL ` RVA 0x3416C6D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` MAC address。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f0be02a7fb105e63](../../evidence/parameters-sets-018.md#p-f0be02a7fb105e63) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016869

```text
(exec)# do-exec undebug condition mac-address all <cr>
```

Handler ` RVA 0xE016320 `；selector ` 1 `；EOL ` RVA 0x3416C980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-6ceb302d17bd53d1](../../evidence/conditions-sets-042.md#c-6ceb302d17bd53d1) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016983

```text
(exec)# do-exec undebug condition match-list <number:1..16> <cr>
```

Handler ` RVA 0x16984060 `；selector ` 1 `；EOL ` RVA 0x3605A110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` tag number。

[条件 C-bb14c7ded5250e01](../../evidence/conditions-sets-072.md#c-bb14c7ded5250e01) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-300a77722ac951e6](../../evidence/parameters-sets-004.md#p-300a77722ac951e6) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-024566

```text
(exec)# do-exec undebug condition portbundle ip <address> bundle <number:0..65536> <cr>
```

Handler ` RVA 0xE016B80 `；selector ` 0 `；EOL ` RVA 0x341699F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` value of address or, hostname；` unsigned_number ` bundle number。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-515e2640ff73bea5](../../evidence/parameters-sets-007.md#p-515e2640ff73bea5) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016902

```text
(exec)# do-exec undebug condition session-id <number:1..4294967295> <cr>
```

Handler ` RVA 0xE016A50 `；selector ` 0 `；EOL ` RVA 0x34169630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Session Number for debug filtering。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3c7c9176ad2e5bff](../../evidence/parameters-sets-005.md#p-3c7c9176ad2e5bff) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016932

```text
(exec)# do-exec undebug condition tnlmsg <number:1..15> <cr>
```

Handler ` RVA 0xE016940 `；selector ` 0 `；EOL ` RVA 0x34169330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` tunnel msgs。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4bad303df9c35ecc](../../evidence/parameters-sets-006.md#p-4bad303df9c35ecc) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016813

```text
(exec)# do-exec undebug condition username <string> <cr>
```

Handler ` RVA 0xE015ED0 `；selector ` 0 `；EOL ` RVA 0x3416BD20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Username for debug filtering。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7f0f7ee5c594aa79](../../evidence/parameters-sets-010.md#p-7f0f7ee5c594aa79) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016879

```text
(exec)# do-exec undebug condition vcid <number:1..4294967295> <cr>
```

Handler ` RVA 0xE0166A0 `；selector ` 0 `；EOL ` RVA 0x3416D0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` VC ID。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4247904d2d01d608](../../evidence/parameters-sets-006.md#p-4247904d2d01d608) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-017013

```text
(exec)# do-exec undebug condition vlan <number:1..4094> <cr>
```

Handler ` RVA 0xC797120 `；selector ` 0 `；EOL ` RVA 0x33AEF408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` VLAN Id。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2879712ac6bc6937](../../evidence/parameters-sets-003.md#p-2879712ac6bc6937) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-016975

```text
(exec)# do-exec undebug condition vrf default <cr>
```

Handler ` RVA 0xDC4B7D0 `；selector ` 0 `；EOL ` RVA 0x34020D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-012930

```text
(exec)# do-exec undebug configuration lock <cr>
```

Handler ` RVA 0xE002120 `；selector ` 24 `；EOL ` RVA 0x340CCDA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-65aa9d0b229fc6fe](../../evidence/conditions-sets-039.md#c-65aa9d0b229fc6fe) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a9b29d7791d84d9d](../../evidence/state_effects-sets-036.md#s-a9b29d7791d84d9d)

### path-012687

```text
(exec)# do-exec undebug confmodem <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x348DCEB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-6e263176d0d9864e](../../evidence/state_effects-sets-023.md#s-6e263176d0d9864e)

### path-012561

```text
(exec)# do-exec undebug conn <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34649160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-890f2cf77e4a0679](../../evidence/state_effects-sets-029.md#s-890f2cf77e4a0679)

### path-012640

```text
(exec)# do-exec undebug cops <cr>
```

Handler ` RVA 0xF449F80 `；selector ` 0 `；EOL ` RVA 0x3464C360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-cf5b38978189cb53](../../evidence/state_effects-sets-044.md#s-cf5b38978189cb53)

### path-014292

```text
(exec)# do-exec undebug cpc function-trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x34CC80E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e24c339e2b7dff58](../../evidence/state_effects-sets-048.md#s-e24c339e2b7dff58)

### path-014270

```text
(exec)# do-exec undebug cpc subblock <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x34CC7E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e24c339e2b7dff58](../../evidence/state_effects-sets-048.md#s-e24c339e2b7dff58)

### path-012697

```text
(exec)# do-exec undebug cpl <cr>
```

Handler ` RVA 0xD8B5AB0 `；selector ` 3 `；EOL ` RVA 0x33F3EC90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-5fae713a7bb9bea3](../../evidence/state_effects-sets-021.md#s-5fae713a7bb9bea3)

### path-015637

```text
(exec)# do-exec undebug cpl cap-xos <cr>
```

Handler ` RVA 0xD8B6630 `；selector ` 13 `；EOL ` RVA 0x33F2FD80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1e408c43b1b1003f](../../evidence/state_effects-sets-007.md#s-1e408c43b1b1003f)

### path-015771

```text
(exec)# do-exec undebug cpl classification <cr>
```

Handler ` RVA 0xD8B64E0 `；selector ` 78 `；EOL ` RVA 0x33F3E9E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e5c843db3f0922b9](../../evidence/state_effects-sets-049.md#s-e5c843db3f0922b9)

### path-019937

```text
(exec)# do-exec undebug cpl classification client <cr>
```

Handler ` RVA 0xE002120 `；selector ` 80 `；EOL ` RVA 0x33F3E490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e5c843db3f0922b9](../../evidence/state_effects-sets-049.md#s-e5c843db3f0922b9)

### path-019949

```text
(exec)# do-exec undebug cpl classification dp <cr>
```

Handler ` RVA 0xE002120 `；selector ` 81 `；EOL ` RVA 0x33F3E738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e5c843db3f0922b9](../../evidence/state_effects-sets-049.md#s-e5c843db3f0922b9)

### path-019928

```text
(exec)# do-exec undebug cpl classification infra <cr>
```

Handler ` RVA 0xE002120 `；selector ` 79 `；EOL ` RVA 0x33F3E1E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-e5c843db3f0922b9](../../evidence/state_effects-sets-049.md#s-e5c843db3f0922b9)

### path-024894

```text
(exec)# do-exec undebug cpl concurrency delay acquire <number:0..300> <number:1..10000> <cr>
```

Handler ` RVA 0xD8B8BD0 `；selector ` 0 `；EOL ` RVA 0x33F2F750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Delay in seconds；` unsigned_number ` Process ID to apply delay to。

[条件 C-737d59b77c36d796](../../evidence/conditions-sets-045.md#c-737d59b77c36d796) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-84d2a1b37008e964](../../evidence/parameters-sets-010.md#p-84d2a1b37008e964) · [状态效果 S-08c4ecd101f34feb](../../evidence/state_effects-sets-002.md#s-08c4ecd101f34feb)

### path-019842

```text
(exec)# do-exec undebug cpl concurrency history <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33F2EE30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3a53a75218fbe148](../../evidence/state_effects-sets-013.md#s-3a53a75218fbe148)

### path-019857

```text
(exec)# do-exec undebug cpl concurrency lock <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33F2F380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3a53a75218fbe148](../../evidence/state_effects-sets-013.md#s-3a53a75218fbe148)

### path-022890

```text
(exec)# do-exec undebug cpl concurrency pid <number:1..10000> <cr>
```

Handler ` RVA 0xD8B8C70 `；selector ` 0 `；EOL ` RVA 0x33F2FAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Process ID。

[条件 C-53a7ca98ab8a7598](../../evidence/conditions-sets-033.md#c-53a7ca98ab8a7598) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-df7cdec8dcffcaec](../../evidence/parameters-sets-017.md#p-df7cdec8dcffcaec) · [状态效果 S-3a53a75218fbe148](../../evidence/state_effects-sets-013.md#s-3a53a75218fbe148)

### path-019853

```text
(exec)# do-exec undebug cpl concurrency trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33F2F0D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3a53a75218fbe148](../../evidence/state_effects-sets-013.md#s-3a53a75218fbe148)

### path-015724

```text
(exec)# do-exec undebug cpl filtering <cr>
```

Handler ` RVA 0xE002120 `；selector ` 77 `；EOL ` RVA 0x33F3DEB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-24f23af9f3b4bbc7](../../evidence/state_effects-sets-008.md#s-24f23af9f3b4bbc7)

### path-019878

```text
(exec)# do-exec undebug cpl function <string> <cr>
```

Handler ` RVA 0xD8B8B50 `；selector ` 0 `；EOL ` RVA 0x33F305E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` function name。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1f5cf5dd81e42be8](../../evidence/parameters-sets-003.md#p-1f5cf5dd81e42be8) · [状态效果 S-1e408c43b1b1003f](../../evidence/state_effects-sets-007.md#s-1e408c43b1b1003f)

### path-015596

```text
(exec)# do-exec undebug cpl inline <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33F28180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1d138b81d4ac464b](../../evidence/state_effects-sets-007.md#s-1d138b81d4ac464b)

### path-015650

```text
(exec)# do-exec undebug cpl pol-shim <cr>
```

Handler ` RVA 0xD8B65D0 `；selector ` 12 `；EOL ` RVA 0x33F30028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1e408c43b1b1003f](../../evidence/state_effects-sets-007.md#s-1e408c43b1b1003f)

### path-015853

```text
(exec)# do-exec undebug cpl ppcp <cr>
```

Handler ` RVA 0xD8B5E60 `；selector ` 4 `；EOL ` RVA 0x33F3DB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-22e68ce2d0a49045](../../evidence/state_effects-sets-008.md#s-22e68ce2d0a49045)

### path-019916

```text
(exec)# do-exec undebug cpl ppcp bind <cr>
```

Handler ` RVA 0xE002120 `；selector ` 27 `；EOL ` RVA 0x33F30E78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-22e68ce2d0a49045](../../evidence/state_effects-sets-008.md#s-22e68ce2d0a49045)

### path-020018

```text
(exec)# do-exec undebug cpl ppcp client <cr>
```

Handler ` RVA 0xD8B6440 `；selector ` 18 `；EOL ` RVA 0x33F326C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-22e68ce2d0a49045](../../evidence/state_effects-sets-008.md#s-22e68ce2d0a49045)

