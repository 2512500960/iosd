# subinterface · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-069057

```text
(config-subif)# aaa connect-info <string> <cr>
```

Handler ` RVA 0xE075DC0 `；selector ` 72 `；EOL ` RVA 0x3419C2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` connect-info。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682) · [参数 P-23ea33b390829d45](../../evidence/parameters-sets-003.md#p-23ea33b390829d45)

### path-069592

```text
(config-subif)# access-expression input <string> <cr>
```

Handler ` RVA 0x1E3FC780 `；selector ` 0 `；EOL ` RVA 0x345EC7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A boolean expression of bridge access lists。

[条件 C-e176df43d420d700](../../evidence/conditions-sets-087.md#c-e176df43d420d700) · [参数 P-6452b2a4f32469b3](../../evidence/parameters-sets-008.md#p-6452b2a4f32469b3) · [状态效果 S-2b17d784b6e209fa](../../evidence/state_effects-sets-010.md#s-2b17d784b6e209fa)

### path-068666

```text
(config-subif)# access-session closed <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 2 `；EOL ` RVA 0x33BA55D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d7b70ab64f158610](../../evidence/conditions-sets-083.md#c-d7b70ab64f158610)

### path-069820

```text
(config-subif)# access-session control-direction both <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 4 `；EOL ` RVA 0x33BA5CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d01bf4c9495641a3](../../evidence/conditions-sets-080.md#c-d01bf4c9495641a3) · [状态效果 S-a117a80198d12d81](../../evidence/state_effects-sets-034.md#s-a117a80198d12d81)

### path-069736

```text
(config-subif)# access-session host-mode multi-auth <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 1 `；EOL ` RVA 0x33BA4CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c342ba47deda8698](../../evidence/conditions-sets-075.md#c-c342ba47deda8698) · [状态效果 S-24a4a4bec8dfda32](../../evidence/state_effects-sets-008.md#s-24a4a4bec8dfda32)

### path-070943

```text
(config-subif)# access-session inherit disable service-policy <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 7 `；EOL ` RVA 0x33BA6680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-366c2145c1d195d1](../../evidence/conditions-sets-021.md#c-366c2145c1d195d1) · [状态效果 S-f1c050a7fad0c05b](../../evidence/state_effects-sets-051.md#s-f1c050a7fad0c05b)

### path-069869

```text
(config-subif)# access-session interface-template sticky <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 6 `；EOL ` RVA 0x33BA60D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d7b70ab64f158610](../../evidence/conditions-sets-083.md#c-d7b70ab64f158610) · [状态效果 S-dc791813f48db18f](../../evidence/state_effects-sets-047.md#s-dc791813f48db18f)

### path-071044

```text
(config-subif)# access-session limit profile-name <string> <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 9 `；EOL ` RVA 0x33BA5258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` session limit profile name maximum 32 characters。

[条件 C-8b81d036faa8b471](../../evidence/conditions-sets-054.md#c-8b81d036faa8b471) · [参数 P-0a95d86c6db4ca1b](../../evidence/parameters-sets-001.md#p-0a95d86c6db4ca1b) · [状态效果 S-2c8a3058564fb3e6](../../evidence/state_effects-sets-010.md#s-2c8a3058564fb3e6)

### path-068616

```text
(config-subif)# access-session monitor <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 10 `；EOL ` RVA 0x33BA4940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f8877db32c126ab](../../evidence/conditions-sets-012.md#c-1f8877db32c126ab)

### path-069795

```text
(config-subif)# access-session port-control auto <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 3 `；EOL ` RVA 0x33BA5910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71a7d3f4360ff3ac](../../evidence/conditions-sets-044.md#c-71a7d3f4360ff3ac) · [状态效果 S-3cb661031864751e](../../evidence/state_effects-sets-013.md#s-3cb661031864751e)

### path-070026

```text
(config-subif)# alps ascu <number:33..79> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 8 `；EOL ` RVA 0x354201A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  RID value。

[条件 C-0a4668f7a9da7767](../../evidence/conditions-sets-004.md#c-0a4668f7a9da7767) · [参数 P-99e755fa8bd22d3d](../../evidence/parameters-sets-012.md#p-99e755fa8bd22d3d)

### path-070012

```text
(config-subif)# alps ascu <number:65..126> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 8 `；EOL ` RVA 0x3541DE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Interchange address。

[条件 C-e45d57df3a3beb07](../../evidence/conditions-sets-088.md#c-e45d57df3a3beb07) · [参数 P-3f81ae14511241f6](../../evidence/parameters-sets-005.md#p-3f81ae14511241f6)

### path-072356

```text
(config-subif)# alps host-hld <number:1..65535> host-link <number:1..255> ax25 <cr>
```

Handler ` RVA 0x11213450 `；selector ` 0 `；EOL ` RVA 0x3541D688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Host HLD Number；` unsigned_number ` Host-link identifier number。

[条件 C-d1fccaa4aac6a927](../../evidence/conditions-sets-081.md#c-d1fccaa4aac6a927) · [参数 P-05eb6bb78df80933](../../evidence/parameters-sets-001.md#p-05eb6bb78df80933) · [状态效果 S-8893e3989301de1d](../../evidence/state_effects-sets-029.md#s-8893e3989301de1d)

### path-068190

```text
(config-subif)# alps n1 <number:1..30> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 2 `；EOL ` RVA 0x3541E3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default value is 10。

[条件 C-1f9ea8e424802660](../../evidence/conditions-sets-012.md#c-1f9ea8e424802660) · [参数 P-0b343ef322441b2c](../../evidence/parameters-sets-001.md#p-0b343ef322441b2c)

### path-068193

```text
(config-subif)# alps n2 <number:1..30> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 3 `；EOL ` RVA 0x3541E660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default value is 1。

[条件 C-ab18a14e0281a68c](../../evidence/conditions-sets-066.md#c-ab18a14e0281a68c) · [参数 P-73ea22168e39844e](../../evidence/parameters-sets-009.md#p-73ea22168e39844e)

### path-068194

```text
(config-subif)# alps n3 <number:1..10> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 4 `；EOL ` RVA 0x3541EBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default value is 3。

[条件 C-f17c324e78ce1e91](../../evidence/conditions-sets-093.md#c-f17c324e78ce1e91) · [参数 P-bea7701772bcb211](../../evidence/parameters-sets-014.md#p-bea7701772bcb211)

### path-068196

```text
(config-subif)# alps poll-pause <number:10..1000> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 6 `；EOL ` RVA 0x3541F128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` default is 50。

[条件 C-96e399a681f0fb5d](../../evidence/conditions-sets-058.md#c-96e399a681f0fb5d) · [参数 P-36bb9f3601b4b6b1](../../evidence/parameters-sets-005.md#p-36bb9f3601b4b6b1)

### path-072640

```text
(config-subif)# alps service-msg data-drop config-term  <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 11 `；EOL ` RVA 0x3541FAB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-de8fba17af2007f6](../../evidence/conditions-sets-086.md#c-de8fba17af2007f6) · [缺口 G-fe76bfa9d9655d59](../../evidence/gaps-sets-009.md#g-fe76bfa9d9655d59) · [状态效果 S-b4fe243a53714ec8](../../evidence/state_effects-sets-038.md#s-b4fe243a53714ec8)

### path-071430

```text
(config-subif)# alps service-msg data-drop msg-term <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 11 `；EOL ` RVA 0x3541FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f89c7d8c0030845](../../evidence/conditions-sets-025.md#c-3f89c7d8c0030845) · [状态效果 S-b0de42607bc9ea49](../../evidence/state_effects-sets-037.md#s-b0de42607bc9ea49)

### path-072639

```text
(config-subif)# alps service-msg format apollo  <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 9 `；EOL ` RVA 0x3541F750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-91df0217e6f5778c](../../evidence/conditions-sets-056.md#c-91df0217e6f5778c) · [缺口 G-36d1b3c8e06115eb](../../evidence/gaps-sets-002.md#g-36d1b3c8e06115eb) · [状态效果 S-0be6c2d0ed5e85cc](../../evidence/state_effects-sets-003.md#s-0be6c2d0ed5e85cc)

### path-071423

```text
(config-subif)# alps service-msg format sita <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 9 `；EOL ` RVA 0x3541F750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f89c7d8c0030845](../../evidence/conditions-sets-025.md#c-3f89c7d8c0030845) · [状态效果 S-77986e0455ecd09f](../../evidence/state_effects-sets-025.md#s-77986e0455ecd09f)

### path-070128

```text
(config-subif)# alps service-msg status-change <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 10 `；EOL ` RVA 0x3541FDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f89c7d8c0030845](../../evidence/conditions-sets-025.md#c-3f89c7d8c0030845)

### path-068195

```text
(config-subif)# alps servlim <number:1..512> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 5 `；EOL ` RVA 0x3541EEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default is 30。

[条件 C-e7fcc8b7f43f9ef3](../../evidence/conditions-sets-090.md#c-e7fcc8b7f43f9ef3) · [参数 P-c1401dc0f3ef9d7d](../../evidence/parameters-sets-015.md#p-c1401dc0f3ef9d7d)

### path-068841

```text
(config-subif)# alps syn-bcc-calc <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 7 `；EOL ` RVA 0x3541EE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc3bd141197c0f38](../../evidence/conditions-sets-085.md#c-dc3bd141197c0f38)

### path-068186

```text
(config-subif)# alps t1 <number:1..20> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 0 `；EOL ` RVA 0x3541DE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default value is 5 tenths of a sec。

[条件 C-4a4e0bf15e209008](../../evidence/conditions-sets-029.md#c-4a4e0bf15e209008) · [参数 P-0ffc687497d964a3](../../evidence/parameters-sets-002.md#p-0ffc687497d964a3)

### path-068189

```text
(config-subif)# alps t2 <number:1..10> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 1 `；EOL ` RVA 0x3541E380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default value is 6 sec。

[条件 C-bbbf9368399e1af3](../../evidence/conditions-sets-072.md#c-bbbf9368399e1af3) · [参数 P-96329195f4b949b5](../../evidence/parameters-sets-012.md#p-96329195f4b949b5)

### path-071328

```text
(config-subif)# alps translate <string> <address> <cr>
```

Handler ` RVA 0x11213450 `；selector ` 1 `；EOL ` RVA 0x3541DAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` X.121 address of remote peer；` address ` IP address for remote peer。

[条件 C-d1fccaa4aac6a927](../../evidence/conditions-sets-081.md#c-d1fccaa4aac6a927) · [参数 P-bb34929031a00e82](../../evidence/parameters-sets-014.md#p-bb34929031a00e82)

### path-070524

```text
(config-subif)# amt gateway relay-address <address> <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 2 `；EOL ` RVA 0x3386B160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP address of AMT discovery。

[条件 C-f0b5130686a1b1ab](../../evidence/conditions-sets-093.md#c-f0b5130686a1b1ab) · [参数 P-e435a110eefa083f](../../evidence/parameters-sets-017.md#p-e435a110eefa083f)

### path-070478

```text
(config-subif)# amt gateway traffic ip <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 1 `；EOL ` RVA 0x3386ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23795068f56fdfa1](../../evidence/conditions-sets-014.md#c-23795068f56fdfa1) · [状态效果 S-6bce64471baa9b4c](../../evidence/state_effects-sets-023.md#s-6bce64471baa9b4c)

### path-071583

```text
(config-subif)# amt relay maximum gateway <number:1..65535> <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 4 `；EOL ` RVA 0x3386B898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-f1cd5dbcfbd3c4d7](../../evidence/conditions-sets-093.md#c-f1cd5dbcfbd3c4d7) · [参数 P-a9b1462474133d9b](../../evidence/parameters-sets-013.md#p-a9b1462474133d9b)

### path-070492

```text
(config-subif)# amt relay traffic ip <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 3 `；EOL ` RVA 0x3386B4C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-23795068f56fdfa1](../../evidence/conditions-sets-014.md#c-23795068f56fdfa1)

### path-068363

```text
(config-subif)# ancp enable <cr>
```

Handler ` RVA 0xB2613A0 `；selector ` 2 `；EOL ` RVA 0x336D75B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5c410a8e06ed019](../../evidence/conditions-sets-089.md#c-e5c410a8e06ed019)

### path-072164

```text
(config-subif)# ancp neighbor name <string> client-id <string> <cr>
```

Handler ` RVA 0xB2613A0 `；selector ` 3 `；EOL ` RVA 0x336D7A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP client ID。

[条件 C-2984da66dd597d62](../../evidence/conditions-sets-016.md#c-2984da66dd597d62) · [参数 P-3eed75d6b4785b53](../../evidence/parameters-sets-005.md#p-3eed75d6b4785b53)

### path-068372

```text
(config-subif)# arp arpa <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 1 `；EOL ` RVA 0x33D3E920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0)

### path-068405

```text
(config-subif)# arp authorized <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 10 `；EOL ` RVA 0x33D3F118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0)

### path-070747

```text
(config-subif)# arp entries interface-limit disable <cr>
```

Handler ` RVA 0xCD664F0 `；selector ` 0 `；EOL ` RVA 0x33D3FE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fda05feebbb2c15](../../evidence/conditions-sets-043.md#c-6fda05feebbb2c15) · [状态效果 S-ff8de25c53050e53](../../evidence/state_effects-sets-054.md#s-ff8de25c53050e53)

### path-068386

```text
(config-subif)# arp frame-relay <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 7 `；EOL ` RVA 0x33D3EBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0)

### path-071707

```text
(config-subif)# arp log threshold entries <number:1..2147483647> <cr>
```

Handler ` RVA 0xCD62360 `；selector ` 0 `；EOL ` RVA 0x33D3FAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Entry count to trigger ARP log。

[条件 C-94e8513d49b3b116](../../evidence/conditions-sets-058.md#c-94e8513d49b3b116) · [参数 P-b96d9ef091779adc](../../evidence/parameters-sets-014.md#p-b96d9ef091779adc)

### path-069326

```text
(config-subif)# arp packet-priority enable <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 11 `；EOL ` RVA 0x33D3F6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0)

### path-072175

```text
(config-subif)# arp probe interval <number:1..10> count <number:1..60> <cr>
```

Handler ` RVA 0xCF75970 `；selector ` 0 `；EOL ` RVA 0x33D3E5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ARP probe interval (1-10 seconds)；` unsigned_number ` ARP probe count (1-60 times)。

[条件 C-7e80cc4fbc1d15b1](../../evidence/conditions-sets-049.md#c-7e80cc4fbc1d15b1) · [参数 P-dc836425c9d8e1d7](../../evidence/parameters-sets-017.md#p-dc836425c9d8e1d7)

### path-068397

```text
(config-subif)# arp snap <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 3 `；EOL ` RVA 0x33D3EE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0)

### path-068082

```text
(config-subif)# arp timeout <number:0..2147483> <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 6 `；EOL ` RVA 0x33D3F140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-e7eaa0042ca78137](../../evidence/conditions-sets-090.md#c-e7eaa0042ca78137) · [参数 P-82ce2c50d16d5e7c](../../evidence/parameters-sets-010.md#p-82ce2c50d16d5e7c)

### path-069132

```text
(config-subif)# asp addr-offset <number:0..255> <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 2 `；EOL ` RVA 0x354A4178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Offset within frame of address byte。

[条件 C-189c8e8fea5957bf](../../evidence/conditions-sets-010.md#c-189c8e8fea5957bf) · [参数 P-0891ccc08b064f40](../../evidence/parameters-sets-001.md#p-0891ccc08b064f40)

### path-068346

```text
(config-subif)# asp assert-dtr <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 3 `；EOL ` RVA 0x354A4468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2f66a5b56a1d87f0](../../evidence/conditions-sets-019.md#c-2f66a5b56a1d87f0)

### path-069116

```text
(config-subif)# asp role secondary <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 1 `；EOL ` RVA 0x354A3DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8bdd7f5a5647f61e](../../evidence/conditions-sets-054.md#c-8bdd7f5a5647f61e) · [状态效果 S-7cdb88ce1fef7a4b](../../evidence/state_effects-sets-026.md#s-7cdb88ce1fef7a4b)

### path-069183

```text
(config-subif)# asp rx-ift <number:1..1000> <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 0 `；EOL ` RVA 0x354A4780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Inter frame timeout value in milliseconds。

[条件 C-748403561738bf0a](../../evidence/conditions-sets-045.md#c-748403561738bf0a) · [参数 P-f0183584b28292e8](../../evidence/parameters-sets-018.md#p-f0183584b28292e8)

### path-069794

```text
(config-subif)# async default routing <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 3 `；EOL ` RVA 0x34931ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ee0ab0468397a6d](../../evidence/conditions-sets-024.md#c-3ee0ab0468397a6d)

### path-069818

```text
(config-subif)# async dynamic address <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 5 `；EOL ` RVA 0x349321C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ee0ab0468397a6d](../../evidence/conditions-sets-024.md#c-3ee0ab0468397a6d)

### path-069841

```text
(config-subif)# async dynamic routing <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 4 `；EOL ` RVA 0x34932470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3ee0ab0468397a6d](../../evidence/conditions-sets-024.md#c-3ee0ab0468397a6d)

### path-069859

```text
(config-subif)# async mode dedicated <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 1 `；EOL ` RVA 0x34932798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8b1b448a907b448](../../evidence/conditions-sets-077.md#c-c8b1b448a907b448)

### path-069876

```text
(config-subif)# async mode interactive <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 0 `；EOL ` RVA 0x34932A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8b1b448a907b448](../../evidence/conditions-sets-077.md#c-c8b1b448a907b448)

### path-070668

```text
(config-subif)# atm-dxi interface-dfa <number:0..15> <number:0..63> <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 2 `；EOL ` RVA 0x344804C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VPI；` unsigned_number ` VCI。

[条件 C-51e6acc51068bf50](../../evidence/conditions-sets-032.md#c-51e6acc51068bf50) · [参数 P-d29bbb695865bd3a](../../evidence/parameters-sets-016.md#p-d29bbb695865bd3a) · [状态效果 S-5c89e887755b0a50](../../evidence/state_effects-sets-020.md#s-5c89e887755b0a50)

### path-072563

```text
(config-subif)# atm-dxi map <?protoaddr_action@5555899d3e70> <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 4 `；EOL ` RVA 0x3447FFD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41abdd82abddb327](../../evidence/conditions-sets-026.md#c-41abdd82abddb327) · [缺口 G-c0d27a435433ceb3](../../evidence/gaps-sets-007.md#g-c0d27a435433ceb3) · [状态效果 S-784d8c2d32462ce1](../../evidence/state_effects-sets-026.md#s-784d8c2d32462ce1)

### path-070646

```text
(config-subif)# atm-dxi pvc <number:0..15> <number:0..63> <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 3 `；EOL ` RVA 0x3447FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VPI；` unsigned_number ` VCI。

[条件 C-51e6acc51068bf50](../../evidence/conditions-sets-032.md#c-51e6acc51068bf50) · [参数 P-1d192fe15f08040c](../../evidence/parameters-sets-003.md#p-1d192fe15f08040c) · [状态效果 S-c19c00d21c23639b](../../evidence/state_effects-sets-041.md#s-c19c00d21c23639b)

### path-068404

```text
(config-subif)# atm-dxi zap <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 1 `；EOL ` RVA 0x34480870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-51e6acc51068bf50](../../evidence/conditions-sets-032.md#c-51e6acc51068bf50) · [状态效果 S-784d8c2d32462ce1](../../evidence/state_effects-sets-026.md#s-784d8c2d32462ce1)

### path-069770

```text
(config-subif)# authentication control-direction both <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 6 `；EOL ` RVA 0x33B95940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6955ab1530234d6c](../../evidence/conditions-sets-041.md#c-6955ab1530234d6c) · [状态效果 S-7c9e697fd39b6e8e](../../evidence/state_effects-sets-026.md#s-7c9e697fd39b6e8e)

### path-072706

```text
(config-subif)# authentication event fail action authorize vlan <number:dynamic> <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5DC20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter a VlanId。

[条件 C-4f2201c7946ac5d3](../../evidence/conditions-sets-031.md#c-4f2201c7946ac5d3) · [缺口 G-899b414426c06a5e](../../evidence/gaps-sets-005.md#g-899b414426c06a5e) · [参数 P-9ed64997a87c1ec3](../../evidence/parameters-sets-012.md#p-9ed64997a87c1ec3) · [状态效果 S-f8e4988801b6dc38](../../evidence/state_effects-sets-053.md#s-f8e4988801b6dc38)

### path-072707

```text
(config-subif)# authentication event fail action authorize vlan <number:dynamic> <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5CF00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter a VlanId。

[条件 C-7199d2176c936ccc](../../evidence/conditions-sets-044.md#c-7199d2176c936ccc) · [缺口 G-2efda3f179015ce4](../../evidence/gaps-sets-002.md#g-2efda3f179015ce4) · [参数 P-301309762296798a](../../evidence/parameters-sets-004.md#p-301309762296798a) · [状态效果 S-f8e4988801b6dc38](../../evidence/state_effects-sets-053.md#s-f8e4988801b6dc38)

### path-072708

```text
(config-subif)# authentication event fail action authorize vlan <number:dynamic> <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5E670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter a VlanId。

[条件 C-446da45ee76b590c](../../evidence/conditions-sets-027.md#c-446da45ee76b590c) · [缺口 G-6f80550da30a102c](../../evidence/gaps-sets-004.md#g-6f80550da30a102c) · [参数 P-2574b9bb8ee4c2e5](../../evidence/parameters-sets-003.md#p-2574b9bb8ee4c2e5) · [状态效果 S-f8e4988801b6dc38](../../evidence/state_effects-sets-053.md#s-f8e4988801b6dc38)

### path-071917

```text
(config-subif)# authentication event fail action next-method <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x33B91810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3dae962ab1a50449](../../evidence/conditions-sets-024.md#c-3dae962ab1a50449) · [状态效果 S-e7e72753139d1ae3](../../evidence/state_effects-sets-049.md#s-e7e72753139d1ae3)

### path-069796

```text
(config-subif)# authentication fallback <string> <cr>
```

Handler ` RVA 0xCAF51B0 `；selector ` 11 `；EOL ` RVA 0x33BAB150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of Webauth Profile (max 200 characters)。

[条件 C-f09ec0fe1f2f31a5](../../evidence/conditions-sets-093.md#c-f09ec0fe1f2f31a5) · [参数 P-1ff8891216cb5820](../../evidence/parameters-sets-003.md#p-1ff8891216cb5820)

### path-069702

```text
(config-subif)# authentication host-mode multi-auth <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 3 `；EOL ` RVA 0x33B94D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b068ca9510e04078](../../evidence/conditions-sets-068.md#c-b068ca9510e04078) · [状态效果 S-56259c537b635dbf](../../evidence/state_effects-sets-019.md#s-56259c537b635dbf)

### path-068659

```text
(config-subif)# authentication open <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 4 `；EOL ` RVA 0x33B95220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ab445ba1bd574f7](../../evidence/conditions-sets-054.md#c-8ab445ba1bd574f7)

### path-072538

```text
(config-subif)# authentication order <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 1 `；EOL ` RVA 0x33B91150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-12ed9d3f23af2ddf](../../evidence/conditions-sets-007.md#c-12ed9d3f23af2ddf) · [缺口 G-64d690baf032ce53](../../evidence/gaps-sets-004.md#g-64d690baf032ce53) · [状态效果 S-a9734089697352a1](../../evidence/state_effects-sets-036.md#s-a9734089697352a1)

### path-072539

```text
(config-subif)# authentication order <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 2 `；EOL ` RVA 0x33B913D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-58150ba4f3dbeace](../../evidence/conditions-sets-035.md#c-58150ba4f3dbeace) · [缺口 G-64d690baf032ce53](../../evidence/gaps-sets-004.md#g-64d690baf032ce53) · [状态效果 S-a9734089697352a1](../../evidence/state_effects-sets-036.md#s-a9734089697352a1)

### path-068603

```text
(config-subif)# authentication periodic <cr>
```

Handler ` RVA 0xCAD2B80 `；selector ` 8 `；EOL ` RVA 0x33B939F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c17387c0a674ce8e](../../evidence/conditions-sets-075.md#c-c17387c0a674ce8e)

### path-069732

```text
(config-subif)# authentication port-control auto <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 5 `；EOL ` RVA 0x33B95558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d94b06152866a7a8](../../evidence/conditions-sets-084.md#c-d94b06152866a7a8) · [状态效果 S-c5441bbca0f422ab](../../evidence/state_effects-sets-042.md#s-c5441bbca0f422ab)

### path-070975

```text
(config-subif)# authentication timer reauthenticate server <cr>
```

Handler ` RVA 0xCAD2B80 `；selector ` 9 `；EOL ` RVA 0x33B93DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e76dba707507d08f](../../evidence/conditions-sets-089.md#c-e76dba707507d08f) · [状态效果 S-26d010c2cf183631](../../evidence/state_effects-sets-009.md#s-26d010c2cf183631)

### path-071021

```text
(config-subif)# authentication timer restart <number:0..65535> <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 9 `；EOL ` RVA 0x33B94168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter a value between 0 and 65535。

[条件 C-84fafbec9e25bca1](../../evidence/conditions-sets-051.md#c-84fafbec9e25bca1) · [参数 P-75b9398c52516fc9](../../evidence/parameters-sets-009.md#p-75b9398c52516fc9) · [状态效果 S-96031c0ad4ddf0ab](../../evidence/state_effects-sets-032.md#s-96031c0ad4ddf0ab)

### path-069737

```text
(config-subif)# authentication violation protect <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 10 `；EOL ` RVA 0x33B946B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5d885b2055ef906](../../evidence/conditions-sets-095.md#c-f5d885b2055ef906) · [状态效果 S-06f85bd2f93fbd03](../../evidence/state_effects-sets-002.md#s-06f85bd2f93fbd03)

### path-068340

```text
(config-subif)# autodetect encapsulation <cr>
```

Handler ` RVA 0xED73570 `；selector ` 0 `；EOL ` RVA 0x3441FC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e794dc95d26f6b83](../../evidence/conditions-sets-089.md#c-e794dc95d26f6b83)

### path-068192

```text
(config-subif)# autostate <cr>
```

Handler ` RVA 0x15DB5230 `；selector ` 0 `；EOL ` RVA 0x35E321A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c5d4346d4bfef45](../../evidence/conditions-sets-030.md#c-4c5d4346d4bfef45)

### path-072599

```text
(config-subif)# backup active interface <interface> <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 3 `；EOL ` RVA 0x34482FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-639f47c7d0590e59](../../evidence/conditions-sets-039.md#c-639f47c7d0590e59) · [缺口 G-dad9af35909d6399](../../evidence/gaps-sets-008.md#g-dad9af35909d6399) · [参数 P-1f5c1edd9740380d](../../evidence/parameters-sets-003.md#p-1f5c1edd9740380d)

### path-070272

```text
(config-subif)# backup delay never never <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 1 `；EOL ` RVA 0x344822F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6e7015dbba3ccaf](../../evidence/conditions-sets-071.md#c-b6e7015dbba3ccaf) · [状态效果 S-fa5135a9236dae68](../../evidence/state_effects-sets-053.md#s-fa5135a9236dae68)

### path-072540

```text
(config-subif)# backup interface <interface> <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 0 `；EOL ` RVA 0x34482748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-af5d63daabe76942](../../evidence/conditions-sets-068.md#c-af5d63daabe76942) · [缺口 G-a4c57a5c30d64c02](../../evidence/gaps-sets-006.md#g-a4c57a5c30d64c02) · [参数 P-192776fde7460399](../../evidence/parameters-sets-002.md#p-192776fde7460399)

### path-070277

```text
(config-subif)# backup load never never <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 2 `；EOL ` RVA 0x34482B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9938d04381b8ace6](../../evidence/conditions-sets-059.md#c-9938d04381b8ace6) · [状态效果 S-377b92a7d7165d20](../../evidence/state_effects-sets-012.md#s-377b92a7d7165d20)

### path-068221

```text
(config-subif)# bandwidth <number:1..200000000> <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 0 `；EOL ` RVA 0x3412F6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kilobits。

[条件 C-a26744b3251cd176](../../evidence/conditions-sets-063.md#c-a26744b3251cd176) · [参数 P-0a254dcaf59a863d](../../evidence/parameters-sets-001.md#p-0a254dcaf59a863d)

### path-068223

```text
(config-subif)# bandwidth inherit <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 9 `；EOL ` RVA 0x3412F808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5faf3556d8e75753](../../evidence/conditions-sets-037.md#c-5faf3556d8e75753)

### path-068883

```text
(config-subif)# bandwidth inherit <number:1..200000000> <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 8 `；EOL ` RVA 0x3412F7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kilobits。

[条件 C-5faf3556d8e75753](../../evidence/conditions-sets-037.md#c-5faf3556d8e75753) · [参数 P-a0997a5ff2b07d27](../../evidence/parameters-sets-012.md#p-a0997a5ff2b07d27)

### path-068888

```text
(config-subif)# bandwidth qos-reference <number:1..10000000> <cr>
```

Handler ` RVA 0xDA50C00 `；selector ` 0 `；EOL ` RVA 0x3412FD78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kbps。

[条件 C-121c41a17cbe4312](../../evidence/conditions-sets-007.md#c-121c41a17cbe4312) · [参数 P-39d9737003289660](../../evidence/parameters-sets-005.md#p-39d9737003289660)

### path-068889

```text
(config-subif)# bandwidth receive <number:1..200000000> <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 7 `；EOL ` RVA 0x34130040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kilobits。

[条件 C-64af81de0ce66a8c](../../evidence/conditions-sets-039.md#c-64af81de0ce66a8c) · [参数 P-692023bef5839186](../../evidence/parameters-sets-008.md#p-692023bef5839186)

### path-068899

```text
(config-subif)# bandwidth receive inherit <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 12 `；EOL ` RVA 0x34130358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64af81de0ce66a8c](../../evidence/conditions-sets-039.md#c-64af81de0ce66a8c)

### path-070271

```text
(config-subif)# bandwidth receive inherit <number:1..200000000> <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 11 `；EOL ` RVA 0x34130330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kilobits。

[条件 C-64af81de0ce66a8c](../../evidence/conditions-sets-039.md#c-64af81de0ce66a8c) · [参数 P-c585cfcd594a1f5e](../../evidence/parameters-sets-015.md#p-c585cfcd594a1f5e)

### path-068467

```text
(config-subif)# bfd echo <cr>
```

Handler ` RVA 0x10B1DA10 `；selector ` 0 `；EOL ` RVA 0x34CB1848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70a3b5d50c196784](../../evidence/conditions-sets-044.md#c-70a3b5d50c196784)

### path-068443

```text
(config-subif)# bfd enable <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 7 `；EOL ` RVA 0x34CB1278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9)

### path-072411

```text
(config-subif)# bfd interval <number:50..9999> min_rx <number:50..9999> multiplier <number:3..50> <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 1 `；EOL ` RVA 0x34CB0AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Milliseconds；` unsigned_number ` Milliseconds；` unsigned_number ` value used to multiply the interval。

[条件 C-1cc46824356256cc](../../evidence/conditions-sets-011.md#c-1cc46824356256cc) · [参数 P-bfa54ca50b21b593](../../evidence/parameters-sets-015.md#p-bfa54ca50b21b593)

### path-072703

```text
(config-subif)# bfd interval <number:50..9999> min_rx <number:dynamic> multiplier <number:3..50> <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 1 `；EOL ` RVA 0x34CB0AC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Milliseconds；` unsigned_number_dynamic ` Milliseconds；` unsigned_number ` value used to multiply the interval。

[条件 C-e75984e664ae4fd1](../../evidence/conditions-sets-089.md#c-e75984e664ae4fd1) · [缺口 G-e9e0873081136d48](../../evidence/gaps-sets-008.md#g-e9e0873081136d48) · [参数 P-cb28fc4a559cd7b5](../../evidence/parameters-sets-015.md#p-cb28fc4a559cd7b5)

### path-068403

```text
(config-subif)# bfd jitter <cr>
```

Handler ` RVA 0x10B1D640 `；selector ` 0 `；EOL ` RVA 0x34CB0790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9)

### path-069363

```text
(config-subif)# bfd local-address <string> <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 8 `；EOL ` RVA 0x34CB1588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ip/ipv6 address。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [参数 P-743928651798c75c](../../evidence/parameters-sets-009.md#p-743928651798c75c)

### path-069373

```text
(config-subif)# bfd neighbor <address> <cr>
```

Handler ` RVA 0x10B4B690 `；selector ` 2 `；EOL ` RVA 0x34CB1D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor ip address。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [参数 P-f55bdc2ac59ef37f](../../evidence/parameters-sets-018.md#p-f55bdc2ac59ef37f) · [状态效果 S-9b591a05221a94a1](../../evidence/state_effects-sets-033.md#s-9b591a05221a94a1)

### path-069325

```text
(config-subif)# bfd template <string> <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 6 `；EOL ` RVA 0x34CB0FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` bfd template name。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [参数 P-b185832473e42b32](../../evidence/parameters-sets-013.md#p-b185832473e42b32)

### path-068422

```text
(config-subif)# bgp-policy accounting <cr>
```

Handler ` RVA 0xB6219A0 `；selector ` 0 `；EOL ` RVA 0x337C76C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84ca569e31294829](../../evidence/conditions-sets-051.md#c-84ca569e31294829) · [状态效果 S-d2ca3f40b0d49841](../../evidence/state_effects-sets-045.md#s-d2ca3f40b0d49841)

### path-072850

```text
(config-subif)# bridge-group <number:1..255> <?params_action_alist@555589b3da38> <?params_action_alist@555589b3df80> <?params_action_alist@555589b3e220> <?params_action_alist@555589b3efc0> <?params_action_alist@555589b3f010> <?params_action_alist@555589b3f2b8> <?params_action_alist@555589b3fad0> <?params_action_alist@555589b3fd50> force <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 24 `；EOL ` RVA 0x345EC2A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-b5588029c06e0f41](../../evidence/conditions-sets-070.md#c-b5588029c06e0f41) · [缺口 G-3991ea17e97c1aa6](../../evidence/gaps-sets-002.md#g-3991ea17e97c1aa6) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252)

### path-072848

```text
(config-subif)# bridge-group <number:1..255> <?params_action_alist@555589b3da38> <?params_action_alist@555589b3df80> <?params_action_alist@555589b3e220> <?params_action_alist@555589b3efc0> <?params_action_alist@555589b3f010> <?params_action_alist@555589b3f2b8> priority <number:0..255> <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 18 `；EOL ` RVA 0x345EB560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.；` unsigned_number ` increments of 16 for IEEE or vlan-bridge, others 1。

[条件 C-ec5b8170f4553bcf](../../evidence/conditions-sets-091.md#c-ec5b8170f4553bcf) · [缺口 G-13c72dfdc256abeb](../../evidence/gaps-sets-001.md#g-13c72dfdc256abeb) · [参数 P-010f92e4c021f57b](../../evidence/parameters-sets-001.md#p-010f92e4c021f57b)

### path-072849

```text
(config-subif)# bridge-group <number:1..255> <?params_action_alist@555589b3da38> <?params_action_alist@555589b3df80> <?params_action_alist@555589b3e220> <?params_action_alist@555589b3efc0> <?params_action_alist@555589b3f010> <?params_action_alist@555589b3f2b8> spanning-disabled <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 19 `；EOL ` RVA 0x345EBAA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-b5588029c06e0f41](../../evidence/conditions-sets-070.md#c-b5588029c06e0f41) · [缺口 G-39d60be161f589df](../../evidence/gaps-sets-003.md#g-39d60be161f589df) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252)

### path-072846

```text
(config-subif)# bridge-group <number:1..255> <?params_action_alist@555589b3da38> <?params_action_alist@555589b3df80> <?params_action_alist@555589b3e220> input-lat-service-deny <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 20 `；EOL ` RVA 0x345EAB98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-37a20cd79a25c73b](../../evidence/conditions-sets-022.md#c-37a20cd79a25c73b) · [缺口 G-0ca11e92e68258a4](../../evidence/gaps-sets-001.md#g-0ca11e92e68258a4) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252) · [状态效果 S-fe073691c75ca8ca](../../evidence/state_effects-sets-054.md#s-fe073691c75ca8ca)

### path-072845

```text
(config-subif)# bridge-group <number:1..255> <?params_action_alist@555589b3da38> <?params_action_alist@555589b3df80> <?params_action_alist@555589b3e220> lat-compression <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 10 `；EOL ` RVA 0x345EA770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-b5588029c06e0f41](../../evidence/conditions-sets-070.md#c-b5588029c06e0f41) · [缺口 G-0ca11e92e68258a4](../../evidence/gaps-sets-001.md#g-0ca11e92e68258a4) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252)

### path-072586

```text
(config-subif)# bridge-group <number:1..255> <?params_action_alist@555589b3da38> path-cost <number:0..65535> <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 17 `；EOL ` RVA 0x345E9CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.；` unsigned_number ` Path cost (higher values are higher costs)。

[条件 C-e0394fdf68a46354](../../evidence/conditions-sets-086.md#c-e0394fdf68a46354) · [缺口 G-42572df15bcaecdf](../../evidence/gaps-sets-003.md#g-42572df15bcaecdf) · [参数 P-b6dc599701134371](../../evidence/parameters-sets-014.md#p-b6dc599701134371)

### path-068618

```text
(config-subif)# bridge-group <number:1..255> <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 1 `；EOL ` RVA 0x345E91A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-7800d77b44caac6d](../../evidence/conditions-sets-047.md#c-7800d77b44caac6d) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252)

### path-068654

```text
(config-subif)# bridge-group <number:1..255> circuit-group <number:1..9> <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 3 `；EOL ` RVA 0x345E9780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.；` unsigned_number ` Circuit group number。

[条件 C-d9e7acf6a9afd654](../../evidence/conditions-sets-084.md#c-d9e7acf6a9afd654) · [参数 P-68718cb6fb95be3b](../../evidence/parameters-sets-008.md#p-68718cb6fb95be3b)

### path-069682

```text
(config-subif)# bridge-group <number:1..255> subscriber-loop-control <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 25 `；EOL ` RVA 0x345E97C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-b5588029c06e0f41](../../evidence/conditions-sets-070.md#c-b5588029c06e0f41) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252)

### path-069681

```text
(config-subif)# bridge-group <number:1..255> subscriber-trunk <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 23 `；EOL ` RVA 0x345E94E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-c11a8a1b77009055](../../evidence/conditions-sets-075.md#c-c11a8a1b77009055) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252)

### path-068374

```text
(config-subif)# bsc char-int <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 11 `；EOL ` RVA 0x354B74A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e)

### path-069133

```text
(config-subif)# bsc char-set ebcdic <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 3 `；EOL ` RVA 0x354B6170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9686b20603346961](../../evidence/conditions-sets-058.md#c-9686b20603346961) · [状态效果 S-a32ab18c81ef2f36](../../evidence/state_effects-sets-035.md#s-a32ab18c81ef2f36)

### path-068364

```text
(config-subif)# bsc contention <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 2 `；EOL ` RVA 0x354B6920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-a65aaf128e4c9d64](../../evidence/state_effects-sets-035.md#s-a65aaf128e4c9d64)

### path-068355

```text
(config-subif)# bsc dial-contention <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 12 `；EOL ` RVA 0x354B65C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-aac2cf9ee3596e29](../../evidence/state_effects-sets-036.md#s-aac2cf9ee3596e29)

### path-068462

```text
(config-subif)# bsc discard-syns <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 14 `；EOL ` RVA 0x354B8D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e)

### path-070557

```text
(config-subif)# bsc extended-address <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 10 `；EOL ` RVA 0x354B7218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Poll address；` unsigned_number ` Select Address。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [参数 P-fce54021b3abaa8a](../../evidence/parameters-sets-019.md#p-fce54021b3abaa8a)

### path-068454

```text
(config-subif)# bsc fdx <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 4 `；EOL ` RVA 0x354B8A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e)

### path-069336

```text
(config-subif)# bsc host-timeout <number:30..3000> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 13 `；EOL ` RVA 0x354B7E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Host inactivity timeout value in deciseconds。

[条件 C-3c8afad2a82a03b1](../../evidence/conditions-sets-023.md#c-3c8afad2a82a03b1) · [参数 P-a8370bda2d7f1bdf](../../evidence/parameters-sets-013.md#p-a8370bda2d7f1bdf)

### path-069387

```text
(config-subif)# bsc pause <number:1..1000> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 5 `；EOL ` RVA 0x354B8818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pause timeout value in tenths of seconds。

[条件 C-a88a46301c962959](../../evidence/conditions-sets-065.md#c-a88a46301c962959) · [参数 P-2e99479a8184bc8c](../../evidence/parameters-sets-004.md#p-2e99479a8184bc8c)

### path-069357

```text
(config-subif)# bsc poll-timeout <number:1..1000> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 7 `；EOL ` RVA 0x354B8178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Poll timeout value in tenths of seconds。

[条件 C-49bc4eeac61ec671](../../evidence/conditions-sets-029.md#c-49bc4eeac61ec671) · [参数 P-7cf80583519b6220](../../evidence/parameters-sets-010.md#p-7cf80583519b6220)

### path-068352

```text
(config-subif)# bsc primary <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 0 `；EOL ` RVA 0x354B6E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e)

### path-069305

```text
(config-subif)# bsc retries <number:1..100> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 8 `；EOL ` RVA 0x354B7AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of retries。

[条件 C-a25a3f3cf22a97d4](../../evidence/conditions-sets-063.md#c-a25a3f3cf22a97d4) · [参数 P-cc73ac87328021c3](../../evidence/parameters-sets-015.md#p-cc73ac87328021c3)

### path-068343

```text
(config-subif)# bsc secondary <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 1 `；EOL ` RVA 0x354B6BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e)

### path-069372

```text
(config-subif)# bsc servlim <number:1..100> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 6 `；EOL ` RVA 0x354B84C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Servlim value as a number。

[条件 C-96509438758347b2](../../evidence/conditions-sets-058.md#c-96509438758347b2) · [参数 P-3a5b6b03ea1d8cad](../../evidence/parameters-sets-005.md#p-3a5b6b03ea1d8cad)

### path-068388

```text
(config-subif)# bsc spec-poll <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 9 `；EOL ` RVA 0x354B7748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e)

### path-069093

```text
(config-subif)# bstun group <number:1..255> <cr>
```

Handler ` RVA 0x113E1E60 `；selector ` 0 `；EOL ` RVA 0x354B5D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` A BSTUN group number from 1 to 255。

[条件 C-463e2fbc9dd48bcd](../../evidence/conditions-sets-027.md#c-463e2fbc9dd48bcd) · [参数 P-86a7a835a111e5a3](../../evidence/parameters-sets-010.md#p-86a7a835a111e5a3)

### path-072652

```text
(config-subif)# bstun route all interface <interface> <cr>
```

Handler ` RVA 0x113E1E60 `；selector ` 1 `；EOL ` RVA 0x354B9338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-99bc31edc8e93a42](../../evidence/conditions-sets-059.md#c-99bc31edc8e93a42) · [缺口 G-4acf9b6d5267c042](../../evidence/gaps-sets-003.md#g-4acf9b6d5267c042) · [参数 P-ba506b2a5cd12d5f](../../evidence/parameters-sets-014.md#p-ba506b2a5cd12d5f) · [状态效果 S-25375d4493f311e7](../../evidence/state_effects-sets-008.md#s-25375d4493f311e7)

### path-071572

```text
(config-subif)# bstun route all tcp <address> <cr>
```

Handler ` RVA 0x113E1E60 `；selector ` 1 `；EOL ` RVA 0x354B9338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote BSTUN peer's IP address。

[条件 C-a06f0de2e242f7dd](../../evidence/conditions-sets-062.md#c-a06f0de2e242f7dd) · [参数 P-e6d3b6f807c79004](../../evidence/parameters-sets-017.md#p-e6d3b6f807c79004) · [状态效果 S-3c2834ab5a2813f3](../../evidence/state_effects-sets-013.md#s-3c2834ab5a2813f3)

### path-068415

```text
(config-subif)# cablelength <number:0..450> <cr>
```

Handler ` RVA 0xED6F530 `；selector ` 6 `；EOL ` RVA 0x34412558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Length of the DS3 cable in feet。

[条件 C-746d082606639c1e](../../evidence/conditions-sets-045.md#c-746d082606639c1e) · [参数 P-c33982c60757d389](../../evidence/parameters-sets-015.md#p-c33982c60757d389)

### path-068234

```text
(config-subif)# carrier-delay <number:0..60> <cr>
```

Handler ` RVA 0xE40DD00 `；selector ` 2 `；EOL ` RVA 0x3413BD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Carrier Transitions delay seconds。

[条件 C-f73ebb0483808119](../../evidence/conditions-sets-095.md#c-f73ebb0483808119) · [参数 P-1e3dfba38bb4d022](../../evidence/parameters-sets-003.md#p-1e3dfba38bb4d022)

### path-068926

```text
(config-subif)# carrier-delay up <number:0..60> <cr>
```

Handler ` RVA 0xE40DCB0 `；selector ` 0 `；EOL ` RVA 0x3413B998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Carrier Up/Down Transitions delay seconds。

[条件 C-9589c59b20e51008](../../evidence/conditions-sets-058.md#c-9589c59b20e51008) · [参数 P-f8b1e65da3600255](../../evidence/parameters-sets-019.md#p-f8b1e65da3600255) · [状态效果 S-b0248c9521fc3813](../../evidence/state_effects-sets-037.md#s-b0248c9521fc3813)

### path-068341

```text
(config-subif)# cdp enable <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 3 `；EOL ` RVA 0x33CE74E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-222e8232a0d9b527](../../evidence/conditions-sets-013.md#c-222e8232a0d9b527)

### path-069256

```text
(config-subif)# cdp filter-tlv-list <string> <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 10 `；EOL ` RVA 0x33CE88D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Filter tlv-list。

[条件 C-f0cf45fa7d4ac8d3](../../evidence/conditions-sets-093.md#c-f0cf45fa7d4ac8d3) · [参数 P-47a81c7d459b9505](../../evidence/parameters-sets-006.md#p-47a81c7d459b9505)

### path-070536

```text
(config-subif)# cdp log mismatch duplex <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 7 `；EOL ` RVA 0x33CE7878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-439c7eb9f9416e31](../../evidence/conditions-sets-026.md#c-439c7eb9f9416e31)

### path-069314

```text
(config-subif)# cdp tlv app <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 8 `；EOL ` RVA 0x33CE8248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cae6bec1476b58f3](../../evidence/conditions-sets-078.md#c-cae6bec1476b58f3) · [状态效果 S-6ee028baf536a33c](../../evidence/state_effects-sets-024.md#s-6ee028baf536a33c)

### path-072396

```text
(config-subif)# cdp tlv app tlvtype <number:1001..65535> value <string> <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 8 `；EOL ` RVA 0x33CE8320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configure App TLV Type information；` string ` Configure App TLV value information。

[条件 C-cae6bec1476b58f3](../../evidence/conditions-sets-078.md#c-cae6bec1476b58f3) · [参数 P-1c1a779fb6ba8023](../../evidence/parameters-sets-003.md#p-1c1a779fb6ba8023) · [状态效果 S-7b9c5e3a03e715c5](../../evidence/state_effects-sets-026.md#s-7b9c5e3a03e715c5)

### path-069238

```text
(config-subif)# cdp tlv location <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 8 `；EOL ` RVA 0x33CE7BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff7c403de075a5bd](../../evidence/conditions-sets-098.md#c-ff7c403de075a5bd) · [状态效果 S-2ca3ca6753e28d62](../../evidence/state_effects-sets-010.md#s-2ca3ca6753e28d62)

### path-069258

```text
(config-subif)# cdp tlv server-location <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 9 `；EOL ` RVA 0x33CE7EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff7c403de075a5bd](../../evidence/conditions-sets-098.md#c-ff7c403de075a5bd)

### path-072534

```text
(config-subif)# channel-group <number:dynamic> <cr>
```

Handler ` RVA 0xE9A5F10 `；selector ` 1 `；EOL ` RVA 0x3436B188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-efdcb81a28220591](../../evidence/conditions-sets-093.md#c-efdcb81a28220591) · [缺口 G-6f347dc1bb4e7378](../../evidence/gaps-sets-004.md#g-6f347dc1bb4e7378) · [参数 P-f98867df9fdf5806](../../evidence/parameters-sets-019.md#p-f98867df9fdf5806)

### path-072611

```text
(config-subif)# channel-group <number:dynamic> mode active <cr>
```

Handler ` RVA 0xE9A5F10 `；selector ` 0 `；EOL ` RVA 0x3436AF88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-f974f416780ac2ed](../../evidence/conditions-sets-096.md#c-f974f416780ac2ed) · [缺口 G-6f347dc1bb4e7378](../../evidence/gaps-sets-004.md#g-6f347dc1bb4e7378) · [参数 P-f98867df9fdf5806](../../evidence/parameters-sets-019.md#p-f98867df9fdf5806) · [状态效果 S-f7375f0efb20a7ed](../../evidence/state_effects-sets-052.md#s-f7375f0efb20a7ed)

### path-069886

```text
(config-subif)# clns access-group <string> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 30 `；EOL ` RVA 0x34B7C800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of filter expression or set。

[条件 C-d6016d05b2d65e24](../../evidence/conditions-sets-083.md#c-d6016d05b2d65e24) · [参数 P-3abec9304f3c295a](../../evidence/parameters-sets-005.md#p-3abec9304f3c295a)

### path-071174

```text
(config-subif)# clns adjacency-filter ES <string> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 33 `；EOL ` RVA 0x34B7CFD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of filter expression or set。

[条件 C-432414daafe8a0a1](../../evidence/conditions-sets-026.md#c-432414daafe8a0a1) · [参数 P-a7e35943b228a6f2](../../evidence/parameters-sets-013.md#p-a7e35943b228a6f2)

### path-068521

```text
(config-subif)# clns checksum <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 9 `；EOL ` RVA 0x34B79FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068531

```text
(config-subif)# clns cluster-alias <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 8 `；EOL ` RVA 0x34B7A298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068116

```text
(config-subif)# clns congestion-threshold <number:0..4294967295> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 10 `；EOL ` RVA 0x34B7A2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets before setting the congestion experience bit。

[条件 C-5d92ce9ca38e4c4f](../../evidence/conditions-sets-036.md#c-5d92ce9ca38e4c4f) · [参数 P-ac2a97a2d7833f4b](../../evidence/parameters-sets-013.md#p-ac2a97a2d7833f4b)

### path-068577

```text
(config-subif)# clns dec-compatible <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 20 `；EOL ` RVA 0x34B7AA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068562

```text
(config-subif)# clns enable <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 11 `；EOL ` RVA 0x34B7A7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068131

```text
(config-subif)# clns erpdu-interval <number:0..4294967295> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 12 `；EOL ` RVA 0x34B7AAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of milliseconds between ERPDUs。

[条件 C-53c6ccd5386a8ff8](../../evidence/conditions-sets-033.md#c-53c6ccd5386a8ff8) · [参数 P-63f6ba7745ba6ec1](../../evidence/parameters-sets-008.md#p-63f6ba7745ba6ec1)

### path-072585

```text
(config-subif)# clns es-neighbor <address> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 13 `；EOL ` RVA 0x34B7B0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` CLNS address or host name。

[条件 C-0b9a1ac08169fd8b](../../evidence/conditions-sets-005.md#c-0b9a1ac08169fd8b) · [缺口 G-fc7e5ec3e8143b2f](../../evidence/gaps-sets-009.md#g-fc7e5ec3e8143b2f) · [参数 P-3b629999e774e7e1](../../evidence/parameters-sets-005.md#p-3b629999e774e7e1) · [状态效果 S-feccd8484d10158b](../../evidence/state_effects-sets-054.md#s-feccd8484d10158b)

### path-069893

```text
(config-subif)# clns esct-time <number:0..65535> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 34 `；EOL ` RVA 0x34B7D338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Configuration time in seconds。

[条件 C-1816f31b34d9fdbd](../../evidence/conditions-sets-009.md#c-1816f31b34d9fdbd) · [参数 P-764becee1bb20a72](../../evidence/parameters-sets-009.md#p-764becee1bb20a72)

### path-068139

```text
(config-subif)# clns mtu <number:512..4294967295> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 15 `；EOL ` RVA 0x34B7B3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CLNS MTU packet size for interface。

[条件 C-22950a135c357afc](../../evidence/conditions-sets-014.md#c-22950a135c357afc) · [参数 P-f75f315f45b190f4](../../evidence/parameters-sets-018.md#p-f75f315f45b190f4)

### path-069467

```text
(config-subif)# clns net <address> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 1 `；EOL ` RVA 0x34B79D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` A CLNS address or host name。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [参数 P-961a29e3f61555f8](../../evidence/parameters-sets-012.md#p-961a29e3f61555f8)

### path-068144

```text
(config-subif)# clns rdpdu-interval <number:0..4294967295> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 16 `；EOL ` RVA 0x34B7B430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum interval between Redirect PDUs in milliseconds。

[条件 C-e01acfcb43f21865](../../evidence/conditions-sets-086.md#c-e01acfcb43f21865) · [参数 P-bd5acb9ae1d7e8bc](../../evidence/parameters-sets-014.md#p-bd5acb9ae1d7e8bc)

### path-068673

```text
(config-subif)# clns route-cache <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 7 `；EOL ` RVA 0x34B7BEB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-069746

```text
(config-subif)# clns router iso-igrp <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 26 `；EOL ` RVA 0x34B7BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-bf51d65d57b8e0fc](../../evidence/state_effects-sets-040.md#s-bf51d65d57b8e0fc)

### path-068668

```text
(config-subif)# clns send-erpdu <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 18 `；EOL ` RVA 0x34B7C150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068679

```text
(config-subif)# clns send-rdpdu <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 19 `；EOL ` RVA 0x34B7C3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068693

```text
(config-subif)# clns split-horizon <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 31 `；EOL ` RVA 0x34B7CC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30)

### path-068243

```text
(config-subif)# clock auto <cr>
```

Handler ` RVA 0xE421F00 `；selector ` 20 `；EOL ` RVA 0x34141588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d0c0d955bb3eaf3](../../evidence/conditions-sets-055.md#c-8d0c0d955bb3eaf3) · [状态效果 S-4af87dbd1a4fda83](../../evidence/state_effects-sets-016.md#s-4af87dbd1a4fda83)

### path-069445

```text
(config-subif)# clock source internal <cr>
```

Handler ` RVA 0xED6B290 `；selector ` 0 `；EOL ` RVA 0x34415AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a36c0be036fb2fdd](../../evidence/conditions-sets-063.md#c-a36c0be036fb2fdd) · [状态效果 S-4fe25b72a8da303b](../../evidence/state_effects-sets-017.md#s-4fe25b72a8da303b)

### path-069081

```text
(config-subif)# clock source line <cr>
```

Handler ` RVA 0xED13570 `；selector ` 0 `；EOL ` RVA 0x34404710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1cb44010a2a0a01](../../evidence/conditions-sets-062.md#c-a1cb44010a2a0a01) · [状态效果 S-2589a4e548170bd3](../../evidence/state_effects-sets-008.md#s-2589a4e548170bd3)

### path-068667

```text
(config-subif)# clockrate <number:1200..8000000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 2 `；EOL ` RVA 0x34417920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `   DCE clock rate (bits per second)。

[条件 C-0d950dd2fe4ca813](../../evidence/conditions-sets-005.md#c-0d950dd2fe4ca813) · [参数 P-b59bac97630e6aa7](../../evidence/parameters-sets-014.md#p-b59bac97630e6aa7)

### path-068634

```text
(config-subif)# clockrate <number:1576..51840000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 2 `；EOL ` RVA 0x34417078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `   HSSI DCE clock rate (bits per second)。

[条件 C-0f3f4a8274a54711](../../evidence/conditions-sets-006.md#c-0f3f4a8274a54711) · [参数 P-7b070450013c75e1](../../evidence/parameters-sets-010.md#p-7b070450013c75e1)

### path-068648

```text
(config-subif)# clockrate <number:246..8064000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 2 `；EOL ` RVA 0x344175C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `   DCE clock rate (bits per second)。

[条件 C-7616352abb643daf](../../evidence/conditions-sets-046.md#c-7616352abb643daf) · [参数 P-3bb5654161eece1c](../../evidence/parameters-sets-005.md#p-3bb5654161eece1c)

### path-068633

```text
(config-subif)# clockrate <number:300..4000000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 0 `；EOL ` RVA 0x34418290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `   Choose clockrate from list above。

[条件 C-d82fcb974e551c7c](../../evidence/conditions-sets-083.md#c-d82fcb974e551c7c) · [参数 P-aa73c157d5df04e2](../../evidence/parameters-sets-013.md#p-aa73c157d5df04e2)

### path-068604

```text
(config-subif)# clockrate <number:300..8000000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 0 `；EOL ` RVA 0x344191C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `   Choose clockrate from list above。

[条件 C-e01f8ba302f0071b](../../evidence/conditions-sets-086.md#c-e01f8ba302f0071b) · [参数 P-754eb1e3145b9a5d](../../evidence/parameters-sets-009.md#p-754eb1e3145b9a5d)

### path-069733

```text
(config-subif)# clockrate line <number:8000..2048000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 0 `；EOL ` RVA 0x34418C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Speed in multiple of 8000。

[条件 C-8b973acb35cedf15](../../evidence/conditions-sets-054.md#c-8b973acb35cedf15) · [参数 P-0b683330c6ea2930](../../evidence/parameters-sets-001.md#p-0b683330c6ea2930) · [状态效果 S-2b1c1b396de1bf84](../../evidence/state_effects-sets-010.md#s-2b1c1b396de1bf84)

### path-069699

```text
(config-subif)# clockrate network <number:56000..2048000> <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 0 `；EOL ` RVA 0x34418690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Speed in multiple of 56000 or 64000, depending on the network-clock base-rate。

[条件 C-2926384789c72882](../../evidence/conditions-sets-016.md#c-2926384789c72882) · [参数 P-c93b6fc0b1eabc71](../../evidence/parameters-sets-015.md#p-c93b6fc0b1eabc71) · [状态效果 S-034d55e40c6d78b4](../../evidence/state_effects-sets-001.md#s-034d55e40c6d78b4)

### path-069653

```text
(config-subif)# clockrate threshold <number:246..8064000> <cr>
```

Handler ` RVA 0xED6B1A0 `；selector ` 0 `；EOL ` RVA 0x34417F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Received clock rate threshold limit for DTE interface。

[条件 C-f2bfa9b209dc3c75](../../evidence/conditions-sets-094.md#c-f2bfa9b209dc3c75) · [参数 P-52c235870c43cb12](../../evidence/parameters-sets-007.md#p-52c235870c43cb12)

### path-068412

```text
(config-subif)# cmns enable <cr>
```

Handler ` RVA 0x105E5970 `；selector ` 2 `；EOL ` RVA 0x34BB3F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2fed3e3230b4922b](../../evidence/conditions-sets-019.md#c-2fed3e3230b4922b)

### path-068080

```text
(config-subif)# compress <cr>
```

Handler ` RVA 0xF423DB0 `；selector ` 0 `；EOL ` RVA 0x346467B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b221999fc10c825](../../evidence/conditions-sets-017.md#c-2b221999fc10c825)

### path-068432

```text
(config-subif)# crc 32 <cr>
```

Handler ` RVA 0xED6DB30 `；selector ` 0 `；EOL ` RVA 0x344137A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b13945f9b7ceb248](../../evidence/conditions-sets-069.md#c-b13945f9b7ceb248) · [状态效果 S-aba5359cb4ab10c7](../../evidence/state_effects-sets-036.md#s-aba5359cb4ab10c7)

### path-069347

```text
(config-subif)# crc bits 5 <cr>
```

Handler ` RVA 0xED6BAE0 `；selector ` 0 `；EOL ` RVA 0x34413508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc8709e3811785c5](../../evidence/conditions-sets-079.md#c-cc8709e3811785c5) · [状态效果 S-86e931b293296e68](../../evidence/state_effects-sets-029.md#s-86e931b293296e68)

### path-068097

```text
(config-subif)# crc4 <cr>
```

Handler ` RVA 0xED6B670 `；selector ` 0 `；EOL ` RVA 0x34415EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-593e4fe1224ba5a2](../../evidence/conditions-sets-035.md#c-593e4fe1224ba5a2)

### path-068786

```text
(config-subif)# cts dot1x <cr>
```

Handler ` RVA 0x13040720 `；selector ` 0 `；EOL ` RVA 0x35A15888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b537ca248c1b16ff](../../evidence/conditions-sets-070.md#c-b537ca248c1b16ff)

### path-071353

```text
(config-subif)# cts layer3 ipv4 policy <cr>
```

Handler ` RVA 0x13040720 `；selector ` 3 `；EOL ` RVA 0x35A154F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd97f0f9607e3400](../../evidence/conditions-sets-073.md#c-bd97f0f9607e3400) · [状态效果 S-8269b6260d2924bc](../../evidence/state_effects-sets-028.md#s-8269b6260d2924bc)

### path-072019

```text
(config-subif)# cts layer3 ipv4 trustsec forwarding <cr>
```

Handler ` RVA 0x13040720 `；selector ` 2 `；EOL ` RVA 0x35A15220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd85a16a29e3c237](../../evidence/conditions-sets-079.md#c-cd85a16a29e3c237) · [状态效果 S-8269b6260d2924bc](../../evidence/state_effects-sets-028.md#s-8269b6260d2924bc)

### path-068791

```text
(config-subif)# cts manual <cr>
```

Handler ` RVA 0x13040720 `；selector ` 1 `；EOL ` RVA 0x35A14D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-096becc58f5b1097](../../evidence/conditions-sets-004.md#c-096becc58f5b1097)

### path-070064

```text
(config-subif)# cts role-based enforcement <cr>
```

Handler ` RVA 0x14203460 `；selector ` 0 `；EOL ` RVA 0x35CFC1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cff03687408d0b54](../../evidence/conditions-sets-080.md#c-cff03687408d0b54) · [状态效果 S-f54fb25d5e348ce9](../../evidence/state_effects-sets-052.md#s-f54fb25d5e348ce9)

### path-071415

```text
(config-subif)# cts role-based sgt-cache egress <cr>
```

Handler ` RVA 0x1413CA60 `；selector ` 165 `；EOL ` RVA 0x35CE9B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-131d7e3af93e1a95](../../evidence/conditions-sets-008.md#c-131d7e3af93e1a95)

### path-071401

```text
(config-subif)# cts role-based sgt-cache ingress <cr>
```

Handler ` RVA 0x1413CA60 `；selector ` 164 `；EOL ` RVA 0x35CE98B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c5d2a7602ef2991](../../evidence/conditions-sets-048.md#c-7c5d2a7602ef2991)

### path-072060

```text
(config-subif)# cts role-based sgt-map security-group <string> <cr>
```

Handler ` RVA 0x14045110 `；selector ` 1 `；EOL ` RVA 0x35CE9418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` security group name。

[条件 C-373acbed5f599072](../../evidence/conditions-sets-021.md#c-373acbed5f599072) · [参数 P-b3e22bf0acebc139](../../evidence/parameters-sets-014.md#p-b3e22bf0acebc139)

### path-072484

```text
(config-subif)# cts role-based sgt-map vlanid <number:1..4094> sgt <number:2..65521> <cr>
```

Handler ` RVA 0x14045110 `；selector ` 2 `；EOL ` RVA 0x35CE9048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VLAN id；` unsigned_number ` Security Group Tag value。

[条件 C-6ce8589252aadfae](../../evidence/conditions-sets-042.md#c-6ce8589252aadfae) · [参数 P-4163ac767e47dc67](../../evidence/parameters-sets-006.md#p-4163ac767e47dc67) · [状态效果 S-afb896fc49f58312](../../evidence/state_effects-sets-037.md#s-afb896fc49f58312)

### path-069652

```text
(config-subif)# cts sgt inline <cr>
```

Handler ` RVA 0x108DB4B0 `；selector ` 1 `；EOL ` RVA 0x34BF4398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce44c09d5ce1521b](../../evidence/conditions-sets-079.md#c-ce44c09d5ce1521b)

### path-068739

```text
(config-subif)# cwmp wan <cr>
```

Handler ` RVA 0x16470900 `；selector ` 7 `；EOL ` RVA 0x35F8E350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0690559e124817f](../../evidence/conditions-sets-062.md#c-a0690559e124817f)

### path-069895

```text
(config-subif)# cwmp wan default <cr>
```

Handler ` RVA 0x16470900 `；selector ` 8 `；EOL ` RVA 0x35F8E0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0690559e124817f](../../evidence/conditions-sets-062.md#c-a0690559e124817f)

### path-068053

```text
(config-subif)# dampening <cr>
```

Handler ` RVA 0xDFF5AC0 `；selector ` 0 `；EOL ` RVA 0x3412DF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29d0a8382d66c45a](../../evidence/conditions-sets-016.md#c-29d0a8382d66c45a)

### path-068120

```text
(config-subif)# dce-terminal-timing-enable <cr>
```

Handler ` RVA 0xED6C030 `；selector ` 0 `；EOL ` RVA 0x34419760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9d7aedba52dd850](../../evidence/conditions-sets-066.md#c-a9d7aedba52dd850)

### path-070399

```text
(config-subif)# default aaa connect-info <string> <cr>
```

Handler ` RVA 0xE075DC0 `；selector ` 72 `；EOL ` RVA 0x3419C2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` connect-info。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682) · [参数 P-23ea33b390829d45](../../evidence/parameters-sets-003.md#p-23ea33b390829d45) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069600

```text
(config-subif)# default access-expression input <cr>
```

Handler ` RVA 0x1E3FC780 `；selector ` 0 `；EOL ` RVA 0x345EC7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d982256c0ee87c6](../../evidence/conditions-sets-055.md#c-8d982256c0ee87c6) · [状态效果 S-aae9a7d91bf8b724](../../evidence/state_effects-sets-036.md#s-aae9a7d91bf8b724)

### path-069742

```text
(config-subif)# default access-session closed <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 2 `；EOL ` RVA 0x33BA55D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7b70ab64f158610](../../evidence/conditions-sets-083.md#c-d7b70ab64f158610) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069829

```text
(config-subif)# default access-session control-direction <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 4 `；EOL ` RVA 0x33BA5CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64252277a3833b95](../../evidence/conditions-sets-039.md#c-64252277a3833b95) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069713

```text
(config-subif)# default access-session host-mode <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 1 `；EOL ` RVA 0x33BA4CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fdfff696a45d0237](../../evidence/conditions-sets-098.md#c-fdfff696a45d0237) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071810

```text
(config-subif)# default access-session inherit disable service-policy <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 7 `；EOL ` RVA 0x33BA6680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-366c2145c1d195d1](../../evidence/conditions-sets-021.md#c-366c2145c1d195d1) · [状态效果 S-947376f7746ad5ed](../../evidence/state_effects-sets-031.md#s-947376f7746ad5ed)

### path-071164

```text
(config-subif)# default access-session interface-template sticky <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 6 `；EOL ` RVA 0x33BA60D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7b70ab64f158610](../../evidence/conditions-sets-083.md#c-d7b70ab64f158610) · [状态效果 S-d305537fa8cd3b02](../../evidence/state_effects-sets-045.md#s-d305537fa8cd3b02)

### path-069748

```text
(config-subif)# default access-session limit <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 9 `；EOL ` RVA 0x33BA5258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98ec9cebc84f91fc](../../evidence/conditions-sets-059.md#c-98ec9cebc84f91fc) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069636

```text
(config-subif)# default access-session monitor <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 10 `；EOL ` RVA 0x33BA4940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1f8877db32c126ab](../../evidence/conditions-sets-012.md#c-1f8877db32c126ab) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069803

```text
(config-subif)# default access-session port-control <cr>
```

Handler ` RVA 0xCAECB20 `；selector ` 3 `；EOL ` RVA 0x33BA5910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aa31777777c7330b](../../evidence/conditions-sets-066.md#c-aa31777777c7330b) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071341

```text
(config-subif)# default alps ascu <number:33..79> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 8 `；EOL ` RVA 0x354201A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  RID value。

[条件 C-0a4668f7a9da7767](../../evidence/conditions-sets-004.md#c-0a4668f7a9da7767) · [参数 P-99e755fa8bd22d3d](../../evidence/parameters-sets-012.md#p-99e755fa8bd22d3d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071329

```text
(config-subif)# default alps ascu <number:65..126> <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 8 `；EOL ` RVA 0x3541DE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Interchange address。

[条件 C-e45d57df3a3beb07](../../evidence/conditions-sets-088.md#c-e45d57df3a3beb07) · [参数 P-3f81ae14511241f6](../../evidence/parameters-sets-005.md#p-3f81ae14511241f6) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072480

```text
(config-subif)# default alps host-hld <number:1..65535> host-link <number:1..255> ax25 <cr>
```

Handler ` RVA 0x11213450 `；selector ` 0 `；EOL ` RVA 0x3541D688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Host HLD Number；` unsigned_number ` Host-link identifier number。

[条件 C-d1fccaa4aac6a927](../../evidence/conditions-sets-081.md#c-d1fccaa4aac6a927) · [参数 P-05eb6bb78df80933](../../evidence/parameters-sets-001.md#p-05eb6bb78df80933) · [状态效果 S-d3b6646c2c3a2705](../../evidence/state_effects-sets-045.md#s-d3b6646c2c3a2705)

### path-068823

```text
(config-subif)# default alps n1 <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 2 `；EOL ` RVA 0x3541E3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9206bbcfe44a3a48](../../evidence/conditions-sets-056.md#c-9206bbcfe44a3a48) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068827

```text
(config-subif)# default alps n2 <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 3 `；EOL ` RVA 0x3541E660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-72bfd64d6e4ce121](../../evidence/conditions-sets-044.md#c-72bfd64d6e4ce121) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068838

```text
(config-subif)# default alps n3 <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 4 `；EOL ` RVA 0x3541EBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d2e2a49adda5e29](../../evidence/conditions-sets-005.md#c-0d2e2a49adda5e29) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068843

```text
(config-subif)# default alps poll-pause <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 6 `；EOL ` RVA 0x3541F128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f4bf8cd3024dd978](../../evidence/conditions-sets-094.md#c-f4bf8cd3024dd978) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072066

```text
(config-subif)# default alps service-msg data-drop msg-term <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 11 `；EOL ` RVA 0x3541FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f89c7d8c0030845](../../evidence/conditions-sets-025.md#c-3f89c7d8c0030845) · [状态效果 S-932233a596b02191](../../evidence/state_effects-sets-031.md#s-932233a596b02191)

### path-072063

```text
(config-subif)# default alps service-msg format sita <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 9 `；EOL ` RVA 0x3541F750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f89c7d8c0030845](../../evidence/conditions-sets-025.md#c-3f89c7d8c0030845) · [状态效果 S-420c8b6839b3b2e5](../../evidence/state_effects-sets-014.md#s-420c8b6839b3b2e5)

### path-071438

```text
(config-subif)# default alps service-msg status-change <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 10 `；EOL ` RVA 0x3541FDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f89c7d8c0030845](../../evidence/conditions-sets-025.md#c-3f89c7d8c0030845) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068839

```text
(config-subif)# default alps servlim <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 5 `；EOL ` RVA 0x3541EEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1e69122b2d1f955a](../../evidence/conditions-sets-012.md#c-1e69122b2d1f955a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070094

```text
(config-subif)# default alps syn-bcc-calc <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 7 `；EOL ` RVA 0x3541EE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dc3bd141197c0f38](../../evidence/conditions-sets-085.md#c-dc3bd141197c0f38) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068804

```text
(config-subif)# default alps t1 <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 0 `；EOL ` RVA 0x3541DE18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-de6e83e9109fd72f](../../evidence/conditions-sets-086.md#c-de6e83e9109fd72f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068822

```text
(config-subif)# default alps t2 <cr>
```

Handler ` RVA 0x11213B30 `；selector ` 1 `；EOL ` RVA 0x3541E380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f539f24656c0fe7a](../../evidence/conditions-sets-095.md#c-f539f24656c0fe7a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072018

```text
(config-subif)# default alps translate <string> <address> <cr>
```

Handler ` RVA 0x11213450 `；selector ` 1 `；EOL ` RVA 0x3541DAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` X.121 address of remote peer；` address ` IP address for remote peer。

[条件 C-d1fccaa4aac6a927](../../evidence/conditions-sets-081.md#c-d1fccaa4aac6a927) · [参数 P-bb34929031a00e82](../../evidence/parameters-sets-014.md#p-bb34929031a00e82) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070527

```text
(config-subif)# default amt gateway relay-address <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 2 `；EOL ` RVA 0x3386B160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c545e478a063b8d2](../../evidence/conditions-sets-076.md#c-c545e478a063b8d2) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071552

```text
(config-subif)# default amt gateway traffic ip <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 1 `；EOL ` RVA 0x3386ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23795068f56fdfa1](../../evidence/conditions-sets-014.md#c-23795068f56fdfa1) · [状态效果 S-dd72d3a8c9fb1542](../../evidence/state_effects-sets-047.md#s-dd72d3a8c9fb1542)

### path-071587

```text
(config-subif)# default amt relay maximum gateway <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 4 `；EOL ` RVA 0x3386B898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-081126a80717ad29](../../evidence/conditions-sets-004.md#c-081126a80717ad29) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071555

```text
(config-subif)# default amt relay traffic ip <cr>
```

Handler ` RVA 0xBB7E9F0 `；selector ` 3 `；EOL ` RVA 0x3386B4C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23795068f56fdfa1](../../evidence/conditions-sets-014.md#c-23795068f56fdfa1) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069159

```text
(config-subif)# default ancp enable <cr>
```

Handler ` RVA 0xB2613A0 `；selector ` 2 `；EOL ` RVA 0x336D75B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5cf0b543e4023735](../../evidence/conditions-sets-036.md#c-5cf0b543e4023735) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072395

```text
(config-subif)# default ancp neighbor name <string> client-id <string> <cr>
```

Handler ` RVA 0xB2613A0 `；selector ` 3 `；EOL ` RVA 0x336D7A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP client ID。

[条件 C-cd99058cee2d045c](../../evidence/conditions-sets-079.md#c-cd99058cee2d045c) · [参数 P-3eed75d6b4785b53](../../evidence/parameters-sets-005.md#p-3eed75d6b4785b53) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069216

```text
(config-subif)# default arp arpa <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 1 `；EOL ` RVA 0x33D3E920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069281

```text
(config-subif)# default arp authorized <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 10 `；EOL ` RVA 0x33D3F118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070751

```text
(config-subif)# default arp entries interface-limit <cr>
```

Handler ` RVA 0xCD664F0 `；selector ` 0 `；EOL ` RVA 0x33D3FE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-03829c7f9b4e5c71](../../evidence/conditions-sets-002.md#c-03829c7f9b4e5c71) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069244

```text
(config-subif)# default arp frame-relay <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 7 `；EOL ` RVA 0x33D3EBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071712

```text
(config-subif)# default arp log threshold entries <cr>
```

Handler ` RVA 0xCD62360 `；selector ` 0 `；EOL ` RVA 0x33D3FAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a528a201eae6e51](../../evidence/conditions-sets-035.md#c-5a528a201eae6e51) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070655

```text
(config-subif)# default arp packet-priority enable <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 11 `；EOL ` RVA 0x33D3F6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069249

```text
(config-subif)# default arp probe <cr>
```

Handler ` RVA 0xCF75970 `；selector ` 0 `；EOL ` RVA 0x33D3E5B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-194896e03b7fc2f9](../../evidence/conditions-sets-010.md#c-194896e03b7fc2f9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069261

```text
(config-subif)# default arp snap <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 3 `；EOL ` RVA 0x33D3EE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-324c20abb67658b0](../../evidence/conditions-sets-020.md#c-324c20abb67658b0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068428

```text
(config-subif)# default arp timeout <cr>
```

Handler ` RVA 0xCF5B390 `；selector ` 6 `；EOL ` RVA 0x33D3F140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-335f6d025c0a7fc9](../../evidence/conditions-sets-020.md#c-335f6d025c0a7fc9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069142

```text
(config-subif)# default asp addr-offset <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 2 `；EOL ` RVA 0x354A4178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c8fbe651fe036a81](../../evidence/conditions-sets-077.md#c-c8fbe651fe036a81) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069140

```text
(config-subif)# default asp assert-dtr <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 3 `；EOL ` RVA 0x354A4468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f66a5b56a1d87f0](../../evidence/conditions-sets-019.md#c-2f66a5b56a1d87f0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069123

```text
(config-subif)# default asp role <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 1 `；EOL ` RVA 0x354A3DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-255412a1d9dcdc8a](../../evidence/conditions-sets-015.md#c-255412a1d9dcdc8a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069196

```text
(config-subif)# default asp rx-ift <cr>
```

Handler ` RVA 0x113A1050 `；selector ` 0 `；EOL ` RVA 0x354A4780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f92526b9c998d5cd](../../evidence/conditions-sets-096.md#c-f92526b9c998d5cd) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071089

```text
(config-subif)# default async default routing <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 3 `；EOL ` RVA 0x34931ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3ee0ab0468397a6d](../../evidence/conditions-sets-024.md#c-3ee0ab0468397a6d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071111

```text
(config-subif)# default async dynamic address <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 5 `；EOL ` RVA 0x349321C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3ee0ab0468397a6d](../../evidence/conditions-sets-024.md#c-3ee0ab0468397a6d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071134

```text
(config-subif)# default async dynamic routing <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 4 `；EOL ` RVA 0x34932470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3ee0ab0468397a6d](../../evidence/conditions-sets-024.md#c-3ee0ab0468397a6d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069866

```text
(config-subif)# default async mode <cr>
```

Handler ` RVA 0xFF4A2D0 `；selector ` 2 `；EOL ` RVA 0x34932770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81f361d4443cec2f](../../evidence/conditions-sets-050.md#c-81f361d4443cec2f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071669

```text
(config-subif)# default atm-dxi interface-dfa <number:0..15> <number:0..63> <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 2 `；EOL ` RVA 0x344804C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` VPI；` unsigned_number ` VCI。

[条件 C-51e6acc51068bf50](../../evidence/conditions-sets-032.md#c-51e6acc51068bf50) · [参数 P-d29bbb695865bd3a](../../evidence/parameters-sets-016.md#p-d29bbb695865bd3a) · [状态效果 S-328bb457e8e01326](../../evidence/state_effects-sets-011.md#s-328bb457e8e01326)

### path-071657

```text
(config-subif)# default atm-dxi pvc <number:0..15> <number:0..63> <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 3 `；EOL ` RVA 0x3447FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` VPI；` unsigned_number ` VCI。

[条件 C-51e6acc51068bf50](../../evidence/conditions-sets-032.md#c-51e6acc51068bf50) · [参数 P-1d192fe15f08040c](../../evidence/parameters-sets-003.md#p-1d192fe15f08040c) · [状态效果 S-dd5a735e0b56104a](../../evidence/state_effects-sets-047.md#s-dd5a735e0b56104a)

### path-069280

```text
(config-subif)# default atm-dxi zap <cr>
```

Handler ` RVA 0xEF30DC0 `；selector ` 1 `；EOL ` RVA 0x34480870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-51e6acc51068bf50](../../evidence/conditions-sets-032.md#c-51e6acc51068bf50) · [状态效果 S-c120c095d4242429](../../evidence/state_effects-sets-041.md#s-c120c095d4242429)

### path-069775

```text
(config-subif)# default authentication control-direction <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 6 `；EOL ` RVA 0x33B95940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5945b34988b4d482](../../evidence/conditions-sets-035.md#c-5945b34988b4d482) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071144

```text
(config-subif)# default authentication event fail <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x33B91810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2af501e59d917570](../../evidence/conditions-sets-017.md#c-2af501e59d917570) · [状态效果 S-522aaa4898e1752e](../../evidence/state_effects-sets-018.md#s-522aaa4898e1752e)

### path-072468

```text
(config-subif)# default authentication event fail action authorize vlan <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5DC20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c813a92fde0a7a9](../../evidence/conditions-sets-054.md#c-8c813a92fde0a7a9) · [状态效果 S-0808ad0c02f9e451](../../evidence/state_effects-sets-002.md#s-0808ad0c02f9e451)

### path-072470

```text
(config-subif)# default authentication event fail action authorize vlan <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5CF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-99fe1777a8fab2e6](../../evidence/conditions-sets-060.md#c-99fe1777a8fab2e6) · [状态效果 S-0808ad0c02f9e451](../../evidence/state_effects-sets-002.md#s-0808ad0c02f9e451)

### path-072472

```text
(config-subif)# default authentication event fail action authorize vlan <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5E670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-daad5ac5e5436348](../../evidence/conditions-sets-084.md#c-daad5ac5e5436348) · [状态效果 S-0808ad0c02f9e451](../../evidence/state_effects-sets-002.md#s-0808ad0c02f9e451)

### path-069804

```text
(config-subif)# default authentication fallback <cr>
```

Handler ` RVA 0xCAF51B0 `；selector ` 11 `；EOL ` RVA 0x33BAB150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-04eeac9d08a1be3f](../../evidence/conditions-sets-002.md#c-04eeac9d08a1be3f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069683

```text
(config-subif)# default authentication host-mode <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 3 `；EOL ` RVA 0x33B94D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4183f3a8a0cd4b22](../../evidence/conditions-sets-026.md#c-4183f3a8a0cd4b22) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069706

```text
(config-subif)# default authentication open <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 4 `；EOL ` RVA 0x33B95220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ab445ba1bd574f7](../../evidence/conditions-sets-054.md#c-8ab445ba1bd574f7) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069639

```text
(config-subif)# default authentication order <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 1 `；EOL ` RVA 0x33B91150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5443ad3801d135ca](../../evidence/conditions-sets-033.md#c-5443ad3801d135ca) · [状态效果 S-e8a3ab3d166846e0](../../evidence/state_effects-sets-049.md#s-e8a3ab3d166846e0)

### path-069618

```text
(config-subif)# default authentication periodic <cr>
```

Handler ` RVA 0xCAD2B80 `；selector ` 8 `；EOL ` RVA 0x33B939F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c17387c0a674ce8e](../../evidence/conditions-sets-075.md#c-c17387c0a674ce8e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069749

```text
(config-subif)# default authentication port-control <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 5 `；EOL ` RVA 0x33B95558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e1e28f1e8bd733c](../../evidence/conditions-sets-061.md#c-9e1e28f1e8bd733c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069660

```text
(config-subif)# default authentication priority <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 2 `；EOL ` RVA 0x33B913D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-28009bd39fce3c02](../../evidence/conditions-sets-016.md#c-28009bd39fce3c02) · [状态效果 S-bad6656aee770c3c](../../evidence/state_effects-sets-039.md#s-bad6656aee770c3c)

### path-070982

```text
(config-subif)# default authentication timer reauthenticate <cr>
```

Handler ` RVA 0xCAD2B80 `；selector ` 9 `；EOL ` RVA 0x33B93DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-edf1ce0acc561ac6](../../evidence/conditions-sets-092.md#c-edf1ce0acc561ac6) · [状态效果 S-1682086566758565](../../evidence/state_effects-sets-005.md#s-1682086566758565)

### path-071033

```text
(config-subif)# default authentication timer restart <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 9 `；EOL ` RVA 0x33B94168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34f6102f83775c2d](../../evidence/conditions-sets-021.md#c-34f6102f83775c2d) · [状态效果 S-835678a09a4db059](../../evidence/state_effects-sets-028.md#s-835678a09a4db059)

### path-069714

```text
(config-subif)# default authentication violation <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 10 `；EOL ` RVA 0x33B946B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-edd919bcd6dcb827](../../evidence/conditions-sets-092.md#c-edd919bcd6dcb827) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069096

```text
(config-subif)# default autodetect encapsulation <cr>
```

Handler ` RVA 0xED73570 `；selector ` 0 `；EOL ` RVA 0x3441FC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5128da435f7d95b](../../evidence/conditions-sets-095.md#c-f5128da435f7d95b) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068826

```text
(config-subif)# default autostate <cr>
```

Handler ` RVA 0x15DB5230 `；selector ` 0 `；EOL ` RVA 0x35E321A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4c5d4346d4bfef45](../../evidence/conditions-sets-030.md#c-4c5d4346d4bfef45) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070282

```text
(config-subif)# default backup active interface <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 3 `；EOL ` RVA 0x34482FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3de6edb7e9aca37c](../../evidence/conditions-sets-024.md#c-3de6edb7e9aca37c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068894

```text
(config-subif)# default backup delay <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 1 `；EOL ` RVA 0x344822F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ee52336d2b9dfc5c](../../evidence/conditions-sets-092.md#c-ee52336d2b9dfc5c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068901

```text
(config-subif)# default backup interface <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 0 `；EOL ` RVA 0x34482748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9c9a67fb6d075451](../../evidence/conditions-sets-060.md#c-9c9a67fb6d075451) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068906

```text
(config-subif)# default backup load <cr>
```

Handler ` RVA 0xEF355D0 `；selector ` 2 `；EOL ` RVA 0x34482B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5637b55a83770768](../../evidence/conditions-sets-034.md#c-5637b55a83770768) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068222

```text
(config-subif)# default bandwidth <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 0 `；EOL ` RVA 0x3412F6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7da0b54a01a40a5](../../evidence/conditions-sets-083.md#c-d7da0b54a01a40a5) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068884

```text
(config-subif)# default bandwidth inherit <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 10 `；EOL ` RVA 0x34130BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8907bcc8c152b13c](../../evidence/conditions-sets-053.md#c-8907bcc8c152b13c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068891

```text
(config-subif)# default bandwidth qos-reference <cr>
```

Handler ` RVA 0xDA50C00 `；selector ` 0 `；EOL ` RVA 0x34130F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e6074dc8de0f3f8](../../evidence/conditions-sets-061.md#c-9e6074dc8de0f3f8) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068887

```text
(config-subif)# default bandwidth receive <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 7 `；EOL ` RVA 0x34130040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-35b7ee85a5064c65](../../evidence/conditions-sets-021.md#c-35b7ee85a5064c65) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070268

```text
(config-subif)# default bandwidth receive inherit <cr>
```

Handler ` RVA 0xE40BD30 `；selector ` 13 `；EOL ` RVA 0x34131278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-35b7ee85a5064c65](../../evidence/conditions-sets-021.md#c-35b7ee85a5064c65) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069395

```text
(config-subif)# default bfd echo <cr>
```

Handler ` RVA 0x10B1DA10 `；selector ` 0 `；EOL ` RVA 0x34CB1848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70a3b5d50c196784](../../evidence/conditions-sets-044.md#c-70a3b5d50c196784) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069353

```text
(config-subif)# default bfd enable <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 7 `；EOL ` RVA 0x34CB1278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069338

```text
(config-subif)# default bfd interval <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 1 `；EOL ` RVA 0x34CB0AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-276e221bdcce110b](../../evidence/conditions-sets-015.md#c-276e221bdcce110b) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069275

```text
(config-subif)# default bfd jitter <cr>
```

Handler ` RVA 0x10B1D640 `；selector ` 0 `；EOL ` RVA 0x34CB0790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070701

```text
(config-subif)# default bfd local-address <string> <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 8 `；EOL ` RVA 0x34CB1588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ip/ipv6 address。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [参数 P-743928651798c75c](../../evidence/parameters-sets-009.md#p-743928651798c75c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070712

```text
(config-subif)# default bfd neighbor <address> <cr>
```

Handler ` RVA 0x10B4B690 `；selector ` 2 `；EOL ` RVA 0x34CB1D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Neighbor ip address。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [参数 P-f55bdc2ac59ef37f](../../evidence/parameters-sets-018.md#p-f55bdc2ac59ef37f) · [状态效果 S-1b2194e5047a8773](../../evidence/state_effects-sets-006.md#s-1b2194e5047a8773)

### path-070654

```text
(config-subif)# default bfd template <string> <cr>
```

Handler ` RVA 0x10B1E3E0 `；selector ` 6 `；EOL ` RVA 0x34CB0FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` bfd template name。

[条件 C-580b33656759f8b9](../../evidence/conditions-sets-034.md#c-580b33656759f8b9) · [参数 P-b185832473e42b32](../../evidence/parameters-sets-013.md#p-b185832473e42b32) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069318

```text
(config-subif)# default bgp-policy accounting <cr>
```

Handler ` RVA 0xB6219A0 `；selector ` 0 `；EOL ` RVA 0x337C76C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84ca569e31294829](../../evidence/conditions-sets-051.md#c-84ca569e31294829) · [状态效果 S-d7def8f0b270de18](../../evidence/state_effects-sets-046.md#s-d7def8f0b270de18)

### path-069642

```text
(config-subif)# default bridge-group <number:1..255> <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 1 `；EOL ` RVA 0x345E91A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-7800d77b44caac6d](../../evidence/conditions-sets-047.md#c-7800d77b44caac6d) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069695

```text
(config-subif)# default bridge-group <number:1..255> circuit-group <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 3 `；EOL ` RVA 0x345E9780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-acf7103fe619ff3d](../../evidence/conditions-sets-067.md#c-acf7103fe619ff3d) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071007

```text
(config-subif)# default bridge-group <number:1..255> subscriber-loop-control <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 25 `；EOL ` RVA 0x345E97C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-b5588029c06e0f41](../../evidence/conditions-sets-070.md#c-b5588029c06e0f41) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071006

```text
(config-subif)# default bridge-group <number:1..255> subscriber-trunk <cr>
```

Handler ` RVA 0xF28B6A0 `；selector ` 23 `；EOL ` RVA 0x345E94E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Assign an interface to a Bridge Group.。

[条件 C-c11a8a1b77009055](../../evidence/conditions-sets-075.md#c-c11a8a1b77009055) · [参数 P-0a8abac33701b252](../../evidence/parameters-sets-001.md#p-0a8abac33701b252) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069225

```text
(config-subif)# default bsc char-int <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 11 `；EOL ` RVA 0x354B74A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069122

```text
(config-subif)# default bsc char-set <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 3 `；EOL ` RVA 0x354B6170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-180dce10c206d88f](../../evidence/conditions-sets-009.md#c-180dce10c206d88f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069201

```text
(config-subif)# default bsc contention <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 2 `；EOL ` RVA 0x354B6920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-ee9bd0a026727a9f](../../evidence/state_effects-sets-050.md#s-ee9bd0a026727a9f)

### path-069166

```text
(config-subif)# default bsc dial-contention <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 12 `；EOL ` RVA 0x354B65C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-4b308674a6c532b7](../../evidence/state_effects-sets-016.md#s-4b308674a6c532b7)

### path-069386

```text
(config-subif)# default bsc discard-syns <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 14 `；EOL ` RVA 0x354B8D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071594

```text
(config-subif)# default bsc extended-address <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 10 `；EOL ` RVA 0x354B7218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Poll address；` unsigned_number ` Select Address。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [参数 P-fce54021b3abaa8a](../../evidence/parameters-sets-019.md#p-fce54021b3abaa8a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069370

```text
(config-subif)# default bsc fdx <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 4 `；EOL ` RVA 0x354B8A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070664

```text
(config-subif)# default bsc host-timeout <number:30..3000> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 13 `；EOL ` RVA 0x354B7E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Host inactivity timeout value in deciseconds。

[条件 C-41bad6889bc74788](../../evidence/conditions-sets-026.md#c-41bad6889bc74788) · [参数 P-a8370bda2d7f1bdf](../../evidence/parameters-sets-013.md#p-a8370bda2d7f1bdf) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070735

```text
(config-subif)# default bsc pause <number:1..1000> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 5 `；EOL ` RVA 0x354B8818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pause timeout value in tenths of seconds。

[条件 C-3f20130b9fcd02f0](../../evidence/conditions-sets-024.md#c-3f20130b9fcd02f0) · [参数 P-2e99479a8184bc8c](../../evidence/parameters-sets-004.md#p-2e99479a8184bc8c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070691

```text
(config-subif)# default bsc poll-timeout <number:1..1000> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 7 `；EOL ` RVA 0x354B8178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Poll timeout value in tenths of seconds。

[条件 C-4bee458474366cf1](../../evidence/conditions-sets-030.md#c-4bee458474366cf1) · [参数 P-7cf80583519b6220](../../evidence/parameters-sets-010.md#p-7cf80583519b6220) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069156

```text
(config-subif)# default bsc primary <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 0 `；EOL ` RVA 0x354B6E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070633

```text
(config-subif)# default bsc retries <number:1..100> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 8 `；EOL ` RVA 0x354B7AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of retries。

[条件 C-ab8750e0e80b9d00](../../evidence/conditions-sets-066.md#c-ab8750e0e80b9d00) · [参数 P-cc73ac87328021c3](../../evidence/parameters-sets-015.md#p-cc73ac87328021c3) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069135

```text
(config-subif)# default bsc secondary <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 1 `；EOL ` RVA 0x354B6BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070710

```text
(config-subif)# default bsc servlim <number:1..100> <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 6 `；EOL ` RVA 0x354B84C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Servlim value as a number。

[条件 C-8c2228df6280c614](../../evidence/conditions-sets-054.md#c-8c2228df6280c614) · [参数 P-3a5b6b03ea1d8cad](../../evidence/parameters-sets-005.md#p-3a5b6b03ea1d8cad) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069247

```text
(config-subif)# default bsc spec-poll <cr>
```

Handler ` RVA 0x113C2D60 `；selector ` 9 `；EOL ` RVA 0x354B7748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c54e430c53d4c21e](../../evidence/conditions-sets-076.md#c-c54e430c53d4c21e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070462

```text
(config-subif)# default bstun group <number:1..255> <cr>
```

Handler ` RVA 0x113E1E60 `；selector ` 0 `；EOL ` RVA 0x354B5D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` A BSTUN group number from 1 to 255。

[条件 C-463e2fbc9dd48bcd](../../evidence/conditions-sets-027.md#c-463e2fbc9dd48bcd) · [参数 P-86a7a835a111e5a3](../../evidence/parameters-sets-010.md#p-86a7a835a111e5a3) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072163

```text
(config-subif)# default bstun route all tcp <address> <cr>
```

Handler ` RVA 0x113E1E60 `；selector ` 1 `；EOL ` RVA 0x354B9338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Remote BSTUN peer's IP address。

[条件 C-a06f0de2e242f7dd](../../evidence/conditions-sets-062.md#c-a06f0de2e242f7dd) · [参数 P-e6d3b6f807c79004](../../evidence/parameters-sets-017.md#p-e6d3b6f807c79004) · [状态效果 S-c778fd81ce78d924](../../evidence/state_effects-sets-042.md#s-c778fd81ce78d924)

### path-068420

```text
(config-subif)# default cablelength <cr>
```

Handler ` RVA 0xED6F530 `；selector ` 6 `；EOL ` RVA 0x34412558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5e17e8a829dc619c](../../evidence/conditions-sets-037.md#c-5e17e8a829dc619c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068233

```text
(config-subif)# default carrier-delay <cr>
```

Handler ` RVA 0xE40DD00 `；selector ` 2 `；EOL ` RVA 0x3413BD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e0a18ea9d0abe976](../../evidence/conditions-sets-086.md#c-e0a18ea9d0abe976) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068929

```text
(config-subif)# default carrier-delay up <cr>
```

Handler ` RVA 0xE40DCB0 `；selector ` 0 `；EOL ` RVA 0x3413B998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-acc3798e03be9cf8](../../evidence/conditions-sets-067.md#c-acc3798e03be9cf8) · [状态效果 S-2d51781d5e7cab2c](../../evidence/state_effects-sets-010.md#s-2d51781d5e7cab2c)

### path-069129

```text
(config-subif)# default cdp enable <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 3 `；EOL ` RVA 0x33CE74E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-222e8232a0d9b527](../../evidence/conditions-sets-013.md#c-222e8232a0d9b527) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070596

```text
(config-subif)# default cdp filter-tlv-list <string> <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 10 `；EOL ` RVA 0x33CE88D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Filter tlv-list。

[条件 C-f0cf45fa7d4ac8d3](../../evidence/conditions-sets-093.md#c-f0cf45fa7d4ac8d3) · [参数 P-47a81c7d459b9505](../../evidence/parameters-sets-006.md#p-47a81c7d459b9505) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071580

```text
(config-subif)# default cdp log mismatch duplex <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 7 `；EOL ` RVA 0x33CE7878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-439c7eb9f9416e31](../../evidence/conditions-sets-026.md#c-439c7eb9f9416e31) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070642

```text
(config-subif)# default cdp tlv app <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 8 `；EOL ` RVA 0x33CE8248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cae6bec1476b58f3](../../evidence/conditions-sets-078.md#c-cae6bec1476b58f3) · [状态效果 S-0aed58039493085c](../../evidence/state_effects-sets-003.md#s-0aed58039493085c)

### path-072495

```text
(config-subif)# default cdp tlv app tlvtype <number:1001..65535> value <string> <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 8 `；EOL ` RVA 0x33CE8320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Configure App TLV Type information；` string ` Configure App TLV value information。

[条件 C-cae6bec1476b58f3](../../evidence/conditions-sets-078.md#c-cae6bec1476b58f3) · [参数 P-1c1a779fb6ba8023](../../evidence/parameters-sets-003.md#p-1c1a779fb6ba8023) · [状态效果 S-805c183b5fcfd5f0](../../evidence/state_effects-sets-027.md#s-805c183b5fcfd5f0)

### path-070578

```text
(config-subif)# default cdp tlv location <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 8 `；EOL ` RVA 0x33CE7BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff7c403de075a5bd](../../evidence/conditions-sets-098.md#c-ff7c403de075a5bd) · [状态效果 S-915e31808434abd5](../../evidence/state_effects-sets-031.md#s-915e31808434abd5)

### path-070598

```text
(config-subif)# default cdp tlv server-location <cr>
```

Handler ` RVA 0xCDA0E50 `；selector ` 9 `；EOL ` RVA 0x33CE7EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff7c403de075a5bd](../../evidence/conditions-sets-098.md#c-ff7c403de075a5bd) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068349

```text
(config-subif)# default channel-group <cr>
```

Handler ` RVA 0xE9A5F10 `；selector ` 0 `；EOL ` RVA 0x3436AF88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-68d4b4279c64bcd1](../../evidence/conditions-sets-041.md#c-68d4b4279c64bcd1) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069909

```text
(config-subif)# default clns access-group <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 30 `；EOL ` RVA 0x34B7C800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52a97c07d04c906d](../../evidence/conditions-sets-032.md#c-52a97c07d04c906d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071181

```text
(config-subif)# default clns adjacency-filter ES <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 33 `；EOL ` RVA 0x34B7CFD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93d0324ae20dc591](../../evidence/conditions-sets-057.md#c-93d0324ae20dc591) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069468

```text
(config-subif)# default clns checksum <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 9 `；EOL ` RVA 0x34B79FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069484

```text
(config-subif)# default clns cluster-alias <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 8 `；EOL ` RVA 0x34B7A298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068553

```text
(config-subif)# default clns congestion-threshold <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 10 `；EOL ` RVA 0x34B7A2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d66fe340b6dd3e79](../../evidence/conditions-sets-083.md#c-d66fe340b6dd3e79) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069551

```text
(config-subif)# default clns dec-compatible <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 20 `；EOL ` RVA 0x34B7AA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069533

```text
(config-subif)# default clns enable <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 11 `；EOL ` RVA 0x34B7A7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068594

```text
(config-subif)# default clns erpdu-interval <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 12 `；EOL ` RVA 0x34B7AAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5d7690b8d2642e9](../../evidence/conditions-sets-095.md#c-f5d7690b8d2642e9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070962

```text
(config-subif)# default clns es-neighbor <address> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 13 `；EOL ` RVA 0x34B7B0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` CLNS address or host name。

[条件 C-a3206db1824c33e7](../../evidence/conditions-sets-063.md#c-a3206db1824c33e7) · [参数 P-3b629999e774e7e1](../../evidence/parameters-sets-005.md#p-3b629999e774e7e1) · [状态效果 S-2d64f44fd35440c4](../../evidence/state_effects-sets-010.md#s-2d64f44fd35440c4)

### path-069902

```text
(config-subif)# default clns esct-time <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 34 `；EOL ` RVA 0x34B7D338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6bdb06ad1ab9497c](../../evidence/conditions-sets-042.md#c-6bdb06ad1ab9497c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068628

```text
(config-subif)# default clns mtu <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 15 `；EOL ` RVA 0x34B7B3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fe1d7494d4be4ec](../../evidence/conditions-sets-062.md#c-9fe1d7494d4be4ec) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070816

```text
(config-subif)# default clns net <address> <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 1 `；EOL ` RVA 0x34B79D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` A CLNS address or host name。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [参数 P-961a29e3f61555f8](../../evidence/parameters-sets-012.md#p-961a29e3f61555f8) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068646

```text
(config-subif)# default clns rdpdu-interval <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 16 `；EOL ` RVA 0x34B7B430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c1480bf6e5d0a94](../../evidence/conditions-sets-048.md#c-7c1480bf6e5d0a94) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069751

```text
(config-subif)# default clns route-cache <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 7 `；EOL ` RVA 0x34B7BEB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071058

```text
(config-subif)# default clns router iso-igrp <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 26 `；EOL ` RVA 0x34B7BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-be283b21c138b2ed](../../evidence/state_effects-sets-040.md#s-be283b21c138b2ed)

### path-069743

```text
(config-subif)# default clns send-erpdu <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 18 `；EOL ` RVA 0x34B7C150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069774

```text
(config-subif)# default clns send-rdpdu <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 19 `；EOL ` RVA 0x34B7C3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069823

```text
(config-subif)# default clns split-horizon <cr>
```

Handler ` RVA 0x1058E190 `；selector ` 31 `；EOL ` RVA 0x34B7CC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a624b955a2e72d30](../../evidence/conditions-sets-064.md#c-a624b955a2e72d30) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068495

```text
(config-subif)# default clock <cr>
```

Handler ` RVA 0xED6B290 `；selector ` 0 `；EOL ` RVA 0x34415AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-767964230a55b74d](../../evidence/conditions-sets-046.md#c-767964230a55b74d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068958

```text
(config-subif)# default clock auto <cr>
```

Handler ` RVA 0xE421F00 `；selector ` 20 `；EOL ` RVA 0x34141588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d0c0d955bb3eaf3](../../evidence/conditions-sets-055.md#c-8d0c0d955bb3eaf3) · [状态效果 S-16d307a37af6e9ec](../../evidence/state_effects-sets-005.md#s-16d307a37af6e9ec)

### path-069074

```text
(config-subif)# default clock source <cr>
```

Handler ` RVA 0xED13570 `；selector ` 0 `；EOL ` RVA 0x34404710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-617c64304d89ed12](../../evidence/conditions-sets-038.md#c-617c64304d89ed12) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068610

```text
(config-subif)# default clockrate <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 0 `；EOL ` RVA 0x344191C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f032728b44b40279](../../evidence/conditions-sets-093.md#c-f032728b44b40279) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068626

```text
(config-subif)# default clockrate <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 0 `；EOL ` RVA 0x34418290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f73d6a8ad0d59801](../../evidence/conditions-sets-095.md#c-f73d6a8ad0d59801) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068644

```text
(config-subif)# default clockrate <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 2 `；EOL ` RVA 0x34417078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c954979f0bb8987d](../../evidence/conditions-sets-078.md#c-c954979f0bb8987d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068656

```text
(config-subif)# default clockrate <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 2 `；EOL ` RVA 0x344175C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e3de69f90bc1af66](../../evidence/conditions-sets-088.md#c-e3de69f90bc1af66) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068677

```text
(config-subif)# default clockrate <cr>
```

Handler ` RVA 0xED6B0B0 `；selector ` 2 `；EOL ` RVA 0x34417920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9044080ebcd8094b](../../evidence/conditions-sets-056.md#c-9044080ebcd8094b) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069666

```text
(config-subif)# default clockrate threshold <cr>
```

Handler ` RVA 0xED6B1A0 `；selector ` 0 `；EOL ` RVA 0x34417F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec54a62ae8a14583](../../evidence/conditions-sets-091.md#c-ec54a62ae8a14583) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069299

```text
(config-subif)# default cmns enable <cr>
```

Handler ` RVA 0x105E5970 `；selector ` 2 `；EOL ` RVA 0x34BB3F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2fed3e3230b4922b](../../evidence/conditions-sets-019.md#c-2fed3e3230b4922b) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068336

```text
(config-subif)# default compress <cr>
```

Handler ` RVA 0xF423DB0 `；selector ` 0 `；EOL ` RVA 0x346467B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad643a141242bfef](../../evidence/conditions-sets-067.md#c-ad643a141242bfef) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069329

```text
(config-subif)# default crc 32 <cr>
```

Handler ` RVA 0xED6DB30 `；selector ` 0 `；EOL ` RVA 0x344137A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b13945f9b7ceb248](../../evidence/conditions-sets-069.md#c-b13945f9b7ceb248) · [状态效果 S-9f07f6076c6bf306](../../evidence/state_effects-sets-034.md#s-9f07f6076c6bf306)

### path-069358

```text
(config-subif)# default crc bits <cr>
```

Handler ` RVA 0xED6BAE0 `；selector ` 0 `；EOL ` RVA 0x34413508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-99fe528b6d4d7ecf](../../evidence/conditions-sets-060.md#c-99fe528b6d4d7ecf) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068493

```text
(config-subif)# default crc4 <cr>
```

Handler ` RVA 0xED6B670 `；selector ` 0 `；EOL ` RVA 0x34415EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-593e4fe1224ba5a2](../../evidence/conditions-sets-035.md#c-593e4fe1224ba5a2) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069990

```text
(config-subif)# default cts dot1x <cr>
```

Handler ` RVA 0x13040720 `；selector ` 0 `；EOL ` RVA 0x35A15888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b537ca248c1b16ff](../../evidence/conditions-sets-070.md#c-b537ca248c1b16ff) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072039

```text
(config-subif)# default cts layer3 ipv4 policy <cr>
```

Handler ` RVA 0x13040720 `；selector ` 3 `；EOL ` RVA 0x35A154F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bd97f0f9607e3400](../../evidence/conditions-sets-073.md#c-bd97f0f9607e3400) · [状态效果 S-b0ddb6dce0a3a7b3](../../evidence/state_effects-sets-037.md#s-b0ddb6dce0a3a7b3)

### path-072353

```text
(config-subif)# default cts layer3 ipv4 trustsec forwarding <cr>
```

Handler ` RVA 0x13040720 `；selector ` 2 `；EOL ` RVA 0x35A15220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd85a16a29e3c237](../../evidence/conditions-sets-079.md#c-cd85a16a29e3c237) · [状态效果 S-b0ddb6dce0a3a7b3](../../evidence/state_effects-sets-037.md#s-b0ddb6dce0a3a7b3)

### path-070002

```text
(config-subif)# default cts manual <cr>
```

Handler ` RVA 0x13040720 `；selector ` 1 `；EOL ` RVA 0x35A14D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-096becc58f5b1097](../../evidence/conditions-sets-004.md#c-096becc58f5b1097) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071385

```text
(config-subif)# default cts role-based enforcement <cr>
```

Handler ` RVA 0x14203460 `；selector ` 0 `；EOL ` RVA 0x35CFC1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cff03687408d0b54](../../evidence/conditions-sets-080.md#c-cff03687408d0b54) · [状态效果 S-56d504632fdc79db](../../evidence/state_effects-sets-019.md#s-56d504632fdc79db)

### path-072061

```text
(config-subif)# default cts role-based sgt-cache egress <cr>
```

Handler ` RVA 0x1413CA60 `；selector ` 165 `；EOL ` RVA 0x35CE9B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-131d7e3af93e1a95](../../evidence/conditions-sets-008.md#c-131d7e3af93e1a95) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072055

```text
(config-subif)# default cts role-based sgt-cache ingress <cr>
```

Handler ` RVA 0x1413CA60 `；selector ` 164 `；EOL ` RVA 0x35CE98B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c5d2a7602ef2991](../../evidence/conditions-sets-048.md#c-7c5d2a7602ef2991) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071446

```text
(config-subif)# default cts role-based sgt-map <cr>
```

Handler ` RVA 0x14045110 `；selector ` 1 `；EOL ` RVA 0x35CE9418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0dfe9aea1715035](../../evidence/conditions-sets-074.md#c-c0dfe9aea1715035) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072360

```text
(config-subif)# default cts role-based sgt-map vlanid <number:1..4094> <cr>
```

Handler ` RVA 0x14045110 `；selector ` 2 `；EOL ` RVA 0x35CE9048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` VLAN id。

[条件 C-2dd25778300b430b](../../evidence/conditions-sets-018.md#c-2dd25778300b430b) · [参数 P-18500808c993142f](../../evidence/parameters-sets-002.md#p-18500808c993142f) · [状态效果 S-53d825509334d553](../../evidence/state_effects-sets-018.md#s-53d825509334d553)

### path-070972

```text
(config-subif)# default cts sgt inline <cr>
```

Handler ` RVA 0x108DB4B0 `；selector ` 1 `；EOL ` RVA 0x34BF4398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce44c09d5ce1521b](../../evidence/conditions-sets-079.md#c-ce44c09d5ce1521b) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069915

```text
(config-subif)# default cwmp wan <cr>
```

Handler ` RVA 0x16470900 `；selector ` 7 `；EOL ` RVA 0x35F8E350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a0690559e124817f](../../evidence/conditions-sets-062.md#c-a0690559e124817f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071191

```text
(config-subif)# default cwmp wan default <cr>
```

Handler ` RVA 0x16470900 `；selector ` 8 `；EOL ` RVA 0x35F8E0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a0690559e124817f](../../evidence/conditions-sets-062.md#c-a0690559e124817f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068205

```text
(config-subif)# default dampening <cr>
```

Handler ` RVA 0xDFF5AC0 `；selector ` 0 `；EOL ` RVA 0x3412DF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c8f026127aaa5ef9](../../evidence/conditions-sets-077.md#c-c8f026127aaa5ef9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068564

```text
(config-subif)# default dce-terminal-timing-enable <cr>
```

Handler ` RVA 0xED6C030 `；selector ` 0 `；EOL ` RVA 0x34419760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a9d7aedba52dd850](../../evidence/conditions-sets-066.md#c-a9d7aedba52dd850) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068059

```text
(config-subif)# default delay <cr>
```

Handler ` RVA 0xE40C610 `；selector ` 1 `；EOL ` RVA 0x3413C100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4dc90757a49985e3](../../evidence/conditions-sets-030.md#c-4dc90757a49985e3) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068201

```text
(config-subif)# default description <cr>
```

Handler ` RVA 0xE40C850 `；selector ` 3 `；EOL ` RVA 0x34149120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-993a0ef02603e998](../../evidence/conditions-sets-059.md#c-993a0ef02603e998) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070273

```text
(config-subif)# default device-tracking attach-policy <string> <cr>
```

Handler ` RVA 0x1368B060 `；selector ` 1121 `；EOL ` RVA 0x35BCB3A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy name for device tracking。

[条件 C-d3b834db83a55e4a](../../evidence/conditions-sets-082.md#c-d3b834db83a55e4a) · [参数 P-55d8ec5958aec910](../../evidence/parameters-sets-007.md#p-55d8ec5958aec910) · [状态效果 S-d2a0583dab183fa8](../../evidence/state_effects-sets-045.md#s-d2a0583dab183fa8)

### path-068225

```text
(config-subif)# default dhcp-border-relay <cr>
```

Handler ` RVA 0x15738330 `；selector ` 0 `；EOL ` RVA 0x35D85200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd7f5c7d3e956f1a](../../evidence/conditions-sets-085.md#c-dd7f5c7d3e956f1a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068724

```text
(config-subif)# default dhcp-server-tracking <cr>
```

Handler ` RVA 0x136A1DA0 `；selector ` 1901 `；EOL ` RVA 0x35C00AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-77b9c998b53695f5](../../evidence/conditions-sets-047.md#c-77b9c998b53695f5) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068369

```text
(config-subif)# default dialer <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 3 `；EOL ` RVA 0x3466F800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f0fac57a77a82b0](../../evidence/conditions-sets-024.md#c-3f0fac57a77a82b0) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069756

```text
(config-subif)# default dialer aaa <cr>
```

Handler ` RVA 0xF4DC320 `；selector ` 25 `；EOL ` RVA 0x34675F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-427040b55cc6e25d](../../evidence/conditions-sets-026.md#c-427040b55cc6e25d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069662

```text
(config-subif)# default dialer callback-secure <cr>
```

Handler ` RVA 0xF48E030 `；selector ` 16 `；EOL ` RVA 0x34660CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c929598c6f0855b5](../../evidence/conditions-sets-077.md#c-c929598c6f0855b5) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070770

```text
(config-subif)# default dialer called <string> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 29 `；EOL ` RVA 0x3466C118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Dialer called string (DNIS)。

[条件 C-51164494e8ab5934](../../evidence/conditions-sets-032.md#c-51164494e8ab5934) · [参数 P-c34abd66b9324d6a](../../evidence/parameters-sets-015.md#p-c34abd66b9324d6a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070791

```text
(config-subif)# default dialer caller <string> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 15 `；EOL ` RVA 0x3466C4C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Dialer caller string (CLID)。

[条件 C-4069c605f45c23c2](../../evidence/conditions-sets-025.md#c-4069c605f45c23c2) · [参数 P-f74ec03bc2cef154](../../evidence/parameters-sets-018.md#p-f74ec03bc2cef154) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071072

```text
(config-subif)# default dialer congestion-threshold <number:0..64000> <cr>
```

Handler ` RVA 0xF4DC320 `；selector ` 28 `；EOL ` RVA 0x346767C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of links for congestion threshold。

[条件 C-6b686a06042a5d3b](../../evidence/conditions-sets-042.md#c-6b686a06042a5d3b) · [参数 P-4e50e66cb39470a8](../../evidence/parameters-sets-006.md#p-4e50e66cb39470a8) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069339

```text
(config-subif)# default dialer disable-multiencaps <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 34 `；EOL ` RVA 0x3466B0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eb5848ddf4b86c6e](../../evidence/conditions-sets-091.md#c-eb5848ddf4b86c6e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069686

```text
(config-subif)# default dialer dns <cr>
```

Handler ` RVA 0xF4DC320 `；selector ` 26 `；EOL ` RVA 0x34675BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3032042fbd405758](../../evidence/conditions-sets-019.md#c-3032042fbd405758) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069542

```text
(config-subif)# default dialer down-with-vInterface <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 40 `；EOL ` RVA 0x3466E708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eea04de4c2e9569](../../evidence/conditions-sets-018.md#c-2eea04de4c2e9569) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069144

```text
(config-subif)# default dialer dtr <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 13 `；EOL ` RVA 0x346700C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2822a8537b4f5306](../../evidence/conditions-sets-016.md#c-2822a8537b4f5306) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068437

```text
(config-subif)# default dialer enable-timeout <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 6 `；EOL ` RVA 0x3466B098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6970cdac198c1cc2](../../evidence/conditions-sets-041.md#c-6970cdac198c1cc2) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069806

```text
(config-subif)# default dialer extsig <cr>
```

Handler ` RVA 0xF48E030 `；selector ` 35 `；EOL ` RVA 0x34661E20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a23fe1e1a6db3207](../../evidence/conditions-sets-063.md#c-a23fe1e1a6db3207) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068396

```text
(config-subif)# default dialer fast-idle <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 5 `；EOL ` RVA 0x3466A3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-300f186fbc7cf727](../../evidence/conditions-sets-019.md#c-300f186fbc7cf727) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069465

```text
(config-subif)# default dialer hold-queue <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 14 `；EOL ` RVA 0x3466D390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eea04de4c2e9569](../../evidence/conditions-sets-018.md#c-2eea04de4c2e9569) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069269

```text
(config-subif)# default dialer idle-timeout <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 0 `；EOL ` RVA 0x3466A480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eaf3f404b7f592f1](../../evidence/conditions-sets-091.md#c-eaf3f404b7f592f1) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069171

```text
(config-subif)# default dialer in-band <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 4 `；EOL ` RVA 0x34670408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-21d9161e0aff4b4d](../../evidence/conditions-sets-013.md#c-21d9161e0aff4b4d) · [状态效果 S-017959495b21672b](../../evidence/state_effects-sets-001.md#s-017959495b21672b)

### path-069309

```text
(config-subif)# default dialer leased <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 33 `；EOL ` RVA 0x3466ADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eb5848ddf4b86c6e](../../evidence/conditions-sets-091.md#c-eb5848ddf4b86c6e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069524

```text
(config-subif)# default dialer load-threshold <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 11 `；EOL ` RVA 0x3466DA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ba0c707eded7d1c9](../../evidence/conditions-sets-072.md#c-ba0c707eded7d1c9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068547

```text
(config-subif)# default dialer max-call <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 20 `；EOL ` RVA 0x3466DE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5348a7a64f99233a](../../evidence/conditions-sets-033.md#c-5348a7a64f99233a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069310

```text
(config-subif)# default dialer mult-map-same-name <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 31 `；EOL ` RVA 0x3466AB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88e3318093061de3](../../evidence/conditions-sets-053.md#c-88e3318093061de3) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069322

```text
(config-subif)# default dialer order <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 39 `；EOL ` RVA 0x34669FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4383247b2f70410a](../../evidence/conditions-sets-026.md#c-4383247b2f70410a) · [状态效果 S-deeea62883f133de](../../evidence/state_effects-sets-047.md#s-deeea62883f133de)

### path-069588

```text
(config-subif)# default dialer persistent <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 38 `；EOL ` RVA 0x3466E318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3dfb9ab286a6de25](../../evidence/conditions-sets-024.md#c-3dfb9ab286a6de25) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070508

```text
(config-subif)# default dialer pool <number:1..255> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 18 `；EOL ` RVA 0x346698F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Dialer pool number。

[条件 C-eb5848ddf4b86c6e](../../evidence/conditions-sets-091.md#c-eb5848ddf4b86c6e) · [参数 P-d015012074be17ef](../../evidence/parameters-sets-016.md#p-d015012074be17ef) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070526

```text
(config-subif)# default dialer pool-member <number:1..255> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 19 `；EOL ` RVA 0x3466FB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Dialer pool number。

[条件 C-e4d9ed9b905727e6](../../evidence/conditions-sets-088.md#c-e4d9ed9b905727e6) · [参数 P-4fb214ed1dbeebd3](../../evidence/parameters-sets-007.md#p-4fb214ed1dbeebd3) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070908

```text
(config-subif)# default dialer pppoe-client-vlan-cos <number:0..7> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 41 `；EOL ` RVA 0x3466ECE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` cos value &lt;0-7&gt;。

[条件 C-2eea04de4c2e9569](../../evidence/conditions-sets-018.md#c-2eea04de4c2e9569) · [参数 P-46b0c689d6fa737c](../../evidence/parameters-sets-006.md#p-46b0c689d6fa737c) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068520

```text
(config-subif)# default dialer priority <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 12 `；EOL ` RVA 0x3466D688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-568a69b53c25c50e](../../evidence/conditions-sets-034.md#c-568a69b53c25c50e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069691

```text
(config-subif)# default dialer redial <cr>
```

Handler ` RVA 0xF48E030 `；selector ` 32 `；EOL ` RVA 0x34661040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1c85d602f8ee7b9](../../evidence/conditions-sets-062.md#c-a1c85d602f8ee7b9) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069234

```text
(config-subif)# default dialer remote-name <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 17 `；EOL ` RVA 0x34669C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d31348fb9e2af867](../../evidence/conditions-sets-081.md#c-d31348fb9e2af867) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071888

```text
(config-subif)# default dialer reserved-links <number:0..64000> <number:0..64000> <cr>
```

Handler ` RVA 0xF4DC320 `；selector ` 27 `；EOL ` RVA 0x34676B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of links reserved for dialin；` unsigned_number ` Number of links reserved for dialout。

[条件 C-2d5d98d8dd05c490](../../evidence/conditions-sets-018.md#c-2d5d98d8dd05c490) · [参数 P-dfb6718e525a4c36](../../evidence/parameters-sets-017.md#p-dfb6718e525a4c36) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070810

```text
(config-subif)# default dialer rotary-group <number:0..255> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 10 `；EOL ` RVA 0x3466F080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Rotary group number。

[条件 C-776ec0e9a23d67ff](../../evidence/conditions-sets-046.md#c-776ec0e9a23d67ff) · [参数 P-1c5a1a278dca110e](../../evidence/parameters-sets-003.md#p-1c5a1a278dca110e) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069319

```text
(config-subif)# default dialer rotor <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 21 `；EOL ` RVA 0x3466F418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3b0bf10b117fc8da](../../evidence/conditions-sets-023.md#c-3b0bf10b117fc8da) · [状态效果 S-5f486a1e1911fd4f](../../evidence/state_effects-sets-020.md#s-5f486a1e1911fd4f)

### path-069718

```text
(config-subif)# default dialer snapshot <cr>
```

Handler ` RVA 0xF48E030 `；selector ` 22 `；EOL ` RVA 0x34661800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eea04de4c2e9569](../../evidence/conditions-sets-018.md#c-2eea04de4c2e9569) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070796

```text
(config-subif)# default dialer string <string> <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 8 `；EOL ` RVA 0x3466BD78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Dialer string (quote strings containing #)。

[条件 C-5a121f7a25c80096](../../evidence/conditions-sets-035.md#c-5a121f7a25c80096) · [参数 P-44305b03b44b5739](../../evidence/parameters-sets-006.md#p-44305b03b44b5739) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069787

```text
(config-subif)# default dialer suffix <cr>
```

Handler ` RVA 0xF4DC320 `；selector ` 36 `；EOL ` RVA 0x346763C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b2d785b45d54f0f](../../evidence/conditions-sets-054.md#c-8b2d785b45d54f0f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069557

```text
(config-subif)# default dialer vpdn <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 30 `；EOL ` RVA 0x3466E9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eea04de4c2e9569](../../evidence/conditions-sets-018.md#c-2eea04de4c2e9569) · [状态效果 S-7b4141c37c431389](../../evidence/state_effects-sets-026.md#s-7b4141c37c431389)

### path-068460

```text
(config-subif)# default dialer wait-for-carrier-time <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 7 `；EOL ` RVA 0x3466B5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c6d22a3d994c6284](../../evidence/conditions-sets-077.md#c-c6d22a3d994c6284) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068450

```text
(config-subif)# default dialer wait-for-line-protocol <cr>
```

Handler ` RVA 0xF4C3DC0 `；selector ` 37 `；EOL ` RVA 0x3466B350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7bbea723547e320a](../../evidence/conditions-sets-048.md#c-7bbea723547e320a) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-069720

```text
(config-subif)# default dialer watch-disable <cr>
```

Handler ` RVA 0xF48E030 `；selector ` 24 `；EOL ` RVA 0x34661510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1c2793b9f179059f](../../evidence/conditions-sets-011.md#c-1c2793b9f179059f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071048

```text
(config-subif)# default dialer watch-group <number:1..255> <cr>
```

Handler ` RVA 0xF48AD10 `；selector ` 0 `；EOL ` RVA 0x34661B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Dialer watch group number。

[条件 C-2eea04de4c2e9569](../../evidence/conditions-sets-018.md#c-2eea04de4c2e9569) · [参数 P-1ea9d8d31181bd1d](../../evidence/parameters-sets-003.md#p-1ea9d8d31181bd1d) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-068337

```text
(config-subif)# default dialer-group <cr>
```

Handler ` RVA 0xF4C89D0 `；selector ` 0 `；EOL ` RVA 0x346707F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3b782f716bc34e94](../../evidence/conditions-sets-023.md#c-3b782f716bc34e94) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071605

```text
(config-subif)# default dlsw llc2-peer listen-sap <number:0..255> <cr>
```

Handler ` RVA 0x11418E90 `；selector ` 0 `；EOL ` RVA 0x354DBCB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Sap value。

[条件 C-1178b216f75b4673](../../evidence/conditions-sets-007.md#c-1178b216f75b4673) · [参数 P-492ccc28a37ad6b8](../../evidence/parameters-sets-006.md#p-492ccc28a37ad6b8) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072497

```text
(config-subif)# default dlsw transparent map local-mac <address> remote-mac <address> <cr>
```

Handler ` RVA 0x11418B10 `；selector ` 2 `；EOL ` RVA 0x354DCAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MAC address (MAC Value)；` address ` MAC address (MAC Value)。

[条件 C-fe67e7925432224a](../../evidence/conditions-sets-098.md#c-fe67e7925432224a) · [参数 P-a8f5dfcbed94c1c5](../../evidence/parameters-sets-013.md#p-a8f5dfcbed94c1c5) · [状态效果 S-db895f8f774d7558](../../evidence/state_effects-sets-046.md#s-db895f8f774d7558)

### path-070637

```text
(config-subif)# default dlsw transparent redundancy-enable <cr>
```

Handler ` RVA 0x11418B10 `；selector ` 0 `；EOL ` RVA 0x354DC130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-358e8a183b78a98f](../../evidence/conditions-sets-021.md#c-358e8a183b78a98f) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-072187

```text
(config-subif)# default dlsw transparent timers netbios <number:100..900> <cr>
```

Handler ` RVA 0x11418B10 `；selector ` 3 `；EOL ` RVA 0x354DC5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` timeout value (milliseconds)。

[条件 C-fe67e7925432224a](../../evidence/conditions-sets-098.md#c-fe67e7925432224a) · [参数 P-e6717908135500a1](../../evidence/parameters-sets-017.md#p-e6717908135500a1) · [状态效果 S-64df38b591c975d6](../../evidence/state_effects-sets-022.md#s-64df38b591c975d6)

### path-070773

```text
(config-subif)# default dot1q tunneling ethertype <cr>
```

Handler ` RVA 0x11D0E110 `；selector ` 1 `；EOL ` RVA 0x356D0D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-511fdad83fe575c6](../../evidence/conditions-sets-032.md#c-511fdad83fe575c6) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-071417

```text
(config-subif)# default dot1x auth-fail vlan <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5EAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f34adfa56c8f7706](../../evidence/conditions-sets-094.md#c-f34adfa56c8f7706) · [状态效果 S-809bf95b8c434da6](../../evidence/state_effects-sets-027.md#s-809bf95b8c434da6)

### path-072032

```text
(config-subif)# default dot1x authenticator eap profile <cr>
```

Handler ` RVA 0xCB262C0 `；selector ` 36 `；EOL ` RVA 0x33BB9288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c9bc4e6dcd90af28](../../evidence/conditions-sets-078.md#c-c9bc4e6dcd90af28) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070150

```text
(config-subif)# default dot1x control-direction <cr>
```

Handler ` RVA 0xCB27850 `；selector ` 4 `；EOL ` RVA 0x33BBC918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-65cb0f58345e003f](../../evidence/conditions-sets-039.md#c-65cb0f58345e003f) · [状态效果 S-f938323ce1617769](../../evidence/state_effects-sets-053.md#s-f938323ce1617769)

### path-070149

```text
(config-subif)# default dot1x credentials <cr>
```

Handler ` RVA 0xCB2FF20 `；selector ` 15 `；EOL ` RVA 0x33BC0908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd295070f0f765c2](../../evidence/conditions-sets-085.md#c-dd295070f0f765c2) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

### path-070119

```text
(config-subif)# default dot1x critical <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x33B81150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a139a454907457d8](../../evidence/conditions-sets-062.md#c-a139a454907457d8) · [状态效果 S-5fc9fe69b3519396](../../evidence/state_effects-sets-021.md#s-5fc9fe69b3519396)

### path-071416

```text
(config-subif)# default dot1x critical vlan <cr>
```

Handler ` RVA 0xCAD1210 `；selector ` 7 `；EOL ` RVA 0x35E5E058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-557a26ecdd4ca8ea](../../evidence/conditions-sets-034.md#c-557a26ecdd4ca8ea) · [状态效果 S-6ae3ba82cc8a0654](../../evidence/state_effects-sets-023.md#s-6ae3ba82cc8a0654)

### path-069991

```text
(config-subif)# default dot1x default <cr>
```

Handler ` RVA 0xCB262C0 `；selector ` 34 `；EOL ` RVA 0x33BB9FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1dda373cb7fd14e5](../../evidence/conditions-sets-012.md#c-1dda373cb7fd14e5) · [状态效果 S-af7d058ced30fb88](../../evidence/state_effects-sets-037.md#s-af7d058ced30fb88)

