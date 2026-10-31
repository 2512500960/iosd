# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-040600

```text
(config)# do-exec show ip rsvp metadata <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A32250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-034ccd44d0c4d08a](../../evidence/state_effects-sets-001.md#s-034ccd44d0c4d08a)

### path-040549

```text
(config)# do-exec show ip rsvp neighbor <cr>
```

Handler ` RVA 0x1006DCE0 `；selector ` 0 `；EOL ` RVA 0x34A309B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-480db0fc85345389](../../evidence/state_effects-sets-016.md#s-480db0fc85345389)

### path-049670

```text
(config)# do-exec show ip rsvp neighbor queues <cr>
```

Handler ` RVA 0x1006DB00 `；selector ` 0 `；EOL ` RVA 0x34A30C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c1ac38b85e1fb7bb](../../evidence/conditions-sets-075.md#c-c1ac38b85e1fb7bb) · [状态效果 S-480db0fc85345389](../../evidence/state_effects-sets-016.md#s-480db0fc85345389)

### path-062116

```text
(config)# do-exec show ip rsvp neighbor vrf * <cr>
```

Handler ` RVA 0x1006DCE0 `；selector ` 0 `；EOL ` RVA 0x34A309B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1df4553151ccaa9b](../../evidence/conditions-sets-012.md#c-1df4553151ccaa9b) · [缺口 G-d6764b42fac56013](../../evidence/gaps-sets-007.md#g-d6764b42fac56013) · [状态效果 S-d1b4353fe17e1009](../../evidence/state_effects-sets-044.md#s-d1b4353fe17e1009)

### path-062412

```text
(config)# do-exec show ip rsvp neighbor vrf * queues <cr>
```

Handler ` RVA 0x1006DB00 `；selector ` 0 `；EOL ` RVA 0x34A30C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e63eaf5d3cbf20bf](../../evidence/conditions-sets-089.md#c-e63eaf5d3cbf20bf) · [缺口 G-d6764b42fac56013](../../evidence/gaps-sets-007.md#g-d6764b42fac56013) · [状态效果 S-d1b4353fe17e1009](../../evidence/state_effects-sets-044.md#s-d1b4353fe17e1009)

### path-049381

```text
(config)# do-exec show ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100723C0 `；selector ` 0 `；EOL ` RVA 0x34A2FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9514e4dc259ba20d](../../evidence/conditions-sets-058.md#c-9514e4dc259ba20d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050063

```text
(config)# do-exec show ip rsvp p2mp counters <cr>
```

Handler ` RVA 0x101A72E0 `；selector ` 0 `；EOL ` RVA 0x34A3A468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-961c18143c16ea2a](../../evidence/conditions-sets-058.md#c-961c18143c16ea2a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040395

```text
(config)# do-exec show ip rsvp policy <cr>
```

Handler ` RVA 0x10113110 `；selector ` 0 `；EOL ` RVA 0x34A40A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c3376d0c22839b3](../../evidence/conditions-sets-060.md#c-9c3376d0c22839b3) · [状态效果 S-e5b15e8e568d8308](../../evidence/state_effects-sets-049.md#s-e5b15e8e568d8308)

### path-049549

```text
(config)# do-exec show ip rsvp policy cops <cr>
```

Handler ` RVA 0x10113110 `；selector ` 8 `；EOL ` RVA 0x34A40AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3c951b0abf3e01c](../../evidence/conditions-sets-088.md#c-e3c951b0abf3e01c) · [状态效果 S-e5b15e8e568d8308](../../evidence/state_effects-sets-049.md#s-e5b15e8e568d8308)

### path-049409

```text
(config)# do-exec show ip rsvp policy identity <cr>
```

Handler ` RVA 0x10112D90 `；selector ` 0 `；EOL ` RVA 0x34A40020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e5b15e8e568d8308](../../evidence/state_effects-sets-049.md#s-e5b15e8e568d8308)

### path-049819

```text
(config)# do-exec show ip rsvp policy local <cr>
```

Handler ` RVA 0x10113110 `；selector ` 1 `；EOL ` RVA 0x34A40490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af443612a5524707](../../evidence/conditions-sets-068.md#c-af443612a5524707) · [状态效果 S-1d896320f0848106](../../evidence/state_effects-sets-007.md#s-1d896320f0848106)

### path-062124

```text
(config)# do-exec show ip rsvp policy local <interface> <cr>
```

Handler ` RVA 0x10113110 `；selector ` 1 `；EOL ` RVA 0x34A40490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c88775c168d1c6ce](../../evidence/conditions-sets-077.md#c-c88775c168d1c6ce) · [缺口 G-e0769badd0fd20ea](../../evidence/gaps-sets-008.md#g-e0769badd0fd20ea) · [参数 P-0536a22aeae684e2](../../evidence/parameters-sets-001.md#p-0536a22aeae684e2) · [状态效果 S-1d896320f0848106](../../evidence/state_effects-sets-007.md#s-1d896320f0848106)

### path-062095

```text
(config)# do-exec show ip rsvp policy vrf * <cr>
```

Handler ` RVA 0x10113110 `；selector ` 0 `；EOL ` RVA 0x34A40A60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c5963f3bb8e3acb3](../../evidence/conditions-sets-076.md#c-c5963f3bb8e3acb3) · [缺口 G-7485f0584ada8c0d](../../evidence/gaps-sets-004.md#g-7485f0584ada8c0d) · [状态效果 S-1b7446926bab0e9d](../../evidence/state_effects-sets-006.md#s-1b7446926bab0e9d)

### path-062405

```text
(config)# do-exec show ip rsvp policy vrf * cops <cr>
```

Handler ` RVA 0x10113110 `；selector ` 8 `；EOL ` RVA 0x34A40AA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8ae6c97b15f36dae](../../evidence/conditions-sets-054.md#c-8ae6c97b15f36dae) · [缺口 G-7485f0584ada8c0d](../../evidence/gaps-sets-004.md#g-7485f0584ada8c0d) · [状态效果 S-1b7446926bab0e9d](../../evidence/state_effects-sets-006.md#s-1b7446926bab0e9d)

### path-062397

```text
(config)# do-exec show ip rsvp policy vrf * identity <cr>
```

Handler ` RVA 0x10112D90 `；selector ` 0 `；EOL ` RVA 0x34A40020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ee8679e8336b175](../../evidence/conditions-sets-037.md#c-5ee8679e8336b175) · [缺口 G-7485f0584ada8c0d](../../evidence/gaps-sets-004.md#g-7485f0584ada8c0d) · [状态效果 S-1b7446926bab0e9d](../../evidence/state_effects-sets-006.md#s-1b7446926bab0e9d)

### path-040757

```text
(config)# do-exec show ip rsvp precedence <cr>
```

Handler ` RVA 0x10054510 `；selector ` 0 `；EOL ` RVA 0x34A33C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-554816663dbba392](../../evidence/conditions-sets-033.md#c-554816663dbba392) · [状态效果 S-862d4bacd39b4c0c](../../evidence/state_effects-sets-028.md#s-862d4bacd39b4c0c)

### path-061637

```text
(config)# do-exec show ip rsvp precedence <interface> <cr>
```

Handler ` RVA 0x10054510 `；selector ` 0 `；EOL ` RVA 0x34A33C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c34016c08d473ea1](../../evidence/conditions-sets-075.md#c-c34016c08d473ea1) · [缺口 G-2b3145c2709f6e6e](../../evidence/gaps-sets-002.md#g-2b3145c2709f6e6e) · [参数 P-9d56f06581e454ae](../../evidence/parameters-sets-012.md#p-9d56f06581e454ae) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040485

```text
(config)# do-exec show ip rsvp sbm <cr>
```

Handler ` RVA 0x1006E490 `；selector ` 0 `；EOL ` RVA 0x34A303A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e394e7d7feb6c7ab](../../evidence/conditions-sets-088.md#c-e394e7d7feb6c7ab) · [状态效果 S-8c807ae98d888411](../../evidence/state_effects-sets-030.md#s-8c807ae98d888411)

### path-061594

```text
(config)# do-exec show ip rsvp sbm <interface> <cr>
```

Handler ` RVA 0x1006E490 `；selector ` 0 `；EOL ` RVA 0x34A303A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-46756a5e6f96569e](../../evidence/conditions-sets-028.md#c-46756a5e6f96569e) · [缺口 G-6567d1442ce4917d](../../evidence/gaps-sets-004.md#g-6567d1442ce4917d) · [参数 P-4ee747faa40a2997](../../evidence/parameters-sets-006.md#p-4ee747faa40a2997) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040605

```text
(config)# do-exec show ip rsvp sender <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A315A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-9aa39fbd3543fb49](../../evidence/state_effects-sets-033.md#s-9aa39fbd3543fb49)

### path-062123

```text
(config)# do-exec show ip rsvp sender vrf * <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A315A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4a2a7aa7d1e6038](../../evidence/conditions-sets-094.md#c-f4a2a7aa7d1e6038) · [缺口 G-8621a7720cb36b5a](../../evidence/gaps-sets-005.md#g-8621a7720cb36b5a) · [状态效果 S-df480d674869e704](../../evidence/state_effects-sets-047.md#s-df480d674869e704)

### path-050262

```text
(config)# do-exec show ip rsvp signalling blockade <cr>
```

Handler ` RVA 0x10067C20 `；selector ` 0 `；EOL ` RVA 0x34A3A0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1de7acaebb82474a](../../evidence/conditions-sets-012.md#c-1de7acaebb82474a) · [状态效果 S-a4d344170224a5c5](../../evidence/state_effects-sets-035.md#s-a4d344170224a5c5)

### path-062443

```text
(config)# do-exec show ip rsvp signalling blockade vrf * <cr>
```

Handler ` RVA 0x10067C20 `；selector ` 0 `；EOL ` RVA 0x34A3A0B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a1a58065baed4781](../../evidence/conditions-sets-062.md#c-a1a58065baed4781) · [缺口 G-400be44d6c2b73c6](../../evidence/gaps-sets-003.md#g-400be44d6c2b73c6) · [状态效果 S-37d8f634e38bc5d8](../../evidence/state_effects-sets-012.md#s-37d8f634e38bc5d8)

### path-050047

```text
(config)# do-exec show ip rsvp signalling fast-local-repair <cr>
```

Handler ` RVA 0x100713E0 `；selector ` 0 `；EOL ` RVA 0x34A38D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050040

```text
(config)# do-exec show ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x100712D0 `；selector ` 0 `；EOL ` RVA 0x34A38FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055909

```text
(config)# do-exec show ip rsvp signalling refresh interval <cr>
```

Handler ` RVA 0x10071130 `；selector ` 0 `；EOL ` RVA 0x34A39858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055924

```text
(config)# do-exec show ip rsvp signalling refresh misses <cr>
```

Handler ` RVA 0x100711A0 `；selector ` 0 `；EOL ` RVA 0x34A39B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055887

```text
(config)# do-exec show ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071210 `；selector ` 0 `；EOL ` RVA 0x34A395B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050070

```text
(config)# do-exec show ip rsvp signalling session-timers <cr>
```

Handler ` RVA 0x10072130 `；selector ` 0 `；EOL ` RVA 0x34A392A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049624

```text
(config)# do-exec show ip rsvp transport clients <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A31E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-f1c2a77fd72339e8](../../evidence/state_effects-sets-051.md#s-f1c2a77fd72339e8)

### path-038694

```text
(config)# do-exec show ip rtp header-compression <cr>
```

Handler ` RVA 0xD194110 `；selector ` 0 `；EOL ` RVA 0x33DAABA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a83c6ecb85845ec](../../evidence/conditions-sets-041.md#c-6a83c6ecb85845ec) · [状态效果 S-a3d3bc64932d287e](../../evidence/state_effects-sets-035.md#s-a3d3bc64932d287e)

### path-061499

```text
(config)# do-exec show ip rtp header-compression <interface> <cr>
```

Handler ` RVA 0xD194110 `；selector ` 0 `；EOL ` RVA 0x33DAABA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b38c5445d157291](../../evidence/conditions-sets-036.md#c-5b38c5445d157291) · [缺口 G-08d103b036b0853f](../../evidence/gaps-sets-001.md#g-08d103b036b0853f) · [参数 P-b5497cfcb9cb25ea](../../evidence/parameters-sets-014.md#p-b5497cfcb9cb25ea) · [状态效果 S-a3d3bc64932d287e](../../evidence/state_effects-sets-035.md#s-a3d3bc64932d287e)

### path-048776

```text
(config)# do-exec show ip sctp association list <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 2 `；EOL ` RVA 0x33D0DFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055025

```text
(config)# do-exec show ip sctp association parameters <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 3 `；EOL ` RVA 0x33D0DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d2fce9ec1de3fa16](../../evidence/parameters-sets-016.md#p-d2fce9ec1de3fa16) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054989

```text
(config)# do-exec show ip sctp association statistics <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 4 `；EOL ` RVA 0x33D0DA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-39686869c9f42ad0](../../evidence/parameters-sets-005.md#p-39686869c9f42ad0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039622

```text
(config)# do-exec show ip sctp errors <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 6 `；EOL ` RVA 0x33D0D6F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039733

```text
(config)# do-exec show ip sctp instances <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 1 `；EOL ` RVA 0x33D0E288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039553

```text
(config)# do-exec show ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 5 `；EOL ` RVA 0x33D0D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031712

```text
(config)# do-exec show ip sdr <cr>
```

Handler ` RVA 0xF87E5A0 `；selector ` 0 `；EOL ` RVA 0x3474E828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a322bbb3e692625](../../evidence/conditions-sets-004.md#c-0a322bbb3e692625) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041034

```text
(config)# do-exec show ip sla application <cr>
```

Handler ` RVA 0x102DD0E0 `；selector ` 0 `；EOL ` RVA 0x34A99F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040638

```text
(config)# do-exec show ip sla authentication <cr>
```

Handler ` RVA 0x101DA830 `；selector ` 0 `；EOL ` RVA 0x34A6E750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050024

```text
(config)# do-exec show ip sla auto discovery <cr>
```

Handler ` RVA 0x10241B90 `；selector ` 0 `；EOL ` RVA 0x34A7ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050008

```text
(config)# do-exec show ip sla auto group <cr>
```

Handler ` RVA 0x10240F70 `；selector ` 0 `；EOL ` RVA 0x34A7A360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5853727462a5bdce](../../evidence/state_effects-sets-019.md#s-5853727462a5bdce)

### path-050003

```text
(config)# do-exec show ip sla auto schedule <cr>
```

Handler ` RVA 0x10241510 `；selector ` 0 `；EOL ` RVA 0x34A7A6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059923

```text
(config)# do-exec show ip sla auto summary-statistics group type ip <string> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 2 `；EOL ` RVA 0x34A7B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-1d5a828fe10a3285](../../evidence/state_effects-sets-007.md#s-1d5a828fe10a3285)

### path-060225

```text
(config)# do-exec show ip sla auto summary-statistics group type ip <string> ip-address <address> port <number:0..64000> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 3 `；EOL ` RVA 0x34A7B2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name；` address ` destination ip address；` unsigned_number ` destination port。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-8528621cf3b47973](../../evidence/parameters-sets-010.md#p-8528621cf3b47973) · [状态效果 S-1d5a828fe10a3285](../../evidence/state_effects-sets-007.md#s-1d5a828fe10a3285)

### path-060105

```text
(config)# do-exec show ip sla auto summary-statistics group type ip <string> ip-address <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 1 `；EOL ` RVA 0x34A7B248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-1d5a828fe10a3285](../../evidence/state_effects-sets-007.md#s-1d5a828fe10a3285)

### path-050052

```text
(config)# do-exec show ip sla auto template <cr>
```

Handler ` RVA 0x102415E0 `；selector ` 0 `；EOL ` RVA 0x34A7AAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e9dc6b5013e2ecd5](../../evidence/state_effects-sets-049.md#s-e9dc6b5013e2ecd5)

### path-062566

```text
(config)# do-exec show ip sla auto template type ip <?keyword_option_mm_action@555589fcea00> <cr>
```

Handler ` RVA 0x102415E0 `；selector ` 0 `；EOL ` RVA 0x34A7AAC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-b84635966b1a6a2f](../../evidence/gaps-sets-006.md#g-b84635966b1a6a2f) · [状态效果 S-8ec7c67c56e9cd12](../../evidence/state_effects-sets-030.md#s-8ec7c67c56e9cd12)

### path-040898

```text
(config)# do-exec show ip sla collection-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 0 `；EOL ` RVA 0x34A97478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040693

```text
(config)# do-exec show ip sla configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 14 `；EOL ` RVA 0x34A95AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041046

```text
(config)# do-exec show ip sla distribution-statistics <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050068

```text
(config)# do-exec show ip sla distribution-statistics full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 1 `；EOL ` RVA 0x34A97A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050039

```text
(config)# do-exec show ip sla distribution-statistics raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 3 `；EOL ` RVA 0x34A977B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050104

```text
(config)# do-exec show ip sla distribution-statistics tabular <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041199

```text
(config)# do-exec show ip sla endpoint-list <cr>
```

Handler ` RVA 0x10241300 `；selector ` 0 `；EOL ` RVA 0x34A9A980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1592afbd4790893d](../../evidence/state_effects-sets-005.md#s-1592afbd4790893d)

### path-050077

```text
(config)# do-exec show ip sla enhanced-history distribution-statistics <cr>
```

Handler ` RVA 0x102DD570 `；selector ` 0 `；EOL ` RVA 0x34A98318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f90e24d709718fef](../../evidence/state_effects-sets-053.md#s-f90e24d709718fef)

### path-050029

```text
(config)# do-exec show ip sla ethernet-monitor configuration <cr>
```

Handler ` RVA 0x103C1120 `；selector ` 0 `；EOL ` RVA 0x34B09AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049967

```text
(config)# do-exec show ip sla ethernet-monitor responder <cr>
```

Handler ` RVA 0x103C1230 `；selector ` 0 `；EOL ` RVA 0x34B09800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040722

```text
(config)# do-exec show ip sla event-publisher <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 1 `；EOL ` RVA 0x34A890E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049860

```text
(config)# do-exec show ip sla event-publisher detail <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 2 `；EOL ` RVA 0x34A890C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049980

```text
(config)# do-exec show ip sla group schedule <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 0 `；EOL ` RVA 0x34A96958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055778

```text
(config)# do-exec show ip sla group schedule details <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 28 `；EOL ` RVA 0x34A96930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041141

```text
(config)# do-exec show ip sla history <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050135

```text
(config)# do-exec show ip sla history full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 5 `；EOL ` RVA 0x34A989A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050190

```text
(config)# do-exec show ip sla history interval-statistics <cr>
```

Handler ` RVA 0x102DDA40 `；selector ` 45 `；EOL ` RVA 0x34A98EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050100

```text
(config)# do-exec show ip sla history raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 7 `；EOL ` RVA 0x34A98700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050162

```text
(config)# do-exec show ip sla history tabular <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040835

```text
(config)# do-exec show ip sla operational-state <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 16 `；EOL ` RVA 0x34A96E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061023

```text
(config)# do-exec show ip sla periodic hostname summary <cr>
```

Handler ` RVA 0x102DDC20 `；selector ` 0 `；EOL ` RVA 0x34A962F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-769e0915910a7529](../../evidence/conditions-sets-046.md#c-769e0915910a7529) · [缺口 G-e795325d219eadad](../../evidence/gaps-sets-008.md#g-e795325d219eadad) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041137

```text
(config)# do-exec show ip sla reaction-configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 17 `；EOL ` RVA 0x34A9A568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041109

```text
(config)# do-exec show ip sla reaction-trigger <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 12 `；EOL ` RVA 0x34A9A278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040710

```text
(config)# do-exec show ip sla responder <cr>
```

Handler ` RVA 0x101FD080 `；selector ` 0 `；EOL ` RVA 0x34A719E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061028

```text
(config)# do-exec show ip sla schedule backup tree summary <cr>
```

Handler ` RVA 0x102DDB30 `；selector ` 0 `；EOL ` RVA 0x34A96598 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-13157d7862ffcce3](../../evidence/conditions-sets-008.md#c-13157d7862ffcce3) · [缺口 G-44211bc20d700a18](../../evidence/gaps-sets-003.md#g-44211bc20d700a18) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041112

```text
(config)# do-exec show ip sla statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 18 `；EOL ` RVA 0x34A99A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050174

```text
(config)# do-exec show ip sla statistics aggregated <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 25 `；EOL ` RVA 0x34A99550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055908

```text
(config)# do-exec show ip sla statistics aggregated details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 26 `；EOL ` RVA 0x34A99528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050159

```text
(config)# do-exec show ip sla statistics details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 22 `；EOL ` RVA 0x34A99A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040721

```text
(config)# do-exec show ip sla summary <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 46 `；EOL ` RVA 0x34A95DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062133

```text
(config)# do-exec show ip sla summary destination <?ipv4orv6_addr_action@555589fe9db8> <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 47 `；EOL ` RVA 0x34A95E20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-60a10f2f63731b25](../../evidence/gaps-sets-004.md#g-60a10f2f63731b25) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040868

```text
(config)# do-exec show ip sla totals-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 4 `；EOL ` RVA 0x34A97188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062650

```text
(config)# do-exec show ip sla twamp connection detail source-ip <?ipv4orv6_addr_action@555589fc81c8> source-port <number:1..65535> <cr>
```

Handler ` RVA 0x1021EB60 `；selector ` 0 `；EOL ` RVA 0x34A73EC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-3043fd9675dd4d51](../../evidence/gaps-sets-002.md#g-3043fd9675dd4d51) · [参数 P-64b2d6d3999edcf3](../../evidence/parameters-sets-008.md#p-64b2d6d3999edcf3) · [状态效果 S-e28162fab2c5e73b](../../evidence/state_effects-sets-048.md#s-e28162fab2c5e73b)

### path-055813

```text
(config)# do-exec show ip sla twamp connection requests <cr>
```

Handler ` RVA 0x1021EB60 `；selector ` 0 `；EOL ` RVA 0x34A73EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9b4b1aac84903742](../../evidence/state_effects-sets-033.md#s-9b4b1aac84903742)

### path-049958

```text
(config)# do-exec show ip sla twamp session <cr>
```

Handler ` RVA 0x10238810 `；selector ` 0 `；EOL ` RVA 0x34A76DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e43b56deba2ef108](../../evidence/state_effects-sets-048.md#s-e43b56deba2ef108)

### path-062628

```text
(config)# do-exec show ip sla twamp session source-ip <?ipv4orv6_addr_action@555589fcac38> source-port <number:1..65535> <cr>
```

Handler ` RVA 0x10238810 `；selector ` 0 `；EOL ` RVA 0x34A76DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Port Number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-279ad19bf90e128a](../../evidence/gaps-sets-002.md#g-279ad19bf90e128a) · [参数 P-ffdcdc98bf822654](../../evidence/parameters-sets-019.md#p-ffdcdc98bf822654) · [状态效果 S-437e0ba10760881e](../../evidence/state_effects-sets-015.md#s-437e0ba10760881e)

### path-049931

```text
(config)# do-exec show ip sla twamp standards <cr>
```

Handler ` RVA 0x10238750 `；selector ` 0 `；EOL ` RVA 0x34A770A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049981

```text
(config)# do-exec show ip sla twamp-light session <cr>
```

Handler ` RVA 0x1023AE80 `；selector ` 0 `；EOL ` RVA 0x34A79728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8bcf36ae1a5eb3af](../../evidence/state_effects-sets-030.md#s-8bcf36ae1a5eb3af)

### path-061064

```text
(config)# do-exec show ip sla udp zero checksum hash <cr>
```

Handler ` RVA 0x101D8B00 `；selector ` 0 `；EOL ` RVA 0x34A9AC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a59afe44892b5443](../../evidence/conditions-sets-064.md#c-a59afe44892b5443) · [缺口 G-ed49a896157802de](../../evidence/gaps-sets-008.md#g-ed49a896157802de) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031097

```text
(config)# do-exec show ip sockets <cr>
```

Handler ` RVA 0xCE441C0 `；selector ` 0 `；EOL ` RVA 0x33D31858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040875

```text
(config)# do-exec show ip source binding <cr>
```

Handler ` RVA 0x15FA8BF0 `；selector ` 0 `；EOL ` RVA 0x35E7DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b8dbd9ab5c91f915](../../evidence/conditions-sets-071.md#c-b8dbd9ab5c91f915) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061655

```text
(config)# do-exec show ip source binding <interface> <cr>
```

Handler ` RVA 0x15FA8BF0 `；selector ` 0 `；EOL ` RVA 0x35E7DBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74f6b6a03950b40d](../../evidence/conditions-sets-045.md#c-74f6b6a03950b40d) · [缺口 G-6f4d204e68ace526](../../evidence/gaps-sets-004.md#g-6f4d204e68ace526) · [参数 P-d5f7439c8e5cf16e](../../evidence/parameters-sets-016.md#p-d5f7439c8e5cf16e) · [状态效果 S-4b9e65720128465d](../../evidence/state_effects-sets-017.md#s-4b9e65720128465d)

### path-031087

```text
(config)# do-exec show ip spd <cr>
```

Handler ` RVA 0xCF78E90 `；selector ` 0 `；EOL ` RVA 0x33D31AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032044

```text
(config)# do-exec show ip ssh <cr>
```

Handler ` RVA 0x12360610 `；selector ` 0 `；EOL ` RVA 0x35828848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061572

```text
(config)# do-exec show ip static route <?ipaddrmask_action@5555897e3ec8> <cr>
```

Handler ` RVA 0xE2A5A00 `；selector ` 0 `；EOL ` RVA 0x3428FF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7d430d601f2f52a4](../../evidence/conditions-sets-049.md#c-7d430d601f2f52a4) · [缺口 G-950b75415e4673aa](../../evidence/gaps-sets-005.md#g-950b75415e4673aa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049252

```text
(config)# do-exec show ip static route bfd <cr>
```

Handler ` RVA 0xE2A6F50 `；selector ` 0 `；EOL ` RVA 0x3428F298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-47dd4a8f8df142f4](../../evidence/conditions-sets-028.md#c-47dd4a8f8df142f4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062080

```text
(config)# do-exec show ip static route bfd <interface> <cr>
```

Handler ` RVA 0xE2A6F50 `；selector ` 0 `；EOL ` RVA 0x3428F298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad99eaabf64e4791](../../evidence/conditions-sets-067.md#c-ad99eaabf64e4791) · [缺口 G-7a1928abc187d8ba](../../evidence/gaps-sets-005.md#g-7a1928abc187d8ba) · [参数 P-0be9fd4c5fb45e31](../../evidence/parameters-sets-001.md#p-0be9fd4c5fb45e31) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049046

```text
(config)# do-exec show ip static route rwatch-rib <cr>
```

Handler ` RVA 0xE2A7940 `；selector ` 0 `；EOL ` RVA 0x3428F850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d082036f9d027b1b](../../evidence/conditions-sets-080.md#c-d082036f9d027b1b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049135

```text
(config)# do-exec show ip static route sr-polices <cr>
```

Handler ` RVA 0xE2A79D0 `；selector ` 0 `；EOL ` RVA 0x3428FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65d1b2164bbdba22](../../evidence/conditions-sets-039.md#c-65d1b2164bbdba22) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048905

```text
(config)# do-exec show ip static route summary <cr>
```

Handler ` RVA 0xE2A7770 `；selector ` 0 `；EOL ` RVA 0x3428EE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032179

```text
(config)# do-exec show ip subscriber <cr>
```

Handler ` RVA 0x11A37870 `；selector ` 0 `；EOL ` RVA 0x355CDAE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1511e093238955bc](../../evidence/state_effects-sets-005.md#s-1511e093238955bc)

### path-061631

```text
(config)# do-exec show ip subscriber interface <interface> <cr>
```

Handler ` RVA 0x11A37870 `；selector ` 0 `；EOL ` RVA 0x355CDAE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d3fe8f4591088e7](../../evidence/conditions-sets-024.md#c-3d3fe8f4591088e7) · [缺口 G-3940a9d15f764f5a](../../evidence/gaps-sets-002.md#g-3940a9d15f764f5a) · [参数 P-333851ce9e569fe5](../../evidence/parameters-sets-004.md#p-333851ce9e569fe5) · [状态效果 S-916aae41f7296519](../../evidence/state_effects-sets-031.md#s-916aae41f7296519)

### path-062047

```text
(config)# do-exec show ip tcp adjust stats <interface> <cr>
```

Handler ` RVA 0xCDEFC60 `；selector ` 0 `；EOL ` RVA 0x33CF7668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-83d54f38f4d74b91](../../evidence/conditions-sets-051.md#c-83d54f38f4d74b91) · [缺口 G-15b09437b8a1a52b](../../evidence/gaps-sets-001.md#g-15b09437b8a1a52b) · [参数 P-9e78a61ab5cdd5f3](../../evidence/parameters-sets-012.md#p-9e78a61ab5cdd5f3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038751

```text
(config)# do-exec show ip tcp header-compression <cr>
```

Handler ` RVA 0xD194400 `；selector ` 0 `；EOL ` RVA 0x33DAB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f8c1239e9b64ddef](../../evidence/conditions-sets-096.md#c-f8c1239e9b64ddef) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061498

```text
(config)# do-exec show ip tcp header-compression <interface> <cr>
```

Handler ` RVA 0xD194400 `；selector ` 0 `；EOL ` RVA 0x33DAB590 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb6bcf8ae607a39d](../../evidence/conditions-sets-072.md#c-bb6bcf8ae607a39d) · [缺口 G-8eadef431675d07a](../../evidence/gaps-sets-005.md#g-8eadef431675d07a) · [参数 P-2789e57579649002](../../evidence/parameters-sets-003.md#p-2789e57579649002) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039098

```text
(config)# do-exec show ip telnet status <cr>
```

Handler ` RVA 0xCDEFBC0 `；selector ` 0 `；EOL ` RVA 0x33D02090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031163

```text
(config)# do-exec show ip traffic <cr>
```

Handler ` RVA 0xCECF560 `；selector ` 0 `；EOL ` RVA 0x33D32270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061479

```text
(config)# do-exec show ip traffic interface <interface> <cr>
```

Handler ` RVA 0xCECF4F0 `；selector ` 0 `；EOL ` RVA 0x33D32330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7fcd817f4d0e3d92](../../evidence/conditions-sets-050.md#c-7fcd817f4d0e3d92) · [缺口 G-3907641989e8551e](../../evidence/gaps-sets-002.md#g-3907641989e8551e) · [参数 P-71065a26c2012cdf](../../evidence/parameters-sets-009.md#p-71065a26c2012cdf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047383

```text
(config)# do-exec show ip traffic topology base <cr>
```

Handler ` RVA 0xCF0ED10 `；selector ` 0 `；EOL ` RVA 0x33D31E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-abffe367ba090e95](../../evidence/state_effects-sets-036.md#s-abffe367ba090e95)

### path-031963

```text
(config)# do-exec show ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 2 `；EOL ` RVA 0x34B5A698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032141

```text
(config)# do-exec show ip virtual-reassembly <cr>
```

Handler ` RVA 0xC78EA70 `；selector ` 0 `；EOL ` RVA 0x33AECED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ed87af899d4f2fe6](../../evidence/conditions-sets-092.md#c-ed87af899d4f2fe6) · [状态效果 S-bc22000ef7ff109b](../../evidence/state_effects-sets-040.md#s-bc22000ef7ff109b)

### path-030963

```text
(config)# do-exec show ipam counts <cr>
```

Handler ` RVA 0xCEA9220 `；selector ` 0 `；EOL ` RVA 0x33D1B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030953

```text
(config)# do-exec show ipam pool <cr>
```

Handler ` RVA 0xCEA02D0 `；selector ` 0 `；EOL ` RVA 0x33D1B340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030975

```text
(config)# do-exec show ipam queues <cr>
```

Handler ` RVA 0xCEA9160 `；selector ` 0 `；EOL ` RVA 0x33D1B5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031005

```text
(config)# do-exec show ipam status <cr>
```

Handler ` RVA 0xCE9D6D0 `；selector ` 0 `；EOL ` RVA 0x33D1B890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029455

```text
(config)# do-exec show ipc all <cr>
```

Handler ` RVA 0xD3B9630 `；selector ` 0 `；EOL ` RVA 0x33E2A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b3a32e79a46161a1](../../evidence/state_effects-sets-038.md#s-b3a32e79a46161a1)

### path-029892

```text
(config)# do-exec show ipc app <cr>
```

Handler ` RVA 0xD3BE590 `；selector ` 0 `；EOL ` RVA 0x33E2D5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029936

```text
(config)# do-exec show ipc buffer <cr>
```

Handler ` RVA 0xD39FCA0 `；selector ` 0 `；EOL ` RVA 0x33E2D858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045122

```text
(config)# do-exec show ipc cli <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xD38B220 `；selector ` 0 `；EOL ` RVA 0x33E2AAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IPC Seatid (in hex)；` string ` Remote command string。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d04ece3d584907a5](../../evidence/parameters-sets-016.md#p-d04ece3d584907a5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029786

```text
(config)# do-exec show ipc delayed <cr>
```

Handler ` RVA 0xD3A24C0 `；selector ` 0 `；EOL ` RVA 0x33E2D018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029304

```text
(config)# do-exec show ipc fc <cr>
```

Handler ` RVA 0xD3B96E0 `；selector ` 0 `；EOL ` RVA 0x33E29FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029912

```text
(config)# do-exec show ipc fragment <cr>
```

Handler ` RVA 0xD3BE5F0 `；selector ` 0 `；EOL ` RVA 0x33E2CD28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1c8023aff40da5dc](../../evidence/state_effects-sets-006.md#s-1c8023aff40da5dc)

### path-029691

```text
(config)# do-exec show ipc hog-info <cr>
```

Handler ` RVA 0xD3B8FB0 `；selector ` 0 `；EOL ` RVA 0x33E2C938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036469

```text
(config)# do-exec show ipc keepalive tx <cr>
```

Handler ` RVA 0xD3B8EC0 `；selector ` 0 `；EOL ` RVA 0x33E2E360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-47f5fd3aedcae528](../../evidence/state_effects-sets-016.md#s-47f5fd3aedcae528)

### path-035665

```text
(config)# do-exec show ipc mcast appclass <cr>
```

Handler ` RVA 0xD408040 `；selector ` 0 `；EOL ` RVA 0x33E42858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-80ec722fc3ee537d](../../evidence/state_effects-sets-027.md#s-80ec722fc3ee537d)

### path-035785

```text
(config)# do-exec show ipc mcast groups <cr>
```

Handler ` RVA 0xD407F80 `；selector ` 0 `；EOL ` RVA 0x33E42C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3068e933c8ebb702](../../evidence/state_effects-sets-011.md#s-3068e933c8ebb702)

### path-045182

```text
(config)# do-exec show ipc mcast groups <number:1..4294967295> <cr>
```

Handler ` RVA 0xD407F10 `；selector ` 0 `；EOL ` RVA 0x33E42F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6d276200dc0ed569](../../evidence/parameters-sets-009.md#p-6d276200dc0ed569) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035992

```text
(config)# do-exec show ipc mcast sessions <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 0 `；EOL ` RVA 0x33E43368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8af7eb8213c3d75d](../../evidence/state_effects-sets-030.md#s-8af7eb8213c3d75d)

### path-045422

```text
(config)# do-exec show ipc mcast sessions verbose <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 1 `；EOL ` RVA 0x33E43340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8af7eb8213c3d75d](../../evidence/state_effects-sets-030.md#s-8af7eb8213c3d75d)

### path-035609

```text
(config)# do-exec show ipc mcast status <cr>
```

Handler ` RVA 0xD408100 `；selector ` 0 `；EOL ` RVA 0x33E42480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4284d01d7f85c247](../../evidence/state_effects-sets-015.md#s-4284d01d7f85c247)

### path-029572

```text
(config)# do-exec show ipc nodes <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 0 `；EOL ` RVA 0x33E2A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-995a10783fbd7b11](../../evidence/state_effects-sets-033.md#s-995a10783fbd7b11)

### path-035818

```text
(config)# do-exec show ipc nodes capabilities <cr>
```

Handler ` RVA 0xD45A9C0 `；selector ` 0 `；EOL ` RVA 0x33E489F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-995a10783fbd7b11](../../evidence/state_effects-sets-033.md#s-995a10783fbd7b11)

### path-035751

```text
(config)# do-exec show ipc nodes issu <cr>
```

Handler ` RVA 0xD45ADB0 `；selector ` 0 `；EOL ` RVA 0x33E48750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-995a10783fbd7b11](../../evidence/state_effects-sets-033.md#s-995a10783fbd7b11)

### path-035819

```text
(config)# do-exec show ipc nodes verbose <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 1 `；EOL ` RVA 0x33E27958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-995a10783fbd7b11](../../evidence/state_effects-sets-033.md#s-995a10783fbd7b11)

### path-029759

```text
(config)# do-exec show ipc ports <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 0 `；EOL ` RVA 0x33E2B120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4f90153ccbb12a90](../../evidence/state_effects-sets-017.md#s-4f90153ccbb12a90)

### path-035880

```text
(config)# do-exec show ipc ports verbose <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 1 `；EOL ` RVA 0x33E2B3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4f90153ccbb12a90](../../evidence/state_effects-sets-017.md#s-4f90153ccbb12a90)

### path-029259

```text
(config)# do-exec show ipc queue <cr>
```

Handler ` RVA 0xD3B91C0 `；selector ` 0 `；EOL ` RVA 0x33E29D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035614

```text
(config)# do-exec show ipc rmi all <cr>
```

Handler ` RVA 0xD3FE890 `；selector ` 0 `；EOL ` RVA 0x33E3F8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3ac0f5844236c9e2](../../evidence/state_effects-sets-013.md#s-3ac0f5844236c9e2)

### path-052835

```text
(config)# do-exec show ipc rmi thresholds ru <string> <cr>
```

Handler ` RVA 0xD3FE9F0 `；selector ` 0 `；EOL ` RVA 0x33E401F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPC RU id(in hex)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-1f71f90238213b0b](../../evidence/parameters-sets-003.md#p-1f71f90238213b0b) · [状态效果 S-2ec9606b37fcd434](../../evidence/state_effects-sets-010.md#s-2ec9606b37fcd434)

### path-030238

```text
(config)# do-exec show ipc rpc <cr>
```

Handler ` RVA 0xD3B90F0 `；selector ` 0 `；EOL ` RVA 0x33E2E7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-bcbf75d58440982c](../../evidence/state_effects-sets-040.md#s-bcbf75d58440982c)

### path-030021

```text
(config)# do-exec show ipc sess-ack <cr>
```

Handler ` RVA 0xD3B92E0 `；selector ` 0 `；EOL ` RVA 0x33E2DDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035983

```text
(config)# do-exec show ipc session all <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 0 `；EOL ` RVA 0x33E2B898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-508a947e3c2f72c1](../../evidence/state_effects-sets-018.md#s-508a947e3c2f72c1)

### path-045416

```text
(config)# do-exec show ipc session all verbose <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 1 `；EOL ` RVA 0x33E2B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-508a947e3c2f72c1](../../evidence/state_effects-sets-018.md#s-508a947e3c2f72c1)

### path-036057

```text
(config)# do-exec show ipc session tx <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 0 `；EOL ` RVA 0x33E2BF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5a63330428614544](../../evidence/state_effects-sets-019.md#s-5a63330428614544)

### path-045460

```text
(config)# do-exec show ipc session tx verbose <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 1 `；EOL ` RVA 0x33E2BF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5a63330428614544](../../evidence/state_effects-sets-019.md#s-5a63330428614544)

### path-029863

```text
(config)# do-exec show ipc status <cr>
```

Handler ` RVA 0xD3B8DA0 `；selector ` 0 `；EOL ` RVA 0x33E2C640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-d9f5e41c27773fd1](../../evidence/state_effects-sets-046.md#s-d9f5e41c27773fd1)

### path-029983

```text
(config)# do-exec show ipc thread-stats <cr>
```

Handler ` RVA 0xD3985A0 `；selector ` 0 `；EOL ` RVA 0x33E2DB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036081

```text
(config)# do-exec show ipc trace <number:1..3> <cr>
```

Handler ` RVA 0xD3B9000 `；selector ` 0 `；EOL ` RVA 0x33E2D328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type of buffer(1. event 2. debug 3. error)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-8efb61522b8c3136](../../evidence/parameters-sets-011.md#p-8efb61522b8c3136) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030152

```text
(config)# do-exec show ipc util <cr>
```

Handler ` RVA 0xD3BC620 `；selector ` 0 `；EOL ` RVA 0x33E2EA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030052

```text
(config)# do-exec show ipc watermark <cr>
```

Handler ` RVA 0xD3B8F20 `；selector ` 0 `；EOL ` RVA 0x33E2E050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029483

```text
(config)# do-exec show ipc zones <cr>
```

Handler ` RVA 0xD3BC120 `；selector ` 0 `；EOL ` RVA 0x33E2AD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032093

```text
(config)# do-exec show ipv6 access-list <cr>
```

Handler ` RVA 0x1217F2C0 `；selector ` 0 `；EOL ` RVA 0x357B0418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0366a2229b2aaf5](../../evidence/conditions-sets-074.md#c-c0366a2229b2aaf5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049743

```text
(config)# do-exec show ipv6 access-list <string> dump-og-database <cr>
```

Handler ` RVA 0x1217F470 `；selector ` 0 `；EOL ` RVA 0x357B04A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User selected string identifying this access list。

[条件 C-f9be45a27f3252dd](../../evidence/conditions-sets-096.md#c-f9be45a27f3252dd) · [参数 P-4019a6f8b247af69](../../evidence/parameters-sets-005.md#p-4019a6f8b247af69) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061018

```text
(config)# do-exec show ipv6 address <?match_ipv6_addrinfo_action@55558ad32ea0> <cr>
```

Handler ` RVA 0x12300550 `；selector ` 0 `；EOL ` RVA 0x357DEED8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-623768671324b260](../../evidence/conditions-sets-038.md#c-623768671324b260) · [缺口 G-f79b1e5aa4785a98](../../evidence/gaps-sets-009.md#g-f79b1e5aa4785a98) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032163

```text
(config)# do-exec show ipv6 alias <cr>
```

Handler ` RVA 0x12303F00 `；selector ` 0 `；EOL ` RVA 0x357DF538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032623

```text
(config)# do-exec show ipv6 cef <cr>
```

Handler ` RVA 0xB662E40 `；selector ` 0 `；EOL ` RVA 0x337CDBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dce39c0405d8719d](../../evidence/conditions-sets-085.md#c-dce39c0405d8719d) · [状态效果 S-f58bed9fce22470d](../../evidence/state_effects-sets-052.md#s-f58bed9fce22470d)

### path-061084

```text
(config)# do-exec show ipv6 cef <interface> <cr>
```

Handler ` RVA 0xB662E40 `；selector ` 0 `；EOL ` RVA 0x337CDBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d12259d84eafde32](../../evidence/conditions-sets-081.md#c-d12259d84eafde32) · [缺口 G-1eb3993852c66ed8](../../evidence/gaps-sets-002.md#g-1eb3993852c66ed8) · [参数 P-a0c8755f7921148b](../../evidence/parameters-sets-012.md#p-a0c8755f7921148b) · [状态效果 S-f58bed9fce22470d](../../evidence/state_effects-sets-052.md#s-f58bed9fce22470d)

### path-041202

```text
(config)# do-exec show ipv6 cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337CE290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7a0a4a69ad47303](../../evidence/conditions-sets-065.md#c-a7a0a4a69ad47303) · [状态效果 S-0d09468c1bb0d9de](../../evidence/state_effects-sets-003.md#s-0d09468c1bb0d9de)

### path-055803

```text
(config)# do-exec show ipv6 cef neighbor discovery throttling <cr>
```

Handler ` RVA 0xB671710 `；selector ` 0 `；EOL ` RVA 0x337CD4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-208fd76d36a9470d](../../evidence/conditions-sets-013.md#c-208fd76d36a9470d) · [状态效果 S-f58bed9fce22470d](../../evidence/state_effects-sets-052.md#s-f58bed9fce22470d)

### path-040706

```text
(config)# do-exec show ipv6 cef protocol-discard <cr>
```

Handler ` RVA 0xB5C2EB0 `；selector ` 73 `；EOL ` RVA 0x337D89C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040775

```text
(config)# do-exec show ipv6 cef summary <cr>
```

Handler ` RVA 0xB670E30 `；selector ` 1 `；EOL ` RVA 0x337CD130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-208fd76d36a9470d](../../evidence/conditions-sets-013.md#c-208fd76d36a9470d) · [状态效果 S-f58bed9fce22470d](../../evidence/state_effects-sets-052.md#s-f58bed9fce22470d)

### path-050076

```text
(config)# do-exec show ipv6 cef switching statistics <cr>
```

Handler ` RVA 0xB66E5F0 `；selector ` 0 `；EOL ` RVA 0x337CDF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7a0a4a69ad47303](../../evidence/conditions-sets-065.md#c-a7a0a4a69ad47303) · [状态效果 S-f58bed9fce22470d](../../evidence/state_effects-sets-052.md#s-f58bed9fce22470d)

### path-050093

```text
(config)# do-exec show ipv6 cef traffic prefix-length <cr>
```

Handler ` RVA 0xB671680 `；selector ` 0 `；EOL ` RVA 0x337CE7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7a0a4a69ad47303](../../evidence/conditions-sets-065.md#c-a7a0a4a69ad47303) · [状态效果 S-ef57381d544df1c2](../../evidence/state_effects-sets-051.md#s-ef57381d544df1c2)

### path-040901

```text
(config)# do-exec show ipv6 cef tree <cr>
```

Handler ` RVA 0xB670D30 `；selector ` 0 `；EOL ` RVA 0x337CD7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-208fd76d36a9470d](../../evidence/conditions-sets-013.md#c-208fd76d36a9470d) · [状态效果 S-f58bed9fce22470d](../../evidence/state_effects-sets-052.md#s-f58bed9fce22470d)

### path-062160

```text
(config)# do-exec show ipv6 cef vrf <?option@555588d20f18> events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337CE290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f112c7cf76d2ca17](../../evidence/conditions-sets-093.md#c-f112c7cf76d2ca17) · [缺口 G-8ed4e6dae7519fca](../../evidence/gaps-sets-005.md#g-8ed4e6dae7519fca) · [状态效果 S-6233b48c162d3e8f](../../evidence/state_effects-sets-021.md#s-6233b48c162d3e8f)

### path-062564

```text
(config)# do-exec show ipv6 cef vrf <?option@555588d20f18> neighbor discovery throttling <cr>
```

Handler ` RVA 0xB671710 `；selector ` 0 `；EOL ` RVA 0x337CD4C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b5c922a6fa8ca224](../../evidence/conditions-sets-070.md#c-b5c922a6fa8ca224) · [缺口 G-8ed4e6dae7519fca](../../evidence/gaps-sets-005.md#g-8ed4e6dae7519fca) · [状态效果 S-da560ff1399f3836](../../evidence/state_effects-sets-046.md#s-da560ff1399f3836)

### path-062141

```text
(config)# do-exec show ipv6 cef vrf <?option@555588d20f18> summary <cr>
```

Handler ` RVA 0xB670E30 `；selector ` 1 `；EOL ` RVA 0x337CD130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b5c922a6fa8ca224](../../evidence/conditions-sets-070.md#c-b5c922a6fa8ca224) · [缺口 G-8ed4e6dae7519fca](../../evidence/gaps-sets-005.md#g-8ed4e6dae7519fca) · [状态效果 S-da560ff1399f3836](../../evidence/state_effects-sets-046.md#s-da560ff1399f3836)

### path-062435

```text
(config)# do-exec show ipv6 cef vrf <?option@555588d20f18> switching statistics <cr>
```

Handler ` RVA 0xB66E5F0 `；selector ` 0 `；EOL ` RVA 0x337CDF00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f112c7cf76d2ca17](../../evidence/conditions-sets-093.md#c-f112c7cf76d2ca17) · [缺口 G-8ed4e6dae7519fca](../../evidence/gaps-sets-005.md#g-8ed4e6dae7519fca) · [状态效果 S-da560ff1399f3836](../../evidence/state_effects-sets-046.md#s-da560ff1399f3836)

### path-062439

```text
(config)# do-exec show ipv6 cef vrf <?option@555588d20f18> traffic prefix-length <cr>
```

Handler ` RVA 0xB671680 `；selector ` 0 `；EOL ` RVA 0x337CE7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f112c7cf76d2ca17](../../evidence/conditions-sets-093.md#c-f112c7cf76d2ca17) · [缺口 G-8ed4e6dae7519fca](../../evidence/gaps-sets-005.md#g-8ed4e6dae7519fca) · [状态效果 S-d07f3e5718cf1a41](../../evidence/state_effects-sets-044.md#s-d07f3e5718cf1a41)

### path-062145

```text
(config)# do-exec show ipv6 cef vrf <?option@555588d20f18> tree <cr>
```

Handler ` RVA 0xB670D30 `；selector ` 0 `；EOL ` RVA 0x337CD7E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b5c922a6fa8ca224](../../evidence/conditions-sets-070.md#c-b5c922a6fa8ca224) · [缺口 G-8ed4e6dae7519fca](../../evidence/gaps-sets-005.md#g-8ed4e6dae7519fca) · [状态效果 S-da560ff1399f3836](../../evidence/state_effects-sets-046.md#s-da560ff1399f3836)

### path-040418

```text
(config)# do-exec show ipv6 destination-guard policy <cr>
```

Handler ` RVA 0x136B13F0 `；selector ` 0 `；EOL ` RVA 0x35C02EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032033

```text
(config)# do-exec show ipv6 dhcp <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 0 `；EOL ` RVA 0x357C0EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040597

```text
(config)# do-exec show ipv6 dhcp binding <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 0 `；EOL ` RVA 0x357C6450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040648

```text
(config)# do-exec show ipv6 dhcp conflict <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 3 `；EOL ` RVA 0x357C6D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040510

```text
(config)# do-exec show ipv6 dhcp database <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 2 `；EOL ` RVA 0x357C5C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040391

```text
(config)# do-exec show ipv6 dhcp interface <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 1 `；EOL ` RVA 0x357C0868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3e89b51bedb64f0f](../../evidence/conditions-sets-024.md#c-3e89b51bedb64f0f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061585

```text
(config)# do-exec show ipv6 dhcp interface <interface> <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 1 `；EOL ` RVA 0x357C0868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-05aa1d7b4f1fdc7e](../../evidence/conditions-sets-003.md#c-05aa1d7b4f1fdc7e) · [缺口 G-3ada891ce285a646](../../evidence/gaps-sets-003.md#g-3ada891ce285a646) · [参数 P-1cb93ec109cdb36a](../../evidence/parameters-sets-003.md#p-1cb93ec109cdb36a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058531

```text
(config)# do-exec show ipv6 dhcp mac-hash-table dump pool <string> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 8 `；EOL ` RVA 0x357C7158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pool name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c08b972a2d83bb8c](../../evidence/parameters-sets-015.md#p-c08b972a2d83bb8c) · [状态效果 S-895ff4c2b927a0e0](../../evidence/state_effects-sets-029.md#s-895ff4c2b927a0e0)

### path-059913

```text
(config)# do-exec show ipv6 dhcp mac-hash-table dump pool <string> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 7 `；EOL ` RVA 0x357C71A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pool name；` unsigned_number ` Lower bound of index range；` unsigned_number ` Upper bound of index range。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6b881825297e6ab3](../../evidence/parameters-sets-008.md#p-6b881825297e6ab3) · [状态效果 S-895ff4c2b927a0e0](../../evidence/state_effects-sets-029.md#s-895ff4c2b927a0e0)

### path-049776

```text
(config)# do-exec show ipv6 dhcp packet statistics <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 6 `；EOL ` RVA 0x357C6A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040595

```text
(config)# do-exec show ipv6 dhcp pool <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 1 `；EOL ` RVA 0x357C6748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049636

```text
(config)# do-exec show ipv6 dhcp relay binding <cr>
```

Handler ` RVA 0x121B3460 `；selector ` 1 `；EOL ` RVA 0x357C33B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049746

```text
(config)# do-exec show ipv6 dhcp route <address> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 5 `；EOL ` RVA 0x357C6040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-bed6f5b93ba7ce08](../../evidence/parameters-sets-014.md#p-bed6f5b93ba7ce08) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061613

```text
(config)# do-exec show ipv6 dhcp route <prefix:dynamic> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 5 `；EOL ` RVA 0x357C6040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix。

[条件 C-34111e537e1d913d](../../evidence/conditions-sets-020.md#c-34111e537e1d913d) · [缺口 G-d33d5530b555eb71](../../evidence/gaps-sets-007.md#g-d33d5530b555eb71) · [参数 P-ad5c34686bcdd5f9](../../evidence/parameters-sets-013.md#p-ad5c34686bcdd5f9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040324

```text
(config)# do-exec show ipv6 dhcp statistics <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 2 `；EOL ` RVA 0x357C0B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040335

```text
(config)# do-exec show ipv6 eigrp accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x35467758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-040316

```text
(config)# do-exec show ipv6 eigrp interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35466788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02072856c732d360](../../evidence/conditions-sets-001.md#c-02072856c732d360) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-061575

```text
(config)# do-exec show ipv6 eigrp interfaces <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35466788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-53fb0ea8d3aa9c49](../../evidence/conditions-sets-033.md#c-53fb0ea8d3aa9c49) · [缺口 G-5e739b92576e1d69](../../evidence/gaps-sets-004.md#g-5e739b92576e1d69) · [参数 P-2a0afa2702cab971](../../evidence/parameters-sets-004.md#p-2a0afa2702cab971) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-040362

```text
(config)# do-exec show ipv6 eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35466290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc2ca51f771d257b](../../evidence/conditions-sets-079.md#c-cc2ca51f771d257b) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-061578

```text
(config)# do-exec show ipv6 eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35466290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7970c120e5c11435](../../evidence/conditions-sets-047.md#c-7970c120e5c11435) · [缺口 G-3ad65496b0f12ccd](../../evidence/gaps-sets-003.md#g-3ad65496b0f12ccd) · [参数 P-a97c2d21c62dc44f](../../evidence/parameters-sets-013.md#p-a97c2d21c62dc44f) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-040421

```text
(config)# do-exec show ipv6 eigrp sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-a52c820b8b5b3ded](../../evidence/state_effects-sets-035.md#s-a52c820b8b5b3ded)

### path-040482

```text
(config)# do-exec show ipv6 eigrp sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-7d4987955eae0152](../../evidence/state_effects-sets-027.md#s-7d4987955eae0152)

### path-040221

```text
(config)# do-exec show ipv6 eigrp timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x35466A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-040606

```text
(config)# do-exec show ipv6 eigrp topology <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x354670B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-54355be19c010d3a](../../evidence/conditions-sets-033.md#c-54355be19c010d3a) · [状态效果 S-24fb65332771b139](../../evidence/state_effects-sets-008.md#s-24fb65332771b139)

### path-061590

```text
(config)# do-exec show ipv6 eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x354670B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Network to display information about。

[条件 C-0fe625d3737945a7](../../evidence/conditions-sets-006.md#c-0fe625d3737945a7) · [缺口 G-9ae72f2157cab30a](../../evidence/gaps-sets-006.md#g-9ae72f2157cab30a) · [参数 P-c610da5717347127](../../evidence/parameters-sets-015.md#p-c610da5717347127) · [状态效果 S-84ee8dab429ccf6a](../../evidence/state_effects-sets-028.md#s-84ee8dab429ccf6a)

### path-040265

```text
(config)# do-exec show ipv6 eigrp traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x35466D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2be69de38a93ad6b](../../evidence/state_effects-sets-010.md#s-2be69de38a93ad6b)

### path-032175

```text
(config)# do-exec show ipv6 enablement <cr>
```

Handler ` RVA 0x123003B0 `；selector ` 0 `；EOL ` RVA 0x357DF7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031646

```text
(config)# do-exec show ipv6 errors-internal <cr>
```

Handler ` RVA 0x12304EF0 `；selector ` 0 `；EOL ` RVA 0x357E3398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7eecc5b66fe76f30](../../evidence/conditions-sets-049.md#c-7eecc5b66fe76f30) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039495

```text
(config)# do-exec show ipv6 features global <cr>
```

Handler ` RVA 0x123058C0 `；selector ` 0 `；EOL ` RVA 0x357E5868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032151

```text
(config)# do-exec show ipv6 general-prefix <cr>
```

Handler ` RVA 0x12303340 `；selector ` 0 `；EOL ` RVA 0x357DF290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039876

```text
(config)# do-exec show ipv6 local pool <cr>
```

Handler ` RVA 0x1232CA00 `；selector ` 0 `；EOL ` RVA 0x358110E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17fc993d24ef1ef9](../../evidence/conditions-sets-009.md#c-17fc993d24ef1ef9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032180

```text
(config)# do-exec show ipv6 mfib <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67c00043da398299](../../evidence/conditions-sets-040.md#c-67c00043da398299) · [状态效果 S-2986c663a78e88f0](../../evidence/state_effects-sets-009.md#s-2986c663a78e88f0)

### path-061031

```text
(config)# do-exec show ipv6 mfib <prefix:dynamic> <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA3A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-ae89847ac9358c28](../../evidence/conditions-sets-067.md#c-ae89847ac9358c28) · [缺口 G-92ef8836a73b47e3](../../evidence/gaps-sets-005.md#g-92ef8836a73b47e3) · [参数 P-2bf571312c34aaa5](../../evidence/parameters-sets-004.md#p-2bf571312c34aaa5) · [状态效果 S-2986c663a78e88f0](../../evidence/state_effects-sets-009.md#s-2986c663a78e88f0)

### path-040199

```text
(config)# do-exec show ipv6 mfib cable <cr>
```

Handler ` RVA 0x1197DD40 `；selector ` 0 `；EOL ` RVA 0x355B8E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6a91de4b030cad37](../../evidence/state_effects-sets-023.md#s-6a91de4b030cad37)

### path-062090

```text
(config)# do-exec show ipv6 mfib instance <?option@55558ab0e1f0> rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f72efb0809edc362](../../evidence/conditions-sets-095.md#c-f72efb0809edc362) · [缺口 G-be710c2cdda43437](../../evidence/gaps-sets-007.md#g-be710c2cdda43437) · [状态效果 S-d6106676761a61c9](../../evidence/state_effects-sets-045.md#s-d6106676761a61c9)

### path-040286

```text
(config)# do-exec show ipv6 mfib interface <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B9DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17430d17b594a709](../../evidence/conditions-sets-009.md#c-17430d17b594a709) · [状态效果 S-8b95ac12033bdb60](../../evidence/state_effects-sets-030.md#s-8b95ac12033bdb60)

### path-061580

```text
(config)# do-exec show ipv6 mfib interface <interface> <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B9DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-246e3074a6ba125d](../../evidence/conditions-sets-014.md#c-246e3074a6ba125d) · [缺口 G-6f86a6cb5cad8b10](../../evidence/gaps-sets-004.md#g-6f86a6cb5cad8b10) · [参数 P-8e3689e2058cb931](../../evidence/parameters-sets-011.md#p-8e3689e2058cb931) · [状态效果 S-8b95ac12033bdb60](../../evidence/state_effects-sets-030.md#s-8b95ac12033bdb60)

### path-049027

```text
(config)# do-exec show ipv6 mfib internal fibidb <cr>
```

Handler ` RVA 0x1197DE80 `；selector ` 0 `；EOL ` RVA 0x355B92A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-286321fcba52f283](../../evidence/state_effects-sets-009.md#s-286321fcba52f283)

### path-049426

```text
(config)# do-exec show ipv6 mfib internal mem <cr>
```

Handler ` RVA 0x1197DF50 `；selector ` 0 `；EOL ` RVA 0x355B95E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c3f95f8226e10ac7](../../evidence/state_effects-sets-041.md#s-c3f95f8226e10ac7)

### path-040336

```text
(config)# do-exec show ipv6 mfib rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355BA698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a03369785d51815](../../evidence/conditions-sets-010.md#c-1a03369785d51815) · [状态效果 S-342b2400a79e0de1](../../evidence/state_effects-sets-012.md#s-342b2400a79e0de1)

### path-040049

```text
(config)# do-exec show ipv6 mfib status <cr>
```

Handler ` RVA 0x1197C470 `；selector ` 0 `；EOL ` RVA 0x355B99F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-286321fcba52f283](../../evidence/state_effects-sets-009.md#s-286321fcba52f283)

### path-040300

```text
(config)# do-exec show ipv6 mld acl-db <cr>
```

Handler ` RVA 0x11625660 `；selector ` 6 `；EOL ` RVA 0x3554A6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b6351f1ad8b8189](../../evidence/conditions-sets-042.md#c-6b6351f1ad8b8189) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-049212

```text
(config)# do-exec show ipv6 mld all-vrfs traffic <cr>
```

Handler ` RVA 0x11625660 `；selector ` 4 `；EOL ` RVA 0x3554B100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f69dd54070d33806](../../evidence/conditions-sets-095.md#c-f69dd54070d33806) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040410

```text
(config)# do-exec show ipv6 mld gir <cr>
```

Handler ` RVA 0x11625660 `；selector ` 7 `；EOL ` RVA 0x3554ADE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bea721c310d17847](../../evidence/conditions-sets-074.md#c-bea721c310d17847) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040434

```text
(config)# do-exec show ipv6 mld groups <cr>
```

Handler ` RVA 0x11625660 `；selector ` 2 `；EOL ` RVA 0x35549A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0fac10020f70ff78](../../evidence/conditions-sets-006.md#c-0fac10020f70ff78) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-061592

```text
(config)# do-exec show ipv6 mld groups <interface> <cr>
```

Handler ` RVA 0x11625660 `；selector ` 2 `；EOL ` RVA 0x35549A80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f3347e68de023069](../../evidence/conditions-sets-094.md#c-f3347e68de023069) · [缺口 G-5f9d1fc2c61a7a71](../../evidence/gaps-sets-004.md#g-5f9d1fc2c61a7a71) · [参数 P-59e4dd46c32aac7c](../../evidence/parameters-sets-007.md#p-59e4dd46c32aac7c) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040239

```text
(config)# do-exec show ipv6 mld interface <cr>
```

Handler ` RVA 0x11625660 `；selector ` 1 `；EOL ` RVA 0x35549758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-754dc9d4e4c68fee](../../evidence/conditions-sets-046.md#c-754dc9d4e4c68fee) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-061568

```text
(config)# do-exec show ipv6 mld interface <interface> <cr>
```

Handler ` RVA 0x11625660 `；selector ` 1 `；EOL ` RVA 0x35549758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-95ed76a97a0e75eb](../../evidence/conditions-sets-058.md#c-95ed76a97a0e75eb) · [缺口 G-6abf17a64776ca89](../../evidence/gaps-sets-004.md#g-6abf17a64776ca89) · [参数 P-8c7a70ffd3f9558f](../../evidence/parameters-sets-011.md#p-8c7a70ffd3f9558f) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040460

```text
(config)# do-exec show ipv6 mld internal <cr>
```

Handler ` RVA 0x11628960 `；selector ` 0 `；EOL ` RVA 0x3554AA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09f80f2f8e1f6319](../../evidence/conditions-sets-004.md#c-09f80f2f8e1f6319) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-061587

```text
(config)# do-exec show ipv6 mld internal <interface> <cr>
```

Handler ` RVA 0x11628960 `；selector ` 0 `；EOL ` RVA 0x3554AA88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-483c33701f30834f](../../evidence/conditions-sets-028.md#c-483c33701f30834f) · [缺口 G-0c173f1f9e8f09e3](../../evidence/gaps-sets-001.md#g-0c173f1f9e8f09e3) · [参数 P-760749805b4d6073](../../evidence/parameters-sets-009.md#p-760749805b4d6073) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040311

```text
(config)# do-exec show ipv6 mld ssm-map <cr>
```

Handler ` RVA 0x11625660 `；selector ` 5 `；EOL ` RVA 0x3554A478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b6351f1ad8b8189](../../evidence/conditions-sets-042.md#c-6b6351f1ad8b8189) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040218

```text
(config)# do-exec show ipv6 mld traffic <cr>
```

Handler ` RVA 0x11625660 `；selector ` 3 `；EOL ` RVA 0x3554A168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b6351f1ad8b8189](../../evidence/conditions-sets-042.md#c-6b6351f1ad8b8189) · [状态效果 S-9ee3c5c3acbfb7e7](../../evidence/state_effects-sets-034.md#s-9ee3c5c3acbfb7e7)

### path-040109

```text
(config)# do-exec show ipv6 mrib client <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 1 `；EOL ` RVA 0x3554F618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3ab54ff739a95459](../../evidence/state_effects-sets-013.md#s-3ab54ff739a95459)

### path-061584

```text
(config)# do-exec show ipv6 mrib route * <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x3554EB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9c3ddb73b8304fe9](../../evidence/conditions-sets-060.md#c-9c3ddb73b8304fe9) · [缺口 G-afe2817616d2ab41](../../evidence/gaps-sets-006.md#g-afe2817616d2ab41) · [状态效果 S-ceb820a9f2f66a2d](../../evidence/state_effects-sets-044.md#s-ceb820a9f2f66a2d)

### path-055451

```text
(config)# do-exec show ipv6 mrib route <address> <address> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3554EFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` source IP address；` address ` source IP address。

[条件 C-4ef006d3a3613d79](../../evidence/conditions-sets-031.md#c-4ef006d3a3613d79) · [参数 P-282323034f78b379](../../evidence/parameters-sets-003.md#p-282323034f78b379) · [状态效果 S-6de6d7b24a083d31](../../evidence/state_effects-sets-023.md#s-6de6d7b24a083d31)

### path-040289

```text
(config)# do-exec show ipv6 mrib route <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x3554EB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9fa33a2f5db67048](../../evidence/conditions-sets-062.md#c-9fa33a2f5db67048) · [状态效果 S-3ab54ff739a95459](../../evidence/state_effects-sets-013.md#s-3ab54ff739a95459)

### path-061571

```text
(config)# do-exec show ipv6 mrib route <prefix:dynamic> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3554EFC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` group IP address/prefix length。

[条件 C-c336fae728f5e719](../../evidence/conditions-sets-075.md#c-c336fae728f5e719) · [缺口 G-b0ed31b6c0c42fae](../../evidence/gaps-sets-006.md#g-b0ed31b6c0c42fae) · [参数 P-1ec5be69b6d07b5c](../../evidence/parameters-sets-003.md#p-1ec5be69b6d07b5c) · [状态效果 S-3ab54ff739a95459](../../evidence/state_effects-sets-013.md#s-3ab54ff739a95459)

### path-048964

```text
(config)# do-exec show ipv6 mrib route summary <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 3 `；EOL ` RVA 0x3554E800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3ab54ff739a95459](../../evidence/state_effects-sets-013.md#s-3ab54ff739a95459)

### path-032070

```text
(config)# do-exec show ipv6 mroute <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x3555E458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-16db4ad30c7c1a69](../../evidence/conditions-sets-009.md#c-16db4ad30c7c1a69) · [状态效果 S-cc36c93518681d03](../../evidence/state_effects-sets-043.md#s-cc36c93518681d03)

### path-040569

```text
(config)# do-exec show ipv6 mroute active <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 18 `；EOL ` RVA 0x3555EC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-991d7bd0b98b4b4a](../../evidence/conditions-sets-059.md#c-991d7bd0b98b4b4a) · [状态效果 S-4d0ac9b31835a093](../../evidence/state_effects-sets-017.md#s-4d0ac9b31835a093)

### path-040455

```text
(config)# do-exec show ipv6 mroute count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 19 `；EOL ` RVA 0x3555E878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-56fdf60944e8c413](../../evidence/conditions-sets-034.md#c-56fdf60944e8c413) · [状态效果 S-07ee0e550b689271](../../evidence/state_effects-sets-002.md#s-07ee0e550b689271)

### path-061612

```text
(config)# do-exec show ipv6 mroute vrf <?option@55558aab2338> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x3555E458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-82d2ddb8ef44a0be](../../evidence/conditions-sets-051.md#c-82d2ddb8ef44a0be) · [缺口 G-ef959bdc50651d14](../../evidence/gaps-sets-008.md#g-ef959bdc50651d14) · [状态效果 S-cc36c93518681d03](../../evidence/state_effects-sets-043.md#s-cc36c93518681d03)

### path-062120

```text
(config)# do-exec show ipv6 mroute vrf <?option@55558aab2338> active <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 18 `；EOL ` RVA 0x3555EC48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-281dcda382789a5b](../../evidence/conditions-sets-016.md#c-281dcda382789a5b) · [缺口 G-ef959bdc50651d14](../../evidence/gaps-sets-008.md#g-ef959bdc50651d14) · [状态效果 S-4d0ac9b31835a093](../../evidence/state_effects-sets-017.md#s-4d0ac9b31835a093)

### path-062100

```text
(config)# do-exec show ipv6 mroute vrf <?option@55558aab2338> count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 19 `；EOL ` RVA 0x3555E878 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-094c89a14abae8d4](../../evidence/conditions-sets-004.md#c-094c89a14abae8d4) · [缺口 G-ef959bdc50651d14](../../evidence/gaps-sets-008.md#g-ef959bdc50651d14) · [状态效果 S-07ee0e550b689271](../../evidence/state_effects-sets-002.md#s-07ee0e550b689271)

### path-031752

```text
(config)# do-exec show ipv6 mtu <cr>
```

Handler ` RVA 0x12306750 `；selector ` 0 `；EOL ` RVA 0x357E5568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-786c3a4775362ce9](../../evidence/state_effects-sets-026.md#s-786c3a4775362ce9)

### path-061521

```text
(config)# do-exec show ipv6 mtu vrf <?match_ipv6_zoneinfo_action@55558ad394c8> <cr>
```

Handler ` RVA 0x12306750 `；selector ` 0 `；EOL ` RVA 0x357E5568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-f9c48474b05caf43](../../evidence/gaps-sets-009.md#g-f9c48474b05caf43) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031994

```text
(config)# do-exec show ipv6 multicast <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 28 `；EOL ` RVA 0x3555F478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-11f086e615cc5d68](../../evidence/conditions-sets-007.md#c-11f086e615cc5d68) · [状态效果 S-f9db6f2ee232c781](../../evidence/state_effects-sets-053.md#s-f9db6f2ee232c781)

### path-055510

```text
(config)# do-exec show ipv6 multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 29 `；EOL ` RVA 0x3555F698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Overlay group address。

[条件 C-f0485cc6ffc631ac](../../evidence/conditions-sets-093.md#c-f0485cc6ffc631ac) · [参数 P-b95907093bfeb6e7](../../evidence/parameters-sets-014.md#p-b95907093bfeb6e7) · [状态效果 S-5332d65d3b208a88](../../evidence/state_effects-sets-018.md#s-5332d65d3b208a88)

### path-062546

```text
(config)# do-exec show ipv6 multicast overlay-mapping lisp <address> interface <interface> <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 29 `；EOL ` RVA 0x3555F698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Overlay group address。

[条件 C-36dac95141363f69](../../evidence/conditions-sets-021.md#c-36dac95141363f69) · [缺口 G-79a1e3159472a6a9](../../evidence/gaps-sets-005.md#g-79a1e3159472a6a9) · [参数 P-383adeb19298fbd9](../../evidence/parameters-sets-005.md#p-383adeb19298fbd9) · [状态效果 S-5332d65d3b208a88](../../evidence/state_effects-sets-018.md#s-5332d65d3b208a88)

### path-049458

```text
(config)# do-exec show ipv6 multicast rpf monitored <cr>
```

Handler ` RVA 0x11757B10 `；selector ` 0 `；EOL ` RVA 0x3555FAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0485cc6ffc631ac](../../evidence/conditions-sets-093.md#c-f0485cc6ffc631ac) · [状态效果 S-f9db6f2ee232c781](../../evidence/state_effects-sets-053.md#s-f9db6f2ee232c781)

### path-058286

```text
(config)# do-exec show ipv6 multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 61 `；EOL ` RVA 0x33A5E878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-4a4b3b45291b2ba0](../../evidence/parameters-sets-006.md#p-4a4b3b45291b2ba0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048933

```text
(config)# do-exec show ipv6 multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 71 `；EOL ` RVA 0x33A5EB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058302

```text
(config)# do-exec show ipv6 multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 69 `；EOL ` RVA 0x33A5EBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7a939613dde89531](../../evidence/parameters-sets-010.md#p-7a939613dde89531) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039981

```text
(config)# do-exec show ipv6 nd destination <cr>
```

Handler ` RVA 0x1231A4C0 `；selector ` 0 `；EOL ` RVA 0x35804F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ef6eb7938f60f73](../../evidence/conditions-sets-061.md#c-9ef6eb7938f60f73) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061544

```text
(config)# do-exec show ipv6 nd destination <interface> <cr>
```

Handler ` RVA 0x1231A4C0 `；selector ` 0 `；EOL ` RVA 0x35804F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-afc8657064439514](../../evidence/conditions-sets-068.md#c-afc8657064439514) · [缺口 G-4381617f18719c85](../../evidence/gaps-sets-003.md#g-4381617f18719c85) · [参数 P-7ae0df22657e867a](../../evidence/parameters-sets-010.md#p-7ae0df22657e867a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048951

```text
(config)# do-exec show ipv6 nd on-link prefix <cr>
```

Handler ` RVA 0x1231A0A0 `；selector ` 0 `；EOL ` RVA 0x35804B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ddae2c3f64fff6e0](../../evidence/conditions-sets-085.md#c-ddae2c3f64fff6e0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062071

```text
(config)# do-exec show ipv6 nd on-link prefix <interface> <cr>
```

Handler ` RVA 0x1231A0A0 `；selector ` 0 `；EOL ` RVA 0x35804B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2f3ca619e8b2042f](../../evidence/conditions-sets-018.md#c-2f3ca619e8b2042f) · [缺口 G-18e902eade06f31f](../../evidence/gaps-sets-001.md#g-18e902eade06f31f) · [参数 P-dfc0696ce9a77d8d](../../evidence/parameters-sets-017.md#p-dfc0696ce9a77d8d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055127

```text
(config)# do-exec show ipv6 nd ra dns server <cr>
```

Handler ` RVA 0x1231C740 `；selector ` 0 `；EOL ` RVA 0x357F91E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c16d6832e94d082f](../../evidence/conditions-sets-075.md#c-c16d6832e94d082f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062367

```text
(config)# do-exec show ipv6 nd ra dns server <interface> <cr>
```

Handler ` RVA 0x1231C740 `；selector ` 0 `；EOL ` RVA 0x357F91E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c139bfab7a376811](../../evidence/conditions-sets-075.md#c-c139bfab7a376811) · [缺口 G-78b0e01a2be3f8c3](../../evidence/gaps-sets-005.md#g-78b0e01a2be3f8c3) · [参数 P-e7a8dd76ed3149d2](../../evidence/parameters-sets-017.md#p-e7a8dd76ed3149d2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048949

```text
(config)# do-exec show ipv6 nd ra dns-search-list <cr>
```

Handler ` RVA 0x1231C960 `；selector ` 0 `；EOL ` RVA 0x357F95A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dccde85957374a97](../../evidence/conditions-sets-085.md#c-dccde85957374a97) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062070

```text
(config)# do-exec show ipv6 nd ra dns-search-list <interface> <cr>
```

Handler ` RVA 0x1231C960 `；selector ` 0 `；EOL ` RVA 0x357F95A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa6d28b4360464db](../../evidence/conditions-sets-066.md#c-aa6d28b4360464db) · [缺口 G-0dee2d38018c29e0](../../evidence/gaps-sets-001.md#g-0dee2d38018c29e0) · [参数 P-acb6d8efd5df2a1d](../../evidence/parameters-sets-013.md#p-acb6d8efd5df2a1d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049017

```text
(config)# do-exec show ipv6 nd ra nat64-prefix <cr>
```

Handler ` RVA 0x1231CBF0 `；selector ` 0 `；EOL ` RVA 0x357F9958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8386af237bbbebea](../../evidence/conditions-sets-051.md#c-8386af237bbbebea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062074

```text
(config)# do-exec show ipv6 nd ra nat64-prefix <interface> <cr>
```

Handler ` RVA 0x1231CBF0 `；selector ` 0 `；EOL ` RVA 0x357F9958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-63abbdac6b3b43fb](../../evidence/conditions-sets-039.md#c-63abbdac6b3b43fb) · [缺口 G-65461dcd9960958b](../../evidence/gaps-sets-004.md#g-65461dcd9960958b) · [参数 P-3dbae635c9f21eb6](../../evidence/parameters-sets-005.md#p-3dbae635c9f21eb6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062064

```text
(config)# do-exec show ipv6 nd ra sessions <interface> <cr>
```

Handler ` RVA 0x1231CD10 `；selector ` 0 `；EOL ` RVA 0x357F8DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d00c9cf3deed7134](../../evidence/conditions-sets-080.md#c-d00c9cf3deed7134) · [缺口 G-cb715bb75440d3f3](../../evidence/gaps-sets-007.md#g-cb715bb75440d3f3) · [参数 P-4565dc2cb57f5f83](../../evidence/parameters-sets-006.md#p-4565dc2cb57f5f83) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049067

```text
(config)# do-exec show ipv6 nd ra specific-route <cr>
```

Handler ` RVA 0x1231CC80 `；selector ` 0 `；EOL ` RVA 0x357F9CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-977c0f06878c1b99](../../evidence/conditions-sets-058.md#c-977c0f06878c1b99) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062075

```text
(config)# do-exec show ipv6 nd ra specific-route <interface> <cr>
```

Handler ` RVA 0x1231CC80 `；selector ` 0 `；EOL ` RVA 0x357F9CE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dce85acb9bec1906](../../evidence/conditions-sets-085.md#c-dce85acb9bec1906) · [缺口 G-cd9895ce2b1c9a9a](../../evidence/gaps-sets-007.md#g-cd9895ce2b1c9a9a) · [参数 P-f5816ff1baafe475](../../evidence/parameters-sets-018.md#p-f5816ff1baafe475) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039867

```text
(config)# do-exec show ipv6 nd suppress <cr>
```

Handler ` RVA 0x136B3070 `；selector ` 0 `；EOL ` RVA 0x35C058E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1ddb110f34a9f5e](../../evidence/conditions-sets-069.md#c-b1ddb110f34a9f5e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031933

```text
(config)# do-exec show ipv6 neighbors <cr>
```

Handler ` RVA 0x12312460 `；selector ` 0 `；EOL ` RVA 0x35802578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9db6527fae527123](../../evidence/conditions-sets-061.md#c-9db6527fae527123) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060998

```text
(config)# do-exec show ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0x12312460 `；selector ` 0 `；EOL ` RVA 0x35802578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c9f15c7cff03e071](../../evidence/conditions-sets-078.md#c-c9f15c7cff03e071) · [缺口 G-edb29b1b5b952ecb](../../evidence/gaps-sets-008.md#g-edb29b1b5b952ecb) · [参数 P-ac9abd9e188fc46f](../../evidence/parameters-sets-013.md#p-ac9abd9e188fc46f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062976

```text
(config)# do-exec show ipv6 neighbors binding bdid <number:dynamic> <cr>
```

Handler ` RVA 0x136862F0 `；selector ` 1048 `；EOL ` RVA 0x35BF49F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-e7cdaff7a8b14012](../../evidence/conditions-sets-089.md#c-e7cdaff7a8b14012) · [缺口 G-f6efde15ad6d544e](../../evidence/gaps-sets-009.md#g-f6efde15ad6d544e) · [参数 P-80cee61582ae6113](../../evidence/parameters-sets-010.md#p-80cee61582ae6113) · [状态效果 S-2614efb5c01fdadf](../../evidence/state_effects-sets-009.md#s-2614efb5c01fdadf)

### path-039877

```text
(config)# do-exec show ipv6 neighbors ha <cr>
```

Handler ` RVA 0x12312380 `；selector ` 0 `；EOL ` RVA 0x35802280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c322c17061de54a](../../evidence/conditions-sets-030.md#c-4c322c17061de54a) · [状态效果 S-8dfb67629c7cab2f](../../evidence/state_effects-sets-030.md#s-8dfb67629c7cab2f)

### path-062066

```text
(config)# do-exec show ipv6 neighbors vrf <?match_ipv6_zoneinfo_action@55558ad56180> ha <cr>
```

Handler ` RVA 0x12312380 `；selector ` 0 `；EOL ` RVA 0x35802280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c322c17061de54a](../../evidence/conditions-sets-030.md#c-4c322c17061de54a) · [缺口 G-d1ec3282ad724509](../../evidence/gaps-sets-007.md#g-d1ec3282ad724509) · [状态效果 S-a5b84a16d919e159](../../evidence/state_effects-sets-035.md#s-a5b84a16d919e159)

### path-032315

```text
(config)# do-exec show ipv6 nhrp <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 0 `；EOL ` RVA 0x3556BAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9729e00f178a2c9](../../evidence/conditions-sets-090.md#c-e9729e00f178a2c9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061045

```text
(config)# do-exec show ipv6 nhrp <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 0 `；EOL ` RVA 0x3556BAA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0a019f88593ada83](../../evidence/conditions-sets-004.md#c-0a019f88593ada83) · [缺口 G-ae135edb5213a6a2](../../evidence/gaps-sets-006.md#g-ae135edb5213a6a2) · [参数 P-2709226bb4c8e330](../../evidence/parameters-sets-003.md#p-2709226bb4c8e330) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061649

```text
(config)# do-exec show ipv6 nhrp <interface> shortcut <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 15 `；EOL ` RVA 0x3556BE38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0a019f88593ada83](../../evidence/conditions-sets-004.md#c-0a019f88593ada83) · [缺口 G-ae135edb5213a6a2](../../evidence/gaps-sets-006.md#g-ae135edb5213a6a2) · [参数 P-2709226bb4c8e330](../../evidence/parameters-sets-003.md#p-2709226bb4c8e330) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040407

```text
(config)# do-exec show ipv6 nhrp attribute <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 16 `；EOL ` RVA 0x3556AF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040480

```text
(config)# do-exec show ipv6 nhrp instances <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 20 `；EOL ` RVA 0x3556B2A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d0c711efb033d4dd](../../evidence/conditions-sets-080.md#c-d0c711efb033d4dd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040457

```text
(config)# do-exec show ipv6 nhrp map <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 17 `；EOL ` RVA 0x3556ACD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5903a3cd8427ee05](../../evidence/conditions-sets-035.md#c-5903a3cd8427ee05) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061593

```text
(config)# do-exec show ipv6 nhrp map <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 17 `；EOL ` RVA 0x3556ACD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ae69f15bf92a7d9f](../../evidence/conditions-sets-067.md#c-ae69f15bf92a7d9f) · [缺口 G-b2ad772a8651e01c](../../evidence/gaps-sets-006.md#g-b2ad772a8651e01c) · [参数 P-36d6f04409b44e1e](../../evidence/parameters-sets-005.md#p-36d6f04409b44e1e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040517

```text
(config)# do-exec show ipv6 nhrp multicast <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 4 `；EOL ` RVA 0x3556A8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6f4b74a4fd5e773](../../evidence/conditions-sets-064.md#c-a6f4b74a4fd5e773) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061595

```text
(config)# do-exec show ipv6 nhrp multicast <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 4 `；EOL ` RVA 0x3556A8B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-152704d9d904cc8a](../../evidence/conditions-sets-008.md#c-152704d9d904cc8a) · [缺口 G-a11a8e4292a334bf](../../evidence/gaps-sets-006.md#g-a11a8e4292a334bf) · [参数 P-7aca9d4e591a67db](../../evidence/parameters-sets-010.md#p-7aca9d4e591a67db) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040461

```text
(config)# do-exec show ipv6 nhrp nhs <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 3 `；EOL ` RVA 0x355696B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7be504c3e53e6060](../../evidence/conditions-sets-048.md#c-7be504c3e53e6060) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061599

```text
(config)# do-exec show ipv6 nhrp nhs <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 3 `；EOL ` RVA 0x355696B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ac09b90bcb4c2c2](../../evidence/conditions-sets-036.md#c-5ac09b90bcb4c2c2) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062111

```text
(config)# do-exec show ipv6 nhrp nhs <interface> redundancy <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 10 `；EOL ` RVA 0x3556A218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ac09b90bcb4c2c2](../../evidence/conditions-sets-036.md#c-5ac09b90bcb4c2c2) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062547

```text
(config)# do-exec show ipv6 nhrp nhs <interface> redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 14 `；EOL ` RVA 0x35569CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-5ac09b90bcb4c2c2](../../evidence/conditions-sets-036.md#c-5ac09b90bcb4c2c2) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-60da779d75ad7109](../../evidence/parameters-sets-008.md#p-60da779d75ad7109) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062409

```text
(config)# do-exec show ipv6 nhrp nhs <interface> redundancy preempted <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 12 `；EOL ` RVA 0x35569F48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ac09b90bcb4c2c2](../../evidence/conditions-sets-036.md#c-5ac09b90bcb4c2c2) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062400

```text
(config)# do-exec show ipv6 nhrp nhs <interface> redundancy running <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 11 `；EOL ` RVA 0x355699B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ac09b90bcb4c2c2](../../evidence/conditions-sets-036.md#c-5ac09b90bcb4c2c2) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062410

```text
(config)# do-exec show ipv6 nhrp nhs <interface> redundancy waiting <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 13 `；EOL ` RVA 0x3556A1F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5ac09b90bcb4c2c2](../../evidence/conditions-sets-036.md#c-5ac09b90bcb4c2c2) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049734

```text
(config)# do-exec show ipv6 nhrp nhs redundancy <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 10 `；EOL ` RVA 0x3556A218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7be504c3e53e6060](../../evidence/conditions-sets-048.md#c-7be504c3e53e6060) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058467

```text
(config)# do-exec show ipv6 nhrp nhs redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 14 `；EOL ` RVA 0x35569CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-7be504c3e53e6060](../../evidence/conditions-sets-048.md#c-7be504c3e53e6060) · [参数 P-f03a6f61f88c6974](../../evidence/parameters-sets-018.md#p-f03a6f61f88c6974) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055588

```text
(config)# do-exec show ipv6 nhrp nhs redundancy preempted <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 12 `；EOL ` RVA 0x35569F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7be504c3e53e6060](../../evidence/conditions-sets-048.md#c-7be504c3e53e6060) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055537

```text
(config)# do-exec show ipv6 nhrp nhs redundancy running <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 11 `；EOL ` RVA 0x355699B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7be504c3e53e6060](../../evidence/conditions-sets-048.md#c-7be504c3e53e6060) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055610

```text
(config)# do-exec show ipv6 nhrp nhs redundancy waiting <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 13 `；EOL ` RVA 0x3556A1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7be504c3e53e6060](../../evidence/conditions-sets-048.md#c-7be504c3e53e6060) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040256

```text
(config)# do-exec show ipv6 nhrp purge <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 2 `；EOL ` RVA 0x355692E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062106

```text
(config)# do-exec show ipv6 nhrp rd <?vrf_rd_action@55558aac0368> redirect <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 6 `；EOL ` RVA 0x3556B620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-1da9e4acea00df4e](../../evidence/gaps-sets-002.md#g-1da9e4acea00df4e) · [状态效果 S-68e8e8780fa8da66](../../evidence/state_effects-sets-022.md#s-68e8e8780fa8da66)

### path-040536

```text
(config)# do-exec show ipv6 nhrp redirect <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 6 `；EOL ` RVA 0x3556B620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040928

```text
(config)# do-exec show ipv6 nhrp shortcut <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 15 `；EOL ` RVA 0x3556BE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9729e00f178a2c9](../../evidence/conditions-sets-090.md#c-e9729e00f178a2c9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040465

```text
(config)# do-exec show ipv6 nhrp stats <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 18 `；EOL ` RVA 0x35568EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a04170884a53453](../../evidence/conditions-sets-041.md#c-6a04170884a53453) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061602

```text
(config)# do-exec show ipv6 nhrp stats <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 18 `；EOL ` RVA 0x35568EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ef9ec1aac7fcdb9c](../../evidence/conditions-sets-093.md#c-ef9ec1aac7fcdb9c) · [缺口 G-fd22e53b7a28fc48](../../evidence/gaps-sets-009.md#g-fd22e53b7a28fc48) · [参数 P-b60092aad0a805e6](../../evidence/parameters-sets-014.md#p-b60092aad0a805e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040314

```text
(config)# do-exec show ipv6 nhrp traffic <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 1 `；EOL ` RVA 0x355689D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062091

```text
(config)# do-exec show ipv6 nhrp traffic interface <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 1 `；EOL ` RVA 0x355689D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7bb5ab979e93c6e7](../../evidence/conditions-sets-048.md#c-7bb5ab979e93c6e7) · [缺口 G-fa7d301a7479830e](../../evidence/gaps-sets-009.md#g-fa7d301a7479830e) · [参数 P-f39a52af321e1fe8](../../evidence/parameters-sets-018.md#p-f39a52af321e1fe8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049263

```text
(config)# do-exec show ipv6 pim all-vrfs traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 17 `；EOL ` RVA 0x3555DF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a6eae929d27f6d9](../../evidence/conditions-sets-023.md#c-3a6eae929d27f6d9) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040695

```text
(config)# do-exec show ipv6 pim anycast-rp <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 20 `；EOL ` RVA 0x3555D920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74f38e406742bb65](../../evidence/conditions-sets-045.md#c-74f38e406742bb65) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062430

```text
(config)# do-exec show ipv6 pim bfd neighbor <interface> inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9D680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3a3abb9487d6e4b2](../../evidence/conditions-sets-023.md#c-3a3abb9487d6e4b2) · [缺口 G-c3d5f5b8c8e0caa5](../../evidence/gaps-sets-007.md#g-c3d5f5b8c8e0caa5) · [参数 P-9f1575569e0001bf](../../evidence/parameters-sets-012.md#p-9f1575569e0001bf) · [状态效果 S-2ce9f8119b5c939d](../../evidence/state_effects-sets-010.md#s-2ce9f8119b5c939d)

### path-055848

```text
(config)# do-exec show ipv6 pim bfd neighbor inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9D680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0bcc001b44461cb6](../../evidence/conditions-sets-005.md#c-0bcc001b44461cb6) · [状态效果 S-2ce9f8119b5c939d](../../evidence/state_effects-sets-010.md#s-2ce9f8119b5c939d)

### path-049949

```text
(config)# do-exec show ipv6 pim bsr candidate-rp <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 13 `；EOL ` RVA 0x35551E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-65fdd66196a37ff9](../../evidence/state_effects-sets-022.md#s-65fdd66196a37ff9)

### path-049998

```text
(config)# do-exec show ipv6 pim bsr election <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 12 `；EOL ` RVA 0x35552360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-65fdd66196a37ff9](../../evidence/state_effects-sets-022.md#s-65fdd66196a37ff9)

### path-049972

```text
(config)# do-exec show ipv6 pim bsr rp-cache <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 14 `；EOL ` RVA 0x355520B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-65fdd66196a37ff9](../../evidence/state_effects-sets-022.md#s-65fdd66196a37ff9)

### path-040550

```text
(config)# do-exec show ipv6 pim df <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 5 `；EOL ` RVA 0x3555AA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65d06a2bc4e5f9f9](../../evidence/conditions-sets-039.md#c-65d06a2bc4e5f9f9) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061611

```text
(config)# do-exec show ipv6 pim df <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 5 `；EOL ` RVA 0x3555AA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d4f09c62b9871fc1](../../evidence/conditions-sets-082.md#c-d4f09c62b9871fc1) · [缺口 G-08257c1e2ce81d6b](../../evidence/gaps-sets-001.md#g-08257c1e2ce81d6b) · [参数 P-b0e5d0b436638c5a](../../evidence/parameters-sets-013.md#p-b0e5d0b436638c5a) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049854

```text
(config)# do-exec show ipv6 pim drlb gdr-candidates <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 22 `；EOL ` RVA 0x3555D3A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65cbd95f3ec04a1c](../../evidence/conditions-sets-039.md#c-65cbd95f3ec04a1c) · [状态效果 S-5c164bf316daf232](../../evidence/state_effects-sets-020.md#s-5c164bf316daf232)

### path-062128

```text
(config)# do-exec show ipv6 pim drlb gdr-candidates <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 22 `；EOL ` RVA 0x3555D3A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6bd6100f2545dc9](../../evidence/conditions-sets-071.md#c-b6bd6100f2545dc9) · [缺口 G-0e5d9a2cc1bb8dee](../../evidence/gaps-sets-001.md#g-0e5d9a2cc1bb8dee) · [参数 P-09e1a72196ef41d4](../../evidence/parameters-sets-001.md#p-09e1a72196ef41d4) · [状态效果 S-5c164bf316daf232](../../evidence/state_effects-sets-020.md#s-5c164bf316daf232)

### path-040687

```text
(config)# do-exec show ipv6 pim gir <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 26 `；EOL ` RVA 0x3555DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57b3d2c861dce348](../../evidence/conditions-sets-034.md#c-57b3d2c861dce348) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040462

```text
(config)# do-exec show ipv6 pim group-map <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 3 `；EOL ` RVA 0x3555A068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44c881d46e627984](../../evidence/conditions-sets-027.md#c-44c881d46e627984) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061601

```text
(config)# do-exec show ipv6 pim group-map <prefix:dynamic> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 3 `；EOL ` RVA 0x3555A068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` group prefix/mask。

[条件 C-260b883901f73843](../../evidence/conditions-sets-015.md#c-260b883901f73843) · [缺口 G-535e8c549d987339](../../evidence/gaps-sets-003.md#g-535e8c549d987339) · [参数 P-03b2d0d72e8e8207](../../evidence/parameters-sets-001.md#p-03b2d0d72e8e8207) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040433

```text
(config)# do-exec show ipv6 pim interface <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 0 `；EOL ` RVA 0x35558B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de74383bc7cbdfd5](../../evidence/conditions-sets-086.md#c-de74383bc7cbdfd5) · [状态效果 S-af3c17fced6804e0](../../evidence/state_effects-sets-037.md#s-af3c17fced6804e0)

### path-061588

```text
(config)# do-exec show ipv6 pim interface <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 0 `；EOL ` RVA 0x35558B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f95e59307d6f387f](../../evidence/conditions-sets-096.md#c-f95e59307d6f387f) · [缺口 G-67e9709bd8c74ca4](../../evidence/gaps-sets-004.md#g-67e9709bd8c74ca4) · [参数 P-08515242a93c3f65](../../evidence/parameters-sets-001.md#p-08515242a93c3f65) · [状态效果 S-af3c17fced6804e0](../../evidence/state_effects-sets-037.md#s-af3c17fced6804e0)

### path-062109

```text
(config)# do-exec show ipv6 pim interface <interface> bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9DA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66d6190f1750e98d](../../evidence/conditions-sets-040.md#c-66d6190f1750e98d) · [缺口 G-67e9709bd8c74ca4](../../evidence/gaps-sets-004.md#g-67e9709bd8c74ca4) · [参数 P-08515242a93c3f65](../../evidence/parameters-sets-001.md#p-08515242a93c3f65) · [状态效果 S-dd38ce82b27c2635](../../evidence/state_effects-sets-047.md#s-dd38ce82b27c2635)

### path-049726

```text
(config)# do-exec show ipv6 pim interface bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9DA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e0e0c85a4263042](../../evidence/conditions-sets-061.md#c-9e0e0c85a4263042) · [状态效果 S-dd38ce82b27c2635](../../evidence/state_effects-sets-047.md#s-dd38ce82b27c2635)

### path-040672

```text
(config)# do-exec show ipv6 pim internal <cr>
```

Handler ` RVA 0x1175D2F0 `；selector ` 0 `；EOL ` RVA 0x3555CF28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-775aab38fcb479fb](../../evidence/conditions-sets-046.md#c-775aab38fcb479fb) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061625

```text
(config)# do-exec show ipv6 pim internal <interface> <cr>
```

Handler ` RVA 0x1175D2F0 `；selector ` 0 `；EOL ` RVA 0x3555CF28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-774f397e7793c8e0](../../evidence/conditions-sets-046.md#c-774f397e7793c8e0) · [缺口 G-3dda9baeb37b261f](../../evidence/gaps-sets-003.md#g-3dda9baeb37b261f) · [参数 P-073220dee3ba98b7](../../evidence/parameters-sets-001.md#p-073220dee3ba98b7) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049759

```text
(config)# do-exec show ipv6 pim join-prune statistic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 15 `；EOL ` RVA 0x3555C028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-830033db2becc416](../../evidence/conditions-sets-051.md#c-830033db2becc416) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062112

```text
(config)# do-exec show ipv6 pim join-prune statistic <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 15 `；EOL ` RVA 0x3555C028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2ce002629d764eb3](../../evidence/conditions-sets-018.md#c-2ce002629d764eb3) · [缺口 G-4e468cab5acd1bc7](../../evidence/gaps-sets-003.md#g-4e468cab5acd1bc7) · [参数 P-2a28748aeaef974d](../../evidence/parameters-sets-004.md#p-2a28748aeaef974d) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040547

```text
(config)# do-exec show ipv6 pim limit <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 7 `；EOL ` RVA 0x3555B988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4224c1b4989d945](../../evidence/conditions-sets-063.md#c-a4224c1b4989d945) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061609

```text
(config)# do-exec show ipv6 pim limit <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 7 `；EOL ` RVA 0x3555B988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-53430a5f3ada6f4e](../../evidence/conditions-sets-033.md#c-53430a5f3ada6f4e) · [缺口 G-0b16c7a32442baa7](../../evidence/gaps-sets-001.md#g-0b16c7a32442baa7) · [参数 P-5be80ea061bfce4c](../../evidence/parameters-sets-007.md#p-5be80ea061bfce4c) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049763

```text
(config)# do-exec show ipv6 pim limit reservation <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 8 `；EOL ` RVA 0x3555B618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d98853c9c5bd1599](../../evidence/conditions-sets-084.md#c-d98853c9c5bd1599) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062114

```text
(config)# do-exec show ipv6 pim limit reservation <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 8 `；EOL ` RVA 0x3555B618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-743cb17b18fe53d4](../../evidence/conditions-sets-045.md#c-743cb17b18fe53d4) · [缺口 G-4946b21c0f6e7b28](../../evidence/gaps-sets-003.md#g-4946b21c0f6e7b28) · [参数 P-5bb5850ec768b0a2](../../evidence/parameters-sets-007.md#p-5bb5850ec768b0a2) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055644

```text
(config)# do-exec show ipv6 pim limit reservation required <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 9 `；EOL ` RVA 0x3555B278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-836aabc056d13cb4](../../evidence/conditions-sets-051.md#c-836aabc056d13cb4) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062413

```text
(config)# do-exec show ipv6 pim limit reservation required <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 9 `；EOL ` RVA 0x3555B278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-345141368a9e3f6b](../../evidence/conditions-sets-020.md#c-345141368a9e3f6b) · [缺口 G-153d6d4467a394e4](../../evidence/gaps-sets-001.md#g-153d6d4467a394e4) · [参数 P-51c476775a0d6c96](../../evidence/parameters-sets-007.md#p-51c476775a0d6c96) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040476

```text
(config)# do-exec show ipv6 pim lisp-rloc-state <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 27 `；EOL ` RVA 0x3555BC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0aac621c353bccfc](../../evidence/conditions-sets-004.md#c-0aac621c353bccfc) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040969

```text
(config)# do-exec show ipv6 pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478A808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-050119

```text
(config)# do-exec show ipv6 pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x347886B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055858

```text
(config)# do-exec show ipv6 pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x34788378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7e749d9f8ebd2b6d](../../evidence/conditions-sets-049.md#c-7e749d9f8ebd2b6d) · [状态效果 S-a74cba544ab0d424](../../evidence/state_effects-sets-035.md#s-a74cba544ab0d424)

### path-058586

```text
(config)# do-exec show ipv6 pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x34787F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [参数 P-957dcedf315a82c2](../../evidence/parameters-sets-011.md#p-957dcedf315a82c2) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055872

```text
(config)# do-exec show ipv6 pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x34788F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c3bf44f02ad1f00](../../evidence/conditions-sets-023.md#c-3c3bf44f02ad1f00) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055940

```text
(config)# do-exec show ipv6 pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x34789A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cde1ef495915f519](../../evidence/conditions-sets-079.md#c-cde1ef495915f519) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055844

```text
(config)# do-exec show ipv6 pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x34788CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ded2554b8e2bc3b3](../../evidence/conditions-sets-086.md#c-ded2554b8e2bc3b3) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055895

```text
(config)# do-exec show ipv6 pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x34789228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b01176a7bf60b428](../../evidence/conditions-sets-068.md#c-b01176a7bf60b428) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055914

```text
(config)# do-exec show ipv6 pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x347894D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17b272665d5233ea](../../evidence/conditions-sets-009.md#c-17b272665d5233ea) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055928

```text
(config)# do-exec show ipv6 pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x34789778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58872643c21126d5](../../evidence/conditions-sets-035.md#c-58872643c21126d5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055965

```text
(config)# do-exec show ipv6 pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x34789FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec264fb8e2489296](../../evidence/conditions-sets-091.md#c-ec264fb8e2489296) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-058666

```text
(config)# do-exec show ipv6 pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478A280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-750a274d6e6b178e](../../evidence/conditions-sets-045.md#c-750a274d6e6b178e) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055948

```text
(config)# do-exec show ipv6 pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x34789CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-699e187b885282f4](../../evidence/conditions-sets-041.md#c-699e187b885282f4) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055964

```text
(config)# do-exec show ipv6 pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-714642d6eb508d99](../../evidence/conditions-sets-044.md#c-714642d6eb508d99) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055827

```text
(config)# do-exec show ipv6 pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x34788A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aea4b772a3ff2ad7](../../evidence/conditions-sets-068.md#c-aea4b772a3ff2ad7) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049977

```text
(config)# do-exec show ipv6 pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x34787A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-055770

```text
(config)# do-exec show ipv6 pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x347879E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049927

```text
(config)# do-exec show ipv6 pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x347876D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc94ffcad311ccbf](../../evidence/conditions-sets-073.md#c-bc94ffcad311ccbf) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040463

```text
(config)# do-exec show ipv6 pim neighbor <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 11 `；EOL ` RVA 0x355599F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ada276680e35130](../../evidence/conditions-sets-036.md#c-5ada276680e35130) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040464

```text
(config)# do-exec show ipv6 pim neighbor <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 2 `；EOL ` RVA 0x35559C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f381642e0b3cc4a](../../evidence/conditions-sets-049.md#c-7f381642e0b3cc4a) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061596

```text
(config)# do-exec show ipv6 pim neighbor <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 11 `；EOL ` RVA 0x355599F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-978c14e0a02c9863](../../evidence/conditions-sets-058.md#c-978c14e0a02c9863) · [缺口 G-848b6056a4643eab](../../evidence/gaps-sets-005.md#g-848b6056a4643eab) · [参数 P-0a6e9ba5a4647764](../../evidence/parameters-sets-001.md#p-0a6e9ba5a4647764) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061597

```text
(config)# do-exec show ipv6 pim neighbor <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 2 `；EOL ` RVA 0x35559C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6c551f5c355c0bb](../../evidence/conditions-sets-071.md#c-b6c551f5c355c0bb) · [缺口 G-848b6056a4643eab](../../evidence/gaps-sets-005.md#g-848b6056a4643eab) · [参数 P-0a6e9ba5a4647764](../../evidence/parameters-sets-001.md#p-0a6e9ba5a4647764) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049741

```text
(config)# do-exec show ipv6 pim pfp-sa announcements <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 23 `；EOL ` RVA 0x3555C3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8181142063b33f80](../../evidence/conditions-sets-050.md#c-8181142063b33f80) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049806

```text
(config)# do-exec show ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 25 `；EOL ` RVA 0x3555C8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8181142063b33f80](../../evidence/conditions-sets-050.md#c-8181142063b33f80) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049779

```text
(config)# do-exec show ipv6 pim pfp-sa originator <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 24 `；EOL ` RVA 0x3555C648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8181142063b33f80](../../evidence/conditions-sets-050.md#c-8181142063b33f80) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040459

```text
(config)# do-exec show ipv6 pim range-list <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 4 `；EOL ` RVA 0x3555A5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3088b1d5ee9da32](../../evidence/conditions-sets-081.md#c-d3088b1d5ee9da32) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040357

```text
(config)# do-exec show ipv6 pim topology <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x355592E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d6d502b8a37de169](../../evidence/conditions-sets-083.md#c-d6d502b8a37de169) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-049358

```text
(config)# do-exec show ipv6 pim topology route-count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 6 `；EOL ` RVA 0x35559040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-720cac7375bf424a](../../evidence/conditions-sets-044.md#c-720cac7375bf424a) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040561

```text
(config)# do-exec show ipv6 pim traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 16 `；EOL ` RVA 0x3555CB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1649ea0be899a88](../../evidence/conditions-sets-081.md#c-d1649ea0be899a88) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-040481

```text
(config)# do-exec show ipv6 pim tunnel <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 10 `；EOL ` RVA 0x3555ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc94fcd9d3653864](../../evidence/conditions-sets-085.md#c-dc94fcd9d3653864) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-061604

```text
(config)# do-exec show ipv6 pim tunnel <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 10 `；EOL ` RVA 0x3555ADC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b5f92c3a9df704f](../../evidence/conditions-sets-005.md#c-0b5f92c3a9df704f) · [缺口 G-6e07848da81fff95](../../evidence/gaps-sets-004.md#g-6e07848da81fff95) · [参数 P-b3e762b644a81f9b](../../evidence/parameters-sets-014.md#p-b3e762b644a81f9b) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062135

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> anycast-rp <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 20 `；EOL ` RVA 0x3555D920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce73b2099b427e22](../../evidence/conditions-sets-079.md#c-ce73b2099b427e22) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062424

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> bsr candidate-rp <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 13 `；EOL ` RVA 0x35551E10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-65fdd66196a37ff9](../../evidence/state_effects-sets-022.md#s-65fdd66196a37ff9)

### path-062429

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> bsr election <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 12 `；EOL ` RVA 0x35552360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-65fdd66196a37ff9](../../evidence/state_effects-sets-022.md#s-65fdd66196a37ff9)

### path-062425

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> bsr rp-cache <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 14 `；EOL ` RVA 0x355520B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-65fdd66196a37ff9](../../evidence/state_effects-sets-022.md#s-65fdd66196a37ff9)

### path-062134

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> gir <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 26 `；EOL ` RVA 0x3555DBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cbcd25e0346cfccc](../../evidence/conditions-sets-078.md#c-cbcd25e0346cfccc) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062103

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> lisp-rloc-state <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 27 `；EOL ` RVA 0x3555BC58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b3c26cd7832f399e](../../evidence/conditions-sets-070.md#c-b3c26cd7832f399e) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062148

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478A808 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062441

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x347886B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062569

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x34788378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e1f0585b0c76d4e7](../../evidence/conditions-sets-087.md#c-e1f0585b0c76d4e7) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-a74cba544ab0d424](../../evidence/state_effects-sets-035.md#s-a74cba544ab0d424)

### path-062630

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x34787F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [参数 P-957dcedf315a82c2](../../evidence/parameters-sets-011.md#p-957dcedf315a82c2) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062570

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x34788F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bae034eebeb9afc8](../../evidence/conditions-sets-072.md#c-bae034eebeb9afc8) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062574

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x34789A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9c8d58f49bd747b8](../../evidence/conditions-sets-060.md#c-9c8d58f49bd747b8) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062568

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x34788CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7dc36bd935f5cae7](../../evidence/conditions-sets-049.md#c-7dc36bd935f5cae7) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062571

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x34789228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74107aa8785a63df](../../evidence/conditions-sets-045.md#c-74107aa8785a63df) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062572

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x347894D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d0b565b3768a1e0](../../evidence/conditions-sets-018.md#c-2d0b565b3768a1e0) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062573

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x34789778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9b0eb9282e646a2](../../evidence/conditions-sets-084.md#c-d9b0eb9282e646a2) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062577

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x34789FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6babdae6076b26ba](../../evidence/conditions-sets-042.md#c-6babdae6076b26ba) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062631

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478A280 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6efab8f130fa8996](../../evidence/conditions-sets-043.md#c-6efab8f130fa8996) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062575

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x34789CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b1827fbd154c653f](../../evidence/conditions-sets-069.md#c-b1827fbd154c653f) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062576

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478A510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f51622a6a43807ad](../../evidence/conditions-sets-095.md#c-f51622a6a43807ad) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062565

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x34788A30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce1f014fbe5b11a0](../../evidence/conditions-sets-079.md#c-ce1f014fbe5b11a0) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062427

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x34787A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062563

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x347879E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062423

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x347876D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc44f9838a672583](../../evidence/conditions-sets-079.md#c-cc44f9838a672583) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062415

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> pfp-sa announcements <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 23 `；EOL ` RVA 0x3555C3A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bed7a8cac8fe21ef](../../evidence/conditions-sets-074.md#c-bed7a8cac8fe21ef) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062418

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> pfp-sa cache <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 25 `；EOL ` RVA 0x3555C8F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bed7a8cac8fe21ef](../../evidence/conditions-sets-074.md#c-bed7a8cac8fe21ef) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062417

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> pfp-sa originator <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 24 `；EOL ` RVA 0x3555C648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bed7a8cac8fe21ef](../../evidence/conditions-sets-074.md#c-bed7a8cac8fe21ef) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062101

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> range-list <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 4 `；EOL ` RVA 0x3555A5A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44de41f4ed01b41e](../../evidence/conditions-sets-027.md#c-44de41f4ed01b41e) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062093

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> topology <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x355592E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-063147a185a3ee7c](../../evidence/conditions-sets-003.md#c-063147a185a3ee7c) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062395

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> topology route-count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 6 `；EOL ` RVA 0x35559040 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-097db88096a415c2](../../evidence/conditions-sets-004.md#c-097db88096a415c2) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-062119

```text
(config)# do-exec show ipv6 pim vrf <?option@55558aaac9d8> traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 16 `；EOL ` RVA 0x3555CB98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2704a7169560a893](../../evidence/conditions-sets-015.md#c-2704a7169560a893) · [缺口 G-5a57feccdfcc5ab5](../../evidence/gaps-sets-004.md#g-5a57feccdfcc5ab5) · [状态效果 S-97afdbbcc15592a1](../../evidence/state_effects-sets-032.md#s-97afdbbcc15592a1)

### path-032120

```text
(config)# do-exec show ipv6 policy <cr>
```

Handler ` RVA 0x118BA0F0 `；selector ` 0 `；EOL ` RVA 0x3559C548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061019

```text
(config)# do-exec show ipv6 prefix <?match_ipv6_pfxinfo_action@55558ad32948> <cr>
```

Handler ` RVA 0x12300A90 `；selector ` 0 `；EOL ` RVA 0x357DE9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d99da25542a68a26](../../evidence/conditions-sets-084.md#c-d99da25542a68a26) · [缺口 G-7d074174f3f780b6](../../evidence/gaps-sets-005.md#g-7d074174f3f780b6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040635

```text
(config)# do-exec show ipv6 prefix reserved <cr>
```

Handler ` RVA 0x12300A90 `；selector ` 0 `；EOL ` RVA 0x357DE9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99da25542a68a26](../../evidence/conditions-sets-084.md#c-d99da25542a68a26) · [状态效果 S-724c5d77df86bea1](../../evidence/state_effects-sets-024.md#s-724c5d77df86bea1)

### path-032108

```text
(config)# do-exec show ipv6 prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x3557F168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df580d5aafc9c146](../../evidence/conditions-sets-086.md#c-df580d5aafc9c146) · [状态效果 S-e1a94215853c7fac](../../evidence/state_effects-sets-048.md#s-e1a94215853c7fac)

### path-061630

```text
(config)# do-exec show ipv6 prefix-list <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 4 `；EOL ` RVA 0x3557F540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-8274201190583b16](../../evidence/conditions-sets-051.md#c-8274201190583b16) · [缺口 G-c72ac1d990c03bb5](../../evidence/gaps-sets-007.md#g-c72ac1d990c03bb5) · [参数 P-7cf8c3bf40aa5c59](../../evidence/parameters-sets-010.md#p-7cf8c3bf40aa5c59) · [状态效果 S-e1a94215853c7fac](../../evidence/state_effects-sets-048.md#s-e1a94215853c7fac)

### path-055647

```text
(config)# do-exec show ipv6 prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x3557F210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-df580d5aafc9c146](../../evidence/conditions-sets-086.md#c-df580d5aafc9c146) · [参数 P-46df89ae42bf78b4](../../evidence/parameters-sets-006.md#p-46df89ae42bf78b4) · [状态效果 S-e1a94215853c7fac](../../evidence/state_effects-sets-048.md#s-e1a94215853c7fac)

### path-040542

```text
(config)# do-exec show ipv6 prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x3557EE68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e1a94215853c7fac](../../evidence/state_effects-sets-048.md#s-e1a94215853c7fac)

### path-040509

```text
(config)# do-exec show ipv6 prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x3557EB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e1a94215853c7fac](../../evidence/state_effects-sets-048.md#s-e1a94215853c7fac)

### path-031772

```text
(config)# do-exec show ipv6 protocols <cr>
```

Handler ` RVA 0x1230B1E0 `；selector ` 0 `；EOL ` RVA 0x357EAF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061527

```text
(config)# do-exec show ipv6 protocols vrf <?match_ipv6_zoneinfo_action@55558ad3ef00> <cr>
```

Handler ` RVA 0x1230B1E0 `；selector ` 0 `；EOL ` RVA 0x357EAF78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-12223e2a05513965](../../evidence/gaps-sets-001.md#g-12223e2a05513965) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061011

```text
(config)# do-exec show ipv6 reassembly <interface> <cr>
```

Handler ` RVA 0xC78A5E0 `；selector ` 0 `；EOL ` RVA 0x33AE9230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51bf728a71c0c334](../../evidence/conditions-sets-032.md#c-51bf728a71c0c334) · [缺口 G-977771d0856f9f40](../../evidence/gaps-sets-006.md#g-977771d0856f9f40) · [参数 P-dff3f5e0b6ccd83c](../../evidence/parameters-sets-017.md#p-dff3f5e0b6ccd83c) · [状态效果 S-b08cdd132fcf22c3](../../evidence/state_effects-sets-037.md#s-b08cdd132fcf22c3)

### path-032047

```text
(config)# do-exec show ipv6 rip <cr>
```

Handler ` RVA 0x118A5B90 `；selector ` 0 `；EOL ` RVA 0x3557C408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b5cba3f93193414b](../../evidence/conditions-sets-070.md#c-b5cba3f93193414b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061017

```text
(config)# do-exec show ipv6 rip <string> <cr>
```

Handler ` RVA 0x118A5B90 `；selector ` 0 `；EOL ` RVA 0x3557C408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RIP process name。

[条件 C-37d6c24683a12064](../../evidence/conditions-sets-022.md#c-37d6c24683a12064) · [缺口 G-3c27e534c7c7a36b](../../evidence/gaps-sets-003.md#g-3c27e534c7c7a36b) · [参数 P-75bb4366d8e82630](../../evidence/parameters-sets-009.md#p-75bb4366d8e82630) · [状态效果 S-c5e702421f006af4](../../evidence/state_effects-sets-042.md#s-c5e702421f006af4)

### path-061614

```text
(config)# do-exec show ipv6 rip <string> database <cr>
```

Handler ` RVA 0x118A4C60 `；selector ` 0 `；EOL ` RVA 0x3557BDF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RIP process name。

[条件 C-e159ec7892263356](../../evidence/conditions-sets-087.md#c-e159ec7892263356) · [缺口 G-3c27e534c7c7a36b](../../evidence/gaps-sets-003.md#g-3c27e534c7c7a36b) · [参数 P-75bb4366d8e82630](../../evidence/parameters-sets-009.md#p-75bb4366d8e82630) · [状态效果 S-c5e702421f006af4](../../evidence/state_effects-sets-042.md#s-c5e702421f006af4)

### path-061619

```text
(config)# do-exec show ipv6 rip <string> next-hops <cr>
```

Handler ` RVA 0x118A5450 `；selector ` 0 `；EOL ` RVA 0x3557C0A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RIP process name。

[条件 C-e159ec7892263356](../../evidence/conditions-sets-087.md#c-e159ec7892263356) · [缺口 G-3c27e534c7c7a36b](../../evidence/gaps-sets-003.md#g-3c27e534c7c7a36b) · [参数 P-75bb4366d8e82630](../../evidence/parameters-sets-009.md#p-75bb4366d8e82630) · [状态效果 S-c5e702421f006af4](../../evidence/state_effects-sets-042.md#s-c5e702421f006af4)

### path-040295

```text
(config)# do-exec show ipv6 rip database <cr>
```

Handler ` RVA 0x118A4C60 `；selector ` 0 `；EOL ` RVA 0x3557BDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9351343fd5534385](../../evidence/conditions-sets-057.md#c-9351343fd5534385) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040329

```text
(config)# do-exec show ipv6 rip next-hops <cr>
```

Handler ` RVA 0x118A5450 `；selector ` 0 `；EOL ` RVA 0x3557C0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9351343fd5534385](../../evidence/conditions-sets-057.md#c-9351343fd5534385) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061606

```text
(config)# do-exec show ipv6 route <?match_ipv6_pfxinfo_action@55558ad3cec8> longer-prefixes <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1318af3bb8627100](../../evidence/conditions-sets-008.md#c-1318af3bb8627100) · [缺口 G-27354695592d47c8](../../evidence/gaps-sets-002.md#g-27354695592d47c8) · [状态效果 S-ea203b8230cbabbc](../../evidence/state_effects-sets-050.md#s-ea203b8230cbabbc)

### path-040513

```text
(config)# do-exec show ipv6 route <address> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 name or address。

[条件 C-ce076a9fb1ca7310](../../evidence/conditions-sets-079.md#c-ce076a9fb1ca7310) · [参数 P-43b1e41b4080817f](../../evidence/parameters-sets-006.md#p-43b1e41b4080817f) · [状态效果 S-923293f37e691223](../../evidence/state_effects-sets-031.md#s-923293f37e691223)

