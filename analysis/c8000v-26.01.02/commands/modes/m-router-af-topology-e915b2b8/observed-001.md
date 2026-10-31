# router-af-topology · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-005001

```text
(config-router-af-topology)# adjacency stagger none <number:1..65535> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 25 `；EOL ` RVA 0x348B6880 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of adjacencies allowed to be forming。

[条件 C-d986980720612073](../../evidence/conditions-sets-084.md#c-d986980720612073) · [参数 P-e8d1c8108a39362d](../../evidence/parameters-sets-017.md#p-e8d1c8108a39362d) · [状态效果 S-c206e42c09c224bb](../../evidence/state_effects-sets-041.md#s-c206e42c09c224bb)

### observed_connections-004857

```text
(config-router-af-topology)# advertise passive-only <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 84 `；EOL ` RVA 0x34B96BD0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3)

### observed_connections-004922

```text
(config-router-af-topology)# area <address> authentication <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 6 `；EOL ` RVA 0x348BAF88 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-ee059b97133752a5](../../evidence/conditions-sets-092.md#c-ee059b97133752a5) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-9d5b13425efedfff](../../evidence/state_effects-sets-033.md#s-9d5b13425efedfff)

### observed_connections-004981

```text
(config-router-af-topology)# area <address> capability default-exclusion <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 14 `；EOL ` RVA 0x348BB290 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-0cc897d098523ce2](../../evidence/conditions-sets-005.md#c-0cc897d098523ce2) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-dae985b8ae8dff57](../../evidence/state_effects-sets-046.md#s-dae985b8ae8dff57)

### observed_connections-004982

```text
(config-router-af-topology)# area <address> default-cost <number:0..16777214> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 5 `；EOL ` RVA 0x348BB5C0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` Stub's advertised external route metric。

[条件 C-fb4701e44491ec38](../../evidence/conditions-sets-097.md#c-fb4701e44491ec38) · [参数 P-3d3801ed98357018](../../evidence/parameters-sets-005.md#p-3d3801ed98357018)

### observed_connections-005018

```text
(config-router-af-topology)# area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 12 `；EOL ` RVA 0x348BCDD0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IP prefix-list。

[条件 C-7d6e3710ca6b0d4d](../../evidence/conditions-sets-049.md#c-7d6e3710ca6b0d4d) · [参数 P-e769b024470f7941](../../evidence/parameters-sets-017.md#p-e769b024470f7941) · [状态效果 S-946181bf573168e9](../../evidence/state_effects-sets-031.md#s-946181bf573168e9)

### observed_connections-004955

```text
(config-router-af-topology)# area <address> nssa <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 3 `；EOL ` RVA 0x348BC528 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-4ef469467590d2f0](../../evidence/conditions-sets-031.md#c-4ef469467590d2f0) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9)

### observed_connections-004986

```text
(config-router-af-topology)# area <address> packet-size <number:576..10000> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 16 `；EOL ` RVA 0x348BB8D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` unsigned_number ` OSPF Area Mode Packet Size。

[条件 C-cb7092f2354b05ee](../../evidence/conditions-sets-078.md#c-cb7092f2354b05ee) · [参数 P-3ac4289a9209239d](../../evidence/parameters-sets-005.md#p-3ac4289a9209239d)

### observed_connections-005008

```text
(config-router-af-topology)# area <address> range <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 2 `；EOL ` RVA 0x348BC948 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP address to match；` address ` IP mask for address。

[条件 C-a194b77e88b35eef](../../evidence/conditions-sets-062.md#c-a194b77e88b35eef) · [参数 P-fbb7eb8a1cb44d99](../../evidence/parameters-sets-019.md#p-fbb7eb8a1cb44d99)

### observed_connections-005010

```text
(config-router-af-topology)# area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 13 `；EOL ` RVA 0x348BE398 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP addr associated with sham-link source；` address ` IP addr associated with sham-link destination。

[条件 C-b883815e7e9a4783](../../evidence/conditions-sets-071.md#c-b883815e7e9a4783) · [参数 P-fe564c79ac44a63c](../../evidence/parameters-sets-019.md#p-fe564c79ac44a63c)

### observed_connections-004944

```text
(config-router-af-topology)# area <address> stub <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 4 `；EOL ` RVA 0x348BBC80 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-8ff34d44ae6ba9c9](../../evidence/conditions-sets-056.md#c-8ff34d44ae6ba9c9) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9)

### observed_connections-005000

```text
(config-router-af-topology)# area <address> virtual-link <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 1 `；EOL ` RVA 0x348BDAB0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` ID (IP addr) associated with virtual link neighbor。

[条件 C-1526a5f74077fd89](../../evidence/conditions-sets-008.md#c-1526a5f74077fd89) · [参数 P-844fb23e9002fdb6](../../evidence/parameters-sets-010.md#p-844fb23e9002fdb6)

### observed_connections-004828

```text
(config-router-af-topology)# auto-cost <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 0 `；EOL ` RVA 0x348B80B8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e)

### observed_connections-004976

```text
(config-router-af-topology)# autoroute-exclude prefix-list <string> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 48 `；EOL ` RVA 0x348BA6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of an IP prefix-list。

[条件 C-818b642c6b59b65b](../../evidence/conditions-sets-050.md#c-818b642c6b59b65b) · [参数 P-1a55825c3aab4011](../../evidence/parameters-sets-002.md#p-1a55825c3aab4011)

### observed_connections-004916

```text
(config-router-af-topology)# capability opaque <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 4 `；EOL ` RVA 0x348BA258 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f78818f9a84e39a2](../../evidence/conditions-sets-096.md#c-f78818f9a84e39a2) · [状态效果 S-ac1e2a5dbc0c0329](../../evidence/state_effects-sets-036.md#s-ac1e2a5dbc0c0329)

### observed_connections-004867

```text
(config-router-af-topology)# compatible rfc1583 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 6 `；EOL ` RVA 0x348B55E0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920)

### observed_connections-004872

```text
(config-router-af-topology)# compatible rfc1587 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 7 `；EOL ` RVA 0x348B58F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af1df3eeeb0f42e6](../../evidence/conditions-sets-068.md#c-af1df3eeeb0f42e6)

### observed_connections-004881

```text
(config-router-af-topology)# compatible rfc5243 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 8 `；EOL ` RVA 0x348B5BC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd2ffbf9ad0b3962](../../evidence/conditions-sets-085.md#c-dd2ffbf9ad0b3962)

### observed_connections-004841

```text
(config-router-af-topology)# context <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNMP Context Name。

[条件 C-9affa1869574e86e](../../evidence/conditions-sets-060.md#c-9affa1869574e86e) · [参数 P-f3e465802edc027f](../../evidence/parameters-sets-018.md#p-f3e465802edc027f) · [状态效果 S-355a44aeb0ea4c7f](../../evidence/state_effects-sets-012.md#s-355a44aeb0ea4c7f)

### observed_connections-004964

```text
(config-router-af-topology)# default adjacency stagger <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 25 `；EOL ` RVA 0x348B6880 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-312b8656fc05d829](../../evidence/conditions-sets-019.md#c-312b8656fc05d829) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004930

```text
(config-router-af-topology)# default advertise passive-only <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 84 `；EOL ` RVA 0x34B96BD0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004959

```text
(config-router-af-topology)# default area <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 11 `；EOL ` RVA 0x348BE738 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-dbf761579fbecabc](../../evidence/conditions-sets-085.md#c-dbf761579fbecabc) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004983

```text
(config-router-af-topology)# default area <address> authentication <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 6 `；EOL ` RVA 0x348BAF88 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-ee059b97133752a5](../../evidence/conditions-sets-092.md#c-ee059b97133752a5) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-e5810a325737becc](../../evidence/state_effects-sets-049.md#s-e5810a325737becc)

### observed_connections-005006

```text
(config-router-af-topology)# default area <address> capability default-exclusion <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 14 `；EOL ` RVA 0x348BB290 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-0cc897d098523ce2](../../evidence/conditions-sets-005.md#c-0cc897d098523ce2) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-1204db9b15b84160](../../evidence/state_effects-sets-004.md#s-1204db9b15b84160)

### observed_connections-004984

```text
(config-router-af-topology)# default area <address> default-cost <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 5 `；EOL ` RVA 0x348BB5C0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-c16a4e545153f0cd](../../evidence/conditions-sets-075.md#c-c16a4e545153f0cd) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005029

```text
(config-router-af-topology)# default area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 12 `；EOL ` RVA 0x348BCDD0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IP prefix-list。

[条件 C-7d6e3710ca6b0d4d](../../evidence/conditions-sets-049.md#c-7d6e3710ca6b0d4d) · [参数 P-e769b024470f7941](../../evidence/parameters-sets-017.md#p-e769b024470f7941) · [状态效果 S-bd682b1877c5c6a3](../../evidence/state_effects-sets-040.md#s-bd682b1877c5c6a3)

### observed_connections-004997

```text
(config-router-af-topology)# default area <address> nssa <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 3 `；EOL ` RVA 0x348BC528 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-4ef469467590d2f0](../../evidence/conditions-sets-031.md#c-4ef469467590d2f0) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004988

```text
(config-router-af-topology)# default area <address> packet-size <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 16 `；EOL ` RVA 0x348BB8D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-844bb2b7a1c3cecb](../../evidence/conditions-sets-051.md#c-844bb2b7a1c3cecb) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005019

```text
(config-router-af-topology)# default area <address> range <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 2 `；EOL ` RVA 0x348BC948 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP address to match；` address ` IP mask for address。

[条件 C-979ce91fb66e748c](../../evidence/conditions-sets-059.md#c-979ce91fb66e748c) · [参数 P-fbb7eb8a1cb44d99](../../evidence/parameters-sets-019.md#p-fbb7eb8a1cb44d99) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005026

```text
(config-router-af-topology)# default area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 13 `；EOL ` RVA 0x348BE398 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP addr associated with sham-link source；` address ` IP addr associated with sham-link destination。

[条件 C-b883815e7e9a4783](../../evidence/conditions-sets-071.md#c-b883815e7e9a4783) · [参数 P-fe564c79ac44a63c](../../evidence/parameters-sets-019.md#p-fe564c79ac44a63c) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004992

```text
(config-router-af-topology)# default area <address> stub <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 4 `；EOL ` RVA 0x348BBC80 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-8ff34d44ae6ba9c9](../../evidence/conditions-sets-056.md#c-8ff34d44ae6ba9c9) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005011

```text
(config-router-af-topology)# default area <address> virtual-link <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 1 `；EOL ` RVA 0x348BDAB0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` ID (IP addr) associated with virtual link neighbor。

[条件 C-1526a5f74077fd89](../../evidence/conditions-sets-008.md#c-1526a5f74077fd89) · [参数 P-844fb23e9002fdb6](../../evidence/parameters-sets-010.md#p-844fb23e9002fdb6) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004883

```text
(config-router-af-topology)# default auto-cost <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 0 `；EOL ` RVA 0x348B80B8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004920

```text
(config-router-af-topology)# default autoroute-exclude <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 48 `；EOL ` RVA 0x348BA6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b1cac64c57da0e09](../../evidence/conditions-sets-069.md#c-b1cac64c57da0e09) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004975

```text
(config-router-af-topology)# default capability opaque <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 4 `；EOL ` RVA 0x348BA258 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f78818f9a84e39a2](../../evidence/conditions-sets-096.md#c-f78818f9a84e39a2) · [状态效果 S-162a0f8aadce67c8](../../evidence/state_effects-sets-005.md#s-162a0f8aadce67c8)

### observed_connections-004935

```text
(config-router-af-topology)# default compatible rfc1583 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 6 `；EOL ` RVA 0x348B55E0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004947

```text
(config-router-af-topology)# default compatible rfc1587 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 7 `；EOL ` RVA 0x348B58F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af1df3eeeb0f42e6](../../evidence/conditions-sets-068.md#c-af1df3eeeb0f42e6) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004951

```text
(config-router-af-topology)# default compatible rfc5243 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 8 `；EOL ` RVA 0x348B5BC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd2ffbf9ad0b3962](../../evidence/conditions-sets-085.md#c-dd2ffbf9ad0b3962) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004840

```text
(config-router-af-topology)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004926

```text
(config-router-af-topology)# default default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x34278370 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-314c82090fe484ba](../../evidence/conditions-sets-019.md#c-314c82090fe484ba) · [状态效果 S-b687400190341c61](../../evidence/state_effects-sets-039.md#s-b687400190341c61)

### observed_connections-004854

```text
(config-router-af-topology)# default default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x34278C38 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e65b5e2dbb356ab9](../../evidence/conditions-sets-089.md#c-e65b5e2dbb356ab9) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004866

```text
(config-router-af-topology)# default distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34277A70 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a9b5e957fa0056f5](../../evidence/conditions-sets-065.md#c-a9b5e957fa0056f5) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004932

```text
(config-router-af-topology)# default distance ospf <cr>
```

Handler ` RVA 0xFC6D2A0 `；selector ` 0 `；EOL ` RVA 0x348C0E30 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4ecd6ea1d95722bf](../../evidence/conditions-sets-031.md#c-4ecd6ea1d95722bf) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004961

```text
(config-router-af-topology)# default distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3427C6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-30a5be791d80a30d](../../evidence/conditions-sets-019.md#c-30a5be791d80a30d) · [状态效果 S-1bd70255ae25b04d](../../evidence/state_effects-sets-006.md#s-1bd70255ae25b04d)

### observed_connections-004880

```text
(config-router-af-topology)# default domain-id <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 9 `；EOL ` RVA 0x348B3FA8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e1679f887cf9e2dc](../../evidence/conditions-sets-087.md#c-e1679f887cf9e2dc) · [状态效果 S-a6fea0d2707cf5ca](../../evidence/state_effects-sets-035.md#s-a6fea0d2707cf5ca)

### observed_connections-004824

```text
(config-router-af-topology)# default domain-tag <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 10 `；EOL ` RVA 0x348B3EC8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3be3fab7feea5f75](../../evidence/conditions-sets-023.md#c-3be3fab7feea5f75) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004912

```text
(config-router-af-topology)# default event-log <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 22 `；EOL ` RVA 0x348B6CE8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-291fbdab516f6b88](../../evidence/conditions-sets-016.md#c-291fbdab516f6b88) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004993

```text
(config-router-af-topology)# default ignore lsa mospf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 3 `；EOL ` RVA 0x348B61F8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004869

```text
(config-router-af-topology)# default ignore-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 27 `；EOL ` RVA 0x34B971A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004939

```text
(config-router-af-topology)# default interface-id snmp-if-index <cr>
```

Handler ` RVA 0xFC6E310 `；selector ` 0 `；EOL ` RVA 0x348B5EC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005017

```text
(config-router-af-topology)# default ip route priority high tag <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 66 `；EOL ` RVA 0x34B96870 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b19b374d1afe6fda](../../evidence/conditions-sets-069.md#c-b19b374d1afe6fda) · [状态效果 S-d188d52ced7faa3c](../../evidence/state_effects-sets-044.md#s-d188d52ced7faa3c)

### observed_connections-004882

```text
(config-router-af-topology)# default ispf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 16 `；EOL ` RVA 0x348B6490 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004972

```text
(config-router-af-topology)# default limit retransmissions <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 13 `；EOL ` RVA 0x348B8DB8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-452a6e9bd44b3e95](../../evidence/conditions-sets-027.md#c-452a6e9bd44b3e95) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004909

```text
(config-router-af-topology)# default log-adjacency-changes <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 2 `；EOL ` RVA 0x348B7480 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004890

```text
(config-router-af-topology)# default max-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 18 `；EOL ` RVA 0x348B8478 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-477cf3b8e6ea52ce](../../evidence/conditions-sets-028.md#c-477cf3b8e6ea52ce) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004847

```text
(config-router-af-topology)# default max-metric intra-area <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 5 `；EOL ` RVA 0x348B47F8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05997d2f9a14e85e](../../evidence/conditions-sets-003.md#c-05997d2f9a14e85e) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004949

```text
(config-router-af-topology)# default max-metric router-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 12 `；EOL ` RVA 0x348B4D20 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ff11218e1b67bcf](../../evidence/conditions-sets-043.md#c-6ff11218e1b67bcf) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004913

```text
(config-router-af-topology)# default metric <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 89 `；EOL ` RVA 0x34B97F28 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27358fc06c154ce7](../../evidence/conditions-sets-015.md#c-27358fc06c154ce7) · [状态效果 S-48e3eba133394d15](../../evidence/state_effects-sets-016.md#s-48e3eba133394d15)

### observed_connections-004919

```text
(config-router-af-topology)# default multicast-intact <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 49 `；EOL ` RVA 0x348BA9E0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004863

```text
(config-router-af-topology)# default never-set-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 28 `；EOL ` RVA 0x34B96EC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004821

```text
(config-router-af-topology)# default packet-size <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 50 `；EOL ` RVA 0x348B3920 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7dfe1059cb50fd2](../../evidence/conditions-sets-083.md#c-d7dfe1059cb50fd2) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004855

```text
(config-router-af-topology)# default prc-interval <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 30 `；EOL ` RVA 0x34B962E8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec2af5063415f528](../../evidence/conditions-sets-091.md#c-ec2af5063415f528) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005003

```text
(config-router-af-topology)# default prefix-priority high route-map <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 28 `；EOL ` RVA 0x348B9B68 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d51271866844f33](../../evidence/conditions-sets-042.md#c-6d51271866844f33) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004907

```text
(config-router-af-topology)# default prefix-suppression <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 27 `；EOL ` RVA 0x348B9E48 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004819

```text
(config-router-af-topology)# default priority <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 19 `；EOL ` RVA 0x348B34A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d39e8ff578d3f7ad](../../evidence/conditions-sets-082.md#c-d39e8ff578d3f7ad) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004851

```text
(config-router-af-topology)# default priority <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 85 `；EOL ` RVA 0x34B95A50 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a2c8af6eb075c7ab](../../evidence/conditions-sets-063.md#c-a2c8af6eb075c7ab) · [状态效果 S-f93c306befdc8312](../../evidence/state_effects-sets-053.md#s-f93c306befdc8312)

### observed_connections-004896

```text
(config-router-af-topology)# default process-min-time percent <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 21 `；EOL ` RVA 0x348B90C8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6200d66cf296e681](../../evidence/conditions-sets-038.md#c-6200d66cf296e681) · [状态效果 S-5c23c5f8f9e9a96c](../../evidence/state_effects-sets-020.md#s-5c23c5f8f9e9a96c)

### observed_connections-004942

```text
(config-router-af-topology)# default queue-depth hello <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 20 `；EOL ` RVA 0x348B5250 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41d44b60b51e96df](../../evidence/conditions-sets-026.md#c-41d44b60b51e96df) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004844

```text
(config-router-af-topology)# default router-id <cr>
```

Handler ` RVA 0xFC6D990 `；selector ` 0 `；EOL ` RVA 0x348B3548 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c732ed2ff8c0edd](../../evidence/conditions-sets-054.md#c-8c732ed2ff8c0edd) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004884

```text
(config-router-af-topology)# default set-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 26 `；EOL ` RVA 0x34B97AF8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7ac2b97e85e50f96](../../evidence/conditions-sets-048.md#c-7ac2b97e85e50f96) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004885

```text
(config-router-af-topology)# default set-overload-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 25 `；EOL ` RVA 0x34B97518 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bc5fabfb76f36d6](../../evidence/conditions-sets-054.md#c-8bc5fabfb76f36d6) · [状态效果 S-d4a19780f456ac5e](../../evidence/state_effects-sets-045.md#s-d4a19780f456ac5e)

### observed_connections-004899

```text
(config-router-af-topology)# default shutdown <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 24 `；EOL ` RVA 0x348B9770 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004933

```text
(config-router-af-topology)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-005023

```text
(config-router-af-topology)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-3447ecc5f47cf3b7](../../evidence/state_effects-sets-012.md#s-3447ecc5f47cf3b7)

### observed_connections-005022

```text
(config-router-af-topology)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-c6f1ff92650f4721](../../evidence/state_effects-sets-042.md#s-c6f1ff92650f4721)

### observed_connections-004865

```text
(config-router-af-topology)# default spf-interval <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 29 `；EOL ` RVA 0x34B95E48 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6beba16ebdfb4eae](../../evidence/conditions-sets-042.md#c-6beba16ebdfb4eae) · [状态效果 S-9d44d6af5e5fa1cd](../../evidence/state_effects-sets-033.md#s-9d44d6af5e5fa1cd)

### observed_connections-004960

```text
(config-router-af-topology)# default statistics rib-timings <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 17 `；EOL ` RVA 0x348B7150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004989

```text
(config-router-af-topology)# default summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x3427B150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-f94f9efc0e1d02cf](../../evidence/conditions-sets-096.md#c-f94f9efc0e1d02cf) · [参数 P-19f6a7c1aa1c9c3a](../../evidence/parameters-sets-002.md#p-19f6a7c1aa1c9c3a) · [状态效果 S-e41bbadfc038e84d](../../evidence/state_effects-sets-048.md#s-e41bbadfc038e84d)

### observed_connections-004931

```text
(config-router-af-topology)# default summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x3427B730 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP summary address。

[条件 C-5391e97961371165](../../evidence/conditions-sets-033.md#c-5391e97961371165) · [参数 P-53d78b0d3a9718f3](../../evidence/parameters-sets-007.md#p-53d78b0d3a9718f3) · [状态效果 S-e41bbadfc038e84d](../../evidence/state_effects-sets-048.md#s-e41bbadfc038e84d)

### observed_connections-004943

```text
(config-router-af-topology)# default timers basic <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x3427D0D0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-605f1fa98d007342](../../evidence/conditions-sets-037.md#c-605f1fa98d007342) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004953

```text
(config-router-af-topology)# default timers lsa arrival <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 8 `；EOL ` RVA 0x348BF9C8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8598e43f2981a77b](../../evidence/conditions-sets-052.md#c-8598e43f2981a77b) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004901

```text
(config-router-af-topology)# default timers lsa-arrival <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 1 `；EOL ` RVA 0x348BFF58 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b31fbd46425da34b](../../evidence/conditions-sets-069.md#c-b31fbd46425da34b) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004891

```text
(config-router-af-topology)# default timers lsa-group-pacing <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 2 `；EOL ` RVA 0x348BF9F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-45cc56af86f0a78f](../../evidence/conditions-sets-027.md#c-45cc56af86f0a78f) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004897

```text
(config-router-af-topology)# default timers lsa-interval <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 0 `；EOL ` RVA 0x348BFCB8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-90e01536d68d6f8e](../../evidence/conditions-sets-056.md#c-90e01536d68d6f8e) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004970

```text
(config-router-af-topology)# default timers pacing flood <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 3 `；EOL ` RVA 0x348C0500 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-49659435b0155479](../../evidence/conditions-sets-029.md#c-49659435b0155479) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004966

```text
(config-router-af-topology)# default timers pacing lsa-group <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 2 `；EOL ` RVA 0x348C0498 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70aa0b72c940a689](../../evidence/conditions-sets-044.md#c-70aa0b72c940a689) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004973

```text
(config-router-af-topology)# default timers pacing retransmission <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 4 `；EOL ` RVA 0x348C07A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b76641f948d10a8b](../../evidence/conditions-sets-071.md#c-b76641f948d10a8b) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004999

```text
(config-router-af-topology)# default timers throttle lsa <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 9 `；EOL ` RVA 0x348BF608 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9c40e6da4053c5ab](../../evidence/conditions-sets-060.md#c-9c40e6da4053c5ab) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004996

```text
(config-router-af-topology)# default timers throttle spf <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 5 `；EOL ` RVA 0x348BF210 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9a2b0c9bb8f0e7da](../../evidence/conditions-sets-060.md#c-9a2b0c9bb8f0e7da) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004978

```text
(config-router-af-topology)# default traffic-share min across-interfaces <cr>
```

Handler ` RVA 0xE1FA2E0 `；selector ` 0 `；EOL ` RVA 0x34277568 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-99e26537a5dcb053](../../evidence/conditions-sets-059.md#c-99e26537a5dcb053) · [状态效果 S-93ed162cf83c13a9](../../evidence/state_effects-sets-031.md#s-93ed162cf83c13a9)

### observed_connections-004968

```text
(config-router-af-topology)# default ttl-security all-interfaces <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 23 `；EOL ` RVA 0x348B9488 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84c0b8478cfd904c](../../evidence/conditions-sets-051.md#c-84c0b8478cfd904c) · [状态效果 S-0be591b30d47851c](../../evidence/state_effects-sets-003.md#s-0be591b30d47851c)

### observed_connections-004852

```text
(config-router-af-topology)# default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x34278370 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-314c82090fe484ba](../../evidence/conditions-sets-019.md#c-314c82090fe484ba) · [状态效果 S-8cfcbddcd06f818b](../../evidence/state_effects-sets-030.md#s-8cfcbddcd06f818b)

### observed_connections-004856

```text
(config-router-af-topology)# default-metric <number:1..16777214> <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x34278C38 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF default metric。

[条件 C-c01d7b542626bf00](../../evidence/conditions-sets-074.md#c-c01d7b542626bf00) · [参数 P-7efb2deb076eb971](../../evidence/parameters-sets-010.md#p-7efb2deb076eb971)

### observed_connections-005030

```text
(config-router-af-topology)# discard-route <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 11 `；EOL ` RVA 0x348B78F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a94d0d67627a16e4](../../evidence/conditions-sets-065.md#c-a94d0d67627a16e4) · [缺口 G-eaf72eff1e03b5d2](../../evidence/gaps-sets-008.md#g-eaf72eff1e03b5d2) · [状态效果 S-69416b50bf09782c](../../evidence/state_effects-sets-023.md#s-69416b50bf09782c)

### observed_connections-004853

```text
(config-router-af-topology)# distance <number:1..255> <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34277A70 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Administrative distance。

[条件 C-0a6d67ab33dfca26](../../evidence/conditions-sets-004.md#c-0a6d67ab33dfca26) · [参数 P-30c1a49c77381156](../../evidence/parameters-sets-004.md#p-30c1a49c77381156)

### observed_connections-004879

```text
(config-router-af-topology)# distance ospf <cr>
```

Handler ` RVA 0xFC6D2A0 `；selector ` 0 `；EOL ` RVA 0x348C0E30 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76354f09e1f6abc0](../../evidence/conditions-sets-046.md#c-76354f09e1f6abc0)

### observed_connections-004895

```text
(config-router-af-topology)# distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3427C6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-30a5be791d80a30d](../../evidence/conditions-sets-019.md#c-30a5be791d80a30d) · [状态效果 S-18eee92931165def](../../evidence/state_effects-sets-006.md#s-18eee92931165def)

### observed_connections-005037

```text
(config-router-af-topology)# distribute-list out <?router_action_proc_vpn@5555897d0660> <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3427C6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a1d18c576258fe8f](../../evidence/conditions-sets-062.md#c-a1d18c576258fe8f) · [缺口 G-32a1d7dc04a3b678](../../evidence/gaps-sets-002.md#g-32a1d7dc04a3b678) · [状态效果 S-63b4d5eb543d8424](../../evidence/state_effects-sets-021.md#s-63b4d5eb543d8424)

### observed_connections-004858

```text
(config-router-af-topology)# domain-id <address> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 9 `；EOL ` RVA 0x348B3FA8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF domain ID in IP address format。

[条件 C-e6a6cc9f1a80a30a](../../evidence/conditions-sets-089.md#c-e6a6cc9f1a80a30a) · [参数 P-dbbc6d0676eb9ab3](../../evidence/parameters-sets-017.md#p-dbbc6d0676eb9ab3)

### observed_connections-005038

```text
(config-router-af-topology)# domain-id type 0005 value <hex-data> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 9 `；EOL ` RVA 0x348B3FA8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexdata ` OSPF domain ID ext. community value in Hex。

[条件 C-7a6f32a770afce86](../../evidence/conditions-sets-047.md#c-7a6f32a770afce86) · [缺口 G-4f6c7c8b93c05f9f](../../evidence/gaps-sets-003.md#g-4f6c7c8b93c05f9f) · [参数 P-b05e50a936882cfc](../../evidence/parameters-sets-013.md#p-b05e50a936882cfc) · [状态效果 S-8e9b632bc434718d](../../evidence/state_effects-sets-030.md#s-8e9b632bc434718d)

### observed_connections-004816

```text
(config-router-af-topology)# domain-tag <number:1..4294967295> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 10 `；EOL ` RVA 0x348B3EC8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF domain tag - 32-bit value。

[条件 C-556d99d5f8baa549](../../evidence/conditions-sets-034.md#c-556d99d5f8baa549) · [参数 P-a4b60a248c055fc2](../../evidence/parameters-sets-013.md#p-a4b60a248c055fc2)

### observed_connections-004837

```text
(config-router-af-topology)# event-log <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 22 `；EOL ` RVA 0x348B6CE8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-291fbdab516f6b88](../../evidence/conditions-sets-016.md#c-291fbdab516f6b88)

### observed_connections-004817

```text
(config-router-af-topology)# exit-router-topology <cr>
```

Handler ` RVA 0xE1A7140 `；selector ` 0 `；EOL ` RVA 0x34276878 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f10ba3a58c55f34f](../../evidence/conditions-sets-093.md#c-f10ba3a58c55f34f)

### observed_connections-004946

```text
(config-router-af-topology)# ignore lsa mospf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 3 `；EOL ` RVA 0x348B61F8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920)

### observed_connections-004826

```text
(config-router-af-topology)# ignore-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 27 `；EOL ` RVA 0x34B971A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3)

### observed_connections-004870

```text
(config-router-af-topology)# interface-id snmp-if-index <cr>
```

Handler ` RVA 0xFC6E310 `；selector ` 0 `；EOL ` RVA 0x348B5EC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920)

### observed_connections-005015

```text
(config-router-af-topology)# ip route priority high tag <number:1..4294967295> <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 66 `；EOL ` RVA 0x34B96870 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` tag value。

[条件 C-26542596c01cbfa3](../../evidence/conditions-sets-015.md#c-26542596c01cbfa3) · [参数 P-a9655d54996f2cdf](../../evidence/parameters-sets-013.md#p-a9655d54996f2cdf) · [状态效果 S-984a633900cb7fac](../../evidence/state_effects-sets-032.md#s-984a633900cb7fac)

### observed_connections-004827

```text
(config-router-af-topology)# ispf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 16 `；EOL ` RVA 0x348B6490 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920)

### observed_connections-004911

```text
(config-router-af-topology)# limit retransmissions <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 13 `；EOL ` RVA 0x348B8DB8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-452a6e9bd44b3e95](../../evidence/conditions-sets-027.md#c-452a6e9bd44b3e95)

### observed_connections-005031

```text
(config-router-af-topology)# local-rib-criteria <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 26 `；EOL ` RVA 0x348B7D10 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a94d0d67627a16e4](../../evidence/conditions-sets-065.md#c-a94d0d67627a16e4) · [缺口 G-cdec0324f6e2773d](../../evidence/gaps-sets-007.md#g-cdec0324f6e2773d) · [状态效果 S-b6582c553eba0d3b](../../evidence/state_effects-sets-039.md#s-b6582c553eba0d3b)

### observed_connections-004836

```text
(config-router-af-topology)# log-adjacency-changes <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 2 `；EOL ` RVA 0x348B7480 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920)

### observed_connections-004915

```text
(config-router-af-topology)# max-lsa <number:1..4294967294> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 18 `；EOL ` RVA 0x348B8478 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of non self-generated LSAs this process can receive。

[条件 C-4f27c355a00a6655](../../evidence/conditions-sets-031.md#c-4f27c355a00a6655) · [参数 P-d4c8d0174a42537e](../../evidence/parameters-sets-016.md#p-d4c8d0174a42537e)

### observed_connections-004822

```text
(config-router-af-topology)# max-metric intra-area <number:1..16777214> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 5 `；EOL ` RVA 0x348B47F8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric value。

[条件 C-42c6b39315298231](../../evidence/conditions-sets-026.md#c-42c6b39315298231) · [参数 P-9b8229e1100d68e2](../../evidence/parameters-sets-012.md#p-9b8229e1100d68e2)

### observed_connections-004878

```text
(config-router-af-topology)# max-metric router-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 12 `；EOL ` RVA 0x348B4D20 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ff11218e1b67bcf](../../evidence/conditions-sets-043.md#c-6ff11218e1b67bcf)

### observed_connections-005034

```text
(config-router-af-topology)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xE1E26B0 `；selector ` 0 `；EOL ` RVA 0x3427BFA0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-caf08cdb3679310a](../../evidence/conditions-sets-078.md#c-caf08cdb3679310a) · [缺口 G-6043991c32c803c1](../../evidence/gaps-sets-004.md#g-6043991c32c803c1) · [参数 P-97129878eddcbd83](../../evidence/parameters-sets-012.md#p-97129878eddcbd83)

### observed_connections-004900

```text
(config-router-af-topology)# metric <number:1..16777214> <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 89 `；EOL ` RVA 0x34B97F28 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default metric。

[条件 C-8f77bcad388ac8b1](../../evidence/conditions-sets-056.md#c-8f77bcad388ac8b1) · [参数 P-0cf609f067aa46a3](../../evidence/parameters-sets-001.md#p-0cf609f067aa46a3) · [状态效果 S-45a7148fad906cbc](../../evidence/state_effects-sets-015.md#s-45a7148fad906cbc)

### observed_connections-004838

```text
(config-router-af-topology)# multicast-intact <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 49 `；EOL ` RVA 0x348BA9E0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e)

### observed_connections-005032

```text
(config-router-af-topology)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x34276B88 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2cc6eee56aa4751](../../evidence/conditions-sets-087.md#c-e2cc6eee56aa4751) · [缺口 G-d7422e053cfc4fdc](../../evidence/gaps-sets-007.md#g-d7422e053cfc4fdc) · [状态效果 S-dabd8dfee52885fc](../../evidence/state_effects-sets-046.md#s-dabd8dfee52885fc)

### observed_connections-005033

```text
(config-router-af-topology)# neighbor <cr>
```

Handler ` RVA 0xE1F37E0 `；selector ` 0 `；EOL ` RVA 0x348BEDA0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9dcc9151e057b413](../../evidence/conditions-sets-061.md#c-9dcc9151e057b413) · [缺口 G-d7422e053cfc4fdc](../../evidence/gaps-sets-007.md#g-d7422e053cfc4fdc) · [状态效果 S-dabd8dfee52885fc](../../evidence/state_effects-sets-046.md#s-dabd8dfee52885fc)

### observed_connections-004825

```text
(config-router-af-topology)# never-set-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 28 `；EOL ` RVA 0x34B96EC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3)

### observed_connections-004962

```text
(config-router-af-topology)# no adjacency stagger <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 25 `；EOL ` RVA 0x348B6880 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f5475ac57a4f0b43](../../evidence/conditions-sets-095.md#c-f5475ac57a4f0b43) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004924

```text
(config-router-af-topology)# no advertise passive-only <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 84 `；EOL ` RVA 0x34B96BD0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004956

```text
(config-router-af-topology)# no area <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 11 `；EOL ` RVA 0x348BE738 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-dbf761579fbecabc](../../evidence/conditions-sets-085.md#c-dbf761579fbecabc) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004979

```text
(config-router-af-topology)# no area <address> authentication <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 6 `；EOL ` RVA 0x348BAF88 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-ee059b97133752a5](../../evidence/conditions-sets-092.md#c-ee059b97133752a5) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-b809d2d88e28f69e](../../evidence/state_effects-sets-039.md#s-b809d2d88e28f69e)

### observed_connections-005005

```text
(config-router-af-topology)# no area <address> capability default-exclusion <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 14 `；EOL ` RVA 0x348BB290 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-0cc897d098523ce2](../../evidence/conditions-sets-005.md#c-0cc897d098523ce2) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-ca8c6111272d4830](../../evidence/state_effects-sets-043.md#s-ca8c6111272d4830)

### observed_connections-004980

```text
(config-router-af-topology)# no area <address> default-cost <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 5 `；EOL ` RVA 0x348BB5C0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-d299f3c6f551d1ee](../../evidence/conditions-sets-081.md#c-d299f3c6f551d1ee) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005028

```text
(config-router-af-topology)# no area <address> filter-list prefix <string> in <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 12 `；EOL ` RVA 0x348BCDD0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` string ` Name of an IP prefix-list。

[条件 C-7d6e3710ca6b0d4d](../../evidence/conditions-sets-049.md#c-7d6e3710ca6b0d4d) · [参数 P-e769b024470f7941](../../evidence/parameters-sets-017.md#p-e769b024470f7941) · [状态效果 S-99bacff95c1b724b](../../evidence/state_effects-sets-033.md#s-99bacff95c1b724b)

### observed_connections-004995

```text
(config-router-af-topology)# no area <address> nssa <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 3 `；EOL ` RVA 0x348BC528 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-4ef469467590d2f0](../../evidence/conditions-sets-031.md#c-4ef469467590d2f0) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004985

```text
(config-router-af-topology)# no area <address> packet-size <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 16 `；EOL ` RVA 0x348BB8D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-8c3df10179ba20f4](../../evidence/conditions-sets-054.md#c-8c3df10179ba20f4) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005016

```text
(config-router-af-topology)# no area <address> range <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 2 `；EOL ` RVA 0x348BC948 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP address to match；` address ` IP mask for address。

[条件 C-2053b31f904f0e60](../../evidence/conditions-sets-013.md#c-2053b31f904f0e60) · [参数 P-fbb7eb8a1cb44d99](../../evidence/parameters-sets-019.md#p-fbb7eb8a1cb44d99) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005025

```text
(config-router-af-topology)# no area <address> sham-link <address> <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 13 `；EOL ` RVA 0x348BE398 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` IP addr associated with sham-link source；` address ` IP addr associated with sham-link destination。

[条件 C-b883815e7e9a4783](../../evidence/conditions-sets-071.md#c-b883815e7e9a4783) · [参数 P-fe564c79ac44a63c](../../evidence/parameters-sets-019.md#p-fe564c79ac44a63c) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004990

```text
(config-router-af-topology)# no area <address> stub <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 4 `；EOL ` RVA 0x348BBC80 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format。

[条件 C-8ff34d44ae6ba9c9](../../evidence/conditions-sets-056.md#c-8ff34d44ae6ba9c9) · [参数 P-a2a28d144db8fcb9](../../evidence/parameters-sets-012.md#p-a2a28d144db8fcb9) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005009

```text
(config-router-af-topology)# no area <address> virtual-link <address> <cr>
```

Handler ` RVA 0xFC633D0 `；selector ` 1 `；EOL ` RVA 0x348BDAB0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` OSPF area ID in IP address format；` address ` ID (IP addr) associated with virtual link neighbor。

[条件 C-1526a5f74077fd89](../../evidence/conditions-sets-008.md#c-1526a5f74077fd89) · [参数 P-844fb23e9002fdb6](../../evidence/parameters-sets-010.md#p-844fb23e9002fdb6) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004875

```text
(config-router-af-topology)# no auto-cost <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 0 `；EOL ` RVA 0x348B80B8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004918

```text
(config-router-af-topology)# no autoroute-exclude <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 48 `；EOL ` RVA 0x348BA6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b1ecbda62c32da0](../../evidence/conditions-sets-054.md#c-8b1ecbda62c32da0) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004974

```text
(config-router-af-topology)# no capability opaque <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 4 `；EOL ` RVA 0x348BA258 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f78818f9a84e39a2](../../evidence/conditions-sets-096.md#c-f78818f9a84e39a2) · [状态效果 S-cea5f1cca9e9f1c6](../../evidence/state_effects-sets-044.md#s-cea5f1cca9e9f1c6)

### observed_connections-004934

```text
(config-router-af-topology)# no compatible rfc1583 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 6 `；EOL ` RVA 0x348B55E0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004941

```text
(config-router-af-topology)# no compatible rfc1587 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 7 `；EOL ` RVA 0x348B58F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-af1df3eeeb0f42e6](../../evidence/conditions-sets-068.md#c-af1df3eeeb0f42e6) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004948

```text
(config-router-af-topology)# no compatible rfc5243 <cr>
```

Handler ` RVA 0xFC6DF20 `；selector ` 8 `；EOL ` RVA 0x348B5BC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dd2ffbf9ad0b3962](../../evidence/conditions-sets-085.md#c-dd2ffbf9ad0b3962) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004839

```text
(config-router-af-topology)# no context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e07495ed56793ecc](../../evidence/conditions-sets-086.md#c-e07495ed56793ecc) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004923

```text
(config-router-af-topology)# no default-information originate <cr>
```

Handler ` RVA 0xE1F1F70 `；selector ` 0 `；EOL ` RVA 0x34278370 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-314c82090fe484ba](../../evidence/conditions-sets-019.md#c-314c82090fe484ba) · [状态效果 S-d46859b9818614f4](../../evidence/state_effects-sets-045.md#s-d46859b9818614f4)

### observed_connections-004849

```text
(config-router-af-topology)# no default-metric <cr>
```

Handler ` RVA 0xE1F35A0 `；selector ` 0 `；EOL ` RVA 0x34278C38 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1e2fd81fb0004667](../../evidence/conditions-sets-012.md#c-1e2fd81fb0004667) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004862

```text
(config-router-af-topology)# no distance <cr>
```

Handler ` RVA 0xE1E3290 `；selector ` 1 `；EOL ` RVA 0x34277A70 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a9b5e957fa0056f5](../../evidence/conditions-sets-065.md#c-a9b5e957fa0056f5) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004927

```text
(config-router-af-topology)# no distance ospf <cr>
```

Handler ` RVA 0xFC6D2A0 `；selector ` 0 `；EOL ` RVA 0x348C0E30 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5a1dab5d0d4717eb](../../evidence/conditions-sets-035.md#c-5a1dab5d0d4717eb) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004958

```text
(config-router-af-topology)# no distribute-list in <cr>
```

Handler ` RVA 0xE1EE180 `；selector ` 0 `；EOL ` RVA 0x3427C6D8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-30a5be791d80a30d](../../evidence/conditions-sets-019.md#c-30a5be791d80a30d) · [状态效果 S-87f413007606dab1](../../evidence/state_effects-sets-029.md#s-87f413007606dab1)

### observed_connections-004871

```text
(config-router-af-topology)# no domain-id <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 9 `；EOL ` RVA 0x348B3FA8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e1679f887cf9e2dc](../../evidence/conditions-sets-087.md#c-e1679f887cf9e2dc) · [状态效果 S-bce9bd35791e9cfe](../../evidence/state_effects-sets-040.md#s-bce9bd35791e9cfe)

### observed_connections-004823

```text
(config-router-af-topology)# no domain-tag <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 10 `；EOL ` RVA 0x348B3EC8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3be3fab7feea5f75](../../evidence/conditions-sets-023.md#c-3be3fab7feea5f75) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004905

```text
(config-router-af-topology)# no event-log <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 22 `；EOL ` RVA 0x348B6CE8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-291fbdab516f6b88](../../evidence/conditions-sets-016.md#c-291fbdab516f6b88) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004991

```text
(config-router-af-topology)# no ignore lsa mospf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 3 `；EOL ` RVA 0x348B61F8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004864

```text
(config-router-af-topology)# no ignore-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 27 `；EOL ` RVA 0x34B971A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004936

```text
(config-router-af-topology)# no interface-id snmp-if-index <cr>
```

Handler ` RVA 0xFC6E310 `；selector ` 0 `；EOL ` RVA 0x348B5EC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005014

```text
(config-router-af-topology)# no ip route priority high tag <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 66 `；EOL ` RVA 0x34B96870 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-731e49052faff49d](../../evidence/conditions-sets-045.md#c-731e49052faff49d) · [状态效果 S-942412658d514f96](../../evidence/state_effects-sets-031.md#s-942412658d514f96)

### observed_connections-004873

```text
(config-router-af-topology)# no ispf <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 16 `；EOL ` RVA 0x348B6490 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004969

```text
(config-router-af-topology)# no limit retransmissions <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 13 `；EOL ` RVA 0x348B8DB8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-452a6e9bd44b3e95](../../evidence/conditions-sets-027.md#c-452a6e9bd44b3e95) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004904

```text
(config-router-af-topology)# no log-adjacency-changes <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 2 `；EOL ` RVA 0x348B7480 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004887

```text
(config-router-af-topology)# no max-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 18 `；EOL ` RVA 0x348B8478 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e6b9ff240e388d71](../../evidence/conditions-sets-089.md#c-e6b9ff240e388d71) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004843

```text
(config-router-af-topology)# no max-metric intra-area <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 5 `；EOL ` RVA 0x348B47F8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05997d2f9a14e85e](../../evidence/conditions-sets-003.md#c-05997d2f9a14e85e) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004945

```text
(config-router-af-topology)# no max-metric router-lsa <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 12 `；EOL ` RVA 0x348B4D20 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6ff11218e1b67bcf](../../evidence/conditions-sets-043.md#c-6ff11218e1b67bcf) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004906

```text
(config-router-af-topology)# no metric <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 89 `；EOL ` RVA 0x34B97F28 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-27358fc06c154ce7](../../evidence/conditions-sets-015.md#c-27358fc06c154ce7) · [状态效果 S-f6685a8fce8309b0](../../evidence/state_effects-sets-052.md#s-f6685a8fce8309b0)

### observed_connections-004917

```text
(config-router-af-topology)# no multicast-intact <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 49 `；EOL ` RVA 0x348BA9E0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004859

```text
(config-router-af-topology)# no never-set-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 28 `；EOL ` RVA 0x34B96EC0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-70b43caf8c0fb5b3](../../evidence/conditions-sets-044.md#c-70b43caf8c0fb5b3) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004820

```text
(config-router-af-topology)# no packet-size <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 50 `；EOL ` RVA 0x348B3920 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d7dfe1059cb50fd2](../../evidence/conditions-sets-083.md#c-d7dfe1059cb50fd2) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004850

```text
(config-router-af-topology)# no prc-interval <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 30 `；EOL ` RVA 0x34B962E8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-38b5190916d903ac](../../evidence/conditions-sets-022.md#c-38b5190916d903ac) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005002

```text
(config-router-af-topology)# no prefix-priority high route-map <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 28 `；EOL ` RVA 0x348B9B68 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fe8c7598131d12ba](../../evidence/conditions-sets-098.md#c-fe8c7598131d12ba) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004903

```text
(config-router-af-topology)# no prefix-suppression <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 27 `；EOL ` RVA 0x348B9E48 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004818

```text
(config-router-af-topology)# no priority <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 19 `；EOL ` RVA 0x348B34A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d39e8ff578d3f7ad](../../evidence/conditions-sets-082.md#c-d39e8ff578d3f7ad) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004845

```text
(config-router-af-topology)# no priority <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 85 `；EOL ` RVA 0x34B95A50 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87e92c66b83204ef](../../evidence/conditions-sets-053.md#c-87e92c66b83204ef) · [状态效果 S-a604a9eb5635f549](../../evidence/state_effects-sets-035.md#s-a604a9eb5635f549)

### observed_connections-004889

```text
(config-router-af-topology)# no process-min-time percent <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 21 `；EOL ` RVA 0x348B90C8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6200d66cf296e681](../../evidence/conditions-sets-038.md#c-6200d66cf296e681) · [状态效果 S-f70a9ae9228f38f6](../../evidence/state_effects-sets-052.md#s-f70a9ae9228f38f6)

### observed_connections-004937

```text
(config-router-af-topology)# no queue-depth hello <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 20 `；EOL ` RVA 0x348B5250 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-37658eb8e2351f7b](../../evidence/conditions-sets-022.md#c-37658eb8e2351f7b) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004842

```text
(config-router-af-topology)# no router-id <cr>
```

Handler ` RVA 0xFC6D990 `；selector ` 0 `；EOL ` RVA 0x348B3548 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f384c3cd5d258905](../../evidence/conditions-sets-094.md#c-f384c3cd5d258905) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004876

```text
(config-router-af-topology)# no set-attached-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 26 `；EOL ` RVA 0x34B97AF8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-649a4b0aa7556c6b](../../evidence/conditions-sets-039.md#c-649a4b0aa7556c6b) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004877

```text
(config-router-af-topology)# no set-overload-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 25 `；EOL ` RVA 0x34B97518 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1bc2114efb3e4d38](../../evidence/conditions-sets-011.md#c-1bc2114efb3e4d38) · [状态效果 S-0f1ee96d6eb11a8e](../../evidence/state_effects-sets-004.md#s-0f1ee96d6eb11a8e)

### observed_connections-004894

```text
(config-router-af-topology)# no shutdown <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 24 `；EOL ` RVA 0x348B9770 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004928

```text
(config-router-af-topology)# no snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-005021

```text
(config-router-af-topology)# no snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-5a416169412196ba](../../evidence/conditions-sets-035.md#c-5a416169412196ba) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-c97f0f2cf9ef3e3c](../../evidence/state_effects-sets-043.md#s-c97f0f2cf9ef3e3c)

### observed_connections-005020

```text
(config-router-af-topology)# no snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-c27aae31069e8d90](../../evidence/conditions-sets-075.md#c-c27aae31069e8d90) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-71e3d05ef0881ea7](../../evidence/state_effects-sets-024.md#s-71e3d05ef0881ea7)

### observed_connections-004861

```text
(config-router-af-topology)# no spf-interval <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 29 `；EOL ` RVA 0x34B95E48 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6c962fa0cc7b83c8](../../evidence/conditions-sets-042.md#c-6c962fa0cc7b83c8) · [状态效果 S-e0934a4a4b19f25d](../../evidence/state_effects-sets-048.md#s-e0934a4a4b19f25d)

### observed_connections-004957

```text
(config-router-af-topology)# no statistics rib-timings <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 17 `；EOL ` RVA 0x348B7150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004987

```text
(config-router-af-topology)# no summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x3427B150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-f94f9efc0e1d02cf](../../evidence/conditions-sets-096.md#c-f94f9efc0e1d02cf) · [参数 P-19f6a7c1aa1c9c3a](../../evidence/parameters-sets-002.md#p-19f6a7c1aa1c9c3a) · [状态效果 S-22f2875fff6c9969](../../evidence/state_effects-sets-008.md#s-22f2875fff6c9969)

### observed_connections-004925

```text
(config-router-af-topology)# no summary-prefix <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x3427B730 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP summary address。

[条件 C-3920aa7b0ba0fa96](../../evidence/conditions-sets-022.md#c-3920aa7b0ba0fa96) · [参数 P-53d78b0d3a9718f3](../../evidence/parameters-sets-007.md#p-53d78b0d3a9718f3) · [状态效果 S-22f2875fff6c9969](../../evidence/state_effects-sets-008.md#s-22f2875fff6c9969)

### observed_connections-004938

```text
(config-router-af-topology)# no timers basic <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x3427D0D0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2d4f117d4a36a7d3](../../evidence/conditions-sets-018.md#c-2d4f117d4a36a7d3) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004952

```text
(config-router-af-topology)# no timers lsa arrival <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 8 `；EOL ` RVA 0x348BF9C8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8598e43f2981a77b](../../evidence/conditions-sets-052.md#c-8598e43f2981a77b) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004898

```text
(config-router-af-topology)# no timers lsa-arrival <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 1 `；EOL ` RVA 0x348BFF58 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b31fbd46425da34b](../../evidence/conditions-sets-069.md#c-b31fbd46425da34b) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004888

```text
(config-router-af-topology)# no timers lsa-group-pacing <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 2 `；EOL ` RVA 0x348BF9F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-45cc56af86f0a78f](../../evidence/conditions-sets-027.md#c-45cc56af86f0a78f) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004892

```text
(config-router-af-topology)# no timers lsa-interval <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 0 `；EOL ` RVA 0x348BFCB8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-90e01536d68d6f8e](../../evidence/conditions-sets-056.md#c-90e01536d68d6f8e) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004967

```text
(config-router-af-topology)# no timers pacing flood <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 3 `；EOL ` RVA 0x348C0500 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49659435b0155479](../../evidence/conditions-sets-029.md#c-49659435b0155479) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004963

```text
(config-router-af-topology)# no timers pacing lsa-group <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 2 `；EOL ` RVA 0x348C0498 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-70aa0b72c940a689](../../evidence/conditions-sets-044.md#c-70aa0b72c940a689) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004971

```text
(config-router-af-topology)# no timers pacing retransmission <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 4 `；EOL ` RVA 0x348C07A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b76641f948d10a8b](../../evidence/conditions-sets-071.md#c-b76641f948d10a8b) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004998

```text
(config-router-af-topology)# no timers throttle lsa <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 9 `；EOL ` RVA 0x348BF608 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-67b6bd090fce6cb1](../../evidence/conditions-sets-040.md#c-67b6bd090fce6cb1) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004994

```text
(config-router-af-topology)# no timers throttle spf <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 5 `；EOL ` RVA 0x348BF210 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8f39c71d113dc4d8](../../evidence/conditions-sets-055.md#c-8f39c71d113dc4d8) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004977

```text
(config-router-af-topology)# no traffic-share min across-interfaces <cr>
```

Handler ` RVA 0xE1FA2E0 `；selector ` 0 `；EOL ` RVA 0x34277568 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-99e26537a5dcb053](../../evidence/conditions-sets-059.md#c-99e26537a5dcb053) · [状态效果 S-0a045ea291337430](../../evidence/state_effects-sets-003.md#s-0a045ea291337430)

### observed_connections-004965

```text
(config-router-af-topology)# no ttl-security all-interfaces <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 23 `；EOL ` RVA 0x348B9488 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-20e1d5808aecd8eb](../../evidence/conditions-sets-013.md#c-20e1d5808aecd8eb) · [状态效果 S-69334997d7e7dd38](../../evidence/state_effects-sets-022.md#s-69334997d7e7dd38)

### observed_connections-004815

```text
(config-router-af-topology)# packet-size <number:576..10000> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 50 `；EOL ` RVA 0x348B3920 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF Router Mode Packet Size。

[条件 C-1f5755c09c789a79](../../evidence/conditions-sets-012.md#c-1f5755c09c789a79) · [参数 P-75ad99ca2c869b5e](../../evidence/parameters-sets-009.md#p-75ad99ca2c869b5e)

### observed_connections-004868

```text
(config-router-af-topology)# prc-interval <number:1..120> <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 30 `；EOL ` RVA 0x34B962E8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum PRC interval in seconds。

[条件 C-41f35e74923b37cd](../../evidence/conditions-sets-026.md#c-41f35e74923b37cd) · [参数 P-141255102f62cb90](../../evidence/parameters-sets-002.md#p-141255102f62cb90) · [状态效果 S-20f6707c28576125](../../evidence/state_effects-sets-007.md#s-20f6707c28576125)

### observed_connections-005004

```text
(config-router-af-topology)# prefix-priority high route-map <string> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 28 `；EOL ` RVA 0x348B9B68 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route-map name。

[条件 C-e9ca6e2d2bc8634e](../../evidence/conditions-sets-090.md#c-e9ca6e2d2bc8634e) · [参数 P-37c3482f0e0e48d9](../../evidence/parameters-sets-005.md#p-37c3482f0e0e48d9)

### observed_connections-004835

```text
(config-router-af-topology)# prefix-suppression <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 27 `；EOL ` RVA 0x348B9E48 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e)

### observed_connections-004814

```text
(config-router-af-topology)# priority <number:0..127> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 19 `；EOL ` RVA 0x348B34A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` OSPF topology priority。

[条件 C-5b6c455135cb2be6](../../evidence/conditions-sets-036.md#c-5b6c455135cb2be6) · [参数 P-e2ee5566abd90c04](../../evidence/parameters-sets-017.md#p-e2ee5566abd90c04)

### observed_connections-004846

```text
(config-router-af-topology)# priority <number:0..127> <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 85 `；EOL ` RVA 0x34B95A50 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` priority value。

[条件 C-331c1dbeedbe381a](../../evidence/conditions-sets-020.md#c-331c1dbeedbe381a) · [参数 P-a19b5db4151c5923](../../evidence/parameters-sets-012.md#p-a19b5db4151c5923) · [状态效果 S-1f1232b5c6ec6c42](../../evidence/state_effects-sets-007.md#s-1f1232b5c6ec6c42)

### observed_connections-004831

```text
(config-router-af-topology)# process-min-time percent <number:1..100> <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 21 `；EOL ` RVA 0x348B90C8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum CPU quantum。

[条件 C-895a2288c292a688](../../evidence/conditions-sets-053.md#c-895a2288c292a688) · [参数 P-b4eaa02c45eec987](../../evidence/parameters-sets-014.md#p-b4eaa02c45eec987) · [状态效果 S-da255e037a224057](../../evidence/state_effects-sets-046.md#s-da255e037a224057)

### observed_connections-004940

```text
(config-router-af-topology)# queue-depth hello unlimited <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 20 `；EOL ` RVA 0x348B5250 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6bb23e6b6c217a21](../../evidence/conditions-sets-042.md#c-6bb23e6b6c217a21) · [状态效果 S-de8f62979466982f](../../evidence/state_effects-sets-047.md#s-de8f62979466982f)

### observed_connections-005036

```text
(config-router-af-topology)# redistribute <?router_action_proc_vpn@5555897cd180> <cr>
```

Handler ` RVA 0xE1E4550 `；selector ` 0 `；EOL ` RVA 0x3427A420 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd8aaf4a2483b482](../../evidence/conditions-sets-073.md#c-bd8aaf4a2483b482) · [缺口 G-e2fdecea7ed8d709](../../evidence/gaps-sets-008.md#g-e2fdecea7ed8d709)

### observed_connections-005039

```text
(config-router-af-topology)# redistribute <?router_action_proc_vpn@5555897cd180> ip level-1 into level-1 route-map <string> <cr>
```

Handler ` RVA 0xCF982D0 `；selector ` 0 `；EOL ` RVA 0x3427AA78 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of the route-map。

[条件 C-9e7ee380c4b6966d](../../evidence/conditions-sets-061.md#c-9e7ee380c4b6966d) · [缺口 G-76397a1036941cec](../../evidence/gaps-sets-005.md#g-76397a1036941cec) · [参数 P-fdb644044523454b](../../evidence/parameters-sets-019.md#p-fdb644044523454b) · [状态效果 S-684ecc7cf2bfd924](../../evidence/state_effects-sets-022.md#s-684ecc7cf2bfd924)

### observed_connections-004848

```text
(config-router-af-topology)# router-id <address> <cr>
```

Handler ` RVA 0xFC6D990 `；selector ` 0 `；EOL ` RVA 0x348B3548 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` OSPF router-id in IP address format。

[条件 C-def3b4237b921b50](../../evidence/conditions-sets-086.md#c-def3b4237b921b50) · [参数 P-4d4e0794b2b19575](../../evidence/parameters-sets-006.md#p-4d4e0794b2b19575)

### observed_connections-004950

```text
(config-router-af-topology)# set-attached-bit route-map <string> <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 26 `；EOL ` RVA 0x34B97AF8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Route map name。

[条件 C-50207fdbfcb6d73d](../../evidence/conditions-sets-031.md#c-50207fdbfcb6d73d) · [参数 P-75d4f7089a253f4e](../../evidence/parameters-sets-009.md#p-75d4f7089a253f4e)

### observed_connections-004829

```text
(config-router-af-topology)# set-overload-bit <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 25 `；EOL ` RVA 0x34B97518 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9517eca0117ca45c](../../evidence/conditions-sets-058.md#c-9517eca0117ca45c) · [状态效果 S-b33c9bf776205c1c](../../evidence/state_effects-sets-038.md#s-b33c9bf776205c1c)

### observed_connections-004833

```text
(config-router-af-topology)# shutdown <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 24 `；EOL ` RVA 0x348B9770 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05e3fdff333e8a4e](../../evidence/conditions-sets-003.md#c-05e3fdff333e8a4e)

### observed_connections-004860

```text
(config-router-af-topology)# snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc)

### observed_connections-005013

```text
(config-router-af-topology)# snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-7f44ea3d5ff83041](../../evidence/conditions-sets-049.md#c-7f44ea3d5ff83041) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-8642eb04023b2323](../../evidence/state_effects-sets-028.md#s-8642eb04023b2323)

### observed_connections-005012

```text
(config-router-af-topology)# snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-6568ff0a78495959](../../evidence/conditions-sets-039.md#c-6568ff0a78495959) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-42394155f848a6f9](../../evidence/state_effects-sets-014.md#s-42394155f848a6f9)

### observed_connections-004874

```text
(config-router-af-topology)# spf-interval <number:1..120> <cr>
```

Handler ` RVA 0xFD3E520 `；selector ` 29 `；EOL ` RVA 0x34B95E48 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum interval between consecutive SPFs in seconds。

[条件 C-b05bb4c2298a9ba4](../../evidence/conditions-sets-068.md#c-b05bb4c2298a9ba4) · [参数 P-9886ebe28003d354](../../evidence/parameters-sets-012.md#p-9886ebe28003d354) · [状态效果 S-7cf4187a9948871b](../../evidence/state_effects-sets-026.md#s-7cf4187a9948871b)

### observed_connections-004893

```text
(config-router-af-topology)# statistics rib-timings <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 17 `；EOL ` RVA 0x348B7150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1ba43747181a920](../../evidence/conditions-sets-081.md#c-d1ba43747181a920)

### observed_connections-004929

```text
(config-router-af-topology)# summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x3427B150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-f94f9efc0e1d02cf](../../evidence/conditions-sets-096.md#c-f94f9efc0e1d02cf) · [参数 P-19f6a7c1aa1c9c3a](../../evidence/parameters-sets-002.md#p-19f6a7c1aa1c9c3a) · [状态效果 S-e7dbc2ed43e465a2](../../evidence/state_effects-sets-049.md#s-e7dbc2ed43e465a2)

### observed_connections-004954

```text
(config-router-af-topology)# summary-prefix <address> <address> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 21 `；EOL ` RVA 0x3427B730 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP summary address；` address ` Summary mask。

[条件 C-7efbeb43a4fa9c80](../../evidence/conditions-sets-049.md#c-7efbeb43a4fa9c80) · [参数 P-280b5f8a3e4e0eba](../../evidence/parameters-sets-003.md#p-280b5f8a3e4e0eba) · [状态效果 S-847ad286c73d9882](../../evidence/state_effects-sets-028.md#s-847ad286c73d9882)

### observed_connections-005035

```text
(config-router-af-topology)# summary-prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xE1DF4C0 `；selector ` 0 `；EOL ` RVA 0x3427B150 `。

模式根 ` RVA 0x34276780 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-1feb62a6b5adc1e3](../../evidence/conditions-sets-012.md#c-1feb62a6b5adc1e3) · [缺口 G-32c8ff95e419ea72](../../evidence/gaps-sets-002.md#g-32c8ff95e419ea72) · [参数 P-0b3909fa038a5699](../../evidence/parameters-sets-001.md#p-0b3909fa038a5699) · [状态效果 S-db8167d6e156353b](../../evidence/state_effects-sets-046.md#s-db8167d6e156353b)

### observed_connections-005007

```text
(config-router-af-topology)# timers basic <number:1..2147483> <number:1..2147483> <number:0..2147483> <cr>
```

Handler ` RVA 0xE1F2D60 `；selector ` 0 `；EOL ` RVA 0x3427D0D0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between updates for RIP；` unsigned_number ` Invalid；` unsigned_number ` Holddown。

[条件 C-7cf30590a1cbfe74](../../evidence/conditions-sets-048.md#c-7cf30590a1cbfe74) · [参数 P-8901884c70ef7fa7](../../evidence/parameters-sets-011.md#p-8901884c70ef7fa7)

### observed_connections-004886

```text
(config-router-af-topology)# timers lsa arrival <number:0..600000> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 8 `；EOL ` RVA 0x348BF9C8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in milliseconds between accepting the same LSA。

[条件 C-d59d23b56c5bb753](../../evidence/conditions-sets-082.md#c-d59d23b56c5bb753) · [参数 P-f9e5ce321dc67249](../../evidence/parameters-sets-019.md#p-f9e5ce321dc67249)

### observed_connections-004834

```text
(config-router-af-topology)# timers lsa-arrival <number:0..600> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 1 `；EOL ` RVA 0x348BFF58 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in sec between accepting the same LSA。

[条件 C-8d86e670380e37d9](../../evidence/conditions-sets-055.md#c-8d86e670380e37d9) · [参数 P-94222fb3c0769d06](../../evidence/parameters-sets-011.md#p-94222fb3c0769d06)

### observed_connections-004830

```text
(config-router-af-topology)# timers lsa-group-pacing <number:10..1800> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 2 `；EOL ` RVA 0x348BF9F0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval between group of LSA being refreshed or maxaged。

[条件 C-05528664895d3ce3](../../evidence/conditions-sets-002.md#c-05528664895d3ce3) · [参数 P-6dcd98c8a003249f](../../evidence/parameters-sets-009.md#p-6dcd98c8a003249f)

### observed_connections-004832

```text
(config-router-af-topology)# timers lsa-interval <number:0..600> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 0 `；EOL ` RVA 0x348BFCB8 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in sec between originating the same LSA。

[条件 C-17f279a808351b71](../../evidence/conditions-sets-009.md#c-17f279a808351b71) · [参数 P-83b879e29d31b7ec](../../evidence/parameters-sets-010.md#p-83b879e29d31b7ec)

### observed_connections-004908

```text
(config-router-af-topology)# timers pacing flood <number:5..100> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 3 `；EOL ` RVA 0x348C0500 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in msec to pace limit flooding on interface。

[条件 C-bee979fe764461cd](../../evidence/conditions-sets-074.md#c-bee979fe764461cd) · [参数 P-2dce82f3f2c06e1e](../../evidence/parameters-sets-004.md#p-2dce82f3f2c06e1e)

### observed_connections-004902

```text
(config-router-af-topology)# timers pacing lsa-group <number:10..1800> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 2 `；EOL ` RVA 0x348C0498 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval in sec between group of LSA being refreshed or maxaged。

[条件 C-c95caadfe4369f42](../../evidence/conditions-sets-078.md#c-c95caadfe4369f42) · [参数 P-2c2f1a13e5a1993b](../../evidence/parameters-sets-004.md#p-2c2f1a13e5a1993b)

### observed_connections-004914

```text
(config-router-af-topology)# timers pacing retransmission <number:5..200> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 4 `；EOL ` RVA 0x348C07A0 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The minimum interval in msec between neighbor retransmissions。

[条件 C-35db909486e333fd](../../evidence/conditions-sets-021.md#c-35db909486e333fd) · [参数 P-3e695a66a34d89ca](../../evidence/parameters-sets-005.md#p-3e695a66a34d89ca)

### observed_connections-005027

```text
(config-router-af-topology)# timers throttle lsa <number:0..600000> <number:1..600000> <number:1..600000> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 9 `；EOL ` RVA 0x348BF608 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay to generate first occurrence of LSA in milliseconds；` unsigned_number ` Minimum delay between originating the same LSA in milliseconds；` unsigned_number ` Maximum delay between originating the same LSA in milliseconds。

[条件 C-9d95cc0cb1cfe82c](../../evidence/conditions-sets-061.md#c-9d95cc0cb1cfe82c) · [参数 P-9a8b946d639d7b2d](../../evidence/parameters-sets-012.md#p-9a8b946d639d7b2d)

### observed_connections-005024

```text
(config-router-af-topology)# timers throttle spf <number:1..600000> <number:1..600000> <number:1..600000> <cr>
```

Handler ` RVA 0xFC67C30 `；selector ` 5 `；EOL ` RVA 0x348BF210 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay between receiving a change to SPF calculation in milliseconds；` unsigned_number ` Delay between first and second SPF calculation in milliseconds；` unsigned_number ` Maximum wait time in milliseconds for SPF calculations。

[条件 C-955550356cc69c5f](../../evidence/conditions-sets-058.md#c-955550356cc69c5f) · [参数 P-b34e967421b42d44](../../evidence/parameters-sets-014.md#p-b34e967421b42d44)

### observed_connections-004921

```text
(config-router-af-topology)# traffic-share min across-interfaces <cr>
```

Handler ` RVA 0xE1FA2E0 `；selector ` 0 `；EOL ` RVA 0x34277568 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-99e26537a5dcb053](../../evidence/conditions-sets-059.md#c-99e26537a5dcb053) · [状态效果 S-2606f1abeff147c8](../../evidence/state_effects-sets-009.md#s-2606f1abeff147c8)

### observed_connections-004910

```text
(config-router-af-topology)# ttl-security all-interfaces <cr>
```

Handler ` RVA 0xFC68900 `；selector ` 23 `；EOL ` RVA 0x348B9488 `。

模式根 ` RVA 0x34276780 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0dc2f163d685f526](../../evidence/conditions-sets-006.md#c-0dc2f163d685f526)

