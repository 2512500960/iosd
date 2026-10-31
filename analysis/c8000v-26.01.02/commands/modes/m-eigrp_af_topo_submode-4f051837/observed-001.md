# eigrp_af_topo_submode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-006853

```text
(config-router-af-topology)# auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346955D8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b9b2e1ba7b47d40](../../evidence/conditions-sets-011.md#c-1b9b2e1ba7b47d40)

### observed_connections-006878

```text
(config-router-af-topology)# cts propagate sgt <cr>
```

Handler ` RVA 0xF59A290 `；selector ` 43 `；EOL ` RVA 0x346920B8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5ae3204b83dc8ebf](../../evidence/conditions-sets-036.md#c-5ae3204b83dc8ebf)

### observed_connections-006873

```text
(config-router-af-topology)# default auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346955D8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1b9b2e1ba7b47d40](../../evidence/conditions-sets-011.md#c-1b9b2e1ba7b47d40) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006917

```text
(config-router-af-topology)# default cts propagate sgt <cr>
```

Handler ` RVA 0xF59A290 `；selector ` 43 `；EOL ` RVA 0x346920B8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5ae3204b83dc8ebf](../../evidence/conditions-sets-036.md#c-5ae3204b83dc8ebf) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006914

```text
(config-router-af-topology)# default default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346C3C80 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad5abf3040e52baf](../../evidence/conditions-sets-067.md#c-ad5abf3040e52baf) · [状态效果 S-fa5871a018d8574e](../../evidence/state_effects-sets-053.md#s-fa5871a018d8574e)

### observed_connections-006872

```text
(config-router-af-topology)# default default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346951B0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3194fe8b283af454](../../evidence/conditions-sets-019.md#c-3194fe8b283af454) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006935

```text
(config-router-af-topology)# default distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346945F8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-8a58377072f8726e](../../evidence/conditions-sets-053.md#c-8a58377072f8726e) · [参数 P-0cca289c26a8e1f0](../../evidence/parameters-sets-001.md#p-0cca289c26a8e1f0) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006904

```text
(config-router-af-topology)# default distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346949C8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e5f6c448f5e60fa2](../../evidence/conditions-sets-089.md#c-e5f6c448f5e60fa2) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006905

```text
(config-router-af-topology)# default distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x34694DF8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-545027b783090af4](../../evidence/conditions-sets-033.md#c-545027b783090af4) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006913

```text
(config-router-af-topology)# default distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346C0748 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b291023e6b0a2c8c](../../evidence/conditions-sets-069.md#c-b291023e6b0a2c8c) · [状态效果 S-41c00cf8e28c3e29](../../evidence/state_effects-sets-014.md#s-41c00cf8e28c3e29)

### observed_connections-006933

```text
(config-router-af-topology)# default distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3545E460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-f937fe0126d8fe97](../../evidence/conditions-sets-096.md#c-f937fe0126d8fe97) · [参数 P-3fd64d524a910c16](../../evidence/parameters-sets-005.md#p-3fd64d524a910c16) · [状态效果 S-5f961ae4473649ba](../../evidence/state_effects-sets-021.md#s-5f961ae4473649ba)

### observed_connections-006903

```text
(config-router-af-topology)# default eigrp event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x34694150 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4bc577d1d7c18b3](../../evidence/conditions-sets-082.md#c-d4bc577d1d7c18b3) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006897

```text
(config-router-af-topology)# default eigrp event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x34693E38 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4e5e481d2602166](../../evidence/conditions-sets-082.md#c-d4e5e481d2602166) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006898

```text
(config-router-af-topology)# default eigrp log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x34693A50 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70ec535eb1bd677c](../../evidence/conditions-sets-044.md#c-70ec535eb1bd677c) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006912

```text
(config-router-af-topology)# default fast-reroute load-sharing <cr>
```

Handler ` RVA 0xF5DDF90 `；selector ` 101 `；EOL ` RVA 0x346C49B8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e0bf17db086c2b91](../../evidence/conditions-sets-087.md#c-e0bf17db086c2b91) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006926

```text
(config-router-af-topology)# default fast-reroute per-prefix all <cr>
```

Handler ` RVA 0xF5DDF90 `；selector ` 103 `；EOL ` RVA 0x346C4158 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e0bf17db086c2b91](../../evidence/conditions-sets-087.md#c-e0bf17db086c2b91) · [状态效果 S-483e2208f3c32278](../../evidence/state_effects-sets-016.md#s-483e2208f3c32278)

### observed_connections-006931

```text
(config-router-af-topology)# default fast-reroute tie-break linecard-disjoint <cr>
```

Handler ` RVA 0xF5DD9C0 `；selector ` 102 `；EOL ` RVA 0x346C45C0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cde195d54508762c](../../evidence/conditions-sets-079.md#c-cde195d54508762c) · [状态效果 S-697f8ff38719e850](../../evidence/state_effects-sets-023.md#s-697f8ff38719e850)

### observed_connections-006858

```text
(config-router-af-topology)# default maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x34692B60 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a6c05f78d3e0f72](../../evidence/conditions-sets-004.md#c-0a6c05f78d3e0f72) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006857

```text
(config-router-af-topology)# default maximum-secondary-paths <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x34692808 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b9951920e11b6c04](../../evidence/conditions-sets-072.md#c-b9951920e11b6c04) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006882

```text
(config-router-af-topology)# default metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x34692460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ac15ca1a3f41c7a](../../evidence/conditions-sets-054.md#c-8ac15ca1a3f41c7a) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006927

```text
(config-router-af-topology)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346C2FD8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-51f82ee0246c664b](../../evidence/conditions-sets-032.md#c-51f82ee0246c664b) · [参数 P-d68cbf379bbeaa89](../../evidence/parameters-sets-016.md#p-d68cbf379bbeaa89) · [状态效果 S-c59eb9150f18fe72](../../evidence/state_effects-sets-042.md#s-c59eb9150f18fe72)

### observed_connections-006894

```text
(config-router-af-topology)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x3545EDB8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9200fb51d427bfe6](../../evidence/conditions-sets-056.md#c-9200fb51d427bfe6) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006899

```text
(config-router-af-topology)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346C12E8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2707a4b1d386b6d8](../../evidence/conditions-sets-015.md#c-2707a4b1d386b6d8) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006886

```text
(config-router-af-topology)# default snmp context <cr>
```

Handler ` RVA 0xF599EC0 `；selector ` 49 `；EOL ` RVA 0x346B1EA0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4d29ca879cd2a011](../../evidence/conditions-sets-030.md#c-4d29ca879cd2a011) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006920

```text
(config-router-af-topology)# default summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346C3568 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-75157f2c70fd3ccc](../../evidence/conditions-sets-045.md#c-75157f2c70fd3ccc) · [参数 P-1089193641c36a2a](../../evidence/parameters-sets-002.md#p-1089193641c36a2a) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006864

```text
(config-router-af-topology)# default table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3545E9A8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d9f5bea5b9a7ec9a](../../evidence/conditions-sets-084.md#c-d9f5bea5b9a7ec9a) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006868

```text
(config-router-af-topology)# default table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x346C0EC8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3d5b59e3ee5c4f19](../../evidence/conditions-sets-024.md#c-3d5b59e3ee5c4f19) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006893

```text
(config-router-af-topology)# default timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x34693638 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ee51d105e897787d](../../evidence/conditions-sets-092.md#c-ee51d105e897787d) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006883

```text
(config-router-af-topology)# default topo-interface default <cr>
```

Handler ` RVA 0xF584C60 `；selector ` 143 `；EOL ` RVA 0x346AD690 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9aee15f63b43f56](../../evidence/conditions-sets-090.md#c-e9aee15f63b43f56) · [状态效果 S-f277599e13fb063b](../../evidence/state_effects-sets-051.md#s-f277599e13fb063b)

### observed_connections-006888

```text
(config-router-af-topology)# default traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x34693250 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4e5e481d2602166](../../evidence/conditions-sets-082.md#c-d4e5e481d2602166) · [状态效果 S-5350fd8da40b53de](../../evidence/state_effects-sets-018.md#s-5350fd8da40b53de)

### observed_connections-006861

```text
(config-router-af-topology)# default variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x34692EB0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-54b48b2c13307651](../../evidence/conditions-sets-033.md#c-54b48b2c13307651) · [状态效果 S-5c36324f1b7e199e](../../evidence/state_effects-sets-020.md#s-5c36324f1b7e199e)

### observed_connections-006877

```text
(config-router-af-topology)# default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346C3C80 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad5abf3040e52baf](../../evidence/conditions-sets-067.md#c-ad5abf3040e52baf) · [状态效果 S-d92cf568a5146f78](../../evidence/state_effects-sets-046.md#s-d92cf568a5146f78)

### observed_connections-006936

```text
(config-router-af-topology)# default-metric <number:1..4294967295> <number:0..4294967295> <number:0..255> <number:1..255> <number:1..65535> <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346951B0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in Kbits per second；` unsigned_number ` delay metric in 10 microsecond units；` unsigned_number ` Reliability metric where 255 is 100% reliable；` unsigned_number ` Effective bandwidth metric (Loading) where 255 is 100% loaded；` unsigned_number ` Maximum Transmission Unit metric of the path 。

[条件 C-10ceeaa5ef75dec0](../../evidence/conditions-sets-007.md#c-10ceeaa5ef75dec0) · [参数 P-c89f8270409f9d18](../../evidence/parameters-sets-015.md#p-c89f8270409f9d18)

### observed_connections-006929

```text
(config-router-af-topology)# distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346945F8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-4c61825acd795585](../../evidence/conditions-sets-030.md#c-4c61825acd795585) · [参数 P-0cca289c26a8e1f0](../../evidence/parameters-sets-001.md#p-0cca289c26a8e1f0)

### observed_connections-006922

```text
(config-router-af-topology)# distance eigrp <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346949C8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for internal routes；` unsigned_number ` Distance for external routes。

[条件 C-98076b6c0516dd00](../../evidence/conditions-sets-059.md#c-98076b6c0516dd00) · [参数 P-5487b3541864806c](../../evidence/parameters-sets-007.md#p-5487b3541864806c)

### observed_connections-006923

```text
(config-router-af-topology)# distance eigrp <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x34694DF8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for internal routes；` unsigned_number ` Distance for external routes。

[条件 C-7879c0c6e25caa1b](../../evidence/conditions-sets-047.md#c-7879c0c6e25caa1b) · [参数 P-46422339d4749205](../../evidence/parameters-sets-006.md#p-46422339d4749205)

### observed_connections-006876

```text
(config-router-af-topology)# distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346C0748 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b291023e6b0a2c8c](../../evidence/conditions-sets-069.md#c-b291023e6b0a2c8c) · [状态效果 S-b0f037cc2a497863](../../evidence/state_effects-sets-037.md#s-b0f037cc2a497863)

### observed_connections-006945

```text
(config-router-af-topology)# distribute-list out <?router_action_proc_vpn@555589c146d0> <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346C0748 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dff06a919e4b39da](../../evidence/conditions-sets-086.md#c-dff06a919e4b39da) · [缺口 G-7893417d514a7131](../../evidence/gaps-sets-005.md#g-7893417d514a7131) · [状态效果 S-62c31ad7ca0dfa4d](../../evidence/state_effects-sets-021.md#s-62c31ad7ca0dfa4d)

### observed_connections-006918

```text
(config-router-af-topology)# distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3545E460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-f937fe0126d8fe97](../../evidence/conditions-sets-096.md#c-f937fe0126d8fe97) · [参数 P-3fd64d524a910c16](../../evidence/parameters-sets-005.md#p-3fd64d524a910c16) · [状态效果 S-15a8cb45ed390547](../../evidence/state_effects-sets-005.md#s-15a8cb45ed390547)

### observed_connections-006947

```text
(config-router-af-topology)# distribute-list prefix-list <string> in <interface> <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3545E460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-b6b283858d990155](../../evidence/conditions-sets-071.md#c-b6b283858d990155) · [缺口 G-551ad77120b555b5](../../evidence/gaps-sets-003.md#g-551ad77120b555b5) · [参数 P-ccfa3a6590f6545b](../../evidence/parameters-sets-016.md#p-ccfa3a6590f6545b) · [状态效果 S-589cc8d58c251a5f](../../evidence/state_effects-sets-019.md#s-589cc8d58c251a5f)

### observed_connections-006944

```text
(config-router-af-topology)# eigrp event-log-size <number:dynamic> <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x34694150 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Max event log entries。

[条件 C-8f334835abed4d07](../../evidence/conditions-sets-055.md#c-8f334835abed4d07) · [缺口 G-6bf371a6231d2d69](../../evidence/gaps-sets-004.md#g-6bf371a6231d2d69) · [参数 P-7e52af5125a7c192](../../evidence/parameters-sets-010.md#p-7e52af5125a7c192)

### observed_connections-006867

```text
(config-router-af-topology)# eigrp event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x34693E38 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4e5e481d2602166](../../evidence/conditions-sets-082.md#c-d4e5e481d2602166)

### observed_connections-006874

```text
(config-router-af-topology)# eigrp log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x34693A50 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49b7a95de7339082](../../evidence/conditions-sets-029.md#c-49b7a95de7339082)

### observed_connections-006852

```text
(config-router-af-topology)# exit-af-topology <cr>
```

Handler ` RVA 0xF574CE0 `；selector ` 0 `；EOL ` RVA 0x34691520 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c296a2debbb0f142](../../evidence/conditions-sets-075.md#c-c296a2debbb0f142)

### observed_connections-006875

```text
(config-router-af-topology)# fast-reroute load-sharing <cr>
```

Handler ` RVA 0xF5DDF90 `；selector ` 101 `；EOL ` RVA 0x346C49B8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0bf17db086c2b91](../../evidence/conditions-sets-087.md#c-e0bf17db086c2b91)

### observed_connections-006906

```text
(config-router-af-topology)# fast-reroute per-prefix all <cr>
```

Handler ` RVA 0xF5DDF90 `；selector ` 103 `；EOL ` RVA 0x346C4158 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0bf17db086c2b91](../../evidence/conditions-sets-087.md#c-e0bf17db086c2b91) · [状态效果 S-e59c1bc7e4caa4f1](../../evidence/state_effects-sets-049.md#s-e59c1bc7e4caa4f1)

### observed_connections-006930

```text
(config-router-af-topology)# fast-reroute tie-break linecard-disjoint <number:1..255> <cr>
```

Handler ` RVA 0xF5DD9C0 `；selector ` 102 `；EOL ` RVA 0x346C45C0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority number。

[条件 C-26b5177f9b29881c](../../evidence/conditions-sets-015.md#c-26b5177f9b29881c) · [参数 P-54e29ab073c48977](../../evidence/parameters-sets-007.md#p-54e29ab073c48977) · [状态效果 S-5ac4135102a80dc4](../../evidence/state_effects-sets-020.md#s-5ac4135102a80dc4)

### observed_connections-006939

```text
(config-router-af-topology)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x34692B60 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-e4852d42f76d80fe](../../evidence/conditions-sets-088.md#c-e4852d42f76d80fe) · [缺口 G-f9a79a9b0ab295df](../../evidence/gaps-sets-009.md#g-f9a79a9b0ab295df) · [参数 P-02f2b892b7788b89](../../evidence/parameters-sets-001.md#p-02f2b892b7788b89)

### observed_connections-006938

```text
(config-router-af-topology)# maximum-secondary-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x34692808 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-11935d93362f2bae](../../evidence/conditions-sets-007.md#c-11935d93362f2bae) · [缺口 G-44feb5becf123995](../../evidence/gaps-sets-003.md#g-44feb5becf123995) · [参数 P-302b6d039e7ae8ee](../../evidence/parameters-sets-004.md#p-302b6d039e7ae8ee)

### observed_connections-006880

```text
(config-router-af-topology)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x34692460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-46332b95fbd0204a](../../evidence/conditions-sets-027.md#c-46332b95fbd0204a) · [参数 P-9b0bd8fe767cfe33](../../evidence/parameters-sets-012.md#p-9b0bd8fe767cfe33)

### observed_connections-006871

```text
(config-router-af-topology)# no auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346955D8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1b9b2e1ba7b47d40](../../evidence/conditions-sets-011.md#c-1b9b2e1ba7b47d40) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006916

```text
(config-router-af-topology)# no cts propagate sgt <cr>
```

Handler ` RVA 0xF59A290 `；selector ` 43 `；EOL ` RVA 0x346920B8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5ae3204b83dc8ebf](../../evidence/conditions-sets-036.md#c-5ae3204b83dc8ebf) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006910

```text
(config-router-af-topology)# no default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346C3C80 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad5abf3040e52baf](../../evidence/conditions-sets-067.md#c-ad5abf3040e52baf) · [状态效果 S-20a07d7f9347cda8](../../evidence/state_effects-sets-007.md#s-20a07d7f9347cda8)

### observed_connections-006870

```text
(config-router-af-topology)# no default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346951B0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f184dd5b7f96756c](../../evidence/conditions-sets-093.md#c-f184dd5b7f96756c) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006934

```text
(config-router-af-topology)# no distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346945F8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-0d5e2e30dd546e94](../../evidence/conditions-sets-005.md#c-0d5e2e30dd546e94) · [参数 P-0cca289c26a8e1f0](../../evidence/parameters-sets-001.md#p-0cca289c26a8e1f0) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006901

```text
(config-router-af-topology)# no distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346949C8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8ef51152be3a8095](../../evidence/conditions-sets-055.md#c-8ef51152be3a8095) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006902

```text
(config-router-af-topology)# no distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x34694DF8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f9d1084a32c2253c](../../evidence/conditions-sets-096.md#c-f9d1084a32c2253c) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006908

```text
(config-router-af-topology)# no distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346C0748 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b291023e6b0a2c8c](../../evidence/conditions-sets-069.md#c-b291023e6b0a2c8c) · [状态效果 S-e9f5c7b56a5d0156](../../evidence/state_effects-sets-049.md#s-e9f5c7b56a5d0156)

### observed_connections-006932

```text
(config-router-af-topology)# no distribute-list prefix-list <string> in <cr>
```

Handler ` RVA 0x112E3690 `；selector ` 29 `；EOL ` RVA 0x3545E460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Prefix-list name。

[条件 C-f937fe0126d8fe97](../../evidence/conditions-sets-096.md#c-f937fe0126d8fe97) · [参数 P-3fd64d524a910c16](../../evidence/parameters-sets-005.md#p-3fd64d524a910c16) · [状态效果 S-1a14cb7e5c0b64d9](../../evidence/state_effects-sets-006.md#s-1a14cb7e5c0b64d9)

### observed_connections-006900

```text
(config-router-af-topology)# no eigrp event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x34694150 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8abbb4489ba9a85](../../evidence/conditions-sets-077.md#c-c8abbb4489ba9a85) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006892

```text
(config-router-af-topology)# no eigrp event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x34693E38 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d4e5e481d2602166](../../evidence/conditions-sets-082.md#c-d4e5e481d2602166) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006895

```text
(config-router-af-topology)# no eigrp log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x34693A50 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bfd1a2a61b33f92d](../../evidence/conditions-sets-074.md#c-bfd1a2a61b33f92d) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006907

```text
(config-router-af-topology)# no fast-reroute load-sharing <cr>
```

Handler ` RVA 0xF5DDF90 `；selector ` 101 `；EOL ` RVA 0x346C49B8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e0bf17db086c2b91](../../evidence/conditions-sets-087.md#c-e0bf17db086c2b91) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006924

```text
(config-router-af-topology)# no fast-reroute per-prefix all <cr>
```

Handler ` RVA 0xF5DDF90 `；selector ` 103 `；EOL ` RVA 0x346C4158 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e0bf17db086c2b91](../../evidence/conditions-sets-087.md#c-e0bf17db086c2b91) · [状态效果 S-67336d9743b5a0d2](../../evidence/state_effects-sets-022.md#s-67336d9743b5a0d2)

### observed_connections-006928

```text
(config-router-af-topology)# no fast-reroute tie-break linecard-disjoint <cr>
```

Handler ` RVA 0xF5DD9C0 `；selector ` 102 `；EOL ` RVA 0x346C45C0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67f068f1f4146b6c](../../evidence/conditions-sets-040.md#c-67f068f1f4146b6c) · [状态效果 S-e15f9578727b5ca2](../../evidence/state_effects-sets-048.md#s-e15f9578727b5ca2)

### observed_connections-006856

```text
(config-router-af-topology)# no maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x34692B60 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ca68f6d889f6e0a3](../../evidence/conditions-sets-078.md#c-ca68f6d889f6e0a3) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006855

```text
(config-router-af-topology)# no maximum-secondary-paths <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x34692808 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7a34d54c621d22c8](../../evidence/conditions-sets-047.md#c-7a34d54c621d22c8) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006879

```text
(config-router-af-topology)# no metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x34692460 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88a2cf72ed74de3f](../../evidence/conditions-sets-053.md#c-88a2cf72ed74de3f) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006925

```text
(config-router-af-topology)# no offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346C2FD8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-51f82ee0246c664b](../../evidence/conditions-sets-032.md#c-51f82ee0246c664b) · [参数 P-d68cbf379bbeaa89](../../evidence/parameters-sets-016.md#p-d68cbf379bbeaa89) · [状态效果 S-da42ffcfe98c7495](../../evidence/state_effects-sets-046.md#s-da42ffcfe98c7495)

### observed_connections-006890

```text
(config-router-af-topology)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x3545EDB8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ee4060c25bcbcb4](../../evidence/conditions-sets-012.md#c-1ee4060c25bcbcb4) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006896

```text
(config-router-af-topology)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346C12E8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1e8aea196b42eb91](../../evidence/conditions-sets-012.md#c-1e8aea196b42eb91) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006884

```text
(config-router-af-topology)# no snmp context <cr>
```

Handler ` RVA 0xF599EC0 `；selector ` 49 `；EOL ` RVA 0x346B1EA0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6e23a771bbb9234c](../../evidence/conditions-sets-043.md#c-6e23a771bbb9234c) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006919

```text
(config-router-af-topology)# no summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346C3568 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-f52bd7aea1bba0ee](../../evidence/conditions-sets-095.md#c-f52bd7aea1bba0ee) · [参数 P-1089193641c36a2a](../../evidence/parameters-sets-002.md#p-1089193641c36a2a) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006862

```text
(config-router-af-topology)# no table-map <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3545E9A8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8e40dc7b2f035187](../../evidence/conditions-sets-055.md#c-8e40dc7b2f035187) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006866

```text
(config-router-af-topology)# no table-map <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x346C0EC8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05ea0a7ce53b869e](../../evidence/conditions-sets-003.md#c-05ea0a7ce53b869e) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006889

```text
(config-router-af-topology)# no timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x34693638 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f37d507c4c0caeb8](../../evidence/conditions-sets-094.md#c-f37d507c4c0caeb8) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006881

```text
(config-router-af-topology)# no topo-interface default <cr>
```

Handler ` RVA 0xF584C60 `；selector ` 143 `；EOL ` RVA 0x346AD690 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e9aee15f63b43f56](../../evidence/conditions-sets-090.md#c-e9aee15f63b43f56) · [状态效果 S-b0c41b9fdd30012c](../../evidence/state_effects-sets-037.md#s-b0c41b9fdd30012c)

### observed_connections-006887

```text
(config-router-af-topology)# no traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x34693250 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d4e5e481d2602166](../../evidence/conditions-sets-082.md#c-d4e5e481d2602166) · [状态效果 S-7b4dd6b2abd84ff7](../../evidence/state_effects-sets-026.md#s-7b4dd6b2abd84ff7)

### observed_connections-006859

```text
(config-router-af-topology)# no variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x34692EB0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67fa7334dae74987](../../evidence/conditions-sets-040.md#c-67fa7334dae74987) · [状态效果 S-1a0578189ba807c7](../../evidence/state_effects-sets-006.md#s-1a0578189ba807c7)

### observed_connections-006921

```text
(config-router-af-topology)# offset-list <number:0..99> in <number:0..2147483647> <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346C2FD8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-c071fefc1a2a63b1](../../evidence/conditions-sets-074.md#c-c071fefc1a2a63b1) · [参数 P-4f96407d2c0f52e8](../../evidence/parameters-sets-007.md#p-4f96407d2c0f52e8) · [状态效果 S-4965db86f02c3f87](../../evidence/state_effects-sets-016.md#s-4965db86f02c3f87)

### observed_connections-006946

```text
(config-router-af-topology)# offset-list <string> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346C2FD8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Access-list name。

[条件 C-1d4daebc9e694b36](../../evidence/conditions-sets-011.md#c-1d4daebc9e694b36) · [缺口 G-22a82cae1f438198](../../evidence/gaps-sets-002.md#g-22a82cae1f438198) · [参数 P-7fc1ae50e752baf1](../../evidence/parameters-sets-010.md#p-7fc1ae50e752baf1) · [状态效果 S-ad3af413ded4021b](../../evidence/state_effects-sets-037.md#s-ad3af413ded4021b)

### observed_connections-006942

```text
(config-router-af-topology)# redistribute <?ipv6_router_action@55558a9b3360> <cr>
```

Handler ` RVA 0x112E4940 `；selector ` 32 `；EOL ` RVA 0x3545FE20 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5a7d3a1e4bfcd727](../../evidence/conditions-sets-035.md#c-5a7d3a1e4bfcd727) · [缺口 G-1081078c7a8b42e6](../../evidence/gaps-sets-001.md#g-1081078c7a8b42e6)

### observed_connections-006943

```text
(config-router-af-topology)# redistribute <?router_action_no_proc_vpn@555589c15930> <cr>
```

Handler ` RVA 0xF5DE550 `；selector ` 32 `；EOL ` RVA 0x346C2918 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44a74a6d90d902fe](../../evidence/conditions-sets-027.md#c-44a74a6d90d902fe) · [缺口 G-aab42ff063f0aabc](../../evidence/gaps-sets-006.md#g-aab42ff063f0aabc)

### observed_connections-006911

```text
(config-router-af-topology)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x3545EDB8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-d461a65457676706](../../evidence/conditions-sets-082.md#c-d461a65457676706) · [参数 P-ad11a04cc3ed1982](../../evidence/parameters-sets-013.md#p-ad11a04cc3ed1982)

### observed_connections-006915

```text
(config-router-af-topology)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346C12E8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-687c50443d318dc0](../../evidence/conditions-sets-040.md#c-687c50443d318dc0) · [参数 P-84d08201acdba00c](../../evidence/parameters-sets-010.md#p-84d08201acdba00c)

### observed_connections-006885

```text
(config-router-af-topology)# snmp context <string> <cr>
```

Handler ` RVA 0xF599EC0 `；selector ` 49 `；EOL ` RVA 0x346B1EA0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name。

[条件 C-1ce99a7957dadfb4](../../evidence/conditions-sets-011.md#c-1ce99a7957dadfb4) · [参数 P-7f21d59e3bd3bfdf](../../evidence/parameters-sets-010.md#p-7f21d59e3bd3bfdf)

### observed_connections-006909

```text
(config-router-af-topology)# summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346C3568 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-73cdbfaef4d98a71](../../evidence/conditions-sets-045.md#c-73cdbfaef4d98a71) · [参数 P-1089193641c36a2a](../../evidence/parameters-sets-002.md#p-1089193641c36a2a)

### observed_connections-006940

```text
(config-router-af-topology)# summary-metric <prefix:dynamic> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x354601C0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary to configure static metric。

[条件 C-939bcf54842e01ab](../../evidence/conditions-sets-057.md#c-939bcf54842e01ab) · [缺口 G-96a9cb5c62b00457](../../evidence/gaps-sets-006.md#g-96a9cb5c62b00457) · [参数 P-59ffcda0d2a67c8e](../../evidence/parameters-sets-007.md#p-59ffcda0d2a67c8e)

### observed_connections-006941

```text
(config-router-af-topology)# summary-metric <prefix:dynamic> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346C3568 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-249105798decc406](../../evidence/conditions-sets-014.md#c-249105798decc406) · [缺口 G-3a58be33006d19e5](../../evidence/gaps-sets-003.md#g-3a58be33006d19e5) · [参数 P-52385144a6f21847](../../evidence/parameters-sets-007.md#p-52385144a6f21847) · [状态效果 S-3bed8936b16c9f6c](../../evidence/state_effects-sets-013.md#s-3bed8936b16c9f6c)

### observed_connections-006865

```text
(config-router-af-topology)# table-map <string> <cr>
```

Handler ` RVA 0x118ADE60 `；selector ` 17 `；EOL ` RVA 0x3545E9A8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-2fbd5418e7df6994](../../evidence/conditions-sets-019.md#c-2fbd5418e7df6994) · [参数 P-5db26ff3a30dc7bf](../../evidence/parameters-sets-007.md#p-5db26ff3a30dc7bf)

### observed_connections-006869

```text
(config-router-af-topology)# table-map <string> <cr>
```

Handler ` RVA 0xE1F4690 `；selector ` 0 `；EOL ` RVA 0x346C0EC8 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` route-map name。

[条件 C-ead1864d120dfc7a](../../evidence/conditions-sets-091.md#c-ead1864d120dfc7a) · [参数 P-738c1797b410488d](../../evidence/parameters-sets-009.md#p-738c1797b410488d)

### observed_connections-006891

```text
(config-router-af-topology)# timers active-time disabled <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x34693638 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-919b1baa6b88fa0e](../../evidence/conditions-sets-056.md#c-919b1baa6b88fa0e)

### observed_connections-006937

```text
(config-router-af-topology)# topo-interface <interface> <cr>
```

Handler ` RVA 0xF584C60 `；selector ` 143 `；EOL ` RVA 0x346AD690 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1e6ed87a078dce83](../../evidence/conditions-sets-012.md#c-1e6ed87a078dce83) · [缺口 G-e3037d0d947a4e70](../../evidence/gaps-sets-008.md#g-e3037d0d947a4e70) · [参数 P-2a3fc4911153082b](../../evidence/parameters-sets-004.md#p-2a3fc4911153082b)

### observed_connections-006854

```text
(config-router-af-topology)# topo-interface default <cr>
```

Handler ` RVA 0xF584C60 `；selector ` 143 `；EOL ` RVA 0x346AD690 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9aee15f63b43f56](../../evidence/conditions-sets-090.md#c-e9aee15f63b43f56) · [状态效果 S-a609a88a9a0beee6](../../evidence/state_effects-sets-035.md#s-a609a88a9a0beee6)

### observed_connections-006863

```text
(config-router-af-topology)# traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x34693250 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d4e5e481d2602166](../../evidence/conditions-sets-082.md#c-d4e5e481d2602166) · [状态效果 S-3ed3ce700ba8c44c](../../evidence/state_effects-sets-014.md#s-3ed3ce700ba8c44c)

### observed_connections-006860

```text
(config-router-af-topology)# variance <number:1..128> <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x34692EB0 `。

模式根 ` RVA 0x346912D0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric variance multiplier。

[条件 C-355bdfa2a5730fc6](../../evidence/conditions-sets-021.md#c-355bdfa2a5730fc6) · [参数 P-5f4df16c38b00aa0](../../evidence/parameters-sets-008.md#p-5f4df16c38b00aa0)

