# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-021432

```text
(exec)# test cef <?dumper_command_func@555588cac488> table signal-suppression Enable <cr>
```

Handler ` RVA 0xB46DE70 `；selector ` 0 `；EOL ` RVA 0x3375DDB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b9a0a0fbf7956899](../../evidence/conditions-sets-072.md#c-b9a0a0fbf7956899) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [状态效果 S-5e8cd874c7fbacc7](../../evidence/state_effects-sets-020.md#s-5e8cd874c7fbacc7)

### path-023657

```text
(exec)# test cef <?dumper_command_func@555588cac488> table stdby-drh <address> add <cr>
```

Handler ` RVA 0xB46C150 `；selector ` 1 `；EOL ` RVA 0x3375AF80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Via IPv4 address。

[条件 C-f13d6a224ddf7cc6](../../evidence/conditions-sets-093.md#c-f13d6a224ddf7cc6) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-a24f27dbee9ff949](../../evidence/parameters-sets-012.md#p-a24f27dbee9ff949)

### path-023674

```text
(exec)# test cef <?dumper_command_func@555588cac488> table stdby-drh <address> add <cr>
```

Handler ` RVA 0xB46C150 `；selector ` 1 `；EOL ` RVA 0x3375E4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Via IPv6 Address。

[条件 C-2517d01d51e81be0](../../evidence/conditions-sets-014.md#c-2517d01d51e81be0) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-cde95a557c1cb0fa](../../evidence/parameters-sets-016.md#p-cde95a557c1cb0fa)

### path-023677

```text
(exec)# test cef <?dumper_command_func@555588cac488> table stdby-drh <address> remove <cr>
```

Handler ` RVA 0xB46C150 `；selector ` 0 `；EOL ` RVA 0x3375B228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Via IPv4 address。

[条件 C-8bf20d899b48a094](../../evidence/conditions-sets-054.md#c-8bf20d899b48a094) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-a24f27dbee9ff949](../../evidence/parameters-sets-012.md#p-a24f27dbee9ff949)

### path-023696

```text
(exec)# test cef <?dumper_command_func@555588cac488> table stdby-drh <address> remove <cr>
```

Handler ` RVA 0xB46C150 `；selector ` 0 `；EOL ` RVA 0x3375E748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Via IPv6 Address。

[条件 C-a6a974fa7ef58d59](../../evidence/conditions-sets-064.md#c-a6a974fa7ef58d59) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-cde95a557c1cb0fa](../../evidence/parameters-sets-016.md#p-cde95a557c1cb0fa)

### path-024985

```text
(exec)# test cef <?dumper_command_func@555588cac488> table subblock add prefix <address> <address> <cr>
```

Handler ` RVA 0xB46D150 `；selector ` 0 `；EOL ` RVA 0x3375A408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix address；` address ` Prefix mask。

[条件 C-222ad07c329f8dd7](../../evidence/conditions-sets-013.md#c-222ad07c329f8dd7) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [参数 P-c3ad5c28e684e7cc](../../evidence/parameters-sets-015.md#p-c3ad5c28e684e7cc) · [状态效果 S-291af4c88abbb026](../../evidence/state_effects-sets-009.md#s-291af4c88abbb026)

### path-025363

```text
(exec)# test cef <?dumper_command_func@555588cac488> table subblock add prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xB46D150 `；selector ` 0 `；EOL ` RVA 0x3375D950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix address。

[条件 C-3ab1e6f73c136c30](../../evidence/conditions-sets-023.md#c-3ab1e6f73c136c30) · [缺口 G-39d16eedd4592670](../../evidence/gaps-sets-003.md#g-39d16eedd4592670) · [参数 P-29d53f6a4fb3ef1c](../../evidence/parameters-sets-004.md#p-29d53f6a4fb3ef1c) · [状态效果 S-026d6c9957f36a09](../../evidence/state_effects-sets-001.md#s-026d6c9957f36a09)

### path-021375

```text
(exec)# test cef <?dumper_command_func@555588cac488> table trigger delete-all <cr>
```

Handler ` RVA 0xB46CD10 `；selector ` 0 `；EOL ` RVA 0x3375C2E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-405277d7ac70a68d](../../evidence/conditions-sets-025.md#c-405277d7ac70a68d) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524) · [状态效果 S-957d11baf87a309d](../../evidence/state_effects-sets-032.md#s-957d11baf87a309d)

### path-021358

```text
(exec)# test cef <?dumper_command_func@555588cac488> walks background disable <cr>
```

Handler ` RVA 0xB352790 `；selector ` 1 `；EOL ` RVA 0x33762F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-84f48df78274c938](../../evidence/conditions-sets-051.md#c-84f48df78274c938) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524)

### path-021357

```text
(exec)# test cef <?dumper_command_func@555588cac488> walks background enable <cr>
```

Handler ` RVA 0xB352790 `；selector ` 0 `；EOL ` RVA 0x33762C60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6b49f4d31d57944](../../evidence/conditions-sets-077.md#c-c6b49f4d31d57944) · [缺口 G-83946bfe84e10524](../../evidence/gaps-sets-005.md#g-83946bfe84e10524)

### path-021267

```text
(exec)# test cef assert fail <?option@555588cac098> fatal <cr>
```

Handler ` RVA 0xB363340 `；selector ` 0 `；EOL ` RVA 0x33758170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa37bc87803bfa8f](../../evidence/conditions-sets-066.md#c-aa37bc87803bfa8f) · [缺口 G-85693a83e589e3d1](../../evidence/gaps-sets-005.md#g-85693a83e589e3d1) · [状态效果 S-e788ddad2fbfb930](../../evidence/state_effects-sets-049.md#s-e788ddad2fbfb930)

### path-004738

```text
(exec)# test cef crimson-oper-db add <cr>
```

Handler ` RVA 0xB369C80 `；selector ` 0 `；EOL ` RVA 0x337520E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64e9503d0d152718](../../evidence/conditions-sets-039.md#c-64e9503d0d152718)

### path-004755

```text
(exec)# test cef crimson-oper-db del <cr>
```

Handler ` RVA 0xB369CF0 `；selector ` 0 `；EOL ` RVA 0x33752388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f84bf9bc0b0a5ea](../../evidence/conditions-sets-025.md#c-3f84bf9bc0b0a5ea)

### path-004698

```text
(exec)# test cef crimson-oper-db disable <cr>
```

Handler ` RVA 0xB369B50 `；selector ` 0 `；EOL ` RVA 0x33751830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc3273fbff2d3a02](../../evidence/conditions-sets-073.md#c-bc3273fbff2d3a02)

### path-004685

```text
(exec)# test cef crimson-oper-db enable <cr>
```

Handler ` RVA 0xB369AE0 `；selector ` 0 `；EOL ` RVA 0x33751588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4cb04edb7a207a4e](../../evidence/conditions-sets-030.md#c-4cb04edb7a207a4e)

### path-008463

```text
(exec)# test cef crimson-oper-db oc-nh-grp-db IPv4 <cr>
```

Handler ` RVA 0xB369BC0 `；selector ` 0 `；EOL ` RVA 0x33751C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-80f57f685328b0bc](../../evidence/conditions-sets-050.md#c-80f57f685328b0bc) · [状态效果 S-deb9aba18d169a0f](../../evidence/state_effects-sets-047.md#s-deb9aba18d169a0f)

### path-000831

```text
(exec)# test cef enable <cr>
```

Handler ` RVA 0xB480BC0 `；selector ` 0 `；EOL ` RVA 0x3374CCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee3625c1c2840a24](../../evidence/conditions-sets-092.md#c-ee3625c1c2840a24) · [状态效果 S-a1dda6db540ce4a0](../../evidence/state_effects-sets-034.md#s-a1dda6db540ce4a0)

### path-008465

```text
(exec)# test cef event-trace IPv4 <string> <cr>
```

Handler ` RVA 0xB47E360 `；selector ` 0 `；EOL ` RVA 0x33764268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` String to insert into event log。

[条件 C-fdc0a034fa1e71f0](../../evidence/conditions-sets-098.md#c-fdc0a034fa1e71f0) · [参数 P-c31ab8da975e92c0](../../evidence/parameters-sets-015.md#p-c31ab8da975e92c0) · [状态效果 S-404b8be51d1a3c3d](../../evidence/state_effects-sets-014.md#s-404b8be51d1a3c3d)

### path-004714

```text
(exec)# test cef ext-lb disable <cr>
```

Handler ` RVA 0xB3F0520 `；selector ` 1 `；EOL ` RVA 0x33753078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21f2340ea87d066f](../../evidence/conditions-sets-013.md#c-21f2340ea87d066f)

### path-004713

```text
(exec)# test cef ext-lb enable <cr>
```

Handler ` RVA 0xB3F0520 `；selector ` 0 `；EOL ` RVA 0x33752DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fe6e43eebc57c2b4](../../evidence/conditions-sets-098.md#c-fe6e43eebc57c2b4)

### path-008554

```text
(exec)# test cef get-nexthop-adj IPv4 <address> <cr>
```

Handler ` RVA 0xB419330 `；selector ` 0 `；EOL ` RVA 0x33755FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-c1c9a15bc5154c79](../../evidence/conditions-sets-075.md#c-c1c9a15bc5154c79) · [参数 P-cec27e68cf98fe44](../../evidence/parameters-sets-016.md#p-cec27e68cf98fe44) · [状态效果 S-aa5a2f23e7332be5](../../evidence/state_effects-sets-036.md#s-aa5a2f23e7332be5)

### path-021282

```text
(exec)# test cef hw-api fail <?option@555588cac4c8> fatal <cr>
```

Handler ` RVA 0xB3D8B00 `；selector ` 0 `；EOL ` RVA 0x337585A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-64d6b0e6200996ac](../../evidence/conditions-sets-039.md#c-64d6b0e6200996ac) · [缺口 G-cf478da77a7d8f22](../../evidence/gaps-sets-007.md#g-cf478da77a7d8f22) · [状态效果 S-39f4f80252cdd64c](../../evidence/state_effects-sets-013.md#s-39f4f80252cdd64c)

### path-004764

```text
(exec)# test cef idb consistency <cr>
```

Handler ` RVA 0xB3DD800 `；selector ` 0 `；EOL ` RVA 0x33754490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a0c5ef348d85d89](../../evidence/conditions-sets-022.md#c-3a0c5ef348d85d89)

### path-024625

```text
(exec)# test cef idb decap <interface> <address> add lisp <cr>
```

Handler ` RVA 0xB3DCE50 `；selector ` 0 `；EOL ` RVA 0x33754918 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-dc942f35d2b873bc](../../evidence/conditions-sets-085.md#c-dc942f35d2b873bc) · [缺口 G-9f74540137529f16](../../evidence/gaps-sets-006.md#g-9f74540137529f16) · [参数 P-5e5e5f533c1ff8af](../../evidence/parameters-sets-008.md#p-5e5e5f533c1ff8af) · [状态效果 S-ca7af6734c4df604](../../evidence/state_effects-sets-043.md#s-ca7af6734c4df604)

### path-023478

```text
(exec)# test cef idb stats IPv4 tx <interface> <cr>
```

Handler ` RVA 0xB3DD930 `；selector ` 0 `；EOL ` RVA 0x33754180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dcb4b216ce803364](../../evidence/conditions-sets-085.md#c-dcb4b216ce803364) · [缺口 G-dfc05f1ab13deee3](../../evidence/gaps-sets-008.md#g-dfc05f1ab13deee3) · [参数 P-6cd06bf7c42e856d](../../evidence/parameters-sets-009.md#p-6cd06bf7c42e856d) · [状态效果 S-7fcf85d189765d65](../../evidence/state_effects-sets-027.md#s-7fcf85d189765d65)

### path-023477

```text
(exec)# test cef lisp authc IPv4 <prefix:dynamic> enable <cr>
```

Handler ` RVA 0xB369550 `；selector ` 0 `；EOL ` RVA 0x337503A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` prefix/len。

[条件 C-5a7fcdbd368b8f12](../../evidence/conditions-sets-035.md#c-5a7fcdbd368b8f12) · [缺口 G-187586db704b5aaa](../../evidence/gaps-sets-001.md#g-187586db704b5aaa) · [参数 P-d35095c05e0db2c8](../../evidence/parameters-sets-016.md#p-d35095c05e0db2c8) · [状态效果 S-3547d2fda8a35d9b](../../evidence/state_effects-sets-012.md#s-3547d2fda8a35d9b)

### path-011967

```text
(exec)# test cef lisp l2instance create <number:0..65520> <number:0..65520> <number:1..4094> <cr>
```

Handler ` RVA 0xB369280 `；selector ` 0 `；EOL ` RVA 0x3374F290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Topology ID；` unsigned_number ` Instance ID；` unsigned_number ` L2 Domain ID。

[条件 C-88c9384ed38b0ef1](../../evidence/conditions-sets-053.md#c-88c9384ed38b0ef1) · [参数 P-418c739674d1ed69](../../evidence/parameters-sets-006.md#p-418c739674d1ed69)

### path-011970

```text
(exec)# test cef lisp map-req IPv4 <address> <address> r-eid <cr>
```

Handler ` RVA 0xB368BF0 `；selector ` 0 `；EOL ` RVA 0x3374EC28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Src Addr；` address ` Dst Addr。

[条件 C-39de570d3a6866ca](../../evidence/conditions-sets-022.md#c-39de570d3a6866ca) · [参数 P-a9fceed457be317e](../../evidence/parameters-sets-013.md#p-a9fceed457be317e) · [状态效果 S-6bf81e9332063e82](../../evidence/state_effects-sets-023.md#s-6bf81e9332063e82)

### path-010589

```text
(exec)# test cef lisp stats IPv4 clear <cr>
```

Handler ` RVA 0xB367480 `；selector ` 0 `；EOL ` RVA 0x3374FDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f4494d3fa172ed2](../../evidence/conditions-sets-043.md#c-6f4494d3fa172ed2) · [状态效果 S-a9f2f651683e63c5](../../evidence/state_effects-sets-036.md#s-a9f2f651683e63c5)

### path-010597

```text
(exec)# test cef lisp sw-fw eid-detection enable <cr>
```

Handler ` RVA 0xB3696E0 `；selector ` 0 `；EOL ` RVA 0x33750950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9709b97c27056596](../../evidence/conditions-sets-058.md#c-9709b97c27056596) · [状态效果 S-0a654e867b70db38](../../evidence/state_effects-sets-003.md#s-0a654e867b70db38)

### path-011653

```text
(exec)# test cef lisp unnum-if top-id <number:0..65520> clear-v4 <cr>
```

Handler ` RVA 0xB3693E0 `；selector ` 0 `；EOL ` RVA 0x3374F7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Topology ID。

[条件 C-71494d5b27a65975](../../evidence/conditions-sets-044.md#c-71494d5b27a65975) · [参数 P-05b6f7fd71866fd1](../../evidence/parameters-sets-001.md#p-05b6f7fd71866fd1)

### path-024608

```text
(exec)# test cef lisp unnum-if top-id <number:0..65520> set-v4 <interface> <cr>
```

Handler ` RVA 0xB3693E0 `；selector ` 0 `；EOL ` RVA 0x3374F7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Topology ID。

[条件 C-c6d2329a30319f35](../../evidence/conditions-sets-077.md#c-c6d2329a30319f35) · [缺口 G-d3713e7a96a73d84](../../evidence/gaps-sets-007.md#g-d3713e7a96a73d84) · [参数 P-ddc7798318bed6a9](../../evidence/parameters-sets-017.md#p-ddc7798318bed6a9)

### path-004643

```text
(exec)# test cef lisp_samecable <address> <cr>
```

Handler ` RVA 0xB368A00 `；selector ` 0 `；EOL ` RVA 0x3374E5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address。

[条件 C-53fbd45a60eb876f](../../evidence/conditions-sets-033.md#c-53fbd45a60eb876f) · [参数 P-7cbacb70d6c94687](../../evidence/parameters-sets-010.md#p-7cbacb70d6c94687)

### path-013196

```text
(exec)# test cef lisp_samecable <prefix:dynamic> <cr>
```

Handler ` RVA 0xB368A00 `；selector ` 0 `；EOL ` RVA 0x3374E5B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 Address。

[条件 C-3004d3f8fd775186](../../evidence/conditions-sets-019.md#c-3004d3f8fd775186) · [缺口 G-ed72ede88817e41c](../../evidence/gaps-sets-008.md#g-ed72ede88817e41c) · [参数 P-3634137072818ee1](../../evidence/parameters-sets-005.md#p-3634137072818ee1)

### path-021251

```text
(exec)# test cef malloc fail <?option@555588cabbc8> fatal <cr>
```

Handler ` RVA 0xB410DF0 `；selector ` 0 `；EOL ` RVA 0x33757CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b7843f980d9d3e99](../../evidence/conditions-sets-071.md#c-b7843f980d9d3e99) · [缺口 G-f0c971659d8334ec](../../evidence/gaps-sets-008.md#g-f0c971659d8334ec) · [状态效果 S-177f9a0a02076bf9](../../evidence/state_effects-sets-005.md#s-177f9a0a02076bf9)

### path-008540

```text
(exec)# test cef oce-explore IPv4 <address> <cr>
```

Handler ` RVA 0xB419590 `；selector ` 0 `；EOL ` RVA 0x337558B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Prefix of interest。

[条件 C-b7aee7c621eb6c3f](../../evidence/conditions-sets-071.md#c-b7aee7c621eb6c3f) · [参数 P-8b695f8397dd7da3](../../evidence/parameters-sets-011.md#p-8b695f8397dd7da3) · [状态效果 S-da861243860fc782](../../evidence/state_effects-sets-046.md#s-da861243860fc782)

### path-000896

```text
(exec)# test cef offset <cr>
```

Handler ` RVA 0xB35E1A0 `；selector ` 0 `；EOL ` RVA 0x3374E258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-781bbeef4e8592c6](../../evidence/conditions-sets-047.md#c-781bbeef4e8592c6)

### path-004777

```text
(exec)# test cef register-interest show <cr>
```

Handler ` RVA 0xB3A90C0 `；selector ` 0 `；EOL ` RVA 0x33754D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bdc7ad6f2fc7680d](../../evidence/conditions-sets-073.md#c-bdc7ad6f2fc7680d) · [状态效果 S-53389d267cd5dbfa](../../evidence/state_effects-sets-018.md#s-53389d267cd5dbfa)

### path-023472

```text
(exec)# test cef rmi <interface> IPv4 <address> add <cr>
```

Handler ` RVA 0xB3DCCB0 `；selector ` 1 `；EOL ` RVA 0x33753550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-cdc10725ecdfa1d6](../../evidence/conditions-sets-079.md#c-cdc10725ecdfa1d6) · [缺口 G-7ed644211bb5f59a](../../evidence/gaps-sets-005.md#g-7ed644211bb5f59a) · [参数 P-56ff103610559c25](../../evidence/parameters-sets-007.md#p-56ff103610559c25) · [状态效果 S-1d68706f7b00a930](../../evidence/state_effects-sets-007.md#s-1d68706f7b00a930)

### path-023482

```text
(exec)# test cef rmi <interface> IPv4 <address> remove <cr>
```

Handler ` RVA 0xB3DCCB0 `；selector ` 0 `；EOL ` RVA 0x337537F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address。

[条件 C-6170c592891ce7e7](../../evidence/conditions-sets-038.md#c-6170c592891ce7e7) · [缺口 G-7ed644211bb5f59a](../../evidence/gaps-sets-005.md#g-7ed644211bb5f59a) · [参数 P-56ff103610559c25](../../evidence/parameters-sets-007.md#p-56ff103610559c25) · [状态效果 S-1d68706f7b00a930](../../evidence/state_effects-sets-007.md#s-1d68706f7b00a930)

### path-017120

```text
(exec)# test cef route-active IPv4 <prefix:dynamic> <cr>
```

Handler ` RVA 0xB369D60 `；selector ` 0 `；EOL ` RVA 0x33752870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` prefix/len。

[条件 C-0ab652057097c024](../../evidence/conditions-sets-004.md#c-0ab652057097c024) · [缺口 G-62bcfcd2be9ff1a4](../../evidence/gaps-sets-004.md#g-62bcfcd2be9ff1a4) · [参数 P-3fac20ab8914458b](../../evidence/parameters-sets-005.md#p-3fac20ab8914458b) · [状态效果 S-fb56ed11cfadac26](../../evidence/state_effects-sets-053.md#s-fb56ed11cfadac26)

### path-004726

```text
(exec)# test cef sadr-oce <address> <cr>
```

Handler ` RVA 0xB369F40 `；selector ` 0 `；EOL ` RVA 0x33753C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address。

[条件 C-a23ed1828e5007da](../../evidence/conditions-sets-063.md#c-a23ed1828e5007da) · [参数 P-ae52a741803cbe9b](../../evidence/parameters-sets-013.md#p-ae52a741803cbe9b)

### path-021133

```text
(exec)# test cef signal-oce IPv4 <prefix:dynamic> insert <cr>
```

Handler ` RVA 0xB369750 `；selector ` 0 `；EOL ` RVA 0x33751018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` prefix/len。

[条件 C-fd4b6dd96b4f3a12](../../evidence/conditions-sets-098.md#c-fd4b6dd96b4f3a12) · [缺口 G-f0413d89a28b83c8](../../evidence/gaps-sets-008.md#g-f0413d89a28b83c8) · [参数 P-259ca47d78c6590e](../../evidence/parameters-sets-003.md#p-259ca47d78c6590e) · [状态效果 S-7baf9c4ace1f6ec6](../../evidence/state_effects-sets-026.md#s-7baf9c4ace1f6ec6)

### path-025200

```text
(exec)# test cef subtree context test add IPv4 <?option@555588cab548> <address> <number:0..32> <number:0..1000> <cr>
```

Handler ` RVA 0xB453970 `；selector ` 0 `；EOL ` RVA 0x33757740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Prefix for ipv4 context；` unsigned_number ` Prefix length；` unsigned_number ` Context value。

[条件 C-ead5a63db9369e60](../../evidence/conditions-sets-091.md#c-ead5a63db9369e60) · [缺口 G-c982285cb2d57546](../../evidence/gaps-sets-007.md#g-c982285cb2d57546) · [参数 P-90f9654fd46995ba](../../evidence/parameters-sets-011.md#p-90f9654fd46995ba) · [状态效果 S-cbdd5a6f91f7c689](../../evidence/state_effects-sets-043.md#s-cbdd5a6f91f7c689)

### path-008374

```text
(exec)# test cef switching IPv4 clear <cr>
```

Handler ` RVA 0xB4561F0 `；selector ` 0 `；EOL ` RVA 0x3374D358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21a3bba65258167a](../../evidence/conditions-sets-013.md#c-21a3bba65258167a) · [状态效果 S-2cf89baa5bd95305](../../evidence/state_effects-sets-010.md#s-2cf89baa5bd95305)

### path-008593

```text
(exec)# test cef track-destination IPv4 local-label <cr>
```

Handler ` RVA 0xB418EB0 `；selector ` 0 `；EOL ` RVA 0x33756740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f93ef4c4e9b86044](../../evidence/conditions-sets-096.md#c-f93ef4c4e9b86044) · [状态效果 S-9381c82d3749403f](../../evidence/state_effects-sets-031.md#s-9381c82d3749403f)

### path-004860

```text
(exec)# test cef user-command <number:1..255> <cr>
```

Handler ` RVA 0xB485500 `；selector ` 0 `；EOL ` RVA 0x33756D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` User-command command number。

[条件 C-eaa58f90f46ffb12](../../evidence/conditions-sets-091.md#c-eaa58f90f46ffb12) · [参数 P-991dea8e01a30443](../../evidence/parameters-sets-012.md#p-991dea8e01a30443)

### path-021138

```text
(exec)# test cellular <interface> cdma rev-a enable <cr>
```

Handler ` RVA 0x16203510 `；selector ` 3 `；EOL ` RVA 0x35F37E98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94b0a92afee1698f](../../evidence/conditions-sets-057.md#c-94b0a92afee1698f) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-169b778aac127734](../../evidence/state_effects-sets-005.md#s-169b778aac127734)

### path-021150

```text
(exec)# test cellular <interface> cnm-process-enqueue messages <number:0..5> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 0 `；EOL ` RVA 0x35F37B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0 - Heartbeat, 1 - Call disc, 2 - too hot,        3 - reset, 4 - modem up, 5 - undefined。

[条件 C-ca86112afe3a7dec](../../evidence/conditions-sets-078.md#c-ca86112afe3a7dec) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-9a3396f3e574aa4d](../../evidence/parameters-sets-012.md#p-9a3396f3e574aa4d)

### path-016993

```text
(exec)# test cellular <interface> geofence-gps-periodic-timer-val <number:2..10> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 16 `；EOL ` RVA 0x35F35610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` GPS periodic update timer value in mins。

[条件 C-949169aed5c5a419](../../evidence/conditions-sets-057.md#c-949169aed5c5a419) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-0a4376ddcafe0447](../../evidence/parameters-sets-001.md#p-0a4376ddcafe0447)

### path-013238

```text
(exec)# test cellular <interface> gps-clear <cr>
```

Handler ` RVA 0x16203510 `；selector ` 9 `；EOL ` RVA 0x35F36B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-031a57bf744c6a7f](../../evidence/conditions-sets-002.md#c-031a57bf744c6a7f) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-017110

```text
(exec)# test cellular <interface> gps-port GPS <cr>
```

Handler ` RVA 0x16203510 `；selector ` 11 `；EOL ` RVA 0x35F36EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ca0554142f556746](../../evidence/conditions-sets-078.md#c-ca0554142f556746) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-b8674e82a0a12f74](../../evidence/state_effects-sets-039.md#s-b8674e82a0a12f74)

### path-017146

```text
(exec)# test cellular <interface> ims-service bind-subscription <cr>
```

Handler ` RVA 0x16203510 `；selector ` 17 `；EOL ` RVA 0x35F376F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d2846f328f13363a](../../evidence/conditions-sets-081.md#c-d2846f328f13363a) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-23f8b0f94d4316d0](../../evidence/state_effects-sets-008.md#s-23f8b0f94d4316d0)

### path-013032

```text
(exec)# test cellular <interface> modem-at-all-admin-tech <cr>
```

Handler ` RVA 0x16203510 `；selector ` 20 `；EOL ` RVA 0x35F34D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1ed9c593d7b651bd](../../evidence/conditions-sets-012.md#c-1ed9c593d7b651bd) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-016957

```text
(exec)# test cellular <interface> modem-at-command <string> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 18 `；EOL ` RVA 0x35F352E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` AT command string。

[条件 C-744fcafd95852137](../../evidence/conditions-sets-045.md#c-744fcafd95852137) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-49fb8efe53ffa1f7](../../evidence/parameters-sets-006.md#p-49fb8efe53ffa1f7)

### path-017056

```text
(exec)# test cellular <interface> modem-dmlog disable <cr>
```

Handler ` RVA 0x16203510 `；selector ` 21 `；EOL ` RVA 0x35F36210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5fda3a754391ba36](../../evidence/conditions-sets-037.md#c-5fda3a754391ba36) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-6e9e611c277c7cf7](../../evidence/state_effects-sets-023.md#s-6e9e611c277c7cf7)

### path-013146

```text
(exec)# test cellular <interface> modem-error-clear <cr>
```

Handler ` RVA 0x16203510 `；selector ` 10 `；EOL ` RVA 0x35F35B50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cff8d16e0fb3c6e6](../../evidence/conditions-sets-080.md#c-cff8d16e0fb3c6e6) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-013160

```text
(exec)# test cellular <interface> modem-power-cycle <cr>
```

Handler ` RVA 0x16203510 `；selector ` 2 `；EOL ` RVA 0x35F35DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-21a5d2ad67db0cd2](../../evidence/conditions-sets-013.md#c-21a5d2ad67db0cd2) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-013275

```text
(exec)# test cellular <interface> modem-power-off <cr>
```

Handler ` RVA 0x16203510 `；selector ` 5 `；EOL ` RVA 0x35F38478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4cea7e9ef7da68d](../../evidence/conditions-sets-094.md#c-f4cea7e9ef7da68d) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-013255

```text
(exec)# test cellular <interface> modem-power-on <cr>
```

Handler ` RVA 0x16203510 `；selector ` 4 `；EOL ` RVA 0x35F381D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2ef38fec0240610](../../evidence/conditions-sets-087.md#c-e2ef38fec0240610) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-013123

```text
(exec)# test cellular <interface> modem-reset <cr>
```

Handler ` RVA 0x16203510 `；selector ` 1 `；EOL ` RVA 0x35F358A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f894a1d2dd5483a2](../../evidence/conditions-sets-096.md#c-f894a1d2dd5483a2) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-017111

```text
(exec)# test cellular <interface> radio-power on <cr>
```

Handler ` RVA 0x16203510 `；selector ` 7 `；EOL ` RVA 0x35F37350 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a45f6d111472e71e](../../evidence/conditions-sets-063.md#c-a45f6d111472e71e) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c) · [状态效果 S-1250e7eaa2745c8d](../../evidence/state_effects-sets-004.md#s-1250e7eaa2745c8d)

### path-017051

```text
(exec)# test cellular <interface> rsrp <number:0..150> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 13 `；EOL ` RVA 0x35F365E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` lte rsrp value。

[条件 C-94b64098da548654](../../evidence/conditions-sets-058.md#c-94b64098da548654) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-80a214569c60241d](../../evidence/parameters-sets-010.md#p-80a214569c60241d)

### path-017066

```text
(exec)# test cellular <interface> rsrq <number:0..20> <cr>
```

Handler ` RVA 0x16203510 `；selector ` 14 `；EOL ` RVA 0x35F368D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` lte rsrq value。

[条件 C-204f757b657f630d](../../evidence/conditions-sets-013.md#c-204f757b657f630d) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-9209a2c8cedfcc4e](../../evidence/parameters-sets-011.md#p-9209a2c8cedfcc4e)

### path-013010

```text
(exec)# test cellular <interface> ursp-get-td <cr>
```

Handler ` RVA 0x16203510 `；selector ` 22 `；EOL ` RVA 0x35F34A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2a3771a814a05f21](../../evidence/conditions-sets-017.md#c-2a3771a814a05f21) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-013053

```text
(exec)# test cellular <interface> ursp-route-clear <cr>
```

Handler ` RVA 0x16203510 `；selector ` 19 `；EOL ` RVA 0x35F34FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-21122eafd6684b12](../../evidence/conditions-sets-013.md#c-21122eafd6684b12) · [缺口 G-5d1103a58c4b0b47](../../evidence/gaps-sets-004.md#g-5d1103a58c4b0b47) · [参数 P-af340358732c790c](../../evidence/parameters-sets-013.md#p-af340358732c790c)

### path-000756

```text
(exec)# test checkpoint add <cr>
```

Handler ` RVA 0xCDD0C40 `；selector ` 0 `；EOL ` RVA 0x33CF0A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-7e9c062a03482bee](../../evidence/state_effects-sets-027.md#s-7e9c062a03482bee)

### path-000926

```text
(exec)# test cisp disable <cr>
```

Handler ` RVA 0xCB25570 `；selector ` 0 `；EOL ` RVA 0x33BB54C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d1b9427b0660df9](../../evidence/conditions-sets-024.md#c-3d1b9427b0660df9)

### path-000927

```text
(exec)# test cisp enable <cr>
```

Handler ` RVA 0xCB254F0 `；selector ` 0 `；EOL ` RVA 0x33BB67C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-317a0d54f37d076a](../../evidence/conditions-sets-019.md#c-317a0d54f37d076a)

### path-024612

```text
(exec)# test cisp intf <interface> client add mac <address> <cr>
```

Handler ` RVA 0xCB25890 `；selector ` 0 `；EOL ` RVA 0x33BB5A48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` 48 bit mac address。

[条件 C-1e615e89326ba07b](../../evidence/conditions-sets-012.md#c-1e615e89326ba07b) · [缺口 G-30493fdda3f1d849](../../evidence/gaps-sets-002.md#g-30493fdda3f1d849) · [参数 P-bc23b0a3bd7fcf69](../../evidence/parameters-sets-014.md#p-bc23b0a3bd7fcf69) · [状态效果 S-603f8f8b7521e47e](../../evidence/state_effects-sets-021.md#s-603f8f8b7521e47e)

### path-017135

```text
(exec)# test cisp intf <interface> stop <cr>
```

Handler ` RVA 0xCB256D0 `；selector ` 0 `；EOL ` RVA 0x33BB6390 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1514c918ca04fa3a](../../evidence/conditions-sets-008.md#c-1514c918ca04fa3a) · [缺口 G-30493fdda3f1d849](../../evidence/gaps-sets-002.md#g-30493fdda3f1d849) · [参数 P-5fc6a08e308c7bce](../../evidence/parameters-sets-008.md#p-5fc6a08e308c7bce) · [状态效果 S-14deb38c549d0105](../../evidence/state_effects-sets-005.md#s-14deb38c549d0105)

### path-024614

```text
(exec)# test cisp intf <interface> user add name <string> <cr>
```

Handler ` RVA 0xCB255C0 `；selector ` 0 `；EOL ` RVA 0x33BB5F68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` user name。

[条件 C-94c5f2a452b05b11](../../evidence/conditions-sets-058.md#c-94c5f2a452b05b11) · [缺口 G-30493fdda3f1d849](../../evidence/gaps-sets-002.md#g-30493fdda3f1d849) · [参数 P-ef4244179b5b6bd7](../../evidence/parameters-sets-018.md#p-ef4244179b5b6bd7) · [状态效果 S-42b819ce95bec176](../../evidence/state_effects-sets-015.md#s-42b819ce95bec176)

### path-002126

```text
(exec)# test clear-nvram local-lock <cr>
```

Handler ` RVA 0xE0E2710 `；selector ` 0 `；EOL ` RVA 0x341FA0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008199

```text
(exec)# test cli-agent config-accounting test-mode disable <cr>
```

Handler ` RVA 0x143F2DB0 `；selector ` 1 `；EOL ` RVA 0x35D5DCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6892b01b0c8ffb00](../../evidence/conditions-sets-040.md#c-6892b01b0c8ffb00)

### path-008180

```text
(exec)# test cli-agent config-accounting test-mode enable <cr>
```

Handler ` RVA 0x143F2DB0 `；selector ` 0 `；EOL ` RVA 0x35D5DA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9185db6208804a1](../../evidence/conditions-sets-077.md#c-c9185db6208804a1)

### path-002257

```text
(exec)# test cns history <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 1 `；EOL ` RVA 0x34612D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-002300

```text
(exec)# test cns inventory <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 2 `；EOL ` RVA 0x34613250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-002281

```text
(exec)# test cns summary <cr>
```

Handler ` RVA 0xF338C70 `；selector ` 3 `；EOL ` RVA 0x34612FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-014017

```text
(exec)# test config_notify_cb <interface> open_access <cr>
```

Handler ` RVA 0x15E9D3A0 `；selector ` 0 `；EOL ` RVA 0x35E5A8A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ee54ff76e9e88b45](../../evidence/conditions-sets-092.md#c-ee54ff76e9e88b45) · [缺口 G-4a6d765040846e70](../../evidence/gaps-sets-003.md#g-4a6d765040846e70) · [参数 P-4b32da70b58e4977](../../evidence/parameters-sets-006.md#p-4b32da70b58e4977) · [状态效果 S-4a172e07768ffeca](../../evidence/state_effects-sets-016.md#s-4a172e07768ffeca)

### path-008900

```text
(exec)# test cops start-listen <address> <number:0..65535> <cr>
```

Handler ` RVA 0xF44A4B0 `；selector ` 1 `；EOL ` RVA 0x3464CA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address to listen for；` unsigned_number ` port number。

[条件 C-0fc166e9adb4f6e4](../../evidence/conditions-sets-006.md#c-0fc166e9adb4f6e4) · [参数 P-1c899d9a6cba1e7a](../../evidence/parameters-sets-003.md#p-1c899d9a6cba1e7a)

### path-008916

```text
(exec)# test cops stop-listen <address> <number:0..65535> <cr>
```

Handler ` RVA 0xF44A4B0 `；selector ` 2 `；EOL ` RVA 0x3464CD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address to stop listening for；` unsigned_number ` port number。

[条件 C-0fc166e9adb4f6e4](../../evidence/conditions-sets-006.md#c-0fc166e9adb4f6e4) · [参数 P-365bcbc13d07ba46](../../evidence/parameters-sets-005.md#p-365bcbc13d07ba46)

### path-004682

```text
(exec)# test cot set def-params <cr>
```

Handler ` RVA 0x161B8850 `；selector ` 0 `；EOL ` RVA 0x35F0AB88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-e4970e6e3cdec396](../../evidence/state_effects-sets-048.md#s-e4970e6e3cdec396)

### path-004358

```text
(exec)# test cpuaccounting debug dump <cr>
```

Handler ` RVA 0xE0822D0 `；selector ` 0 `；EOL ` RVA 0x341DCE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-7f1d76a693230784](../../evidence/state_effects-sets-027.md#s-7f1d76a693230784)

### path-004324

```text
(exec)# test cpurmi hog complex <cr>
```

Handler ` RVA 0xD6D2410 `；selector ` 2 `；EOL ` RVA 0x33ECD828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008080

```text
(exec)# test cpurmi hog simple <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2410 `；selector ` 1 `；EOL ` RVA 0x33ECD5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Slot Number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-8683939829a6685a](../../evidence/parameters-sets-010.md#p-8683939829a6685a)

### path-000132

```text
(exec)# test crash <cr>
```

Handler ` RVA 0xE8F5540 `；selector ` 0 `；EOL ` RVA 0x3433F780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-012126

```text
(exec)# test crypto kgs-test perf controller <number:1..300> <number:1..300> <number:1..10000> <number:1..300> <cr>
```

Handler ` RVA 0x12132450 `；selector ` 0 `；EOL ` RVA 0x357A1208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting k-value；` unsigned_number ` Ending k-value；` unsigned_number ` Number of trials for timing；` unsigned_number ` K-value interval size。

[条件 C-9a593addb33d5c36](../../evidence/conditions-sets-060.md#c-9a593addb33d5c36) · [参数 P-720889cf2f064708](../../evidence/parameters-sets-009.md#p-720889cf2f064708) · [状态效果 S-c2b8cefe88013a03](../../evidence/state_effects-sets-041.md#s-c2b8cefe88013a03)

### path-005858

```text
(exec)# test crypto modexp perf-test <cr>
```

Handler ` RVA 0x120E8FF0 `；selector ` 0 `；EOL ` RVA 0x357A0AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a593addb33d5c36](../../evidence/conditions-sets-060.md#c-9a593addb33d5c36)

### path-005886

```text
(exec)# test crypto modexp self-test <cr>
```

Handler ` RVA 0x120E8C60 `；selector ` 0 `；EOL ` RVA 0x357A0D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a593addb33d5c36](../../evidence/conditions-sets-060.md#c-9a593addb33d5c36)

### path-005949

```text
(exec)# test crypto nist-tests cfb8 <cr>
```

Handler ` RVA 0x120E8B50 `；selector ` 0 `；EOL ` RVA 0x357A1650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a593addb33d5c36](../../evidence/conditions-sets-060.md#c-9a593addb33d5c36) · [状态效果 S-09be142526331f4f](../../evidence/state_effects-sets-002.md#s-09be142526331f4f)

### path-009386

```text
(exec)# test crypto pki api <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 9 `；EOL ` RVA 0x3575A2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` API name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-56e00e3d600f8fae](../../evidence/parameters-sets-007.md#p-56e00e3d600f8fae)

### path-009289

```text
(exec)# test crypto pki benchmark rsa <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 4 `；EOL ` RVA 0x35757D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-011159

```text
(exec)# test crypto pki benchmark validate-peer <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 6 `；EOL ` RVA 0x35758420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-e5897f7a7dfdc707](../../evidence/parameters-sets-017.md#p-e5897f7a7dfdc707)

### path-011154

```text
(exec)# test crypto pki benchmark validate-router <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 5 `；EOL ` RVA 0x35758120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint to validate。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-a79f40b9c7686186](../../evidence/parameters-sets-013.md#p-a79f40b9c7686186)

### path-009304

```text
(exec)# test crypto pki cache on <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 10 `；EOL ` RVA 0x357590F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-756396783dc1539d](../../evidence/state_effects-sets-025.md#s-756396783dc1539d)

### path-005893

```text
(exec)# test crypto pki cert-attributes <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 1 `；EOL ` RVA 0x35757150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009165

```text
(exec)# test crypto pki config-update-notify <string> <cr>
```

Handler ` RVA 0x11F3D8C0 `；selector ` 0 `；EOL ` RVA 0x35756438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` HA request string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-cace0a1b6548127a](../../evidence/parameters-sets-015.md#p-cace0a1b6548127a)

### path-011106

```text
(exec)# test crypto pki crl request <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 18 `；EOL ` RVA 0x35756760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for the CRL request。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-823609e6f38dac50](../../evidence/parameters-sets-010.md#p-823609e6f38dac50)

### path-011142

```text
(exec)# test crypto pki csr <string> nb <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 8 `；EOL ` RVA 0x35758788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint for new certificate。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-9385614f2d1b8c51](../../evidence/parameters-sets-011.md#p-9385614f2d1b8c51) · [状态效果 S-1ae7faaeb0b91306](../../evidence/state_effects-sets-006.md#s-1ae7faaeb0b91306)

### path-006264

```text
(exec)# test crypto pki enrollment-proxy-api <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 12 `；EOL ` RVA 0x3575A6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009373

```text
(exec)# test crypto pki expiry-alerts reset <cr>
```

Handler ` RVA 0x1202AFD0 `；selector ` 0 `；EOL ` RVA 0x35759F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009354

```text
(exec)# test crypto pki expiry-alerts shrink-periodicity <cr>
```

Handler ` RVA 0x1202AF70 `；selector ` 0 `；EOL ` RVA 0x35759CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009248

```text
(exec)# test crypto pki new-cert <string> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 7 `；EOL ` RVA 0x357579B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint to se for new certificate (shadow) operations。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-c90f6fedf1b7f7ab](../../evidence/parameters-sets-015.md#p-c90f6fedf1b7f7ab)

### path-011823

```text
(exec)# test crypto pki ocsp-get-staple <string> chain blocking-test <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 16 `；EOL ` RVA 0x35756DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-a0283f60f8b05691](../../evidence/parameters-sets-012.md#p-a0283f60f8b05691) · [状态效果 S-449917abbf60e423](../../evidence/state_effects-sets-015.md#s-449917abbf60e423)

### path-006044

```text
(exec)# test crypto pki openssl <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 19 `；EOL ` RVA 0x35758A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005817

```text
(exec)# test crypto pki pkcs7verify <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 0 `；EOL ` RVA 0x357569F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009294

```text
(exec)# test crypto pki safemode on <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 11 `；EOL ` RVA 0x35758D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-30f7f3a861d92ce0](../../evidence/state_effects-sets-011.md#s-30f7f3a861d92ce0)

### path-005946

```text
(exec)# test crypto pki self-signed-certificate <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 3 `；EOL ` RVA 0x357576A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009320

```text
(exec)# test crypto pki session <number:1..60> <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 15 `；EOL ` RVA 0x35759450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session Lifetime。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-d9270027cf31aba6](../../evidence/parameters-sets-016.md#p-d9270027cf31aba6)

### path-009358

```text
(exec)# test crypto pki trustpool remove <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 14 `；EOL ` RVA 0x357599E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009334

```text
(exec)# test crypto pki trustpool reset <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 13 `；EOL ` RVA 0x35759740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005913

```text
(exec)# test crypto pki verify-certificate <cr>
```

Handler ` RVA 0x11F35250 `；selector ` 2 `；EOL ` RVA 0x357573F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005835

```text
(exec)# test crypto replay <number:1..4294967295> <cr>
```

Handler ` RVA 0x120E8740 `；selector ` 0 `；EOL ` RVA 0x357A0528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Replay counter value。

[条件 C-2eace69440c76f36](../../evidence/conditions-sets-018.md#c-2eace69440c76f36) · [参数 P-17461aa5dd937e32](../../evidence/parameters-sets-002.md#p-17461aa5dd937e32)

### path-009205

```text
(exec)# test crypto replay time <number:1..42949672> <cr>
```

Handler ` RVA 0x120E88B0 `；selector ` 0 `；EOL ` RVA 0x357A0280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Replay time value (seconds)。

[条件 C-6a54b22bb1ff7441](../../evidence/conditions-sets-041.md#c-6a54b22bb1ff7441) · [参数 P-b5994b27a0bb9e74](../../evidence/parameters-sets-014.md#p-b5994b27a0bb9e74)

### path-002001

```text
(exec)# test crypto rng-tests <cr>
```

Handler ` RVA 0x120E8C00 `；selector ` 0 `；EOL ` RVA 0x3579FE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a593addb33d5c36](../../evidence/conditions-sets-060.md#c-9a593addb33d5c36) · [状态效果 S-c21949f208eb1f63](../../evidence/state_effects-sets-041.md#s-c21949f208eb1f63)

### path-002040

```text
(exec)# test crypto self-test <cr>
```

Handler ` RVA 0x12953C40 `；selector ` 0 `；EOL ` RVA 0x357A07C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a593addb33d5c36](../../evidence/conditions-sets-060.md#c-9a593addb33d5c36)

### path-009171

```text
(exec)# test crypto wui tti petitioner <cr>
```

Handler ` RVA 0x12E03210 `；selector ` 0 `；EOL ` RVA 0x359E4640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-002049

```text
(exec)# test cts enable <cr>
```

Handler ` RVA 0x13026640 `；selector ` 0 `；EOL ` RVA 0x35A121F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4bf6e0b6f7a17262](../../evidence/conditions-sets-030.md#c-4bf6e0b6f7a17262) · [状态效果 S-697907684e229ff7](../../evidence/state_effects-sets-023.md#s-697907684e229ff7)

### path-009277

```text
(exec)# test cts event trace enable <cr>
```

Handler ` RVA 0x131020F0 `；selector ` 0 `；EOL ` RVA 0x35A48190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-906250ff7a953336](../../evidence/conditions-sets-056.md#c-906250ff7a953336) · [状态效果 S-d68d0c3d1ff8cefb](../../evidence/state_effects-sets-045.md#s-d68d0c3d1ff8cefb)

### path-011263

```text
(exec)# test cts role-based cgc qlist sort <cr>
```

Handler ` RVA 0x1423AAA0 `；selector ` 0 `；EOL ` RVA 0x35D07930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc)

### path-012134

```text
(exec)# test cts role-based counters from <number:2..65521> to <number:2..65521> hw <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 6 `；EOL ` RVA 0x35CFEF68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Security Group Tag；` unsigned_number ` Security Group Tag。

[条件 C-293394962683e000](../../evidence/conditions-sets-016.md#c-293394962683e000) · [参数 P-efb1785cb7b80b9c](../../evidence/parameters-sets-018.md#p-efb1785cb7b80b9c) · [状态效果 S-674971e89e4bb9c8](../../evidence/state_effects-sets-022.md#s-674971e89e4bb9c8)

### path-011232

```text
(exec)# test cts role-based dump ipsgt <address> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 3 `；EOL ` RVA 0x35CEAD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 host address。

[条件 C-5113b4ec94dce541](../../evidence/conditions-sets-032.md#c-5113b4ec94dce541) · [参数 P-b80a5b0d81b8ff65](../../evidence/parameters-sets-014.md#p-b80a5b0d81b8ff65) · [状态效果 S-5bf94c7af548e747](../../evidence/state_effects-sets-020.md#s-5bf94c7af548e747)

### path-022191

```text
(exec)# test cts role-based dump ipsgt <prefix:dynamic> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 3 `；EOL ` RVA 0x35CEAD98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-4d0025d9a3346e23](../../evidence/conditions-sets-030.md#c-4d0025d9a3346e23) · [缺口 G-09f47e5f6b20a016](../../evidence/gaps-sets-001.md#g-09f47e5f6b20a016) · [参数 P-81b24352e21d9ea8](../../evidence/parameters-sets-010.md#p-81b24352e21d9ea8) · [状态效果 S-b9ae6c3967b46fa4](../../evidence/state_effects-sets-039.md#s-b9ae6c3967b46fa4)

### path-009523

```text
(exec)# test cts role-based dump permissions <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 1 `；EOL ` RVA 0x35D028E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-d65f03260d49fb5d](../../evidence/state_effects-sets-045.md#s-d65f03260d49fb5d)

### path-011269

```text
(exec)# test cts role-based dump policy dynamic <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 0 `；EOL ` RVA 0x35D020E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b24407fda852fb3](../../evidence/conditions-sets-048.md#c-7b24407fda852fb3) · [状态效果 S-37af93b875db8995](../../evidence/state_effects-sets-012.md#s-37af93b875db8995)

### path-009477

```text
(exec)# test cts role-based dump sg-info <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 11 `；EOL ` RVA 0x35D02C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-c7d7b664e9be1995](../../evidence/state_effects-sets-042.md#s-c7d7b664e9be1995)

### path-011325

```text
(exec)# test cts role-based echo cli <string> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 14 `；EOL ` RVA 0x35CEDD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Text line to print in selected context。

[条件 C-317ae93921646279](../../evidence/conditions-sets-019.md#c-317ae93921646279) · [参数 P-f304f9509e72a317](../../evidence/parameters-sets-018.md#p-f304f9509e72a317) · [状态效果 S-553bb81e2af65728](../../evidence/state_effects-sets-019.md#s-553bb81e2af65728)

### path-009616

```text
(exec)# test cts role-based enforcement enable <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 13 `；EOL ` RVA 0x35D01AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-31aa336356f5889b](../../evidence/state_effects-sets-011.md#s-31aa336356f5889b)

### path-022158

```text
(exec)# test cts role-based ipm <interface> stop <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 7 `；EOL ` RVA 0x35CEC6E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c340ccb86e1c621](../../evidence/conditions-sets-011.md#c-1c340ccb86e1c621) · [缺口 G-e224891e0ba87efc](../../evidence/gaps-sets-008.md#g-e224891e0ba87efc) · [参数 P-d273da3bd234e50b](../../evidence/parameters-sets-016.md#p-d273da3bd234e50b) · [状态效果 S-6e10f5f37438f7fe](../../evidence/state_effects-sets-023.md#s-6e10f5f37438f7fe)

### path-009497

```text
(exec)# test cts role-based ipsgt refresh <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 2 `；EOL ` RVA 0x35CEB560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-2a6fd8fde6b6029e](../../evidence/state_effects-sets-010.md#s-2a6fd8fde6b6029e)

### path-006394

```text
(exec)# test cts role-based ping <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 12 `；EOL ` RVA 0x35CED858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc)

### path-009614

```text
(exec)# test cts role-based policy close <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 4 `；EOL ` RVA 0x35CFF6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-4ea979ac1493bc1f](../../evidence/state_effects-sets-017.md#s-4ea979ac1493bc1f)

### path-009613

```text
(exec)# test cts role-based rbacl save <cr>
```

Handler ` RVA 0x1414C4D0 `；selector ` 5 `；EOL ` RVA 0x35D01258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-48d88d5c447b3ac9](../../evidence/state_effects-sets-016.md#s-48d88d5c447b3ac9)

### path-006301

```text
(exec)# test cts role-based sgacl-log <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 15 `；EOL ` RVA 0x35CED318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc)

### path-011260

```text
(exec)# test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 5 `；EOL ` RVA 0x35CF4950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55ae73f76c8235d7](../../evidence/conditions-sets-034.md#c-55ae73f76c8235d7) · [状态效果 S-683d8c276a4a043d](../../evidence/state_effects-sets-022.md#s-683d8c276a4a043d)

### path-011268

```text
(exec)# test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 4 `；EOL ` RVA 0x35CF4E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4142e31ec8f546f3](../../evidence/conditions-sets-026.md#c-4142e31ec8f546f3) · [状态效果 S-683d8c276a4a043d](../../evidence/state_effects-sets-022.md#s-683d8c276a4a043d)

### path-011278

```text
(exec)# test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 3 `；EOL ` RVA 0x35CF5168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88180d292abb9f97](../../evidence/conditions-sets-053.md#c-88180d292abb9f97) · [状态效果 S-683d8c276a4a043d](../../evidence/state_effects-sets-022.md#s-683d8c276a4a043d)

### path-011286

```text
(exec)# test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 2 `；EOL ` RVA 0x35CF5840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8237000ed89ae9a5](../../evidence/conditions-sets-050.md#c-8237000ed89ae9a5) · [状态效果 S-683d8c276a4a043d](../../evidence/state_effects-sets-022.md#s-683d8c276a4a043d)

### path-011299

```text
(exec)# test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 1 `；EOL ` RVA 0x35CF5FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b9d826b67eaf50b](../../evidence/conditions-sets-005.md#c-0b9d826b67eaf50b) · [状态效果 S-683d8c276a4a043d](../../evidence/state_effects-sets-022.md#s-683d8c276a4a043d)

### path-011307

```text
(exec)# test cts role-based snmp mapping first <cr>
```

Handler ` RVA 0x1407C2C0 `；selector ` 0 `；EOL ` RVA 0x35CF6688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de454cc04f8d34de](../../evidence/conditions-sets-086.md#c-de454cc04f8d34de) · [状态效果 S-683d8c276a4a043d](../../evidence/state_effects-sets-022.md#s-683d8c276a4a043d)

### path-009561

```text
(exec)# test cts role-based sw-dp enable <cr>
```

Handler ` RVA 0x142353B0 `；selector ` 0 `；EOL ` RVA 0x35D069B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [状态效果 S-bec6518cd8b76cac](../../evidence/state_effects-sets-040.md#s-bec6518cd8b76cac)

### path-025164

```text
(exec)# test cts role-based sw-dp feature ipv4 in punt <?number_help_func_action@55558b25ae78> add <cr>
```

Handler ` RVA 0x142353B0 `；selector ` 1 `；EOL ` RVA 0x35D06F28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-247ec609d06adf6e](../../evidence/conditions-sets-014.md#c-247ec609d06adf6e) · [缺口 G-783cc8bbdf1b6ccb](../../evidence/gaps-sets-005.md#g-783cc8bbdf1b6ccb) · [状态效果 S-cb0e7097041650ae](../../evidence/state_effects-sets-043.md#s-cb0e7097041650ae)

### path-009350

```text
(exec)# test cts role-based sync <number:1..2147483647> <cr>
```

Handler ` RVA 0x1404B8A0 `；selector ` 8 `；EOL ` RVA 0x35CECA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of times to synchronize。

[条件 C-ef0b65519f7fb8dc](../../evidence/conditions-sets-092.md#c-ef0b65519f7fb8dc) · [参数 P-d4f39e730e109d93](../../evidence/parameters-sets-016.md#p-d4f39e730e109d93)

### path-006005

```text
(exec)# test cts sap enable <cr>
```

Handler ` RVA 0x13060720 `；selector ` 0 `；EOL ` RVA 0x35A1DD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-955c29ad44ebed5f](../../evidence/conditions-sets-058.md#c-955c29ad44ebed5f) · [状态效果 S-2fbedee1297ac377](../../evidence/state_effects-sets-011.md#s-2fbedee1297ac377)

### path-009287

```text
(exec)# test cts slist_mib del ste <cr>
```

Handler ` RVA 0x130F3EA0 `；selector ` 0 `；EOL ` RVA 0x35A46768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-448ea7d33637e6ad](../../evidence/conditions-sets-027.md#c-448ea7d33637e6ad) · [状态效果 S-25a5691fd747df7f](../../evidence/state_effects-sets-008.md#s-25a5691fd747df7f)

### path-011180

```text
(exec)# test cts sxp ipsgt action <number:0..2> <cr>
```

Handler ` RVA 0x13279440 `；selector ` 0 `；EOL ` RVA 0x35A53288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SNMP Action value。

[条件 C-18ef971313174e40](../../evidence/conditions-sets-010.md#c-18ef971313174e40) · [参数 P-09cbcd616efb3894](../../evidence/parameters-sets-001.md#p-09cbcd616efb3894) · [状态效果 S-0aab01b894068174](../../evidence/state_effects-sets-003.md#s-0aab01b894068174)

### path-004606

```text
(exec)# test cwoir incr_sync on <cr>
```

Handler ` RVA 0xED96790 `；selector ` 0 `；EOL ` RVA 0x34430918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-74a5e561127e28e6](../../evidence/state_effects-sets-025.md#s-74a5e561127e28e6)

### path-008236

```text
(exec)# test cwoir insert <number:1..13> <number:1..99> <cr>
```

Handler ` RVA 0xEDAEE90 `；selector ` 0 `；EOL ` RVA 0x3442F710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` card type (cwpa=15, cwatm=16, cwpos=17)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-bb83453e04561a3a](../../evidence/parameters-sets-014.md#p-bb83453e04561a3a)

### path-010539

```text
(exec)# test cwoir iosrunning <number:1..13> <number:0..1> <number:1..99> <cr>
```

Handler ` RVA 0xEDAEDD0 `；selector ` 0 `；EOL ` RVA 0x3442FE10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` cpu number；` unsigned_number ` card type (cwpa=15, cwatm=16, cwpos=17)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-041e16eff84e84cf](../../evidence/parameters-sets-001.md#p-041e16eff84e84cf)

### path-010533

```text
(exec)# test cwoir ipcready <number:1..13> <number:0..1> <number:0..3> <cr>
```

Handler ` RVA 0xEDAED10 `；selector ` 0 `；EOL ` RVA 0x3442FA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number；` unsigned_number ` cpu number；` unsigned_number ` swichover type。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-a6eb3d08caf0a08c](../../evidence/parameters-sets-013.md#p-a6eb3d08caf0a08c)

### path-000808

```text
(exec)# test cwoir read <cr>
```

Handler ` RVA 0xEDAEFB0 `；selector ` 0 `；EOL ` RVA 0x34430388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004544

```text
(exec)# test cwoir remove <number:1..13> <cr>
```

Handler ` RVA 0xEDAEF30 `；selector ` 0 `；EOL ` RVA 0x34430100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-9ca06d371d94a736](../../evidence/parameters-sets-012.md#p-9ca06d371d94a736)

### path-000838

```text
(exec)# test cwoir show <cr>
```

Handler ` RVA 0xEDAEFF0 `；selector ` 0 `；EOL ` RVA 0x34430630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-000292

```text
(exec)# test data-descriptor <cr>
```

Handler ` RVA 0xD550170 `；selector ` 0 `；EOL ` RVA 0x33E7FB68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0847434071cb57fd](../../evidence/conditions-sets-004.md#c-0847434071cb57fd)

### path-002051

```text
(exec)# test dhcp ns <cr>
```

Handler ` RVA 0xF4743A0 `；selector ` 0 `；EOL ` RVA 0x34652410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-002026

```text
(exec)# test dhcp release <cr>
```

Handler ` RVA 0xF4733F0 `；selector ` 0 `；EOL ` RVA 0x346518B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-14ed1e783a0b2b32](../../evidence/state_effects-sets-005.md#s-14ed1e783a0b2b32)

### path-025415

```text
(exec)# test diagnostic simulation failure slot <?option@5555898db9d0> test <?number_help_func_action@555589917be8> <cr>
```

Handler ` RVA 0xEB7FFE0 `；selector ` 0 `；EOL ` RVA 0x343C3CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d8f869e92c67fc8c](../../evidence/conditions-sets-084.md#c-d8f869e92c67fc8c) · [缺口 G-fa35fb9275f4c2a8](../../evidence/gaps-sets-009.md#g-fa35fb9275f4c2a8) · [状态效果 S-21016aded756b684](../../evidence/state_effects-sets-007.md#s-21016aded756b684)

### path-005344

```text
(exec)# test dmtm <number:0..64> cmd <cr>
```

Handler ` RVA 0x10C43D50 `；selector ` 0 `；EOL ` RVA 0x34CEBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot numbers (specify 0+ slots)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-0e7af595ea053c84](../../evidence/parameters-sets-002.md#p-0e7af595ea053c84) · [状态效果 S-81f0ef1a443e05ef](../../evidence/state_effects-sets-028.md#s-81f0ef1a443e05ef)

### path-008665

```text
(exec)# test dtp switch crash <number:0..3> <cr>
```

Handler ` RVA 0x15F15700 `；selector ` 0 `；EOL ` RVA 0x35E68DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` crash point:0-nocrash 1-reneg 2-compl 3-oper。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-576c7c500f9d549b](../../evidence/parameters-sets-007.md#p-576c7c500f9d549b)

### path-001157

```text
(exec)# test dwnld_mgr <string> <cr>
```

Handler ` RVA 0x10656760 `；selector ` 0 `；EOL ` RVA 0x34BDA0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` profile name。

[条件 C-78e45182aef430d9](../../evidence/conditions-sets-047.md#c-78e45182aef430d9) · [参数 P-0dadb8908436ba2e](../../evidence/parameters-sets-001.md#p-0dadb8908436ba2e)

### path-004419

```text
(exec)# test eci add <string> <cr>
```

Handler ` RVA 0xDF98570 `；selector ` 0 `；EOL ` RVA 0x340E2DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` file containing eci chain input。

[条件 C-4d3e9f24051795b2](../../evidence/conditions-sets-030.md#c-4d3e9f24051795b2) · [参数 P-87f51bdf5a11fcb0](../../evidence/parameters-sets-010.md#p-87f51bdf5a11fcb0)

### path-004403

```text
(exec)# test eci delete <string> <cr>
```

Handler ` RVA 0xDF97EA0 `；selector ` 0 `；EOL ` RVA 0x340E2AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` file containing eci chain input。

[条件 C-4d3e9f24051795b2](../../evidence/conditions-sets-030.md#c-4d3e9f24051795b2) · [参数 P-b0019edcb90aef5f](../../evidence/parameters-sets-013.md#p-b0019edcb90aef5f)

### path-000693

```text
(exec)# test eci scan <cr>
```

Handler ` RVA 0xDF986D0 `；selector ` 0 `；EOL ` RVA 0x340E30C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4d3e9f24051795b2](../../evidence/conditions-sets-030.md#c-4d3e9f24051795b2)

### path-008193

```text
(exec)# test eci set timeout <number:0..1000> <cr>
```

Handler ` RVA 0xDF988A0 `；selector ` 0 `；EOL ` RVA 0x340E33F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds to wait。

[条件 C-4d3e9f24051795b2](../../evidence/conditions-sets-030.md#c-4d3e9f24051795b2) · [参数 P-5e273781dbffcb2e](../../evidence/parameters-sets-008.md#p-5e273781dbffcb2e)

### path-000718

```text
(exec)# test eci show <cr>
```

Handler ` RVA 0xDF985D0 `；selector ` 0 `；EOL ` RVA 0x340E36C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4d3e9f24051795b2](../../evidence/conditions-sets-030.md#c-4d3e9f24051795b2)

### path-000309

```text
(exec)# test eem <cr>
```

Handler ` RVA 0x1107A0B0 `；selector ` 0 `；EOL ` RVA 0x35386950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001629

```text
(exec)# test eigrp SIA <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 105 `；EOL ` RVA 0x3469D878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd1c80468f73b53f](../../evidence/conditions-sets-098.md#c-fd1c80468f73b53f) · [状态效果 S-4828b182811ec5bf](../../evidence/state_effects-sets-016.md#s-4828b182811ec5bf)

### path-009051

```text
(exec)# test eigrp address-family ipv4 ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x346B9888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a332536b7e83dd25](../../evidence/conditions-sets-063.md#c-a332536b7e83dd25) · [状态效果 S-143dae196a1fa52d](../../evidence/state_effects-sets-005.md#s-143dae196a1fa52d)

### path-011082

```text
(exec)# test eigrp address-family ipv4 error-percent <number:0..100> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x346B9F98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-1c1b28fe640449c9](../../evidence/conditions-sets-011.md#c-1c1b28fe640449c9) · [参数 P-f2279363519f3eb4](../../evidence/parameters-sets-018.md#p-f2279363519f3eb4) · [状态效果 S-8686634775320f43](../../evidence/state_effects-sets-029.md#s-8686634775320f43)

### path-024010

```text
(exec)# test eigrp address-family ipv4 error-percent <number:0..100> <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x346B9F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-12b892af8cc3e7c9](../../evidence/conditions-sets-007.md#c-12b892af8cc3e7c9) · [缺口 G-b666d46d08e756b9](../../evidence/gaps-sets-006.md#g-b666d46d08e756b9) · [参数 P-0ed98bbe6cb039b5](../../evidence/parameters-sets-002.md#p-0ed98bbe6cb039b5) · [状态效果 S-8686634775320f43](../../evidence/state_effects-sets-029.md#s-8686634775320f43)

### path-009044

```text
(exec)# test eigrp address-family ipv6 ack <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 108 `；EOL ` RVA 0x35457E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4c83413d24593cd](../../evidence/conditions-sets-070.md#c-b4c83413d24593cd) · [状态效果 S-e43209b5083e6bb3](../../evidence/state_effects-sets-048.md#s-e43209b5083e6bb3)

### path-011081

```text
(exec)# test eigrp address-family ipv6 error-percent <number:0..100> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x35458518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-d2bbb8d7547372dd](../../evidence/conditions-sets-081.md#c-d2bbb8d7547372dd) · [参数 P-9704e8c7268e4d69](../../evidence/parameters-sets-012.md#p-9704e8c7268e4d69) · [状态效果 S-493ebd5badcb37c4](../../evidence/state_effects-sets-016.md#s-493ebd5badcb37c4)

### path-024007

```text
(exec)# test eigrp address-family ipv6 error-percent <number:0..100> <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 107 `；EOL ` RVA 0x35458518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Error percentage。

[条件 C-9a3cf170231fb3fe](../../evidence/conditions-sets-060.md#c-9a3cf170231fb3fe) · [缺口 G-44b8315ac1655495](../../evidence/gaps-sets-003.md#g-44b8315ac1655495) · [参数 P-db7f017bd84e4834](../../evidence/parameters-sets-017.md#p-db7f017bd84e4834) · [状态效果 S-493ebd5badcb37c4](../../evidence/state_effects-sets-016.md#s-493ebd5badcb37c4)

### path-001530

```text
(exec)# test eigrp crimson <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 106 `；EOL ` RVA 0x3469D428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7ddf978129a9f1d](../../evidence/conditions-sets-096.md#c-f7ddf978129a9f1d) · [状态效果 S-4828b182811ec5bf](../../evidence/state_effects-sets-016.md#s-4828b182811ec5bf)

### path-017858

```text
(exec)# test eigrp neighbor <interface> <address> <cr>
```

Handler ` RVA 0xF590F90 `；selector ` 0 `；EOL ` RVA 0x3469DEA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 Neighbor Address。

[条件 C-3f387c97c1c4dca8](../../evidence/conditions-sets-025.md#c-3f387c97c1c4dca8) · [缺口 G-5b4c0f1fa7f61a5a](../../evidence/gaps-sets-004.md#g-5b4c0f1fa7f61a5a) · [参数 P-6fec578f8498d521](../../evidence/parameters-sets-009.md#p-6fec578f8498d521) · [状态效果 S-4828b182811ec5bf](../../evidence/state_effects-sets-016.md#s-4828b182811ec5bf)

### path-010906

```text
(exec)# test ethernet errdisable recovery-timer unit second <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 0 `；EOL ` RVA 0x339882A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-79cde6b729464437](../../evidence/conditions-sets-047.md#c-79cde6b729464437) · [状态效果 S-231c91f30ef73f4b](../../evidence/state_effects-sets-008.md#s-231c91f30ef73f4b)

### path-021058

```text
(exec)# test ethernet l2ctrl safe-iteration vports <interface> <cr>
```

Handler ` RVA 0xC05DAC0 `；selector ` 0 `；EOL ` RVA 0x3398BB08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-921f8ce62ae9420f](../../evidence/conditions-sets-056.md#c-921f8ce62ae9420f) · [缺口 G-99af9ad78aebf475](../../evidence/gaps-sets-006.md#g-99af9ad78aebf475) · [参数 P-564e2f745bdafea1](../../evidence/parameters-sets-007.md#p-564e2f745bdafea1) · [状态效果 S-b281e72b4f3ece6c](../../evidence/state_effects-sets-038.md#s-b281e72b4f3ece6c)

### path-008806

```text
(exec)# test ethernet mirp-rcv isid <number:1..16777215> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 2 `；EOL ` RVA 0x33987DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` isid id。

[条件 C-e2f7e37c4570f32a](../../evidence/conditions-sets-087.md#c-e2f7e37c4570f32a) · [参数 P-e964ebd939a67768](../../evidence/parameters-sets-017.md#p-e964ebd939a67768)

### path-021547

```text
(exec)# test ethernet mlacp unknown interface <interface> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 3 `；EOL ` RVA 0x33987A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e33a12e91569686b](../../evidence/conditions-sets-088.md#c-e33a12e91569686b) · [缺口 G-1b2d9a673017c37a](../../evidence/gaps-sets-001.md#g-1b2d9a673017c37a) · [参数 P-4555fbb600f078f9](../../evidence/parameters-sets-006.md#p-4555fbb600f078f9) · [状态效果 S-3bfdb780c044af81](../../evidence/state_effects-sets-013.md#s-3bfdb780c044af81)

### path-017577

```text
(exec)# test ethernet mstp-tcn-enable <interface> <number:0..1> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 6 `；EOL ` RVA 0x339871A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Test value。

[条件 C-30c8b616d090f44c](../../evidence/conditions-sets-019.md#c-30c8b616d090f44c) · [缺口 G-b04d24ac69d96cde](../../evidence/gaps-sets-006.md#g-b04d24ac69d96cde) · [参数 P-1a3a2550c907e43a](../../evidence/parameters-sets-002.md#p-1a3a2550c907e43a)

### path-021532

```text
(exec)# test ethernet populate-statistics interface <interface> <number:1..16384> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 4 `；EOL ` RVA 0x339875D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance identifier。

[条件 C-8653592a182eb6da](../../evidence/conditions-sets-052.md#c-8653592a182eb6da) · [缺口 G-2aa7737c7d10dc6b](../../evidence/gaps-sets-002.md#g-2aa7737c7d10dc6b) · [参数 P-46c4b52712c73218](../../evidence/parameters-sets-006.md#p-46c4b52712c73218)

### path-005101

```text
(exec)# test ethernet safe-iteration <number:0..5> <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 5 `；EOL ` RVA 0x33986DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Test case number。

[条件 C-479499b36f577fc9](../../evidence/conditions-sets-028.md#c-479499b36f577fc9) · [参数 P-bd87e469a1d0f0e7](../../evidence/parameters-sets-014.md#p-bd87e469a1d0f0e7)

### path-021623

```text
(exec)# test ethernet stp-fwdstate <number:1..16384> <interface> disable <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 0 `；EOL ` RVA 0x339882A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance identifier。

[条件 C-744b8596ef981a10](../../evidence/conditions-sets-045.md#c-744b8596ef981a10) · [缺口 G-e199592ab58a2dc6](../../evidence/gaps-sets-008.md#g-e199592ab58a2dc6) · [参数 P-2d7fffaeea583df5](../../evidence/parameters-sets-004.md#p-2d7fffaeea583df5) · [状态效果 S-3c9414bd3a3252b2](../../evidence/state_effects-sets-013.md#s-3c9414bd3a3252b2)

### path-021624

```text
(exec)# test ethernet stp-fwdstate <number:1..16384> <interface> forwarding <cr>
```

Handler ` RVA 0xC037E10 `；selector ` 1 `；EOL ` RVA 0x339885C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance identifier。

[条件 C-7881c4b209eda5aa](../../evidence/conditions-sets-047.md#c-7881c4b209eda5aa) · [缺口 G-e199592ab58a2dc6](../../evidence/gaps-sets-008.md#g-e199592ab58a2dc6) · [参数 P-2d7fffaeea583df5](../../evidence/parameters-sets-004.md#p-2d7fffaeea583df5) · [状态效果 S-ab9e6db0775fe342](../../evidence/state_effects-sets-036.md#s-ab9e6db0775fe342)

### path-009113

```text
(exec)# test event manager ged define <cr>
```

Handler ` RVA 0x110CDE30 `；selector ` 0 `；EOL ` RVA 0x353A63D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d034565b3f514f1e](../../evidence/conditions-sets-080.md#c-d034565b3f514f1e)

### path-009123

```text
(exec)# test event manager ged publish <cr>
```

Handler ` RVA 0x110CDC70 `；selector ` 0 `；EOL ` RVA 0x353A6678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-256aad430549a571](../../evidence/conditions-sets-015.md#c-256aad430549a571)

### path-009129

```text
(exec)# test event manager ged subscribe <cr>
```

Handler ` RVA 0x110CDD70 `；selector ` 0 `；EOL ` RVA 0x353A6920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a5b238eb78e41aa](../../evidence/conditions-sets-060.md#c-9a5b238eb78e41aa)

### path-011087

```text
(exec)# test event manager ged unsubscribe <number:0..2147483647> <cr>
```

Handler ` RVA 0x110CDDD0 `；selector ` 0 `；EOL ` RVA 0x353A6C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` subscription id。

[条件 C-2423d7dbaa4e5f8f](../../evidence/conditions-sets-014.md#c-2423d7dbaa4e5f8f) · [参数 P-e54fd61c119df86e](../../evidence/parameters-sets-017.md#p-e54fd61c119df86e)

### path-006337

```text
(exec)# test flowspec client stop <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 1 `；EOL ` RVA 0x35A9B978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d8b4e60aa029bc2](../../evidence/conditions-sets-011.md#c-1d8b4e60aa029bc2)

### path-006267

```text
(exec)# test flowspec client xos <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 0 `；EOL ` RVA 0x35A9B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1c796e23081e6be7](../../evidence/conditions-sets-011.md#c-1c796e23081e6be7) · [状态效果 S-70bf2c4702a5858f](../../evidence/state_effects-sets-024.md#s-70bf2c4702a5858f)

### path-002414

```text
(exec)# test flowspec rt-dump <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 4 `；EOL ` RVA 0x35A9C2F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eb4ded426ba0b473](../../evidence/conditions-sets-091.md#c-eb4ded426ba0b473) · [状态效果 S-2643ea0b304b5d4a](../../evidence/state_effects-sets-009.md#s-2643ea0b304b5d4a)

### path-002391

```text
(exec)# test flowspec txlist-dump <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 5 `；EOL ` RVA 0x35A9C5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1202652d8296a4d0](../../evidence/conditions-sets-007.md#c-1202652d8296a4d0)

### path-002434

```text
(exec)# test flowspec xtf <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 2 `；EOL ` RVA 0x35A9BFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0aba5b8414a2c9fe](../../evidence/conditions-sets-004.md#c-0aba5b8414a2c9fe)

### path-006303

```text
(exec)# test flowspec xtf print <cr>
```

Handler ` RVA 0x134655F0 `；selector ` 3 `；EOL ` RVA 0x35A9BC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7db23d73666e7db1](../../evidence/conditions-sets-049.md#c-7db23d73666e7db1)

### path-001755

```text
(exec)# test fqdn <number:0..14> <cr>
```

Handler ` RVA 0xC2E4050 `；selector ` 5 `；EOL ` RVA 0x33A3DF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 0 to disable ut test flag, 1-14 to execute different ut cases。

[条件 C-4cd511929db3273f](../../evidence/conditions-sets-030.md#c-4cd511929db3273f) · [参数 P-c9a94d867a4371a2](../../evidence/parameters-sets-015.md#p-c9a94d867a4371a2)

### path-004740

```text
(exec)# test garp_retry add <address> <cr>
```

Handler ` RVA 0xCF73340 `；selector ` 0 `；EOL ` RVA 0x33D441B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` ip address。

[条件 C-27abeffed741c780](../../evidence/conditions-sets-016.md#c-27abeffed741c780) · [参数 P-e55458f9b27c5030](../../evidence/parameters-sets-017.md#p-e55458f9b27c5030) · [状态效果 S-d9ed925affcb9749](../../evidence/state_effects-sets-046.md#s-d9ed925affcb9749)

### path-008855

```text
(exec)# test glbp redundancy events enable <cr>
```

Handler ` RVA 0xE169F90 `；selector ` 50 `；EOL ` RVA 0x34224F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-4a2ff6a0c3466269](../../evidence/state_effects-sets-016.md#s-4a2ff6a0c3466269)

### path-023880

```text
(exec)# test glbp transport <interface> <number:0..1023> ipv6 <address> <cr>
```

Handler ` RVA 0xE169F90 `；selector ` 51 `；EOL ` RVA 0x34224B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number；` address ` IPv6 address。

[条件 C-32d74f34c984bd69](../../evidence/conditions-sets-020.md#c-32d74f34c984bd69) · [缺口 G-1a7b639af7992f5f](../../evidence/gaps-sets-001.md#g-1a7b639af7992f5f) · [参数 P-7ac840779107458d](../../evidence/parameters-sets-010.md#p-7ac840779107458d) · [状态效果 S-5278a1e5fcab078f](../../evidence/state_effects-sets-018.md#s-5278a1e5fcab078f)

### path-011225

```text
(exec)# test gsi httpc <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 0 `；EOL ` RVA 0x346228C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-d5031aa979f9915f](../../evidence/state_effects-sets-045.md#s-d5031aa979f9915f)

### path-009410

```text
(exec)# test gsi httpc <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 0 `；EOL ` RVA 0x346225B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-797c33550bf9bd5f](../../evidence/state_effects-sets-026.md#s-797c33550bf9bd5f)

### path-011844

```text
(exec)# test gsi httpc <number:0..9> start <string> post <cr>
```

Handler ` RVA 0xF3B2930 `；selector ` 0 `；EOL ` RVA 0x34621F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-a85c754192468da0](../../evidence/parameters-sets-013.md#p-a85c754192468da0) · [状态效果 S-b8ae2a991a2a55f8](../../evidence/state_effects-sets-039.md#s-b8ae2a991a2a55f8)

### path-009449

```text
(exec)# test gsi httpc <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 0 `；EOL ` RVA 0x34622BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-98b65764ba5cdb09](../../evidence/parameters-sets-012.md#p-98b65764ba5cdb09) · [状态效果 S-2f5756cab9615b5a](../../evidence/state_effects-sets-010.md#s-2f5756cab9615b5a)

### path-006242

```text
(exec)# test gsi httpc stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 0 `；EOL ` RVA 0x34622280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-797c33550bf9bd5f](../../evidence/state_effects-sets-026.md#s-797c33550bf9bd5f)

### path-011214

```text
(exec)# test gsi https <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 1 `；EOL ` RVA 0x346215E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-32f23c47c782c74d](../../evidence/state_effects-sets-011.md#s-32f23c47c782c74d)

### path-009397

```text
(exec)# test gsi https <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 1 `；EOL ` RVA 0x346212D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-c642ed0c13d3051a](../../evidence/state_effects-sets-042.md#s-c642ed0c13d3051a)

### path-012039

```text
(exec)# test gsi https <number:0..9> start <string> encrypt post <cr>
```

Handler ` RVA 0xF3B2A20 `；selector ` 0 `；EOL ` RVA 0x34620AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-49005321df5f5cf4](../../evidence/parameters-sets-006.md#p-49005321df5f5cf4) · [状态效果 S-6fa929c68c64704d](../../evidence/state_effects-sets-024.md#s-6fa929c68c64704d)

### path-009428

```text
(exec)# test gsi https <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 1 `；EOL ` RVA 0x346218E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-85bb7d9d00437dea](../../evidence/parameters-sets-010.md#p-85bb7d9d00437dea) · [状态效果 S-701a646b65013869](../../evidence/state_effects-sets-024.md#s-701a646b65013869)

### path-006213

```text
(exec)# test gsi https stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 1 `；EOL ` RVA 0x34620FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-c642ed0c13d3051a](../../evidence/state_effects-sets-042.md#s-c642ed0c13d3051a)

### path-011204

```text
(exec)# test gsi sshc <number:0..9> debug off <cr>
```

Handler ` RVA 0xF3B0380 `；selector ` 2 `；EOL ` RVA 0x34620068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-54e5095c8b586166](../../evidence/state_effects-sets-018.md#s-54e5095c8b586166)

### path-009383

```text
(exec)# test gsi sshc <number:0..9> show <cr>
```

Handler ` RVA 0xF3B0610 `；selector ` 2 `；EOL ` RVA 0x3461FD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-0f8277821064c1d4](../../evidence/state_effects-sets-004.md#s-0f8277821064c1d4)

### path-011842

```text
(exec)# test gsi sshc <number:0..9> start <string> wsma <cr>
```

Handler ` RVA 0xF3B10E0 `；selector ` 0 `；EOL ` RVA 0x3461F6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number；` string ` URL to use。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-0608e1b131dc833a](../../evidence/parameters-sets-001.md#p-0608e1b131dc833a) · [状态效果 S-87a2e86cc854b65e](../../evidence/state_effects-sets-029.md#s-87a2e86cc854b65e)

### path-009413

```text
(exec)# test gsi sshc <number:0..9> xml-header <cr>
```

Handler ` RVA 0xF3B09C0 `；selector ` 2 `；EOL ` RVA 0x34620360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` instance number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-db878564e0d39553](../../evidence/parameters-sets-017.md#p-db878564e0d39553) · [状态效果 S-a430d111c2cae1fa](../../evidence/state_effects-sets-035.md#s-a430d111c2cae1fa)

### path-006186

```text
(exec)# test gsi sshc stop <cr>
```

Handler ` RVA 0xF3B0E90 `；selector ` 2 `；EOL ` RVA 0x3461FA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-0f8277821064c1d4](../../evidence/state_effects-sets-004.md#s-0f8277821064c1d4)

### path-005494

```text
(exec)# test gssapi init_sec_context <string> <cr>
```

Handler ` RVA 0xC3DCF70 `；selector ` 1 `；EOL ` RVA 0x33A66FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The server name or target name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-43e4e0daf266aaf3](../../evidence/parameters-sets-006.md#p-43e4e0daf266aaf3)

### path-011076

```text
(exec)# test gssapi token_exchange no_wrap <address> <string> <cr>
```

Handler ` RVA 0xC3DCF70 `；selector ` 2 `；EOL ` RVA 0x33A673D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote hostname or IP address；` string ` The server name or target name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-fd7d94e1b385dba2](../../evidence/parameters-sets-019.md#p-fd7d94e1b385dba2) · [状态效果 S-f9df264d26b77615](../../evidence/state_effects-sets-053.md#s-f9df264d26b77615)

### path-009753

```text
(exec)# test gx access-accept service <string> <cr>
```

Handler ` RVA 0xBD23280 `；selector ` 1 `；EOL ` RVA 0x338C3BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Service name。

[条件 C-da0c66082fa4750c](../../evidence/conditions-sets-084.md#c-da0c66082fa4750c) · [参数 P-62d5f9834b5f4036](../../evidence/parameters-sets-008.md#p-62d5f9834b5f4036) · [状态效果 S-203f5d6cfbf6644c](../../evidence/state_effects-sets-007.md#s-203f5d6cfbf6644c)

### path-002600

```text
(exec)# test gx access-reject <cr>
```

Handler ` RVA 0xBD23380 `；selector ` 1 `；EOL ` RVA 0x338C3E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da0c66082fa4750c](../../evidence/conditions-sets-084.md#c-da0c66082fa4750c)

### path-025383

```text
(exec)# test gx create-session ip <address> mac <hex-data> vrf <string> vlan-id <string> <interface> client-handle <number:1000..2000> <cr>
```

Handler ` RVA 0xBD21B90 `；selector ` 1 `；EOL ` RVA 0x338C2940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the subscriber；` unsigned_number ` Client Handle limit。

[条件 C-9ff71922f6acde77](../../evidence/conditions-sets-062.md#c-9ff71922f6acde77) · [缺口 G-672d03da2093e5cd](../../evidence/gaps-sets-004.md#g-672d03da2093e5cd) · [参数 P-ca5b96fd1ea8020b](../../evidence/parameters-sets-015.md#p-ca5b96fd1ea8020b) · [状态效果 S-a81ec50ffa56e676](../../evidence/state_effects-sets-036.md#s-a81ec50ffa56e676)

### path-009744

```text
(exec)# test gx delete-session ip <address> <cr>
```

Handler ` RVA 0xBD21FF0 `；selector ` 1 `；EOL ` RVA 0x338C2DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of the subscriber。

[条件 C-da0c66082fa4750c](../../evidence/conditions-sets-084.md#c-da0c66082fa4750c) · [参数 P-e8e8b1f79c8c540d](../../evidence/parameters-sets-017.md#p-e8e8b1f79c8c540d) · [状态效果 S-ad364191fd691c85](../../evidence/state_effects-sets-037.md#s-ad364191fd691c85)

### path-002527

```text
(exec)# test gx enable <cr>
```

Handler ` RVA 0xBD20610 `；selector ` 0 `；EOL ` RVA 0x338C2268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8d7847a9c5084c63](../../evidence/conditions-sets-055.md#c-8d7847a9c5084c63) · [状态效果 S-de32e6dec54a8e90](../../evidence/state_effects-sets-047.md#s-de32e6dec54a8e90)

### path-011874

```text
(exec)# test gx rar-sb session-id <number:1..4294967295> install-service <string> <cr>
```

Handler ` RVA 0xBD23560 `；selector ` 1 `；EOL ` RVA 0x338C4328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session id；` string ` Service name。

[条件 C-da0c66082fa4750c](../../evidence/conditions-sets-084.md#c-da0c66082fa4750c) · [参数 P-b0c10cbbfe902699](../../evidence/parameters-sets-013.md#p-b0c10cbbfe902699) · [状态效果 S-1474c52917781af7](../../evidence/state_effects-sets-005.md#s-1474c52917781af7)

### path-025167

```text
(exec)# test gx update-session id ip <address> data <interface> client-handle <number:1000..2000> <cr>
```

Handler ` RVA 0xBD22230 `；selector ` 1 `；EOL ` RVA 0x338C3688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the subscriber；` unsigned_number ` Client Handle limit。

[条件 C-048f9eb158bd8063](../../evidence/conditions-sets-002.md#c-048f9eb158bd8063) · [缺口 G-5bea4dc6e83c4cc9](../../evidence/gaps-sets-004.md#g-5bea4dc6e83c4cc9) · [参数 P-8e34add9c2a6d6d5](../../evidence/parameters-sets-011.md#p-8e34add9c2a6d6d5) · [状态效果 S-afab03b959af5a61](../../evidence/state_effects-sets-037.md#s-afab03b959af5a61)

### path-010593

```text
(exec)# test hsrp ha sync mac enable <cr>
```

Handler ` RVA 0xD321940 `；selector ` 50 `；EOL ` RVA 0x33E15B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-410e1415b5ff30ab](../../evidence/state_effects-sets-014.md#s-410e1415b5ff30ab)

### path-024604

```text
(exec)# test hw-module subslot <?slotcard_func_action@5555899c11b0> all async loopback enable <cr>
```

Handler ` RVA 0x15B6D850 `；selector ` 0 `；EOL ` RVA 0x35DEF4D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f6b770f1118f9081](../../evidence/conditions-sets-095.md#c-f6b770f1118f9081) · [缺口 G-bee7e332974cad0b](../../evidence/gaps-sets-007.md#g-bee7e332974cad0b) · [状态效果 S-5aa3eb73774aeb61](../../evidence/state_effects-sets-020.md#s-5aa3eb73774aeb61)

### path-024615

```text
(exec)# test hw-module subslot <?slotcard_func_action@5555899c11b0> all cwan message gsm-profile-get <cr>
```

Handler ` RVA 0x15B0B5D0 `；selector ` 0 `；EOL ` RVA 0x35DE9C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ebc6bf64663cd536](../../evidence/conditions-sets-091.md#c-ebc6bf64663cd536) · [缺口 G-bee7e332974cad0b](../../evidence/gaps-sets-007.md#g-bee7e332974cad0b) · [状态效果 S-b9b0914ff09b2db0](../../evidence/state_effects-sets-039.md#s-b9b0914ff09b2db0)

### path-001819

```text
(exec)# test idmgr init <cr>
```

Handler ` RVA 0xE1926E0 `；selector ` 0 `；EOL ` RVA 0x3422BCB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-01b42f25268e460f](../../evidence/state_effects-sets-001.md#s-01b42f25268e460f)

### path-011800

```text
(exec)# test idmgr req-type session-assert key-list <string> data-list <cr>
```

Handler ` RVA 0xE1926E0 `；selector ` 0 `；EOL ` RVA 0x3422C0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of Attribute list。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-04fef1596abad51d](../../evidence/parameters-sets-001.md#p-04fef1596abad51d) · [状态效果 S-b114a157f9fbeb66](../../evidence/state_effects-sets-038.md#s-b114a157f9fbeb66)

### path-011117

```text
(exec)# test ifs appn read <address> <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 1 `；EOL ` RVA 0x33EC2460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` string ` Filename only。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-727d586e085e9dc5](../../evidence/parameters-sets-009.md#p-727d586e085e9dc5)

### path-011121

```text
(exec)# test ifs appn write <address> <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 2 `；EOL ` RVA 0x33EC2760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` string ` Filename only。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-9696f29e228907e8](../../evidence/parameters-sets-012.md#p-9696f29e228907e8)

### path-005902

```text
(exec)# test ifs boot <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 3 `；EOL ` RVA 0x33EC2A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Remainder of the bootstrap 'boot' command。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f0def853533d3d07](../../evidence/parameters-sets-018.md#p-f0def853533d3d07)

### path-002091

```text
(exec)# test ifs defaults <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 4 `；EOL ` RVA 0x33EC2CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-009278

```text
(exec)# test ifs disk cluster <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 8 `；EOL ` RVA 0x33EC39F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-efdb0d55b0727b4f](../../evidence/parameters-sets-018.md#p-efdb0d55b0727b4f)

### path-009291

```text
(exec)# test ifs disk modes <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 9 `；EOL ` RVA 0x33EC3CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-9c06b36a6a837b34](../../evidence/parameters-sets-012.md#p-9c06b36a6a837b34)

### path-009268

```text
(exec)# test ifs disk rdwr <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 7 `；EOL ` RVA 0x33EC3710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for disk file。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-c0576a6ad695a918](../../evidence/parameters-sets-015.md#p-c0576a6ad695a918)

### path-005981

```text
(exec)# test ifs show hidden <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 5 `；EOL ` RVA 0x33EC33D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-006063

```text
(exec)# test ifs slot <string> <cr>
```

Handler ` RVA 0xD65FD60 `；selector ` 6 `；EOL ` RVA 0x33EC3018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` URL for slot core destination。

[条件 C-33ff0814f99a84d5](../../evidence/conditions-sets-020.md#c-33ff0814f99a84d5) · [参数 P-dd661fa056efeb7f](../../evidence/parameters-sets-017.md#p-dd661fa056efeb7f) · [状态效果 S-0bc26b65d70a8263](../../evidence/state_effects-sets-003.md#s-0bc26b65d70a8263)

### path-025315

```text
(exec)# test install <string> <url:dynamic> <?url_prefix_action@55558b337468> <cr>
```

Handler ` RVA 0x15A6C9C0 `；selector ` 0 `；EOL ` RVA 0x35DE34E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-4b3c4aaf92353b81](../../evidence/conditions-sets-030.md#c-4b3c4aaf92353b81) · [缺口 G-8a52c413254bff3b](../../evidence/gaps-sets-005.md#g-8a52c413254bff3b) · [参数 P-da0a1e05cda2a7ed](../../evidence/parameters-sets-016.md#p-da0a1e05cda2a7ed)

### path-000139

```text
(exec)# test interfaces <cr>
```

Handler ` RVA 0xE8F4F60 `；selector ` 0 `；EOL ` RVA 0x3433F348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4083dcd77759bd87](../../evidence/conditions-sets-025.md#c-4083dcd77759bd87)

### path-012378

```text
(exec)# test interfaces <interface> <cr>
```

Handler ` RVA 0xE8F4F60 `；selector ` 0 `；EOL ` RVA 0x3433F348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dc4fb4365b8d9b33](../../evidence/conditions-sets-085.md#c-dc4fb4365b8d9b33) · [缺口 G-57b7b4a38f996144](../../evidence/gaps-sets-004.md#g-57b7b4a38f996144) · [参数 P-cd39dfba9be5979d](../../evidence/parameters-sets-016.md#p-cd39dfba9be5979d)

### path-011656

```text
(exec)# test ip access-list dynamic delete <number:100..199> <number:1..262144> <cr>
```

Handler ` RVA 0xCF06CB0 `；selector ` 0 `；EOL ` RVA 0x33D565B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Extended ACL；` unsigned_number ` handle。

[条件 C-551b49b00f8abec5](../../evidence/conditions-sets-033.md#c-551b49b00f8abec5) · [参数 P-891680d3d0bbb4cb](../../evidence/parameters-sets-011.md#p-891680d3d0bbb4cb) · [状态效果 S-1f21182584faff3d](../../evidence/state_effects-sets-007.md#s-1f21182584faff3d)

### path-010588

```text
(exec)# test ip access-list dynamic empty <number:100..199> <cr>
```

Handler ` RVA 0xCF073F0 `；selector ` 0 `；EOL ` RVA 0x33D560A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Extended ACL。

[条件 C-551b49b00f8abec5](../../evidence/conditions-sets-033.md#c-551b49b00f8abec5) · [参数 P-3210d07544b61f37](../../evidence/parameters-sets-004.md#p-3210d07544b61f37)

### path-004696

```text
(exec)# test ip access-list register <cr>
```

Handler ` RVA 0xCF065A0 `；selector ` 0 `；EOL ` RVA 0x33D56DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b1a4ad3067fe20b](../../evidence/conditions-sets-011.md#c-1b1a4ad3067fe20b) · [状态效果 S-9c57c46577e91c20](../../evidence/state_effects-sets-033.md#s-9c57c46577e91c20)

### path-011982

```text
(exec)# test ip dhcp api pool <string> <string> create <cr>
```

Handler ` RVA 0xD2C3400 `；selector ` 0 `；EOL ` RVA 0x33DD7270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name；` string ` Pool owner name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-07dc240d29126b32](../../evidence/parameters-sets-001.md#p-07dc240d29126b32) · [状态效果 S-dfcfda23b02b708f](../../evidence/state_effects-sets-047.md#s-dfcfda23b02b708f)

### path-008628

```text
(exec)# test ip dhcp query <address> <cr>
```

Handler ` RVA 0xD250100 `；selector ` 0 `；EOL ` RVA 0x33DD6E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Client IP address。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-e83f674c88cc9462](../../evidence/parameters-sets-017.md#p-e83f674c88cc9462)

### path-008586

```text
(exec)# test ip dhcp terminate <address> <cr>
```

Handler ` RVA 0xD250060 `；selector ` 0 `；EOL ` RVA 0x33DD6AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Client IP address。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-3b4645e85fd16383](../../evidence/parameters-sets-005.md#p-3b4645e85fd16383)

### path-010664

```text
(exec)# test ip domain apis <address> <string> <cr>
```

Handler ` RVA 0xD139D60 `；selector ` 0 `；EOL ` RVA 0x33D96B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Host IP address；` string ` VRF name。

[条件 C-2ff90d17642c5632](../../evidence/conditions-sets-019.md#c-2ff90d17642c5632) · [参数 P-787fba5cde6b4234](../../evidence/parameters-sets-009.md#p-787fba5cde6b4234)

### path-004807

```text
(exec)# test ip domain default-domain <cr>
```

Handler ` RVA 0xD139380 `；selector ` 0 `；EOL ` RVA 0x33D95E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05df1117dd3b590f](../../evidence/conditions-sets-003.md#c-05df1117dd3b590f)

### path-008546

```text
(exec)# test ip domain get-ipv4-server <number:0..25> <cr>
```

Handler ` RVA 0xD139580 `；selector ` 0 `；EOL ` RVA 0x33D967E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Server index。

[条件 C-dd51a3b79305276e](../../evidence/conditions-sets-085.md#c-dd51a3b79305276e) · [参数 P-64d2f2e2a2204061](../../evidence/parameters-sets-008.md#p-64d2f2e2a2204061)

### path-008533

```text
(exec)# test ip domain get-server <number:0..25> <cr>
```

Handler ` RVA 0xD139440 `；selector ` 0 `；EOL ` RVA 0x33D964F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Server index。

[条件 C-af9de867f199a062](../../evidence/conditions-sets-068.md#c-af9de867f199a062) · [参数 P-a508c7655a359164](../../evidence/parameters-sets-013.md#p-a508c7655a359164)

### path-008650

```text
(exec)# test ip domain lookup <address> <cr>
```

Handler ` RVA 0xD137930 `；selector ` 0 `；EOL ` RVA 0x33D972D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address。

[条件 C-3859b2b7a525681b](../../evidence/conditions-sets-022.md#c-3859b2b7a525681b) · [参数 P-b70e952a38201f2e](../../evidence/parameters-sets-014.md#p-b70e952a38201f2e)

### path-008613

```text
(exec)# test ip domain mcast-lookup <address> <cr>
```

Handler ` RVA 0xD140A70 `；selector ` 0 `；EOL ` RVA 0x33D976F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address。

[条件 C-f5feb5db7431e15b](../../evidence/conditions-sets-095.md#c-f5feb5db7431e15b) · [参数 P-c09f62870a65c5cd](../../evidence/parameters-sets-015.md#p-c09f62870a65c5cd)

### path-011668

```text
(exec)# test ip domain name-delete <string> <number:1..255> <number:1..4194304> <cr>
```

Handler ` RVA 0xD139670 `；selector ` 0 `；EOL ` RVA 0x33D96200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname；` unsigned_number ` Namekind；` unsigned_number ` Type。

[条件 C-53d8ba3c400737f5](../../evidence/conditions-sets-033.md#c-53d8ba3c400737f5) · [参数 P-e34808f4aca9e093](../../evidence/parameters-sets-017.md#p-e34808f4aca9e093)

### path-008485

```text
(exec)# test ip multicast sync resume <cr>
```

Handler ` RVA 0xD470550 `；selector ` 1 `；EOL ` RVA 0x33E51598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008466

```text
(exec)# test ip multicast sync suspend <cr>
```

Handler ` RVA 0xD470550 `；selector ` 0 `；EOL ` RVA 0x33E512F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008559

```text
(exec)# test ip nat clear translations <cr>
```

Handler ` RVA 0xFA39690 `；selector ` 0 `；EOL ` RVA 0x347DE818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004960

```text
(exec)# test ip nat dump <cr>
```

Handler ` RVA 0xFA39B10 `；selector ` 0 `；EOL ` RVA 0x347DF4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-5e7c42cdd4d48fde](../../evidence/state_effects-sets-020.md#s-5e7c42cdd4d48fde)

### path-008606

```text
(exec)# test ip nat portmap trans_report <cr>
```

Handler ` RVA 0xFA39700 `；selector ` 0 `；EOL ` RVA 0x347DEDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-d64463ffbb437085](../../evidence/state_effects-sets-045.md#s-d64463ffbb437085)

### path-010683

```text
(exec)# test ip nat show pool <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 0 `；EOL ` RVA 0x347DDF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-5f0173fb2c325d8c](../../evidence/conditions-sets-037.md#c-5f0173fb2c325d8c) · [参数 P-2fc9437051580fb2](../../evidence/parameters-sets-004.md#p-2fc9437051580fb2)

### path-010649

```text
(exec)# test ip nat show pool all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 1 `；EOL ` RVA 0x347DDC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-010698

```text
(exec)# test ip nat show rule <string> <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 2 `；EOL ` RVA 0x347DE508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Rule name。

[条件 C-75bc5b06ca4e328f](../../evidence/conditions-sets-046.md#c-75bc5b06ca4e328f) · [参数 P-83418bd3b9811e31](../../evidence/parameters-sets-010.md#p-83418bd3b9811e31)

### path-010665

```text
(exec)# test ip nat show rule all <cr>
```

Handler ` RVA 0xFA38D50 `；selector ` 3 `；EOL ` RVA 0x347DE208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004852

```text
(exec)# test ip nat-route database <cr>
```

Handler ` RVA 0x13725FC0 `；selector ` 0 `；EOL ` RVA 0x35C0F330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-cd585c95ee81edee](../../evidence/state_effects-sets-043.md#s-cd585c95ee81edee)

### path-008567

```text
(exec)# test ip nbar batch-config end <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 5 `；EOL ` RVA 0x35259330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008547

```text
(exec)# test ip nbar batch-config start <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 4 `；EOL ` RVA 0x35259088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008578

```text
(exec)# test ip nbar byte-count-window disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 9 `；EOL ` RVA 0x352596A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-2310be6e66048f93](../../evidence/state_effects-sets-008.md#s-2310be6e66048f93)

### path-008491

```text
(exec)# test ip nbar caches clear <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 29 `；EOL ` RVA 0x35255258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-010608

```text
(exec)# test ip nbar caches export <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 28 `；EOL ` RVA 0x35254FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-3b46f8fae4be42bd](../../evidence/parameters-sets-005.md#p-3b46f8fae4be42bd)

### path-010599

```text
(exec)# test ip nbar caches import <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 27 `；EOL ` RVA 0x35254CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-693dea4536eeb117](../../evidence/parameters-sets-008.md#p-693dea4536eeb117)

### path-008507

```text
(exec)# test ip nbar caches show <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 30 `；EOL ` RVA 0x35255500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008588

```text
(exec)# test ip nbar cedge-simulation disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 11 `；EOL ` RVA 0x35259C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008574

```text
(exec)# test ip nbar cedge-simulation enable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 10 `；EOL ` RVA 0x352599D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008500

```text
(exec)# test ip nbar config-mode async <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 8 `；EOL ` RVA 0x35257498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008513

```text
(exec)# test ip nbar config-mode sync <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 7 `；EOL ` RVA 0x35257740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-011681

```text
(exec)# test ip nbar dataplane-info-monitor memory-thresholds low <number:1..100> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 14 `；EOL ` RVA 0x3525A618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Low threshold in percents。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-2360135968ca2bc4](../../evidence/parameters-sets-003.md#p-2360135968ca2bc4)

### path-010707

```text
(exec)# test ip nbar dataplane-info-monitor traffic-over-subscription-state false <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 12 `；EOL ` RVA 0x3525A290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-010690

```text
(exec)# test ip nbar dataplane-info-monitor traffic-over-subscription-state true <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 13 `；EOL ` RVA 0x35259FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-024636

```text
(exec)# test ip nbar field-extraction disable <string> <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 1 `；EOL ` RVA 0x35258520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name；` string ` Field Name。

[条件 C-9ccbbe1153fa0f73](../../evidence/conditions-sets-061.md#c-9ccbbe1153fa0f73) · [缺口 G-cd951a775f374281](../../evidence/gaps-sets-007.md#g-cd951a775f374281) · [参数 P-94dc6b02cb1e9c89](../../evidence/parameters-sets-011.md#p-94dc6b02cb1e9c89)

### path-024635

```text
(exec)# test ip nbar field-extraction enable <string> <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 0 `；EOL ` RVA 0x35258120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name；` string ` Field Name。

[条件 C-39df0f65d528e864](../../evidence/conditions-sets-022.md#c-39df0f65d528e864) · [缺口 G-633b3ee2b75a9955](../../evidence/gaps-sets-004.md#g-633b3ee2b75a9955) · [参数 P-15e5eefa6e6d1241](../../evidence/parameters-sets-002.md#p-15e5eefa6e6d1241)

### path-008529

```text
(exec)# test ip nbar function <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 6 `；EOL ` RVA 0x35257AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Function name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-4af9a509018bb542](../../evidence/parameters-sets-006.md#p-4af9a509018bb542)

### path-008483

```text
(exec)# test ip nbar npc disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 19 `；EOL ` RVA 0x35255B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-010617

```text
(exec)# test ip nbar npc enable <string> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 18 `；EOL ` RVA 0x352558E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` File name to load (json format)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-b8c3dd324e3e92e2](../../evidence/parameters-sets-014.md#p-b8c3dd324e3e92e2)

### path-010626

```text
(exec)# test ip nbar npc pack-mode allow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 21 `；EOL ` RVA 0x35256120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-010634

```text
(exec)# test ip nbar npc pack-mode disallow <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 22 `；EOL ` RVA 0x352563C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008504

```text
(exec)# test ip nbar npc save <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 20 `；EOL ` RVA 0x35255E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-023537

```text
(exec)# test ip nbar per-txn disable <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 3 `；EOL ` RVA 0x35258D48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name。

[条件 C-60afb10f540abb0c](../../evidence/conditions-sets-038.md#c-60afb10f540abb0c) · [缺口 G-8877933b2961233b](../../evidence/gaps-sets-005.md#g-8877933b2961233b) · [参数 P-fc8a54166f8fe8f7](../../evidence/parameters-sets-019.md#p-fc8a54166f8fe8f7)

### path-023524

```text
(exec)# test ip nbar per-txn enable <string> <interface> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 2 `；EOL ` RVA 0x35258988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Protocol Name。

[条件 C-11d173682e11325c](../../evidence/conditions-sets-007.md#c-11d173682e11325c) · [缺口 G-bd7ba8dcf14b9128](../../evidence/gaps-sets-007.md#g-bd7ba8dcf14b9128) · [参数 P-0f9162a8201fad4e](../../evidence/parameters-sets-002.md#p-0f9162a8201fad4e)

### path-023684

```text
(exec)# test ip nbar resources flow max-session <number:dynamic> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 7 `；EOL ` RVA 0x3525B6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of Session 。

[条件 C-71cc1e62dbbdd18f](../../evidence/conditions-sets-044.md#c-71cc1e62dbbdd18f) · [缺口 G-ff61c9cb02187930](../../evidence/gaps-sets-009.md#g-ff61c9cb02187930) · [参数 P-0371b5c114cf1601](../../evidence/parameters-sets-001.md#p-0371b5c114cf1601)

### path-023702

```text
(exec)# test ip nbar resources protocol <number:1..100000000> <?option@55558a7af308> <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 1 `；EOL ` RVA 0x3525B3E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Link age greater than system link age (secs.)。

[条件 C-c694815929270ed5](../../evidence/conditions-sets-076.md#c-c694815929270ed5) · [缺口 G-00e7d5557b85ef27](../../evidence/gaps-sets-001.md#g-00e7d5557b85ef27) · [参数 P-69e4dd58e3555f6a](../../evidence/parameters-sets-008.md#p-69e4dd58e3555f6a)

### path-008600

```text
(exec)# test ip nbar set-max-protocol-id-no-cloud_ext <number:0..32767> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 15 `；EOL ` RVA 0x3525A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max protocol id without cloud extension。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-507a9096f4509329](../../evidence/parameters-sets-007.md#p-507a9096f4509329)

### path-010717

```text
(exec)# test ip nbar set-protocol-feature-support <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 16 `；EOL ` RVA 0x3525AC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Feature id；` unsigned_number ` Feature value。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-bdb8d401bdc33739](../../evidence/parameters-sets-014.md#p-bdb8d401bdc33739)

### path-004999

```text
(exec)# test ip nbar show-features-activation <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 17 `；EOL ` RVA 0x3525AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004976

```text
(exec)# test ip nbar show-fib-ad-info <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 31 `；EOL ` RVA 0x3525BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008502

```text
(exec)# test ip nbar track-ip disable <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 24 `；EOL ` RVA 0x35256C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-012200

```text
(exec)# test ip nbar track-ip enable <string> port <number:0..4294967295> vrf-id <number:0..4294967295> l4-proto <number:0..255> memory-size <number:0..20000> <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 23 `；EOL ` RVA 0x35256978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPv4/v6 to track；` unsigned_number ` port number；` unsigned_number ` VRF id；` unsigned_number ` L4 Protocol；` unsigned_number ` memory size in KB。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-74d155980cc4da67](../../evidence/parameters-sets-009.md#p-74d155980cc4da67)

### path-008515

```text
(exec)# test ip nbar track-ip flush <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 25 `；EOL ` RVA 0x35256ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008525

```text
(exec)# test ip nbar track-ip status <cr>
```

Handler ` RVA 0x10F37220 `；selector ` 26 `；EOL ` RVA 0x35257180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004863

```text
(exec)# test ip omp flush <cr>
```

Handler ` RVA 0x137422E0 `；selector ` 0 `；EOL ` RVA 0x35C105C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-336c162ed488efdc](../../evidence/conditions-sets-020.md#c-336c162ed488efdc) · [状态效果 S-e42b6ce1c94ce1e4](../../evidence/state_effects-sets-048.md#s-e42b6ce1c94ce1e4)

### path-017178

```text
(exec)# test ip pbr enqueue <interface> <cr>
```

Handler ` RVA 0x10C6F3F0 `；selector ` 0 `；EOL ` RVA 0x34CF0960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9a2921508a1500bf](../../evidence/conditions-sets-060.md#c-9a2921508a1500bf) · [缺口 G-c4fb390967749761](../../evidence/gaps-sets-007.md#g-c4fb390967749761) · [参数 P-a2ddcf5466c5f96e](../../evidence/parameters-sets-012.md#p-a2ddcf5466c5f96e) · [状态效果 S-1c3df31263b22bfc](../../evidence/state_effects-sets-006.md#s-1c3df31263b22bfc)

### path-008433

```text
(exec)# test ip pbr ipv6 attach <cr>
```

Handler ` RVA 0x10C6E4E0 `；selector ` 0 `；EOL ` RVA 0x34CF0520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5ec6ae704382b2d](../../evidence/conditions-sets-064.md#c-a5ec6ae704382b2d) · [状态效果 S-d0e6cacfa2a88fb9](../../evidence/state_effects-sets-044.md#s-d0e6cacfa2a88fb9)

### path-008418

```text
(exec)# test ip pbr map <string> <cr>
```

Handler ` RVA 0x10C6E570 `；selector ` 0 `；EOL ` RVA 0x34CF0228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` PBR route-map name。

[条件 C-a5ec6ae704382b2d](../../evidence/conditions-sets-064.md#c-a5ec6ae704382b2d) · [参数 P-e93b53fee09f3a16](../../evidence/parameters-sets-017.md#p-e93b53fee09f3a16)

### path-023494

```text
(exec)# test ip rib api iprib_get_route <?ipaddrmask_action@55558978f690> exact_match <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 1 `；EOL ` RVA 0x3423B738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-083a1b0fc41c3b4e](../../evidence/gaps-sets-001.md#g-083a1b0fc41c3b4e) · [状态效果 S-9d30934bdeb585d1](../../evidence/state_effects-sets-033.md#s-9d30934bdeb585d1)

### path-008524

```text
(exec)# test ip rib api iprib_geteachroute <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 2 `；EOL ` RVA 0x3423BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-c2201769bcee92a9](../../evidence/state_effects-sets-041.md#s-c2201769bcee92a9)

### path-021213

```text
(exec)# test ip rib api iprib_rtlookup <?ipaddrmask_action@55558978fa30> <cr>
```

Handler ` RVA 0xE2634E0 `；selector ` 0 `；EOL ` RVA 0x3423BA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-278486a76bcce1e7](../../evidence/gaps-sets-002.md#g-278486a76bcce1e7) · [状态效果 S-c2201769bcee92a9](../../evidence/state_effects-sets-041.md#s-c2201769bcee92a9)

### path-001161

```text
(exec)# test ip rmap <cr>
```

Handler ` RVA 0xE207640 `；selector ` 0 `；EOL ` RVA 0x3423B1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c201c42927af4b3](../../evidence/conditions-sets-060.md#c-9c201c42927af4b3)

### path-021250

```text
(exec)# test ip rmap associate <string> <interface> <cr>
```

Handler ` RVA 0xE2025D0 `；selector ` 0 `；EOL ` RVA 0x3423ADC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-7cbc51bd5dae7af9](../../evidence/conditions-sets-048.md#c-7cbc51bd5dae7af9) · [缺口 G-e3bd8b7ccca6db15](../../evidence/gaps-sets-008.md#g-e3bd8b7ccca6db15) · [参数 P-0952a71dc783579b](../../evidence/parameters-sets-001.md#p-0952a71dc783579b) · [状态效果 S-157f0bda20a67fb3](../../evidence/state_effects-sets-005.md#s-157f0bda20a67fb3)

### path-010688

```text
(exec)# test ip rmap associate <string> local <cr>
```

Handler ` RVA 0xE2025D0 `；selector ` 0 `；EOL ` RVA 0x3423ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` rmap name to (dis)associate。

[条件 C-410e9654fa3c0374](../../evidence/conditions-sets-025.md#c-410e9654fa3c0374) · [参数 P-bd73181f983ba232](../../evidence/parameters-sets-014.md#p-bd73181f983ba232) · [状态效果 S-eda55fa3b7350d01](../../evidence/state_effects-sets-050.md#s-eda55fa3b7350d01)

### path-010600

```text
(exec)# test ip rmap batch-commit <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE208090 `；selector ` 0 `；EOL ` RVA 0x34234C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify rmapHandle；` unsigned_number ` Application: 1 - AAA。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-ab77153375655df9](../../evidence/parameters-sets-013.md#p-ab77153375655df9)

### path-010618

```text
(exec)# test ip rmap create <number:0..2147483647> <string> <cr>
```

Handler ` RVA 0xE202AC0 `；selector ` 0 `；EOL ` RVA 0x34234FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application: 1 - AAA；` string ` application specific string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-0a14d68c1ec1aa26](../../evidence/parameters-sets-001.md#p-0a14d68c1ec1aa26)

### path-010659

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> <cr>
```

Handler ` RVA 0xE202FB0 `；selector ` 0 `；EOL ` RVA 0x3423A5F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-6ed09e80c8297b9c](../../evidence/conditions-sets-043.md#c-6ed09e80c8297b9c) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012096

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> match acl <string> <cr>
```

Handler ` RVA 0xE203110 `；selector ` 0 `；EOL ` RVA 0x342357B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` acl name。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [参数 P-272ac774548295cd](../../evidence/parameters-sets-003.md#p-272ac774548295cd) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012161

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> match destination tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 2 `；EOL ` RVA 0x34236208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` dgt id value。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [参数 P-6d91a93fa721550c](../../evidence/parameters-sets-009.md#p-6d91a93fa721550c) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012158

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> match length <number:0..2147483647> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2036F0 `；selector ` 0 `；EOL ` RVA 0x34235B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Minimum packet length；` unsigned_number ` Maximum packet length。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [参数 P-937ae3c156e0cb63](../../evidence/parameters-sets-011.md#p-937ae3c156e0cb63) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012160

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> match source tag <number:0..1000> <cr>
```

Handler ` RVA 0xE2039C0 `；selector ` 1 `；EOL ` RVA 0x34235EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Security id value。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [参数 P-4ef7f2833cf942dd](../../evidence/parameters-sets-007.md#p-4ef7f2833cf942dd) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012099

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> match vrf <string> <cr>
```

Handler ` RVA 0xE2033E0 `；selector ` 0 `；EOL ` RVA 0x342364E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [参数 P-7568d67122bab58a](../../evidence/parameters-sets-009.md#p-7568d67122bab58a) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012108

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set color red <cr>
```

Handler ` RVA 0xE203F30 `；selector ` 0 `；EOL ` RVA 0x3423A160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-b503777d087c83f6](../../evidence/conditions-sets-070.md#c-b503777d087c83f6) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-c7eb32f3ccd007c0](../../evidence/state_effects-sets-042.md#s-c7eb32f3ccd007c0)

### path-012101

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set def-global-nh <address> <cr>
```

Handler ` RVA 0xE205C50 `；selector ` 0 `；EOL ` RVA 0x34237A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-ea7c91e852d793a4](../../evidence/parameters-sets-018.md#p-ea7c91e852d793a4) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012103

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set def-next-hop <address> <cr>
```

Handler ` RVA 0xE2059B0 `；selector ` 0 `；EOL ` RVA 0x34238050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of default next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-b3295dd415de6554](../../evidence/parameters-sets-014.md#p-b3295dd415de6554) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-011986

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set def-nh-verify <cr>
```

Handler ` RVA 0xE205720 `；selector ` 0 `；EOL ` RVA 0x342382D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012163

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set def-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE205EF0 `；selector ` 0 `；EOL ` RVA 0x34237D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-6835e23ae0bf3d34](../../evidence/parameters-sets-008.md#p-6835e23ae0bf3d34) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-025006

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set default-interface <interface> <cr>
```

Handler ` RVA 0xE203C80 `；selector ` 0 `；EOL ` RVA 0x34239E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-09d67e508dfeaba0](../../evidence/conditions-sets-004.md#c-09d67e508dfeaba0) · [缺口 G-62d51b42f17297a5](../../evidence/gaps-sets-004.md#g-62d51b42f17297a5) · [参数 P-95d6304157d6adf5](../../evidence/parameters-sets-012.md#p-95d6304157d6adf5) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012106

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set df <number:0..65535> <cr>
```

Handler ` RVA 0xE204F40 `；selector ` 0 `；EOL ` RVA 0x34238BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of df。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-06c275ebd6daa0a6](../../evidence/parameters-sets-001.md#p-06c275ebd6daa0a6) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012097

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set gateway <address> <cr>
```

Handler ` RVA 0xE206C40 `；selector ` 0 `；EOL ` RVA 0x34236890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of gateway。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-e729039b021e96f0](../../evidence/parameters-sets-017.md#p-e729039b021e96f0) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-011996

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set global <cr>
```

Handler ` RVA 0xE204CB0 `；selector ` 0 `；EOL ` RVA 0x34239130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012159

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set gw-vrf <string> <address> <cr>
```

Handler ` RVA 0xE206EE0 `；selector ` 0 `；EOL ` RVA 0x34236BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of gateway。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-2acbe67311ea0ecd](../../evidence/parameters-sets-004.md#p-2acbe67311ea0ecd) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-025009

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set interface <interface> <cr>
```

Handler ` RVA 0xE2041D0 `；selector ` 0 `；EOL ` RVA 0x342399F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-194171e0699db431](../../evidence/conditions-sets-010.md#c-194171e0699db431) · [缺口 G-9ce68728a18b5716](../../evidence/gaps-sets-006.md#g-9ce68728a18b5716) · [参数 P-f8dc5504182ee306](../../evidence/parameters-sets-019.md#p-f8dc5504182ee306) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012100

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set ip-global-nh <address> <cr>
```

Handler ` RVA 0xE2066E0 `；selector ` 0 `；EOL ` RVA 0x34237430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-b63ee37da7e7cdd4](../../evidence/parameters-sets-014.md#p-b63ee37da7e7cdd4) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012162

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set ip-vrf-nh <string> <address> <cr>
```

Handler ` RVA 0xE206980 `；selector ` 0 `；EOL ` RVA 0x34237758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-ceeec3d0d198abf4](../../evidence/parameters-sets-016.md#p-ceeec3d0d198abf4) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012098

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set next-hop <address> <cr>
```

Handler ` RVA 0xE206440 `；selector ` 0 `；EOL ` RVA 0x34236EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-ac5b408e00df8dee](../../evidence/parameters-sets-013.md#p-ac5b408e00df8dee) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-011981

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set nh-verify <cr>
```

Handler ` RVA 0xE2061B0 `；selector ` 0 `；EOL ` RVA 0x34237120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-cd3e0fed6134dbc5](../../evidence/parameters-sets-016.md#p-cd3e0fed6134dbc5) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-025381

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set oce <?general_pointer_number_action@55558978d3d8> next-hop <address> interface <interface> <cr>
```

Handler ` RVA 0xE204720 `；selector ` 0 `；EOL ` RVA 0x342395D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` address ` IP address of next-hop。

[条件 C-33b787e36c658266](../../evidence/conditions-sets-020.md#c-33b787e36c658266) · [缺口 G-7d0679fc03f2c95a](../../evidence/gaps-sets-005.md#g-7d0679fc03f2c95a) · [参数 P-05ea5f58abea45dc](../../evidence/parameters-sets-001.md#p-05ea5f58abea45dc) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012105

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set precedence <number:0..65535> <cr>
```

Handler ` RVA 0xE2051E0 `；selector ` 0 `；EOL ` RVA 0x342388D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of precedence。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-c55c967820bd003f](../../evidence/parameters-sets-015.md#p-c55c967820bd003f) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012104

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set tos <number:0..65535> <cr>
```

Handler ` RVA 0xE205480 `；selector ` 0 `；EOL ` RVA 0x342385E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` unsigned_number ` Value of tos。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-4dce7f6ad2f960e0](../../evidence/parameters-sets-006.md#p-4dce7f6ad2f960e0) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-012107

```text
(exec)# test ip rmap delete <string> <number:0..4294967295> set vrf <string> <cr>
```

Handler ` RVA 0xE204A00 `；selector ` 0 `；EOL ` RVA 0x34238EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag；` unsigned_number ` entry handle；` string ` VRF name。

[条件 C-ba816207864f254e](../../evidence/conditions-sets-072.md#c-ba816207864f254e) · [参数 P-e80fe2c3ff0d0f92](../../evidence/parameters-sets-017.md#p-e80fe2c3ff0d0f92) · [状态效果 S-5c15171d31b748b4](../../evidence/state_effects-sets-020.md#s-5c15171d31b748b4)

### path-010646

```text
(exec)# test ip rmap delete <string> permit <cr>
```

Handler ` RVA 0xE202DC0 `；selector ` 0 `；EOL ` RVA 0x3423A900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` routemap tag。

[条件 C-769ea3f63d3bd095](../../evidence/conditions-sets-046.md#c-769ea3f63d3bd095) · [参数 P-55050655b3d5bb05](../../evidence/parameters-sets-007.md#p-55050655b3d5bb05) · [状态效果 S-3df721dda58746a6](../../evidence/state_effects-sets-014.md#s-3df721dda58746a6)

### path-008432

```text
(exec)# test ip rmap register <number:0..2147483647> <cr>
```

Handler ` RVA 0xE2028D0 `；selector ` 0 `；EOL ` RVA 0x34234888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Application。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7f8a93636669cf1c](../../evidence/parameters-sets-010.md#p-7f8a93636669cf1c) · [状态效果 S-cba7dbe256e49edc](../../evidence/state_effects-sets-043.md#s-cba7dbe256e49edc)

### path-010612

```text
(exec)# test ip rmap remove <string> <number:0..2147483647> <cr>
```

Handler ` RVA 0xE202C80 `；selector ` 0 `；EOL ` RVA 0x342352F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` application specific string；` unsigned_number ` Application: 1 - AAA。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-c35ad9aae5dc6839](../../evidence/parameters-sets-015.md#p-c35ad9aae5dc6839)

### path-017376

```text
(exec)# test ip static-route add <?ipaddrmask_action@5555897e2690> <cr>
```

Handler ` RVA 0xE2A7490 `；selector ` 0 `；EOL ` RVA 0x3428E9F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a04b67f287497900](../../evidence/conditions-sets-062.md#c-a04b67f287497900) · [缺口 G-bcc8f11adb1cbb06](../../evidence/gaps-sets-007.md#g-bcc8f11adb1cbb06) · [状态效果 S-c9828a0a0667b285](../../evidence/state_effects-sets-043.md#s-c9828a0a0667b285)

### path-025377

```text
(exec)# test ip subscriber create-session ip <address> mac <hex-data> vrf <string> <interface> routed <cr>
```

Handler ` RVA 0x11A3A080 `；selector ` 1 `；EOL ` RVA 0x355CFF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the subscriber。

[条件 C-21c1b252397b6b01](../../evidence/conditions-sets-013.md#c-21c1b252397b6b01) · [缺口 G-fe25c5c20e8eb23b](../../evidence/gaps-sets-009.md#g-fe25c5c20e8eb23b) · [参数 P-24c03866b70f1a89](../../evidence/parameters-sets-003.md#p-24c03866b70f1a89) · [状态效果 S-67870bd48aca2495](../../evidence/state_effects-sets-022.md#s-67870bd48aca2495)

### path-004920

```text
(exec)# test ip subscriber enable <cr>
```

Handler ` RVA 0x11A36370 `；selector ` 0 `；EOL ` RVA 0x355CF310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c6eed75834655e7](../../evidence/conditions-sets-030.md#c-4c6eed75834655e7) · [状态效果 S-3ea265c41e03e182](../../evidence/state_effects-sets-014.md#s-3ea265c41e03e182)

### path-010731

```text
(exec)# test ip subscriber interface association disable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 0 `；EOL ` RVA 0x355CF9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5496f91ad28240b3](../../evidence/conditions-sets-033.md#c-5496f91ad28240b3)

### path-010730

```text
(exec)# test ip subscriber interface association enable <cr>
```

Handler ` RVA 0x11A362F0 `；selector ` 1 `；EOL ` RVA 0x355CF740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26b516dec827fb73](../../evidence/conditions-sets-015.md#c-26b516dec827fb73)

### path-008479

```text
(exec)# test ipam pool local alloc <cr>
```

Handler ` RVA 0xCEB79B0 `；selector ` 0 `；EOL ` RVA 0x33D1C4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49b1b8c2525585a2](../../evidence/conditions-sets-029.md#c-49b1b8c2525585a2) · [状态效果 S-21bafd7a91659808](../../evidence/state_effects-sets-008.md#s-21bafd7a91659808)

### path-021171

```text
(exec)# test ipam pool local alloc <interface> <cr>
```

Handler ` RVA 0xCEB79B0 `；selector ` 0 `；EOL ` RVA 0x33D1C4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6d1d4592420a061b](../../evidence/conditions-sets-042.md#c-6d1d4592420a061b) · [缺口 G-f4da123b70c6d43d](../../evidence/gaps-sets-008.md#g-f4da123b70c6d43d) · [参数 P-375e1720f744f024](../../evidence/parameters-sets-005.md#p-375e1720f744f024) · [状态效果 S-21bafd7a91659808](../../evidence/state_effects-sets-008.md#s-21bafd7a91659808)

### path-009225

```text
(exec)# test ipc FC <number:1..5> <number:0..50000> <cr>
```

Handler ` RVA 0xD3C63E0 `；selector ` 0 `；EOL ` RVA 0x33E33C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` threshold type；` unsigned_number ` Value。

[条件 C-f6a85b179112fa5b](../../evidence/conditions-sets-095.md#c-f6a85b179112fa5b) · [参数 P-569822aca9aeb7ed](../../evidence/parameters-sets-007.md#p-569822aca9aeb7ed)

### path-005834

```text
(exec)# test ipc ack-drop <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6310 `；selector ` 0 `；EOL ` RVA 0x33E33138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-732f7f082f4d9286](../../evidence/conditions-sets-045.md#c-732f7f082f4d9286) · [参数 P-58b2f2cef5d5926b](../../evidence/parameters-sets-007.md#p-58b2f2cef5d5926b)

### path-005860

```text
(exec)# test ipc ack-pending <number:1..10000> <cr>
```

Handler ` RVA 0xD3C6260 `；selector ` 0 `；EOL ` RVA 0x33E334C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-cef75ef4b257cda1](../../evidence/conditions-sets-080.md#c-cef75ef4b257cda1) · [参数 P-8a3569dabade40fa](../../evidence/parameters-sets-011.md#p-8a3569dabade40fa)

### path-006471

```text
(exec)# test ipc ack-timer <number:0..50000> <cr>
```

Handler ` RVA 0xD3C65C0 `；selector ` 0 `；EOL ` RVA 0x33E3B6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-90be1626a3d9d9fe](../../evidence/parameters-sets-011.md#p-90be1626a3d9d9fe)

### path-002079

```text
(exec)# test ipc api <cr>
```

Handler ` RVA 0xD3C1A60 `；selector ` 0 `；EOL ` RVA 0x33E33EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002325

```text
(exec)# test ipc app-send <cr>
```

Handler ` RVA 0xD3C5F70 `；selector ` 0 `；EOL ` RVA 0x33E36440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-011272

```text
(exec)# test ipc bundle mode seat on <cr>
```

Handler ` RVA 0xD3C4B50 `；selector ` 0 `；EOL ` RVA 0x33E3B080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [状态效果 S-5fe9ae5e4eb19b6f](../../evidence/state_effects-sets-021.md#s-5fe9ae5e4eb19b6f)

### path-011262

```text
(exec)# test ipc bundle mode session on <cr>
```

Handler ` RVA 0xD3C4A80 `；selector ` 0 `；EOL ` RVA 0x33E3AD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [状态效果 S-4e1c2d778fd75755](../../evidence/state_effects-sets-017.md#s-4e1c2d778fd75755)

### path-012045

```text
(exec)# test ipc bundle status seat <number:0..4294967295> seat-level on <cr>
```

Handler ` RVA 0xD3C4E20 `；selector ` 0 `；EOL ` RVA 0x33E3A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-a3276e418678fa92](../../evidence/parameters-sets-012.md#p-a3276e418678fa92) · [状态效果 S-b5a2c64c8f754d53](../../evidence/state_effects-sets-038.md#s-b5a2c64c8f754d53)

### path-012047

```text
(exec)# test ipc bundle status session <number:0..4294967295> <number:0..65535> on <cr>
```

Handler ` RVA 0xD3C4C20 `；selector ` 0 `；EOL ` RVA 0x33E3A570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-67bb089c8c087a64](../../evidence/parameters-sets-008.md#p-67bb089c8c087a64) · [状态效果 S-be306982dcd803b2](../../evidence/state_effects-sets-040.md#s-be306982dcd803b2)

### path-002179

```text
(exec)# test ipc callback <cr>
```

Handler ` RVA 0xD3C28E0 `；selector ` 0 `；EOL ` RVA 0x33E35280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002307

```text
(exec)# test ipc diag <cr>
```

Handler ` RVA 0xD3C50D0 `；selector ` 0 `；EOL ` RVA 0x33E36708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-005884

```text
(exec)# test ipc driver stop <cr>
```

Handler ` RVA 0xD3FF9D0 `；selector ` 0 `；EOL ` RVA 0x33E41AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67089e709fb5bf53](../../evidence/conditions-sets-040.md#c-67089e709fb5bf53) · [状态效果 S-5397a62130b1eb2d](../../evidence/state_effects-sets-018.md#s-5397a62130b1eb2d)

### path-005958

```text
(exec)# test ipc drop <number:0..9999> <cr>
```

Handler ` RVA 0xD3C1990 `；selector ` 0 `；EOL ` RVA 0x33E34468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` n: drop every nth packet sent; n=0 for no dropping。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-95af16f3e49d885d](../../evidence/parameters-sets-011.md#p-95af16f3e49d885d)

### path-011837

```text
(exec)# test ipc drop ack <number:65540..4294967295> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C1860 `；selector ` 0 `；EOL ` RVA 0x33E34A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port id；` unsigned_number ` Session id；` unsigned_number ` Number of ACKs to drop。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-71a0b4089b1449b0](../../evidence/parameters-sets-009.md#p-71a0b4089b1449b0)

### path-005986

```text
(exec)# test ipc drop next <cr>
```

Handler ` RVA 0xD3C1930 `；selector ` 0 `；EOL ` RVA 0x33E34718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-011821

```text
(exec)# test ipc mcast appclass subscribe <string> <number:0..15> <cr>
```

Handler ` RVA 0xD452370 `；selector ` 0 `；EOL ` RVA 0x33E44940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` appclass name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-43a6c12fa7a112c4](../../evidence/parameters-sets-006.md#p-43a6c12fa7a112c4)

### path-011838

```text
(exec)# test ipc mcast group close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD452A50 `；selector ` 0 `；EOL ` RVA 0x33E473E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` session id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-5c89ea6d871c9a6c](../../evidence/parameters-sets-007.md#p-5c89ea6d871c9a6c)

### path-012034

```text
(exec)# test ipc mcast group create <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453670 `；selector ` 0 `；EOL ` RVA 0x33E45A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-1dc629c309feb0c9](../../evidence/parameters-sets-003.md#p-1dc629c309feb0c9)

### path-011833

```text
(exec)# test ipc mcast group locate <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453280 `；selector ` 0 `；EOL ` RVA 0x33E46438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-acb97f54bcda4b49](../../evidence/parameters-sets-013.md#p-acb97f54bcda4b49)

### path-012037

```text
(exec)# test ipc mcast group member add <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452C20 `；selector ` 0 `；EOL ` RVA 0x33E46F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` member id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-7e52d3e5b9cd8270](../../evidence/parameters-sets-010.md#p-7e52d3e5b9cd8270) · [状态效果 S-37f4980c9fccdff0](../../evidence/state_effects-sets-012.md#s-37f4980c9fccdff0)

### path-011839

```text
(exec)# test ipc mcast group open <number:0..4294967295> <number:1..2> <cr>
```

Handler ` RVA 0xD452570 `；selector ` 0 `；EOL ` RVA 0x33E477F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id；` unsigned_number ` mode of group open(1. reliable 2. unreliable)。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-64e154c7c2bb31ab](../../evidence/parameters-sets-008.md#p-64e154c7c2bb31ab)

### path-011140

```text
(exec)# test ipc mcast group remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD452EE0 `；selector ` 0 `；EOL ` RVA 0x33E46B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-87c59ea63b268029](../../evidence/parameters-sets-010.md#p-87c59ea63b268029)

### path-011827

```text
(exec)# test ipc mcast group reserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD4533E0 `；selector ` 0 `；EOL ` RVA 0x33E45DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-d67325ad12ec381b](../../evidence/parameters-sets-016.md#p-d67325ad12ec381b)

### path-012035

```text
(exec)# test ipc mcast group subscribe <string> <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453040 `；selector ` 0 `；EOL ` RVA 0x33E467F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` string ` appclass name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-d154cfe91c8424b2](../../evidence/parameters-sets-016.md#p-d154cfe91c8424b2)

### path-011831

```text
(exec)# test ipc mcast group unreserve <string> <number:0..15> <cr>
```

Handler ` RVA 0xD453540 `；selector ` 0 `；EOL ` RVA 0x33E46108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name；` unsigned_number ` zone number。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-4cbd93331c44b6dc](../../evidence/parameters-sets-006.md#p-4cbd93331c44b6dc)

### path-011832

```text
(exec)# test ipc mcast platform emulation <number:0..4294967295> disable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 0 `；EOL ` RVA 0x33E45560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad)

### path-011828

```text
(exec)# test ipc mcast platform emulation <number:0..4294967295> enable <cr>
```

Handler ` RVA 0xD453C00 `；selector ` 1 `；EOL ` RVA 0x33E452B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-59a3f025174c90ad](../../evidence/parameters-sets-007.md#p-59a3f025174c90ad)

### path-011824

```text
(exec)# test ipc mcast platform max-groups <number:0..15> <number:0..65535> <cr>
```

Handler ` RVA 0xD453D60 `；selector ` 0 `；EOL ` RVA 0x33E44FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` zone number；` unsigned_number ` max group count。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-784d9380b4381ff2](../../evidence/parameters-sets-009.md#p-784d9380b4381ff2)

### path-009184

```text
(exec)# test ipc mcast platform registries <cr>
```

Handler ` RVA 0xD453E30 `；selector ` 0 `；EOL ` RVA 0x33E44C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002243

```text
(exec)# test ipc misc <cr>
```

Handler ` RVA 0xD3C40D0 `；selector ` 0 `；EOL ` RVA 0x33E35E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-006368

```text
(exec)# test ipc ping <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C4640 `；selector ` 0 `；EOL ` RVA 0x33E3A0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seat id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-e106634c2595c7c8](../../evidence/parameters-sets-017.md#p-e106634c2595c7c8)

### path-011273

```text
(exec)# test ipc port close <number:0..4294967295> <number:0..65535> <cr>
```

Handler ` RVA 0xD3C8D40 `；selector ` 0 `；EOL ` RVA 0x33E38F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` session id 。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-53b2dab481ba7761](../../evidence/parameters-sets-007.md#p-53b2dab481ba7761)

### path-011285

```text
(exec)# test ipc port create <string> <number:1..3> <cr>
```

Handler ` RVA 0xD3C7F80 `；selector ` 0 `；EOL ` RVA 0x33E37500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` port name；` unsigned_number ` method of message reception(1. callback 2. fast callback 3. queue)。

[条件 C-da4262f7637e28ed](../../evidence/conditions-sets-084.md#c-da4262f7637e28ed) · [参数 P-127dda5a32adb5cf](../../evidence/parameters-sets-002.md#p-127dda5a32adb5cf)

### path-011312

```text
(exec)# test ipc port free <number:0..4294967295> <number:1..1000000> <cr>
```

Handler ` RVA 0xD3C8FA0 `；selector ` 0 `；EOL ` RVA 0x33E39A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` Number of messages。

[条件 C-2e07d5ccaf018ad8](../../evidence/conditions-sets-018.md#c-2e07d5ccaf018ad8) · [参数 P-cbcec36820e3d032](../../evidence/parameters-sets-015.md#p-cbcec36820e3d032)

### path-012131

```text
(exec)# test ipc port msend <number:0..4294967295> <number:0..65535> <number:0..65535> <number:1..1000000> <number:1..4064> <cr>
```

Handler ` RVA 0xD3C8300 `；selector ` 0 `；EOL ` RVA 0x33E38040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` start session id；` unsigned_number ` end session id；` unsigned_number ` number of messages to be sent；` unsigned_number ` size of message。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-78d8a152dee698ee](../../evidence/parameters-sets-009.md#p-78d8a152dee698ee)

### path-009548

```text
(exec)# test ipc port notify enable <cr>
```

Handler ` RVA 0xD3C8F00 `；selector ` 0 `；EOL ` RVA 0x33E395B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [状态效果 S-cd9dcda018827f03](../../evidence/state_effects-sets-044.md#s-cd9dcda018827f03)

### path-011298

```text
(exec)# test ipc port open <number:0..4294967295> <number:1..3> <cr>
```

Handler ` RVA 0xD3C80F0 `；selector ` 0 `；EOL ` RVA 0x33E37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id；` unsigned_number ` mode of port open(1. reliable 2. unreliable 3. unrel-with-not)。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-d00235038e651bbb](../../evidence/parameters-sets-016.md#p-d00235038e651bbb)

### path-009551

```text
(exec)# test ipc port remove <number:0..4294967295> <cr>
```

Handler ` RVA 0xD3C8DC0 `；selector ` 0 `；EOL ` RVA 0x33E392B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` port id。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-a00f33de364d076f](../../evidence/parameters-sets-012.md#p-a00f33de364d076f)

### path-009578

```text
(exec)# test ipc port send header <cr>
```

Handler ` RVA 0xD3C8890 `；selector ` 0 `；EOL ` RVA 0x33E38678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba078f8950c2bf1b](../../evidence/conditions-sets-072.md#c-ba078f8950c2bf1b) · [状态效果 S-f2559594c9c922a3](../../evidence/state_effects-sets-051.md#s-f2559594c9c922a3)

### path-002156

```text
(exec)# test ipc queue <cr>
```

Handler ` RVA 0xD3C2330 `；selector ` 0 `；EOL ` RVA 0x33E34FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-006435

```text
(exec)# test ipc retry-period <number:0..50000> <cr>
```

Handler ` RVA 0xD3C6520 `；selector ` 0 `；EOL ` RVA 0x33E3B410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-8966cb03db7d6b54](../../evidence/parameters-sets-011.md#p-8966cb03db7d6b54)

### path-002251

```text
(exec)# test ipc rpc <cr>
```

Handler ` RVA 0xD3C1DE0 `；selector ` 0 `；EOL ` RVA 0x33E358B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-011822

```text
(exec)# test ipc ru create <string> <number:1..15> conf <cr>
```

Handler ` RVA 0xD3FEFE0 `；selector ` 0 `；EOL ` RVA 0x33E40F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU name；` unsigned_number ` Priority of IPC RU。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-799b680ccf4bb802](../../evidence/parameters-sets-009.md#p-799b680ccf4bb802) · [状态效果 S-05e781d7779aea9b](../../evidence/state_effects-sets-002.md#s-05e781d7779aea9b)

### path-009209

```text
(exec)# test ipc ru remove <string> <cr>
```

Handler ` RVA 0xD3FF380 `；selector ` 0 `；EOL ` RVA 0x33E412F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU id to be removed(in hex)。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-d52691dd1900e41d](../../evidence/parameters-sets-016.md#p-d52691dd1900e41d)

### path-012127

```text
(exec)# test ipc ru tune-thresh <string> <number:1..6> rising major <number:0..10000> <cr>
```

Handler ` RVA 0xD3FF5E0 `；selector ` 0 `；EOL ` RVA 0x33E41728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU id(in hex) whose threshold need to be tuned；` unsigned_number ` Entity to be thresholded: 1. Tx Session Usage 2. Rx Session Usage 3. Rx Port Usage 4. RU Usage 5. Reliable Session ACK pending 6. Seat level ACK pending ；` unsigned_number ` New threshold value。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-8d1eaef814f1e8b7](../../evidence/parameters-sets-011.md#p-8d1eaef814f1e8b7) · [状态效果 S-59df5068fc1f0f04](../../evidence/state_effects-sets-019.md#s-59df5068fc1f0f04)

### path-005883

```text
(exec)# test ipc seat-fc <number:0..1024> <cr>
```

Handler ` RVA 0xD3C61B0 `；selector ` 0 `；EOL ` RVA 0x33E33848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` state。

[条件 C-8fa375cafcd67fe5](../../evidence/conditions-sets-056.md#c-8fa375cafcd67fe5) · [参数 P-c3cdd8e9175bec8d](../../evidence/parameters-sets-015.md#p-c3cdd8e9175bec8d)

### path-009437

```text
(exec)# test ipc size <number:0..100000> <number:0..1000> <cr>
```

Handler ` RVA 0xD3C3720 `；selector ` 0 `；EOL ` RVA 0x33E39DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPC packet size；` unsigned_number ` Number of IPC packet。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-646aa7c03b43ab31](../../evidence/parameters-sets-008.md#p-646aa7c03b43ab31)

### path-002098

```text
(exec)# test ipc slavecore <cr>
```

Handler ` RVA 0xD3C3CC0 `；selector ` 0 `；EOL ` RVA 0x33E34158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002136

```text
(exec)# test ipc slavelog <cr>
```

Handler ` RVA 0xD3C3D00 `；selector ` 0 `；EOL ` RVA 0x33E34D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002225

```text
(exec)# test ipc speed <cr>
```

Handler ` RVA 0xD3C3840 `；selector ` 0 `；EOL ` RVA 0x33E35B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002268

```text
(exec)# test ipc split-init <cr>
```

Handler ` RVA 0xD3C1330 `；selector ` 0 `；EOL ` RVA 0x33E360B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002198

```text
(exec)# test ipc task-pool <cr>
```

Handler ` RVA 0xD3C2D00 `；selector ` 0 `；EOL ` RVA 0x33E35528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-002015

```text
(exec)# test ipc toggle-mask-error <cr>
```

Handler ` RVA 0xD3FFA80 `；selector ` 0 `；EOL ` RVA 0x33E40B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

### path-011835

```text
(exec)# test ipc traffic <number:0..4294967295> <number:1..2147483647> <number:1..5> <number:1..50000> <cr>
```

Handler ` RVA 0xD3C5290 `；selector ` 0 `；EOL ` RVA 0x33E32570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Destination Seat ID or Port ID；` unsigned_number ` Number of messages to be sent；` unsigned_number `  1 - Unreliable 2 - Reliable Non-blocking 3 - RPC blocking 4 - Reliable Non-Blocking and Final Blocked 5 - Reliable Blocking；` unsigned_number ` Size of each IPC message。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-8ec07d117ce331bc](../../evidence/parameters-sets-011.md#p-8ec07d117ce331bc) · [状态效果 S-61e53b63bfba1fb0](../../evidence/state_effects-sets-021.md#s-61e53b63bfba1fb0)

### path-009172

```text
(exec)# test ipc traffic abort <number:0..2147483647> <cr>
```

Handler ` RVA 0xD3C5D40 `；selector ` 0 `；EOL ` RVA 0x33E32A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The process id which is sending the traffic。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5) · [参数 P-116ec98253371dfa](../../evidence/parameters-sets-002.md#p-116ec98253371dfa)

### path-006273

```text
(exec)# test ipc watermark callback <cr>
```

Handler ` RVA 0xD3C6050 `；selector ` 0 `；EOL ` RVA 0x33E36F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0765afe5b8570c5](../../evidence/conditions-sets-093.md#c-f0765afe5b8570c5)

