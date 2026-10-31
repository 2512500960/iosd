# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-050532

```text
(config)# do-exec show policy-map session brief <string> <cr>
```

Handler ` RVA 0xD889230 `；selector ` 0 `；EOL ` RVA 0x33F22138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-d032ba8a06103bf7](../../evidence/state_effects-sets-044.md#s-d032ba8a06103bf7)

### path-056068

```text
(config)# do-exec show policy-map session brief <string> timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 2 `；EOL ` RVA 0x33F21EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-17e65166934f7e81](../../evidence/state_effects-sets-005.md#s-17e65166934f7e81)

### path-056100

```text
(config)# do-exec show policy-map session brief <string> vrf <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F21BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[条件 C-40770bc8a4c52717](../../evidence/conditions-sets-025.md#c-40770bc8a4c52717) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-0824c3205c9ad7fe](../../evidence/state_effects-sets-002.md#s-0824c3205c9ad7fe)

### path-058699

```text
(config)# do-exec show policy-map session brief <string> vrf <string> <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F21948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name；` string ` VRF name。

[条件 C-40770bc8a4c52717](../../evidence/conditions-sets-025.md#c-40770bc8a4c52717) · [参数 P-3dbd6dbc914eb89a](../../evidence/parameters-sets-005.md#p-3dbd6dbc914eb89a) · [状态效果 S-0e8e44693a5229dc](../../evidence/state_effects-sets-003.md#s-0e8e44693a5229dc)

### path-059568

```text
(config)# do-exec show policy-map session brief <string> vrf <string> timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F216D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name；` string ` VRF name。

[条件 C-40770bc8a4c52717](../../evidence/conditions-sets-025.md#c-40770bc8a4c52717) · [参数 P-3dbd6dbc914eb89a](../../evidence/parameters-sets-005.md#p-3dbd6dbc914eb89a) · [状态效果 S-f86fd70b6b1ef664](../../evidence/state_effects-sets-053.md#s-f86fd70b6b1ef664)

### path-058695

```text
(config)# do-exec show policy-map session brief <string> vrf timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F212F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy-map name。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-3607f57d332cc936](../../evidence/state_effects-sets-012.md#s-3607f57d332cc936)

### path-050443

```text
(config)# do-exec show policy-map session brief timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 2 `；EOL ` RVA 0x33F20E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0225f4279e87a276](../../evidence/conditions-sets-001.md#c-0225f4279e87a276) · [状态效果 S-e30b5ec682c6f5ad](../../evidence/state_effects-sets-048.md#s-e30b5ec682c6f5ad)

### path-050474

```text
(config)# do-exec show policy-map session brief vrfs <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F206C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9989e47c1ebeff96](../../evidence/conditions-sets-059.md#c-9989e47c1ebeff96) · [状态效果 S-e30b5ec682c6f5ad](../../evidence/state_effects-sets-048.md#s-e30b5ec682c6f5ad)

### path-056045

```text
(config)# do-exec show policy-map session brief vrfs <string> <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F20730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name。

[条件 C-9989e47c1ebeff96](../../evidence/conditions-sets-059.md#c-9989e47c1ebeff96) · [参数 P-e418100594147980](../../evidence/parameters-sets-017.md#p-e418100594147980) · [状态效果 S-e30b5ec682c6f5ad](../../evidence/state_effects-sets-048.md#s-e30b5ec682c6f5ad)

### path-058691

```text
(config)# do-exec show policy-map session brief vrfs <string> timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F20770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name。

[条件 C-9989e47c1ebeff96](../../evidence/conditions-sets-059.md#c-9989e47c1ebeff96) · [参数 P-e418100594147980](../../evidence/parameters-sets-017.md#p-e418100594147980) · [状态效果 S-d61e53861322a2da](../../evidence/state_effects-sets-045.md#s-d61e53861322a2da)

### path-056030

```text
(config)# do-exec show policy-map session brief vrfs timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F203D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0225f4279e87a276](../../evidence/conditions-sets-001.md#c-0225f4279e87a276) · [状态效果 S-a918368beb4427e4](../../evidence/state_effects-sets-036.md#s-a918368beb4427e4)

### path-050440

```text
(config)# do-exec show policy-map session class <string> <cr>
```

Handler ` RVA 0xD88A410 `；selector ` 0 `；EOL ` RVA 0x33F22688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` class-map name。

[条件 C-0225f4279e87a276](../../evidence/conditions-sets-001.md#c-0225f4279e87a276) · [参数 P-a4b7ae5f6035cab1](../../evidence/parameters-sets-013.md#p-a4b7ae5f6035cab1) · [状态效果 S-e30b5ec682c6f5ad](../../evidence/state_effects-sets-048.md#s-e30b5ec682c6f5ad)

### path-032425

```text
(config)# do-exec show policy-map summary <cr>
```

Handler ` RVA 0xD888ED0 `；selector ` 0 `；EOL ` RVA 0x33F23D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f893f7d9e7163cf](../../evidence/conditions-sets-031.md#c-4f893f7d9e7163cf) · [状态效果 S-5a36616b011c7804](../../evidence/state_effects-sets-019.md#s-5a36616b011c7804)

### path-032663

```text
(config)# do-exec show policy-map target <cr>
```

Handler ` RVA 0xD894B50 `；selector ` 1 `；EOL ` RVA 0x33F27068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [状态效果 S-189253730a34769d](../../evidence/state_effects-sets-006.md#s-189253730a34769d)

### path-041418

```text
(config)# do-exec show policy-map target sub-interface <cr>
```

Handler ` RVA 0xD894B50 `；selector ` 0 `；EOL ` RVA 0x33F26BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [状态效果 S-4e34accb12a13802](../../evidence/state_effects-sets-017.md#s-4e34accb12a13802)

### path-058690

```text
(config)# do-exec show policy-map target vrf <string> ipv4 input <cr>
```

Handler ` RVA 0xD8A0B50 `；selector ` 0 `；EOL ` RVA 0x33F28DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF Name.。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [参数 P-977bbc179da5941a](../../evidence/parameters-sets-012.md#p-977bbc179da5941a) · [状态效果 S-3f04ed16b63ba6c9](../../evidence/state_effects-sets-014.md#s-3f04ed16b63ba6c9)

### path-058705

```text
(config)# do-exec show policy-map target vrf <string> type nwpi <cr>
```

Handler ` RVA 0xD8A1240 `；selector ` 0 `；EOL ` RVA 0x33F292B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF Name.。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [参数 P-977bbc179da5941a](../../evidence/parameters-sets-012.md#p-977bbc179da5941a) · [状态效果 S-f068a8930dcc0948](../../evidence/state_effects-sets-051.md#s-f068a8930dcc0948)

### path-061692

```text
(config)# do-exec show policy-map type control <?option@555589143ca8> <cr>
```

Handler ` RVA 0xCB5AF00 `；selector ` 0 `；EOL ` RVA 0x33BEFE40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc2547d278b58e49](../../evidence/conditions-sets-097.md#c-fc2547d278b58e49) · [缺口 G-0367ee558c03806b](../../evidence/gaps-sets-001.md#g-0367ee558c03806b) · [状态效果 S-8d2a361a9bee17a4](../../evidence/state_effects-sets-030.md#s-8d2a361a9bee17a4)

### path-027805

```text
(config)# do-exec show port-security <cr>
```

Handler ` RVA 0x15F55EA0 `；selector ` 0 `；EOL ` RVA 0x35E724E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-32fabe02d7eafa75](../../evidence/state_effects-sets-011.md#s-32fabe02d7eafa75)

### path-061193

```text
(config)# do-exec show port-security interface <interface> <cr>
```

Handler ` RVA 0x15F55EA0 `；selector ` 0 `；EOL ` RVA 0x35E724E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2e2dd3ffdaeb41aa](../../evidence/conditions-sets-018.md#c-2e2dd3ffdaeb41aa) · [缺口 G-bd069296f95bd877](../../evidence/gaps-sets-007.md#g-bd069296f95bd877) · [参数 P-56a9f6ef0db1cb73](../../evidence/parameters-sets-007.md#p-56a9f6ef0db1cb73) · [状态效果 S-c98be657b328ca79](../../evidence/state_effects-sets-043.md#s-c98be657b328ca79)

### path-027427

```text
(config)# do-exec show power <cr>
```

Handler ` RVA 0x1606BEB0 `；selector ` 0 `；EOL ` RVA 0x35EABE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-114e00f417e641ac](../../evidence/conditions-sets-007.md#c-114e00f417e641ac) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030691

```text
(config)# do-exec show power detail <cr>
```

Handler ` RVA 0x1606BFA0 `；selector ` 0 `；EOL ` RVA 0x35EABB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d66e06e55a6f6b34](../../evidence/conditions-sets-083.md#c-d66e06e55a6f6b34) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030749

```text
(config)# do-exec show power history <cr>
```

Handler ` RVA 0x1606BF00 `；selector ` 0 `；EOL ` RVA 0x35EABE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef51306a05334dd5](../../evidence/conditions-sets-092.md#c-ef51306a05334dd5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030802

```text
(config)# do-exec show power inline <cr>
```

Handler ` RVA 0x16028620 `；selector ` 0 `；EOL ` RVA 0x35EA27D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-365e7e9b55f0a771](../../evidence/conditions-sets-021.md#c-365e7e9b55f0a771) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060925

```text
(config)# do-exec show power inline <interface> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 1 `；EOL ` RVA 0x35EA22A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b16476322f2487bd](../../evidence/conditions-sets-069.md#c-b16476322f2487bd) · [缺口 G-ff3697d5e265f0d1](../../evidence/gaps-sets-009.md#g-ff3697d5e265f0d1) · [参数 P-141eef88753092a7](../../evidence/parameters-sets-002.md#p-141eef88753092a7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061426

```text
(config)# do-exec show power inline <interface> detail <cr>
```

Handler ` RVA 0x16028620 `；selector ` 2 `；EOL ` RVA 0x35EA2278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b16476322f2487bd](../../evidence/conditions-sets-069.md#c-b16476322f2487bd) · [缺口 G-ff3697d5e265f0d1](../../evidence/gaps-sets-009.md#g-ff3697d5e265f0d1) · [参数 P-141eef88753092a7](../../evidence/parameters-sets-002.md#p-141eef88753092a7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062835

```text
(config)# do-exec show power inline allocation default <cr>
```

Handler ` RVA 0x16028620 `；selector ` 3 `；EOL ` RVA 0x35EA3BF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-37e0a868660af903](../../evidence/conditions-sets-022.md#c-37e0a868660af903) · [缺口 G-4dcf7a999c326c71](../../evidence/gaps-sets-003.md#g-4dcf7a999c326c71) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-062797

```text
(config)# do-exec show power inline consumption <cr>
```

Handler ` RVA 0x16028620 `；selector ` 4 `；EOL ` RVA 0x35EA3520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4b6f25722d3e14b1](../../evidence/conditions-sets-030.md#c-4b6f25722d3e14b1) · [缺口 G-4dcf7a999c326c71](../../evidence/gaps-sets-003.md#g-4dcf7a999c326c71) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-062959

```text
(config)# do-exec show power inline consumption <interface> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 6 `；EOL ` RVA 0x35EA3210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9145002df76d4ee8](../../evidence/conditions-sets-056.md#c-9145002df76d4ee8) · [缺口 G-0bd84587e6c865e6](../../evidence/gaps-sets-001.md#g-0bd84587e6c865e6) · [参数 P-8314efcc850522ed](../../evidence/parameters-sets-010.md#p-8314efcc850522ed) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-062974

```text
(config)# do-exec show power inline consumption module <number:dynamic> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 5 `；EOL ` RVA 0x35EA3650 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-1b630d525d56d907](../../evidence/conditions-sets-011.md#c-1b630d525d56d907) · [缺口 G-f294df5f89823088](../../evidence/gaps-sets-008.md#g-f294df5f89823088) · [参数 P-fd4cf5e3866ba9fa](../../evidence/parameters-sets-019.md#p-fd4cf5e3866ba9fa) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-037489

```text
(config)# do-exec show power inline dynamic-priority <cr>
```

Handler ` RVA 0x16013BA0 `；selector ` 0 `；EOL ` RVA 0x35EA1400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d558c2c7f55b6a7](../../evidence/conditions-sets-011.md#c-1d558c2c7f55b6a7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062992

```text
(config)# do-exec show power inline hardware poe get <number:dynamic> global <cr>
```

Handler ` RVA 0x16038630 `；selector ` 4 `；EOL ` RVA 0x35EA4140 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-e1052a0537d85524](../../evidence/conditions-sets-087.md#c-e1052a0537d85524) · [缺口 G-a3d2f539196446cc](../../evidence/gaps-sets-006.md#g-a3d2f539196446cc) · [参数 P-86d131f4901970ab](../../evidence/parameters-sets-010.md#p-86d131f4901970ab) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-062993

```text
(config)# do-exec show power inline hardware poe get <number:dynamic> port <cr>
```

Handler ` RVA 0x16038630 `；selector ` 3 `；EOL ` RVA 0x35EA4410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-2550662aa740542c](../../evidence/conditions-sets-015.md#c-2550662aa740542c) · [缺口 G-a3d2f539196446cc](../../evidence/gaps-sets-006.md#g-a3d2f539196446cc) · [参数 P-86d131f4901970ab](../../evidence/parameters-sets-010.md#p-86d131f4901970ab) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-062997

```text
(config)# do-exec show power inline hardware poe get <number:dynamic> port <number:1..48> <cr>
```

Handler ` RVA 0x16038630 `；selector ` 1 `；EOL ` RVA 0x35EA43E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Port Number。

[条件 C-2550662aa740542c](../../evidence/conditions-sets-015.md#c-2550662aa740542c) · [缺口 G-a3d2f539196446cc](../../evidence/gaps-sets-006.md#g-a3d2f539196446cc) · [参数 P-9bb54f29180486e6](../../evidence/parameters-sets-012.md#p-9bb54f29180486e6) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-062998

```text
(config)# do-exec show power inline hardware pse get <number:dynamic> <number:0..24> <number:1..255> <cr>
```

Handler ` RVA 0x16038630 `；selector ` 6 `；EOL ` RVA 0x35EA4B40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number；` unsigned_number ` Quad Chip number；` unsigned_number ` PSE register number。

[条件 C-a60c96f71b6e9b89](../../evidence/conditions-sets-064.md#c-a60c96f71b6e9b89) · [缺口 G-16c3e7708a13abbd](../../evidence/gaps-sets-001.md#g-16c3e7708a13abbd) · [参数 P-f28ea203ab0c2336](../../evidence/parameters-sets-018.md#p-f28ea203ab0c2336) · [状态效果 S-1de5d2b7a117ae54](../../evidence/state_effects-sets-007.md#s-1de5d2b7a117ae54)

### path-037509

```text
(config)# do-exec show power inline meter <cr>
```

Handler ` RVA 0x16028620 `；selector ` 18 `；EOL ` RVA 0x35E9F800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec90d2f1179777b1](../../evidence/conditions-sets-091.md#c-ec90d2f1179777b1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061411

```text
(config)# do-exec show power inline meter <interface> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 19 `；EOL ` RVA 0x35E9F4F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f82ec2d1eb54fbd9](../../evidence/conditions-sets-096.md#c-f82ec2d1eb54fbd9) · [缺口 G-98f2742e5a10e31a](../../evidence/gaps-sets-006.md#g-98f2742e5a10e31a) · [参数 P-93da883d9cbb6469](../../evidence/parameters-sets-011.md#p-93da883d9cbb6469) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061996

```text
(config)# do-exec show power inline meter module <number:dynamic> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 20 `；EOL ` RVA 0x35E9F930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-c23af7836f397ea2](../../evidence/conditions-sets-075.md#c-c23af7836f397ea2) · [缺口 G-30f385d6dd13275c](../../evidence/gaps-sets-002.md#g-30f385d6dd13275c) · [参数 P-b596ec6ee21aa010](../../evidence/parameters-sets-014.md#p-b596ec6ee21aa010) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061441

```text
(config)# do-exec show power inline module <number:dynamic> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 7 `；EOL ` RVA 0x35EA2978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-48e19f2df38ba763](../../evidence/conditions-sets-029.md#c-48e19f2df38ba763) · [缺口 G-f4dddcae040db549](../../evidence/gaps-sets-008.md#g-f4dddcae040db549) · [参数 P-94d63b1dd04e83f2](../../evidence/parameters-sets-011.md#p-94d63b1dd04e83f2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062005

```text
(config)# do-exec show power inline module <number:dynamic> detail <cr>
```

Handler ` RVA 0x16028620 `；selector ` 11 `；EOL ` RVA 0x35EA2950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-48e19f2df38ba763](../../evidence/conditions-sets-029.md#c-48e19f2df38ba763) · [缺口 G-f4dddcae040db549](../../evidence/gaps-sets-008.md#g-f4dddcae040db549) · [参数 P-94d63b1dd04e83f2](../../evidence/parameters-sets-011.md#p-94d63b1dd04e83f2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037572

```text
(config)# do-exec show power inline police <cr>
```

Handler ` RVA 0x16028620 `；selector ` 8 `；EOL ` RVA 0x35EA0D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cec7f9a8277ff60b](../../evidence/conditions-sets-080.md#c-cec7f9a8277ff60b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061416

```text
(config)# do-exec show power inline police <interface> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 9 `；EOL ` RVA 0x35EA0A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad4308f39708426f](../../evidence/conditions-sets-067.md#c-ad4308f39708426f) · [缺口 G-19c10a5823827dd3](../../evidence/gaps-sets-001.md#g-19c10a5823827dd3) · [参数 P-f9e7966890675d57](../../evidence/parameters-sets-019.md#p-f9e7966890675d57) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061999

```text
(config)# do-exec show power inline police module <number:dynamic> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 10 `；EOL ` RVA 0x35EA0E80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-846c7c1b8d50622e](../../evidence/conditions-sets-051.md#c-846c7c1b8d50622e) · [缺口 G-d6f56753aca764c5](../../evidence/gaps-sets-007.md#g-d6f56753aca764c5) · [参数 P-b1f58c7dc7f84fe4](../../evidence/parameters-sets-013.md#p-b1f58c7dc7f84fe4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037604

```text
(config)# do-exec show power inline priority <cr>
```

Handler ` RVA 0x16028620 `；selector ` 12 `；EOL ` RVA 0x35EA1AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f59b921c71fcfeb](../../evidence/conditions-sets-037.md#c-5f59b921c71fcfeb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061420

```text
(config)# do-exec show power inline priority <interface> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 14 `；EOL ` RVA 0x35EA17D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cda1484f20adc73a](../../evidence/conditions-sets-079.md#c-cda1484f20adc73a) · [缺口 G-e4e5e24bb21ff895](../../evidence/gaps-sets-008.md#g-e4e5e24bb21ff895) · [参数 P-768d37648d27b9e1](../../evidence/parameters-sets-009.md#p-768d37648d27b9e1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062001

```text
(config)# do-exec show power inline priority module <number:dynamic> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 13 `；EOL ` RVA 0x35EA1C10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-824bdfbc60f078e6](../../evidence/conditions-sets-050.md#c-824bdfbc60f078e6) · [缺口 G-aae5a5276eb60ea7](../../evidence/gaps-sets-006.md#g-aae5a5276eb60ea7) · [参数 P-df5be7ec87c14f05](../../evidence/parameters-sets-017.md#p-df5be7ec87c14f05) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037543

```text
(config)# do-exec show power inline upoe-plus <cr>
```

Handler ` RVA 0x16028620 `；selector ` 15 `；EOL ` RVA 0x35EA02A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-041254ca3cd26ab4](../../evidence/conditions-sets-002.md#c-041254ca3cd26ab4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061414

```text
(config)# do-exec show power inline upoe-plus <interface> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 16 `；EOL ` RVA 0x35E9FF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3ea1ae7f1996ffdc](../../evidence/conditions-sets-024.md#c-3ea1ae7f1996ffdc) · [缺口 G-f82e6221758893d6](../../evidence/gaps-sets-009.md#g-f82e6221758893d6) · [参数 P-e5bf57bd1be58069](../../evidence/parameters-sets-017.md#p-e5bf57bd1be58069) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061997

```text
(config)# do-exec show power inline upoe-plus module <number:dynamic> <cr>
```

Handler ` RVA 0x16028620 `；selector ` 17 `；EOL ` RVA 0x35EA03D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-9db67bdb89fa75f9](../../evidence/conditions-sets-061.md#c-9db67bdb89fa75f9) · [缺口 G-bbda7e7a28cec4dd](../../evidence/gaps-sets-007.md#g-bbda7e7a28cec4dd) · [参数 P-164e2a6af5a5b8e0](../../evidence/parameters-sets-002.md#p-164e2a6af5a5b8e0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030654

```text
(config)# do-exec show power usage <cr>
```

Handler ` RVA 0x1606BF50 `；selector ` 0 `；EOL ` RVA 0x35EAB858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf58bb22cacad229](../../evidence/conditions-sets-074.md#c-bf58bb22cacad229) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029767

```text
(config)# do-exec show ppp all <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 1 `；EOL ` RVA 0x3490D890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036984

```text
(config)# do-exec show ppp bap counters <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 18 `；EOL ` RVA 0x34487EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037136

```text
(config)# do-exec show ppp bap group <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 16 `；EOL ` RVA 0x34487558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-10a510f4b69a46c3](../../evidence/conditions-sets-007.md#c-10a510f4b69a46c3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046497

```text
(config)# do-exec show ppp bap group <string> <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 15 `；EOL ` RVA 0x34487530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-10a510f4b69a46c3](../../evidence/conditions-sets-007.md#c-10a510f4b69a46c3) · [参数 P-f42785924a741e53](../../evidence/parameters-sets-018.md#p-f42785924a741e53) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061966

```text
(config)# do-exec show ppp bap group zap <interface> <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 16 `；EOL ` RVA 0x34487558 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bdf6baa752264d47](../../evidence/conditions-sets-073.md#c-bdf6baa752264d47) · [缺口 G-6706f6f7b37d4412](../../evidence/gaps-sets-004.md#g-6706f6f7b37d4412) · [参数 P-8d5e9220e830d3b7](../../evidence/parameters-sets-011.md#p-8d5e9220e830d3b7) · [状态效果 S-45fa24192cebd8f2](../../evidence/state_effects-sets-015.md#s-45fa24192cebd8f2)

### path-062313

```text
(config)# do-exec show ppp bap group zap <interface> <string> <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 15 `；EOL ` RVA 0x34487530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Group name。

[条件 C-bdf6baa752264d47](../../evidence/conditions-sets-073.md#c-bdf6baa752264d47) · [缺口 G-6706f6f7b37d4412](../../evidence/gaps-sets-004.md#g-6706f6f7b37d4412) · [参数 P-b73a747992e33c34](../../evidence/parameters-sets-014.md#p-b73a747992e33c34) · [状态效果 S-45fa24192cebd8f2](../../evidence/state_effects-sets-015.md#s-45fa24192cebd8f2)

### path-036889

```text
(config)# do-exec show ppp bap queues <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 17 `；EOL ` RVA 0x34487BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036257

```text
(config)# do-exec show ppp disconnect history <cr>
```

Handler ` RVA 0xFEDDCC0 `；selector ` 0 `；EOL ` RVA 0x3490DE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036073

```text
(config)# do-exec show ppp disconnect stats <cr>
```

Handler ` RVA 0xFEDDD20 `；selector ` 0 `；EOL ` RVA 0x3490DBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036219

```text
(config)# do-exec show ppp id <number:1..4294967295> <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 2 `；EOL ` RVA 0x3490E538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPP Unique ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d4e284cec2e04a4a](../../evidence/parameters-sets-016.md#p-d4e284cec2e04a4a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060857

```text
(config)# do-exec show ppp interface <interface> <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 3 `；EOL ` RVA 0x3490E210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-de0101e67ed04c03](../../evidence/conditions-sets-086.md#c-de0101e67ed04c03) · [缺口 G-18e209ab5f26c7a5](../../evidence/gaps-sets-001.md#g-18e209ab5f26c7a5) · [参数 P-c8a782bee30302ec](../../evidence/parameters-sets-015.md#p-c8a782bee30302ec) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030225

```text
(config)# do-exec show ppp memory <cr>
```

Handler ` RVA 0xFEC1750 `；selector ` 10 `；EOL ` RVA 0x3490FB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060885

```text
(config)# do-exec show ppp mppe <interface> <cr>
```

Handler ` RVA 0xFEC1660 `；selector ` 9 `；EOL ` RVA 0x349101D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4430a3fd4df24008](../../evidence/conditions-sets-027.md#c-4430a3fd4df24008) · [缺口 G-a7e23245a990ae21](../../evidence/gaps-sets-006.md#g-a7e23245a990ae21) · [参数 P-bd6391580d03e41a](../../evidence/parameters-sets-014.md#p-bd6391580d03e41a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030522

```text
(config)# do-exec show ppp multilink <cr>
```

Handler ` RVA 0xFF79560 `；selector ` 14 `；EOL ` RVA 0x3493E320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061393

```text
(config)# do-exec show ppp multilink interface <interface> <cr>
```

Handler ` RVA 0xFF79560 `；selector ` 14 `；EOL ` RVA 0x3493E320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a21b53b9b95927c](../../evidence/conditions-sets-047.md#c-7a21b53b9b95927c) · [缺口 G-b6d052acccd4c51c](../../evidence/gaps-sets-006.md#g-b6d052acccd4c51c) · [参数 P-4f19527cf9bf1bea](../../evidence/parameters-sets-007.md#p-4f19527cf9bf1bea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030150

```text
(config)# do-exec show ppp protocols <cr>
```

Handler ` RVA 0xFEC1700 `；selector ` 7 `；EOL ` RVA 0x3490F868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030078

```text
(config)# do-exec show ppp queues <cr>
```

Handler ` RVA 0xFEDEC00 `；selector ` 8 `；EOL ` RVA 0x3490F318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030092

```text
(config)# do-exec show ppp statistics <cr>
```

Handler ` RVA 0xFEDD2E0 `；selector ` 6 `；EOL ` RVA 0x3490ED78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036347

```text
(config)# do-exec show ppp statistics fsm <cr>
```

Handler ` RVA 0xFEC76B0 `；selector ` 13 `；EOL ` RVA 0x3490EAD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036673

```text
(config)# do-exec show ppp subscriber statistics <cr>
```

Handler ` RVA 0xFF12CE0 `；selector ` 11 `；EOL ` RVA 0x3490FE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029977

```text
(config)# do-exec show ppp summary <cr>
```

Handler ` RVA 0xFEDE3A0 `；selector ` 5 `；EOL ` RVA 0x3490E7C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036408

```text
(config)# do-exec show ppp syslog statistics <cr>
```

Handler ` RVA 0xFEDECC0 `；selector ` 12 `；EOL ` RVA 0x3490F088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030119

```text
(config)# do-exec show ppp throttled <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 4 `；EOL ` RVA 0x3490F5C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032627

```text
(config)# do-exec show pppatm redundancy <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 3 `；EOL ` RVA 0x35404A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032689

```text
(config)# do-exec show pppatm session <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 2 `；EOL ` RVA 0x35404FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061697

```text
(config)# do-exec show pppatm session interface <interface> <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 2 `；EOL ` RVA 0x35404FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-90ba76e609447fb3](../../evidence/conditions-sets-056.md#c-90ba76e609447fb3) · [缺口 G-67d964d285f2fb2f](../../evidence/gaps-sets-004.md#g-67d964d285f2fb2f) · [参数 P-82db2b7afcd93685](../../evidence/parameters-sets-010.md#p-82db2b7afcd93685) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032650

```text
(config)# do-exec show pppatm statistics <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 4 `；EOL ` RVA 0x35404CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032599

```text
(config)# do-exec show pppatm summary <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 1 `；EOL ` RVA 0x35404788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062446

```text
(config)# do-exec show pppatm trace interface <interface> vc <string> <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 0 `；EOL ` RVA 0x35404310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Connection Name。

[条件 C-3bd05da70ffb0bd4](../../evidence/conditions-sets-023.md#c-3bd05da70ffb0bd4) · [缺口 G-f96603fac7f1509d](../../evidence/gaps-sets-009.md#g-f96603fac7f1509d) · [参数 P-c12a3ed39316178c](../../evidence/parameters-sets-015.md#p-c12a3ed39316178c) · [状态效果 S-14c1085f6e970258](../../evidence/state_effects-sets-005.md#s-14c1085f6e970258)

### path-048370

```text
(config)# do-exec show pppoe derived group <string> <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 7 `；EOL ` RVA 0x356ADAD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the PPPoE group。

[条件 C-8b73de39b2bfa08a](../../evidence/conditions-sets-054.md#c-8b73de39b2bfa08a) · [参数 P-4b93aedf3e835547](../../evidence/parameters-sets-006.md#p-4b93aedf3e835547) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061513

```text
(config)# do-exec show pppoe session interface <interface> <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 8 `；EOL ` RVA 0x356ACF98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f76fdba57d14fa0c](../../evidence/conditions-sets-096.md#c-f76fdba57d14fa0c) · [缺口 G-04fec21f48763f61](../../evidence/gaps-sets-001.md#g-04fec21f48763f61) · [参数 P-7075e6d365f35ae6](../../evidence/parameters-sets-009.md#p-7075e6d365f35ae6) · [状态效果 S-6c8a53c23cda28b1](../../evidence/state_effects-sets-023.md#s-6c8a53c23cda28b1)

### path-031684

```text
(config)# do-exec show pppoe statistics <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 9 `；EOL ` RVA 0x356ADD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b73de39b2bfa08a](../../evidence/conditions-sets-054.md#c-8b73de39b2bfa08a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031609

```text
(config)# do-exec show pppoe summary <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 8 `；EOL ` RVA 0x356ACF98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-661833a3c51ae4a1](../../evidence/state_effects-sets-022.md#s-661833a3c51ae4a1)

### path-039551

```text
(config)# do-exec show pppoe vrrs summary <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 10 `；EOL ` RVA 0x356AE0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-035738617d0a2b60](../../evidence/conditions-sets-002.md#c-035738617d0a2b60) · [状态效果 S-edde24977a4457ef](../../evidence/state_effects-sets-050.md#s-edde24977a4457ef)

### path-026387

```text
(config)# do-exec show privilege <cr>
```

Handler ` RVA 0xDF438A0 `；selector ` 0 `；EOL ` RVA 0x34126C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027339

```text
(config)# do-exec show processes <cr>
```

Handler ` RVA 0xE083200 `；selector ` 0 `；EOL ` RVA 0x341E2588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030346

```text
(config)# do-exec show processes <number:1..2147483647> <cr>
```

Handler ` RVA 0xE0475E0 `；selector ` 0 `；EOL ` RVA 0x341E22D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IOS(d) Process Number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-56677249233b99d8](../../evidence/parameters-sets-007.md#p-56677249233b99d8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030115

```text
(config)# do-exec show processes all-events <cr>
```

Handler ` RVA 0xE0863A0 `；selector ` 0 `；EOL ` RVA 0x341DF120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd969664c9724878](../../evidence/conditions-sets-073.md#c-bd969664c9724878) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030257

```text
(config)# do-exec show processes bootup-init <cr>
```

Handler ` RVA 0xE047460 `；selector ` 0 `；EOL ` RVA 0x341E0338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c2248ce3c0bc6834](../../evidence/conditions-sets-075.md#c-c2248ce3c0bc6834) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030219

```text
(config)# do-exec show processes bootup-time <cr>
```

Handler ` RVA 0xE0472D0 `；selector ` 0 `；EOL ` RVA 0x341E0090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef446159c9cea4be](../../evidence/conditions-sets-092.md#c-ef446159c9cea4be) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030421

```text
(config)# do-exec show processes cpu <cr>
```

Handler ` RVA 0xE083260 `；selector ` 0 `；EOL ` RVA 0x341E1820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046277

```text
(config)# do-exec show processes cpu autoprofile hog <cr>
```

Handler ` RVA 0xE087310 `；selector ` 0 `；EOL ` RVA 0x341E12B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046327

```text
(config)# do-exec show processes cpu autoprofile process <cr>
```

Handler ` RVA 0xE087380 `；selector ` 0 `；EOL ` RVA 0x341E1560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037033

```text
(config)# do-exec show processes cpu extended <cr>
```

Handler ` RVA 0xE0873F0 `；selector ` 0 `；EOL ` RVA 0x341E1860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046387

```text
(config)# do-exec show processes cpu extended accounting <cr>
```

Handler ` RVA 0xE088780 `；selector ` 0 `；EOL ` RVA 0x341E1B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1214c0b787e7dd1](../../evidence/conditions-sets-062.md#c-a1214c0b787e7dd1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036836

```text
(config)# do-exec show processes cpu history <cr>
```

Handler ` RVA 0xE048EC0 `；selector ` 0 `；EOL ` RVA 0x341E06D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046168

```text
(config)# do-exec show processes cpu history table <cr>
```

Handler ` RVA 0xE0869D0 `；selector ` 0 `；EOL ` RVA 0x341E06B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036873

```text
(config)# do-exec show processes cpu monitor <cr>
```

Handler ` RVA 0xE083C90 `；selector ` 0 `；EOL ` RVA 0x341E0C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036905

```text
(config)# do-exec show processes cpu sorted <cr>
```

Handler ` RVA 0xE083640 `；selector ` 0 `；EOL ` RVA 0x341E0F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030190

```text
(config)# do-exec show processes events <cr>
```

Handler ` RVA 0xE0862A0 `；selector ` 0 `；EOL ` RVA 0x341DF430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a5b0ed31ac872242](../../evidence/conditions-sets-064.md#c-a5b0ed31ac872242) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030040

```text
(config)# do-exec show processes heapcheck <cr>
```

Handler ` RVA 0xE04C3C0 `；selector ` 0 `；EOL ` RVA 0x341DEBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030320

```text
(config)# do-exec show processes history <cr>
```

Handler ` RVA 0xE047B20 `；selector ` 0 `；EOL ` RVA 0x341E2030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030332

```text
(config)# do-exec show processes memory <cr>
```

Handler ` RVA 0xE084D90 `；selector ` 0 `；EOL ` RVA 0x341DF720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036778

```text
(config)# do-exec show processes memory old-header <cr>
```

Handler ` RVA 0xE084D00 `；selector ` 0 `；EOL ` RVA 0x341DFD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036793

```text
(config)# do-exec show processes memory sorted <cr>
```

Handler ` RVA 0xE085350 `；selector ` 0 `；EOL ` RVA 0x341DFA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030074

```text
(config)# do-exec show processes timercheck <cr>
```

Handler ` RVA 0xE0489C0 `；selector ` 0 `；EOL ` RVA 0x341DEE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027753

```text
(config)# do-exec show profile <cr>
```

Handler ` RVA 0xD7AEFD0 `；selector ` 0 `；EOL ` RVA 0x34178530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027626

```text
(config)# do-exec show protocols <cr>
```

Handler ` RVA 0xDFEAD70 `；selector ` 0 `；EOL ` RVA 0x3423C118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1cd75225e0ca61d](../../evidence/conditions-sets-081.md#c-d1cd75225e0ca61d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060715

```text
(config)# do-exec show protocols <interface> <cr>
```

Handler ` RVA 0xDFEAD70 `；selector ` 0 `；EOL ` RVA 0x3423C118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8ae0690b50125781](../../evidence/conditions-sets-054.md#c-8ae0690b50125781) · [缺口 G-d51bee00845a0def](../../evidence/gaps-sets-007.md#g-d51bee00845a0def) · [参数 P-45ca6741250fa5c1](../../evidence/parameters-sets-006.md#p-45ca6741250fa5c1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061008

```text
(config)# do-exec show protocols phdf <?fpm_protocol_action@55558935bdc0> <cr>
```

Handler ` RVA 0xD2DFED0 `；selector ` 0 `；EOL ` RVA 0x33E07E00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d1cd75225e0ca61d](../../evidence/conditions-sets-081.md#c-d1cd75225e0ca61d) · [缺口 G-94cb69df9dc5cdf5](../../evidence/gaps-sets-005.md#g-94cb69df9dc5cdf5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030454

```text
(config)# do-exec show qbm client <cr>
```

Handler ` RVA 0xFF96040 `；selector ` 0 `；EOL ` RVA 0x34942438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030510

```text
(config)# do-exec show qbm pool <cr>
```

Handler ` RVA 0xFF96600 `；selector ` 0 `；EOL ` RVA 0x34942748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036624

```text
(config)# do-exec show qfp drops thresholds <cr>
```

Handler ` RVA 0x1595C690 `；selector ` 0 `；EOL ` RVA 0x35DC95C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036574

```text
(config)# do-exec show qfp utilization monitor <cr>
```

Handler ` RVA 0x1595C620 `；selector ` 0 `；EOL ` RVA 0x35DC92F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027801

```text
(config)# do-exec show qllc <cr>
```

Handler ` RVA 0x11CBDCB0 `；selector ` 0 `；EOL ` RVA 0x356C1070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64c425b4cea208ea](../../evidence/conditions-sets-039.md#c-64c425b4cea208ea) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060752

```text
(config)# do-exec show qllc <interface> <cr>
```

Handler ` RVA 0x11CBDCB0 `；selector ` 0 `；EOL ` RVA 0x356C1070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c1e17704ccda63e4](../../evidence/conditions-sets-075.md#c-c1e17704ccda63e4) · [缺口 G-6037e35549f8e352](../../evidence/gaps-sets-004.md#g-6037e35549f8e352) · [参数 P-3f2137cd0af843fa](../../evidence/parameters-sets-005.md#p-3f2137cd0af843fa) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038397

```text
(config)# do-exec show qos adaptive db <cr>
```

Handler ` RVA 0x127CCFD0 `；selector ` 0 `；EOL ` RVA 0x358D01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038464

```text
(config)# do-exec show qos adaptive multipoint <cr>
```

Handler ` RVA 0x127CCF40 `；selector ` 0 `；EOL ` RVA 0x358CFF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66766805ceb0420c](../../evidence/conditions-sets-040.md#c-66766805ceb0420c) · [状态效果 S-1e116bbd1f20c35f](../../evidence/state_effects-sets-007.md#s-1e116bbd1f20c35f)

### path-061489

```text
(config)# do-exec show qos adaptive multipoint <interface> <cr>
```

Handler ` RVA 0x127CCF40 `；selector ` 0 `；EOL ` RVA 0x358CFF08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2842e0eb3ef9c42d](../../evidence/conditions-sets-016.md#c-2842e0eb3ef9c42d) · [缺口 G-168eecb9cb5c6613](../../evidence/gaps-sets-001.md#g-168eecb9cb5c6613) · [参数 P-07748da7d586df9a](../../evidence/parameters-sets-001.md#p-07748da7d586df9a) · [状态效果 S-1e116bbd1f20c35f](../../evidence/state_effects-sets-007.md#s-1e116bbd1f20c35f)

### path-031254

```text
(config)# do-exec show qos event <cr>
```

Handler ` RVA 0x13FB7E50 `；selector ` 0 `；EOL ` RVA 0x35CE0FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031351

```text
(config)# do-exec show qos trace <cr>
```

Handler ` RVA 0x13FB8240 `；selector ` 0 `；EOL ` RVA 0x35CE1FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038529

```text
(config)# do-exec show qos trace error <cr>
```

Handler ` RVA 0x13FB81C0 `；selector ` 0 `；EOL ` RVA 0x35CE1D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038430

```text
(config)# do-exec show qos trace event <cr>
```

Handler ` RVA 0x13FB80D0 `；selector ` 0 `；EOL ` RVA 0x35CE17E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038478

```text
(config)# do-exec show qos trace warning <cr>
```

Handler ` RVA 0x13FB8140 `；selector ` 0 `；EOL ` RVA 0x35CE1A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042219

```text
(config)# do-exec show radius server-group all <cr>
```

Handler ` RVA 0xFFDBDE0 `；selector ` 0 `；EOL ` RVA 0x3494E698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2b5478c60b6eb524](../../evidence/state_effects-sets-010.md#s-2b5478c60b6eb524)

### path-033005

```text
(config)# do-exec show radius statistics <cr>
```

Handler ` RVA 0xFFDA670 `；selector ` 0 `；EOL ` RVA 0x3494E3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042220

```text
(config)# do-exec show radius table attributes <cr>
```

Handler ` RVA 0x10038220 `；selector ` 1 `；EOL ` RVA 0x34A263E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039231

```text
(config)# do-exec show radius-proxy client <address> <cr>
```

Handler ` RVA 0x11CE8890 `；selector ` 0 `；EOL ` RVA 0x356C6F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of client。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-06758b1faa69743d](../../evidence/parameters-sets-001.md#p-06758b1faa69743d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048245

```text
(config)# do-exec show radius-proxy session id <number:1..4294967295> <cr>
```

Handler ` RVA 0x11CE8EA0 `；selector ` 0 `；EOL ` RVA 0x356C7368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RP ID of session。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-dabd2c907aaaeecf](../../evidence/parameters-sets-016.md#p-dabd2c907aaaeecf) · [状态效果 S-fbb1568caaca1d7a](../../evidence/state_effects-sets-053.md#s-fbb1568caaca1d7a)

### path-031600

```text
(config)# do-exec show radius-proxy statistics <cr>
```

Handler ` RVA 0x11CE92C0 `；selector ` 0 `；EOL ` RVA 0x356C7738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032482

```text
(config)# do-exec show rbscp state <cr>
```

Handler ` RVA 0xFBC94F0 `；selector ` 0 `；EOL ` RVA 0x34840320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bf98c086abec49cc](../../evidence/conditions-sets-074.md#c-bf98c086abec49cc) · [状态效果 S-09e8490c9072ecec](../../evidence/state_effects-sets-002.md#s-09e8490c9072ecec)

### path-061068

```text
(config)# do-exec show rbscp state <interface> <cr>
```

Handler ` RVA 0xFBC94F0 `；selector ` 0 `；EOL ` RVA 0x34840320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b176266e655d22d4](../../evidence/conditions-sets-069.md#c-b176266e655d22d4) · [缺口 G-d0df979e6f024ece](../../evidence/gaps-sets-007.md#g-d0df979e6f024ece) · [参数 P-065037eac5db024d](../../evidence/parameters-sets-001.md#p-065037eac5db024d) · [状态效果 S-09e8490c9072ecec](../../evidence/state_effects-sets-002.md#s-09e8490c9072ecec)

### path-031544

```text
(config)# do-exec show redirect group <cr>
```

Handler ` RVA 0x11AA26F0 `；selector ` 3 `；EOL ` RVA 0x355E14B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031627

```text
(config)# do-exec show redirect translations <cr>
```

Handler ` RVA 0x11AA26F0 `；selector ` 7 `；EOL ` RVA 0x355E1868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa8e750fd86d79ba](../../evidence/conditions-sets-097.md#c-fa8e750fd86d79ba) · [状态效果 S-f1d74284c63a33de](../../evidence/state_effects-sets-051.md#s-f1d74284c63a33de)

### path-027393

```text
(config)# do-exec show redundancy <cr>
```

Handler ` RVA 0xDB583B0 `；selector ` 0 `；EOL ` RVA 0x33FD6160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-edcfd5914f2fe30b](../../evidence/conditions-sets-092.md#c-edcfd5914f2fe30b) · [状态效果 S-1582d6382d8a816a](../../evidence/state_effects-sets-005.md#s-1582d6382d8a816a)

### path-037374

```text
(config)# do-exec show redundancy application group <cr>
```

Handler ` RVA 0xCC193A0 `；selector ` 0 `；EOL ` RVA 0x33C1F348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-2af5ac60130f3624](../../evidence/state_effects-sets-010.md#s-2af5ac60130f3624)

### path-030355

```text
(config)# do-exec show redundancy clients <cr>
```

Handler ` RVA 0xDB584B0 `；selector ` 0 `；EOL ` RVA 0x33FD6630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-25c3f9b854800240](../../evidence/state_effects-sets-008.md#s-25c3f9b854800240)

### path-061367

```text
(config)# do-exec show redundancy clients domain <?option@55558952a4c8> <cr>
```

Handler ` RVA 0xDB584B0 `；selector ` 0 `；EOL ` RVA 0x33FD6630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7426770e002ec02e](../../evidence/conditions-sets-045.md#c-7426770e002ec02e) · [缺口 G-877a4a63481babde](../../evidence/gaps-sets-005.md#g-877a4a63481babde) · [状态效果 S-0f949fcdd2f3faeb](../../evidence/state_effects-sets-004.md#s-0f949fcdd2f3faeb)

### path-037332

```text
(config)# do-exec show redundancy cloud provider <cr>
```

Handler ` RVA 0x1441BDA0 `；selector ` 0 `；EOL ` RVA 0x35D61218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-b39790cd55053280](../../evidence/state_effects-sets-038.md#s-b39790cd55053280)

### path-060898

```text
(config)# do-exec show redundancy domain <?option@55558952a0f8> <cr>
```

Handler ` RVA 0xDB583B0 `；selector ` 0 `；EOL ` RVA 0x33FD6160 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-be51afc06337b071](../../evidence/conditions-sets-073.md#c-be51afc06337b071) · [缺口 G-11b331c9c4a9f6d7](../../evidence/gaps-sets-001.md#g-11b331c9c4a9f6d7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037071

```text
(config)# do-exec show redundancy history monitor <cr>
```

Handler ` RVA 0x127EBDA0 `；selector ` 0 `；EOL ` RVA 0x358D4828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030388

```text
(config)# do-exec show redundancy idb-sync-history <cr>
```

Handler ` RVA 0xDB584B0 `；selector ` 0 `；EOL ` RVA 0x33FD9DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-74f4e52b73e508ab](../../evidence/state_effects-sets-025.md#s-74f4e52b73e508ab)

### path-030594

```text
(config)# do-exec show redundancy interchassis <cr>
```

Handler ` RVA 0xC936BE0 `；selector ` 0 `；EOL ` RVA 0x33B309D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-40254caf86a75b46](../../evidence/state_effects-sets-014.md#s-40254caf86a75b46)

### path-030541

```text
(config)# do-exec show redundancy rii <cr>
```

Handler ` RVA 0xCC18EE0 `；selector ` 0 `；EOL ` RVA 0x33C1EB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037142

```text
(config)# do-exec show redundancy rii <number:1..65535> <cr>
```

Handler ` RVA 0xCC18F30 `；selector ` 0 `；EOL ` RVA 0x33C1EB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RII id。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [参数 P-2d0fad45d62d9dbd](../../evidence/parameters-sets-004.md#p-2d0fad45d62d9dbd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037125

```text
(config)# do-exec show redundancy switchover history <cr>
```

Handler ` RVA 0xDB3B5C0 `；selector ` 0 `；EOL ` RVA 0x33FCFB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-f77c05d3e6d5cf26](../../evidence/state_effects-sets-052.md#s-f77c05d3e6d5cf26)

### path-061967

```text
(config)# do-exec show redundancy switchover history domain <?option@555589523af0> <cr>
```

Handler ` RVA 0xDB3B5C0 `；selector ` 0 `；EOL ` RVA 0x33FCFB58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-839e26ec8468adbc](../../evidence/conditions-sets-051.md#c-839e26ec8468adbc) · [缺口 G-c72d11ec94fcbe13](../../evidence/gaps-sets-007.md#g-c72d11ec94fcbe13) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037214

```text
(config)# do-exec show redundancy trace main <cr>
```

Handler ` RVA 0xDB56250 `；selector ` 0 `；EOL ` RVA 0x33FDC188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-7f20ded1aa2a04ac](../../evidence/state_effects-sets-027.md#s-7f20ded1aa2a04ac)

### path-061972

```text
(config)# do-exec show redundancy trace main domain <?option@555589530120> <cr>
```

Handler ` RVA 0xDB56250 `；selector ` 0 `；EOL ` RVA 0x33FDC188 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-862a5a8ed0197dd4](../../evidence/conditions-sets-052.md#c-862a5a8ed0197dd4) · [缺口 G-e06a124f9cb50dd6](../../evidence/gaps-sets-008.md#g-e06a124f9cb50dd6) · [状态效果 S-cac9325b776d5443](../../evidence/state_effects-sets-043.md#s-cac9325b776d5443)

### path-027625

```text
(config)# do-exec show refuse-message <cr>
```

Handler ` RVA 0xCE36CF0 `；selector ` 0 `；EOL ` RVA 0x33CF5EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027750

```text
(config)# do-exec show region <cr>
```

Handler ` RVA 0xE046370 `；selector ` 0 `；EOL ` RVA 0x34175668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061172

```text
(config)# do-exec show region address <?general_pointer_number_action@5555896c9640> <cr>
```

Handler ` RVA 0xE046E90 `；selector ` 0 `；EOL ` RVA 0x341756A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-e31c3abe819ce33b](../../evidence/gaps-sets-008.md#g-e31c3abe819ce33b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027759

```text
(config)# do-exec show registry <cr>
```

Handler ` RVA 0xE053860 `；selector ` 0 `；EOL ` RVA 0x3417BC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4525ec4e185f3f19](../../evidence/conditions-sets-027.md#c-4525ec4e185f3f19) · [状态效果 S-55285a46fb39275b](../../evidence/state_effects-sets-018.md#s-55285a46fb39275b)

### path-033474

```text
(config)# do-exec show registry calls <cr>
```

Handler ` RVA 0xE053C40 `；selector ` 0 `；EOL ` RVA 0x3417C340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062458

```text
(config)# do-exec show registry calls <string> detail fn <?general_pointer_number_action@5555896d0468> <cr>
```

Handler ` RVA 0xE053C40 `；selector ` 0 `；EOL ` RVA 0x3417C340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of registry to examine。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-c5f9e3d37dfc0dd2](../../evidence/gaps-sets-007.md#g-c5f9e3d37dfc0dd2) · [参数 P-e9711b67b439c192](../../evidence/parameters-sets-017.md#p-e9711b67b439c192) · [状态效果 S-b5cb82f57f418d93](../../evidence/state_effects-sets-038.md#s-b5cb82f57f418d93)

### path-026832

```text
(config)# do-exec show reload <cr>
```

Handler ` RVA 0xE003920 `；selector ` 0 `；EOL ` RVA 0x341630A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029056

```text
(config)# do-exec show reload history <cr>
```

Handler ` RVA 0xE003A10 `；selector ` 0 `；EOL ` RVA 0x34163078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033915

```text
(config)# do-exec show remote-management status <cr>
```

Handler ` RVA 0x15696D40 `；selector ` 1 `；EOL ` RVA 0x35D77D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029391

```text
(config)# do-exec show resource database <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 2 `；EOL ` RVA 0x33ECAC50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035764

```text
(config)# do-exec show resource monitor all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 6 `；EOL ` RVA 0x33ECAEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b68742e66895ffbd](../../evidence/state_effects-sets-039.md#s-b68742e66895ffbd)

### path-057160

```text
(config)# do-exec show resource notification owner all user all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 4 `；EOL ` RVA 0x33ECA780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-67ee9646f6dd9e91](../../evidence/state_effects-sets-022.md#s-67ee9646f6dd9e91)

### path-052905

```text
(config)# do-exec show resource owner all user-type all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 0 `；EOL ` RVA 0x33EC5E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2d1b10249624b43d](../../evidence/state_effects-sets-010.md#s-2d1b10249624b43d)

### path-035655

```text
(config)# do-exec show resource policy all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 5 `；EOL ` RVA 0x33ECB120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c7d61e448384990a](../../evidence/state_effects-sets-042.md#s-c7d61e448384990a)

### path-045210

```text
(config)# do-exec show resource relationship user-type all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 1 `；EOL ` RVA 0x33ECA9E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b3055c2ca3f68484](../../evidence/state_effects-sets-038.md#s-b3055c2ca3f68484)

### path-035669

```text
(config)# do-exec show resource user-type all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 3 `；EOL ` RVA 0x33ECA518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c5d68f8579b839a5](../../evidence/state_effects-sets-042.md#s-c5d68f8579b839a5)

### path-027758

```text
(config)# do-exec show resource-group <cr>
```

Handler ` RVA 0xE07E6B0 `；selector ` 0 `；EOL ` RVA 0x341D2E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-73d9a4158e9caff1](../../evidence/conditions-sets-045.md#c-73d9a4158e9caff1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033486

```text
(config)# do-exec show resource-group memory <cr>
```

Handler ` RVA 0xE07E4F0 `；selector ` 0 `；EOL ` RVA 0x341D2B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042724

```text
(config)# do-exec show rfs issu endpoints <cr>
```

Handler ` RVA 0xDB4F1B0 `；selector ` 0 `；EOL ` RVA 0x33FD4F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027517

```text
(config)# do-exec show rhosts <cr>
```

Handler ` RVA 0xD000AB0 `；selector ` 0 `；EOL ` RVA 0x33D7B298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032352

```text
(config)# do-exec show rib application <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 3 `；EOL ` RVA 0x34007B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc656dac66f7b24a](../../evidence/conditions-sets-073.md#c-bc656dac66f7b24a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032317

```text
(config)# do-exec show rib client <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 0 `；EOL ` RVA 0x340075C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032351

```text
(config)# do-exec show rib gr <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 4 `；EOL ` RVA 0x340078A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a544e22af09ab98](../../evidence/conditions-sets-004.md#c-0a544e22af09ab98) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032410

```text
(config)# do-exec show rib ut <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 5 `；EOL ` RVA 0x34007EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcbfaca7f6543416](../../evidence/conditions-sets-098.md#c-fcbfaca7f6543416) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027142

```text
(config)# do-exec show rif <cr>
```

Handler ` RVA 0x12407300 `；selector ` 0 `；EOL ` RVA 0x35850320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d02a98cc9ab96ed1](../../evidence/conditions-sets-080.md#c-d02a98cc9ab96ed1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027735

```text
(config)# do-exec show rmon <cr>
```

Handler ` RVA 0xC4EE610 `；selector ` 0 `；EOL ` RVA 0x33AAC218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027283

```text
(config)# do-exec show romvar <cr>
```

Handler ` RVA 0xD5569E0 `；selector ` 0 `；EOL ` RVA 0x33E81B68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bde6284139aff4e6](../../evidence/conditions-sets-073.md#c-bde6284139aff4e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027631

```text
(config)# do-exec show route-map <cr>
```

Handler ` RVA 0xE2347F0 `；selector ` 0 `；EOL ` RVA 0x34257DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b97c00fac0fb17a6](../../evidence/conditions-sets-072.md#c-b97c00fac0fb17a6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031950

```text
(config)# do-exec show route-map all <cr>
```

Handler ` RVA 0xE234D20 `；selector ` 0 `；EOL ` RVA 0x3423C418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032035

```text
(config)# do-exec show route-map dynamic <cr>
```

Handler ` RVA 0xE234B40 `；selector ` 0 `；EOL ` RVA 0x3423CA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4ae6c0c05a47de02](../../evidence/conditions-sets-029.md#c-4ae6c0c05a47de02) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040307

```text
(config)# do-exec show route-map dynamic application <cr>
```

Handler ` RVA 0xE202550 `；selector ` 0 `；EOL ` RVA 0x3423C768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032015

```text
(config)# do-exec show route-map ipc <cr>
```

Handler ` RVA 0x10C71530 `；selector ` 0 `；EOL ` RVA 0x34CF1368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027624

```text
(config)# do-exec show route-tag <cr>
```

Handler ` RVA 0xE22F780 `；selector ` 0 `；EOL ` RVA 0x3423CE98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027524

```text
(config)# do-exec show rsh-disable-commands <cr>
```

Handler ` RVA 0xD000BD0 `；selector ` 0 `；EOL ` RVA 0x33D7B540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032810

```text
(config)# do-exec show rudpv1 failures <cr>
```

Handler ` RVA 0x1617CB20 `；selector ` 2 `；EOL ` RVA 0x35F06620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032824

```text
(config)# do-exec show rudpv1 parameters <cr>
```

Handler ` RVA 0x1617CB20 `；selector ` 3 `；EOL ` RVA 0x35F068C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032793

```text
(config)# do-exec show rudpv1 statistics <cr>
```

Handler ` RVA 0x1617CB20 `；selector ` 1 `；EOL ` RVA 0x35F06378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027162

```text
(config)# do-exec show running-config <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 5 `；EOL ` RVA 0x340B15F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a06168f59dfec7d8](../../evidence/conditions-sets-062.md#c-a06168f59dfec7d8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060574

```text
(config)# do-exec show running-config <interface> <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 5 `；EOL ` RVA 0x340B15F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6010286fcb35c99c](../../evidence/conditions-sets-037.md#c-6010286fcb35c99c) · [缺口 G-62d5810181220d7d](../../evidence/gaps-sets-004.md#g-62d5810181220d7d) · [参数 P-c3d1a312ae8c06e4](../../evidence/parameters-sets-015.md#p-c3d1a312ae8c06e4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030470

```text
(config)# do-exec show running-config aaa <cr>
```

Handler ` RVA 0xDD6BB00 `；selector ` 0 `；EOL ` RVA 0x340449B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060836

```text
(config)# do-exec show running-config bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xBF85F50 `；selector ` 0 `；EOL ` RVA 0x3395BED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain id。

[条件 C-2c0ca54c27c1b26c](../../evidence/conditions-sets-017.md#c-2c0ca54c27c1b26c) · [缺口 G-961bbedf58310440](../../evidence/gaps-sets-005.md#g-961bbedf58310440) · [参数 P-2cec3dd380056676](../../evidence/parameters-sets-004.md#p-2cec3dd380056676) · [状态效果 S-7c2674eb05998c5b](../../evidence/state_effects-sets-026.md#s-7c2674eb05998c5b)

### path-045219

```text
(config)# do-exec show running-config bridge-domain parameterized vlan <cr>
```

Handler ` RVA 0xBF85F50 `；selector ` 0 `；EOL ` RVA 0x3395BED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-038eb9b68d69c22a](../../evidence/state_effects-sets-001.md#s-038eb9b68d69c22a)

### path-029811

```text
(config)# do-exec show running-config class-map <cr>
```

Handler ` RVA 0xD893B70 `；selector ` 0 `；EOL ` RVA 0x33F1F410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88a189be23da6a8c](../../evidence/conditions-sets-053.md#c-88a189be23da6a8c) · [状态效果 S-20835585392167e7](../../evidence/state_effects-sets-007.md#s-20835585392167e7)

### path-060835

```text
(config)# do-exec show running-config controller <?controller_action@55558994a5f8> <cr>
```

Handler ` RVA 0xECFF030 `；selector ` 0 `；EOL ` RVA 0x343F6620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bbec45826c1b9be9](../../evidence/conditions-sets-073.md#c-bbec45826c1b9be9) · [缺口 G-cee7fc6bc73f5631](../../evidence/gaps-sets-007.md#g-cee7fc6bc73f5631) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030240

```text
(config)# do-exec show running-config cts <cr>
```

Handler ` RVA 0x1304F6C0 `；selector ` 0 `；EOL ` RVA 0x35A284E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045767

```text
(config)# do-exec show running-config eap method profiles <cr>
```

Handler ` RVA 0xCB3C8F0 `；selector ` 5 `；EOL ` RVA 0x33BC7A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036265

```text
(config)# do-exec show running-config eap profiles <cr>
```

Handler ` RVA 0xCB3C8F0 `；selector ` 1 `；EOL ` RVA 0x33BC7710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036719

```text
(config)# do-exec show running-config ethernet cfm <cr>
```

Handler ` RVA 0xBDD5760 `；selector ` 0 `；EOL ` RVA 0x338F5008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-90b20cd21c769fd5](../../evidence/conditions-sets-056.md#c-90b20cd21c769fd5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061350

```text
(config)# do-exec show running-config ethernet cfm global ais lck <cr>
```

Handler ` RVA 0xBDD5760 `；selector ` 0 `；EOL ` RVA 0x338F5008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a09fe5db8b050e57](../../evidence/conditions-sets-062.md#c-a09fe5db8b050e57) · [缺口 G-d55826c6ca9deb96](../../evidence/gaps-sets-007.md#g-d55826c6ca9deb96) · [状态效果 S-a4a0927f933418ac](../../evidence/state_effects-sets-035.md#s-a4a0927f933418ac)

### path-061287

```text
(config)# do-exec show running-config flow exporter <?option@555588f51338> <cr>
```

Handler ` RVA 0xC1E9D20 `；selector ` 0 `；EOL ` RVA 0x339FD378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0368f7d329e6a10f](../../evidence/conditions-sets-002.md#c-0368f7d329e6a10f) · [缺口 G-620e66bbd1cff5ba](../../evidence/gaps-sets-004.md#g-620e66bbd1cff5ba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035719

```text
(config)# do-exec show running-config flow exporter <cr>
```

Handler ` RVA 0xC1E9D20 `；selector ` 0 `；EOL ` RVA 0x339FD378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e6e1437737bfb457](../../evidence/conditions-sets-089.md#c-e6e1437737bfb457) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035993

```text
(config)# do-exec show running-config flow monitor <cr>
```

Handler ` RVA 0xC1F8920 `；selector ` 0 `；EOL ` RVA 0x33A05C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-62751fa88fa1d018](../../evidence/conditions-sets-038.md#c-62751fa88fa1d018) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035920

```text
(config)# do-exec show running-config flow record <cr>
```

Handler ` RVA 0xC1D91C0 `；selector ` 0 `；EOL ` RVA 0x339F8F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-59218ebc35d895a2](../../evidence/conditions-sets-035.md#c-59218ebc35d895a2) · [状态效果 S-af0c04d2fa129720](../../evidence/state_effects-sets-037.md#s-af0c04d2fa129720)

### path-060847

```text
(config)# do-exec show running-config flow record <cr>
```

Handler ` RVA 0xC1D91C0 `；selector ` 0 `；EOL ` RVA 0x339F8F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e364fe548f4f183d](../../evidence/conditions-sets-088.md#c-e364fe548f4f183d) · [缺口 G-ab5213be77b659ee](../../evidence/gaps-sets-006.md#g-ab5213be77b659ee) · [状态效果 S-6fdda0fb55ac4ad4](../../evidence/state_effects-sets-024.md#s-6fdda0fb55ac4ad4)

### path-036201

```text
(config)# do-exec show running-config identity policy <cr>
```

Handler ` RVA 0xCB51AE0 `；selector ` 0 `；EOL ` RVA 0x33BE23F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-453ca184710fab72](../../evidence/state_effects-sets-015.md#s-453ca184710fab72)

### path-045762

```text
(config)# do-exec show running-config ip dhcp pool <cr>
```

Handler ` RVA 0xD29EF30 `；selector ` 0 `；EOL ` RVA 0x33DE34D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045818

```text
(config)# do-exec show running-config ipv6 dhcp pool <cr>
```

Handler ` RVA 0x121C95B0 `；selector ` 0 `；EOL ` RVA 0x357C7800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029807

```text
(config)# do-exec show running-config map-class <cr>
```

Handler ` RVA 0xDCFE700 `；selector ` 0 `；EOL ` RVA 0x3403FCD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-37306ac52a11d300](../../evidence/conditions-sets-021.md#c-37306ac52a11d300) · [状态效果 S-587500ff72170b91](../../evidence/state_effects-sets-019.md#s-587500ff72170b91)

### path-030205

```text
(config)# do-exec show running-config mdns-sd <cr>
```

Handler ` RVA 0x1434F450 `；selector ` 0 `；EOL ` RVA 0x35D0F400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a716e7993073a3fc](../../evidence/conditions-sets-064.md#c-a716e7993073a3fc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029089

```text
(config)# do-exec show running-config nat <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 10 `；EOL ` RVA 0x340B0F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-798ed45be4f827f7](../../evidence/conditions-sets-047.md#c-798ed45be4f827f7) · [状态效果 S-07a1b4e70431e94f](../../evidence/state_effects-sets-002.md#s-07a1b4e70431e94f)

### path-028846

```text
(config)# do-exec show running-config nve <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 9 `；EOL ` RVA 0x340B0C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029502

```text
(config)# do-exec show running-config service-group <cr>
```

Handler ` RVA 0xCC57A30 `；selector ` 0 `；EOL ` RVA 0x33C26D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060828

```text
(config)# do-exec show running-config service-group <number:dynamic> <cr>
```

Handler ` RVA 0xCC57A30 `；selector ` 0 `；EOL ` RVA 0x33C26D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Service Group ID Number。

[条件 C-cc0de4032e428b9b](../../evidence/conditions-sets-079.md#c-cc0de4032e428b9b) · [缺口 G-932784f131787fae](../../evidence/gaps-sets-005.md#g-932784f131787fae) · [参数 P-9b9572b711265a3f](../../evidence/parameters-sets-012.md#p-9b9572b711265a3f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029860

```text
(config)# do-exec show running-config switchport <cr>
```

Handler ` RVA 0x15DC91D0 `；selector ` 0 `；EOL ` RVA 0x35E26980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [状态效果 S-ab8a72d315a93686](../../evidence/state_effects-sets-036.md#s-ab8a72d315a93686)

### path-029864

```text
(config)# do-exec show running-config vc-class <cr>
```

Handler ` RVA 0xDCFE700 `；selector ` 0 `；EOL ` RVA 0x34040258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-62eba2c3dc8660db](../../evidence/conditions-sets-038.md#c-62eba2c3dc8660db) · [状态效果 S-a49852bccd70cb86](../../evidence/state_effects-sets-035.md#s-a49852bccd70cb86)

### path-029861

```text
(config)# do-exec show running-config vlan <cr>
```

Handler ` RVA 0x15CAA3F0 `；selector ` 0 `；EOL ` RVA 0x35E03398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-681b11b282788a60](../../evidence/conditions-sets-040.md#c-681b11b282788a60) · [状态效果 S-665d29455b7b50c5](../../evidence/state_effects-sets-022.md#s-665d29455b7b50c5)

### path-060613

```text
(config)# do-exec show running-config vnet <cr>
```

Handler ` RVA 0x1246E040 `；selector ` 8 `；EOL ` RVA 0x35875658 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-f60f7b6dd3d964bb](../../evidence/gaps-sets-008.md#g-f60f7b6dd3d964bb) · [状态效果 S-384c3f2ceb95ef56](../../evidence/state_effects-sets-012.md#s-384c3f2ceb95ef56)

### path-028791

```text
(config)# do-exec show running-config vrf <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 8 `；EOL ` RVA 0x340B0928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060902

```text
(config)# do-exec show running-config yang aaa <cr>
```

Handler ` RVA 0xDD6BB00 `；selector ` 0 `；EOL ` RVA 0x340449B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-060851

```text
(config)# do-exec show running-config yang class-map <cr>
```

Handler ` RVA 0xD893B70 `；selector ` 0 `；EOL ` RVA 0x33F1F410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-88a189be23da6a8c](../../evidence/conditions-sets-053.md#c-88a189be23da6a8c) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-cf16741b1790403d](../../evidence/state_effects-sets-044.md#s-cf16741b1790403d)

### path-060883

```text
(config)# do-exec show running-config yang cts <cr>
```

Handler ` RVA 0x1304F6C0 `；selector ` 0 `；EOL ` RVA 0x35A284E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-061915

```text
(config)# do-exec show running-config yang eap method profiles <cr>
```

Handler ` RVA 0xCB3C8F0 `；selector ` 5 `；EOL ` RVA 0x33BC7A88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-061327

```text
(config)# do-exec show running-config yang eap profiles <cr>
```

Handler ` RVA 0xCB3C8F0 `；selector ` 1 `；EOL ` RVA 0x33BC7710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-061304

```text
(config)# do-exec show running-config yang flow monitor <cr>
```

Handler ` RVA 0xC1F8920 `；selector ` 0 `；EOL ` RVA 0x33A05C58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-62751fa88fa1d018](../../evidence/conditions-sets-038.md#c-62751fa88fa1d018) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-061321

```text
(config)# do-exec show running-config yang identity policy <cr>
```

Handler ` RVA 0xCB51AE0 `；selector ` 0 `；EOL ` RVA 0x33BE23F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-5f1bb6c6d6cf62e0](../../evidence/state_effects-sets-020.md#s-5f1bb6c6d6cf62e0)

### path-061914

```text
(config)# do-exec show running-config yang ip dhcp pool <cr>
```

Handler ` RVA 0xD29EF30 `；selector ` 0 `；EOL ` RVA 0x33DE34D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-061917

```text
(config)# do-exec show running-config yang ipv6 dhcp pool <cr>
```

Handler ` RVA 0x121C95B0 `；selector ` 0 `；EOL ` RVA 0x357C7800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-060850

```text
(config)# do-exec show running-config yang map-class <cr>
```

Handler ` RVA 0xDCFE700 `；selector ` 0 `；EOL ` RVA 0x3403FCD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-37306ac52a11d300](../../evidence/conditions-sets-021.md#c-37306ac52a11d300) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-9535f15113f426c9](../../evidence/state_effects-sets-032.md#s-9535f15113f426c9)

### path-060879

```text
(config)# do-exec show running-config yang mdns-sd <cr>
```

Handler ` RVA 0x1434F450 `；selector ` 0 `；EOL ` RVA 0x35D0F400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a716e7993073a3fc](../../evidence/conditions-sets-064.md#c-a716e7993073a3fc) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-060816

```text
(config)# do-exec show running-config yang nat <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 10 `；EOL ` RVA 0x340B0F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-798ed45be4f827f7](../../evidence/conditions-sets-047.md#c-798ed45be4f827f7) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-cd8ebc2ea2a58ae7](../../evidence/state_effects-sets-044.md#s-cd8ebc2ea2a58ae7)

### path-060802

```text
(config)# do-exec show running-config yang nve <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 9 `；EOL ` RVA 0x340B0C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-060854

```text
(config)# do-exec show running-config yang switchport <cr>
```

Handler ` RVA 0x15DC91D0 `；selector ` 0 `；EOL ` RVA 0x35E26980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6fdcff7f59c97e6a](../../evidence/conditions-sets-043.md#c-6fdcff7f59c97e6a) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-9ef58f97461156ed](../../evidence/state_effects-sets-034.md#s-9ef58f97461156ed)

### path-060856

```text
(config)# do-exec show running-config yang vc-class <cr>
```

Handler ` RVA 0xDCFE700 `；selector ` 0 `；EOL ` RVA 0x34040258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-62eba2c3dc8660db](../../evidence/conditions-sets-038.md#c-62eba2c3dc8660db) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-12141ee1e1f26418](../../evidence/state_effects-sets-004.md#s-12141ee1e1f26418)

### path-060855

```text
(config)# do-exec show running-config yang vlan <cr>
```

Handler ` RVA 0x15CAA3F0 `；selector ` 0 `；EOL ` RVA 0x35E03398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-681b11b282788a60](../../evidence/conditions-sets-040.md#c-681b11b282788a60) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-573e150165fcddcb](../../evidence/state_effects-sets-019.md#s-573e150165fcddcb)

### path-060797

```text
(config)# do-exec show running-config yang vrf <cr>
```

Handler ` RVA 0xDFE9DB0 `；selector ` 8 `；EOL ` RVA 0x340B0928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-cc3a6fa23be141f5](../../evidence/gaps-sets-007.md#g-cc3a6fa23be141f5) · [状态效果 S-1a604a7a96dd295e](../../evidence/state_effects-sets-006.md#s-1a604a7a96dd295e)

### path-027732

```text
(config)# do-exec show rwatch <cr>
```

Handler ` RVA 0xDC09810 `；selector ` 1 `；EOL ` RVA 0x3400CEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060675

```text
(config)# do-exec show sampler <?option@555588f3c1e0> <cr>
```

Handler ` RVA 0xC17E0A0 `；selector ` 0 `；EOL ` RVA 0x339E7EC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0fad9c4f0b35bf3e](../../evidence/conditions-sets-006.md#c-0fad9c4f0b35bf3e) · [缺口 G-872760272567e191](../../evidence/gaps-sets-005.md#g-872760272567e191) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027478

```text
(config)# do-exec show sampler <cr>
```

Handler ` RVA 0xC17E0A0 `；selector ` 0 `；EOL ` RVA 0x339E7EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0275a1dbe4cd682f](../../evidence/conditions-sets-001.md#c-0275a1dbe4cd682f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030820

```text
(config)# do-exec show sampler broker <cr>
```

Handler ` RVA 0xC227540 `；selector ` 0 `；EOL ` RVA 0x33A10C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033927

```text
(config)# do-exec show sasl all <cr>
```

Handler ` RVA 0x103D10B0 `；selector ` 5 `；EOL ` RVA 0x34B16E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033942

```text
(config)# do-exec show sasl context <cr>
```

Handler ` RVA 0x103D10B0 `；selector ` 1 `；EOL ` RVA 0x34B17990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033936

```text
(config)# do-exec show sasl mechanisms <cr>
```

Handler ` RVA 0x103D10B0 `；selector ` 2 `；EOL ` RVA 0x34B176E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043821

```text
(config)# do-exec show sasl profile <string> <cr>
```

Handler ` RVA 0x103D10B0 `；selector ` 3 `；EOL ` RVA 0x34B17458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile Name。

[条件 C-7d100d3209135e24](../../evidence/conditions-sets-048.md#c-7d100d3209135e24) · [参数 P-9774d5c395a63b2e](../../evidence/parameters-sets-012.md#p-9774d5c395a63b2e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043802

```text
(config)# do-exec show sasl profile all <cr>
```

Handler ` RVA 0x103D10B0 `；selector ` 4 `；EOL ` RVA 0x34B17158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030005

```text
(config)# do-exec show scalable-queue statistics <cr>
```

Handler ` RVA 0xE082060 `；selector ` 0 `；EOL ` RVA 0x341DCAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033874

```text
(config)# do-exec show sd-card summary <cr>
```

Handler ` RVA 0xE981420 `；selector ` 0 `；EOL ` RVA 0x3435DEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2b5f013d58a1c17f](../../evidence/conditions-sets-017.md#c-2b5f013d58a1c17f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027746

```text
(config)# do-exec show sdb <cr>
```

Handler ` RVA 0xDEC80B0 `；selector ` 0 `；EOL ` RVA 0x34092DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027789

```text
(config)# do-exec show sdllc <cr>
```

Handler ` RVA 0x113C14F0 `；selector ` 0 `；EOL ` RVA 0x354A7108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-713f6bad54270e10](../../evidence/conditions-sets-044.md#c-713f6bad54270e10) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060750

```text
(config)# do-exec show sdllc <interface> <cr>
```

Handler ` RVA 0x113C14F0 `；selector ` 0 `；EOL ` RVA 0x354A7108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0f580334e76a848a](../../evidence/conditions-sets-006.md#c-0f580334e76a848a) · [缺口 G-b11736620f678cac](../../evidence/gaps-sets-006.md#g-b11736620f678cac) · [参数 P-ad3a29a1bd221739](../../evidence/parameters-sets-013.md#p-ad3a29a1bd221739) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027802

```text
(config)# do-exec show self-diagnostics <cr>
```

Handler ` RVA 0x159C4890 `；selector ` 0 `；EOL ` RVA 0x35DD4070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6062a682846ff5f5](../../evidence/state_effects-sets-021.md#s-6062a682846ff5f5)

### path-029095

```text
(config)# do-exec show sensor-mgr db <cr>
```

Handler ` RVA 0xC739FE0 `；selector ` 0 `；EOL ` RVA 0x33ADA370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060679

```text
(config)# do-exec show service-group <number:dynamic> <cr>
```

Handler ` RVA 0xCC557D0 `；selector ` 0 `；EOL ` RVA 0x33C27B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Service Group ID Number。

[条件 C-d9667d94e5b15b8c](../../evidence/conditions-sets-084.md#c-d9667d94e5b15b8c) · [缺口 G-2ce13fbadc6b9a2e](../../evidence/gaps-sets-002.md#g-2ce13fbadc6b9a2e) · [参数 P-e80f78333efb772d](../../evidence/parameters-sets-017.md#p-e80f78333efb772d) · [状态效果 S-0ad97906e12f581c](../../evidence/state_effects-sets-003.md#s-0ad97906e12f581c)

### path-030872

```text
(config)# do-exec show service-group all <cr>
```

Handler ` RVA 0xCC557D0 `；selector ` 0 `；EOL ` RVA 0x33C27B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8ce1f4c765713933](../../evidence/state_effects-sets-030.md#s-8ce1f4c765713933)

### path-041084

```text
(config)# do-exec show service-overlay applications registered <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 2 `；EOL ` RVA 0x34BF56C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-341220d4656ebc0e](../../evidence/state_effects-sets-012.md#s-341220d4656ebc0e)

### path-062157

```text
(config)# do-exec show service-overlay interface <interface> applications registered <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 2 `；EOL ` RVA 0x34BF56C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a3aae2ec480951b](../../evidence/conditions-sets-047.md#c-7a3aae2ec480951b) · [缺口 G-5b28894655b203f2](../../evidence/gaps-sets-004.md#g-5b28894655b203f2) · [参数 P-f2cf258aee18c945](../../evidence/parameters-sets-018.md#p-f2cf258aee18c945) · [状态效果 S-341220d4656ebc0e](../../evidence/state_effects-sets-012.md#s-341220d4656ebc0e)

### path-061665

```text
(config)# do-exec show service-overlay interface <interface> internal <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 6 `；EOL ` RVA 0x34BF5C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a776673363fb43f2](../../evidence/conditions-sets-065.md#c-a776673363fb43f2) · [缺口 G-5b28894655b203f2](../../evidence/gaps-sets-004.md#g-5b28894655b203f2) · [参数 P-f2cf258aee18c945](../../evidence/parameters-sets-018.md#p-f2cf258aee18c945) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062155

```text
(config)# do-exec show service-overlay interface <interface> peer database <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 5 `；EOL ` RVA 0x34BF5380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-de9d5bd6f2f79582](../../evidence/conditions-sets-086.md#c-de9d5bd6f2f79582) · [缺口 G-5b28894655b203f2](../../evidence/gaps-sets-004.md#g-5b28894655b203f2) · [参数 P-f2cf258aee18c945](../../evidence/parameters-sets-018.md#p-f2cf258aee18c945) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061661

```text
(config)# do-exec show service-overlay interface <interface> stats <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 4 `；EOL ` RVA 0x34BF5F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a3aae2ec480951b](../../evidence/conditions-sets-047.md#c-7a3aae2ec480951b) · [缺口 G-5b28894655b203f2](../../evidence/gaps-sets-004.md#g-5b28894655b203f2) · [参数 P-f2cf258aee18c945](../../evidence/parameters-sets-018.md#p-f2cf258aee18c945) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061664

```text
(config)# do-exec show service-overlay interface <interface> summary <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 3 `；EOL ` RVA 0x34BF59C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7a3aae2ec480951b](../../evidence/conditions-sets-047.md#c-7a3aae2ec480951b) · [缺口 G-5b28894655b203f2](../../evidence/gaps-sets-004.md#g-5b28894655b203f2) · [参数 P-f2cf258aee18c945](../../evidence/parameters-sets-018.md#p-f2cf258aee18c945) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032437

```text
(config)# do-exec show service-overlay internal <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 6 `；EOL ` RVA 0x34BF5C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-601380eff665df62](../../evidence/conditions-sets-037.md#c-601380eff665df62) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032403

```text
(config)# do-exec show service-overlay stats <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 4 `；EOL ` RVA 0x34BF5F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032420

```text
(config)# do-exec show service-overlay summary <cr>
```

Handler ` RVA 0x108F4910 `；selector ` 3 `；EOL ` RVA 0x34BF59C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032620

```text
(config)# do-exec show service-routing capabilities-manager <cr>
```

Handler ` RVA 0x1045B580 `；selector ` 78 `；EOL ` RVA 0x34B340E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5375c862f01854d](../../evidence/conditions-sets-095.md#c-f5375c862f01854d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032570

```text
(config)# do-exec show service-routing database <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 9 `；EOL ` RVA 0x34B2C890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062689

```text
(config)# do-exec show service-routing database <number:0..65535> : <number:0..65535> : <number:0..4294967295> - <number:0..65535> - <number:0..65535> - <number:0..65535> - <hex-string> <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 9 `；EOL ` RVA 0x34B2C890 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` hexstring ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-96303930dd702cc2](../../evidence/conditions-sets-058.md#c-96303930dd702cc2) · [缺口 G-1fd00151a6d9ba69](../../evidence/gaps-sets-002.md#g-1fd00151a6d9ba69) · [参数 P-deeb97a4abd9f601](../../evidence/parameters-sets-017.md#p-deeb97a4abd9f601) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032559

```text
(config)# do-exec show service-routing parser <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 10 `；EOL ` RVA 0x34B2BE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-81b22d7a1cc05331](../../evidence/state_effects-sets-028.md#s-81b22d7a1cc05331)

### path-032577

```text
(config)# do-exec show service-routing plugins <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 11 `；EOL ` RVA 0x34B2C190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-354e75d64ea390cc](../../evidence/conditions-sets-021.md#c-354e75d64ea390cc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032571

```text
(config)# do-exec show service-routing registered <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 12 `；EOL ` RVA 0x34B361B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041401

```text
(config)# do-exec show service-routing registered detail <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 13 `；EOL ` RVA 0x34B36188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-29ed63a98d0f355b](../../evidence/state_effects-sets-009.md#s-29ed63a98d0f355b)

### path-032590

```text
(config)# do-exec show service-routing subscriptions <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 14 `；EOL ` RVA 0x34B36720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041433

```text
(config)# do-exec show service-routing subscriptions detail <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 15 `；EOL ` RVA 0x34B366F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-202ef8e30ecbc05a](../../evidence/state_effects-sets-007.md#s-202ef8e30ecbc05a)

### path-032555

```text
(config)# do-exec show service-routing tech-support <cr>
```

Handler ` RVA 0x104524E0 `；selector ` 16 `；EOL ` RVA 0x34B2C588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061706

```text
(config)# do-exec show service-routing xmcp clients <address> <cr>
```

Handler ` RVA 0x10472940 `；selector ` 51 `；EOL ` RVA 0x34B36D10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address of a single client to display。

[条件 C-e6c47e40a06ad5b6](../../evidence/conditions-sets-089.md#c-e6c47e40a06ad5b6) · [缺口 G-02d9486a6e08a932](../../evidence/gaps-sets-001.md#g-02d9486a6e08a932) · [参数 P-7c413fdef570f283](../../evidence/parameters-sets-010.md#p-7c413fdef570f283) · [状态效果 S-9f5c46ee9cf51c3e](../../evidence/state_effects-sets-034.md#s-9f5c46ee9cf51c3e)

### path-041605

```text
(config)# do-exec show service-routing xmcp clients <cr>
```

Handler ` RVA 0x10472940 `；selector ` 51 `；EOL ` RVA 0x34B36D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b572fcf6776186bc](../../evidence/conditions-sets-070.md#c-b572fcf6776186bc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041511

```text
(config)# do-exec show service-routing xmcp server <cr>
```

Handler ` RVA 0x10472940 `；selector ` 52 `；EOL ` RVA 0x34B37128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041556

```text
(config)# do-exec show service-routing xmcp timers <cr>
```

Handler ` RVA 0x10472940 `；selector ` 53 `；EOL ` RVA 0x34B373D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027739

```text
(config)# do-exec show service-template <cr>
```

Handler ` RVA 0xCB518F0 `；selector ` 0 `；EOL ` RVA 0x33BE33A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e89b5bc85da7a427](../../evidence/state_effects-sets-049.md#s-e89b5bc85da7a427)

### path-026767

```text
(config)# do-exec show sessions <cr>
```

Handler ` RVA 0xDE865C0 `；selector ` 0 `；EOL ` RVA 0x341881C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028184

```text
(config)# do-exec show shell data-path <cr>
```

Handler ` RVA 0xDF07800 `；selector ` 0 `；EOL ` RVA 0x340B8530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e117d478d5e7bdb7](../../evidence/conditions-sets-087.md#c-e117d478d5e7bdb7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028123

```text
(config)# do-exec show shell environment <cr>
```

Handler ` RVA 0xDF78B10 `；selector ` 0 `；EOL ` RVA 0x340B7FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e117d478d5e7bdb7](../../evidence/conditions-sets-087.md#c-e117d478d5e7bdb7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060523

```text
(config)# do-exec show shell functions <cr>
```

Handler ` RVA 0xDF78330 `；selector ` 0 `；EOL ` RVA 0x340B7C30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51931e6bdffa0870](../../evidence/conditions-sets-032.md#c-51931e6bdffa0870) · [缺口 G-03eea53f4f2b680a](../../evidence/gaps-sets-001.md#g-03eea53f4f2b680a) · [状态效果 S-803e2beab2fa706a](../../evidence/state_effects-sets-027.md#s-803e2beab2fa706a)

### path-034133

```text
(config)# do-exec show shell functions brief <cr>
```

Handler ` RVA 0xDF78330 `；selector ` 0 `；EOL ` RVA 0x340B7C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e117d478d5e7bdb7](../../evidence/conditions-sets-087.md#c-e117d478d5e7bdb7) · [状态效果 S-56549e5ebe3b3b26](../../evidence/state_effects-sets-019.md#s-56549e5ebe3b3b26)

### path-028188

```text
(config)# do-exec show shell triggers <cr>
```

Handler ` RVA 0xDF78B70 `；selector ` 0 `；EOL ` RVA 0x340B82B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e117d478d5e7bdb7](../../evidence/conditions-sets-087.md#c-e117d478d5e7bdb7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033154

```text
(config)# do-exec show shell-exec status <cr>
```

Handler ` RVA 0xEBB20D0 `；selector ` 0 `；EOL ` RVA 0x343D0CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027665

```text
(config)# do-exec show slip <cr>
```

Handler ` RVA 0xFF3FE50 `；selector ` 0 `；EOL ` RVA 0x34934938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031403

```text
(config)# do-exec show smds addresses <cr>
```

Handler ` RVA 0x10511DA0 `；selector ` 0 `；EOL ` RVA 0x34B4CCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55f44a455d60ee1c](../../evidence/conditions-sets-034.md#c-55f44a455d60ee1c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031423

```text
(config)# do-exec show smds map <cr>
```

Handler ` RVA 0x10511DA0 `；selector ` 1 `；EOL ` RVA 0x34B4CF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55f44a455d60ee1c](../../evidence/conditions-sets-034.md#c-55f44a455d60ee1c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031443

```text
(config)# do-exec show smds traffic <cr>
```

Handler ` RVA 0x10511DA0 `；selector ` 2 `；EOL ` RVA 0x34B4D218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55f44a455d60ee1c](../../evidence/conditions-sets-034.md#c-55f44a455d60ee1c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027638

```text
(config)# do-exec show smf <cr>
```

Handler ` RVA 0xF296DB0 `；selector ` 0 `；EOL ` RVA 0x345F1970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09f1ce833e22d7b4](../../evidence/conditions-sets-004.md#c-09f1ce833e22d7b4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060721

```text
(config)# do-exec show smf <interface> <cr>
```

Handler ` RVA 0xF296DB0 `；selector ` 0 `；EOL ` RVA 0x345F1970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-490bbf846765e11d](../../evidence/conditions-sets-029.md#c-490bbf846765e11d) · [缺口 G-972151c9f19a7d1d](../../evidence/gaps-sets-006.md#g-972151c9f19a7d1d) · [参数 P-8393274fddc91c2d](../../evidence/parameters-sets-010.md#p-8393274fddc91c2d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027677

```text
(config)# do-exec show sna <cr>
```

Handler ` RVA 0x114FAC00 `；selector ` 13 `；EOL ` RVA 0x35512918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027716

```text
(config)# do-exec show snapshot <cr>
```

Handler ` RVA 0x10518130 `；selector ` 0 `；EOL ` RVA 0x34B4FFA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19c0f4b863d795b8](../../evidence/conditions-sets-010.md#c-19c0f4b863d795b8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060738

```text
(config)# do-exec show snapshot <interface> <cr>
```

Handler ` RVA 0x10518130 `；selector ` 0 `；EOL ` RVA 0x34B4FFA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8fb74c90bf5eeb21](../../evidence/conditions-sets-056.md#c-8fb74c90bf5eeb21) · [缺口 G-432c19944dfba657](../../evidence/gaps-sets-003.md#g-432c19944dfba657) · [参数 P-0c674b720eab7819](../../evidence/parameters-sets-001.md#p-0c674b720eab7819) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027664

```text
(config)# do-exec show snmp <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 0 `；EOL ` RVA 0x33C3DB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cce5e913698621e](../../evidence/conditions-sets-048.md#c-7cce5e913698621e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032340

```text
(config)# do-exec show snmp chassis <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 4 `；EOL ` RVA 0x33C2D7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032360

```text
(config)# do-exec show snmp community <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 7 `；EOL ` RVA 0x33C2DA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032306

```text
(config)# do-exec show snmp contact <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 8 `；EOL ` RVA 0x33C2D290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032220

```text
(config)# do-exec show snmp context <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 3 `；EOL ` RVA 0x33C2C038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040763

```text
(config)# do-exec show snmp context mapping <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 21 `；EOL ` RVA 0x33C2C010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032189

```text
(config)# do-exec show snmp cpu-stats <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 24 `；EOL ` RVA 0x33C2BC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a092e525892be25b](../../evidence/conditions-sets-062.md#c-a092e525892be25b) · [状态效果 S-deaf40b9b9ca5900](../../evidence/state_effects-sets-047.md#s-deaf40b9b9ca5900)

### path-032216

```text
(config)# do-exec show snmp engineID <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 12 `；EOL ` RVA 0x33C2C508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032248

```text
(config)# do-exec show snmp group <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 11 `；EOL ` RVA 0x33C2CA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032289

```text
(config)# do-exec show snmp host <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 6 `；EOL ` RVA 0x33C2CFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032323

```text
(config)# do-exec show snmp location <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 9 `；EOL ` RVA 0x33C2D538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032256

```text
(config)# do-exec show snmp mib <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 1 `；EOL ` RVA 0x33C3F0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050000

```text
(config)# do-exec show snmp mib bulkstat transfer <cr>
```

Handler ` RVA 0xBC76F40 `；selector ` 2 `；EOL ` RVA 0x3388C798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055792

```text
(config)# do-exec show snmp mib bulkstat transfer <string> <cr>
```

Handler ` RVA 0xBC76F40 `；selector ` 1 `；EOL ` RVA 0x3388C770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show specific bulkstat transfer parameters。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-492468bed9f09700](../../evidence/parameters-sets-006.md#p-492468bed9f09700) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040825

```text
(config)# do-exec show snmp mib context <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 22 `；EOL ` RVA 0x33C3F0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050033

```text
(config)# do-exec show snmp mib ifmib ifindex <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 13 `；EOL ` RVA 0x33C3DF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19b337399e53c55b](../../evidence/conditions-sets-010.md#c-19b337399e53c55b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062142

```text
(config)# do-exec show snmp mib ifmib ifindex <interface> <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 13 `；EOL ` RVA 0x33C3DF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-af5b80b0ca437d25](../../evidence/conditions-sets-068.md#c-af5b80b0ca437d25) · [缺口 G-d101cd63a49d9383](../../evidence/gaps-sets-007.md#g-d101cd63a49d9383) · [参数 P-9f712c1bd09b1a8b](../../evidence/parameters-sets-012.md#p-9f712c1bd09b1a8b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055817

```text
(config)# do-exec show snmp mib ifmib ifindex free-list <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 14 `；EOL ` RVA 0x33C3E338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19b337399e53c55b](../../evidence/conditions-sets-010.md#c-19b337399e53c55b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049951

```text
(config)# do-exec show snmp mib ifmib traps <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 23 `；EOL ` RVA 0x33C3E610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049946

```text
(config)# do-exec show snmp mib nhrp status <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 9 `；EOL ` RVA 0x348E8B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-890a389bcba87aee](../../evidence/state_effects-sets-029.md#s-890a389bcba87aee)

### path-040870

```text
(config)# do-exec show snmp mib notification-log <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 15 `；EOL ` RVA 0x33C3EBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049945

```text
(config)# do-exec show snmp mib notification-log all <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 16 `；EOL ` RVA 0x33C3E910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049970

```text
(config)# do-exec show snmp mib notification-log default <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 17 `；EOL ` RVA 0x33C3EBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060727

```text
(config)# do-exec show snmp monitor response <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 27 `；EOL ` RVA 0x33C2DFD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-59729245f94eda5d](../../evidence/conditions-sets-035.md#c-59729245f94eda5d) · [缺口 G-eb3f1bdc27669571](../../evidence/gaps-sets-008.md#g-eb3f1bdc27669571) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032231

```text
(config)# do-exec show snmp notify <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 10 `；EOL ` RVA 0x33C2C7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032515

```text
(config)# do-exec show snmp pending <cr>
```

Handler ` RVA 0x10527260 `；selector ` 1 `；EOL ` RVA 0x34B528E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cce5e913698621e](../../evidence/conditions-sets-048.md#c-7cce5e913698621e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041334

```text
(config)# do-exec show snmp sa cache-stat <cr>
```

Handler ` RVA 0xC72E920 `；selector ` 0 `；EOL ` RVA 0x33AD4B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cce5e913698621e](../../evidence/conditions-sets-048.md#c-7cce5e913698621e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032519

```text
(config)# do-exec show snmp sessions <cr>
```

Handler ` RVA 0x10527260 `；selector ` 2 `；EOL ` RVA 0x34B52640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7cce5e913698621e](../../evidence/conditions-sets-048.md#c-7cce5e913698621e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032443

```text
(config)# do-exec show snmp slot-mapping <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 25 `；EOL ` RVA 0x33C2E868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9924486f2041ab40](../../evidence/conditions-sets-059.md#c-9924486f2041ab40) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041177

```text
(config)# do-exec show snmp stats hosts <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 26 `；EOL ` RVA 0x33C2E590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041145

```text
(config)# do-exec show snmp stats oid <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 18 `；EOL ` RVA 0x33C2E2E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032295

```text
(config)# do-exec show snmp user <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 5 `；EOL ` RVA 0x33C2CD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032376

```text
(config)# do-exec show snmp view <cr>
```

Handler ` RVA 0x104C4660 `；selector ` 2 `；EOL ` RVA 0x33C2DD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027479

```text
(config)# do-exec show sntp <cr>
```

Handler ` RVA 0xCC924B0 `；selector ` 0 `；EOL ` RVA 0x33C478C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027647

```text
(config)# do-exec show sockets <cr>
```

Handler ` RVA 0xD066BA0 `；selector ` 0 `；EOL ` RVA 0x33D88C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032238

```text
(config)# do-exec show sockets <number:1..4294967295> <cr>
```

Handler ` RVA 0xD066E30 `；selector ` 0 `；EOL ` RVA 0x33D88C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` \[pid\]。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-9b6a9c3e8c8e89b1](../../evidence/parameters-sets-012.md#p-9b6a9c3e8c8e89b1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040766

```text
(config)# do-exec show sockets <number:1..4294967295> events <cr>
```

Handler ` RVA 0xD0673A0 `；selector ` 0 `；EOL ` RVA 0x33D88F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` \[pid\]。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-9b6a9c3e8c8e89b1](../../evidence/parameters-sets-012.md#p-9b6a9c3e8c8e89b1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061798

```text
(config)# do-exec show software authenticity file <url:dynamic> <cr>
```

Handler ` RVA 0x14423620 `；selector ` 0 `；EOL ` RVA 0x35D63FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b41342c01fbbf6f](../../evidence/conditions-sets-054.md#c-8b41342c01fbbf6f) · [缺口 G-2b0be3adb83f032d](../../evidence/gaps-sets-002.md#g-2b0be3adb83f032d) · [参数 P-077c05f76a193772](../../evidence/parameters-sets-001.md#p-077c05f76a193772) · [状态效果 S-14336e5a9108e4e5](../../evidence/state_effects-sets-005.md#s-14336e5a9108e4e5)

### path-043624

```text
(config)# do-exec show software authenticity keys <cr>
```

Handler ` RVA 0x14423620 `；selector ` 0 `；EOL ` RVA 0x35D63FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-32f270a831f09210](../../evidence/conditions-sets-020.md#c-32f270a831f09210) · [状态效果 S-5ae43da3814e1d5d](../../evidence/state_effects-sets-020.md#s-5ae43da3814e1d5d)

### path-027791

```text
(config)# do-exec show source-bridge <cr>
```

Handler ` RVA 0x113B1070 `；selector ` 0 `；EOL ` RVA 0x354A5F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e374030f4f615236](../../evidence/conditions-sets-088.md#c-e374030f4f615236) · [状态效果 S-3fab7e0b5851af8c](../../evidence/state_effects-sets-014.md#s-3fab7e0b5851af8c)

### path-027786

```text
(config)# do-exec show spanning-tree <cr>
```

Handler ` RVA 0xF2D2320 `；selector ` 0 `；EOL ` RVA 0x345FF128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060748

```text
(config)# do-exec show spanning-tree <interface> <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 25 `；EOL ` RVA 0x345FA770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31926bf4ea576d1c](../../evidence/conditions-sets-019.md#c-31926bf4ea576d1c) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061176

```text
(config)# do-exec show spanning-tree <interface> cost <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 28 `；EOL ` RVA 0x345F9678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76890ebbdea2e59c](../../evidence/conditions-sets-046.md#c-76890ebbdea2e59c) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061181

```text
(config)# do-exec show spanning-tree <interface> inconsistency <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 31 `；EOL ` RVA 0x345FA450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76890ebbdea2e59c](../../evidence/conditions-sets-046.md#c-76890ebbdea2e59c) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061182

```text
(config)# do-exec show spanning-tree <interface> portfast <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 30 `；EOL ` RVA 0x345FA180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-db8dbe9b7da70955](../../evidence/conditions-sets-085.md#c-db8dbe9b7da70955) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061177

```text
(config)# do-exec show spanning-tree <interface> priority <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 29 `；EOL ` RVA 0x345F9920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76890ebbdea2e59c](../../evidence/conditions-sets-046.md#c-76890ebbdea2e59c) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061180

```text
(config)# do-exec show spanning-tree <interface> rootcost <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 26 `；EOL ` RVA 0x345F9E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76890ebbdea2e59c](../../evidence/conditions-sets-046.md#c-76890ebbdea2e59c) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061178

```text
(config)# do-exec show spanning-tree <interface> state <cr>
```

Handler ` RVA 0xF2D0190 `；selector ` 27 `；EOL ` RVA 0x345F9BC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-76890ebbdea2e59c](../../evidence/conditions-sets-046.md#c-76890ebbdea2e59c) · [缺口 G-56908459f029face](../../evidence/gaps-sets-003.md#g-56908459f029face) · [参数 P-7217d302438ef92d](../../evidence/parameters-sets-009.md#p-7217d302438ef92d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033616

```text
(config)# do-exec show spanning-tree blockedports <cr>
```

Handler ` RVA 0xF2CD530 `；selector ` 0 `；EOL ` RVA 0x345FE1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033696

```text
(config)# do-exec show spanning-tree bridge <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 4 `；EOL ` RVA 0x345FAE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043272

```text
(config)# do-exec show spanning-tree bridge address <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 5 `；EOL ` RVA 0x345FB0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043292

```text
(config)# do-exec show spanning-tree bridge forward-time <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 6 `；EOL ` RVA 0x345FB378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043314

```text
(config)# do-exec show spanning-tree bridge hello-time <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 7 `；EOL ` RVA 0x345FB620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043397

```text
(config)# do-exec show spanning-tree bridge id <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 9 `；EOL ` RVA 0x345FC378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043336

```text
(config)# do-exec show spanning-tree bridge max-age <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 8 `；EOL ` RVA 0x345FB8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043378

```text
(config)# do-exec show spanning-tree bridge priority <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 11 `；EOL ` RVA 0x345FBC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051715

```text
(config)# do-exec show spanning-tree bridge priority system-id <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 10 `；EOL ` RVA 0x345FBBD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043375

```text
(config)# do-exec show spanning-tree bridge protocol <cr>
```

Handler ` RVA 0xF2CE060 `；selector ` 12 `；EOL ` RVA 0x345FC0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060749

```text
(config)# do-exec show spanning-tree detail <cr>
```

Handler ` RVA 0xF2D2320 `；selector ` 0 `；EOL ` RVA 0x345FF128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-23cecebf22d0211e](../../evidence/conditions-sets-014.md#c-23cecebf22d0211e) · [缺口 G-9b9c3135dee8ce4f](../../evidence/gaps-sets-006.md#g-9b9c3135dee8ce4f) · [状态效果 S-fbc95edacdfe4da9](../../evidence/state_effects-sets-053.md#s-fbc95edacdfe4da9)

### path-033651

```text
(config)# do-exec show spanning-tree inconsistentports <cr>
```

Handler ` RVA 0xF2CDBD0 `；selector ` 0 `；EOL ` RVA 0x345FE9D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033640

```text
(config)# do-exec show spanning-tree instances <cr>
```

Handler ` RVA 0xF2CD400 `；selector ` 0 `；EOL ` RVA 0x345FE730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033626

```text
(config)# do-exec show spanning-tree platform <cr>
```

Handler ` RVA 0xF2D3270 `；selector ` 0 `；EOL ` RVA 0x345FE488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033719

```text
(config)# do-exec show spanning-tree root <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 15 `；EOL ` RVA 0x345FC728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043288

```text
(config)# do-exec show spanning-tree root address <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 16 `；EOL ` RVA 0x345FC9A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043310

```text
(config)# do-exec show spanning-tree root cost <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 24 `；EOL ` RVA 0x345FCC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043333

```text
(config)# do-exec show spanning-tree root forward-time <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 17 `；EOL ` RVA 0x345FCEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043353

```text
(config)# do-exec show spanning-tree root hello-time <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 18 `；EOL ` RVA 0x345FD198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043431

```text
(config)# do-exec show spanning-tree root id <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 20 `；EOL ` RVA 0x345FDEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043372

```text
(config)# do-exec show spanning-tree root max-age <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 19 `；EOL ` RVA 0x345FD440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043395

```text
(config)# do-exec show spanning-tree root port <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 23 `；EOL ` RVA 0x345FD6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043434

```text
(config)# do-exec show spanning-tree root priority <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 22 `；EOL ` RVA 0x345FDA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051757

```text
(config)# do-exec show spanning-tree root priority system-id <cr>
```

Handler ` RVA 0xF2CEBA0 `；selector ` 21 `；EOL ` RVA 0x345FD9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a3af8fb2c07b277](../../evidence/conditions-sets-041.md#c-6a3af8fb2c07b277) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033677

```text
(config)# do-exec show spanning-tree summary <cr>
```

Handler ` RVA 0xF2CBD20 `；selector ` 0 `；EOL ` RVA 0x345FED58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2bc815e8e1559759](../../evidence/conditions-sets-017.md#c-2bc815e8e1559759) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032129

```text
(config)# do-exec show sse all <cr>
```

Handler ` RVA 0xC58F120 `；selector ` 0 `；EOL ` RVA 0x33ABB2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-886c560832c83832](../../evidence/state_effects-sets-029.md#s-886c560832c83832)

### path-060729

```text
(config)# do-exec show ssh <?ttyline_action@55558ad7c1b0> <cr>
```

Handler ` RVA 0x12360A90 `；selector ` 0 `；EOL ` RVA 0x358281F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-6d279aef54aaf1d8](../../evidence/gaps-sets-004.md#g-6d279aef54aaf1d8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062851

```text
(config)# do-exec show ssh <?ttyline_action@55558ad7c1b0> rekey <?ttyline_action@55558ad7c510> <cr>
```

Handler ` RVA 0x12360B50 `；selector ` 0 `；EOL ` RVA 0x35828550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-34ce4cc9e8212c85](../../evidence/conditions-sets-021.md#c-34ce4cc9e8212c85) · [缺口 G-29730ffbd76a070d](../../evidence/gaps-sets-002.md#g-29730ffbd76a070d) · [状态效果 S-268a5dc278f46c6a](../../evidence/state_effects-sets-009.md#s-268a5dc278f46c6a)

### path-031355

```text
(config)# do-exec show ssm cdb <cr>
```

Handler ` RVA 0x10429E00 `；selector ` 0 `；EOL ` RVA 0x34B1B930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031549

```text
(config)# do-exec show ssm group <cr>
```

Handler ` RVA 0x10413040 `；selector ` 0 `；EOL ` RVA 0x34B1D598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031504

```text
(config)# do-exec show ssm id <cr>
```

Handler ` RVA 0x10412B40 `；selector ` 0 `；EOL ` RVA 0x34B1BCB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038762

```text
(config)# do-exec show ssm id all <cr>
```

Handler ` RVA 0x10431F40 `；selector ` 0 `；EOL ` RVA 0x34B1BF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-08946b2a95e3d377](../../evidence/state_effects-sets-002.md#s-08946b2a95e3d377)

### path-031502

```text
(config)# do-exec show ssm memory <cr>
```

Handler ` RVA 0x10412FC0 `；selector ` 0 `；EOL ` RVA 0x34B1C6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054653

```text
(config)# do-exec show ssm memory chunk variable feature <cr>
```

Handler ` RVA 0x10428010 `；selector ` 0 `；EOL ` RVA 0x34B1C9D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054693

```text
(config)# do-exec show ssm memory chunk variable queue <cr>
```

Handler ` RVA 0x103F24B0 `；selector ` 0 `；EOL ` RVA 0x34B1CF28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054670

```text
(config)# do-exec show ssm memory chunk variable segment <cr>
```

Handler ` RVA 0x10427B00 `；selector ` 0 `；EOL ` RVA 0x34B1CC80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031475

```text
(config)# do-exec show ssm stats <cr>
```

Handler ` RVA 0x10412220 `；selector ` 0 `；EOL ` RVA 0x34B1D1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027184

```text
(config)# do-exec show stacks <cr>
```

Handler ` RVA 0xE093EC0 `；selector ` 0 `；EOL ` RVA 0x341DB048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027569

```text
(config)# do-exec show standby <cr>
```

Handler ` RVA 0xD31F3E0 `；selector ` 0 `；EOL ` RVA 0x33E156D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-909628c941eadc11](../../evidence/conditions-sets-056.md#c-909628c941eadc11) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060703

```text
(config)# do-exec show standby <interface> <cr>
```

Handler ` RVA 0xD31F3E0 `；selector ` 0 `；EOL ` RVA 0x33E156D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ccaf81df150d22a4](../../evidence/conditions-sets-079.md#c-ccaf81df150d22a4) · [缺口 G-a75903086490ba3e](../../evidence/gaps-sets-006.md#g-a75903086490ba3e) · [参数 P-7cfd46d819168c06](../../evidence/parameters-sets-010.md#p-7cfd46d819168c06) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031125

```text
(config)# do-exec show standby capability <cr>
```

Handler ` RVA 0xD31ECB0 `；selector ` 0 `；EOL ` RVA 0x33E13D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f7bfc21fb96033f](../../evidence/conditions-sets-025.md#c-3f7bfc21fb96033f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060953

```text
(config)# do-exec show standby capability <interface> <cr>
```

Handler ` RVA 0xD31ECB0 `；selector ` 0 `；EOL ` RVA 0x33E13D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c70c13a0af132d13](../../evidence/conditions-sets-077.md#c-c70c13a0af132d13) · [缺口 G-f03c7911bb3295c1](../../evidence/gaps-sets-008.md#g-f03c7911bb3295c1) · [参数 P-cfff618231ae368f](../../evidence/parameters-sets-016.md#p-cfff618231ae368f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031182

```text
(config)# do-exec show standby delay <cr>
```

Handler ` RVA 0xD31EAA0 `；selector ` 0 `；EOL ` RVA 0x33E15288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-27248807d9e52d79](../../evidence/conditions-sets-015.md#c-27248807d9e52d79) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060961

```text
(config)# do-exec show standby delay <interface> <cr>
```

Handler ` RVA 0xD31EAA0 `；selector ` 0 `；EOL ` RVA 0x33E15288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5f01a18a55517f51](../../evidence/conditions-sets-037.md#c-5f01a18a55517f51) · [缺口 G-2e02ec208376b098](../../evidence/gaps-sets-002.md#g-2e02ec208376b098) · [参数 P-8fc7c8354e2382f8](../../evidence/parameters-sets-011.md#p-8fc7c8354e2382f8) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031185

```text
(config)# do-exec show standby internal <cr>
```

Handler ` RVA 0xD31D100 `；selector ` 0 `；EOL ` RVA 0x33E148C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6056dbbf3d54939](../../evidence/conditions-sets-070.md#c-b6056dbbf3d54939) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060964

```text
(config)# do-exec show standby internal <interface> <cr>
```

Handler ` RVA 0xD31D100 `；selector ` 0 `；EOL ` RVA 0x33E148C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e24809208f1fd3c](../../evidence/conditions-sets-055.md#c-8e24809208f1fd3c) · [缺口 G-73eea3cc7d808655](../../evidence/gaps-sets-004.md#g-73eea3cc7d808655) · [参数 P-a46af4c5024fb43a](../../evidence/parameters-sets-013.md#p-a46af4c5024fb43a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061488

```text
(config)# do-exec show standby internal <interface> summary <cr>
```

Handler ` RVA 0xD31E560 `；selector ` 1 `；EOL ` RVA 0x33E149D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8cfb712de6f828d0](../../evidence/conditions-sets-055.md#c-8cfb712de6f828d0) · [缺口 G-73eea3cc7d808655](../../evidence/gaps-sets-004.md#g-73eea3cc7d808655) · [参数 P-a46af4c5024fb43a](../../evidence/parameters-sets-013.md#p-a46af4c5024fb43a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062041

```text
(config)# do-exec show standby internal <interface> summary all <cr>
```

Handler ` RVA 0xD31E560 `；selector ` 2 `；EOL ` RVA 0x33E149B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c5263a4fc33e28b](../../evidence/conditions-sets-017.md#c-2c5263a4fc33e28b) · [缺口 G-73eea3cc7d808655](../../evidence/gaps-sets-004.md#g-73eea3cc7d808655) · [参数 P-a46af4c5024fb43a](../../evidence/parameters-sets-013.md#p-a46af4c5024fb43a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038158

```text
(config)# do-exec show standby internal summary <cr>
```

Handler ` RVA 0xD31E560 `；selector ` 0 `；EOL ` RVA 0x33E14578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8766b213d56f88f0](../../evidence/conditions-sets-052.md#c-8766b213d56f88f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031099

```text
(config)# do-exec show standby neighbors <cr>
```

Handler ` RVA 0xD31F270 `；selector ` 0 `；EOL ` RVA 0x33E139E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb4e3dba9b92b388](../../evidence/conditions-sets-097.md#c-fb4e3dba9b92b388) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060952

```text
(config)# do-exec show standby neighbors <interface> <cr>
```

Handler ` RVA 0xD31F270 `；selector ` 0 `；EOL ` RVA 0x33E139E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4e270a3e848c8663](../../evidence/conditions-sets-031.md#c-4e270a3e848c8663) · [缺口 G-a44680e0a2534356](../../evidence/gaps-sets-006.md#g-a44680e0a2534356) · [参数 P-162ebbc099e68cd0](../../evidence/parameters-sets-002.md#p-162ebbc099e68cd0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031209

```text
(config)# do-exec show standby redirect <cr>
```

Handler ` RVA 0xD31C260 `；selector ` 0 `；EOL ` RVA 0x33E14178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8fe1d8a4eacbee29](../../evidence/conditions-sets-056.md#c-8fe1d8a4eacbee29) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060962

```text
(config)# do-exec show standby redirect <interface> <cr>
```

Handler ` RVA 0xD31C260 `；selector ` 0 `；EOL ` RVA 0x33E14178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd2288226e5e7749](../../evidence/conditions-sets-085.md#c-dd2288226e5e7749) · [缺口 G-2c1de0b866cbbfee](../../evidence/gaps-sets-002.md#g-2c1de0b866cbbfee) · [参数 P-4271b6a17f0c4bd5](../../evidence/parameters-sets-006.md#p-4271b6a17f0c4bd5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028686

```text
(config)# do-exec show starting-keyword <string> <cr>
```

Handler ` RVA 0xDFC94C0 `；selector ` 0 `；EOL ` RVA 0x340D14C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-ff06a9bc530a6b38](../../evidence/parameters-sets-019.md#p-ff06a9bc530a6b38) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026710

```text
(config)# do-exec show startup-config <cr>
```

Handler ` RVA 0xDFF0C60 `；selector ` 0 `；EOL ` RVA 0x340C66B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d2c1d906dd046d8f](../../evidence/conditions-sets-081.md#c-d2c1d906dd046d8f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027799

```text
(config)# do-exec show stun <cr>
```

Handler ` RVA 0x11534340 `；selector ` 0 `；EOL ` RVA 0x354FCF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-992d3734140dce40](../../evidence/conditions-sets-059.md#c-992d3734140dce40) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031540

```text
(config)# do-exec show subscriber circuits <cr>
```

Handler ` RVA 0x10546CA0 `；selector ` 0 `；EOL ` RVA 0x34B58448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038991

```text
(config)# do-exec show subscriber coa statistics <cr>
```

Handler ` RVA 0x109E1420 `；selector ` 0 `；EOL ` RVA 0x34BFC838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031588

```text
(config)# do-exec show subscriber default-session <cr>
```

Handler ` RVA 0x10A1C140 `；selector ` 0 `；EOL ` RVA 0x34BFE1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039234

```text
(config)# do-exec show subscriber disconnect history <cr>
```

Handler ` RVA 0x10A1B270 `；selector ` 0 `；EOL ` RVA 0x34BFDC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

