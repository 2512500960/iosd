# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-062295

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> table stdby-drh <address> remove <cr>
```

Handler ` RVA 0xB46C150 `；selector ` 0 `；EOL ` RVA 0x3375B228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Via IPv4 address。

[条件 C-e71285bf302a1abd](../../evidence/conditions-sets-089.md#c-e71285bf302a1abd) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-a24f27dbee9ff949](../../evidence/parameters-sets-012.md#p-a24f27dbee9ff949) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062301

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> table stdby-drh <address> remove <cr>
```

Handler ` RVA 0xB46C150 `；selector ` 0 `；EOL ` RVA 0x3375E748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Via IPv6 Address。

[条件 C-2ddc0639cd8cd16d](../../evidence/conditions-sets-018.md#c-2ddc0639cd8cd16d) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-cde95a557c1cb0fa](../../evidence/parameters-sets-016.md#p-cde95a557c1cb0fa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062601

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> table subblock add prefix <address> <address> <cr>
```

Handler ` RVA 0xB46D150 `；selector ` 0 `；EOL ` RVA 0x3375A408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix address；` address ` Prefix mask。

[条件 C-b348ee3d99eacbe9](../../evidence/conditions-sets-069.md#c-b348ee3d99eacbe9) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-c3ad5c28e684e7cc](../../evidence/parameters-sets-015.md#p-c3ad5c28e684e7cc) · [状态效果 S-51ece57ea9817294](../../evidence/state_effects-sets-018.md#s-51ece57ea9817294)

### path-062913

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> table subblock add prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xB46D150 `；selector ` 0 `；EOL ` RVA 0x3375D950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix address。

[条件 C-c328a7bcf3517fb3](../../evidence/conditions-sets-075.md#c-c328a7bcf3517fb3) · [缺口 G-39d16eedd4592670](../../evidence/gaps-sets-003.md#g-39d16eedd4592670) · [参数 P-29d53f6a4fb3ef1c](../../evidence/parameters-sets-004.md#p-29d53f6a4fb3ef1c) · [状态效果 S-2357edacc0fb91e4](../../evidence/state_effects-sets-008.md#s-2357edacc0fb91e4)

### path-061916

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> table trigger delete-all <cr>
```

Handler ` RVA 0xB46CD10 `；selector ` 0 `；EOL ` RVA 0x3375C2E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9ae5087a509344c4](../../evidence/conditions-sets-060.md#c-9ae5087a509344c4) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [状态效果 S-120b69cbbc040a03](../../evidence/state_effects-sets-004.md#s-120b69cbbc040a03)

### path-061913

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> walks background disable <cr>
```

Handler ` RVA 0xB352790 `；selector ` 1 `；EOL ` RVA 0x33762F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3a5291bd0e47b575](../../evidence/conditions-sets-023.md#c-3a5291bd0e47b575) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061912

```text
(config)# do-exec test cef <?dumper_command_func@555588cac488> walks background enable <cr>
```

Handler ` RVA 0xB352790 `；selector ` 0 `；EOL ` RVA 0x33762C60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f66c6b0caec3f962](../../evidence/conditions-sets-095.md#c-f66c6b0caec3f962) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061895

```text
(config)# do-exec test cef assert fail <?option@555588cac098> fatal <cr>
```

Handler ` RVA 0xB363340 `；selector ` 0 `；EOL ` RVA 0x33758170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e366026d903e0a82](../../evidence/conditions-sets-088.md#c-e366026d903e0a82) · [缺口 G-85693a83e589e3d1](../../evidence/gaps-sets-005.md#g-85693a83e589e3d1) · [状态效果 S-b3104c3c7ccd63b0](../../evidence/state_effects-sets-038.md#s-b3104c3c7ccd63b0)

### path-035477

```text
(config)# do-exec test cef crimson-oper-db add <cr>
```

Handler ` RVA 0xB369C80 `；selector ` 0 `；EOL ` RVA 0x337520E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-10b1979508e04de9](../../evidence/conditions-sets-007.md#c-10b1979508e04de9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035529

```text
(config)# do-exec test cef crimson-oper-db del <cr>
```

Handler ` RVA 0xB369CF0 `；selector ` 0 `；EOL ` RVA 0x33752388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd0f47df170f1d69](../../evidence/conditions-sets-098.md#c-fd0f47df170f1d69) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035359

```text
(config)# do-exec test cef crimson-oper-db disable <cr>
```

Handler ` RVA 0xB369B50 `；selector ` 0 `；EOL ` RVA 0x33751830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f945adc87c8d7315](../../evidence/conditions-sets-096.md#c-f945adc87c8d7315) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035294

```text
(config)# do-exec test cef crimson-oper-db enable <cr>
```

Handler ` RVA 0xB369AE0 `；selector ` 0 `；EOL ` RVA 0x33751588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-344052f2725b19c4](../../evidence/conditions-sets-020.md#c-344052f2725b19c4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045116

```text
(config)# do-exec test cef crimson-oper-db oc-nh-grp-db IPv4 <cr>
```

Handler ` RVA 0xB369BC0 `；selector ` 0 `；EOL ` RVA 0x33751C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9857a820d2e2129e](../../evidence/conditions-sets-059.md#c-9857a820d2e2129e) · [状态效果 S-ce357c5a628d3e3a](../../evidence/state_effects-sets-044.md#s-ce357c5a628d3e3a)

### path-062261

```text
(config)# do-exec test cef crimson-oper-db oc-nh-grp-db IPv4 vrf <?option@555588ca5c48> <cr>
```

Handler ` RVA 0xB369BC0 `；selector ` 0 `；EOL ` RVA 0x33751C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c887bc56f6b4ba8a](../../evidence/conditions-sets-077.md#c-c887bc56f6b4ba8a) · [缺口 G-efb06a221e4efa76](../../evidence/gaps-sets-008.md#g-efb06a221e4efa76) · [状态效果 S-22cef554eccc2b25](../../evidence/state_effects-sets-008.md#s-22cef554eccc2b25)

### path-028821

```text
(config)# do-exec test cef enable <cr>
```

Handler ` RVA 0xB480BC0 `；selector ` 0 `；EOL ` RVA 0x3374CCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-71e289f25df36c27](../../evidence/conditions-sets-044.md#c-71e289f25df36c27) · [状态效果 S-e82f41e3560bb6d2](../../evidence/state_effects-sets-049.md#s-e82f41e3560bb6d2)

### path-045123

```text
(config)# do-exec test cef event-trace IPv4 <string> <cr>
```

Handler ` RVA 0xB47E360 `；selector ` 0 `；EOL ` RVA 0x33764268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` String to insert into event log。

[条件 C-f85779ff9a12c23c](../../evidence/conditions-sets-096.md#c-f85779ff9a12c23c) · [参数 P-c31ab8da975e92c0](../../evidence/parameters-sets-015.md#p-c31ab8da975e92c0) · [状态效果 S-9f193b8579adb8a8](../../evidence/state_effects-sets-034.md#s-9f193b8579adb8a8)

### path-035418

```text
(config)# do-exec test cef ext-lb disable <cr>
```

Handler ` RVA 0xB3F0520 `；selector ` 1 `；EOL ` RVA 0x33753078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e674079c9d5e5bf](../../evidence/conditions-sets-049.md#c-7e674079c9d5e5bf) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035417

```text
(config)# do-exec test cef ext-lb enable <cr>
```

Handler ` RVA 0xB3F0520 `；selector ` 0 `；EOL ` RVA 0x33752DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcd4bc85b21c9ac8](../../evidence/conditions-sets-073.md#c-bcd4bc85b21c9ac8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045465

```text
(config)# do-exec test cef get-nexthop-adj IPv4 <address> <cr>
```

Handler ` RVA 0xB419330 `；selector ` 0 `；EOL ` RVA 0x33755FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-e1152de66941f30f](../../evidence/conditions-sets-087.md#c-e1152de66941f30f) · [参数 P-cec27e68cf98fe44](../../evidence/parameters-sets-016.md#p-cec27e68cf98fe44) · [状态效果 S-9ee49937e8180c0c](../../evidence/state_effects-sets-034.md#s-9ee49937e8180c0c)

### path-062274

```text
(config)# do-exec test cef get-nexthop-adj IPv4 vrf <?option@555588ca9d48> <address> <cr>
```

Handler ` RVA 0xB419330 `；selector ` 0 `；EOL ` RVA 0x33755FA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-5895bfe74091ff39](../../evidence/conditions-sets-035.md#c-5895bfe74091ff39) · [缺口 G-33bdfcbecaa367b1](../../evidence/gaps-sets-002.md#g-33bdfcbecaa367b1) · [参数 P-cec27e68cf98fe44](../../evidence/parameters-sets-016.md#p-cec27e68cf98fe44) · [状态效果 S-ee08f5c30a323210](../../evidence/state_effects-sets-050.md#s-ee08f5c30a323210)

### path-061899

```text
(config)# do-exec test cef hw-api fail <?option@555588cac4c8> fatal <cr>
```

Handler ` RVA 0xB3D8B00 `；selector ` 0 `；EOL ` RVA 0x337585A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c08072983dbad8c0](../../evidence/conditions-sets-074.md#c-c08072983dbad8c0) · [缺口 G-cf478da77a7d8f22](../../evidence/gaps-sets-007.md#g-cf478da77a7d8f22) · [状态效果 S-378ac91628fa1da8](../../evidence/state_effects-sets-012.md#s-378ac91628fa1da8)

### path-035577

```text
(config)# do-exec test cef idb consistency <cr>
```

Handler ` RVA 0xB3DD800 `；selector ` 0 `；EOL ` RVA 0x33754490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6da3a09591ea7b95](../../evidence/conditions-sets-042.md#c-6da3a09591ea7b95) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062486

```text
(config)# do-exec test cef idb decap <interface> <address> add lisp <cr>
```

Handler ` RVA 0xB3DCE50 `；selector ` 0 `；EOL ` RVA 0x33754918 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-0756bd18dca6f752](../../evidence/conditions-sets-003.md#c-0756bd18dca6f752) · [缺口 G-9f74540137529f16](../../evidence/gaps-sets-006.md#g-9f74540137529f16) · [参数 P-5e5e5f533c1ff8af](../../evidence/parameters-sets-008.md#p-5e5e5f533c1ff8af) · [状态效果 S-22521be463b6a560](../../evidence/state_effects-sets-008.md#s-22521be463b6a560)

### path-062265

```text
(config)# do-exec test cef idb stats IPv4 tx <interface> <cr>
```

Handler ` RVA 0xB3DD930 `；selector ` 0 `；EOL ` RVA 0x33754180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-52352ea12adf265a](../../evidence/conditions-sets-032.md#c-52352ea12adf265a) · [缺口 G-dfc05f1ab13deee3](../../evidence/gaps-sets-008.md#g-dfc05f1ab13deee3) · [参数 P-6cd06bf7c42e856d](../../evidence/parameters-sets-009.md#p-6cd06bf7c42e856d) · [状态效果 S-02b5516445e20e89](../../evidence/state_effects-sets-001.md#s-02b5516445e20e89)

### path-062264

```text
(config)# do-exec test cef lisp authc IPv4 <prefix:dynamic> enable <cr>
```

Handler ` RVA 0xB369550 `；selector ` 0 `；EOL ` RVA 0x337503A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` prefix/len。

[条件 C-f8466673e83da616](../../evidence/conditions-sets-096.md#c-f8466673e83da616) · [缺口 G-187586db704b5aaa](../../evidence/gaps-sets-001.md#g-187586db704b5aaa) · [参数 P-d35095c05e0db2c8](../../evidence/parameters-sets-016.md#p-d35095c05e0db2c8) · [状态效果 S-0aad4397a97999f4](../../evidence/state_effects-sets-003.md#s-0aad4397a97999f4)

### path-059039

```text
(config)# do-exec test cef lisp l2instance create <number:0..65520> <number:0..65520> <number:1..4094> <cr>
```

Handler ` RVA 0xB369280 `；selector ` 0 `；EOL ` RVA 0x3374F290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Topology ID；` unsigned_number ` Instance ID；` unsigned_number ` L2 Domain ID。

[条件 C-939762f2d506bdf0](../../evidence/conditions-sets-057.md#c-939762f2d506bdf0) · [参数 P-418c739674d1ed69](../../evidence/parameters-sets-006.md#p-418c739674d1ed69) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059055

```text
(config)# do-exec test cef lisp map-req IPv4 <address> <address> r-eid <cr>
```

Handler ` RVA 0xB368BF0 `；selector ` 0 `；EOL ` RVA 0x3374EC28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Src Addr；` address ` Dst Addr。

[条件 C-eb7803fd2758bcb1](../../evidence/conditions-sets-091.md#c-eb7803fd2758bcb1) · [参数 P-a9fceed457be317e](../../evidence/parameters-sets-013.md#p-a9fceed457be317e) · [状态效果 S-c116240e3d199034](../../evidence/state_effects-sets-041.md#s-c116240e3d199034)

### path-062638

```text
(config)# do-exec test cef lisp map-req IPv4 vrf <?option@555588ca2a88> <address> <address> r-eid <cr>
```

Handler ` RVA 0xB368BF0 `；selector ` 0 `；EOL ` RVA 0x3374EC28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Src Addr；` address ` Dst Addr。

[条件 C-627155dbeca643d5](../../evidence/conditions-sets-038.md#c-627155dbeca643d5) · [缺口 G-bbc3670176e6bf0d](../../evidence/gaps-sets-007.md#g-bbc3670176e6bf0d) · [参数 P-a9fceed457be317e](../../evidence/parameters-sets-013.md#p-a9fceed457be317e) · [状态效果 S-2b3b1bed6340c50a](../../evidence/state_effects-sets-010.md#s-2b3b1bed6340c50a)

### path-052762

```text
(config)# do-exec test cef lisp stats IPv4 clear <cr>
```

Handler ` RVA 0xB367480 `；selector ` 0 `；EOL ` RVA 0x3374FDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05c741388770c820](../../evidence/conditions-sets-003.md#c-05c741388770c820) · [状态效果 S-f7c654106f9ae0d4](../../evidence/state_effects-sets-052.md#s-f7c654106f9ae0d4)

### path-052804

```text
(config)# do-exec test cef lisp sw-fw eid-detection enable <cr>
```

Handler ` RVA 0xB3696E0 `；selector ` 0 `；EOL ` RVA 0x33750950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-767e2026818adc87](../../evidence/conditions-sets-046.md#c-767e2026818adc87) · [状态效果 S-e64e143fe2b75f10](../../evidence/state_effects-sets-049.md#s-e64e143fe2b75f10)

### path-057089

```text
(config)# do-exec test cef lisp unnum-if top-id <number:0..65520> clear-v4 <cr>
```

Handler ` RVA 0xB3693E0 `；selector ` 0 `；EOL ` RVA 0x3374F7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Topology ID。

[条件 C-a27f76df5f88e7bd](../../evidence/conditions-sets-063.md#c-a27f76df5f88e7bd) · [参数 P-05b6f7fd71866fd1](../../evidence/parameters-sets-001.md#p-05b6f7fd71866fd1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062479

```text
(config)# do-exec test cef lisp unnum-if top-id <number:0..65520> set-v4 <interface> <cr>
```

Handler ` RVA 0xB3693E0 `；selector ` 0 `；EOL ` RVA 0x3374F7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Topology ID。

[条件 C-77710f86db6c39af](../../evidence/conditions-sets-046.md#c-77710f86db6c39af) · [缺口 G-d3713e7a96a73d84](../../evidence/gaps-sets-007.md#g-d3713e7a96a73d84) · [参数 P-ddc7798318bed6a9](../../evidence/parameters-sets-017.md#p-ddc7798318bed6a9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035093

```text
(config)# do-exec test cef lisp_samecable <address> <cr>
```

Handler ` RVA 0xB368A00 `；selector ` 0 `；EOL ` RVA 0x3374E5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address。

[条件 C-b280d06b9c450e6d](../../evidence/conditions-sets-069.md#c-b280d06b9c450e6d) · [参数 P-7cbacb70d6c94687](../../evidence/parameters-sets-010.md#p-7cbacb70d6c94687) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060811

```text
(config)# do-exec test cef lisp_samecable <prefix:dynamic> <cr>
```

Handler ` RVA 0xB368A00 `；selector ` 0 `；EOL ` RVA 0x3374E5B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 Address。

[条件 C-145b8c80edf29810](../../evidence/conditions-sets-008.md#c-145b8c80edf29810) · [缺口 G-ed72ede88817e41c](../../evidence/gaps-sets-008.md#g-ed72ede88817e41c) · [参数 P-3634137072818ee1](../../evidence/parameters-sets-005.md#p-3634137072818ee1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061893

```text
(config)# do-exec test cef malloc fail <?option@555588cabbc8> fatal <cr>
```

Handler ` RVA 0xB410DF0 `；selector ` 0 `；EOL ` RVA 0x33757CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1caa83ab506a158a](../../evidence/conditions-sets-011.md#c-1caa83ab506a158a) · [缺口 G-f0c971659d8334ec](../../evidence/gaps-sets-008.md#g-f0c971659d8334ec) · [状态效果 S-d0e4fd8a727afa2c](../../evidence/state_effects-sets-044.md#s-d0e4fd8a727afa2c)

### path-045420

```text
(config)# do-exec test cef oce-explore IPv4 <address> <cr>
```

Handler ` RVA 0xB419590 `；selector ` 0 `；EOL ` RVA 0x337558B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-3ad4c58cf1ded92b](../../evidence/conditions-sets-023.md#c-3ad4c58cf1ded92b) · [参数 P-8b695f8397dd7da3](../../evidence/parameters-sets-011.md#p-8b695f8397dd7da3) · [状态效果 S-2dd9ad1847e4f84e](../../evidence/state_effects-sets-010.md#s-2dd9ad1847e4f84e)

### path-062271

```text
(config)# do-exec test cef oce-explore IPv4 vrf <?option@555588ca9660> <address> <cr>
```

Handler ` RVA 0xB419590 `；selector ` 0 `；EOL ` RVA 0x337558B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-2dcfb0cda3cbdfd1](../../evidence/conditions-sets-018.md#c-2dcfb0cda3cbdfd1) · [缺口 G-c0eaa1ea317d7e7e](../../evidence/gaps-sets-007.md#g-c0eaa1ea317d7e7e) · [参数 P-8b695f8397dd7da3](../../evidence/parameters-sets-011.md#p-8b695f8397dd7da3) · [状态效果 S-e019fbe43a0172c3](../../evidence/state_effects-sets-047.md#s-e019fbe43a0172c3)

### path-028984

```text
(config)# do-exec test cef offset <cr>
```

Handler ` RVA 0xB35E1A0 `；selector ` 0 `；EOL ` RVA 0x3374E258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc4fa007aa084224](../../evidence/conditions-sets-085.md#c-dc4fa007aa084224) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062273

```text
(config)# do-exec test cef register-interest IPv4 <?option@555588ca9088> <address> <number:0..32> <cr>
```

Handler ` RVA 0xB3A90C0 `；selector ` 0 `；EOL ` RVA 0x33754D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 prefix to register interest in；` unsigned_number ` IPv4 prefix mask。

[条件 C-fa8e86c18547fcd2](../../evidence/conditions-sets-097.md#c-fa8e86c18547fcd2) · [缺口 G-117eeb8e8ef26d9f](../../evidence/gaps-sets-001.md#g-117eeb8e8ef26d9f) · [参数 P-713ed46fa143524e](../../evidence/parameters-sets-009.md#p-713ed46fa143524e) · [状态效果 S-94fb75fd24e96996](../../evidence/state_effects-sets-032.md#s-94fb75fd24e96996)

### path-035625

```text
(config)# do-exec test cef register-interest show <cr>
```

Handler ` RVA 0xB3A90C0 `；selector ` 0 `；EOL ` RVA 0x33754D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d2d1f1a717981c2](../../evidence/conditions-sets-055.md#c-8d2d1f1a717981c2) · [状态效果 S-e718581f8fb29c2a](../../evidence/state_effects-sets-049.md#s-e718581f8fb29c2a)

### path-062263

```text
(config)# do-exec test cef rmi <interface> IPv4 <address> add <cr>
```

Handler ` RVA 0xB3DCCB0 `；selector ` 1 `；EOL ` RVA 0x33753550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-817fe486ebe67ad2](../../evidence/conditions-sets-050.md#c-817fe486ebe67ad2) · [缺口 G-7ed644211bb5f59a](../../evidence/gaps-sets-005.md#g-7ed644211bb5f59a) · [参数 P-56ff103610559c25](../../evidence/parameters-sets-007.md#p-56ff103610559c25) · [状态效果 S-6dedfd8b1b0718df](../../evidence/state_effects-sets-023.md#s-6dedfd8b1b0718df)

### path-062266

```text
(config)# do-exec test cef rmi <interface> IPv4 <address> remove <cr>
```

Handler ` RVA 0xB3DCCB0 `；selector ` 0 `；EOL ` RVA 0x337537F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-814abbbca567240f](../../evidence/conditions-sets-050.md#c-814abbbca567240f) · [缺口 G-7ed644211bb5f59a](../../evidence/gaps-sets-005.md#g-7ed644211bb5f59a) · [参数 P-56ff103610559c25](../../evidence/parameters-sets-007.md#p-56ff103610559c25) · [状态效果 S-6dedfd8b1b0718df](../../evidence/state_effects-sets-023.md#s-6dedfd8b1b0718df)

### path-061275

```text
(config)# do-exec test cef route-active IPv4 <prefix:dynamic> <cr>
```

Handler ` RVA 0xB369D60 `；selector ` 0 `；EOL ` RVA 0x33752870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` prefix/len。

[条件 C-890954a50f06118e](../../evidence/conditions-sets-053.md#c-890954a50f06118e) · [缺口 G-62bcfcd2be9ff1a4](../../evidence/gaps-sets-004.md#g-62bcfcd2be9ff1a4) · [参数 P-3fac20ab8914458b](../../evidence/parameters-sets-005.md#p-3fac20ab8914458b) · [状态效果 S-aeae402df84dd4a8](../../evidence/state_effects-sets-037.md#s-aeae402df84dd4a8)

### path-035454

```text
(config)# do-exec test cef sadr-oce <address> <cr>
```

Handler ` RVA 0xB369F40 `；selector ` 0 `；EOL ` RVA 0x33753C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address。

[条件 C-5987672af60d653c](../../evidence/conditions-sets-035.md#c-5987672af60d653c) · [参数 P-ae52a741803cbe9b](../../evidence/parameters-sets-013.md#p-ae52a741803cbe9b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061879

```text
(config)# do-exec test cef signal-oce IPv4 <prefix:dynamic> insert <cr>
```

Handler ` RVA 0xB369750 `；selector ` 0 `；EOL ` RVA 0x33751018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` prefix/len。

[条件 C-992d61d5c0450468](../../evidence/conditions-sets-059.md#c-992d61d5c0450468) · [缺口 G-f0413d89a28b83c8](../../evidence/gaps-sets-008.md#g-f0413d89a28b83c8) · [参数 P-259ca47d78c6590e](../../evidence/parameters-sets-003.md#p-259ca47d78c6590e) · [状态效果 S-aeac9f7c97a1eeb2](../../evidence/state_effects-sets-037.md#s-aeac9f7c97a1eeb2)

### path-062660

```text
(config)# do-exec test cef subtree context test add IPv4 <?option@555588cab548> <address> <number:0..32> <number:0..1000> <cr>
```

Handler ` RVA 0xB453970 `；selector ` 0 `；EOL ` RVA 0x33757740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix for ipv4 context；` unsigned_number ` Prefix length；` unsigned_number ` Context value。

[条件 C-be6697b4469ffe7f](../../evidence/conditions-sets-073.md#c-be6697b4469ffe7f) · [缺口 G-c982285cb2d57546](../../evidence/gaps-sets-007.md#g-c982285cb2d57546) · [参数 P-90f9654fd46995ba](../../evidence/parameters-sets-011.md#p-90f9654fd46995ba) · [状态效果 S-30f35c1895856ca3](../../evidence/state_effects-sets-011.md#s-30f35c1895856ca3)

### path-044833

```text
(config)# do-exec test cef switching IPv4 clear <cr>
```

Handler ` RVA 0xB4561F0 `；selector ` 0 `；EOL ` RVA 0x3374D358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b81d13bff9f87c3](../../evidence/conditions-sets-017.md#c-2b81d13bff9f87c3) · [状态效果 S-6805d9250a4a4b8d](../../evidence/state_effects-sets-022.md#s-6805d9250a4a4b8d)

### path-045643

```text
(config)# do-exec test cef track-destination IPv4 local-label <cr>
```

Handler ` RVA 0xB418EB0 `；selector ` 0 `；EOL ` RVA 0x33756740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b041c77c77a89b0](../../evidence/conditions-sets-048.md#c-7b041c77c77a89b0) · [状态效果 S-d1e929d079188bfd](../../evidence/state_effects-sets-044.md#s-d1e929d079188bfd)

### path-062278

```text
(config)# do-exec test cef track-destination IPv4 vrf <?option@555588caa480> local-label <cr>
```

Handler ` RVA 0xB418EB0 `；selector ` 0 `；EOL ` RVA 0x33756740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bbaa666db37f26f3](../../evidence/conditions-sets-072.md#c-bbaa666db37f26f3) · [缺口 G-59bfd0fe54820bea](../../evidence/gaps-sets-004.md#g-59bfd0fe54820bea) · [状态效果 S-9226d6d1799f1f23](../../evidence/state_effects-sets-031.md#s-9226d6d1799f1f23)

### path-035962

```text
(config)# do-exec test cef user-command <number:1..255> <cr>
```

Handler ` RVA 0xB485500 `；selector ` 0 `；EOL ` RVA 0x33756D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` User-command command number。

[条件 C-007620b9fa604aea](../../evidence/conditions-sets-001.md#c-007620b9fa604aea) · [参数 P-991dea8e01a30443](../../evidence/parameters-sets-012.md#p-991dea8e01a30443) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061880

```text
(config)# do-exec test cellular <interface> cdma rev-a enable <cr>
```

Handler ` RVA 0x16203510 `；selector ` 3 `；EOL ` RVA 0x35F37E98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1ade8326db941895](../../evidence/conditions-sets-011.md#c-1ade8326db941895) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-5b468e59624fd5ec](../../evidence/state_effects-sets-020.md#s-5b468e59624fd5ec)

### path-061883

```text
(config)# do-exec test cellular <interface> cnm-process-enqueue messages <number:0..5> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 0 `；EOL ` RVA 0x35F37B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0 - Heartbeat, 1 - Call disc, 2 - too hot,        3 - reset, 4 - modem up, 5 - undefined。

[条件 C-16d92fd39e12e218](../../evidence/conditions-sets-009.md#c-16d92fd39e12e218) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-9a3396f3e574aa4d](../../evidence/parameters-sets-012.md#p-9a3396f3e574aa4d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061252

```text
(config)# do-exec test cellular <interface> geofence-gps-periodic-timer-val <number:2..10> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 16 `；EOL ` RVA 0x35F35610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` GPS periodic update timer value in mins。

[条件 C-e028b57c935f3e94](../../evidence/conditions-sets-086.md#c-e028b57c935f3e94) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-0a4376ddcafe0447](../../evidence/parameters-sets-001.md#p-0a4376ddcafe0447) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060819

```text
(config)# do-exec test cellular <interface> gps-clear <cr>
```

Handler ` RVA 0x16203510 `；selector ` 9 `；EOL ` RVA 0x35F36B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a7747e5ab8f8ae09](../../evidence/conditions-sets-065.md#c-a7747e5ab8f8ae09) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061273

```text
(config)# do-exec test cellular <interface> gps-port GPS <cr>
```

Handler ` RVA 0x16203510 `；selector ` 11 `；EOL ` RVA 0x35F36EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1f684a152448df3b](../../evidence/conditions-sets-012.md#c-1f684a152448df3b) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-10df7c34eb884b9e](../../evidence/state_effects-sets-004.md#s-10df7c34eb884b9e)

### path-061278

```text
(config)# do-exec test cellular <interface> ims-service bind-subscription <cr>
```

Handler ` RVA 0x16203510 `；selector ` 17 `；EOL ` RVA 0x35F376F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c33fcb27c9df4889](../../evidence/conditions-sets-075.md#c-c33fcb27c9df4889) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-200c7c35540bec55](../../evidence/state_effects-sets-007.md#s-200c7c35540bec55)

### path-060786

```text
(config)# do-exec test cellular <interface> modem-at-all-admin-tech <cr>
```

Handler ` RVA 0x16203510 `；selector ` 20 `；EOL ` RVA 0x35F34D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f673516f62d7cb7](../../evidence/conditions-sets-031.md#c-4f673516f62d7cb7) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061249

```text
(config)# do-exec test cellular <interface> modem-at-command <string> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 18 `；EOL ` RVA 0x35F352E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` AT command string。

[条件 C-5085552c558d683c](../../evidence/conditions-sets-031.md#c-5085552c558d683c) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-49fb8efe53ffa1f7](../../evidence/parameters-sets-006.md#p-49fb8efe53ffa1f7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061261

```text
(config)# do-exec test cellular <interface> modem-dmlog disable <cr>
```

Handler ` RVA 0x16203510 `；selector ` 21 `；EOL ` RVA 0x35F36210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c5f5a83b4c60064b](../../evidence/conditions-sets-076.md#c-c5f5a83b4c60064b) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-000cbc53d7d975a3](../../evidence/state_effects-sets-001.md#s-000cbc53d7d975a3)

### path-060801

```text
(config)# do-exec test cellular <interface> modem-error-clear <cr>
```

Handler ` RVA 0x16203510 `；selector ` 10 `；EOL ` RVA 0x35F35B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-90f8c364d11c2010](../../evidence/conditions-sets-056.md#c-90f8c364d11c2010) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060807

```text
(config)# do-exec test cellular <interface> modem-power-cycle <cr>
```

Handler ` RVA 0x16203510 `；selector ` 2 `；EOL ` RVA 0x35F35DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ebb1874c19291a06](../../evidence/conditions-sets-091.md#c-ebb1874c19291a06) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060823

```text
(config)# do-exec test cellular <interface> modem-power-off <cr>
```

Handler ` RVA 0x16203510 `；selector ` 5 `；EOL ` RVA 0x35F38478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ec1532a6b049421](../../evidence/conditions-sets-037.md#c-5ec1532a6b049421) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060821

```text
(config)# do-exec test cellular <interface> modem-power-on <cr>
```

Handler ` RVA 0x16203510 `；selector ` 4 `；EOL ` RVA 0x35F381D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a7d8f836a7a7b9de](../../evidence/conditions-sets-065.md#c-a7d8f836a7a7b9de) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060796

```text
(config)# do-exec test cellular <interface> modem-reset <cr>
```

Handler ` RVA 0x16203510 `；selector ` 1 `；EOL ` RVA 0x35F358A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ffb417f4862a2f26](../../evidence/conditions-sets-099.md#c-ffb417f4862a2f26) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061274

```text
(config)# do-exec test cellular <interface> radio-power on <cr>
```

Handler ` RVA 0x16203510 `；selector ` 7 `；EOL ` RVA 0x35F37350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-43b6e3259c26864d](../../evidence/conditions-sets-026.md#c-43b6e3259c26864d) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-c0dac0cd7afd0734](../../evidence/state_effects-sets-041.md#s-c0dac0cd7afd0734)

### path-061260

```text
(config)# do-exec test cellular <interface> rsrp <number:0..150> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 13 `；EOL ` RVA 0x35F365E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` lte rsrp value。

[条件 C-a2dbf5f4e846873e](../../evidence/conditions-sets-063.md#c-a2dbf5f4e846873e) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-80a214569c60241d](../../evidence/parameters-sets-010.md#p-80a214569c60241d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061263

```text
(config)# do-exec test cellular <interface> rsrq <number:0..20> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 14 `；EOL ` RVA 0x35F368D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` lte rsrq value。

[条件 C-e45f1596baeb2384](../../evidence/conditions-sets-088.md#c-e45f1596baeb2384) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-9209a2c8cedfcc4e](../../evidence/parameters-sets-011.md#p-9209a2c8cedfcc4e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060784

```text
(config)# do-exec test cellular <interface> ursp-get-td <cr>
```

Handler ` RVA 0x16203510 `；selector ` 22 `；EOL ` RVA 0x35F34A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c7fc1913e0d7efd4](../../evidence/conditions-sets-077.md#c-c7fc1913e0d7efd4) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060788

```text
(config)# do-exec test cellular <interface> ursp-route-clear <cr>
```

Handler ` RVA 0x16203510 `；selector ` 19 `；EOL ` RVA 0x35F34FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-769419f9c9857887](../../evidence/conditions-sets-046.md#c-769419f9c9857887) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028680

```text
(config)# do-exec test checkpoint add <cr>
```

Handler ` RVA 0xCDD0C40 `；selector ` 0 `；EOL ` RVA 0x33CF0A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-4ef62180c1f3b774](../../evidence/state_effects-sets-017.md#s-4ef62180c1f3b774)

### path-029061

```text
(config)# do-exec test cisp disable <cr>
```

Handler ` RVA 0xCB25570 `；selector ` 0 `；EOL ` RVA 0x33BB54C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7568087aa5df99c9](../../evidence/conditions-sets-046.md#c-7568087aa5df99c9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029062

```text
(config)# do-exec test cisp enable <cr>
```

Handler ` RVA 0xCB254F0 `；selector ` 0 `；EOL ` RVA 0x33BB67C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7826896257e4387c](../../evidence/conditions-sets-047.md#c-7826896257e4387c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062480

```text
(config)# do-exec test cisp intf <interface> client add mac <address> <cr>
```

Handler ` RVA 0xCB25890 `；selector ` 0 `；EOL ` RVA 0x33BB5A48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48 bit mac address。

[条件 C-54fab9676dbf46ff](../../evidence/conditions-sets-033.md#c-54fab9676dbf46ff) · [缺口 G-30493fdda3f1d849](../../evidence/gaps-sets-002.md#g-30493fdda3f1d849) · [参数 P-bc23b0a3bd7fcf69](../../evidence/parameters-sets-014.md#p-bc23b0a3bd7fcf69) · [状态效果 S-a4dce89b992d43d6](../../evidence/state_effects-sets-035.md#s-a4dce89b992d43d6)

### path-061276

```text
(config)# do-exec test cisp intf <interface> stop <cr>
```

Handler ` RVA 0xCB256D0 `；selector ` 0 `；EOL ` RVA 0x33BB6390 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-81e20539a9a8e589](../../evidence/conditions-sets-050.md#c-81e20539a9a8e589) · [缺口 G-30493fdda3f1d849](../../evidence/gaps-sets-002.md#g-30493fdda3f1d849) · [参数 P-5fc6a08e308c7bce](../../evidence/parameters-sets-008.md#p-5fc6a08e308c7bce) · [状态效果 S-e12ec3ed69a3f612](../../evidence/state_effects-sets-048.md#s-e12ec3ed69a3f612)

### path-062482

```text
(config)# do-exec test cisp intf <interface> user add name <string> <cr>
```

Handler ` RVA 0xCB255C0 `；selector ` 0 `；EOL ` RVA 0x33BB5F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` user name。

[条件 C-b8b19e39b8037e4c](../../evidence/conditions-sets-071.md#c-b8b19e39b8037e4c) · [缺口 G-30493fdda3f1d849](../../evidence/gaps-sets-002.md#g-30493fdda3f1d849) · [参数 P-ef4244179b5b6bd7](../../evidence/parameters-sets-018.md#p-ef4244179b5b6bd7) · [状态效果 S-5bbc50497d3a6224](../../evidence/state_effects-sets-020.md#s-5bbc50497d3a6224)

### path-031508

```text
(config)# do-exec test clear-nvram local-lock <cr>
```

Handler ` RVA 0xE0E2710 `；selector ` 0 `；EOL ` RVA 0x341FA0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044389

```text
(config)# do-exec test cli-agent config-accounting test-mode disable <cr>
```

Handler ` RVA 0x143F2DB0 `；selector ` 1 `；EOL ` RVA 0x35D5DCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f42a4947ee5384e5](../../evidence/conditions-sets-094.md#c-f42a4947ee5384e5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044348

```text
(config)# do-exec test cli-agent config-accounting test-mode enable <cr>
```

Handler ` RVA 0x143F2DB0 `；selector ` 0 `；EOL ` RVA 0x35D5DA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d854b211a95e2849](../../evidence/conditions-sets-083.md#c-d854b211a95e2849) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031655

```text
(config)# do-exec test cns history <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 1 `；EOL ` RVA 0x34612D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031701

```text
(config)# do-exec test cns inventory <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 2 `；EOL ` RVA 0x34613250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031681

```text
(config)# do-exec test cns summary <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 3 `；EOL ` RVA 0x34612FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060936

```text
(config)# do-exec test config_notify_cb <interface> open_access <cr>
```

Handler ` RVA 0x15E9D3A0 `；selector ` 0 `；EOL ` RVA 0x35E5A8A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a42d48a0e7604f6](../../evidence/conditions-sets-047.md#c-7a42d48a0e7604f6) · [缺口 G-4a6d765040846e70](../../evidence/gaps-sets-003.md#g-4a6d765040846e70) · [参数 P-4b32da70b58e4977](../../evidence/parameters-sets-006.md#p-4b32da70b58e4977) · [状态效果 S-d46bf5ac0b6fcaaa](../../evidence/state_effects-sets-045.md#s-d46bf5ac0b6fcaaa)

### path-046620

```text
(config)# do-exec test cops start-listen <address> <number:0..65535> <cr>
```

Handler ` RVA 0xF44A4B0 `；selector ` 1 `；EOL ` RVA 0x3464CA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address to listen for；` unsigned_number ` port number。

[条件 C-c804a50dadac8b22](../../evidence/conditions-sets-077.md#c-c804a50dadac8b22) · [参数 P-1c899d9a6cba1e7a](../../evidence/parameters-sets-003.md#p-1c899d9a6cba1e7a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-046668

```text
(config)# do-exec test cops stop-listen <address> <number:0..65535> <cr>
```

Handler ` RVA 0xF44A4B0 `；selector ` 2 `；EOL ` RVA 0x3464CD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address to stop listening for；` unsigned_number ` port number。

[条件 C-c804a50dadac8b22](../../evidence/conditions-sets-077.md#c-c804a50dadac8b22) · [参数 P-365bcbc13d07ba46](../../evidence/parameters-sets-005.md#p-365bcbc13d07ba46) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061865

```text
(config)# do-exec test cot loop-on <?controller_action@55558b45eaa8> : <number:0..29> <cr>
```

Handler ` RVA 0x161B8850 `；selector ` 0 `；EOL ` RVA 0x35F0AB88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS0 Number。

[条件 C-ce1262f8fe33f6c0](../../evidence/conditions-sets-079.md#c-ce1262f8fe33f6c0) · [缺口 G-2395d8a2f53c6fbd](../../evidence/gaps-sets-002.md#g-2395d8a2f53c6fbd) · [参数 P-9e40bf7e70a74299](../../evidence/parameters-sets-012.md#p-9e40bf7e70a74299) · [状态效果 S-4151293dfcb44e5a](../../evidence/state_effects-sets-014.md#s-4151293dfcb44e5a)

### path-035277

```text
(config)# do-exec test cot set def-params <cr>
```

Handler ` RVA 0x161B8850 `；selector ` 0 `；EOL ` RVA 0x35F0AB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-7978a5221bb56ae1](../../evidence/state_effects-sets-026.md#s-7978a5221bb56ae1)

### path-034359

```text
(config)# do-exec test cpuaccounting debug dump <cr>
```

Handler ` RVA 0xE0822D0 `；selector ` 0 `；EOL ` RVA 0x341DCE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f60f537ad29f8993](../../evidence/state_effects-sets-052.md#s-f60f537ad29f8993)

### path-034250

```text
(config)# do-exec test cpurmi hog complex <cr>
```

Handler ` RVA 0xD6D2410 `；selector ` 2 `；EOL ` RVA 0x33ECD828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044032

```text
(config)# do-exec test cpurmi hog simple <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2410 `；selector ` 1 `；EOL ` RVA 0x33ECD5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Slot Number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-8683939829a6685a](../../evidence/parameters-sets-010.md#p-8683939829a6685a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026613

```text
(config)# do-exec test crash <cr>
```

Handler ` RVA 0xE8F5540 `；selector ` 0 `；EOL ` RVA 0x3433F780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059872

```text
(config)# do-exec test crypto kgs-test perf controller <number:1..300> <number:1..300> <number:1..10000> <number:1..300> <cr>
```

Handler ` RVA 0x12132450 `；selector ` 0 `；EOL ` RVA 0x357A1208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting k-value；` unsigned_number ` Ending k-value；` unsigned_number ` Number of trials for timing；` unsigned_number ` K-value interval size。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [参数 P-720889cf2f064708](../../evidence/parameters-sets-009.md#p-720889cf2f064708) · [状态效果 S-8bf7f823be69a58f](../../evidence/state_effects-sets-030.md#s-8bf7f823be69a58f)

### path-038806

```text
(config)# do-exec test crypto modexp perf-test <cr>
```

Handler ` RVA 0x120E8FF0 `；selector ` 0 `；EOL ` RVA 0x357A0AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038860

```text
(config)# do-exec test crypto modexp self-test <cr>
```

Handler ` RVA 0x120E8C60 `；selector ` 0 `；EOL ` RVA 0x357A0D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038974

```text
(config)# do-exec test crypto nist-tests cfb8 <cr>
```

Handler ` RVA 0x120E8B50 `；selector ` 0 `；EOL ` RVA 0x357A1650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-e9b1c7d1013c8c14](../../evidence/state_effects-sets-049.md#s-e9b1c7d1013c8c14)

### path-048506

```text
(config)# do-exec test crypto pki api <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 9 `；EOL ` RVA 0x3575A2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` API name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-56e00e3d600f8fae](../../evidence/parameters-sets-007.md#p-56e00e3d600f8fae) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048197

```text
(config)# do-exec test crypto pki benchmark rsa <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 4 `；EOL ` RVA 0x35757D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054764

```text
(config)# do-exec test crypto pki benchmark validate-peer <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 6 `；EOL ` RVA 0x35758420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e5897f7a7dfdc707](../../evidence/parameters-sets-017.md#p-e5897f7a7dfdc707) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054744

```text
(config)# do-exec test crypto pki benchmark validate-router <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 5 `；EOL ` RVA 0x35758120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint to validate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a79f40b9c7686186](../../evidence/parameters-sets-013.md#p-a79f40b9c7686186) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048249

```text
(config)# do-exec test crypto pki cache on <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 10 `；EOL ` RVA 0x357590F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-2c1c92c68a557679](../../evidence/state_effects-sets-010.md#s-2c1c92c68a557679)

### path-038871

```text
(config)# do-exec test crypto pki cert-attributes <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 1 `；EOL ` RVA 0x35757150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047702

```text
(config)# do-exec test crypto pki config-update-notify <string> <cr>
```

Handler ` RVA 0x11F3D8C0 `；selector ` 0 `；EOL ` RVA 0x35756438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` HA request string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-cace0a1b6548127a](../../evidence/parameters-sets-015.md#p-cace0a1b6548127a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054557

```text
(config)# do-exec test crypto pki crl request <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 18 `；EOL ` RVA 0x35756760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for the CRL request。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-823609e6f38dac50](../../evidence/parameters-sets-010.md#p-823609e6f38dac50) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054706

```text
(config)# do-exec test crypto pki csr <string> nb <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 8 `；EOL ` RVA 0x35758788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint for new certificate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9385614f2d1b8c51](../../evidence/parameters-sets-011.md#p-9385614f2d1b8c51) · [状态效果 S-3cc3ce81ceb1ac99](../../evidence/state_effects-sets-013.md#s-3cc3ce81ceb1ac99)

### path-039591

```text
(config)# do-exec test crypto pki enrollment-proxy-api <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 12 `；EOL ` RVA 0x3575A6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048442

```text
(config)# do-exec test crypto pki expiry-alerts reset <cr>
```

Handler ` RVA 0x1202AFD0 `；selector ` 0 `；EOL ` RVA 0x35759F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048378

```text
(config)# do-exec test crypto pki expiry-alerts shrink-periodicity <cr>
```

Handler ` RVA 0x1202AF70 `；selector ` 0 `；EOL ` RVA 0x35759CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048036

```text
(config)# do-exec test crypto pki new-cert <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 7 `；EOL ` RVA 0x357579B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint to se for new certificate (shadow) operations。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c90f6fedf1b7f7ab](../../evidence/parameters-sets-015.md#p-c90f6fedf1b7f7ab) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-058090

```text
(config)# do-exec test crypto pki ocsp-get-staple <string> chain blocking-test <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 16 `；EOL ` RVA 0x35756DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a0283f60f8b05691](../../evidence/parameters-sets-012.md#p-a0283f60f8b05691) · [状态效果 S-f4a2ba69d728492b](../../evidence/state_effects-sets-052.md#s-f4a2ba69d728492b)

### path-039177

```text
(config)# do-exec test crypto pki openssl <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 19 `；EOL ` RVA 0x35758A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038723

```text
(config)# do-exec test crypto pki pkcs7verify <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 0 `；EOL ` RVA 0x357569F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048207

```text
(config)# do-exec test crypto pki safemode on <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 11 `；EOL ` RVA 0x35758D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-ea89bd81590bb45f](../../evidence/state_effects-sets-050.md#s-ea89bd81590bb45f)

### path-038967

```text
(config)# do-exec test crypto pki self-signed-certificate <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 3 `；EOL ` RVA 0x357576A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048288

```text
(config)# do-exec test crypto pki session <number:1..60> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 15 `；EOL ` RVA 0x35759450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session Lifetime。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-d9270027cf31aba6](../../evidence/parameters-sets-016.md#p-d9270027cf31aba6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048386

```text
(config)# do-exec test crypto pki trustpool remove <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 14 `；EOL ` RVA 0x357599E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048330

```text
(config)# do-exec test crypto pki trustpool reset <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 13 `；EOL ` RVA 0x35759740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038909

```text
(config)# do-exec test crypto pki verify-certificate <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 2 `；EOL ` RVA 0x357573F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038764

```text
(config)# do-exec test crypto replay <number:1..4294967295> <cr>
```

Handler ` RVA 0x120E8740 `；selector ` 0 `；EOL ` RVA 0x357A0528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Replay counter value。

[条件 C-b8190406c976fefd](../../evidence/conditions-sets-071.md#c-b8190406c976fefd) · [参数 P-17461aa5dd937e32](../../evidence/parameters-sets-002.md#p-17461aa5dd937e32) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047858

```text
(config)# do-exec test crypto replay time <number:1..42949672> <cr>
```

Handler ` RVA 0x120E88B0 `；selector ` 0 `；EOL ` RVA 0x357A0280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Replay time value (seconds)。

[条件 C-3d196f218cec6a7d](../../evidence/conditions-sets-024.md#c-3d196f218cec6a7d) · [参数 P-b5994b27a0bb9e74](../../evidence/parameters-sets-014.md#p-b5994b27a0bb9e74) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031360

```text
(config)# do-exec test crypto rng-tests <cr>
```

Handler ` RVA 0x120E8C00 `；selector ` 0 `；EOL ` RVA 0x3579FE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-c3d07ca8db526df9](../../evidence/state_effects-sets-041.md#s-c3d07ca8db526df9)

### path-031411

```text
(config)# do-exec test crypto self-test <cr>
```

Handler ` RVA 0x12953C40 `；selector ` 0 `；EOL ` RVA 0x357A07C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6a17afdfb05f914](../../evidence/conditions-sets-095.md#c-f6a17afdfb05f914) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047734

```text
(config)# do-exec test crypto wui tti petitioner <cr>
```

Handler ` RVA 0x12E03210 `；selector ` 0 `；EOL ` RVA 0x359E4640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031424

```text
(config)# do-exec test cts enable <cr>
```

Handler ` RVA 0x13026640 `；selector ` 0 `；EOL ` RVA 0x35A121F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c46600dafa2c63f](../../evidence/conditions-sets-042.md#c-6c46600dafa2c63f) · [状态效果 S-7615380cbc7dc45f](../../evidence/state_effects-sets-025.md#s-7615380cbc7dc45f)

### path-048159

```text
(config)# do-exec test cts event trace enable <cr>
```

Handler ` RVA 0x131020F0 `；selector ` 0 `；EOL ` RVA 0x35A48190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-242c7a679db4d255](../../evidence/conditions-sets-014.md#c-242c7a679db4d255) · [状态效果 S-b0b4cdb5a575c1f5](../../evidence/state_effects-sets-037.md#s-b0b4cdb5a575c1f5)

### path-055138

```text
(config)# do-exec test cts role-based cgc qlist sort <cr>
```

Handler ` RVA 0x1423AAA0 `；selector ` 0 `；EOL ` RVA 0x35D07930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-059907

```text
(config)# do-exec test cts role-based counters from <number:2..65521> to <number:2..65521> hw <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 6 `；EOL ` RVA 0x35CFEF68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Security Group Tag；` unsigned_number ` Security Group Tag。

[条件 C-555d92626230ac57](../../evidence/conditions-sets-034.md#c-555d92626230ac57) · [参数 P-efb1785cb7b80b9c](../../evidence/parameters-sets-018.md#p-efb1785cb7b80b9c) · [状态效果 S-20c9b31b1fc190d1](../../evidence/state_effects-sets-007.md#s-20c9b31b1fc190d1)

### path-055018

```text
(config)# do-exec test cts role-based dump ipsgt <address> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 3 `；EOL ` RVA 0x35CEAD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 host address。

[条件 C-01cac479efb307bb](../../evidence/conditions-sets-001.md#c-01cac479efb307bb) · [参数 P-b80a5b0d81b8ff65](../../evidence/parameters-sets-014.md#p-b80a5b0d81b8ff65) · [状态效果 S-ce61e82cd936e6be](../../evidence/state_effects-sets-044.md#s-ce61e82cd936e6be)

### path-062056

```text
(config)# do-exec test cts role-based dump ipsgt <prefix:dynamic> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 3 `；EOL ` RVA 0x35CEAD98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-c20ae07807c8d056](../../evidence/conditions-sets-075.md#c-c20ae07807c8d056) · [缺口 G-09f47e5f6b20a016](../../evidence/gaps-sets-001.md#g-09f47e5f6b20a016) · [参数 P-81b24352e21d9ea8](../../evidence/parameters-sets-010.md#p-81b24352e21d9ea8) · [状态效果 S-fa159221fbc2a3d1](../../evidence/state_effects-sets-053.md#s-fa159221fbc2a3d1)

### path-048957

```text
(config)# do-exec test cts role-based dump permissions <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 1 `；EOL ` RVA 0x35D028E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-768d48daa17b6ad3](../../evidence/state_effects-sets-025.md#s-768d48daa17b6ad3)

### path-055176

```text
(config)# do-exec test cts role-based dump policy dynamic <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 0 `；EOL ` RVA 0x35D020E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e103ddfcec73277d](../../evidence/conditions-sets-087.md#c-e103ddfcec73277d) · [状态效果 S-10d7badbf4aa7d8e](../../evidence/state_effects-sets-004.md#s-10d7badbf4aa7d8e)

### path-048817

```text
(config)# do-exec test cts role-based dump sg-info <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 11 `；EOL ` RVA 0x35D02C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-e6b9ef8bcb5a216d](../../evidence/state_effects-sets-049.md#s-e6b9ef8bcb5a216d)

### path-055404

```text
(config)# do-exec test cts role-based echo cli <string> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 14 `；EOL ` RVA 0x35CEDD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Text line to print in selected context。

[条件 C-97473c061a130e0e](../../evidence/conditions-sets-058.md#c-97473c061a130e0e) · [参数 P-f304f9509e72a317](../../evidence/parameters-sets-018.md#p-f304f9509e72a317) · [状态效果 S-351371266af2d1e6](../../evidence/state_effects-sets-012.md#s-351371266af2d1e6)

### path-049202

```text
(config)# do-exec test cts role-based enforcement enable <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 13 `；EOL ` RVA 0x35D01AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-6195c9080de85d11](../../evidence/state_effects-sets-021.md#s-6195c9080de85d11)

### path-062053

```text
(config)# do-exec test cts role-based ipm <interface> stop <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 7 `；EOL ` RVA 0x35CEC6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b90b2e4a09e95ef9](../../evidence/conditions-sets-071.md#c-b90b2e4a09e95ef9) · [缺口 G-e224891e0ba87efc](../../evidence/gaps-sets-008.md#g-e224891e0ba87efc) · [参数 P-d273da3bd234e50b](../../evidence/parameters-sets-016.md#p-d273da3bd234e50b) · [状态效果 S-046d2559e85a5333](../../evidence/state_effects-sets-001.md#s-046d2559e85a5333)

### path-062073

```text
(config)# do-exec test cts role-based ipsgt add <prefix:dynamic> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 2 `；EOL ` RVA 0x35CEB560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-347ac834d4682a1d](../../evidence/conditions-sets-020.md#c-347ac834d4682a1d) · [缺口 G-33a060d1b0919c2f](../../evidence/gaps-sets-002.md#g-33a060d1b0919c2f) · [参数 P-6cfa815575ff5223](../../evidence/parameters-sets-009.md#p-6cfa815575ff5223) · [状态效果 S-8f5d292421c1483f](../../evidence/state_effects-sets-030.md#s-8f5d292421c1483f)

### path-048885

```text
(config)# do-exec test cts role-based ipsgt refresh <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 2 `；EOL ` RVA 0x35CEB560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-26212eccb70fbb2e](../../evidence/state_effects-sets-009.md#s-26212eccb70fbb2e)

### path-039826

```text
(config)# do-exec test cts role-based ping <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 12 `；EOL ` RVA 0x35CED858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-049199

```text
(config)# do-exec test cts role-based policy close <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 4 `；EOL ` RVA 0x35CFF6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-c209cc8af8347b00](../../evidence/state_effects-sets-041.md#s-c209cc8af8347b00)

### path-049198

```text
(config)# do-exec test cts role-based rbacl save <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 5 `；EOL ` RVA 0x35D01258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-348c9463d6b1a4c9](../../evidence/state_effects-sets-012.md#s-348c9463d6b1a4c9)

### path-039660

```text
(config)# do-exec test cts role-based sgacl-log <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 15 `；EOL ` RVA 0x35CED318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-055126

```text
(config)# do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 5 `；EOL ` RVA 0x35CF4950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18488cd3b28704ab](../../evidence/conditions-sets-009.md#c-18488cd3b28704ab) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-055174

```text
(config)# do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 4 `；EOL ` RVA 0x35CF4E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ca591f5cbabee00](../../evidence/conditions-sets-011.md#c-1ca591f5cbabee00) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-055216

```text
(config)# do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 3 `；EOL ` RVA 0x35CF5168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b932facf861018e](../../evidence/conditions-sets-017.md#c-2b932facf861018e) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-055248

```text
(config)# do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 2 `；EOL ` RVA 0x35CF5840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0c8a1607dafcbaf](../../evidence/conditions-sets-087.md#c-e0c8a1607dafcbaf) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-055286

```text
(config)# do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 1 `；EOL ` RVA 0x35CF5FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5bcef35116645995](../../evidence/conditions-sets-036.md#c-5bcef35116645995) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-055319

```text
(config)# do-exec test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 0 `；EOL ` RVA 0x35CF6688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c85c43e1b66083b8](../../evidence/conditions-sets-077.md#c-c85c43e1b66083b8) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-062372

```text
(config)# do-exec test cts role-based snmp mapping first <prefix:dynamic> <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 5 `；EOL ` RVA 0x35CF4950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Mappings for IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-6aecda040520671c](../../evidence/conditions-sets-041.md#c-6aecda040520671c) · [缺口 G-37f6681db1b2ce8f](../../evidence/gaps-sets-002.md#g-37f6681db1b2ce8f) · [参数 P-71c64710dd8ab2bf](../../evidence/parameters-sets-009.md#p-71c64710dd8ab2bf) · [状态效果 S-3cade3ea13fd7ddb](../../evidence/state_effects-sets-013.md#s-3cade3ea13fd7ddb)

### path-049069

```text
(config)# do-exec test cts role-based sw-dp enable <cr>
```

Handler ` RVA 0x142353B0 `；selector ` 0 `；EOL ` RVA 0x35D069B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [状态效果 S-2957dbdab256b79c](../../evidence/state_effects-sets-009.md#s-2957dbdab256b79c)

### path-062647

```text
(config)# do-exec test cts role-based sw-dp feature ipv4 in punt <?number_help_func_action@55558b25ae78> add <cr>
```

Handler ` RVA 0x142353B0 `；selector ` 1 `；EOL ` RVA 0x35D06F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f995db660610ff91](../../evidence/conditions-sets-096.md#c-f995db660610ff91) · [缺口 G-783cc8bbdf1b6ccb](../../evidence/gaps-sets-005.md#g-783cc8bbdf1b6ccb) · [状态效果 S-0ad7ffad4f2bd778](../../evidence/state_effects-sets-003.md#s-0ad7ffad4f2bd778)

### path-048373

```text
(config)# do-exec test cts role-based sync <number:1..2147483647> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 8 `；EOL ` RVA 0x35CECA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of times to synchronize。

[条件 C-74b8a98d68b9d9da](../../evidence/conditions-sets-045.md#c-74b8a98d68b9d9da) · [参数 P-d4f39e730e109d93](../../evidence/parameters-sets-016.md#p-d4f39e730e109d93) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039096

```text
(config)# do-exec test cts sap enable <cr>
```

Handler ` RVA 0x13060720 `；selector ` 0 `；EOL ` RVA 0x35A1DD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d6d417ef00db0b16](../../evidence/conditions-sets-083.md#c-d6d417ef00db0b16) · [状态效果 S-0acbf24de7a8e1cf](../../evidence/state_effects-sets-003.md#s-0acbf24de7a8e1cf)

### path-048188

```text
(config)# do-exec test cts slist_mib del ste <cr>
```

Handler ` RVA 0x130F3EA0 `；selector ` 0 `；EOL ` RVA 0x35A46768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-30ba82477e81d434](../../evidence/conditions-sets-019.md#c-30ba82477e81d434) · [状态效果 S-f4c97dfda0cb8c8e](../../evidence/state_effects-sets-052.md#s-f4c97dfda0cb8c8e)

### path-061506

```text
(config)# do-exec test cts snmp pacinfo <hex-string> <cr>
```

Handler ` RVA 0x13060720 `；selector ` 0 `；EOL ` RVA 0x35A1DD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` A-ID expressed as hex string。

[条件 C-48a34650e72757f3](../../evidence/conditions-sets-028.md#c-48a34650e72757f3) · [缺口 G-575aca7e43d8ba67](../../evidence/gaps-sets-004.md#g-575aca7e43d8ba67) · [参数 P-844fc89cb25ea8fa](../../evidence/parameters-sets-010.md#p-844fc89cb25ea8fa) · [状态效果 S-0cbce60b6653a63f](../../evidence/state_effects-sets-003.md#s-0cbce60b6653a63f)

### path-054851

```text
(config)# do-exec test cts sxp ipsgt action <number:0..2> <cr>
```

Handler ` RVA 0x13279440 `；selector ` 0 `；EOL ` RVA 0x35A53288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SNMP Action value。

[条件 C-c2e9c3decb32dd82](../../evidence/conditions-sets-075.md#c-c2e9c3decb32dd82) · [参数 P-09cbcd616efb3894](../../evidence/parameters-sets-001.md#p-09cbcd616efb3894) · [状态效果 S-5d94a7a88a64853e](../../evidence/state_effects-sets-020.md#s-5d94a7a88a64853e)

### path-034983

```text
(config)# do-exec test cwoir incr_sync on <cr>
```

Handler ` RVA 0xED96790 `；selector ` 0 `；EOL ` RVA 0x34430918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-3b7d90bfae2c5d45](../../evidence/state_effects-sets-013.md#s-3b7d90bfae2c5d45)

### path-044461

```text
(config)# do-exec test cwoir insert <number:1..13> <number:1..99> <cr>
```

Handler ` RVA 0xEDAEE90 `；selector ` 0 `；EOL ` RVA 0x3442F710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` card type (cwpa=15, cwatm=16, cwpos=17)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-bb83453e04561a3a](../../evidence/parameters-sets-014.md#p-bb83453e04561a3a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052490

```text
(config)# do-exec test cwoir iosrunning <number:1..13> <number:0..1> <number:1..99> <cr>
```

Handler ` RVA 0xEDAEDD0 `；selector ` 0 `；EOL ` RVA 0x3442FE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` cpu number；` unsigned_number ` card type (cwpa=15, cwatm=16, cwpos=17)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-041e16eff84e84cf](../../evidence/parameters-sets-001.md#p-041e16eff84e84cf) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052466

```text
(config)# do-exec test cwoir ipcready <number:1..13> <number:0..1> <number:0..3> <cr>
```

Handler ` RVA 0xEDAED10 `；selector ` 0 `；EOL ` RVA 0x3442FA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` cpu number；` unsigned_number ` swichover type。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a6eb3d08caf0a08c](../../evidence/parameters-sets-013.md#p-a6eb3d08caf0a08c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028768

```text
(config)# do-exec test cwoir read <cr>
```

Handler ` RVA 0xEDAEFB0 `；selector ` 0 `；EOL ` RVA 0x34430388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034831

```text
(config)# do-exec test cwoir remove <number:1..13> <cr>
```

Handler ` RVA 0xEDAEF30 `；selector ` 0 `；EOL ` RVA 0x34430100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9ca06d371d94a736](../../evidence/parameters-sets-012.md#p-9ca06d371d94a736) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028829

```text
(config)# do-exec test cwoir show <cr>
```

Handler ` RVA 0xEDAEFF0 `；selector ` 0 `；EOL ` RVA 0x34430630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027589

```text
(config)# do-exec test data-descriptor <cr>
```

Handler ` RVA 0xD550170 `；selector ` 0 `；EOL ` RVA 0x33E7FB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c78521e4c567f81f](../../evidence/conditions-sets-077.md#c-c78521e4c567f81f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060981

```text
(config)# do-exec test dhcp nonblocking <interface> <cr>
```

Handler ` RVA 0xF4733F0 `；selector ` 0 `；EOL ` RVA 0x346518B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f9fdcb38095a1d9c](../../evidence/conditions-sets-097.md#c-f9fdcb38095a1d9c) · [缺口 G-77fe4b9319fa4d93](../../evidence/gaps-sets-005.md#g-77fe4b9319fa4d93) · [参数 P-8feadcdc6b7fb192](../../evidence/parameters-sets-011.md#p-8feadcdc6b7fb192) · [状态效果 S-e3f897b10923544f](../../evidence/state_effects-sets-048.md#s-e3f897b10923544f)

### path-031426

```text
(config)# do-exec test dhcp ns <cr>
```

Handler ` RVA 0xF4743A0 `；selector ` 0 `；EOL ` RVA 0x34652410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031391

```text
(config)# do-exec test dhcp release <cr>
```

Handler ` RVA 0xF4733F0 `；selector ` 0 `；EOL ` RVA 0x346518B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-21f19451490b61f5](../../evidence/state_effects-sets-008.md#s-21f19451490b61f5)

### path-062995

```text
(config)# do-exec test diagnostic simulation failure slot <?option@5555898db9d0> test <?number_help_func_action@555589917be8> <cr>
```

Handler ` RVA 0xEB7FFE0 `；selector ` 0 `；EOL ` RVA 0x343C3CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-014e9eefd5a05121](../../evidence/conditions-sets-001.md#c-014e9eefd5a05121) · [缺口 G-fa35fb9275f4c2a8](../../evidence/gaps-sets-009.md#g-fa35fb9275f4c2a8) · [状态效果 S-3eda16ca5f816408](../../evidence/state_effects-sets-014.md#s-3eda16ca5f816408)

### path-037472

```text
(config)# do-exec test dmtm <number:0..64> cmd <cr>
```

Handler ` RVA 0x10C43D50 `；selector ` 0 `；EOL ` RVA 0x34CEBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot numbers (specify 0+ slots)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0e7af595ea053c84](../../evidence/parameters-sets-002.md#p-0e7af595ea053c84) · [状态效果 S-f3bcab1c6885807b](../../evidence/state_effects-sets-052.md#s-f3bcab1c6885807b)

### path-045886

```text
(config)# do-exec test dtp switch crash <number:0..3> <cr>
```

Handler ` RVA 0x15F15700 `；selector ` 0 `；EOL ` RVA 0x35E68DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` crash point:0-nocrash 1-reneg 2-compl 3-oper。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-576c7c500f9d549b](../../evidence/parameters-sets-007.md#p-576c7c500f9d549b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-029792

```text
(config)# do-exec test dwnld_mgr <string> <cr>
```

Handler ` RVA 0x10656760 `；selector ` 0 `；EOL ` RVA 0x34BDA0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` profile name。

[条件 C-59bebd9794d844b9](../../evidence/conditions-sets-035.md#c-59bebd9794d844b9) · [参数 P-0dadb8908436ba2e](../../evidence/parameters-sets-001.md#p-0dadb8908436ba2e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034549

```text
(config)# do-exec test eci add <string> <cr>
```

Handler ` RVA 0xDF98570 `；selector ` 0 `；EOL ` RVA 0x340E2DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` file containing eci chain input。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [参数 P-87f51bdf5a11fcb0](../../evidence/parameters-sets-010.md#p-87f51bdf5a11fcb0) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-034510

```text
(config)# do-exec test eci delete <string> <cr>
```

Handler ` RVA 0xDF97EA0 `；selector ` 0 `；EOL ` RVA 0x340E2AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` file containing eci chain input。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [参数 P-b0019edcb90aef5f](../../evidence/parameters-sets-013.md#p-b0019edcb90aef5f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028533

```text
(config)# do-exec test eci scan <cr>
```

Handler ` RVA 0xDF986D0 `；selector ` 0 `；EOL ` RVA 0x340E30C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-044378

```text
(config)# do-exec test eci set timeout <number:0..1000> <cr>
```

Handler ` RVA 0xDF988A0 `；selector ` 0 `；EOL ` RVA 0x340E33F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds to wait。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [参数 P-5e273781dbffcb2e](../../evidence/parameters-sets-008.md#p-5e273781dbffcb2e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-028595

```text
(config)# do-exec test eci show <cr>
```

Handler ` RVA 0xDF985D0 `；selector ` 0 `；EOL ` RVA 0x340E36C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b209e9867ab93018](../../evidence/conditions-sets-069.md#c-b209e9867ab93018) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-027609

```text
(config)# do-exec test eem <cr>
```

Handler ` RVA 0x1107A0B0 `；selector ` 0 `；EOL ` RVA 0x35386950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030826

```text
(config)# do-exec test eigrp SIA <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 105 `；EOL ` RVA 0x3469D878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7298c1a9645892c](../../evidence/conditions-sets-095.md#c-f7298c1a9645892c) · [状态效果 S-8636bce7446d34bb](../../evidence/state_effects-sets-028.md#s-8636bce7446d34bb)

### path-060933

```text
(config)# do-exec test eigrp SIA fast <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 105 `；EOL ` RVA 0x3469D878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7298c1a9645892c](../../evidence/conditions-sets-095.md#c-f7298c1a9645892c) · [缺口 G-6614e3e718917195](../../evidence/gaps-sets-004.md#g-6614e3e718917195) · [状态效果 S-6dd1a5cc0e411fbb](../../evidence/state_effects-sets-023.md#s-6dd1a5cc0e411fbb)

### path-047145

```text
(config)# do-exec test eigrp address-family ipv4 ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x346B9888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41f8139d1c26a2b9](../../evidence/conditions-sets-026.md#c-41f8139d1c26a2b9) · [状态效果 S-7ad92b570153c657](../../evidence/state_effects-sets-026.md#s-7ad92b570153c657)

### path-054464

```text
(config)# do-exec test eigrp address-family ipv4 error-percent <number:0..100> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x346B9F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-567eebbcb0aad439](../../evidence/conditions-sets-034.md#c-567eebbcb0aad439) · [参数 P-f2279363519f3eb4](../../evidence/parameters-sets-018.md#p-f2279363519f3eb4) · [状态效果 S-3dd643286d883947](../../evidence/state_effects-sets-014.md#s-3dd643286d883947)

### path-062356

```text
(config)# do-exec test eigrp address-family ipv4 error-percent <number:0..100> <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x346B9F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-b714a6ffe42da3d2](../../evidence/conditions-sets-071.md#c-b714a6ffe42da3d2) · [缺口 G-b666d46d08e756b9](../../evidence/gaps-sets-006.md#g-b666d46d08e756b9) · [参数 P-0ed98bbe6cb039b5](../../evidence/parameters-sets-002.md#p-0ed98bbe6cb039b5) · [状态效果 S-3dd643286d883947](../../evidence/state_effects-sets-014.md#s-3dd643286d883947)

### path-047115

```text
(config)# do-exec test eigrp address-family ipv6 ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x35457E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dffd991031595cab](../../evidence/conditions-sets-086.md#c-dffd991031595cab) · [状态效果 S-b90d203b8b57ed49](../../evidence/state_effects-sets-039.md#s-b90d203b8b57ed49)

### path-054453

```text
(config)# do-exec test eigrp address-family ipv6 error-percent <number:0..100> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x35458518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-332e7febc4848829](../../evidence/conditions-sets-020.md#c-332e7febc4848829) · [参数 P-9704e8c7268e4d69](../../evidence/parameters-sets-012.md#p-9704e8c7268e4d69) · [状态效果 S-00084c6fbb2c5f39](../../evidence/state_effects-sets-001.md#s-00084c6fbb2c5f39)

### path-062354

```text
(config)# do-exec test eigrp address-family ipv6 error-percent <number:0..100> <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x35458518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-618fa309458d6587](../../evidence/conditions-sets-038.md#c-618fa309458d6587) · [缺口 G-44b8315ac1655495](../../evidence/gaps-sets-003.md#g-44b8315ac1655495) · [参数 P-db7f017bd84e4834](../../evidence/parameters-sets-017.md#p-db7f017bd84e4834) · [状态效果 S-00084c6fbb2c5f39](../../evidence/state_effects-sets-001.md#s-00084c6fbb2c5f39)

### path-062335

```text
(config)# do-exec test eigrp address-family ipv6 topology <prefix:dynamic> ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x35457E08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to display information about。

[条件 C-f6a91d7ff9d4ae87](../../evidence/conditions-sets-095.md#c-f6a91d7ff9d4ae87) · [缺口 G-43d42dbacc6ab480](../../evidence/gaps-sets-003.md#g-43d42dbacc6ab480) · [参数 P-76139d13deebc6f8](../../evidence/parameters-sets-009.md#p-76139d13deebc6f8) · [状态效果 S-b90d203b8b57ed49](../../evidence/state_effects-sets-039.md#s-b90d203b8b57ed49)

### path-030690

```text
(config)# do-exec test eigrp crimson <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 106 `；EOL ` RVA 0x3469D428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d930ca6119535a50](../../evidence/conditions-sets-084.md#c-d930ca6119535a50) · [状态效果 S-8636bce7446d34bb](../../evidence/state_effects-sets-028.md#s-8636bce7446d34bb)

### path-061433

```text
(config)# do-exec test eigrp neighbor <interface> <address> <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 0 `；EOL ` RVA 0x3469DEA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 Neighbor Address。

[条件 C-1021fa73ffc0f404](../../evidence/conditions-sets-006.md#c-1021fa73ffc0f404) · [缺口 G-5b4c0f1fa7f61a5a](../../evidence/gaps-sets-004.md#g-5b4c0f1fa7f61a5a) · [参数 P-6fec578f8498d521](../../evidence/parameters-sets-009.md#p-6fec578f8498d521) · [状态效果 S-8636bce7446d34bb](../../evidence/state_effects-sets-028.md#s-8636bce7446d34bb)

### path-053798

```text
(config)# do-exec test ethernet errdisable recovery-timer unit second <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 0 `；EOL ` RVA 0x339882A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b8edb4566933087f](../../evidence/conditions-sets-071.md#c-b8edb4566933087f) · [状态效果 S-718c2d09494734f1](../../evidence/state_effects-sets-024.md#s-718c2d09494734f1)

### path-061873

```text
(config)# do-exec test ethernet l2ctrl safe-iteration vports <interface> <cr>
```

Handler ` RVA 0xC05DAC0 `；selector ` 0 `；EOL ` RVA 0x3398BB08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e33891baaab72b0f](../../evidence/conditions-sets-088.md#c-e33891baaab72b0f) · [缺口 G-99af9ad78aebf475](../../evidence/gaps-sets-006.md#g-99af9ad78aebf475) · [参数 P-564e2f745bdafea1](../../evidence/parameters-sets-007.md#p-564e2f745bdafea1) · [状态效果 S-2a126734d1a1d5f8](../../evidence/state_effects-sets-009.md#s-2a126734d1a1d5f8)

### path-046313

```text
(config)# do-exec test ethernet mirp-rcv isid <number:1..16777215> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 2 `；EOL ` RVA 0x33987DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` isid id。

[条件 C-df35fc317e2776ad](../../evidence/conditions-sets-086.md#c-df35fc317e2776ad) · [参数 P-e964ebd939a67768](../../evidence/parameters-sets-017.md#p-e964ebd939a67768) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061955

```text
(config)# do-exec test ethernet mlacp unknown interface <interface> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 3 `；EOL ` RVA 0x33987A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54479e1216c2576e](../../evidence/conditions-sets-033.md#c-54479e1216c2576e) · [缺口 G-1b2d9a673017c37a](../../evidence/gaps-sets-001.md#g-1b2d9a673017c37a) · [参数 P-4555fbb600f078f9](../../evidence/parameters-sets-006.md#p-4555fbb600f078f9) · [状态效果 S-00fa9daec2cb157a](../../evidence/state_effects-sets-001.md#s-00fa9daec2cb157a)

### path-061370

```text
(config)# do-exec test ethernet mstp-tcn-enable <interface> <number:0..1> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 6 `；EOL ` RVA 0x339871A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Test value。

[条件 C-29ab11f08175ef06](../../evidence/conditions-sets-016.md#c-29ab11f08175ef06) · [缺口 G-b04d24ac69d96cde](../../evidence/gaps-sets-006.md#g-b04d24ac69d96cde) · [参数 P-1a3a2550c907e43a](../../evidence/parameters-sets-002.md#p-1a3a2550c907e43a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061951

```text
(config)# do-exec test ethernet populate-statistics interface <interface> <number:1..16384> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 4 `；EOL ` RVA 0x339875D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance identifier。

[条件 C-c8ac2ccf8869f6b8](../../evidence/conditions-sets-077.md#c-c8ac2ccf8869f6b8) · [缺口 G-2aa7737c7d10dc6b](../../evidence/gaps-sets-002.md#g-2aa7737c7d10dc6b) · [参数 P-46c4b52712c73218](../../evidence/parameters-sets-006.md#p-46c4b52712c73218) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036761

```text
(config)# do-exec test ethernet safe-iteration <number:0..5> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 5 `；EOL ` RVA 0x33986DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Test case number。

[条件 C-fa740d3d754318cc](../../evidence/conditions-sets-097.md#c-fa740d3d754318cc) · [参数 P-bd87e469a1d0f0e7](../../evidence/parameters-sets-014.md#p-bd87e469a1d0f0e7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061974

```text
(config)# do-exec test ethernet stp-fwdstate <number:1..16384> <interface> disable <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 0 `；EOL ` RVA 0x339882A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance identifier。

[条件 C-315104c3e8c100c6](../../evidence/conditions-sets-019.md#c-315104c3e8c100c6) · [缺口 G-e199592ab58a2dc6](../../evidence/gaps-sets-008.md#g-e199592ab58a2dc6) · [参数 P-2d7fffaeea583df5](../../evidence/parameters-sets-004.md#p-2d7fffaeea583df5) · [状态效果 S-116811947cc5a293](../../evidence/state_effects-sets-004.md#s-116811947cc5a293)

### path-061975

```text
(config)# do-exec test ethernet stp-fwdstate <number:1..16384> <interface> forwarding <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 1 `；EOL ` RVA 0x339885C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance identifier。

[条件 C-ac06cbd2bafb9a8a](../../evidence/conditions-sets-066.md#c-ac06cbd2bafb9a8a) · [缺口 G-e199592ab58a2dc6](../../evidence/gaps-sets-008.md#g-e199592ab58a2dc6) · [参数 P-2d7fffaeea583df5](../../evidence/parameters-sets-004.md#p-2d7fffaeea583df5) · [状态效果 S-47ba8faf69fb93e8](../../evidence/state_effects-sets-016.md#s-47ba8faf69fb93e8)

### path-047446

```text
(config)# do-exec test event manager ged define <cr>
```

Handler ` RVA 0x110CDE30 `；selector ` 0 `；EOL ` RVA 0x353A63D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5d3923f222a3ef82](../../evidence/conditions-sets-036.md#c-5d3923f222a3ef82) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047498

```text
(config)# do-exec test event manager ged publish <cr>
```

Handler ` RVA 0x110CDC70 `；selector ` 0 `；EOL ` RVA 0x353A6678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05ffda84a3a2a421](../../evidence/conditions-sets-003.md#c-05ffda84a3a2a421) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-047544

```text
(config)# do-exec test event manager ged subscribe <cr>
```

Handler ` RVA 0x110CDD70 `；selector ` 0 `；EOL ` RVA 0x353A6920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b16be1f54ae86ae2](../../evidence/conditions-sets-069.md#c-b16be1f54ae86ae2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054485

```text
(config)# do-exec test event manager ged unsubscribe <number:0..2147483647> <cr>
```

Handler ` RVA 0x110CDDD0 `；selector ` 0 `；EOL ` RVA 0x353A6C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` subscription id。

[条件 C-b4cefe565a8a17d8](../../evidence/conditions-sets-070.md#c-b4cefe565a8a17d8) · [参数 P-e54fd61c119df86e](../../evidence/parameters-sets-017.md#p-e54fd61c119df86e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039730

```text
(config)# do-exec test flowspec client stop <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 1 `；EOL ` RVA 0x35A9B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b71df096cc2567e3](../../evidence/conditions-sets-071.md#c-b71df096cc2567e3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039608

```text
(config)# do-exec test flowspec client xos <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 0 `；EOL ` RVA 0x35A9B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f56987fb75cd6a8b](../../evidence/conditions-sets-095.md#c-f56987fb75cd6a8b) · [状态效果 S-581489f23f580e6d](../../evidence/state_effects-sets-019.md#s-581489f23f580e6d)

### path-031828

```text
(config)# do-exec test flowspec rt-dump <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 4 `；EOL ` RVA 0x35A9C2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b01bef5386753493](../../evidence/conditions-sets-068.md#c-b01bef5386753493) · [状态效果 S-60889f06e74ffddb](../../evidence/state_effects-sets-021.md#s-60889f06e74ffddb)

### path-031801

```text
(config)# do-exec test flowspec txlist-dump <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 5 `；EOL ` RVA 0x35A9C5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f802aac3afb08c4a](../../evidence/conditions-sets-096.md#c-f802aac3afb08c4a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031850

```text
(config)# do-exec test flowspec xtf <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 2 `；EOL ` RVA 0x35A9BFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29b6b000659bdeff](../../evidence/conditions-sets-016.md#c-29b6b000659bdeff) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039667

```text
(config)# do-exec test flowspec xtf print <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 3 `；EOL ` RVA 0x35A9BC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-092e5569d02a3416](../../evidence/conditions-sets-004.md#c-092e5569d02a3416) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-030998

```text
(config)# do-exec test fqdn <number:0..14> <cr>
```

Handler ` RVA 0xC2E4050 `；selector ` 5 `；EOL ` RVA 0x33A3DF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 0 to disable ut test flag, 1-14 to execute different ut cases。

[条件 C-e48d1444c828648f](../../evidence/conditions-sets-088.md#c-e48d1444c828648f) · [参数 P-c9a94d867a4371a2](../../evidence/parameters-sets-015.md#p-c9a94d867a4371a2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035494

```text
(config)# do-exec test garp_retry add <address> <cr>
```

Handler ` RVA 0xCF73340 `；selector ` 0 `；EOL ` RVA 0x33D441B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` ip address。

[条件 C-3cbae58812f0e31a](../../evidence/conditions-sets-024.md#c-3cbae58812f0e31a) · [参数 P-e55458f9b27c5030](../../evidence/parameters-sets-017.md#p-e55458f9b27c5030) · [状态效果 S-da09ddf5d2fb3cdd](../../evidence/state_effects-sets-046.md#s-da09ddf5d2fb3cdd)

### path-061884

```text
(config)# do-exec test garp_retry add <address> <interface> <number:0..2> <cr>
```

Handler ` RVA 0xCF73340 `；selector ` 0 `；EOL ` RVA 0x33D441B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address；` unsigned_number ` Trigger。

[条件 C-d82f653a9353c3db](../../evidence/conditions-sets-083.md#c-d82f653a9353c3db) · [缺口 G-bd830bbaea9935f0](../../evidence/gaps-sets-007.md#g-bd830bbaea9935f0) · [参数 P-633efffd12831efa](../../evidence/parameters-sets-008.md#p-633efffd12831efa) · [状态效果 S-da09ddf5d2fb3cdd](../../evidence/state_effects-sets-046.md#s-da09ddf5d2fb3cdd)

### path-046477

```text
(config)# do-exec test glbp redundancy events enable <cr>
```

Handler ` RVA 0xE169F90 `；selector ` 50 `；EOL ` RVA 0x34224F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-7ca2f0e313739c6c](../../evidence/state_effects-sets-026.md#s-7ca2f0e313739c6c)

### path-062323

```text
(config)# do-exec test glbp transport <interface> <number:0..1023> ipv6 <address> <cr>
```

Handler ` RVA 0xE169F90 `；selector ` 51 `；EOL ` RVA 0x34224B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number；` address ` IPv6 address。

[条件 C-6127714d47afbc1e](../../evidence/conditions-sets-038.md#c-6127714d47afbc1e) · [缺口 G-1a7b639af7992f5f](../../evidence/gaps-sets-001.md#g-1a7b639af7992f5f) · [参数 P-7ac840779107458d](../../evidence/parameters-sets-010.md#p-7ac840779107458d) · [状态效果 S-6bfcfb07aaf09e56](../../evidence/state_effects-sets-023.md#s-6bfcfb07aaf09e56)

### path-054995

```text
(config)# do-exec test gsi httpc <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 0 `；EOL ` RVA 0x346228C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-bc21db5c44e878eb](../../evidence/state_effects-sets-040.md#s-bc21db5c44e878eb)

### path-048604

```text
(config)# do-exec test gsi httpc <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 0 `；EOL ` RVA 0x346225B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-5ebcceb8883dfe78](../../evidence/state_effects-sets-020.md#s-5ebcceb8883dfe78)

### path-058235

```text
(config)# do-exec test gsi httpc <number:0..9> start <string> post <cr>
```

Handler ` RVA 0xF3B2930 `；selector ` 0 `；EOL ` RVA 0x34621F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a85c754192468da0](../../evidence/parameters-sets-013.md#p-a85c754192468da0) · [状态效果 S-54e783c9e761e5b3](../../evidence/state_effects-sets-018.md#s-54e783c9e761e5b3)

### path-048717

```text
(config)# do-exec test gsi httpc <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 0 `；EOL ` RVA 0x34622BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-ca28a00e8a9712b0](../../evidence/state_effects-sets-043.md#s-ca28a00e8a9712b0)

### path-039561

```text
(config)# do-exec test gsi httpc stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 0 `；EOL ` RVA 0x34622280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-5ebcceb8883dfe78](../../evidence/state_effects-sets-020.md#s-5ebcceb8883dfe78)

### path-054964

```text
(config)# do-exec test gsi https <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 1 `；EOL ` RVA 0x346215E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-4f8591ad805b8ed6](../../evidence/state_effects-sets-017.md#s-4f8591ad805b8ed6)

### path-048545

```text
(config)# do-exec test gsi https <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 1 `；EOL ` RVA 0x346212D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-c9e32d26ab281d1b](../../evidence/state_effects-sets-043.md#s-c9e32d26ab281d1b)

### path-059442

```text
(config)# do-exec test gsi https <number:0..9> start <string> encrypt post <cr>
```

Handler ` RVA 0xF3B2A20 `；selector ` 0 `；EOL ` RVA 0x34620AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-49005321df5f5cf4](../../evidence/parameters-sets-006.md#p-49005321df5f5cf4) · [状态效果 S-658b05980d758a64](../../evidence/state_effects-sets-022.md#s-658b05980d758a64)

### path-048661

```text
(config)# do-exec test gsi https <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 1 `；EOL ` RVA 0x346218E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-6252938825b632cd](../../evidence/state_effects-sets-021.md#s-6252938825b632cd)

### path-039508

```text
(config)# do-exec test gsi https stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 1 `；EOL ` RVA 0x34620FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-c9e32d26ab281d1b](../../evidence/state_effects-sets-043.md#s-c9e32d26ab281d1b)

### path-054934

```text
(config)# do-exec test gsi sshc <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 2 `；EOL ` RVA 0x34620068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-ab901e9a66d30925](../../evidence/state_effects-sets-036.md#s-ab901e9a66d30925)

### path-048487

```text
(config)# do-exec test gsi sshc <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 2 `；EOL ` RVA 0x3461FD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-1bead617cf04387a](../../evidence/state_effects-sets-006.md#s-1bead617cf04387a)

### path-058212

```text
(config)# do-exec test gsi sshc <number:0..9> start <string> wsma <cr>
```

Handler ` RVA 0xF3B10E0 `；selector ` 0 `；EOL ` RVA 0x3461F6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0608e1b131dc833a](../../evidence/parameters-sets-001.md#p-0608e1b131dc833a) · [状态效果 S-f660a01116aaa07c](../../evidence/state_effects-sets-052.md#s-f660a01116aaa07c)

### path-048609

```text
(config)# do-exec test gsi sshc <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 2 `；EOL ` RVA 0x34620360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-5100407b160010fa](../../evidence/state_effects-sets-018.md#s-5100407b160010fa)

### path-039457

```text
(config)# do-exec test gsi sshc stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 2 `；EOL ` RVA 0x3461FA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1bead617cf04387a](../../evidence/state_effects-sets-006.md#s-1bead617cf04387a)

### path-038015

```text
(config)# do-exec test gssapi init_sec_context <string> <cr>
```

Handler ` RVA 0xC3DCF70 `；selector ` 1 `；EOL ` RVA 0x33A66FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The server name or target name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-43e4e0daf266aaf3](../../evidence/parameters-sets-006.md#p-43e4e0daf266aaf3) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054418

```text
(config)# do-exec test gssapi token_exchange no_wrap <address> <string> <cr>
```

Handler ` RVA 0xC3DCF70 `；selector ` 2 `；EOL ` RVA 0x33A673D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote hostname or IP address；` string ` The server name or target name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-fd7d94e1b385dba2](../../evidence/parameters-sets-019.md#p-fd7d94e1b385dba2) · [状态效果 S-5b9abbe6df9ba302](../../evidence/state_effects-sets-020.md#s-5b9abbe6df9ba302)

### path-049582

```text
(config)# do-exec test gx access-accept service <string> <cr>
```

Handler ` RVA 0xBD23280 `；selector ` 1 `；EOL ` RVA 0x338C3BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Service name。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [参数 P-62d5f9834b5f4036](../../evidence/parameters-sets-008.md#p-62d5f9834b5f4036) · [状态效果 S-ecf74eb681f6ea91](../../evidence/state_effects-sets-050.md#s-ecf74eb681f6ea91)

### path-032039

```text
(config)# do-exec test gx access-reject <cr>
```

Handler ` RVA 0xBD23380 `；selector ` 1 `；EOL ` RVA 0x338C3E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062941

```text
(config)# do-exec test gx create-session ip <address> mac <hex-data> vrf <string> vlan-id <string> <interface> client-handle <number:1000..2000> <cr>
```

Handler ` RVA 0xBD21B90 `；selector ` 1 `；EOL ` RVA 0x338C2940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the subscriber；` unsigned_number ` Client Handle limit。

[条件 C-c02979819a657213](../../evidence/conditions-sets-074.md#c-c02979819a657213) · [缺口 G-672d03da2093e5cd](../../evidence/gaps-sets-004.md#g-672d03da2093e5cd) · [参数 P-ca5b96fd1ea8020b](../../evidence/parameters-sets-015.md#p-ca5b96fd1ea8020b) · [状态效果 S-c2ac8bb65c490deb](../../evidence/state_effects-sets-041.md#s-c2ac8bb65c490deb)

### path-049535

```text
(config)# do-exec test gx delete-session ip <address> <cr>
```

Handler ` RVA 0xBD21FF0 `；selector ` 1 `；EOL ` RVA 0x338C2DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of the subscriber。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [参数 P-e8e8b1f79c8c540d](../../evidence/parameters-sets-017.md#p-e8e8b1f79c8c540d) · [状态效果 S-80701a3ced7c043a](../../evidence/state_effects-sets-027.md#s-80701a3ced7c043a)

### path-062407

```text
(config)# do-exec test gx delete-session mac <hex-data> client-handle <number:1000..2000> <cr>
```

Handler ` RVA 0xBD21FF0 `；selector ` 1 `；EOL ` RVA 0x338C2DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Client Handle limit。

[条件 C-4e95eaa90135d7a0](../../evidence/conditions-sets-031.md#c-4e95eaa90135d7a0) · [缺口 G-d7342cf05b2af0e8](../../evidence/gaps-sets-007.md#g-d7342cf05b2af0e8) · [参数 P-ed60420a6e6296ec](../../evidence/parameters-sets-018.md#p-ed60420a6e6296ec) · [状态效果 S-ebc61837968dc2c2](../../evidence/state_effects-sets-050.md#s-ebc61837968dc2c2)

### path-031952

```text
(config)# do-exec test gx enable <cr>
```

Handler ` RVA 0xBD20610 `；selector ` 0 `；EOL ` RVA 0x338C2268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4e3cbe498bf9eaa](../../evidence/conditions-sets-076.md#c-c4e3cbe498bf9eaa) · [状态效果 S-cae3226cafad3a00](../../evidence/state_effects-sets-043.md#s-cae3226cafad3a00)

### path-058504

```text
(config)# do-exec test gx rar-sb session-id <number:1..4294967295> install-service <string> <cr>
```

Handler ` RVA 0xBD23560 `；selector ` 1 `；EOL ` RVA 0x338C4328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session id；` string ` Service name。

[条件 C-8294c28eb72c34ec](../../evidence/conditions-sets-051.md#c-8294c28eb72c34ec) · [参数 P-b0c10cbbfe902699](../../evidence/parameters-sets-013.md#p-b0c10cbbfe902699) · [状态效果 S-5601a7ad157d50ab](../../evidence/state_effects-sets-019.md#s-5601a7ad157d50ab)

### path-062648

```text
(config)# do-exec test gx update-session id ip <address> data <interface> client-handle <number:1000..2000> <cr>
```

Handler ` RVA 0xBD22230 `；selector ` 1 `；EOL ` RVA 0x338C3688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the subscriber；` unsigned_number ` Client Handle limit。

[条件 C-58a206b3afe402c9](../../evidence/conditions-sets-035.md#c-58a206b3afe402c9) · [缺口 G-5bea4dc6e83c4cc9](../../evidence/gaps-sets-004.md#g-5bea4dc6e83c4cc9) · [参数 P-8e34add9c2a6d6d5](../../evidence/parameters-sets-011.md#p-8e34add9c2a6d6d5) · [状态效果 S-c49968b698acd89f](../../evidence/state_effects-sets-042.md#s-c49968b698acd89f)

### path-052773

```text
(config)# do-exec test hsrp ha sync mac enable <cr>
```

Handler ` RVA 0xD321940 `；selector ` 50 `；EOL ` RVA 0x33E15B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-aa3ce5b29a35c98f](../../evidence/state_effects-sets-036.md#s-aa3ce5b29a35c98f)

### path-062478

```text
(config)# do-exec test hw-module subslot <?slotcard_func_action@5555899c11b0> all async loopback enable <cr>
```

Handler ` RVA 0x15B6D850 `；selector ` 0 `；EOL ` RVA 0x35DEF4D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3fe5a621de566e35](../../evidence/conditions-sets-025.md#c-3fe5a621de566e35) · [缺口 G-bee7e332974cad0b](../../evidence/gaps-sets-007.md#g-bee7e332974cad0b) · [状态效果 S-b42d885d3c160368](../../evidence/state_effects-sets-038.md#s-b42d885d3c160368)

### path-062483

```text
(config)# do-exec test hw-module subslot <?slotcard_func_action@5555899c11b0> all cwan message gsm-profile-get <cr>
```

Handler ` RVA 0x15B0B5D0 `；selector ` 0 `；EOL ` RVA 0x35DE9C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e7b8be28ed4a117](../../evidence/conditions-sets-043.md#c-6e7b8be28ed4a117) · [缺口 G-bee7e332974cad0b](../../evidence/gaps-sets-007.md#g-bee7e332974cad0b) · [状态效果 S-173a8a2e47740bc8](../../evidence/state_effects-sets-005.md#s-173a8a2e47740bc8)

### path-031108

```text
(config)# do-exec test idmgr init <cr>
```

Handler ` RVA 0xE1926E0 `；selector ` 0 `；EOL ` RVA 0x3422BCB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-1679a0e06a5a5178](../../evidence/state_effects-sets-005.md#s-1679a0e06a5a5178)

### path-058028

```text
(config)# do-exec test idmgr req-type session-assert key-list <string> data-list <cr>
```

Handler ` RVA 0xE1926E0 `；selector ` 0 `；EOL ` RVA 0x3422C0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of Attribute list。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-04fef1596abad51d](../../evidence/parameters-sets-001.md#p-04fef1596abad51d) · [状态效果 S-9087e71e17ea21db](../../evidence/state_effects-sets-031.md#s-9087e71e17ea21db)

### path-054621

```text
(config)# do-exec test ifs appn read <address> <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 1 `；EOL ` RVA 0x33EC2460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` string ` Filename only。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-727d586e085e9dc5](../../evidence/parameters-sets-009.md#p-727d586e085e9dc5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-054635

```text
(config)# do-exec test ifs appn write <address> <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 2 `；EOL ` RVA 0x33EC2760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` string ` Filename only。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9696f29e228907e8](../../evidence/parameters-sets-012.md#p-9696f29e228907e8) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038889

```text
(config)# do-exec test ifs boot <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 3 `；EOL ` RVA 0x33EC2A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Remainder of the bootstrap 'boot' command。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f0def853533d3d07](../../evidence/parameters-sets-018.md#p-f0def853533d3d07) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031469

```text
(config)# do-exec test ifs defaults <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 4 `；EOL ` RVA 0x33EC2CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048160

```text
(config)# do-exec test ifs disk cluster <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 8 `；EOL ` RVA 0x33EC39F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-efdb0d55b0727b4f](../../evidence/parameters-sets-018.md#p-efdb0d55b0727b4f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048203

```text
(config)# do-exec test ifs disk modes <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 9 `；EOL ` RVA 0x33EC3CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9c06b36a6a837b34](../../evidence/parameters-sets-012.md#p-9c06b36a6a837b34) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-048115

```text
(config)# do-exec test ifs disk rdwr <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 7 `；EOL ` RVA 0x33EC3710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c0576a6ad695a918](../../evidence/parameters-sets-015.md#p-c0576a6ad695a918) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039044

```text
(config)# do-exec test ifs show hidden <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 5 `；EOL ` RVA 0x33EC33D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039214

```text
(config)# do-exec test ifs slot <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 6 `；EOL ` RVA 0x33EC3018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for slot core destination。

[条件 C-66124d6ff35a19b2](../../evidence/conditions-sets-039.md#c-66124d6ff35a19b2) · [参数 P-dd661fa056efeb7f](../../evidence/parameters-sets-017.md#p-dd661fa056efeb7f) · [状态效果 S-c54da6177e8a74bc](../../evidence/state_effects-sets-042.md#s-c54da6177e8a74bc)

### path-062850

```text
(config)# do-exec test install <string> <url:dynamic> <?url_prefix_action@55558b337468> <cr>
```

Handler ` RVA 0x15A6C9C0 `；selector ` 0 `；EOL ` RVA 0x35DE34E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-77382f49aec84a88](../../evidence/conditions-sets-046.md#c-77382f49aec84a88) · [缺口 G-8a52c413254bff3b](../../evidence/gaps-sets-005.md#g-8a52c413254bff3b) · [参数 P-da0a1e05cda2a7ed](../../evidence/parameters-sets-016.md#p-da0a1e05cda2a7ed) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026625

```text
(config)# do-exec test interfaces <cr>
```

Handler ` RVA 0xE8F4F60 `；selector ` 0 `；EOL ` RVA 0x3433F348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18472d7888f7c1a4](../../evidence/conditions-sets-009.md#c-18472d7888f7c1a4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060545

```text
(config)# do-exec test interfaces <interface> <cr>
```

Handler ` RVA 0xE8F4F60 `；selector ` 0 `；EOL ` RVA 0x3433F348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f325fd0c394a81d7](../../evidence/conditions-sets-094.md#c-f325fd0c394a81d7) · [缺口 G-57b7b4a38f996144](../../evidence/gaps-sets-004.md#g-57b7b4a38f996144) · [参数 P-cd39dfba9be5979d](../../evidence/parameters-sets-016.md#p-cd39dfba9be5979d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057112

```text
(config)# do-exec test ip access-list dynamic delete <number:100..199> <number:1..262144> <cr>
```

Handler ` RVA 0xCF06CB0 `；selector ` 0 `；EOL ` RVA 0x33D565B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Extended ACL；` unsigned_number ` handle。

[条件 C-aad388a616fbeb7d](../../evidence/conditions-sets-066.md#c-aad388a616fbeb7d) · [参数 P-891680d3d0bbb4cb](../../evidence/parameters-sets-011.md#p-891680d3d0bbb4cb) · [状态效果 S-2e279efc2661f0b3](../../evidence/state_effects-sets-010.md#s-2e279efc2661f0b3)

### path-052749

```text
(config)# do-exec test ip access-list dynamic empty <number:100..199> <cr>
```

Handler ` RVA 0xCF073F0 `；selector ` 0 `；EOL ` RVA 0x33D560A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Extended ACL。

[条件 C-aad388a616fbeb7d](../../evidence/conditions-sets-066.md#c-aad388a616fbeb7d) · [参数 P-3210d07544b61f37](../../evidence/parameters-sets-004.md#p-3210d07544b61f37) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062599

```text
(config)# do-exec test ip access-list dynamic match <number:100..199> <number:1..5> <number:100..199> <interface> <cr>
```

Handler ` RVA 0xCF06CB0 `；selector ` 0 `；EOL ` RVA 0x33D565B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Extended ACL；` unsigned_number ` Match Priority；` unsigned_number ` Match Criteria (please specify ACL containing match criteria)。

[条件 C-adf0283e2a67bf1b](../../evidence/conditions-sets-067.md#c-adf0283e2a67bf1b) · [缺口 G-1c93b1808c1b66e1](../../evidence/gaps-sets-001.md#g-1c93b1808c1b66e1) · [参数 P-f53fd6090ea42396](../../evidence/parameters-sets-018.md#p-f53fd6090ea42396) · [状态效果 S-01e2698eb61f2f11](../../evidence/state_effects-sets-001.md#s-01e2698eb61f2f11)

### path-035357

```text
(config)# do-exec test ip access-list register <cr>
```

Handler ` RVA 0xCF065A0 `；selector ` 0 `；EOL ` RVA 0x33D56DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f75acb2a779d8db1](../../evidence/conditions-sets-096.md#c-f75acb2a779d8db1) · [状态效果 S-36ec62d6513f0572](../../evidence/state_effects-sets-012.md#s-36ec62d6513f0572)

### path-062661

```text
(config)# do-exec test ip dhcp api pool <string> <string> add network <address> <?ipmask_action@55558932b668> <cr>
```

Handler ` RVA 0xD2C3400 `；selector ` 0 `；EOL ` RVA 0x33DD7270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Pool name；` string ` Pool owner name；` address ` Network number in dotted-decimal notation。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [缺口 G-0271de62f0a20fa7](../../evidence/gaps-sets-001.md#g-0271de62f0a20fa7) · [参数 P-94e7efeb15f0ae38](../../evidence/parameters-sets-011.md#p-94e7efeb15f0ae38) · [状态效果 S-975fc8256309802c](../../evidence/state_effects-sets-032.md#s-975fc8256309802c)

### path-059126

```text
(config)# do-exec test ip dhcp api pool <string> <string> create <cr>
```

Handler ` RVA 0xD2C3400 `；selector ` 0 `；EOL ` RVA 0x33DD7270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name；` string ` Pool owner name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-07dc240d29126b32](../../evidence/parameters-sets-001.md#p-07dc240d29126b32) · [状态效果 S-462922bbc9c6f405](../../evidence/state_effects-sets-015.md#s-462922bbc9c6f405)

### path-045739

```text
(config)# do-exec test ip dhcp query <address> <cr>
```

Handler ` RVA 0xD250100 `；selector ` 0 `；EOL ` RVA 0x33DD6E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Client IP address。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-e83f674c88cc9462](../../evidence/parameters-sets-017.md#p-e83f674c88cc9462) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045610

```text
(config)# do-exec test ip dhcp terminate <address> <cr>
```

Handler ` RVA 0xD250060 `；selector ` 0 `；EOL ` RVA 0x33DD6AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Client IP address。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3b4645e85fd16383](../../evidence/parameters-sets-005.md#p-3b4645e85fd16383) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053069

```text
(config)# do-exec test ip domain apis <address> <string> <cr>
```

Handler ` RVA 0xD139D60 `；selector ` 0 `；EOL ` RVA 0x33D96B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Host IP address；` string ` VRF name。

[条件 C-f4c93b68702085dd](../../evidence/conditions-sets-094.md#c-f4c93b68702085dd) · [参数 P-787fba5cde6b4234](../../evidence/parameters-sets-009.md#p-787fba5cde6b4234) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035744

```text
(config)# do-exec test ip domain default-domain <cr>
```

Handler ` RVA 0xD139380 `；selector ` 0 `；EOL ` RVA 0x33D95E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8a6173b822f2a2c](../../evidence/conditions-sets-083.md#c-d8a6173b822f2a2c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045449

```text
(config)# do-exec test ip domain get-ipv4-server <number:0..25> <cr>
```

Handler ` RVA 0xD139580 `；selector ` 0 `；EOL ` RVA 0x33D967E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Server index。

[条件 C-0e897ddcacc96c4e](../../evidence/conditions-sets-006.md#c-0e897ddcacc96c4e) · [参数 P-64d2f2e2a2204061](../../evidence/parameters-sets-008.md#p-64d2f2e2a2204061) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045395

```text
(config)# do-exec test ip domain get-server <number:0..25> <cr>
```

Handler ` RVA 0xD139440 `；selector ` 0 `；EOL ` RVA 0x33D964F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Server index。

[条件 C-915c9c26d21d1955](../../evidence/conditions-sets-056.md#c-915c9c26d21d1955) · [参数 P-a508c7655a359164](../../evidence/parameters-sets-013.md#p-a508c7655a359164) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045832

```text
(config)# do-exec test ip domain lookup <address> <cr>
```

Handler ` RVA 0xD137930 `；selector ` 0 `；EOL ` RVA 0x33D972D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address。

[条件 C-0b99e5c2da2dd36e](../../evidence/conditions-sets-005.md#c-0b99e5c2da2dd36e) · [参数 P-b70e952a38201f2e](../../evidence/parameters-sets-014.md#p-b70e952a38201f2e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045694

```text
(config)# do-exec test ip domain mcast-lookup <address> <cr>
```

Handler ` RVA 0xD140A70 `；selector ` 0 `；EOL ` RVA 0x33D976F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address。

[条件 C-be304ce819f20fed](../../evidence/conditions-sets-073.md#c-be304ce819f20fed) · [参数 P-c09f62870a65c5cd](../../evidence/parameters-sets-015.md#p-c09f62870a65c5cd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057182

```text
(config)# do-exec test ip domain name-delete <string> <number:1..255> <number:1..4194304> <cr>
```

Handler ` RVA 0xD139670 `；selector ` 0 `；EOL ` RVA 0x33D96200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname；` unsigned_number ` Namekind；` unsigned_number ` Type。

[条件 C-4b21fbaa6292d072](../../evidence/conditions-sets-029.md#c-4b21fbaa6292d072) · [参数 P-e34808f4aca9e093](../../evidence/parameters-sets-017.md#p-e34808f4aca9e093) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045183

```text
(config)# do-exec test ip multicast sync resume <cr>
```

Handler ` RVA 0xD470550 `；selector ` 1 `；EOL ` RVA 0x33E51598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045128

```text
(config)# do-exec test ip multicast sync suspend <cr>
```

Handler ` RVA 0xD470550 `；selector ` 0 `；EOL ` RVA 0x33E512F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045494

```text
(config)# do-exec test ip nat clear translations <cr>
```

Handler ` RVA 0xFA39690 `；selector ` 0 `；EOL ` RVA 0x347DE818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036309

```text
(config)# do-exec test ip nat dump <cr>
```

Handler ` RVA 0xFA39B10 `；selector ` 0 `；EOL ` RVA 0x347DF4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-6af480e7ad8ce086](../../evidence/state_effects-sets-023.md#s-6af480e7ad8ce086)

### path-045674

```text
(config)# do-exec test ip nat portmap trans_report <cr>
```

Handler ` RVA 0xFA39700 `；selector ` 0 `；EOL ` RVA 0x347DEDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-229e102c98d3cb95](../../evidence/state_effects-sets-008.md#s-229e102c98d3cb95)

### path-053119

```text
(config)# do-exec test ip nat show pool <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 0 `；EOL ` RVA 0x347DDF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-b1309a7e1ed805ca](../../evidence/conditions-sets-069.md#c-b1309a7e1ed805ca) · [参数 P-2fc9437051580fb2](../../evidence/parameters-sets-004.md#p-2fc9437051580fb2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053028

```text
(config)# do-exec test ip nat show pool all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 1 `；EOL ` RVA 0x347DDC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053159

```text
(config)# do-exec test ip nat show rule <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 2 `；EOL ` RVA 0x347DE508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Rule name。

[条件 C-a188749f3840f2b8](../../evidence/conditions-sets-062.md#c-a188749f3840f2b8) · [参数 P-83418bd3b9811e31](../../evidence/parameters-sets-010.md#p-83418bd3b9811e31) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053070

```text
(config)# do-exec test ip nat show rule all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 3 `；EOL ` RVA 0x347DE208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035940

```text
(config)# do-exec test ip nat-route database <cr>
```

Handler ` RVA 0x13725FC0 `；selector ` 0 `；EOL ` RVA 0x35C0F330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-99b583311488a6a0](../../evidence/state_effects-sets-033.md#s-99b583311488a6a0)

### path-061902

```text
(config)# do-exec test ip nat-route route inside <prefix:dynamic> <cr>
```

Handler ` RVA 0x13725FC0 `；selector ` 0 `；EOL ` RVA 0x35C0F330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix/length。

[条件 C-b1b3638b8de9894e](../../evidence/conditions-sets-069.md#c-b1b3638b8de9894e) · [缺口 G-e0456d69ac3273ad](../../evidence/gaps-sets-008.md#g-e0456d69ac3273ad) · [参数 P-94a97b8ad2cfbd7e](../../evidence/parameters-sets-011.md#p-94a97b8ad2cfbd7e) · [状态效果 S-b5d85f81c4a153f4](../../evidence/state_effects-sets-038.md#s-b5d85f81c4a153f4)

### path-045512

```text
(config)# do-exec test ip nbar batch-config end <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 5 `；EOL ` RVA 0x35259330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045451

```text
(config)# do-exec test ip nbar batch-config start <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 4 `；EOL ` RVA 0x35259088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045566

```text
(config)# do-exec test ip nbar byte-count-window disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 9 `；EOL ` RVA 0x352596A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-11512a74cf4fa438](../../evidence/state_effects-sets-004.md#s-11512a74cf4fa438)

### path-045196

```text
(config)# do-exec test ip nbar caches clear <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 29 `；EOL ` RVA 0x35255258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052839

```text
(config)# do-exec test ip nbar caches export <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 28 `；EOL ` RVA 0x35254FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-3b46f8fae4be42bd](../../evidence/parameters-sets-005.md#p-3b46f8fae4be42bd) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052807

```text
(config)# do-exec test ip nbar caches import <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 27 `；EOL ` RVA 0x35254CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-693dea4536eeb117](../../evidence/parameters-sets-008.md#p-693dea4536eeb117) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045246

```text
(config)# do-exec test ip nbar caches show <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 30 `；EOL ` RVA 0x35255500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045615

```text
(config)# do-exec test ip nbar cedge-simulation disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 11 `；EOL ` RVA 0x35259C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045553

```text
(config)# do-exec test ip nbar cedge-simulation enable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 10 `；EOL ` RVA 0x352599D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045224

```text
(config)# do-exec test ip nbar config-mode async <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 8 `；EOL ` RVA 0x35257498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045296

```text
(config)# do-exec test ip nbar config-mode sync <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 7 `；EOL ` RVA 0x35257740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-057357

```text
(config)# do-exec test ip nbar dataplane-info-monitor memory-thresholds low <number:1..100> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 14 `；EOL ` RVA 0x3525A618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Low threshold in percents。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-2360135968ca2bc4](../../evidence/parameters-sets-003.md#p-2360135968ca2bc4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053198

```text
(config)# do-exec test ip nbar dataplane-info-monitor traffic-over-subscription-state false <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 12 `；EOL ` RVA 0x3525A290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053138

```text
(config)# do-exec test ip nbar dataplane-info-monitor traffic-over-subscription-state true <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 13 `；EOL ` RVA 0x35259FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062490

```text
(config)# do-exec test ip nbar field-extraction disable <string> <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 1 `；EOL ` RVA 0x35258520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name；` string ` Field Name。

[条件 C-0036563246745203](../../evidence/conditions-sets-001.md#c-0036563246745203) · [缺口 G-cd951a775f374281](../../evidence/gaps-sets-007.md#g-cd951a775f374281) · [参数 P-94dc6b02cb1e9c89](../../evidence/parameters-sets-011.md#p-94dc6b02cb1e9c89) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062489

```text
(config)# do-exec test ip nbar field-extraction enable <string> <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 0 `；EOL ` RVA 0x35258120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name；` string ` Field Name。

[条件 C-99523156422bc16d](../../evidence/conditions-sets-059.md#c-99523156422bc16d) · [缺口 G-633b3ee2b75a9955](../../evidence/gaps-sets-004.md#g-633b3ee2b75a9955) · [参数 P-15e5eefa6e6d1241](../../evidence/parameters-sets-002.md#p-15e5eefa6e6d1241) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045374

```text
(config)# do-exec test ip nbar function <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 6 `；EOL ` RVA 0x35257AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Function name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-4af9a509018bb542](../../evidence/parameters-sets-006.md#p-4af9a509018bb542) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045181

```text
(config)# do-exec test ip nbar npc disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 19 `；EOL ` RVA 0x35255B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052896

```text
(config)# do-exec test ip nbar npc enable <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 18 `；EOL ` RVA 0x352558E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b8c3dd324e3e92e2](../../evidence/parameters-sets-014.md#p-b8c3dd324e3e92e2) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052938

```text
(config)# do-exec test ip nbar npc pack-mode allow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 21 `；EOL ` RVA 0x35256120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052973

```text
(config)# do-exec test ip nbar npc pack-mode disallow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 22 `；EOL ` RVA 0x352563C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045239

```text
(config)# do-exec test ip nbar npc save <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 20 `；EOL ` RVA 0x35255E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062275

```text
(config)# do-exec test ip nbar per-txn disable <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 3 `；EOL ` RVA 0x35258D48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name。

[条件 C-b66c2a89d6cf01be](../../evidence/conditions-sets-071.md#c-b66c2a89d6cf01be) · [缺口 G-8877933b2961233b](../../evidence/gaps-sets-005.md#g-8877933b2961233b) · [参数 P-fc8a54166f8fe8f7](../../evidence/parameters-sets-019.md#p-fc8a54166f8fe8f7) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062272

```text
(config)# do-exec test ip nbar per-txn enable <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 2 `；EOL ` RVA 0x35258988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name。

[条件 C-18765f6c06704713](../../evidence/conditions-sets-010.md#c-18765f6c06704713) · [缺口 G-bd7ba8dcf14b9128](../../evidence/gaps-sets-007.md#g-bd7ba8dcf14b9128) · [参数 P-0f9162a8201fad4e](../../evidence/parameters-sets-002.md#p-0f9162a8201fad4e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062296

```text
(config)# do-exec test ip nbar resources flow max-session <number:dynamic> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 7 `；EOL ` RVA 0x3525B6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of Session 。

[条件 C-e6c979d555a10765](../../evidence/conditions-sets-089.md#c-e6c979d555a10765) · [缺口 G-ff61c9cb02187930](../../evidence/gaps-sets-009.md#g-ff61c9cb02187930) · [参数 P-0371b5c114cf1601](../../evidence/parameters-sets-001.md#p-0371b5c114cf1601) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062302

```text
(config)# do-exec test ip nbar resources protocol <number:1..100000000> <?option@55558a7af308> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 1 `；EOL ` RVA 0x3525B3E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Link age greater than system link age (secs.)。

[条件 C-83f3c9fd7d20863c](../../evidence/conditions-sets-051.md#c-83f3c9fd7d20863c) · [缺口 G-00e7d5557b85ef27](../../evidence/gaps-sets-001.md#g-00e7d5557b85ef27) · [参数 P-69e4dd58e3555f6a](../../evidence/parameters-sets-008.md#p-69e4dd58e3555f6a) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045663

```text
(config)# do-exec test ip nbar set-max-protocol-id-no-cloud_ext <number:0..32767> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 15 `；EOL ` RVA 0x3525A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max protocol id without cloud extension。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-507a9096f4509329](../../evidence/parameters-sets-007.md#p-507a9096f4509329) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053232

```text
(config)# do-exec test ip nbar set-protocol-feature-support <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 16 `；EOL ` RVA 0x3525AC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Feature id；` unsigned_number ` Feature value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-bdb8d401bdc33739](../../evidence/parameters-sets-014.md#p-bdb8d401bdc33739) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036435

```text
(config)# do-exec test ip nbar show-features-activation <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 17 `；EOL ` RVA 0x3525AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-036377

```text
(config)# do-exec test ip nbar show-fib-ad-info <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 31 `；EOL ` RVA 0x3525BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045229

```text
(config)# do-exec test ip nbar track-ip disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 24 `；EOL ` RVA 0x35256C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060230

```text
(config)# do-exec test ip nbar track-ip enable <string> port <number:0..4294967295> vrf-id <number:0..4294967295> l4-proto <number:0..255> memory-size <number:0..20000> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 23 `；EOL ` RVA 0x35256978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPv4/v6 to track；` unsigned_number ` port number；` unsigned_number ` VRF id；` unsigned_number ` L4 Protocol；` unsigned_number ` memory size in KB。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-74d155980cc4da67](../../evidence/parameters-sets-009.md#p-74d155980cc4da67) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045302

```text
(config)# do-exec test ip nbar track-ip flush <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 25 `；EOL ` RVA 0x35256ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045364

```text
(config)# do-exec test ip nbar track-ip status <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 26 `；EOL ` RVA 0x35257180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-035985

```text
(config)# do-exec test ip omp flush <cr>
```

Handler ` RVA 0x137422E0 `；selector ` 0 `；EOL ` RVA 0x35C105C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5d31c3f438ffd21](../../evidence/conditions-sets-082.md#c-d5d31c3f438ffd21) · [状态效果 S-c98a39177fb201b4](../../evidence/state_effects-sets-043.md#s-c98a39177fb201b4)

### path-061303

```text
(config)# do-exec test ip omp route <prefix:dynamic> <cr>
```

Handler ` RVA 0x137422E0 `；selector ` 0 `；EOL ` RVA 0x35C105C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix/length。

[条件 C-3be5a014bdce5d4c](../../evidence/conditions-sets-023.md#c-3be5a014bdce5d4c) · [缺口 G-41ea3828704bfd7b](../../evidence/gaps-sets-003.md#g-41ea3828704bfd7b) · [参数 P-817351ede9d4fa46](../../evidence/parameters-sets-010.md#p-817351ede9d4fa46) · [状态效果 S-63dcfbcbeb684c63](../../evidence/state_effects-sets-021.md#s-63dcfbcbeb684c63)

### path-061283

```text
(config)# do-exec test ip pbr enqueue <interface> <cr>
```

Handler ` RVA 0x10C6F3F0 `；selector ` 0 `；EOL ` RVA 0x34CF0960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3ad2b7c717294d96](../../evidence/conditions-sets-023.md#c-3ad2b7c717294d96) · [缺口 G-c4fb390967749761](../../evidence/gaps-sets-007.md#g-c4fb390967749761) · [参数 P-a2ddcf5466c5f96e](../../evidence/parameters-sets-012.md#p-a2ddcf5466c5f96e) · [状态效果 S-7aed08c5ba9e99d1](../../evidence/state_effects-sets-026.md#s-7aed08c5ba9e99d1)

### path-045009

```text
(config)# do-exec test ip pbr ipv6 attach <cr>
```

Handler ` RVA 0x10C6E4E0 `；selector ` 0 `；EOL ` RVA 0x34CF0520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4292a4821897d1f5](../../evidence/conditions-sets-026.md#c-4292a4821897d1f5) · [状态效果 S-06d623eb89970e20](../../evidence/state_effects-sets-002.md#s-06d623eb89970e20)

### path-044968

```text
(config)# do-exec test ip pbr map <string> <cr>
```

Handler ` RVA 0x10C6E570 `；selector ` 0 `；EOL ` RVA 0x34CF0228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` PBR route-map name。

[条件 C-4292a4821897d1f5](../../evidence/conditions-sets-026.md#c-4292a4821897d1f5) · [参数 P-e93b53fee09f3a16](../../evidence/parameters-sets-017.md#p-e93b53fee09f3a16) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062269

```text
(config)# do-exec test ip rib api iprib_get_route <?ipaddrmask_action@55558978f690> exact_match <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 1 `；EOL ` RVA 0x3423B738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [缺口 G-083a1b0fc41c3b4e](../../evidence/gaps-sets-001.md#g-083a1b0fc41c3b4e) · [状态效果 S-4274862c8d754457](../../evidence/state_effects-sets-015.md#s-4274862c8d754457)

### path-045362

```text
(config)# do-exec test ip rib api iprib_geteachroute <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 2 `；EOL ` RVA 0x3423BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f2692d7316ca346d](../../evidence/state_effects-sets-051.md#s-f2692d7316ca346d)

### path-061889

```text
(config)# do-exec test ip rib api iprib_rtlookup <?ipaddrmask_action@55558978fa30> <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 0 `；EOL ` RVA 0x3423BA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [缺口 G-278486a76bcce1e7](../../evidence/gaps-sets-002.md#g-278486a76bcce1e7) · [状态效果 S-f2692d7316ca346d](../../evidence/state_effects-sets-051.md#s-f2692d7316ca346d)

### path-029815

```text
(config)# do-exec test ip rmap <cr>
```

Handler ` RVA 0xE207640 `；selector ` 0 `；EOL ` RVA 0x3423B1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e13b9363d2692b4](../../evidence/conditions-sets-061.md#c-9e13b9363d2692b4) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061892

```text
(config)# do-exec test ip rmap associate <string> <interface> <cr>
```

Handler ` RVA 0xE2025D0 `；selector ` 0 `；EOL ` RVA 0x3423ADC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-94e73e05fe0ecf46](../../evidence/conditions-sets-058.md#c-94e73e05fe0ecf46) · [缺口 G-e3bd8b7ccca6db15](../../evidence/gaps-sets-008.md#g-e3bd8b7ccca6db15) · [参数 P-0952a71dc783579b](../../evidence/parameters-sets-001.md#p-0952a71dc783579b) · [状态效果 S-c206bf896e090b48](../../evidence/state_effects-sets-041.md#s-c206bf896e090b48)

### path-053128

```text
(config)# do-exec test ip rmap associate <string> local <cr>
```

Handler ` RVA 0xE2025D0 `；selector ` 0 `；EOL ` RVA 0x3423ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-0d322722fb87f580](../../evidence/conditions-sets-005.md#c-0d322722fb87f580) · [参数 P-bd73181f983ba232](../../evidence/parameters-sets-014.md#p-bd73181f983ba232) · [状态效果 S-e47a29face672e20](../../evidence/state_effects-sets-048.md#s-e47a29face672e20)

### path-052809

```text
(config)# do-exec test ip rmap batch-commit <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE208090 `；selector ` 0 `；EOL ` RVA 0x34234C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify rmapHandle；` unsigned_number ` Application: 1 - AAA。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ab77153375655df9](../../evidence/parameters-sets-013.md#p-ab77153375655df9) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052898

```text
(config)# do-exec test ip rmap create <number:0..2147483647> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x34234FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0a14d68c1ec1aa26](../../evidence/parameters-sets-001.md#p-0a14d68c1ec1aa26) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053062

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3423A5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-23491533d0d4bfd8](../../evidence/conditions-sets-014.md#c-23491533d0d4bfd8) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059738

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0xE203110 `；selector ` 0 `；EOL ` RVA 0x342357B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-272ac774548295cd](../../evidence/parameters-sets-003.md#p-272ac774548295cd) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-060013

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> match destination tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 2 `；EOL ` RVA 0x34236208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` dgt id value。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-6d91a93fa721550c](../../evidence/parameters-sets-009.md#p-6d91a93fa721550c) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-060008

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x34235B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-937ae3c156e0cb63](../../evidence/parameters-sets-011.md#p-937ae3c156e0cb63) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-060011

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> match source tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 1 `；EOL ` RVA 0x34235EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Security id value。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-4ef7f2833cf942dd](../../evidence/parameters-sets-007.md#p-4ef7f2833cf942dd) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059744

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> match vrf <string> <cr>
```

Handler ` RVA 0xE2033E0 `；selector ` 0 `；EOL ` RVA 0x342364E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-7568d67122bab58a](../../evidence/parameters-sets-009.md#p-7568d67122bab58a) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059799

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set color red <cr>
```

Handler ` RVA 0xE203F30 `；selector ` 0 `；EOL ` RVA 0x3423A160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-da4144df48a5bbb3](../../evidence/conditions-sets-084.md#c-da4144df48a5bbb3) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-f5d631e4fe75391c](../../evidence/state_effects-sets-052.md#s-f5d631e4fe75391c)

### path-059754

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-global-nh <address> <cr>
```

Handler ` RVA 0xE205C50 `；selector ` 0 `；EOL ` RVA 0x34237A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-ea7c91e852d793a4](../../evidence/parameters-sets-018.md#p-ea7c91e852d793a4) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059762

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-next-hop <address> <cr>
```

Handler ` RVA 0xE2059B0 `；selector ` 0 `；EOL ` RVA 0x34238050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of default next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-b3295dd415de6554](../../evidence/parameters-sets-014.md#p-b3295dd415de6554) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059166

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-nh-verify <cr>
```

Handler ` RVA 0xE205720 `；selector ` 0 `；EOL ` RVA 0x342382D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-060027

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set def-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE205EF0 `；selector ` 0 `；EOL ` RVA 0x34237D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-6835e23ae0bf3d34](../../evidence/parameters-sets-008.md#p-6835e23ae0bf3d34) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-062608

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set default-interface <interface> <cr>
```

Handler ` RVA 0xE203C80 `；selector ` 0 `；EOL ` RVA 0x34239E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-acefd9f4803ab01b](../../evidence/conditions-sets-067.md#c-acefd9f4803ab01b) · [缺口 G-62d51b42f17297a5](../../evidence/gaps-sets-004.md#g-62d51b42f17297a5) · [参数 P-95d6304157d6adf5](../../evidence/parameters-sets-012.md#p-95d6304157d6adf5) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059781

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set df <number:0..65535> <cr>
```

Handler ` RVA 0xE204F40 `；selector ` 0 `；EOL ` RVA 0x34238BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of df。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-06c275ebd6daa0a6](../../evidence/parameters-sets-001.md#p-06c275ebd6daa0a6) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059740

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set gateway <address> <cr>
```

Handler ` RVA 0xE206C40 `；selector ` 0 `；EOL ` RVA 0x34236890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of gateway。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-e729039b021e96f0](../../evidence/parameters-sets-017.md#p-e729039b021e96f0) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059201

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x34239130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-060010

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set gw-vrf <string> <address> <cr>
```

Handler ` RVA 0xE206EE0 `；selector ` 0 `；EOL ` RVA 0x34236BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of gateway。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-2acbe67311ea0ecd](../../evidence/parameters-sets-004.md#p-2acbe67311ea0ecd) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-062609

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set interface <interface> <cr>
```

Handler ` RVA 0xE2041D0 `；selector ` 0 `；EOL ` RVA 0x342399F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-328d69976cc2ea6a](../../evidence/conditions-sets-020.md#c-328d69976cc2ea6a) · [缺口 G-9ce68728a18b5716](../../evidence/gaps-sets-006.md#g-9ce68728a18b5716) · [参数 P-f8dc5504182ee306](../../evidence/parameters-sets-019.md#p-f8dc5504182ee306) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059748

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set ip-global-nh <address> <cr>
```

Handler ` RVA 0xE2066E0 `；selector ` 0 `；EOL ` RVA 0x34237430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-b63ee37da7e7cdd4](../../evidence/parameters-sets-014.md#p-b63ee37da7e7cdd4) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-060019

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set ip-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE206980 `；selector ` 0 `；EOL ` RVA 0x34237758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-ceeec3d0d198abf4](../../evidence/parameters-sets-016.md#p-ceeec3d0d198abf4) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059742

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0xE206440 `；selector ` 0 `；EOL ` RVA 0x34236EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-ac5b408e00df8dee](../../evidence/parameters-sets-013.md#p-ac5b408e00df8dee) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059119

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set nh-verify <cr>
```

Handler ` RVA 0xE2061B0 `；selector ` 0 `；EOL ` RVA 0x34237120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-062939

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set oce <?general_pointer_number_action@55558978d3d8> next-hop <address> interface <interface> <cr>
```

Handler ` RVA 0xE204720 `；selector ` 0 `；EOL ` RVA 0x342395D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-d90407b62377e85f](../../evidence/conditions-sets-084.md#c-d90407b62377e85f) · [缺口 G-7d0679fc03f2c95a](../../evidence/gaps-sets-005.md#g-7d0679fc03f2c95a) · [参数 P-05ea5f58abea45dc](../../evidence/parameters-sets-001.md#p-05ea5f58abea45dc) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059775

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set precedence <number:0..65535> <cr>
```

Handler ` RVA 0xE2051E0 `；selector ` 0 `；EOL ` RVA 0x342388D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-c55c967820bd003f](../../evidence/parameters-sets-015.md#p-c55c967820bd003f) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059769

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set tos <number:0..65535> <cr>
```

Handler ` RVA 0xE205480 `；selector ` 0 `；EOL ` RVA 0x342385E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of tos。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-4dce7f6ad2f960e0](../../evidence/parameters-sets-006.md#p-4dce7f6ad2f960e0) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-059785

```text
(config)# do-exec test ip rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x34238EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-a9998f50032d241f](../../evidence/conditions-sets-065.md#c-a9998f50032d241f) · [参数 P-e80fe2c3ff0d0f92](../../evidence/parameters-sets-017.md#p-e80fe2c3ff0d0f92) · [状态效果 S-23ea49ee5b98cb45](../../evidence/state_effects-sets-008.md#s-23ea49ee5b98cb45)

### path-053021

```text
(config)# do-exec test ip rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3423A900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag。

[条件 C-8c36b7a250ffc64c](../../evidence/conditions-sets-054.md#c-8c36b7a250ffc64c) · [参数 P-55050655b3d5bb05](../../evidence/parameters-sets-007.md#p-55050655b3d5bb05) · [状态效果 S-cc3336b641bf97ce](../../evidence/state_effects-sets-043.md#s-cc3336b641bf97ce)

### path-045005

```text
(config)# do-exec test ip rmap register <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x34234888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7f8a93636669cf1c](../../evidence/parameters-sets-010.md#p-7f8a93636669cf1c) · [状态效果 S-17b88bc853c6164d](../../evidence/state_effects-sets-005.md#s-17b88bc853c6164d)

### path-052869

```text
(config)# do-exec test ip rmap remove <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x342352F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c35ad9aae5dc6839](../../evidence/parameters-sets-015.md#p-c35ad9aae5dc6839) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061322

```text
(config)# do-exec test ip static-route add <?ipaddrmask_action@5555897e2690> <cr>
```

Handler ` RVA 0xE2A7490 `；selector ` 0 `；EOL ` RVA 0x3428E9F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-704f161ae9b944d1](../../evidence/conditions-sets-043.md#c-704f161ae9b944d1) · [缺口 G-bcc8f11adb1cbb06](../../evidence/gaps-sets-007.md#g-bcc8f11adb1cbb06) · [状态效果 S-36b5289189c0fda6](../../evidence/state_effects-sets-012.md#s-36b5289189c0fda6)

### path-062934

```text
(config)# do-exec test ip subscriber create-session ip <address> mac <hex-data> vrf <string> <interface> routed <cr>
```

Handler ` RVA 0x11A3A080 `；selector ` 1 `；EOL ` RVA 0x355CFF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the subscriber。

[条件 C-acb3466d10066119](../../evidence/conditions-sets-067.md#c-acb3466d10066119) · [缺口 G-fe25c5c20e8eb23b](../../evidence/gaps-sets-009.md#g-fe25c5c20e8eb23b) · [参数 P-24c03866b70f1a89](../../evidence/parameters-sets-003.md#p-24c03866b70f1a89) · [状态效果 S-33945ddbb7bd4b34](../../evidence/state_effects-sets-011.md#s-33945ddbb7bd4b34)

### path-036168

```text
(config)# do-exec test ip subscriber enable <cr>
```

Handler ` RVA 0x11A36370 `；selector ` 0 `；EOL ` RVA 0x355CF310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f34cff36dcdd4978](../../evidence/conditions-sets-094.md#c-f34cff36dcdd4978) · [状态效果 S-de7b211d7b2efbec](../../evidence/state_effects-sets-047.md#s-de7b211d7b2efbec)

### path-053286

```text
(config)# do-exec test ip subscriber interface association disable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 0 `；EOL ` RVA 0x355CF9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc3a6a867e229f9b](../../evidence/conditions-sets-085.md#c-dc3a6a867e229f9b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-053285

```text
(config)# do-exec test ip subscriber interface association enable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 1 `；EOL ` RVA 0x355CF740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b60c70310e5ef397](../../evidence/conditions-sets-070.md#c-b60c70310e5ef397) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-045166

```text
(config)# do-exec test ipam pool local alloc <cr>
```

Handler ` RVA 0xCEB79B0 `；selector ` 0 `；EOL ` RVA 0x33D1C4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9bcda9bfd9837237](../../evidence/conditions-sets-060.md#c-9bcda9bfd9837237) · [状态效果 S-7642f9d8500e2fb8](../../evidence/state_effects-sets-025.md#s-7642f9d8500e2fb8)

### path-061885

```text
(config)# do-exec test ipam pool local alloc <interface> <cr>
```

Handler ` RVA 0xCEB79B0 `；selector ` 0 `；EOL ` RVA 0x33D1C4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7df664de27211577](../../evidence/conditions-sets-049.md#c-7df664de27211577) · [缺口 G-f4da123b70c6d43d](../../evidence/gaps-sets-008.md#g-f4da123b70c6d43d) · [参数 P-375e1720f744f024](../../evidence/parameters-sets-005.md#p-375e1720f744f024) · [状态效果 S-7642f9d8500e2fb8](../../evidence/state_effects-sets-025.md#s-7642f9d8500e2fb8)

### path-047942

```text
(config)# do-exec test ipc FC <number:1..5> <number:0..50000> <cr>
```

Handler ` RVA 0xD3C63E0 `；selector ` 0 `；EOL ` RVA 0x33E33C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold type；` unsigned_number ` Value。

[条件 C-7944f21a3b55c661](../../evidence/conditions-sets-047.md#c-7944f21a3b55c661) · [参数 P-569822aca9aeb7ed](../../evidence/parameters-sets-007.md#p-569822aca9aeb7ed) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038763

```text
(config)# do-exec test ipc ack-drop <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6310 `；selector ` 0 `；EOL ` RVA 0x33E33138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-4c17065756994bdc](../../evidence/conditions-sets-030.md#c-4c17065756994bdc) · [参数 P-58b2f2cef5d5926b](../../evidence/parameters-sets-007.md#p-58b2f2cef5d5926b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-038810

```text
(config)# do-exec test ipc ack-pending <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6260 `；selector ` 0 `；EOL ` RVA 0x33E334C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-fb98a3674073ddea](../../evidence/conditions-sets-097.md#c-fb98a3674073ddea) · [参数 P-8a3569dabade40fa](../../evidence/parameters-sets-011.md#p-8a3569dabade40fa) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-039944

```text
(config)# do-exec test ipc ack-timer <number:0..50000> <cr>
```

Handler ` RVA 0xD3C65C0 `；selector ` 0 `；EOL ` RVA 0x33E3B6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [参数 P-90be1626a3d9d9fe](../../evidence/parameters-sets-011.md#p-90be1626a3d9d9fe) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031456

```text
(config)# do-exec test ipc api <cr>
```

Handler ` RVA 0xD3C1A60 `；selector ` 0 `；EOL ` RVA 0x33E33EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-031729

```text
(config)# do-exec test ipc app-send <cr>
```

Handler ` RVA 0xD3C5F70 `；selector ` 0 `；EOL ` RVA 0x33E36440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061516

```text
(config)# do-exec test ipc app-send default domain <number:1..1000000> <cr>
```

Handler ` RVA 0xD3C5F70 `；selector ` 0 `；EOL ` RVA 0x33E36440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of messages to be sent。

[条件 C-29a8558eda3a24e8](../../evidence/conditions-sets-016.md#c-29a8558eda3a24e8) · [缺口 G-175ed21dc06fc483](../../evidence/gaps-sets-001.md#g-175ed21dc06fc483) · [参数 P-d90078855ebaa9a0](../../evidence/parameters-sets-016.md#p-d90078855ebaa9a0) · [状态效果 S-eb5c6a1c76fa04e8](../../evidence/state_effects-sets-050.md#s-eb5c6a1c76fa04e8)

### path-055181

```text
(config)# do-exec test ipc bundle mode seat on <cr>
```

Handler ` RVA 0xD3C4B50 `；selector ` 0 `；EOL ` RVA 0x33E3B080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-df1477fb09c7ca45](../../evidence/state_effects-sets-047.md#s-df1477fb09c7ca45)

### path-055135

```text
(config)# do-exec test ipc bundle mode session on <cr>
```

Handler ` RVA 0xD3C4A80 `；selector ` 0 `；EOL ` RVA 0x33E3AD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae2d0968cb19fe5b](../../evidence/conditions-sets-067.md#c-ae2d0968cb19fe5b) · [状态效果 S-0ff5f15c9eca2f42](../../evidence/state_effects-sets-004.md#s-0ff5f15c9eca2f42)
