# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-000399

```text
(exec)# show fqdn <cr>
```

Handler ` RVA 0xC2E0FF0 `；selector ` 0 `；EOL ` RVA 0x33A3C390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006973

```text
(exec)# show frame-relay end-to-end keepalive <cr>
```

Handler ` RVA 0xF630D90 `；selector ` 0 `；EOL ` RVA 0x34710498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e9971aa27d5f7d6](../../evidence/conditions-sets-061.md#c-9e9971aa27d5f7d6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002891

```text
(exec)# show frame-relay fragment <cr>
```

Handler ` RVA 0xD2EE7F0 `；selector ` 99 `；EOL ` RVA 0x33E09DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12f4747393fa7571](../../evidence/conditions-sets-007.md#c-12f4747393fa7571) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015233

```text
(exec)# show frame-relay fragment <interface> <cr>
```

Handler ` RVA 0xD2EE7F0 `；selector ` 99 `；EOL ` RVA 0x33E09DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5f1a750e6103b21](../../evidence/conditions-sets-089.md#c-e5f1a750e6103b21) · [缺口 G-c272ab721f882f4f](../../evidence/gaps-sets-007.md#g-c272ab721f882f4f) · [参数 P-27022a69d7a0347e](../../evidence/parameters-sets-003.md#p-27022a69d7a0347e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009941

```text
(exec)# show frame-relay ip rtp header-compression <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x347068B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a34c8fcaa049772c](../../evidence/conditions-sets-063.md#c-a34c8fcaa049772c) · [状态效果 S-30c6d76ab8d41926](../../evidence/state_effects-sets-011.md#s-30c6d76ab8d41926)

### path-022749

```text
(exec)# show frame-relay ip rtp header-compression <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x347068B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aca7ea7755378664](../../evidence/conditions-sets-067.md#c-aca7ea7755378664) · [缺口 G-84a12cf35f00a9a4](../../evidence/gaps-sets-005.md#g-84a12cf35f00a9a4) · [参数 P-e0598c6cf328ed48](../../evidence/parameters-sets-017.md#p-e0598c6cf328ed48) · [状态效果 S-30c6d76ab8d41926](../../evidence/state_effects-sets-011.md#s-30c6d76ab8d41926)

### path-009933

```text
(exec)# show frame-relay ip tcp header-compression <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x34706468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-192bc92395cbfa38](../../evidence/conditions-sets-010.md#c-192bc92395cbfa38) · [状态效果 S-bfa7f55c37991e43](../../evidence/state_effects-sets-041.md#s-bfa7f55c37991e43)

### path-022741

```text
(exec)# show frame-relay ip tcp header-compression <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x34706468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-da52c661e598b7e6](../../evidence/conditions-sets-084.md#c-da52c661e598b7e6) · [缺口 G-36572982cea49168](../../evidence/gaps-sets-002.md#g-36572982cea49168) · [参数 P-c21e71008274daa9](../../evidence/parameters-sets-015.md#p-c21e71008274daa9) · [状态效果 S-bfa7f55c37991e43](../../evidence/state_effects-sets-041.md#s-bfa7f55c37991e43)

### path-002734

```text
(exec)# show frame-relay lmi <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 5 `；EOL ` RVA 0x346FDE90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-751a69b64be21d46](../../evidence/conditions-sets-045.md#c-751a69b64be21d46) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015059

```text
(exec)# show frame-relay lmi <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 5 `；EOL ` RVA 0x346FDE90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-64caa1af03b4cc19](../../evidence/conditions-sets-039.md#c-64caa1af03b4cc19) · [缺口 G-1e6372393f355bdf](../../evidence/gaps-sets-002.md#g-1e6372393f355bdf) · [参数 P-6bbeb00abf3c76ed](../../evidence/parameters-sets-008.md#p-6bbeb00abf3c76ed) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002698

```text
(exec)# show frame-relay map <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 0 `；EOL ` RVA 0x346FCE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21292ae335c5ca76](../../evidence/conditions-sets-013.md#c-21292ae335c5ca76) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015033

```text
(exec)# show frame-relay map <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 0 `；EOL ` RVA 0x346FCE48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6d76330e358aad8](../../evidence/conditions-sets-077.md#c-c6d76330e358aad8) · [缺口 G-f6404e06abfde94a](../../evidence/gaps-sets-008.md#g-f6404e06abfde94a) · [参数 P-a0d2c8da41af61d6](../../evidence/parameters-sets-012.md#p-a0d2c8da41af61d6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002903

```text
(exec)# show frame-relay multilink <cr>
```

Handler ` RVA 0xC4BF980 `；selector ` 129 `；EOL ` RVA 0x33AA5228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e76b5f317febf59](../../evidence/conditions-sets-061.md#c-9e76b5f317febf59) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015264

```text
(exec)# show frame-relay multilink <interface> <cr>
```

Handler ` RVA 0xC4BF980 `；selector ` 129 `；EOL ` RVA 0x33AA5228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-260bfe0fa659d830](../../evidence/conditions-sets-015.md#c-260bfe0fa659d830) · [缺口 G-e7ac503f935d64fe](../../evidence/gaps-sets-008.md#g-e7ac503f935d64fe) · [参数 P-b2885959629d0317](../../evidence/parameters-sets-014.md#p-b2885959629d0317) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002748

```text
(exec)# show frame-relay pvc <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 2 `；EOL ` RVA 0x346FD508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac0eb9b1222d698c](../../evidence/conditions-sets-066.md#c-ac0eb9b1222d698c) · [状态效果 S-4e29cfcb6092b4aa](../../evidence/state_effects-sets-017.md#s-4e29cfcb6092b4aa)

### path-015087

```text
(exec)# show frame-relay pvc <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 2 `；EOL ` RVA 0x346FD508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-927c49ab754f1e35](../../evidence/conditions-sets-056.md#c-927c49ab754f1e35) · [缺口 G-9bd5779da4972ad3](../../evidence/gaps-sets-006.md#g-9bd5779da4972ad3) · [参数 P-2e0459c18d51caf3](../../evidence/parameters-sets-004.md#p-2e0459c18d51caf3) · [状态效果 S-4e29cfcb6092b4aa](../../evidence/state_effects-sets-017.md#s-4e29cfcb6092b4aa)

### path-002746

```text
(exec)# show frame-relay qos-autosense <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 6 `；EOL ` RVA 0x346FE238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfa96ee587e66981](../../evidence/conditions-sets-080.md#c-cfa96ee587e66981) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015077

```text
(exec)# show frame-relay qos-autosense <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 6 `；EOL ` RVA 0x346FE238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ae26cec3d0efc053](../../evidence/conditions-sets-067.md#c-ae26cec3d0efc053) · [缺口 G-4877c555659f710a](../../evidence/gaps-sets-003.md#g-4877c555659f710a) · [参数 P-82085a31f3bdf5d2](../../evidence/parameters-sets-010.md#p-82085a31f3bdf5d2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002743

```text
(exec)# show frame-relay route <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 7 `；EOL ` RVA 0x346FE538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00bf8ff1252a97eb](../../evidence/conditions-sets-001.md#c-00bf8ff1252a97eb) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002665

```text
(exec)# show frame-relay traffic <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 1 `；EOL ` RVA 0x346FD110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002719

```text
(exec)# show frame-relay vofr <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 3 `；EOL ` RVA 0x346FDA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-104a6a4c01294952](../../evidence/conditions-sets-006.md#c-104a6a4c01294952) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015071

```text
(exec)# show frame-relay vofr <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 3 `；EOL ` RVA 0x346FDA48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b13a955c2b8ff596](../../evidence/conditions-sets-069.md#c-b13a955c2b8ff596) · [缺口 G-9e08199d7b868b69](../../evidence/gaps-sets-006.md#g-9e08199d7b868b69) · [参数 P-d318f6ca22964952](../../evidence/parameters-sets-016.md#p-d318f6ca22964952) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000514

```text
(exec)# show fras <cr>
```

Handler ` RVA 0x1140B8D0 `；selector ` 0 `；EOL ` RVA 0x354C4D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000382

```text
(exec)# show fras-host <cr>
```

Handler ` RVA 0x11388CD0 `；selector ` 0 `；EOL ` RVA 0x3549F568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b49496eed9529b58](../../evidence/conditions-sets-070.md#c-b49496eed9529b58) · [状态效果 S-34d74c0e96a682a7](../../evidence/state_effects-sets-012.md#s-34d74c0e96a682a7)

### path-012675

```text
(exec)# show fras-host <interface> <cr>
```

Handler ` RVA 0x11388CD0 `；selector ` 0 `；EOL ` RVA 0x3549F568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92b8676a14768736](../../evidence/conditions-sets-057.md#c-92b8676a14768736) · [缺口 G-12e0c1051580010b](../../evidence/gaps-sets-001.md#g-12e0c1051580010b) · [参数 P-9c6d7a3c7390aae3](../../evidence/parameters-sets-012.md#p-9c6d7a3c7390aae3) · [状态效果 S-34d74c0e96a682a7](../../evidence/state_effects-sets-012.md#s-34d74c0e96a682a7)

### path-000368

```text
(exec)# show glbp <cr>
```

Handler ` RVA 0xE166D30 `；selector ` 0 `；EOL ` RVA 0x34224068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a30212fac52bb5e2](../../evidence/conditions-sets-063.md#c-a30212fac52bb5e2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002890

```text
(exec)# show glbp capability <cr>
```

Handler ` RVA 0xE166970 `；selector ` 0 `；EOL ` RVA 0x34223BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e17f773f7002d3b0](../../evidence/conditions-sets-087.md#c-e17f773f7002d3b0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015221

```text
(exec)# show glbp capability <interface> <cr>
```

Handler ` RVA 0xE166970 `；selector ` 0 `；EOL ` RVA 0x34223BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-336bde69c349451a](../../evidence/conditions-sets-020.md#c-336bde69c349451a) · [缺口 G-f38835cfab48a756](../../evidence/gaps-sets-008.md#g-f38835cfab48a756) · [参数 P-8f5e1c323fae0d94](../../evidence/parameters-sets-011.md#p-8f5e1c323fae0d94) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002873

```text
(exec)# show glbp internal <cr>
```

Handler ` RVA 0xE166CA0 `；selector ` 0 `；EOL ` RVA 0x342237D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5033c2fc02426220](../../evidence/conditions-sets-031.md#c-5033c2fc02426220) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015232

```text
(exec)# show glbp internal <interface> <cr>
```

Handler ` RVA 0xE166CA0 `；selector ` 0 `；EOL ` RVA 0x342237D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1f98602333b0a8c3](../../evidence/conditions-sets-012.md#c-1f98602333b0a8c3) · [缺口 G-2a5a778008b1d554](../../evidence/gaps-sets-002.md#g-2a5a778008b1d554) · [参数 P-ac0ba157b887c9b3](../../evidence/parameters-sets-013.md#p-ac0ba157b887c9b3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012653

```text
(exec)# show glbp network <cr>
```

Handler ` RVA 0xE166D30 `；selector ` 0 `；EOL ` RVA 0x34224068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa0d2c1767d59297](../../evidence/conditions-sets-066.md#c-aa0d2c1767d59297) · [缺口 G-e5a757d73b0537f1](../../evidence/gaps-sets-008.md#g-e5a757d73b0537f1) · [状态效果 S-84f147ebb88babe7](../../evidence/state_effects-sets-028.md#s-84f147ebb88babe7)

### path-000175

```text
(exec)# show hardware <cr>
```

Handler ` RVA 0xE0065E0 `；selector ` 0 `；EOL ` RVA 0x34165E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8237cd43d4724294](../../evidence/conditions-sets-050.md#c-8237cd43d4724294) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004175

```text
(exec)# show hdd-devices summary <cr>
```

Handler ` RVA 0x1581A210 `；selector ` 0 `；EOL ` RVA 0x3435DBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000140

```text
(exec)# show history <cr>
```

Handler ` RVA 0xE2D2A30 `；selector ` 0 `；EOL ` RVA 0x340C59A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-357048054665d8bc](../../evidence/conditions-sets-021.md#c-357048054665d8bc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000686

```text
(exec)# show history all <cr>
```

Handler ` RVA 0xE2D2B30 `；selector ` 0 `；EOL ` RVA 0x340C5700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012274

```text
(exec)# show hosts <cr>
```

Handler ` RVA 0xD12D240 `；selector ` 0 `；EOL ` RVA 0x33D94D18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d968ffbaf9160f86](../../evidence/conditions-sets-084.md#c-d968ffbaf9160f86) · [缺口 G-1b07875653eb7371](../../evidence/gaps-sets-001.md#g-1b07875653eb7371) · [状态效果 S-5496b5ae70dd2167](../../evidence/state_effects-sets-018.md#s-5496b5ae70dd2167)

### path-002814

```text
(exec)# show hosts summary <cr>
```

Handler ` RVA 0xD12D240 `；selector ` 0 `；EOL ` RVA 0x33D94D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-72c6a888620fc8d7](../../evidence/conditions-sets-044.md#c-72c6a888620fc8d7) · [状态效果 S-32131e6c39ab89bb](../../evidence/state_effects-sets-011.md#s-32131e6c39ab89bb)

### path-003112

```text
(exec)# show hqf full-qos <cr>
```

Handler ` RVA 0x10CE5200 `；selector ` 2 `；EOL ` RVA 0x34D0D9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-679f6ac99c5b398e](../../evidence/conditions-sets-040.md#c-679f6ac99c5b398e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003128

```text
(exec)# show hqf interface <cr>
```

Handler ` RVA 0x10CE4BA0 `；selector ` 0 `；EOL ` RVA 0x34D0CBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de279314f9cedf69](../../evidence/conditions-sets-086.md#c-de279314f9cedf69) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015457

```text
(exec)# show hqf interface <interface> <cr>
```

Handler ` RVA 0x10CE4750 `；selector ` 0 `；EOL ` RVA 0x34D0CBA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b6bd344b091fd47](../../evidence/conditions-sets-023.md#c-3b6bd344b091fd47) · [缺口 G-32f74396c131a590](../../evidence/gaps-sets-002.md#g-32f74396c131a590) · [参数 P-fa46588795320b19](../../evidence/parameters-sets-019.md#p-fa46588795320b19) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003057

```text
(exec)# show hqf size <cr>
```

Handler ` RVA 0x10CE8DC0 `；selector ` 0 `；EOL ` RVA 0x34D0C818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-679f6ac99c5b398e](../../evidence/conditions-sets-040.md#c-679f6ac99c5b398e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003122

```text
(exec)# show hqf sub-interface <cr>
```

Handler ` RVA 0x10CE4DD0 `；selector ` 2 `；EOL ` RVA 0x34D0D160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-679f6ac99c5b398e](../../evidence/conditions-sets-040.md#c-679f6ac99c5b398e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011450

```text
(exec)# show hqf sub-interface <string> dlci <number:16..1007> <cr>
```

Handler ` RVA 0x10CE4DD0 `；selector ` 3 `；EOL ` RVA 0x34D0D208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Namestring of subinterface；` unsigned_number ` DLCI value。

[条件 C-679f6ac99c5b398e](../../evidence/conditions-sets-040.md#c-679f6ac99c5b398e) · [参数 P-b25e912a1f765fbf](../../evidence/parameters-sets-014.md#p-b25e912a1f765fbf) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011452

```text
(exec)# show hqf sub-interface <string> vcd <number:0..8191> <cr>
```

Handler ` RVA 0x10CE4DD0 `；selector ` 6 `；EOL ` RVA 0x34D0D4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Namestring of subinterface；` unsigned_number ` ATM vcd value。

[条件 C-679f6ac99c5b398e](../../evidence/conditions-sets-040.md#c-679f6ac99c5b398e) · [参数 P-fc9a4861b06efba4](../../evidence/parameters-sets-019.md#p-fc9a4861b06efba4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009929

```text
(exec)# show html module command <string> <cr>
```

Handler ` RVA 0xD223470 `；selector ` 4 `；EOL ` RVA 0x33DC6E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The command to execute over modules。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-d9e4f37aa80a5bc6](../../evidence/parameters-sets-016.md#p-d9e4f37aa80a5bc6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006966

```text
(exec)# show html module count <cr>
```

Handler ` RVA 0xD223470 `；selector ` 0 `；EOL ` RVA 0x33DC6B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006954

```text
(exec)# show html module names <cr>
```

Handler ` RVA 0xD223470 `；selector ` 3 `；EOL ` RVA 0x33DC6880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006929

```text
(exec)# show html module options <cr>
```

Handler ` RVA 0xD223470 `；selector ` 2 `；EOL ` RVA 0x33DC62D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006956

```text
(exec)# show html module ports <cr>
```

Handler ` RVA 0xD223470 `；selector ` 1 `；EOL ` RVA 0x33DC65E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009949

```text
(exec)# show html port command <string> <cr>
```

Handler ` RVA 0xD223730 `；selector ` 4 `；EOL ` RVA 0x33DC5ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The command to execute over ports。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-6ee3a3ffd6d25ffc](../../evidence/parameters-sets-009.md#p-6ee3a3ffd6d25ffc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007012

```text
(exec)# show html port count <cr>
```

Handler ` RVA 0xD223730 `；selector ` 0 `；EOL ` RVA 0x33DC5BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006984

```text
(exec)# show html port names <cr>
```

Handler ` RVA 0xD223730 `；selector ` 2 `；EOL ` RVA 0x33DC56A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006968

```text
(exec)# show html port options <cr>
```

Handler ` RVA 0xD223730 `；selector ` 3 `；EOL ` RVA 0x33DC53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006999

```text
(exec)# show html port shortnames <cr>
```

Handler ` RVA 0xD223730 `；selector ` 1 `；EOL ` RVA 0x33DC5948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005342

```text
(exec)# show hw-module all attribute <cr>
```

Handler ` RVA 0x159B8210 `；selector ` 0 `；EOL ` RVA 0x35DD11A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7829c8bb5b9c94d](../../evidence/conditions-sets-065.md#c-a7829c8bb5b9c94d) · [状态效果 S-090ee33403a8c54c](../../evidence/state_effects-sets-002.md#s-090ee33403a8c54c)

### path-005358

```text
(exec)# show hw-module all entity <cr>
```

Handler ` RVA 0xEED4AF0 `；selector ` 0 `；EOL ` RVA 0x34461B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7829c8bb5b9c94d](../../evidence/conditions-sets-065.md#c-a7829c8bb5b9c94d) · [状态效果 S-090ee33403a8c54c](../../evidence/state_effects-sets-002.md#s-090ee33403a8c54c)

### path-005357

```text
(exec)# show hw-module all module <cr>
```

Handler ` RVA 0x159BE350 `；selector ` 0 `；EOL ` RVA 0x35DD3020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b637fa4988c25a0](../../evidence/conditions-sets-048.md#c-7b637fa4988c25a0) · [状态效果 S-090ee33403a8c54c](../../evidence/state_effects-sets-002.md#s-090ee33403a8c54c)

### path-005415

```text
(exec)# show hw-module all oir <cr>
```

Handler ` RVA 0xEEDF390 `；selector ` 0 `；EOL ` RVA 0x34465A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-026ba3854aeed48d](../../evidence/conditions-sets-001.md#c-026ba3854aeed48d) · [状态效果 S-8cd31be0afe224d1](../../evidence/state_effects-sets-030.md#s-8cd31be0afe224d1)

### path-005436

```text
(exec)# show hw-module all sensors <cr>
```

Handler ` RVA 0xEEDAD70 `；selector ` 0 `；EOL ` RVA 0x34463300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-87f594214389bd48](../../evidence/conditions-sets-053.md#c-87f594214389bd48) · [状态效果 S-81d5d58b1720709f](../../evidence/state_effects-sets-028.md#s-81d5d58b1720709f)

### path-005380

```text
(exec)# show hw-module all subblock <cr>
```

Handler ` RVA 0xEEE18D0 `；selector ` 0 `；EOL ` RVA 0x344667D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a2cec3aaf45debb](../../evidence/conditions-sets-016.md#c-2a2cec3aaf45debb) · [状态效果 S-090ee33403a8c54c](../../evidence/state_effects-sets-002.md#s-090ee33403a8c54c)

### path-005413

```text
(exec)# show hw-module all tech-support <cr>
```

Handler ` RVA 0xEEDBE30 `；selector ` 0 `；EOL ` RVA 0x34465D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-026ba3854aeed48d](../../evidence/conditions-sets-001.md#c-026ba3854aeed48d) · [状态效果 S-090ee33403a8c54c](../../evidence/state_effects-sets-002.md#s-090ee33403a8c54c)

### path-021802

```text
(exec)# show hw-module all transceiver <number:dynamic> status <cr>
```

Handler ` RVA 0xEEE1B10 `；selector ` 0 `；EOL ` RVA 0x34466C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` transceiver port number。

[条件 C-3d12f047553f0156](../../evidence/conditions-sets-024.md#c-3d12f047553f0156) · [缺口 G-0b1ac8f46e7627af](../../evidence/gaps-sets-001.md#g-0b1ac8f46e7627af) · [参数 P-5cc20972785a59b2](../../evidence/parameters-sets-007.md#p-5cc20972785a59b2) · [状态效果 S-214d34416ffb3801](../../evidence/state_effects-sets-008.md#s-214d34416ffb3801)

### path-002629

```text
(exec)# show icm stats <cr>
```

Handler ` RVA 0xC2FAF60 `；selector ` 0 `；EOL ` RVA 0x33A40208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-ae3642f62d8d0105](../../evidence/state_effects-sets-037.md#s-ae3642f62d8d0105)

### path-003897

```text
(exec)# show id-manager traceback <cr>
```

Handler ` RVA 0xE115ED0 `；selector ` 0 `；EOL ` RVA 0x342097B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-77a777eefeb4701b](../../evidence/state_effects-sets-025.md#s-77a777eefeb4701b)

### path-000457

```text
(exec)# show idb <cr>
```

Handler ` RVA 0xE3EEB50 `；selector ` 0 `；EOL ` RVA 0x341CF3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6401cd6dc3dd1070](../../evidence/conditions-sets-039.md#c-6401cd6dc3dd1070) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016366

```text
(exec)# show idb <interface> bits <cr>
```

Handler ` RVA 0xE3EFF80 `；selector ` 0 `；EOL ` RVA 0x341D1330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-61be79fff772e092](../../evidence/conditions-sets-038.md#c-61be79fff772e092) · [缺口 G-675a2c85f8f6bd59](../../evidence/gaps-sets-004.md#g-675a2c85f8f6bd59) · [参数 P-9d24ce7442dc7462](../../evidence/parameters-sets-012.md#p-9d24ce7442dc7462) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003957

```text
(exec)# show idb bits <cr>
```

Handler ` RVA 0xE3EFF80 `；selector ` 0 `；EOL ` RVA 0x341D1330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f77eb5ebc47bc6f](../../evidence/conditions-sets-031.md#c-4f77eb5ebc47bc6f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003908

```text
(exec)# show idb ifnum <cr>
```

Handler ` RVA 0xED1CEC0 `；selector ` 0 `；EOL ` RVA 0x34406B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47a84f60ab31b2c2](../../evidence/conditions-sets-028.md#c-47a84f60ab31b2c2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003911

```text
(exec)# show idb pointers <cr>
```

Handler ` RVA 0xE3EFC20 `；selector ` 0 `；EOL ` RVA 0x341D0F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da4f0dbefae566](../../evidence/conditions-sets-059.md#c-97da4f0dbefae566) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003674

```text
(exec)# show identity policy <cr>
```

Handler ` RVA 0xCB518F0 `；selector ` 0 `；EOL ` RVA 0x33BE2038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-ab38650fdb5617f9](../../evidence/state_effects-sets-036.md#s-ab38650fdb5617f9)

### path-003675

```text
(exec)# show identity profile <cr>
```

Handler ` RVA 0xCB50300 `；selector ` 0 `；EOL ` RVA 0x33BE1C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-b16d790968c628ca](../../evidence/state_effects-sets-038.md#s-b16d790968c628ca)

### path-003462

```text
(exec)# show idmgr memory <cr>
```

Handler ` RVA 0xE186C50 `；selector ` 0 `；EOL ` RVA 0x3422A9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-c3df3704858ed64a](../../evidence/state_effects-sets-041.md#s-c3df3704858ed64a)

### path-003418

```text
(exec)# show idmgr statistics <cr>
```

Handler ` RVA 0xE186C50 `；selector ` 0 `；EOL ` RVA 0x34229E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2647b1ac7f61c2db](../../evidence/state_effects-sets-009.md#s-2647b1ac7f61c2db)

### path-000241

```text
(exec)# show if-mgr <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 0 `；EOL ` RVA 0x33A35908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005196

```text
(exec)# show if-mgr db ifStack <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 6 `；EOL ` RVA 0x33A350E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008824

```text
(exec)# show if-mgr db interface brief <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 2 `；EOL ` RVA 0x33A34348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010933

```text
(exec)# show if-mgr db interface ifIndex <number:0..4294967295> <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 1 `；EOL ` RVA 0x33A346C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interface's ifIndex。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-ed37c063ae2f72f0](../../evidence/parameters-sets-018.md#p-ed37c063ae2f72f0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011730

```text
(exec)# show if-mgr db interface ifIndex <number:0..4294967295> ifStack <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 5 `；EOL ` RVA 0x33A346A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interface's ifIndex。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-ed37c063ae2f72f0](../../evidence/parameters-sets-018.md#p-ed37c063ae2f72f0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008880

```text
(exec)# show if-mgr db interface ifName <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 4 `；EOL ` RVA 0x33A34C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010922

```text
(exec)# show if-mgr db interface ifName <string> <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 3 `；EOL ` RVA 0x33A34BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` interface's ifName。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-5e93dbc60763e120](../../evidence/parameters-sets-008.md#p-5e93dbc60763e120) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001409

```text
(exec)# show if-mgr hash <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 7 `；EOL ` RVA 0x33A35438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005194

```text
(exec)# show if-mgr hash brief <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 8 `；EOL ` RVA 0x33A35410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000628

```text
(exec)# show ifnum list <cr>
```

Handler ` RVA 0xED27C20 `；selector ` 0 `；EOL ` RVA 0x34406588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000640

```text
(exec)# show ifnum statistics <cr>
```

Handler ` RVA 0xED27C20 `；selector ` 1 `；EOL ` RVA 0x34406830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012241

```text
(exec)# show interfaces <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 0 `；EOL ` RVA 0x34125150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-18d168ad4cdb88b1](../../evidence/conditions-sets-010.md#c-18d168ad4cdb88b1) · [缺口 G-38b0b5be34db5940](../../evidence/gaps-sets-002.md#g-38b0b5be34db5940) · [状态效果 S-eb701cb8061b8590](../../evidence/state_effects-sets-050.md#s-eb701cb8061b8590)

### path-012919

```text
(exec)# show interfaces <interface> switchport <cr>
```

Handler ` RVA 0x15C36D40 `；selector ` 1 `；EOL ` RVA 0x35DF3070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4090e462a3e697b2](../../evidence/conditions-sets-025.md#c-4090e462a3e697b2) · [缺口 G-fafd5741871f1eb9](../../evidence/gaps-sets-009.md#g-fafd5741871f1eb9) · [参数 P-abfa956765e3a60b](../../evidence/parameters-sets-013.md#p-abfa956765e3a60b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008292

```text
(exec)# show interfaces counters protocol status <cr>
```

Handler ` RVA 0xE4456B0 `；selector ` 0 `；EOL ` RVA 0x342C20E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-affa0ecf314e7fc9](../../evidence/conditions-sets-068.md#c-affa0ecf314e7fc9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000602

```text
(exec)# show interfaces dampening <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 0 `；EOL ` RVA 0x34125150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a10a9973b15f400](../../evidence/conditions-sets-029.md#c-4a10a9973b15f400) · [状态效果 S-e1fe7881e23bfbb0](../../evidence/state_effects-sets-048.md#s-e1fe7881e23bfbb0)

### path-000733

```text
(exec)# show interfaces flowcontrol <cr>
```

Handler ` RVA 0x15DB0A30 `；selector ` 0 `；EOL ` RVA 0x35E1F540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6bf686dcdf673547](../../evidence/conditions-sets-042.md#c-6bf686dcdf673547) · [状态效果 S-575543c1faffb7e6](../../evidence/state_effects-sets-019.md#s-575543c1faffb7e6)

### path-000890

```text
(exec)# show interfaces history <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 21 `；EOL ` RVA 0x34125AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-affa0ecf314e7fc9](../../evidence/conditions-sets-068.md#c-affa0ecf314e7fc9) · [状态效果 S-727bfbdb34b6bb25](../../evidence/state_effects-sets-024.md#s-727bfbdb34b6bb25)

### path-000454

```text
(exec)# show inventory <cr>
```

Handler ` RVA 0xE01BD20 `；selector ` 0 `；EOL ` RVA 0x3416E5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d5dec2e58c2b1db](../../evidence/conditions-sets-005.md#c-0d5dec2e58c2b1db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003574

```text
(exec)# show iosp-server status <cr>
```

Handler ` RVA 0xE8C47B0 `；selector ` 0 `；EOL ` RVA 0x3433C288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000511

```text
(exec)# show iox-service <cr>
```

Handler ` RVA 0xE9E9380 `；selector ` 1 `；EOL ` RVA 0x34384010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004199

```text
(exec)# show iox-service detail <cr>
```

Handler ` RVA 0xE9E9380 `；selector ` 3 `；EOL ` RVA 0x34383FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002060

```text
(exec)# show ip access-lists <cr>
```

Handler ` RVA 0xCEED5F0 `；selector ` 0 `；EOL ` RVA 0x33D54CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-824757fadfc0503f](../../evidence/conditions-sets-050.md#c-824757fadfc0503f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009201

```text
(exec)# show ip access-lists <number:1..199> dump-og-database <cr>
```

Handler ` RVA 0xCEED520 `；selector ` 0 `；EOL ` RVA 0x33D558A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-185fcf624f14e66f](../../evidence/conditions-sets-009.md#c-185fcf624f14e66f) · [参数 P-8145ab0f3d0aa67b](../../evidence/parameters-sets-010.md#p-8145ab0f3d0aa67b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009222

```text
(exec)# show ip access-lists <number:1..199> dump-reflexive <cr>
```

Handler ` RVA 0xCEED210 `；selector ` 0 `；EOL ` RVA 0x33D55B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-5c9b0ba30abf27c7](../../evidence/conditions-sets-036.md#c-5c9b0ba30abf27c7) · [参数 P-8145ab0f3d0aa67b](../../evidence/parameters-sets-010.md#p-8145ab0f3d0aa67b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009181

```text
(exec)# show ip access-lists <number:1..199> expanded <cr>
```

Handler ` RVA 0xCEED760 `；selector ` 0 `；EOL ` RVA 0x33D55578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-9929ff3c4a26b4db](../../evidence/conditions-sets-059.md#c-9929ff3c4a26b4db) · [参数 P-8145ab0f3d0aa67b](../../evidence/parameters-sets-010.md#p-8145ab0f3d0aa67b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018415

```text
(exec)# show ip access-lists interface <interface> <cr>
```

Handler ` RVA 0xCEED960 `；selector ` 0 `；EOL ` RVA 0x33D55168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-99139f0d97b5f5bb](../../evidence/conditions-sets-059.md#c-99139f0d97b5f5bb) · [缺口 G-fa7f9ae50c0a9ba8](../../evidence/gaps-sets-009.md#g-fa7f9ae50c0a9ba8) · [参数 P-66b42d6f3c85068c](../../evidence/parameters-sets-008.md#p-66b42d6f3c85068c) · [状态效果 S-6b6399900faccb6b](../../evidence/state_effects-sets-023.md#s-6b6399900faccb6b)

### path-002720

```text
(exec)# show ip accounting <cr>
```

Handler ` RVA 0xD17A1A0 `；selector ` 0 `；EOL ` RVA 0x33DA7150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44731adc3ad1460c](../../evidence/conditions-sets-027.md#c-44731adc3ad1460c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002432

```text
(exec)# show ip aliases <cr>
```

Handler ` RVA 0xD17BFF0 `；selector ` 0 `；EOL ` RVA 0x33DA83B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006246

```text
(exec)# show ip amt tunnel <cr>
```

Handler ` RVA 0xBB7D800 `；selector ` 0 `；EOL ` RVA 0x3386C998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5623e8bc26bfe91c](../../evidence/conditions-sets-034.md#c-5623e8bc26bfe91c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005625

```text
(exec)# show ip arp <address> <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 3 `；EOL ` RVA 0x33D1F210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` 48-bit hardware address of ARP entry。

[条件 C-76cceedcc850b249](../../evidence/conditions-sets-046.md#c-76cceedcc850b249) · [参数 P-271dd2dbc889757e](../../evidence/parameters-sets-003.md#p-271dd2dbc889757e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005670

```text
(exec)# show ip arp <address> <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 2 `；EOL ` RVA 0x33D1F778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address or hostname of ARP entry。

[条件 C-09693ece4fc965aa](../../evidence/conditions-sets-004.md#c-09693ece4fc965aa) · [参数 P-eac77c0fd9a82cc9](../../evidence/parameters-sets-018.md#p-eac77c0fd9a82cc9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001898

```text
(exec)# show ip arp <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 0 `；EOL ` RVA 0x33D1F4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76cceedcc850b249](../../evidence/conditions-sets-046.md#c-76cceedcc850b249) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014154

```text
(exec)# show ip arp <interface> <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 1 `；EOL ` RVA 0x33D1EF68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e3d138c1cb7a9cc8](../../evidence/conditions-sets-088.md#c-e3d138c1cb7a9cc8) · [缺口 G-f761f1beb1dd7250](../../evidence/gaps-sets-009.md#g-f761f1beb1dd7250) · [参数 P-4e1b23c080c06fe5](../../evidence/parameters-sets-006.md#p-4e1b23c080c06fe5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005574

```text
(exec)# show ip arp garpretry <cr>
```

Handler ` RVA 0xCF704B0 `；selector ` 0 `；EOL ` RVA 0x33D1FA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b4a3f7226b498b5](../../evidence/conditions-sets-060.md#c-9b4a3f7226b498b5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005557

```text
(exec)# show ip arp incomplete <cr>
```

Handler ` RVA 0xCF6DDD0 `；selector ` 0 `；EOL ` RVA 0x33D1FD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-787815ccc587836a](../../evidence/conditions-sets-047.md#c-787815ccc587836a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005511

```text
(exec)# show ip arp poll <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 5 `；EOL ` RVA 0x33D1E860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005506

```text
(exec)# show ip arp summary <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 4 `；EOL ` RVA 0x33D1EB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002272

```text
(exec)# show ip as-path-access-list <cr>
```

Handler ` RVA 0xF24D440 `；selector ` 0 `；EOL ` RVA 0x344BB918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002124

```text
(exec)# show ip cache <cr>
```

Handler ` RVA 0xD49E9E0 `；selector ` 0 `；EOL ` RVA 0x33E55378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66a8ae06a0c4d6d0](../../evidence/conditions-sets-040.md#c-66a8ae06a0c4d6d0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014437

```text
(exec)# show ip cache <interface> <cr>
```

Handler ` RVA 0xD49E9E0 `；selector ` 0 `；EOL ` RVA 0x33E55378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e29cf83e12ccc2d7](../../evidence/conditions-sets-087.md#c-e29cf83e12ccc2d7) · [缺口 G-6b31f0b012fe1896](../../evidence/gaps-sets-004.md#g-6b31f0b012fe1896) · [参数 P-0061b1ed422a21f0](../../evidence/parameters-sets-001.md#p-0061b1ed422a21f0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018516

```text
(exec)# show ip cache <interface> flow <cr>
```

Handler ` RVA 0x10BB3E20 `；selector ` 0 `；EOL ` RVA 0x34CCC258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f974c8fdd074e21](../../evidence/conditions-sets-025.md#c-3f974c8fdd074e21) · [缺口 G-6b31f0b012fe1896](../../evidence/gaps-sets-004.md#g-6b31f0b012fe1896) · [参数 P-0061b1ed422a21f0](../../evidence/parameters-sets-001.md#p-0061b1ed422a21f0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006027

```text
(exec)# show ip cache flow <cr>
```

Handler ` RVA 0x10BB3E20 `；selector ` 0 `；EOL ` RVA 0x34CCC258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-36f0bd57c0f1ee01](../../evidence/conditions-sets-021.md#c-36f0bd57c0f1ee01) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005865

```text
(exec)# show ip cache policy <cr>
```

Handler ` RVA 0xD49E9E0 `；selector ` 0 `；EOL ` RVA 0x34804F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-fb36fb904787840e](../../evidence/state_effects-sets-053.md#s-fb36fb904787840e)

### path-006676

```text
(exec)# show ip casa oper <cr>
```

Handler ` RVA 0x11266710 `；selector ` 0 `；EOL ` RVA 0x354406C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-796e911c5e6ac3a8](../../evidence/state_effects-sets-026.md#s-796e911c5e6ac3a8)

### path-006804

```text
(exec)# show ip casa wildcard <cr>
```

Handler ` RVA 0x1132CDC0 `；selector ` 0 `；EOL ` RVA 0x35498E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2caa31edd279f934](../../evidence/state_effects-sets-010.md#s-2caa31edd279f934)

### path-003131

```text
(exec)# show ip cef <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 0 `；EOL ` RVA 0x337B5CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-896733f6d6a79f4c](../../evidence/conditions-sets-053.md#c-896733f6d6a79f4c) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-015456

```text
(exec)# show ip cef <interface> <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 0 `；EOL ` RVA 0x337B5CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44879ea83caa14e2](../../evidence/conditions-sets-027.md#c-44879ea83caa14e2) · [缺口 G-a4eb6b2c27b9e40c](../../evidence/gaps-sets-006.md#g-a4eb6b2c27b9e40c) · [参数 P-5bf33fa929e3f371](../../evidence/parameters-sets-007.md#p-5bf33fa929e3f371) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-007038

```text
(exec)# show ip cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337B67B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e9444642e37b3ea](../../evidence/conditions-sets-024.md#c-3e9444642e37b3ea) · [状态效果 S-a9c545985c4e544d](../../evidence/state_effects-sets-036.md#s-a9c545985c4e544d)

### path-006972

```text
(exec)# show ip cef inconsistency <cr>
```

Handler ` RVA 0xB5FCCD0 `；selector ` 0 `；EOL ` RVA 0x337B6D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e9444642e37b3ea](../../evidence/conditions-sets-024.md#c-3e9444642e37b3ea) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-006988

```text
(exec)# show ip cef label-table <cr>
```

Handler ` RVA 0xB5FBF00 `；selector ` 0 `；EOL ` RVA 0x337B6370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e9444642e37b3ea](../../evidence/conditions-sets-024.md#c-3e9444642e37b3ea) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-006856

```text
(exec)# show ip cef protocol-discard <cr>
```

Handler ` RVA 0xB5C2EB0 `；selector ` 74 `；EOL ` RVA 0x337C4AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006878

```text
(exec)# show ip cef summary <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 1 `；EOL ` RVA 0x337B5518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16e40a679283bf53](../../evidence/conditions-sets-009.md#c-16e40a679283bf53) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-009895

```text
(exec)# show ip cef switching statistics <cr>
```

Handler ` RVA 0xB5F8C90 `；selector ` 0 `；EOL ` RVA 0x337B6018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e9444642e37b3ea](../../evidence/conditions-sets-024.md#c-3e9444642e37b3ea) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-009919

```text
(exec)# show ip cef traffic prefix-length <cr>
```

Handler ` RVA 0xB5FCBD0 `；selector ` 0 `；EOL ` RVA 0x337B7068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e9444642e37b3ea](../../evidence/conditions-sets-024.md#c-3e9444642e37b3ea) · [状态效果 S-4b0c55f8b6fde130](../../evidence/state_effects-sets-016.md#s-4b0c55f8b6fde130)

### path-006926

```text
(exec)# show ip cef tree <cr>
```

Handler ` RVA 0xB5FC9E0 `；selector ` 0 `；EOL ` RVA 0x337B5828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16e40a679283bf53](../../evidence/conditions-sets-009.md#c-16e40a679283bf53) · [状态效果 S-25f7f35a99e3a6ec](../../evidence/state_effects-sets-009.md#s-25f7f35a99e3a6ec)

### path-002292

```text
(exec)# show ip community-list <cr>
```

Handler ` RVA 0xF248DA0 `；selector ` 0 `；EOL ` RVA 0x344BB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126c64d7c9eb12c2](../../evidence/conditions-sets-007.md#c-126c64d7c9eb12c2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006838

```text
(exec)# show ip ddns update <cr>
```

Handler ` RVA 0xF4811F0 `；selector ` 0 `；EOL ` RVA 0x3465B360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7705a1fb587c2a9](../../evidence/conditions-sets-089.md#c-e7705a1fb587c2a9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019394

```text
(exec)# show ip ddns update <interface> <cr>
```

Handler ` RVA 0xF4811F0 `；selector ` 0 `；EOL ` RVA 0x3465B360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-52b48a619b84ff79](../../evidence/conditions-sets-032.md#c-52b48a619b84ff79) · [缺口 G-cd0a7da60ce72d65](../../evidence/gaps-sets-007.md#g-cd0a7da60ce72d65) · [参数 P-dd8c8ede646185fc](../../evidence/parameters-sets-017.md#p-dd8c8ede646185fc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009799

```text
(exec)# show ip ddns update method <cr>
```

Handler ` RVA 0xF480EE0 `；selector ` 0 `；EOL ` RVA 0x3465B008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001847

```text
(exec)# show ip default-gateway <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 1 `；EOL ` RVA 0x33D32B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002607

```text
(exec)# show ip dfp <cr>
```

Handler ` RVA 0x11285090 `；selector ` 0 `；EOL ` RVA 0x354459E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009931

```text
(exec)# show ip dhcp binding <address> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 1 `；EOL ` RVA 0x33DE0540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address in dotted-decimal notation。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-b433863fc480c7af](../../evidence/parameters-sets-014.md#p-b433863fc480c7af) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006990

```text
(exec)# show ip dhcp binding <cr>
```

Handler ` RVA 0xD298440 `；selector ` 0 `；EOL ` RVA 0x33DE0128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006958

```text
(exec)# show ip dhcp conflict <cr>
```

Handler ` RVA 0xD298440 `；selector ` 2 `；EOL ` RVA 0x33DE0F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006897

```text
(exec)# show ip dhcp database <cr>
```

Handler ` RVA 0xD251DB0 `；selector ` 3 `；EOL ` RVA 0x33DD6410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009858

```text
(exec)# show ip dhcp database <string> <cr>
```

Handler ` RVA 0xD251DB0 `；selector ` 4 `；EOL ` RVA 0x33DD63E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Uniform Resource Locator (URL)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-faf497cd99c246ca](../../evidence/parameters-sets-019.md#p-faf497cd99c246ca) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009855

```text
(exec)# show ip dhcp excluded-addresses all <cr>
```

Handler ` RVA 0xD29AF20 `；selector ` 15 `；EOL ` RVA 0x33DD5B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011395

```text
(exec)# show ip dhcp excluded-addresses pool <string> <cr>
```

Handler ` RVA 0xD29AF20 `；selector ` 14 `；EOL ` RVA 0x33DD6100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-39a02f901b7b7a04](../../evidence/parameters-sets-005.md#p-39a02f901b7b7a04) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011391

```text
(exec)# show ip dhcp excluded-addresses vrf <string> <cr>
```

Handler ` RVA 0xD29AF20 `；selector ` 16 `；EOL ` RVA 0x33DD5E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-3fc957922bee21ab](../../evidence/parameters-sets-005.md#p-3fc957922bee21ab) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024383

```text
(exec)# show ip dhcp hash find-index <number:0..65535> <hex-string> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 20 `；EOL ` RVA 0x33DE30E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` htype value；` hexstring ` haddr value (Hexstring)。

[条件 C-aca2907ee5b67e89](../../evidence/conditions-sets-067.md#c-aca2907ee5b67e89) · [缺口 G-80c79e6647736ce2](../../evidence/gaps-sets-005.md#g-80c79e6647736ce2) · [参数 P-084e89d8230e234e](../../evidence/parameters-sets-001.md#p-084e89d8230e234e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011445

```text
(exec)# show ip dhcp hash global dump <cr>
```

Handler ` RVA 0xD298440 `；selector ` 19 `；EOL ` RVA 0x33DE2D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce995e6fd163215d](../../evidence/conditions-sets-080.md#c-ce995e6fd163215d) · [状态效果 S-fe8e0c620b962924](../../evidence/state_effects-sets-054.md#s-fe8e0c620b962924)

### path-011444

```text
(exec)# show ip dhcp hash global statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 18 `；EOL ` RVA 0x33DE2A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce995e6fd163215d](../../evidence/conditions-sets-080.md#c-ce995e6fd163215d) · [状态效果 S-fe8e0c620b962924](../../evidence/state_effects-sets-054.md#s-fe8e0c620b962924)

### path-006969

```text
(exec)# show ip dhcp import <cr>
```

Handler ` RVA 0xD298440 `；selector ` 6 `；EOL ` RVA 0x33DE1520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009957

```text
(exec)# show ip dhcp limit lease <cr>
```

Handler ` RVA 0xD298440 `；selector ` 10 `；EOL ` RVA 0x33DE24E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1909e6b34ce9721a](../../evidence/conditions-sets-010.md#c-1909e6b34ce9721a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022766

```text
(exec)# show ip dhcp limit lease <interface> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 10 `；EOL ` RVA 0x33DE24E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4f57ff019a195fe2](../../evidence/conditions-sets-031.md#c-4f57ff019a195fe2) · [缺口 G-0977f4ecd41c659f](../../evidence/gaps-sets-001.md#g-0977f4ecd41c659f) · [参数 P-7938f911247cd3c1](../../evidence/parameters-sets-009.md#p-7938f911247cd3c1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009907

```text
(exec)# show ip dhcp packet statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 17 `；EOL ` RVA 0x33DE1290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007014

```text
(exec)# show ip dhcp pool <cr>
```

Handler ` RVA 0xD298440 `；selector ` 7 `；EOL ` RVA 0x33DE2140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011383

```text
(exec)# show ip dhcp relay information trusted-sources <cr>
```

Handler ` RVA 0xD24E100 `；selector ` 0 `；EOL ` RVA 0x33DD5830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009935

```text
(exec)# show ip dhcp server odap-statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 12 `；EOL ` RVA 0x33DE1E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009945

```text
(exec)# show ip dhcp server statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 5 `；EOL ` RVA 0x33DE1940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa9c072073dc5ceb](../../evidence/conditions-sets-066.md#c-aa9c072073dc5ceb) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022752

```text
(exec)# show ip dhcp server statistics <interface> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 11 `；EOL ` RVA 0x33DE1918 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5bd607d7863f9816](../../evidence/conditions-sets-036.md#c-5bd607d7863f9816) · [缺口 G-5de8a475d9cee600](../../evidence/gaps-sets-004.md#g-5de8a475d9cee600) · [参数 P-b533da34b300ad73](../../evidence/parameters-sets-014.md#p-b533da34b300ad73) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009926

```text
(exec)# show ip dhcp sip session <cr>
```

Handler ` RVA 0x1128DD50 `；selector ` 0 `；EOL ` RVA 0x354479F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-0ea44d15957a0c48](../../evidence/state_effects-sets-003.md#s-0ea44d15957a0c48)

### path-009932

```text
(exec)# show ip dhcp sip statistics <cr>
```

Handler ` RVA 0x1128D470 `；selector ` 0 `；EOL ` RVA 0x35447E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006975

```text
(exec)# show ip dhcp snooping <cr>
```

Handler ` RVA 0x15FA8760 `；selector ` 0 `；EOL ` RVA 0x35E812A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-039b5552afb7a736](../../evidence/conditions-sets-002.md#c-039b5552afb7a736) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009959

```text
(exec)# show ip dhcp snooping binding <cr>
```

Handler ` RVA 0x15FA9210 `；selector ` 0 `；EOL ` RVA 0x35E80808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67cc22093db9019c](../../evidence/conditions-sets-040.md#c-67cc22093db9019c) · [状态效果 S-d8a2825e95809653](../../evidence/state_effects-sets-046.md#s-d8a2825e95809653)

### path-009924

```text
(exec)# show ip dhcp snooping database <cr>
```

Handler ` RVA 0x15FAA370 `；selector ` 0 `；EOL ` RVA 0x35E80FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-083c33c693bb42d0](../../evidence/conditions-sets-004.md#c-083c33c693bb42d0) · [状态效果 S-0d6816248f4a7a2e](../../evidence/state_effects-sets-003.md#s-0d6816248f4a7a2e)

### path-009912

```text
(exec)# show ip dhcp snooping multi-chassis <cr>
```

Handler ` RVA 0x15FAAA70 `；selector ` 0 `；EOL ` RVA 0x35E801F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-845a992b6c2792a2](../../evidence/conditions-sets-051.md#c-845a992b6c2792a2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009925

```text
(exec)# show ip dhcp snooping statistics <cr>
```

Handler ` RVA 0x15FA9710 `；selector ` 0 `；EOL ` RVA 0x35E812F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-039b5552afb7a736](../../evidence/conditions-sets-002.md#c-039b5552afb7a736) · [状态效果 S-c4549a6dff2891ff](../../evidence/state_effects-sets-042.md#s-c4549a6dff2891ff)

### path-011415

```text
(exec)# show ip dhcp snooping track host <cr>
```

Handler ` RVA 0x15FA2CD0 `；selector ` 0 `；EOL ` RVA 0x35E7FF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-767a25932b4d150a](../../evidence/conditions-sets-046.md#c-767a25932b4d150a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024365

```text
(exec)# show ip dhcp vrf <string> binding * <cr>
```

Handler ` RVA 0xD298440 `；selector ` 8 `；EOL ` RVA 0x33DE08F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-4837786e78457c3f](../../evidence/conditions-sets-028.md#c-4837786e78457c3f) · [缺口 G-9e1b18fdc4821f49](../../evidence/gaps-sets-006.md#g-9e1b18fdc4821f49) · [参数 P-29398c16343455a3](../../evidence/parameters-sets-004.md#p-29398c16343455a3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011891

```text
(exec)# show ip dhcp vrf <string> binding <address> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 9 `；EOL ` RVA 0x33DE0C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name；` address ` Show a specific binding in a VRF。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-2b5d8d8b934943db](../../evidence/parameters-sets-004.md#p-2b5d8d8b934943db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011884

```text
(exec)# show ip dhcp vrf <string> binding assigned <cr>
```

Handler ` RVA 0xD298440 `；selector ` 8 `；EOL ` RVA 0x33DE08F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-29398c16343455a3](../../evidence/parameters-sets-004.md#p-29398c16343455a3) · [状态效果 S-b524e95ac37f373c](../../evidence/state_effects-sets-038.md#s-b524e95ac37f373c)

### path-006418

```text
(exec)# show ip dns name-list <cr>
```

Handler ` RVA 0xD16CAF0 `；selector ` 0 `；EOL ` RVA 0x33D9AAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006455

```text
(exec)# show ip dns primary <cr>
```

Handler ` RVA 0xD134080 `；selector ` 1 `；EOL ` RVA 0x33D9AD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006478

```text
(exec)# show ip dns servers <cr>
```

Handler ` RVA 0xD1337C0 `；selector ` 0 `；EOL ` RVA 0x33D9B2B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006444

```text
(exec)# show ip dns statistics <cr>
```

Handler ` RVA 0xD134080 `；selector ` 2 `；EOL ` RVA 0x33D9B010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006463

```text
(exec)# show ip dns view <cr>
```

Handler ` RVA 0xD132740 `；selector ` 0 `；EOL ` RVA 0x33D9A408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-812897e433780ac6](../../evidence/conditions-sets-050.md#c-812897e433780ac6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006386

```text
(exec)# show ip dns view-list <cr>
```

Handler ` RVA 0xD16E690 `；selector ` 0 `；EOL ` RVA 0x33D9A7B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001865

```text
(exec)# show ip domain-name <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 0 `；EOL ` RVA 0x33D32E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002023

```text
(exec)# show ip drp <cr>
```

Handler ` RVA 0xF4F09B0 `；selector ` 0 `；EOL ` RVA 0x34679008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006684

```text
(exec)# show ip eigrp accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x346DBEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6003dddf41312d2c](../../evidence/conditions-sets-037.md#c-6003dddf41312d2c) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-006673

```text
(exec)# show ip eigrp interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x346DADC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7bfeeea5f80fc52a](../../evidence/conditions-sets-048.md#c-7bfeeea5f80fc52a) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-019191

```text
(exec)# show ip eigrp interfaces <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x346DADC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eba8da5b7517863f](../../evidence/conditions-sets-091.md#c-eba8da5b7517863f) · [缺口 G-1d76c37cdf9433ef](../../evidence/gaps-sets-002.md#g-1d76c37cdf9433ef) · [参数 P-e9c8852ddbde1b77](../../evidence/parameters-sets-017.md#p-e9c8852ddbde1b77) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-006700

```text
(exec)# show ip eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x346DA8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-927b4a3f22128bea](../../evidence/conditions-sets-056.md#c-927b4a3f22128bea) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-019220

```text
(exec)# show ip eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x346DA8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aedfb9477946b70c](../../evidence/conditions-sets-068.md#c-aedfb9477946b70c) · [缺口 G-ea2bc9caefcb8e78](../../evidence/gaps-sets-008.md#g-ea2bc9caefcb8e78) · [参数 P-cfe916be7650cb18](../../evidence/parameters-sets-016.md#p-cfe916be7650cb18) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-006731

```text
(exec)# show ip eigrp sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x346DC240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6003dddf41312d2c](../../evidence/conditions-sets-037.md#c-6003dddf41312d2c) · [状态效果 S-2457c861d5ab8458](../../evidence/state_effects-sets-008.md#s-2457c861d5ab8458)

### path-006770

```text
(exec)# show ip eigrp sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x346DC5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6003dddf41312d2c](../../evidence/conditions-sets-037.md#c-6003dddf41312d2c) · [状态效果 S-f612d677add69252](../../evidence/state_effects-sets-052.md#s-f612d677add69252)

### path-006614

```text
(exec)# show ip eigrp timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x346DB098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6003dddf41312d2c](../../evidence/conditions-sets-037.md#c-6003dddf41312d2c) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-006849

```text
(exec)# show ip eigrp topology <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x346DB6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab91a49576e85efe](../../evidence/conditions-sets-066.md#c-ab91a49576e85efe) · [状态效果 S-02485ef74359b07a](../../evidence/state_effects-sets-001.md#s-02485ef74359b07a)

### path-019305

```text
(exec)# show ip eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x346DB6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-4254df732852e780](../../evidence/conditions-sets-026.md#c-4254df732852e780) · [缺口 G-293d570fc1b9fc60](../../evidence/gaps-sets-002.md#g-293d570fc1b9fc60) · [参数 P-7d6f9034aaa5c9b0](../../evidence/parameters-sets-010.md#p-7d6f9034aaa5c9b0) · [状态效果 S-2f09d5bf7d58e439](../../evidence/state_effects-sets-010.md#s-2f09d5bf7d58e439)

### path-006640

```text
(exec)# show ip eigrp traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x346DB340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6003dddf41312d2c](../../evidence/conditions-sets-037.md#c-6003dddf41312d2c) · [状态效果 S-84d7c8828485cb38](../../evidence/state_effects-sets-028.md#s-84d7c8828485cb38)

### path-002230

```text
(exec)# show ip extcommunity-list <cr>
```

Handler ` RVA 0xE246790 `；selector ` 0 `；EOL ` RVA 0x344BAF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e45a21ad3f834e4d](../../evidence/conditions-sets-088.md#c-e45a21ad3f834e4d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002358

```text
(exec)# show ip ftp-password <cr>
```

Handler ` RVA 0xD018280 `；selector ` 4 `；EOL ` RVA 0x33D856C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002341

```text
(exec)# show ip ftp-username <cr>
```

Handler ` RVA 0xD018280 `；selector ` 3 `；EOL ` RVA 0x33D85418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001926

```text
(exec)# show ip helper-address <cr>
```

Handler ` RVA 0xCF36E40 `；selector ` 0 `；EOL ` RVA 0x33D331B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e08880261b14824](../../evidence/conditions-sets-012.md#c-1e08880261b14824) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014223

```text
(exec)# show ip helper-address <interface> <cr>
```

Handler ` RVA 0xCF36E40 `；selector ` 0 `；EOL ` RVA 0x33D331B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0d1a32e17d9d282](../../evidence/conditions-sets-093.md#c-f0d1a32e17d9d282) · [缺口 G-23c1e3a3b9f23f38](../../evidence/gaps-sets-002.md#g-23c1e3a3b9f23f38) · [参数 P-d68acf3c1ecbff1a](../../evidence/parameters-sets-016.md#p-d68acf3c1ecbff1a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002647

```text
(exec)# show ip host-list <cr>
```

Handler ` RVA 0xF4878A0 `；selector ` 0 `；EOL ` RVA 0x3465B6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009426

```text
(exec)# show ip http client all <cr>
```

Handler ` RVA 0xD1D40C0 `；selector ` 14 `；EOL ` RVA 0x33DB4600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009519

```text
(exec)# show ip http client cache <cr>
```

Handler ` RVA 0xD1D3BD0 `；selector ` 16 `；EOL ` RVA 0x33DB4E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011254

```text
(exec)# show ip http client cache brief <cr>
```

Handler ` RVA 0xD1D3BD0 `；selector ` 17 `；EOL ` RVA 0x33DB4E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009470

```text
(exec)# show ip http client connection <cr>
```

Handler ` RVA 0xD1D3570 `；selector ` 20 `；EOL ` RVA 0x33DB4B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011297

```text
(exec)# show ip http client cookie summary <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 23 `；EOL ` RVA 0x33DB5A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-a62fbf512fbbba6a](../../evidence/state_effects-sets-035.md#s-a62fbf512fbbba6a)

### path-012048

```text
(exec)# show ip http client cookie summary domain <string> <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 25 `；EOL ` RVA 0x33DB5760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client cookie domain (or) host name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-5d48c863bc7d385e](../../evidence/parameters-sets-007.md#p-5d48c863bc7d385e) · [状态效果 S-a62fbf512fbbba6a](../../evidence/state_effects-sets-035.md#s-a62fbf512fbbba6a)

### path-012049

```text
(exec)# show ip http client cookie summary name <string> <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 26 `；EOL ` RVA 0x33DB5A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client cookie name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-acf97ba8b51a0b28](../../evidence/parameters-sets-013.md#p-acf97ba8b51a0b28) · [状态效果 S-a62fbf512fbbba6a](../../evidence/state_effects-sets-035.md#s-a62fbf512fbbba6a)

### path-012046

```text
(exec)# show ip http client cookie summary session <string> <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 24 `；EOL ` RVA 0x33DB5478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client session name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-64ac1130dd55272a](../../evidence/parameters-sets-008.md#p-64ac1130dd55272a) · [状态效果 S-a62fbf512fbbba6a](../../evidence/state_effects-sets-035.md#s-a62fbf512fbbba6a)

### path-009408

```text
(exec)# show ip http client history <cr>
```

Handler ` RVA 0xD1D39C0 `；selector ` 19 `；EOL ` RVA 0x33DB4358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011291

```text
(exec)# show ip http client secure status <cr>
```

Handler ` RVA 0xC49F370 `；selector ` 22 `；EOL ` RVA 0x33A9AA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009390

```text
(exec)# show ip http client session-module <cr>
```

Handler ` RVA 0xD1D3DD0 `；selector ` 15 `；EOL ` RVA 0x33DB40B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009447

```text
(exec)# show ip http client statistics <cr>
```

Handler ` RVA 0xD1D3930 `；selector ` 18 `；EOL ` RVA 0x33DB48A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009378

```text
(exec)# show ip http server all <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 1 `；EOL ` RVA 0x33DB1C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009448

```text
(exec)# show ip http server connection <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 10 `；EOL ` RVA 0x33DB3598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011251

```text
(exec)# show ip http server external registration <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 5 `；EOL ` RVA 0x33DB2AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c72a1ee4ab8da84](../../evidence/conditions-sets-042.md#c-6c72a1ee4ab8da84) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011845

```text
(exec)# show ip http server external registration <string> <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 6 `；EOL ` RVA 0x33DB2808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of registered url。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-fb0953dfbba3d052](../../evidence/parameters-sets-019.md#p-fb0953dfbba3d052) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011854

```text
(exec)# show ip http server external statistics data <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 9 `；EOL ` RVA 0x33DB32D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011849

```text
(exec)# show ip http server external statistics registration <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 8 `；EOL ` RVA 0x33DB3030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011847

```text
(exec)# show ip http server external statistics summary <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 7 `；EOL ` RVA 0x33DB2D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009513

```text
(exec)# show ip http server help-path <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 13 `；EOL ` RVA 0x33DB3D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009492

```text
(exec)# show ip http server history <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 12 `；EOL ` RVA 0x33DB3AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011292

```text
(exec)# show ip http server secure status <cr>
```

Handler ` RVA 0xC49E900 `；selector ` 21 `；EOL ` RVA 0x33A9A070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009458

```text
(exec)# show ip http server session-module <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 3 `；EOL ` RVA 0x33DB24D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7d2075b8e0d635af](../../evidence/conditions-sets-049.md#c-7d2075b8e0d635af) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011212

```text
(exec)# show ip http server session-module <string> <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 4 `；EOL ` RVA 0x33DB21F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a session module。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-c24c9205b4226549](../../evidence/parameters-sets-015.md#p-c24c9205b4226549) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009471

```text
(exec)# show ip http server statistics <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 11 `；EOL ` RVA 0x33DB3840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009393

```text
(exec)# show ip http server status <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 2 `；EOL ` RVA 0x33DB1EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005544

```text
(exec)# show ip icmp rate-limit <cr>
```

Handler ` RVA 0xCFE5270 `；selector ` 0 `；EOL ` RVA 0x33D31238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-573d2c66951dcbd3](../../evidence/conditions-sets-034.md#c-573d2c66951dcbd3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018013

```text
(exec)# show ip icmp rate-limit <interface> <cr>
```

Handler ` RVA 0xCFE5270 `；selector ` 0 `；EOL ` RVA 0x33D31238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a738ada2be7dcb09](../../evidence/conditions-sets-064.md#c-a738ada2be7dcb09) · [缺口 G-ed14de01b6abefba](../../evidence/gaps-sets-008.md#g-ed14de01b6abefba) · [参数 P-48a213035c927ce5](../../evidence/parameters-sets-006.md#p-48a213035c927ce5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006518

```text
(exec)# show ip igmp filter <cr>
```

Handler ` RVA 0xE7AFD20 `；selector ` 0 `；EOL ` RVA 0x343394C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66ea28c0a527f1af](../../evidence/conditions-sets-040.md#c-66ea28c0a527f1af) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006379

```text
(exec)# show ip igmp gir <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 42 `；EOL ` RVA 0x3472C608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-300c7d68399553a6](../../evidence/conditions-sets-019.md#c-300c7d68399553a6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006327

```text
(exec)# show ip igmp groups <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 4 `；EOL ` RVA 0x3472AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6c1377392a8fbec](../../evidence/conditions-sets-064.md#c-a6c1377392a8fbec) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018794

```text
(exec)# show ip igmp groups <interface> <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 4 `；EOL ` RVA 0x3472AE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-daea01d3038b1d79](../../evidence/conditions-sets-084.md#c-daea01d3038b1d79) · [缺口 G-d7ae899b084ec470](../../evidence/gaps-sets-007.md#g-d7ae899b084ec470) · [参数 P-40db9dd45ed1ddcd](../../evidence/parameters-sets-005.md#p-40db9dd45ed1ddcd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022172

```text
(exec)# show ip igmp groups <interface> detail <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 28 `；EOL ` RVA 0x3472ADF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-daea01d3038b1d79](../../evidence/conditions-sets-084.md#c-daea01d3038b1d79) · [缺口 G-d7ae899b084ec470](../../evidence/gaps-sets-007.md#g-d7ae899b084ec470) · [参数 P-40db9dd45ed1ddcd](../../evidence/parameters-sets-005.md#p-40db9dd45ed1ddcd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009414

```text
(exec)# show ip igmp groups detail <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 28 `；EOL ` RVA 0x3472ADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6c1377392a8fbec](../../evidence/conditions-sets-064.md#c-a6c1377392a8fbec) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006201

```text
(exec)# show ip igmp interface <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 5 `；EOL ` RVA 0x3472A9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3642715e1bd6858](../../evidence/conditions-sets-075.md#c-c3642715e1bd6858) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018671

```text
(exec)# show ip igmp interface <interface> <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 5 `；EOL ` RVA 0x3472A9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-455c4bf164e4bf32](../../evidence/conditions-sets-027.md#c-455c4bf164e4bf32) · [缺口 G-db75ed2e13a7b533](../../evidence/gaps-sets-008.md#g-db75ed2e13a7b533) · [参数 P-52e579f658d4dd94](../../evidence/parameters-sets-007.md#p-52e579f658d4dd94) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006392

```text
(exec)# show ip igmp membership <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 31 `；EOL ` RVA 0x3472BE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006522

```text
(exec)# show ip igmp profile <cr>
```

Handler ` RVA 0xE7B30A0 `；selector ` 2 `；EOL ` RVA 0x3433A878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66ea28c0a527f1af](../../evidence/conditions-sets-040.md#c-66ea28c0a527f1af) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009530

```text
(exec)# show ip igmp profile <number:1..4294967295> <cr>
```

Handler ` RVA 0xE7B30A0 `；selector ` 1 `；EOL ` RVA 0x3433A850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Profile number。

[条件 C-66ea28c0a527f1af](../../evidence/conditions-sets-040.md#c-66ea28c0a527f1af) · [参数 P-6dcf44850ec5b755](../../evidence/parameters-sets-009.md#p-6dcf44850ec5b755) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006629

```text
(exec)# show ip igmp snooping <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 10 `；EOL ` RVA 0x33A54C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e2a90b41b4f32b0](../../evidence/conditions-sets-031.md#c-4e2a90b41b4f32b0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011296

```text
(exec)# show ip igmp snooping bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 11 `；EOL ` RVA 0x33A47310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-930ef3002e026a8a](../../evidence/conditions-sets-057.md#c-930ef3002e026a8a) · [参数 P-62a440c0a1746977](../../evidence/parameters-sets-008.md#p-62a440c0a1746977) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011858

```text
(exec)# show ip igmp snooping bd <number:1006..4094> forced <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 29 `；EOL ` RVA 0x33A472E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-7a74309b791ad4f9](../../evidence/conditions-sets-047.md#c-7a74309b791ad4f9) · [参数 P-62a440c0a1746977](../../evidence/parameters-sets-008.md#p-62a440c0a1746977) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022333

```text
(exec)# show ip igmp snooping bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 11 `；EOL ` RVA 0x33A47310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-a0b1861a60322fab](../../evidence/conditions-sets-062.md#c-a0b1861a60322fab) · [缺口 G-4b0d124b1701eada](../../evidence/gaps-sets-003.md#g-4b0d124b1701eada) · [参数 P-5cad3408e6aed164](../../evidence/parameters-sets-007.md#p-5cad3408e6aed164) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024208

```text
(exec)# show ip igmp snooping bd <number:dynamic> forced <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 29 `；EOL ` RVA 0x33A472E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-3672bf86bce58aa9](../../evidence/conditions-sets-021.md#c-3672bf86bce58aa9) · [缺口 G-4b0d124b1701eada](../../evidence/gaps-sets-003.md#g-4b0d124b1701eada) · [参数 P-5cad3408e6aed164](../../evidence/parameters-sets-007.md#p-5cad3408e6aed164) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009591

```text
(exec)# show ip igmp snooping counters <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 77 `；EOL ` RVA 0x33A490A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e2a90b41b4f32b0](../../evidence/conditions-sets-031.md#c-4e2a90b41b4f32b0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011862

```text
(exec)# show ip igmp snooping counters bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 78 `；EOL ` RVA 0x33A490E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-a3fba4425965d831](../../evidence/conditions-sets-063.md#c-a3fba4425965d831) · [参数 P-14d525f738305481](../../evidence/parameters-sets-002.md#p-14d525f738305481) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024223

```text
(exec)# show ip igmp snooping counters bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 78 `；EOL ` RVA 0x33A490E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-3366b84208ae6986](../../evidence/conditions-sets-020.md#c-3366b84208ae6986) · [缺口 G-14ec10243bfe0091](../../evidence/gaps-sets-001.md#g-14ec10243bfe0091) · [参数 P-bab0e90ae4e41e57](../../evidence/parameters-sets-014.md#p-bab0e90ae4e41e57) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011860

```text
(exec)# show ip igmp snooping filter BD <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 51 `；EOL ` RVA 0x33A47950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-ce290e2a06eb9009](../../evidence/conditions-sets-079.md#c-ce290e2a06eb9009) · [参数 P-dae9d46e28f0594c](../../evidence/parameters-sets-016.md#p-dae9d46e28f0594c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024213

```text
(exec)# show ip igmp snooping filter BD <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 51 `；EOL ` RVA 0x33A47950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-7f76032dd53364a6](../../evidence/conditions-sets-049.md#c-7f76032dd53364a6) · [缺口 G-ca1533759929be84](../../evidence/gaps-sets-007.md#g-ca1533759929be84) · [参数 P-e71149ed3d713055](../../evidence/parameters-sets-017.md#p-e71149ed3d713055) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011316

```text
(exec)# show ip igmp snooping filter et <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 54 `；EOL ` RVA 0x33A47D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-254736ef868c5c96](../../evidence/conditions-sets-015.md#c-254736ef868c5c96) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024271

```text
(exec)# show ip igmp snooping filter interface <interface> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 52 `；EOL ` RVA 0x33A484D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6a85826359b2f6a](../../evidence/conditions-sets-071.md#c-b6a85826359b2f6a) · [缺口 G-08340c3d9423f65b](../../evidence/gaps-sets-001.md#g-08340c3d9423f65b) · [参数 P-f8df29fc34a51391](../../evidence/parameters-sets-019.md#p-f8df29fc34a51391) · [状态效果 S-e59a821817c73d1b](../../evidence/state_effects-sets-049.md#s-e59a821817c73d1b)

### path-024854

```text
(exec)# show ip igmp snooping filter interface <interface> statistics <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 53 `；EOL ` RVA 0x33A488A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6a85826359b2f6a](../../evidence/conditions-sets-071.md#c-b6a85826359b2f6a) · [缺口 G-08340c3d9423f65b](../../evidence/gaps-sets-001.md#g-08340c3d9423f65b) · [参数 P-f8df29fc34a51391](../../evidence/parameters-sets-019.md#p-f8df29fc34a51391) · [状态效果 S-e59a821817c73d1b](../../evidence/state_effects-sets-049.md#s-e59a821817c73d1b)

### path-009682

```text
(exec)# show ip igmp snooping groups <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 17 `；EOL ` RVA 0x33A4A138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0b864ed9401dd40](../../evidence/conditions-sets-087.md#c-e0b864ed9401dd40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011311

```text
(exec)# show ip igmp snooping groups count <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 18 `；EOL ` RVA 0x33A49CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e2a90b41b4f32b0](../../evidence/conditions-sets-031.md#c-4e2a90b41b4f32b0) · [状态效果 S-860754a3b008bdc6](../../evidence/state_effects-sets-028.md#s-860754a3b008bdc6)

### path-009749

```text
(exec)# show ip igmp snooping membership <cr>
```

Handler ` RVA 0xC31D110 `；selector ` 26 `；EOL ` RVA 0x33A5A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e2a90b41b4f32b0](../../evidence/conditions-sets-031.md#c-4e2a90b41b4f32b0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009611

```text
(exec)# show ip igmp snooping mrouter <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 12 `；EOL ` RVA 0x33A496D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4e2a90b41b4f32b0](../../evidence/conditions-sets-031.md#c-4e2a90b41b4f32b0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011864

```text
(exec)# show ip igmp snooping mrouter bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 13 `；EOL ` RVA 0x33A49710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-4c122300d9ad24d4](../../evidence/conditions-sets-030.md#c-4c122300d9ad24d4) · [参数 P-2f4b396e2c97b79a](../../evidence/parameters-sets-004.md#p-2f4b396e2c97b79a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024237

```text
(exec)# show ip igmp snooping mrouter bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 13 `；EOL ` RVA 0x33A49710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-54130c2976d310f7](../../evidence/conditions-sets-033.md#c-54130c2976d310f7) · [缺口 G-0aefb1ced3d0cc86](../../evidence/gaps-sets-001.md#g-0aefb1ced3d0cc86) · [参数 P-4253578c0de1914e](../../evidence/parameters-sets-006.md#p-4253578c0de1914e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009594

```text
(exec)# show ip igmp snooping querier <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 14 `；EOL ` RVA 0x33A48D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73bfc7a37135abea](../../evidence/conditions-sets-045.md#c-73bfc7a37135abea) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006262

```text
(exec)# show ip igmp ssm-mapping <cr>
```

Handler ` RVA 0xF6C18D0 `；selector ` 0 `；EOL ` RVA 0x3472B6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009454

```text
(exec)# show ip igmp static-group class-map <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 14 `；EOL ` RVA 0x3472C248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006323

```text
(exec)# show ip igmp udlr <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 6 `；EOL ` RVA 0x3472BA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006225

```text
(exec)# show ip igmp virtual-group-cache <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 41 `；EOL ` RVA 0x3472B3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005545

```text
(exec)# show ip interface address <cr>
```

Handler ` RVA 0xCF36F30 `；selector ` 0 `；EOL ` RVA 0x33D30310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef049e3cbb327973](../../evidence/conditions-sets-092.md#c-ef049e3cbb327973) · [状态效果 S-6c4bfffc4b9b8c1f](../../evidence/state_effects-sets-023.md#s-6c4bfffc4b9b8c1f)

### path-021884

```text
(exec)# show ip interface address <interface> stats <cr>
```

Handler ` RVA 0xCF38EA0 `；selector ` 0 `；EOL ` RVA 0x33D308D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a7bbd8373ed9f64](../../evidence/conditions-sets-029.md#c-4a7bbd8373ed9f64) · [缺口 G-a283d3503a383560](../../evidence/gaps-sets-006.md#g-a283d3503a383560) · [参数 P-eb983603e1fd151a](../../evidence/parameters-sets-018.md#p-eb983603e1fd151a) · [状态效果 S-6c4bfffc4b9b8c1f](../../evidence/state_effects-sets-023.md#s-6c4bfffc4b9b8c1f)

### path-024772

```text
(exec)# show ip interface address <interface> topology base stats <cr>
```

Handler ` RVA 0xCF38E30 `；selector ` 0 `；EOL ` RVA 0x33D30438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-06a9cd608c44ae07](../../evidence/conditions-sets-003.md#c-06a9cd608c44ae07) · [缺口 G-a283d3503a383560](../../evidence/gaps-sets-006.md#g-a283d3503a383560) · [参数 P-eb983603e1fd151a](../../evidence/parameters-sets-018.md#p-eb983603e1fd151a) · [状态效果 S-ff4597437a52d398](../../evidence/state_effects-sets-054.md#s-ff4597437a52d398)

### path-002103

```text
(exec)# show ip irdp <cr>
```

Handler ` RVA 0xE242F00 `；selector ` 0 `；EOL ` RVA 0x34285418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-211767c284449ac5](../../evidence/conditions-sets-013.md#c-211767c284449ac5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014405

```text
(exec)# show ip irdp <interface> <cr>
```

Handler ` RVA 0xE242F00 `；selector ` 0 `；EOL ` RVA 0x34285418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-67148425fb659201](../../evidence/conditions-sets-040.md#c-67148425fb659201) · [缺口 G-c8021c976e6b312d](../../evidence/gaps-sets-007.md#g-c8021c976e6b312d) · [参数 P-21e7ece8580a1d7c](../../evidence/parameters-sets-003.md#p-21e7ece8580a1d7c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002273

```text
(exec)# show ip largecommunity-list <cr>
```

Handler ` RVA 0xF24B100 `；selector ` 0 `；EOL ` RVA 0x344BB208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a6c8cbac1910b98](../../evidence/conditions-sets-004.md#c-0a6c8cbac1910b98) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005713

```text
(exec)# show ip local policy <cr>
```

Handler ` RVA 0xFAD8CE0 `；selector ` 0 `；EOL ` RVA 0x34804760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005802

```text
(exec)# show ip local pool <cr>
```

Handler ` RVA 0xCEB0290 `；selector ` 0 `；EOL ` RVA 0x33D18188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b465e2573dbddc6](../../evidence/conditions-sets-030.md#c-4b465e2573dbddc6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002139

```text
(exec)# show ip masks <cr>
```

Handler ` RVA 0xE1D6200 `；selector ` 0 `；EOL ` RVA 0x3422EDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b08a11e675f4114a](../../evidence/conditions-sets-068.md#c-b08a11e675f4114a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002327

```text
(exec)# show ip mcache <cr>
```

Handler ` RVA 0xF6D6320 `；selector ` 0 `；EOL ` RVA 0x3474EDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5804c2c7b89405b](../../evidence/conditions-sets-089.md#c-e5804c2c7b89405b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002858

```text
(exec)# show ip mfib <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-464994083e65d722](../../evidence/conditions-sets-027.md#c-464994083e65d722) · [状态效果 S-b45502040c715193](../../evidence/state_effects-sets-038.md#s-b45502040c715193)

### path-006789

```text
(exec)# show ip mfib cable <cr>
```

Handler ` RVA 0x1197DD40 `；selector ` 0 `；EOL ` RVA 0x355B4548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-1e2bf9e318e80a9c](../../evidence/state_effects-sets-007.md#s-1e2bf9e318e80a9c)

### path-006818

```text
(exec)# show ip mfib interface <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B54B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-393047ed2c8859fe](../../evidence/conditions-sets-022.md#c-393047ed2c8859fe) · [状态效果 S-bc863d9237b64356](../../evidence/state_effects-sets-040.md#s-bc863d9237b64356)

### path-009727

```text
(exec)# show ip mfib internal fibidb <cr>
```

Handler ` RVA 0x1197DE80 `；selector ` 0 `；EOL ` RVA 0x355B49A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-e24bcbf01c9d5470](../../evidence/state_effects-sets-048.md#s-e24bcbf01c9d5470)

### path-009827

```text
(exec)# show ip mfib internal mem <cr>
```

Handler ` RVA 0x1197DF50 `；selector ` 0 `；EOL ` RVA 0x355B4CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-0f9925699ceba333](../../evidence/state_effects-sets-004.md#s-0f9925699ceba333)

### path-006836

```text
(exec)# show ip mfib rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc84839fe0c9ae5c](../../evidence/conditions-sets-085.md#c-dc84839fe0c9ae5c) · [状态效果 S-f79fb9128dca0843](../../evidence/state_effects-sets-052.md#s-f79fb9128dca0843)

### path-006721

```text
(exec)# show ip mfib status <cr>
```

Handler ` RVA 0x1197C470 `；selector ` 0 `；EOL ` RVA 0x355B50E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-e24bcbf01c9d5470](../../evidence/state_effects-sets-048.md#s-e24bcbf01c9d5470)

### path-002400

```text
(exec)# show ip mpacket <cr>
```

Handler ` RVA 0xF70B090 `；selector ` 0 `；EOL ` RVA 0x347508C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8535f723b8a2931](../../evidence/conditions-sets-077.md#c-c8535f723b8a2931) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006751

```text
(exec)# show ip mrib client <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 1 `；EOL ` RVA 0x3537A9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-09ba2778bec2b657](../../evidence/state_effects-sets-002.md#s-09ba2778bec2b657)

### path-011367

```text
(exec)# show ip mrib route <address> <address> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3537A398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` source IP address；` address ` source IP address。

[条件 C-8ce7972629561859](../../evidence/conditions-sets-055.md#c-8ce7972629561859) · [参数 P-d7ab31900369f8e6](../../evidence/parameters-sets-016.md#p-d7ab31900369f8e6) · [状态效果 S-c320300680b93658](../../evidence/state_effects-sets-041.md#s-c320300680b93658)

### path-006821

```text
(exec)# show ip mrib route <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x35379F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e4b0f3b48613a5d](../../evidence/conditions-sets-061.md#c-9e4b0f3b48613a5d) · [状态效果 S-09ba2778bec2b657](../../evidence/state_effects-sets-002.md#s-09ba2778bec2b657)

### path-019372

```text
(exec)# show ip mrib route <prefix:dynamic> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3537A398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` group IP address/prefix length。

[条件 C-ee99487912a95eb1](../../evidence/conditions-sets-092.md#c-ee99487912a95eb1) · [缺口 G-12174f1388aa4471](../../evidence/gaps-sets-001.md#g-12174f1388aa4471) · [参数 P-bd5aaf12b2b81081](../../evidence/parameters-sets-014.md#p-bd5aaf12b2b81081) · [状态效果 S-09ba2778bec2b657](../../evidence/state_effects-sets-002.md#s-09ba2778bec2b657)

### path-009706

```text
(exec)# show ip mrib route summary <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 3 `；EOL ` RVA 0x35379BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-09ba2778bec2b657](../../evidence/state_effects-sets-002.md#s-09ba2778bec2b657)

### path-006559

```text
(exec)# show ip mrm interface <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 2 `；EOL ` RVA 0x3471FA18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2fc746684835954](../../evidence/conditions-sets-081.md#c-d2fc746684835954) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019073

```text
(exec)# show ip mrm interface <interface> <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 2 `；EOL ` RVA 0x3471FA18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-305ea9957cef1fab](../../evidence/conditions-sets-019.md#c-305ea9957cef1fab) · [缺口 G-a26ab3a82305f7d9](../../evidence/gaps-sets-006.md#g-a26ab3a82305f7d9) · [参数 P-ea1e4a7b740e8306](../../evidence/parameters-sets-018.md#p-ea1e4a7b740e8306) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006520

```text
(exec)# show ip mrm manager <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 1 `；EOL ` RVA 0x3471F6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006557

```text
(exec)# show ip mrm status-report <cr>
```

Handler ` RVA 0xF671F00 `；selector ` 3 `；EOL ` RVA 0x3471FD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002575

```text
(exec)# show ip mroute <cr>
```

Handler ` RVA 0xF741DF0 `；selector ` 0 `；EOL ` RVA 0x3474F2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9987836f13ae0d31](../../evidence/conditions-sets-059.md#c-9987836f13ae0d31) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006296

```text
(exec)# show ip msdp count <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 23 `；EOL ` RVA 0x3473CBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011206

```text
(exec)# show ip msdp peer <address> accepted-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 27 `；EOL ` RVA 0x3473C668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011195

```text
(exec)# show ip msdp peer <address> advertised-SAs <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 26 `；EOL ` RVA 0x3473C3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer name or address。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-215ab85ec08c212f](../../evidence/parameters-sets-003.md#p-215ab85ec08c212f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006261

```text
(exec)# show ip msdp peer <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 25 `；EOL ` RVA 0x3473C380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009406

```text
(exec)# show ip msdp rpf-peer <address> <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 24 `；EOL ` RVA 0x3473CE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` RP name or address。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-1e4a8b942f0e7cfd](../../evidence/parameters-sets-003.md#p-1e4a8b942f0e7cfd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006300

```text
(exec)# show ip msdp sa-cache <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 22 `；EOL ` RVA 0x3473BBE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3abd48937b0ceacc](../../evidence/conditions-sets-023.md#c-3abd48937b0ceacc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006152

```text
(exec)# show ip msdp summary <cr>
```

Handler ` RVA 0xF78DB60 `；selector ` 21 `；EOL ` RVA 0x3473B8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002403

```text
(exec)# show ip multicast <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 0 `；EOL ` RVA 0x34770E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2863c5d5b092e25c](../../evidence/conditions-sets-016.md#c-2863c5d5b092e25c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009317

```text
(exec)# show ip multicast gir clients <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 6 `；EOL ` RVA 0x3474C4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a527e69e720f2b8c](../../evidence/conditions-sets-064.md#c-a527e69e720f2b8c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006228

```text
(exec)# show ip multicast interface <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 2 `；EOL ` RVA 0x3474D178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-53611cab13ba6968](../../evidence/conditions-sets-033.md#c-53611cab13ba6968) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018702

```text
(exec)# show ip multicast interface <interface> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 2 `；EOL ` RVA 0x3474D178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-031fe20c17ed6999](../../evidence/conditions-sets-002.md#c-031fe20c17ed6999) · [缺口 G-361d0c48fadd2b96](../../evidence/gaps-sets-002.md#g-361d0c48fadd2b96) · [参数 P-acd724441907d345](../../evidence/parameters-sets-013.md#p-acd724441907d345) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006265

```text
(exec)# show ip multicast limit <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 1 `；EOL ` RVA 0x3474D520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95ee56e8e734fd7a](../../evidence/conditions-sets-058.md#c-95ee56e8e734fd7a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018732

```text
(exec)# show ip multicast limit <interface> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 1 `；EOL ` RVA 0x3474D520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d92eb97fe72d85d8](../../evidence/conditions-sets-084.md#c-d92eb97fe72d85d8) · [缺口 G-71dd44afeefd19a3](../../evidence/gaps-sets-004.md#g-71dd44afeefd19a3) · [参数 P-864e86fd306f3647](../../evidence/parameters-sets-010.md#p-864e86fd306f3647) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006254

```text
(exec)# show ip multicast lisp-rloc-state <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 5 `；EOL ` RVA 0x3474DC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-500ff4a0f1d00c67](../../evidence/conditions-sets-031.md#c-500ff4a0f1d00c67) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011172

```text
(exec)# show ip multicast mpls mrib-client ipv4 <cr>
```

Handler ` RVA 0xF7114E0 `；selector ` 0 `；EOL ` RVA 0x3474C8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a44a626a55731237](../../evidence/conditions-sets-063.md#c-a44a626a55731237) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011183

```text
(exec)# show ip multicast mpls mrib-client ipv6 <cr>
```

Handler ` RVA 0xF711410 `；selector ` 0 `；EOL ` RVA 0x3474CB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a44a626a55731237](../../evidence/conditions-sets-063.md#c-a44a626a55731237) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009356

```text
(exec)# show ip multicast mpls vif <cr>
```

Handler ` RVA 0xF7113A0 `；selector ` 0 `；EOL ` RVA 0x3474CDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a44a626a55731237](../../evidence/conditions-sets-063.md#c-a44a626a55731237) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011252

```text
(exec)# show ip multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 8 `；EOL ` RVA 0x3474E0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Overlay group address。

[条件 C-bd1df820ef59d9b2](../../evidence/conditions-sets-073.md#c-bd1df820ef59d9b2) · [参数 P-c33f2326c4cd42ed](../../evidence/parameters-sets-015.md#p-c33f2326c4cd42ed) · [状态效果 S-1d0042c818ae5830](../../evidence/state_effects-sets-007.md#s-1d0042c818ae5830)

### path-009661

```text
(exec)# show ip multicast redundancy ole <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 2 `；EOL ` RVA 0x33E52298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5372855a732cb028](../../evidence/conditions-sets-033.md#c-5372855a732cb028) · [状态效果 S-98207274411356a0](../../evidence/state_effects-sets-032.md#s-98207274411356a0)

### path-022392

```text
(exec)# show ip multicast redundancy reachability <?ipv4orv6_addr_action@5555893a5f60> <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 3 `；EOL ` RVA 0x33E51F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b53c17a996a2086](../../evidence/conditions-sets-048.md#c-7b53c17a996a2086) · [缺口 G-c409a7e8a8282212](../../evidence/gaps-sets-007.md#g-c409a7e8a8282212) · [状态效果 S-98207274411356a0](../../evidence/state_effects-sets-032.md#s-98207274411356a0)

### path-011301

```text
(exec)# show ip multicast redundancy reachability summary <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 3 `；EOL ` RVA 0x33E51F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7b53c17a996a2086](../../evidence/conditions-sets-048.md#c-7b53c17a996a2086) · [状态效果 S-be6dded6d3e49c69](../../evidence/state_effects-sets-040.md#s-be6dded6d3e49c69)

### path-009557

```text
(exec)# show ip multicast redundancy state <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 0 `；EOL ` RVA 0x33E51948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2863c5d5b092e25c](../../evidence/conditions-sets-016.md#c-2863c5d5b092e25c) · [状态效果 S-98207274411356a0](../../evidence/state_effects-sets-032.md#s-98207274411356a0)

### path-009553

```text
(exec)# show ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 1 `；EOL ` RVA 0x33E51BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2863c5d5b092e25c](../../evidence/conditions-sets-016.md#c-2863c5d5b092e25c) · [状态效果 S-98207274411356a0](../../evidence/state_effects-sets-032.md#s-98207274411356a0)

### path-009312

```text
(exec)# show ip multicast rpf monitored <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 3 `；EOL ` RVA 0x3474C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011850

```text
(exec)# show ip multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 60 `；EOL ` RVA 0x33A5DEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-2863c5d5b092e25c](../../evidence/conditions-sets-016.md#c-2863c5d5b092e25c) · [参数 P-236b3a3e749d1c7b](../../evidence/parameters-sets-003.md#p-236b3a3e749d1c7b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009539

```text
(exec)# show ip multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 70 `；EOL ` RVA 0x33A5E1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2863c5d5b092e25c](../../evidence/conditions-sets-016.md#c-2863c5d5b092e25c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011855

```text
(exec)# show ip multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 68 `；EOL ` RVA 0x33A5E230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-2863c5d5b092e25c](../../evidence/conditions-sets-016.md#c-2863c5d5b092e25c) · [参数 P-0e6e0511934953b5](../../evidence/parameters-sets-002.md#p-0e6e0511934953b5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006317

```text
(exec)# show ip multicast timer <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 7 `；EOL ` RVA 0x3474E490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1935d7c6b76c2d1](../../evidence/conditions-sets-081.md#c-d1935d7c6b76c2d1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006393

```text
(exec)# show ip multicast topology <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 4 `；EOL ` RVA 0x3474D988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be5798f577b8d5dd](../../evidence/conditions-sets-073.md#c-be5798f577b8d5dd) · [状态效果 S-feb1f22c04ba99ec](../../evidence/state_effects-sets-054.md#s-feb1f22c04ba99ec)

### path-001852

```text
(exec)# show ip name-servers <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 2 `；EOL ` RVA 0x33D328D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009690

```text
(exec)# show ip nat aggregation top-100-allocator <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 9 `；EOL ` RVA 0x347DB178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-024d64af34db730e](../../evidence/conditions-sets-001.md#c-024d64af34db730e) · [状态效果 S-94bef3f776ec0d02](../../evidence/state_effects-sets-032.md#s-94bef3f776ec0d02)

### path-006799

```text
(exec)# show ip nat alias-usecount <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 10 `；EOL ` RVA 0x347DC148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6029d9efd46f44b3](../../evidence/conditions-sets-037.md#c-6029d9efd46f44b3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006638

```text
(exec)# show ip nat bpa <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 5 `；EOL ` RVA 0x347DA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-193d9f05a2dd85cc](../../evidence/conditions-sets-010.md#c-193d9f05a2dd85cc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009765

```text
(exec)# show ip nat dia track <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 12 `；EOL ` RVA 0x347DBB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beb9e4ba9899399b](../../evidence/conditions-sets-074.md#c-beb9e4ba9899399b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006780

```text
(exec)# show ip nat entry-static <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 11 `；EOL ` RVA 0x347DBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-712c25594c4e7981](../../evidence/conditions-sets-044.md#c-712c25594c4e7981) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006829

```text
(exec)# show ip nat ha <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 0 `；EOL ` RVA 0x34CE8678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e372799d653bec7](../../evidence/conditions-sets-012.md#c-1e372799d653bec7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011366

```text
(exec)# show ip nat ha inside destination <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 7 `；EOL ` RVA 0x34CE71F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-98fe7756a188c0ea](../../evidence/conditions-sets-059.md#c-98fe7756a188c0ea) · [状态效果 S-d29211dcd32821e6](../../evidence/state_effects-sets-045.md#s-d29211dcd32821e6)

### path-012050

```text
(exec)# show ip nat ha inside destination list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 6 `；EOL ` RVA 0x34CE7230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-98fe7756a188c0ea](../../evidence/conditions-sets-059.md#c-98fe7756a188c0ea) · [参数 P-9c7276b446f8ff6f](../../evidence/parameters-sets-012.md#p-9c7276b446f8ff6f) · [状态效果 S-d29211dcd32821e6](../../evidence/state_effects-sets-045.md#s-d29211dcd32821e6)

### path-011362

```text
(exec)# show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 3 `；EOL ` RVA 0x34CE5E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8fdb423466be0f66](../../evidence/conditions-sets-056.md#c-8fdb423466be0f66) · [状态效果 S-2027fd7ad45292c9](../../evidence/state_effects-sets-007.md#s-2027fd7ad45292c9)

### path-011375

```text
(exec)# show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 5 `；EOL ` RVA 0x34CE6298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83083c856b57aebc](../../evidence/conditions-sets-051.md#c-83083c856b57aebc) · [状态效果 S-2027fd7ad45292c9](../../evidence/state_effects-sets-007.md#s-2027fd7ad45292c9)

### path-012137

```text
(exec)# show ip nat ha inside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 4 `；EOL ` RVA 0x34CE64A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-83083c856b57aebc](../../evidence/conditions-sets-051.md#c-83083c856b57aebc) · [参数 P-93cfcae875ad4313](../../evidence/parameters-sets-011.md#p-93cfcae875ad4313) · [状态效果 S-2027fd7ad45292c9](../../evidence/state_effects-sets-007.md#s-2027fd7ad45292c9)

### path-009811

```text
(exec)# show ip nat ha mappings <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 11 `；EOL ` RVA 0x34CE8650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e372799d653bec7](../../evidence/conditions-sets-012.md#c-1e372799d653bec7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011378

```text
(exec)# show ip nat ha outside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 10 `；EOL ` RVA 0x34CE7D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e372799d653bec7](../../evidence/conditions-sets-012.md#c-1e372799d653bec7) · [状态效果 S-acee76df60fefabc](../../evidence/state_effects-sets-037.md#s-acee76df60fefabc)

### path-012051

```text
(exec)# show ip nat ha outside source list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 8 `；EOL ` RVA 0x34CE79C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-1e372799d653bec7](../../evidence/conditions-sets-012.md#c-1e372799d653bec7) · [参数 P-b102d76a95775281](../../evidence/parameters-sets-013.md#p-b102d76a95775281) · [状态效果 S-acee76df60fefabc](../../evidence/state_effects-sets-037.md#s-acee76df60fefabc)

### path-012136

```text
(exec)# show ip nat ha outside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 9 `；EOL ` RVA 0x34CE7F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-1e372799d653bec7](../../evidence/conditions-sets-012.md#c-1e372799d653bec7) · [参数 P-bac6837be306eb44](../../evidence/parameters-sets-014.md#p-bac6837be306eb44) · [状态效果 S-acee76df60fefabc](../../evidence/state_effects-sets-037.md#s-acee76df60fefabc)

### path-009773

```text
(exec)# show ip nat ha pool <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 2 `；EOL ` RVA 0x34CE57E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eb9ca0834663b60c](../../evidence/conditions-sets-091.md#c-eb9ca0834663b60c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011350

```text
(exec)# show ip nat ha pool <string> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 1 `；EOL ` RVA 0x34CE57C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-eb9ca0834663b60c](../../evidence/conditions-sets-091.md#c-eb9ca0834663b60c) · [参数 P-9337e862cefa55d7](../../evidence/parameters-sets-011.md#p-9337e862cefa55d7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009724

```text
(exec)# show ip nat limits all-host <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 4 `；EOL ` RVA 0x347DA148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2571a3f518519d4a](../../evidence/conditions-sets-015.md#c-2571a3f518519d4a) · [状态效果 S-86bdcaf2f06e0f74](../../evidence/state_effects-sets-029.md#s-86bdcaf2f06e0f74)

### path-006729

```text
(exec)# show ip nat map <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 7 `；EOL ` RVA 0x347DB578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea98c059beec8bfa](../../evidence/conditions-sets-091.md#c-ea98c059beec8bfa) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006583

```text
(exec)# show ip nat platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 3 `；EOL ` RVA 0x347D94C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009710

```text
(exec)# show ip nat pool platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 6 `；EOL ` RVA 0x347DADD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9173fdf2e288a8d3](../../evidence/conditions-sets-056.md#c-9173fdf2e288a8d3) · [状态效果 S-43ef4f738e5dcc12](../../evidence/state_effects-sets-015.md#s-43ef4f738e5dcc12)

### path-009635

```text
(exec)# show ip nat portblock pat <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 2 `；EOL ` RVA 0x347D9910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb713cfc77ac281f](../../evidence/conditions-sets-072.md#c-bb713cfc77ac281f) · [状态效果 S-13b7ab61e0b0b53f](../../evidence/state_effects-sets-005.md#s-13b7ab61e0b0b53f)

### path-006746

```text
(exec)# show ip nat route-dia <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 8 `；EOL ` RVA 0x347DB840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7554f4fea0cf35d8](../../evidence/conditions-sets-046.md#c-7554f4fea0cf35d8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006621

```text
(exec)# show ip nat statistics <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 1 `；EOL ` RVA 0x347DA700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-998b575abb2ff5bc](../../evidence/conditions-sets-059.md#c-998b575abb2ff5bc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006874

```text
(exec)# show ip nat status <cr>
```

Handler ` RVA 0xFA2FB50 `；selector ` 0 `；EOL ` RVA 0x347DC440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63964d0505049c32](../../evidence/conditions-sets-039.md#c-63964d0505049c32) · [状态效果 S-e3fc4895d86512f5](../../evidence/state_effects-sets-048.md#s-e3fc4895d86512f5)

### path-006792

```text
(exec)# show ip nat translations <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 0 `；EOL ` RVA 0x347D7750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-317a21ee9e267e48](../../evidence/conditions-sets-019.md#c-317a21ee9e267e48) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025422

```text
(exec)# show ip nbar attribute <?option@55558a79a9e0> <?option@55558a79ab48> <?option@55558a79ac48> <?option@55558a79ad48> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 60 `；EOL ` RVA 0x35246E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ef8f6ae83ace6056](../../evidence/conditions-sets-093.md#c-ef8f6ae83ace6056) · [缺口 G-669af0bc54f8680c](../../evidence/gaps-sets-004.md#g-669af0bc54f8680c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025347

```text
(exec)# show ip nbar attribute <?option@55558a79a9e0> <?signed_number_func_action@55558a79b578> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 21 `；EOL ` RVA 0x35246CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9fad880b2ec89252](../../evidence/conditions-sets-062.md#c-9fad880b2ec89252) · [缺口 G-d789f3d2e27ad4fe](../../evidence/gaps-sets-007.md#g-d789f3d2e27ad4fe) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019004

```text
(exec)# show ip nbar attribute <?option@55558a79a9e0> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 20 `；EOL ` RVA 0x35246BB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1c2dc169ad3edbee](../../evidence/conditions-sets-011.md#c-1c2dc169ad3edbee) · [缺口 G-e7c8595bed475462](../../evidence/gaps-sets-008.md#g-e7c8595bed475462) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006388

```text
(exec)# show ip nbar attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 19 `；EOL ` RVA 0x35246A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006515

```text
(exec)# show ip nbar attribute-custom <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 36 `；EOL ` RVA 0x35248AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96cbe7288fb81dee](../../evidence/conditions-sets-058.md#c-96cbe7288fb81dee) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006521

```text
(exec)# show ip nbar attribute-map <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 26 `；EOL ` RVA 0x35248618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96cbe7288fb81dee](../../evidence/conditions-sets-058.md#c-96cbe7288fb81dee) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009529

```text
(exec)# show ip nbar attribute-map <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 25 `；EOL ` RVA 0x352485F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Attribute Map name。

[条件 C-96cbe7288fb81dee](../../evidence/conditions-sets-058.md#c-96cbe7288fb81dee) · [参数 P-00d2c85d1e33763e](../../evidence/parameters-sets-001.md#p-00d2c85d1e33763e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012132

```text
(exec)# show ip nbar classification cache sync export format table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 54 `；EOL ` RVA 0x352440D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1583fef683a80834](../../evidence/conditions-sets-008.md#c-1583fef683a80834) · [状态效果 S-b1f8b1b124b92ece](../../evidence/state_effects-sets-038.md#s-b1f8b1b124b92ece)

### path-012043

```text
(exec)# show ip nbar classification cache sync import last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x35244498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f1c66aae229318c3](../../evidence/conditions-sets-093.md#c-f1c66aae229318c3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011243

```text
(exec)# show ip nbar classification dns learning <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 44 `；EOL ` RVA 0x35243730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012044

```text
(exec)# show ip nbar classification dns learning cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 45 `；EOL ` RVA 0x352428C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025159

```text
(exec)# show ip nbar classification dns learning cache <number:1..100000> protocol <?option@55558a796510> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 48 `；EOL ` RVA 0x35242610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-ee7a7d0001423b05](../../evidence/conditions-sets-092.md#c-ee7a7d0001423b05) · [缺口 G-53287de20e574113](../../evidence/gaps-sets-003.md#g-53287de20e574113) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012128

```text
(exec)# show ip nbar classification dns learning cache <number:1..100000> unclassified <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 50 `；EOL ` RVA 0x352428A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012130

```text
(exec)# show ip nbar classification dns learning cache clients-servers <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 46 `；EOL ` RVA 0x35242E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-c79de3b2a66f150c](../../evidence/parameters-sets-015.md#p-c79de3b2a66f150c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025215

```text
(exec)# show ip nbar classification dns learning cache clients-servers <number:1..100000> protocol <?option@55558a796e50> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 49 `；EOL ` RVA 0x35242F50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-1fd90165e758667b](../../evidence/conditions-sets-012.md#c-1fd90165e758667b) · [缺口 G-64b7fc008b189aca](../../evidence/gaps-sets-004.md#g-64b7fc008b189aca) · [参数 P-c79de3b2a66f150c](../../evidence/parameters-sets-015.md#p-c79de3b2a66f150c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012129

```text
(exec)# show ip nbar classification dns learning cache ip-address <address> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 47 `；EOL ` RVA 0x35243470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 address。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-d80f378e85a44dd1](../../evidence/parameters-sets-016.md#p-d80f378e85a44dd1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011846

```text
(exec)# show ip nbar classification dns learning stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 51 `；EOL ` RVA 0x35243708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009415

```text
(exec)# show ip nbar classification granularity <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 38 `；EOL ` RVA 0x35241B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024149

```text
(exec)# show ip nbar classification granularity protocol <?option@55558a795b48> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 39 `；EOL ` RVA 0x35241C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eb30483075ff64ab](../../evidence/conditions-sets-091.md#c-eb30483075ff64ab) · [缺口 G-1c48352e6920e863](../../evidence/gaps-sets-001.md#g-1c48352e6920e863) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011220

```text
(exec)# show ip nbar classification granularity protocol <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 40 `；EOL ` RVA 0x35241BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011236

```text
(exec)# show ip nbar classification socket-cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 52 `；EOL ` RVA 0x35244788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of sockets to show。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-6099c4f0a96ec586](../../evidence/parameters-sets-008.md#p-6099c4f0a96ec586) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011259

```text
(exec)# show ip nbar classification socket-cache pl-sockets <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 53 `；EOL ` RVA 0x35244A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006182

```text
(exec)# show ip nbar control-plane <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 42 `；EOL ` RVA 0x35241228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009432

```text
(exec)# show ip nbar function <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 37 `；EOL ` RVA 0x35244E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Function name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-d038cc713a4324ff](../../evidence/parameters-sets-016.md#p-d038cc713a4324ff) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018993

```text
(exec)# show ip nbar link-age <?option@55558a79bf48> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 2 `；EOL ` RVA 0x35248070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-43d533f6e54c3ca8](../../evidence/conditions-sets-027.md#c-43d533f6e54c3ca8) · [缺口 G-136e7033e55c606d](../../evidence/gaps-sets-001.md#g-136e7033e55c606d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006457

```text
(exec)# show ip nbar link-age <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 3 `；EOL ` RVA 0x35247FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009379

```text
(exec)# show ip nbar npc detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 64 `；EOL ` RVA 0x35241538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5213b935ae02128c](../../evidence/conditions-sets-032.md#c-5213b935ae02128c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009394

```text
(exec)# show ip nbar npc summary <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 65 `；EOL ` RVA 0x352417E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd7f7a0b3419e594](../../evidence/conditions-sets-085.md#c-dd7f7a0b3419e594) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022263

```text
(exec)# show ip nbar parameter extraction <?option@55558a799320> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 28 `；EOL ` RVA 0x352454B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e99dbd117ca72c64](../../evidence/conditions-sets-090.md#c-e99dbd117ca72c64) · [缺口 G-41761292c625804c](../../evidence/gaps-sets-003.md#g-41761292c625804c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024167

```text
(exec)# show ip nbar parameter extraction <?option@55558a799320> activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 29 `；EOL ` RVA 0x35245488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e99dbd117ca72c64](../../evidence/conditions-sets-090.md#c-e99dbd117ca72c64) · [缺口 G-41761292c625804c](../../evidence/gaps-sets-003.md#g-41761292c625804c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009474

```text
(exec)# show ip nbar parameter extraction <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 34 `；EOL ` RVA 0x352459A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011238

```text
(exec)# show ip nbar parameter extraction activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 35 `；EOL ` RVA 0x35245980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022289

```text
(exec)# show ip nbar parameter subclassification <?option@55558a799e80> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 30 `；EOL ` RVA 0x35245FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-915af9710e80108f](../../evidence/conditions-sets-056.md#c-915af9710e80108f) · [缺口 G-b928edce73d1eca0](../../evidence/gaps-sets-007.md#g-b928edce73d1eca0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024176

```text
(exec)# show ip nbar parameter subclassification <?option@55558a799e80> activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 31 `；EOL ` RVA 0x35245FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-915af9710e80108f](../../evidence/conditions-sets-056.md#c-915af9710e80108f) · [缺口 G-b928edce73d1eca0](../../evidence/gaps-sets-007.md#g-b928edce73d1eca0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009494

```text
(exec)# show ip nbar parameter subclassification <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 32 `；EOL ` RVA 0x352464E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011245

```text
(exec)# show ip nbar parameter subclassification activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 33 `；EOL ` RVA 0x352464C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018952

```text
(exec)# show ip nbar protocol-attribute <?option@55558a79b948> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 23 `；EOL ` RVA 0x35247A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5a11cb49b3ae311d](../../evidence/conditions-sets-035.md#c-5a11cb49b3ae311d) · [缺口 G-ba29e7926f65a2b5](../../evidence/gaps-sets-007.md#g-ba29e7926f65a2b5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006423

```text
(exec)# show ip nbar protocol-attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 22 `；EOL ` RVA 0x352479E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006820

```text
(exec)# show ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F338B0 `；selector ` 0 `；EOL ` RVA 0x3524DED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e650c1566de3a692](../../evidence/conditions-sets-089.md#c-e650c1566de3a692) · [状态效果 S-38ebbfe72290f826](../../evidence/state_effects-sets-013.md#s-38ebbfe72290f826)

### path-019132

```text
(exec)# show ip nbar protocol-id <?option@55558a79f970> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 43 `；EOL ` RVA 0x3524BAA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31d7afcc814c211c](../../evidence/conditions-sets-020.md#c-31d7afcc814c211c) · [缺口 G-cb6064e297dd7b3c](../../evidence/gaps-sets-007.md#g-cb6064e297dd7b3c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006581

```text
(exec)# show ip nbar protocol-id <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 0 `；EOL ` RVA 0x3524BA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd96f1037804e673](../../evidence/conditions-sets-085.md#c-dd96f1037804e673) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009663

```text
(exec)# show ip nbar protocol-pack <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 12 `；EOL ` RVA 0x3524AEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-df4ccfe02099f3bf](../../evidence/conditions-sets-086.md#c-df4ccfe02099f3bf) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011310

```text
(exec)# show ip nbar protocol-pack <string> detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 11 `；EOL ` RVA 0x3524AC10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-df4ccfe02099f3bf](../../evidence/conditions-sets-086.md#c-df4ccfe02099f3bf) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011321

```text
(exec)# show ip nbar protocol-pack <string> taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 13 `；EOL ` RVA 0x3524AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-df4ccfe02099f3bf](../../evidence/conditions-sets-086.md#c-df4ccfe02099f3bf) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009576

```text
(exec)# show ip nbar protocol-pack active <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 5 `；EOL ` RVA 0x35249130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011270

```text
(exec)# show ip nbar protocol-pack active detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 4 `；EOL ` RVA 0x35248E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011281

```text
(exec)# show ip nbar protocol-pack active taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 14 `；EOL ` RVA 0x35249108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009593

```text
(exec)# show ip nbar protocol-pack inactive <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 7 `；EOL ` RVA 0x35249940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011279

```text
(exec)# show ip nbar protocol-pack inactive detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 6 `；EOL ` RVA 0x35249670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011305

```text
(exec)# show ip nbar protocol-pack inactive taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 16 `；EOL ` RVA 0x352499A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011857

```text
(exec)# show ip nbar protocol-pack inactive taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 15 `；EOL ` RVA 0x35249980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR inactive protocol pack name。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [参数 P-677a9bb0ef608bac](../../evidence/parameters-sets-008.md#p-677a9bb0ef608bac) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009612

```text
(exec)# show ip nbar protocol-pack loaded <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 9 `；EOL ` RVA 0x3524A3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011289

```text
(exec)# show ip nbar protocol-pack loaded detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 8 `；EOL ` RVA 0x3524A128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011315

```text
(exec)# show ip nbar protocol-pack loaded taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 18 `；EOL ` RVA 0x3524A460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011859

```text
(exec)# show ip nbar protocol-pack loaded taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 17 `；EOL ` RVA 0x3524A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` NBAR loaded protocol pack name。

[条件 C-f7984553236e75b1](../../evidence/conditions-sets-096.md#c-f7984553236e75b1) · [参数 P-658de79b2d501530](../../evidence/parameters-sets-008.md#p-658de79b2d501530) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006648

```text
(exec)# show ip nbar resources <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 20 `；EOL ` RVA 0x3524C368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009645

```text
(exec)# show ip nbar resources flow <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 24 `；EOL ` RVA 0x3524C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f5a454ef9cbbe57](../../evidence/conditions-sets-062.md#c-9f5a454ef9cbbe57) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009723

```text
(exec)# show ip nbar resources status <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 19 `；EOL ` RVA 0x3524CE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011341

```text
(exec)# show ip nbar resources status <number:10..86400> <cr>
```

Handler ` RVA 0x10F219A0 `；selector ` 22 `；EOL ` RVA 0x3524CEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [参数 P-49c60d7b54c4f3ee](../../evidence/parameters-sets-006.md#p-49c60d7b54c4f3ee) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011869

```text
(exec)# show ip nbar resources status <number:10..86400> <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 23 `；EOL ` RVA 0x3524CEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)；` unsigned_number ` Number of links to view。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [参数 P-d71cbaf17a27d2ca](../../evidence/parameters-sets-016.md#p-d71cbaf17a27d2ca) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011337

```text
(exec)# show ip nbar resources status fadebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 24 `；EOL ` RVA 0x3524C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011866

```text
(exec)# show ip nbar resources status fadebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 25 `；EOL ` RVA 0x3524C968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [参数 P-663e50933124a4cf](../../evidence/parameters-sets-008.md#p-663e50933124a4cf) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011331

```text
(exec)# show ip nbar resources status freebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 26 `；EOL ` RVA 0x3524C438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab456b9cb3f5c3b4](../../evidence/conditions-sets-066.md#c-ab456b9cb3f5c3b4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)
