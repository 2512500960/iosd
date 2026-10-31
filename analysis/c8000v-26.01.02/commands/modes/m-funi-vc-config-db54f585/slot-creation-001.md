# funi-vc-config · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-003226

```text
(config-if-funi-vc)# aaa connect-info <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 87 `；EOL ` RVA 0x369B51F8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` connect-info。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-392971e1e742ffa0](../../evidence/conditions-sets-022.md#c-392971e1e742ffa0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-6cedab252d1d7e4e](../../evidence/parameters-sets-009.md#p-6cedab252d1d7e4e)

### static_slot_creation_candidates-003178

```text
(config-if-funi-vc)# ancp enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 89 `；EOL ` RVA 0x369B4100 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-7db522e90dccc62d](../../evidence/conditions-sets-049.md#c-7db522e90dccc62d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003254

```text
(config-if-funi-vc)# ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 88 `；EOL ` RVA 0x369B45F8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-25704023f85138cf](../../evidence/conditions-sets-015.md#c-25704023f85138cf) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9effe1076205afae](../../evidence/parameters-sets-012.md#p-9effe1076205afae)

### static_slot_creation_candidates-003259

```text
(config-if-funi-vc)# bre-connect <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 64 `；EOL ` RVA 0x369B60D0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN Number。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-50996309d08fcb09](../../evidence/conditions-sets-031.md#c-50996309d08fcb09) · [缺口 G-1624f0f46695e323](../../evidence/gaps-sets-001.md#g-1624f0f46695e323) · [参数 P-2c31ad9f050763d3](../../evidence/parameters-sets-004.md#p-2c31ad9f050763d3)

### static_slot_creation_candidates-003264

```text
(config-if-funi-vc)# bridge-dot1q encap <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x369B3860 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` vlan id to be inserted in dot1q tag header。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a70adc907fca1b99](../../evidence/conditions-sets-064.md#c-a70adc907fca1b99) · [缺口 G-fd92f1e02b8926f9](../../evidence/gaps-sets-009.md#g-fd92f1e02b8926f9) · [参数 P-f2fbe35c3cec72ee](../../evidence/parameters-sets-018.md#p-f2fbe35c3cec72ee)

### static_slot_creation_candidates-003221

```text
(config-if-funi-vc)# bridge-dot1q encap priority-tag <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x369B3860 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a5f1cd92647a71d8](../../evidence/conditions-sets-064.md#c-a5f1cd92647a71d8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-91f8021294296529](../../evidence/state_effects-sets-031.md#s-91f8021294296529)

### static_slot_creation_candidates-003260

```text
(config-if-funi-vc)# bridge-vlan <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 63 `；EOL ` RVA 0x369B5688 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-7b6841d9345c626f](../../evidence/conditions-sets-048.md#c-7b6841d9345c626f) · [缺口 G-3d8cda3f74495f80](../../evidence/gaps-sets-003.md#g-3d8cda3f74495f80) · [参数 P-6d235d8b58da5f03](../../evidence/parameters-sets-009.md#p-6d235d8b58da5f03)

### static_slot_creation_candidates-003160

```text
(config-if-funi-vc)# broadcast <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 27 `；EOL ` RVA 0x369BBC00 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-11852d9a612b7aff](../../evidence/conditions-sets-007.md#c-11852d9a612b7aff) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-d7bef855f6bb7d33](../../evidence/state_effects-sets-046.md#s-d7bef855f6bb7d33)

### static_slot_creation_candidates-003161

```text
(config-if-funi-vc)# cac_off <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 74 `；EOL ` RVA 0x369B4A18 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-d79ee00233ccb3f5](../../evidence/conditions-sets-083.md#c-d79ee00233ccb3f5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003172

```text
(config-if-funi-vc)# class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x369BBF68 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fdb9e84a3c707e84](../../evidence/conditions-sets-098.md#c-fdb9e84a3c707e84) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-41f75cc812e87951](../../evidence/parameters-sets-006.md#p-41f75cc812e87951)

### static_slot_creation_candidates-003215

```text
(config-if-funi-vc)# dbs enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 69 `；EOL ` RVA 0x369B85C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4d8086b766999bd6](../../evidence/conditions-sets-030.md#c-4d8086b766999bd6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-f9afedc953920d90](../../evidence/state_effects-sets-053.md#s-f9afedc953920d90)

### static_slot_creation_candidates-003227

```text
(config-if-funi-vc)# default aaa connect-info <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 87 `；EOL ` RVA 0x369B51F8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-44a00d10f9767a8c](../../evidence/conditions-sets-027.md#c-44a00d10f9767a8c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003224

```text
(config-if-funi-vc)# default ancp enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 89 `；EOL ` RVA 0x369B4100 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-5e69431ba66269d8](../../evidence/conditions-sets-037.md#c-5e69431ba66269d8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003256

```text
(config-if-funi-vc)# default ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 88 `；EOL ` RVA 0x369B45F8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-ccab0b48122b6c66](../../evidence/conditions-sets-079.md#c-ccab0b48122b6c66) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9effe1076205afae](../../evidence/parameters-sets-012.md#p-9effe1076205afae) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003189

```text
(config-if-funi-vc)# default bre-connect <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 64 `；EOL ` RVA 0x369B60D0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-7d692a76823cff72](../../evidence/conditions-sets-049.md#c-7d692a76823cff72) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003219

```text
(config-if-funi-vc)# default bridge-dot1q encap <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x369B3860 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a7a47774b35dbf3d](../../evidence/conditions-sets-065.md#c-a7a47774b35dbf3d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003196

```text
(config-if-funi-vc)# default bridge-vlan <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 63 `；EOL ` RVA 0x369B5688 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a35850da2ea35ee0](../../evidence/conditions-sets-063.md#c-a35850da2ea35ee0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003173

```text
(config-if-funi-vc)# default broadcast <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 27 `；EOL ` RVA 0x369BBC00 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-11852d9a612b7aff](../../evidence/conditions-sets-007.md#c-11852d9a612b7aff) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-163751077d96bfff](../../evidence/state_effects-sets-005.md#s-163751077d96bfff)

### static_slot_creation_candidates-003179

```text
(config-if-funi-vc)# default cac_off <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 74 `；EOL ` RVA 0x369B4A18 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-d79ee00233ccb3f5](../../evidence/conditions-sets-083.md#c-d79ee00233ccb3f5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003223

```text
(config-if-funi-vc)# default class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x369BBF68 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fdb9e84a3c707e84](../../evidence/conditions-sets-098.md#c-fdb9e84a3c707e84) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-41f75cc812e87951](../../evidence/parameters-sets-006.md#p-41f75cc812e87951) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003234

```text
(config-if-funi-vc)# default dbs enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 69 `；EOL ` RVA 0x369B85C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-257063f45fc2e503](../../evidence/conditions-sets-015.md#c-257063f45fc2e503) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003176

```text
(config-if-funi-vc)# default description <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 9 `；EOL ` RVA 0x369BC278 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4d11ed7f34d458a6](../../evidence/conditions-sets-030.md#c-4d11ed7f34d458a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003185

```text
(config-if-funi-vc)# default encapsulation <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x369B4D98 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-cdd4f03ad62dc985](../../evidence/conditions-sets-079.md#c-cdd4f03ad62dc985) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003208

```text
(config-if-funi-vc)# default idle-timeout <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x369B7CE8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-6dcdcdcca4a00343](../../evidence/conditions-sets-042.md#c-6dcdcdcca4a00343) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003229

```text
(config-if-funi-vc)# default ilmi manage <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 15 `；EOL ` RVA 0x369B6818 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-79fd04d2dbd3e552](../../evidence/conditions-sets-047.md#c-79fd04d2dbd3e552) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003197

```text
(config-if-funi-vc)# default inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 13 `；EOL ` RVA 0x369BB218 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-6b90a00a89e4732a](../../evidence/conditions-sets-042.md#c-6b90a00a89e4732a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003202

```text
(config-if-funi-vc)# default ip <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 61 `；EOL ` RVA 0x369BB530 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-5e1e214dc266e601](../../evidence/conditions-sets-037.md#c-5e1e214dc266e601) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003183

```text
(config-if-funi-vc)# default max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x369BC9A8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-27d17b1819002ba6](../../evidence/conditions-sets-016.md#c-27d17b1819002ba6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-7cfaa3e65a676589](../../evidence/state_effects-sets-027.md#s-7cfaa3e65a676589)

### static_slot_creation_candidates-003193

```text
(config-if-funi-vc)# default mid <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 28 `；EOL ` RVA 0x369B6508 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-79fd04d2dbd3e552](../../evidence/conditions-sets-047.md#c-79fd04d2dbd3e552) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003203

```text
(config-if-funi-vc)# default multiqueue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 33 `；EOL ` RVA 0x369B6F40 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-8a224d73e7253fc0](../../evidence/conditions-sets-053.md#c-8a224d73e7253fc0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003236

```text
(config-if-funi-vc)# default oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x369B98E0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-87a6fddbfcfcc812](../../evidence/conditions-sets-052.md#c-87a6fddbfcfcc812) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4bed57fdf246c73b](../../evidence/state_effects-sets-017.md#s-4bed57fdf246c73b)

### static_slot_creation_candidates-003238

```text
(config-if-funi-vc)# default oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x369B94A8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-d25b93dbf0c24b52](../../evidence/conditions-sets-081.md#c-d25b93dbf0c24b52) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-dc9d6cbfa744203a](../../evidence/state_effects-sets-047.md#s-dc9d6cbfa744203a)

### static_slot_creation_candidates-003250

```text
(config-if-funi-vc)# default oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x369B9040 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3ecc85b88791e8b9](../../evidence/conditions-sets-024.md#c-3ecc85b88791e8b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4b30552561621095](../../evidence/state_effects-sets-016.md#s-4b30552561621095)

### static_slot_creation_candidates-003247

```text
(config-if-funi-vc)# default oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x369B8C08 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3ecc85b88791e8b9](../../evidence/conditions-sets-024.md#c-3ecc85b88791e8b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8b5e7071a597e173](../../evidence/state_effects-sets-030.md#s-8b5e7071a597e173)

### static_slot_creation_candidates-003214

```text
(config-if-funi-vc)# default oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x369BAC10 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-cd632b0d95709f93](../../evidence/conditions-sets-079.md#c-cd632b0d95709f93) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-5db118517330466b](../../evidence/state_effects-sets-020.md#s-5db118517330466b)

### static_slot_creation_candidates-003253

```text
(config-if-funi-vc)# default oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x369BA4A0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-30cabef790d91e84](../../evidence/conditions-sets-019.md#c-30cabef790d91e84) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a1bebb9a9e7d8bd0](../../evidence/state_effects-sets-034.md#s-a1bebb9a9e7d8bd0)

### static_slot_creation_candidates-003251

```text
(config-if-funi-vc)# default oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x369B9E28 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-31962ba4eece6cb7](../../evidence/conditions-sets-019.md#c-31962ba4eece6cb7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-75a0709c5974114e](../../evidence/state_effects-sets-025.md#s-75a0709c5974114e)

### static_slot_creation_candidates-003232

```text
(config-if-funi-vc)# default pppoe max-sessions <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 44 `；EOL ` RVA 0x369B8178 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-f334b98cb1df3deb](../../evidence/conditions-sets-094.md#c-f334b98cb1df3deb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003245

```text
(config-if-funi-vc)# default radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 84 `；EOL ` RVA 0x369BB908 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a6ba4271a69e1f10](../../evidence/conditions-sets-064.md#c-a6ba4271a69e1f10) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-377e5f657989ffc7](../../evidence/parameters-sets-005.md#p-377e5f657989ffc7) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003209

```text
(config-if-funi-vc)# default rx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 62 `；EOL ` RVA 0x369B7648 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fb3c71abcdd0ebeb](../../evidence/conditions-sets-097.md#c-fb3c71abcdd0ebeb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003170

```text
(config-if-funi-vc)# default rx-speed <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 86 `；EOL ` RVA 0x369B3C90 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-0f7602bb900e7b7d](../../evidence/conditions-sets-006.md#c-0f7602bb900e7b7d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003198

```text
(config-if-funi-vc)# default transmit-priority <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x369B6B78 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-5b49f459b38f638d](../../evidence/conditions-sets-036.md#c-5b49f459b38f638d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003205

```text
(config-if-funi-vc)# default tx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x369B7298 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-8279ab14056c6f8e](../../evidence/conditions-sets-051.md#c-8279ab14056c6f8e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003212

```text
(config-if-funi-vc)# default tx-ring-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x369B79C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4266f65598824c81](../../evidence/conditions-sets-026.md#c-4266f65598824c81) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003186

```text
(config-if-funi-vc)# default vcci <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 36 `；EOL ` RVA 0x369BC5D8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-cd84437df154471e](../../evidence/conditions-sets-079.md#c-cd84437df154471e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-febf26e70009fca4](../../evidence/state_effects-sets-054.md#s-febf26e70009fca4)

### static_slot_creation_candidates-003175

```text
(config-if-funi-vc)# description <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 9 `；EOL ` RVA 0x369BC278 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VC description upto 80 characters。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3cc1379d726287c4](../../evidence/conditions-sets-024.md#c-3cc1379d726287c4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9899dd17daeb3f32](../../evidence/parameters-sets-012.md#p-9899dd17daeb3f32)

### static_slot_creation_candidates-003265

```text
(config-if-funi-vc)# encapsulation aal5mux <?protoname_action@55558bf10cd0> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x369B4D98 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-d0439392d48a9bf8](../../evidence/conditions-sets-080.md#c-d0439392d48a9bf8) · [缺口 G-7f76e97dde1bc8ff](../../evidence/gaps-sets-005.md#g-7f76e97dde1bc8ff) · [状态效果 S-10162604213831b7](../../evidence/state_effects-sets-004.md#s-10162604213831b7)

### static_slot_creation_candidates-003188

```text
(config-if-funi-vc)# encapsulation aal5snap <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x369B4D98 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-0765aa73662c8a25](../../evidence/conditions-sets-003.md#c-0765aa73662c8a25) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ca1763d17894f44c](../../evidence/state_effects-sets-043.md#s-ca1763d17894f44c)

### static_slot_creation_candidates-003211

```text
(config-if-funi-vc)# idle-timeout <number:0..2000000> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x369B7CE8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Idle timeout in seconds。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-345e773bf9d7159e](../../evidence/conditions-sets-020.md#c-345e773bf9d7159e) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-bf13b1261c9f9db2](../../evidence/parameters-sets-014.md#p-bf13b1261c9f9db2)

### static_slot_creation_candidates-003266

```text
(config-if-funi-vc)# idle-timeout <number:0..2000000> <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x369B7CE8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Idle timeout in seconds；` unsigned_number_dynamic ` minimum traffic rate (Kbps) to keep the connection。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a0162a3c9eea0e44](../../evidence/conditions-sets-062.md#c-a0162a3c9eea0e44) · [缺口 G-94de2e663b0d87f6](../../evidence/gaps-sets-005.md#g-94de2e663b0d87f6) · [参数 P-8c03e0238457b86a](../../evidence/parameters-sets-011.md#p-8c03e0238457b86a)

### static_slot_creation_candidates-003192

```text
(config-if-funi-vc)# ilmi manage <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 15 `；EOL ` RVA 0x369B6818 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-79fd04d2dbd3e552](../../evidence/conditions-sets-047.md#c-79fd04d2dbd3e552) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003164

```text
(config-if-funi-vc)# inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 13 `；EOL ` RVA 0x369BB218 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-6b90a00a89e4732a](../../evidence/conditions-sets-042.md#c-6b90a00a89e4732a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003230

```text
(config-if-funi-vc)# ip addr inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 61 `；EOL ` RVA 0x369BB530 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-22202b28e0b73dd0](../../evidence/conditions-sets-013.md#c-22202b28e0b73dd0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003162

```text
(config-if-funi-vc)# max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x369BC9A8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-27d17b1819002ba6](../../evidence/conditions-sets-016.md#c-27d17b1819002ba6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-92da1417da0f7811](../../evidence/state_effects-sets-031.md#s-92da1417da0f7811)

### static_slot_creation_candidates-003163

```text
(config-if-funi-vc)# mid <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 28 `；EOL ` RVA 0x369B6508 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-79fd04d2dbd3e552](../../evidence/conditions-sets-047.md#c-79fd04d2dbd3e552) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003165

```text
(config-if-funi-vc)# multiqueue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 33 `；EOL ` RVA 0x369B6F40 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-8a224d73e7253fc0](../../evidence/conditions-sets-053.md#c-8a224d73e7253fc0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003225

```text
(config-if-funi-vc)# no aaa connect-info <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 87 `；EOL ` RVA 0x369B51F8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-209c1f62f77c328d](../../evidence/conditions-sets-013.md#c-209c1f62f77c328d) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003222

```text
(config-if-funi-vc)# no ancp enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 89 `；EOL ` RVA 0x369B4100 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-8f1c1333a7a4df0c](../../evidence/conditions-sets-055.md#c-8f1c1333a7a4df0c) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003255

```text
(config-if-funi-vc)# no ancp neighbor name <string> id <string> client-id <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 88 `；EOL ` RVA 0x369B45F8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Neighbor name；` string ` ANCP neighbor ID；` string ` ANCP client ID。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-53030d90949f75fc](../../evidence/conditions-sets-032.md#c-53030d90949f75fc) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-9effe1076205afae](../../evidence/parameters-sets-012.md#p-9effe1076205afae) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003187

```text
(config-if-funi-vc)# no bre-connect <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 64 `；EOL ` RVA 0x369B60D0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4bfc65ef1228bd80](../../evidence/conditions-sets-030.md#c-4bfc65ef1228bd80) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003218

```text
(config-if-funi-vc)# no bridge-dot1q encap <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 93 `；EOL ` RVA 0x369B3860 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-51a28952bd9193d7](../../evidence/conditions-sets-032.md#c-51a28952bd9193d7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003191

```text
(config-if-funi-vc)# no bridge-vlan <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 63 `；EOL ` RVA 0x369B5688 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a35850da2ea35ee0](../../evidence/conditions-sets-063.md#c-a35850da2ea35ee0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003171

```text
(config-if-funi-vc)# no broadcast <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 27 `；EOL ` RVA 0x369BBC00 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-11852d9a612b7aff](../../evidence/conditions-sets-007.md#c-11852d9a612b7aff) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-870aed7ce4c09a70](../../evidence/state_effects-sets-029.md#s-870aed7ce4c09a70)

### static_slot_creation_candidates-003177

```text
(config-if-funi-vc)# no cac_off <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 74 `；EOL ` RVA 0x369B4A18 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-d79ee00233ccb3f5](../../evidence/conditions-sets-083.md#c-d79ee00233ccb3f5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003220

```text
(config-if-funi-vc)# no class-vc <string> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 10 `；EOL ` RVA 0x369BBF68 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ATM vc-class name to use on this VC。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fdb9e84a3c707e84](../../evidence/conditions-sets-098.md#c-fdb9e84a3c707e84) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-41f75cc812e87951](../../evidence/parameters-sets-006.md#p-41f75cc812e87951) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003233

```text
(config-if-funi-vc)# no dbs enable <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 69 `；EOL ` RVA 0x369B85C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4b8541d40e395280](../../evidence/conditions-sets-030.md#c-4b8541d40e395280) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003174

```text
(config-if-funi-vc)# no description <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 9 `；EOL ` RVA 0x369BC278 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-b5bf44c5b80584f4](../../evidence/conditions-sets-070.md#c-b5bf44c5b80584f4) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003181

```text
(config-if-funi-vc)# no encapsulation <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 12 `；EOL ` RVA 0x369B4D98 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-82b6d2bd170563b9](../../evidence/conditions-sets-051.md#c-82b6d2bd170563b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003206

```text
(config-if-funi-vc)# no idle-timeout <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 26 `；EOL ` RVA 0x369B7CE8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-f5955ac39b60036f](../../evidence/conditions-sets-095.md#c-f5955ac39b60036f) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003228

```text
(config-if-funi-vc)# no ilmi manage <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 15 `；EOL ` RVA 0x369B6818 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-79fd04d2dbd3e552](../../evidence/conditions-sets-047.md#c-79fd04d2dbd3e552) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003194

```text
(config-if-funi-vc)# no inarp <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 13 `；EOL ` RVA 0x369BB218 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-6b90a00a89e4732a](../../evidence/conditions-sets-042.md#c-6b90a00a89e4732a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003199

```text
(config-if-funi-vc)# no ip <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 61 `；EOL ` RVA 0x369BB530 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-19f42a124e3ac0a7](../../evidence/conditions-sets-010.md#c-19f42a124e3ac0a7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003180

```text
(config-if-funi-vc)# no max-reserved-bandwidth <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 66 `；EOL ` RVA 0x369BC9A8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-27d17b1819002ba6](../../evidence/conditions-sets-016.md#c-27d17b1819002ba6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-752efc34adf9aafa](../../evidence/state_effects-sets-025.md#s-752efc34adf9aafa)

### static_slot_creation_candidates-003190

```text
(config-if-funi-vc)# no mid <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 28 `；EOL ` RVA 0x369B6508 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-79fd04d2dbd3e552](../../evidence/conditions-sets-047.md#c-79fd04d2dbd3e552) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003200

```text
(config-if-funi-vc)# no multiqueue <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 33 `；EOL ` RVA 0x369B6F40 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-8a224d73e7253fc0](../../evidence/conditions-sets-053.md#c-8a224d73e7253fc0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003235

```text
(config-if-funi-vc)# no oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x369B98E0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-b340d282eb661aff](../../evidence/conditions-sets-069.md#c-b340d282eb661aff) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-4d64bd08f9e6b677](../../evidence/state_effects-sets-017.md#s-4d64bd08f9e6b677)

### static_slot_creation_candidates-003237

```text
(config-if-funi-vc)# no oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x369B94A8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a95b47d4518ad282](../../evidence/conditions-sets-065.md#c-a95b47d4518ad282) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-55bc70ec73279eff](../../evidence/state_effects-sets-019.md#s-55bc70ec73279eff)

### static_slot_creation_candidates-003248

```text
(config-if-funi-vc)# no oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x369B9040 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3ecc85b88791e8b9](../../evidence/conditions-sets-024.md#c-3ecc85b88791e8b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-eb5090e86fa2ee5c](../../evidence/state_effects-sets-050.md#s-eb5090e86fa2ee5c)

### static_slot_creation_candidates-003246

```text
(config-if-funi-vc)# no oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x369B8C08 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3ecc85b88791e8b9](../../evidence/conditions-sets-024.md#c-3ecc85b88791e8b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-044c21e37aa627b5](../../evidence/state_effects-sets-001.md#s-044c21e37aa627b5)

### static_slot_creation_candidates-003213

```text
(config-if-funi-vc)# no oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x369BAC10 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-cd632b0d95709f93](../../evidence/conditions-sets-079.md#c-cd632b0d95709f93) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-ac887dfe1374c955](../../evidence/state_effects-sets-036.md#s-ac887dfe1374c955)

### static_slot_creation_candidates-003252

```text
(config-if-funi-vc)# no oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x369BA4A0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-30cabef790d91e84](../../evidence/conditions-sets-019.md#c-30cabef790d91e84) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6d2b8a71b6190267](../../evidence/state_effects-sets-023.md#s-6d2b8a71b6190267)

### static_slot_creation_candidates-003249

```text
(config-if-funi-vc)# no oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x369B9E28 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-31962ba4eece6cb7](../../evidence/conditions-sets-019.md#c-31962ba4eece6cb7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-26775717303f015a](../../evidence/state_effects-sets-009.md#s-26775717303f015a)

### static_slot_creation_candidates-003231

```text
(config-if-funi-vc)# no pppoe max-sessions <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 44 `；EOL ` RVA 0x369B8178 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-f7dc0c8f1d77e0df](../../evidence/conditions-sets-096.md#c-f7dc0c8f1d77e0df) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003244

```text
(config-if-funi-vc)# no radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 84 `；EOL ` RVA 0x369BB908 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a6ba4271a69e1f10](../../evidence/conditions-sets-064.md#c-a6ba4271a69e1f10) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-377e5f657989ffc7](../../evidence/parameters-sets-005.md#p-377e5f657989ffc7) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003207

```text
(config-if-funi-vc)# no rx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 62 `；EOL ` RVA 0x369B7648 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fb3c71abcdd0ebeb](../../evidence/conditions-sets-097.md#c-fb3c71abcdd0ebeb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003169

```text
(config-if-funi-vc)# no rx-speed <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 86 `；EOL ` RVA 0x369B3C90 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-9e978ed897cbf942](../../evidence/conditions-sets-061.md#c-9e978ed897cbf942) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003195

```text
(config-if-funi-vc)# no transmit-priority <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x369B6B78 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-df317505247b89b8](../../evidence/conditions-sets-086.md#c-df317505247b89b8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003204

```text
(config-if-funi-vc)# no tx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x369B7298 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-eed0f3f70f457649](../../evidence/conditions-sets-092.md#c-eed0f3f70f457649) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003210

```text
(config-if-funi-vc)# no tx-ring-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x369B79C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4266f65598824c81](../../evidence/conditions-sets-026.md#c-4266f65598824c81) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003182

```text
(config-if-funi-vc)# no vcci <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 36 `；EOL ` RVA 0x369BC5D8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-e32370327a1142e0](../../evidence/conditions-sets-087.md#c-e32370327a1142e0) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fc1513299a7365c5](../../evidence/state_effects-sets-053.md#s-fc1513299a7365c5)

### static_slot_creation_candidates-003216

```text
(config-if-funi-vc)# oam ais-rdi <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 23 `；EOL ` RVA 0x369B98E0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-f51f806719890533](../../evidence/conditions-sets-095.md#c-f51f806719890533) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-28811641d0eca42e](../../evidence/state_effects-sets-009.md#s-28811641d0eca42e)

### static_slot_creation_candidates-003217

```text
(config-if-funi-vc)# oam retry <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 20 `；EOL ` RVA 0x369B94A8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-067ff195a3a516b8](../../evidence/conditions-sets-003.md#c-067ff195a3a516b8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-8b2c8a308ce36306](../../evidence/state_effects-sets-030.md#s-8b2c8a308ce36306)

### static_slot_creation_candidates-003241

```text
(config-if-funi-vc)# oam retry cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 21 `；EOL ` RVA 0x369B9040 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3ecc85b88791e8b9](../../evidence/conditions-sets-024.md#c-3ecc85b88791e8b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-13ea20f4175b0198](../../evidence/state_effects-sets-005.md#s-13ea20f4175b0198)

### static_slot_creation_candidates-003240

```text
(config-if-funi-vc)# oam retry cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 22 `；EOL ` RVA 0x369B8C08 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3ecc85b88791e8b9](../../evidence/conditions-sets-024.md#c-3ecc85b88791e8b9) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-15e688be70f2d5f3](../../evidence/state_effects-sets-005.md#s-15e688be70f2d5f3)

### static_slot_creation_candidates-003168

```text
(config-if-funi-vc)# oam-pvc <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 16 `；EOL ` RVA 0x369BAC10 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-cd632b0d95709f93](../../evidence/conditions-sets-079.md#c-cd632b0d95709f93) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-bfa322eff6dda30b](../../evidence/state_effects-sets-041.md#s-bfa322eff6dda30b)

### static_slot_creation_candidates-003243

```text
(config-if-funi-vc)# oam-pvc manage cc end <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 17 `；EOL ` RVA 0x369BA4A0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-30cabef790d91e84](../../evidence/conditions-sets-019.md#c-30cabef790d91e84) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-b1282107b973517a](../../evidence/state_effects-sets-038.md#s-b1282107b973517a)

### static_slot_creation_candidates-003242

```text
(config-if-funi-vc)# oam-pvc manage cc segment <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 18 `；EOL ` RVA 0x369B9E28 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-31962ba4eece6cb7](../../evidence/conditions-sets-019.md#c-31962ba4eece6cb7) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-fcaa40ee97091772](../../evidence/state_effects-sets-054.md#s-fcaa40ee97091772)

### static_slot_creation_candidates-003267

```text
(config-if-funi-vc)# pppoe max-sessions <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 44 `；EOL ` RVA 0x369B8178 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum PPPOE sessions。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fe59129f14e3736b](../../evidence/conditions-sets-098.md#c-fe59129f14e3736b) · [缺口 G-d9b7aba068aba091](../../evidence/gaps-sets-008.md#g-d9b7aba068aba091) · [参数 P-cbfb6214ef3a5777](../../evidence/parameters-sets-015.md#p-cbfb6214ef3a5777)

### static_slot_creation_candidates-003258

```text
(config-if-funi-vc)# protocol <?protoaddr_inarp_action@55558bf268a8> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 11 `；EOL ` RVA 0x369D2A08 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-c6a1a4691406e829](../../evidence/conditions-sets-077.md#c-c6a1a4691406e829) · [缺口 G-76784d5208cf838b](../../evidence/gaps-sets-005.md#g-76784d5208cf838b)

### static_slot_creation_candidates-003239

```text
(config-if-funi-vc)# radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 84 `；EOL ` RVA 0x369BB908 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-a6ba4271a69e1f10](../../evidence/conditions-sets-064.md#c-a6ba4271a69e1f10) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-377e5f657989ffc7](../../evidence/parameters-sets-005.md#p-377e5f657989ffc7)

### static_slot_creation_candidates-003166

```text
(config-if-funi-vc)# rx-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 62 `；EOL ` RVA 0x369B7648 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-fb3c71abcdd0ebeb](../../evidence/conditions-sets-097.md#c-fb3c71abcdd0ebeb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003257

```text
(config-if-funi-vc)# rx-speed <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 86 `；EOL ` RVA 0x369B3C90 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Incoming Cell Rate for L2TP AVP 38 in Kbps。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-9a6bf3e7d05d8634](../../evidence/conditions-sets-060.md#c-9a6bf3e7d05d8634) · [缺口 G-c8ab08fac128c79c](../../evidence/gaps-sets-007.md#g-c8ab08fac128c79c) · [参数 P-383c1854dc8d326a](../../evidence/parameters-sets-005.md#p-383c1854dc8d326a)

### static_slot_creation_candidates-003201

```text
(config-if-funi-vc)# transmit-priority <number:1..4> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x369B6B78 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority level。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-616c74825503b739](../../evidence/conditions-sets-038.md#c-616c74825503b739) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-c34a0cda1527be6f](../../evidence/parameters-sets-015.md#p-c34a0cda1527be6f)

### static_slot_creation_candidates-003261

```text
(config-if-funi-vc)# transmit-priority <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 30 `；EOL ` RVA 0x369B6B78 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` priority level。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-1a2e11643d14700c](../../evidence/conditions-sets-010.md#c-1a2e11643d14700c) · [缺口 G-40c82acbd8e450c5](../../evidence/gaps-sets-003.md#g-40c82acbd8e450c5) · [参数 P-c989cc0e1f8d04f6](../../evidence/parameters-sets-015.md#p-c989cc0e1f8d04f6)

### static_slot_creation_candidates-003262

```text
(config-if-funi-vc)# tx-limit <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 90 `；EOL ` RVA 0x369B7298 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of tx buffers for this VC。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-e6940c3ce52ae603](../../evidence/conditions-sets-089.md#c-e6940c3ce52ae603) · [缺口 G-51a065114b63b72b](../../evidence/gaps-sets-003.md#g-51a065114b63b72b) · [参数 P-d260bc72428e6e58](../../evidence/parameters-sets-016.md#p-d260bc72428e6e58)

### static_slot_creation_candidates-003167

```text
(config-if-funi-vc)# tx-ring-limit <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x369B79C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-4266f65598824c81](../../evidence/conditions-sets-026.md#c-4266f65598824c81) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-003263

```text
(config-if-funi-vc)# tx-ring-limit <number:dynamic> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 32 `；EOL ` RVA 0x369B79C0 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number (ring limit)。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-82e48f527cf32a86](../../evidence/conditions-sets-051.md#c-82e48f527cf32a86) · [缺口 G-752c7c318b99bab1](../../evidence/gaps-sets-005.md#g-752c7c318b99bab1) · [参数 P-d99451de6319c07b](../../evidence/parameters-sets-016.md#p-d99451de6319c07b)

### static_slot_creation_candidates-003184

```text
(config-if-funi-vc)# vcci <number:0..32767> <cr>
```

Handler ` RVA 0xEC62F30 `；selector ` 36 `；EOL ` RVA 0x369BC5D8 `。

模式根 ` RVA 0x369B3688 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VCCI value。

[候选注册 R-8ea22db328f15ced](../../evidence/conditional_registrations-sets-002.md#r-8ea22db328f15ced) · [条件 C-3861c4cb13c80a57](../../evidence/conditions-sets-022.md#c-3861c4cb13c80a57) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-831b19a2a4735d57](../../evidence/parameters-sets-010.md#p-831b19a2a4735d57)

