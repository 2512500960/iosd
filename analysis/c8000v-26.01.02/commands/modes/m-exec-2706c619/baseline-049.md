# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-006669

```text
(exec)# show ipv6 mld ssm-map <cr>
```

Handler ` RVA 0x11625660 `；selector ` 5 `；EOL ` RVA 0x3554A478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a72383b5b9871bd](../../evidence/conditions-sets-060.md#c-9a72383b5b9871bd) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-006610

```text
(exec)# show ipv6 mld traffic <cr>
```

Handler ` RVA 0x11625660 `；selector ` 3 `；EOL ` RVA 0x3554A168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a72383b5b9871bd](../../evidence/conditions-sets-060.md#c-9a72383b5b9871bd) · [状态效果 S-43ec1695eed2982a](../../evidence/state_effects-sets-015.md#s-43ec1695eed2982a)

### path-006560

```text
(exec)# show ipv6 mrib client <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 1 `；EOL ` RVA 0x3554F618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-94d168eb5d18ab9e](../../evidence/state_effects-sets-032.md#s-94d168eb5d18ab9e)

### path-011332

```text
(exec)# show ipv6 mrib route <address> <address> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3554EFC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` source IP address；` address ` source IP address。

[条件 C-65e75d13ad3fec51](../../evidence/conditions-sets-039.md#c-65e75d13ad3fec51) · [参数 P-282323034f78b379](../../evidence/parameters-sets-003.md#p-282323034f78b379) · [状态效果 S-e0927ef7f5c5a72c](../../evidence/state_effects-sets-048.md#s-e0927ef7f5c5a72c)

### path-006656

```text
(exec)# show ipv6 mrib route <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x3554EB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-32313e0318335ac8](../../evidence/conditions-sets-020.md#c-32313e0318335ac8) · [状态效果 S-94d168eb5d18ab9e](../../evidence/state_effects-sets-032.md#s-94d168eb5d18ab9e)

### path-019175

```text
(exec)# show ipv6 mrib route <prefix:dynamic> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3554EFC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` group IP address/prefix length。

[条件 C-6b9cd7ccc082d4cc](../../evidence/conditions-sets-042.md#c-6b9cd7ccc082d4cc) · [缺口 G-b0ed31b6c0c42fae](../../evidence/gaps-sets-006.md#g-b0ed31b6c0c42fae) · [参数 P-1ec5be69b6d07b5c](../../evidence/parameters-sets-003.md#p-1ec5be69b6d07b5c) · [状态效果 S-94d168eb5d18ab9e](../../evidence/state_effects-sets-032.md#s-94d168eb5d18ab9e)

### path-009527

```text
(exec)# show ipv6 mrib route summary <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 3 `；EOL ` RVA 0x3554E800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-94d168eb5d18ab9e](../../evidence/state_effects-sets-032.md#s-94d168eb5d18ab9e)

### path-002626

```text
(exec)# show ipv6 mroute <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x3555E458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9191311256f7dfc](../../evidence/conditions-sets-071.md#c-b9191311256f7dfc) · [状态效果 S-3c677b6ec2cdce3a](../../evidence/state_effects-sets-013.md#s-3c677b6ec2cdce3a)

### path-006816

```text
(exec)# show ipv6 mroute active <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 18 `；EOL ` RVA 0x3555EC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55987220baad4093](../../evidence/conditions-sets-034.md#c-55987220baad4093) · [状态效果 S-39dca7b3116ffc0f](../../evidence/state_effects-sets-013.md#s-39dca7b3116ffc0f)

### path-006750

```text
(exec)# show ipv6 mroute count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 19 `；EOL ` RVA 0x3555E878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5655b8c20a1c583](../../evidence/conditions-sets-088.md#c-e5655b8c20a1c583) · [状态效果 S-5c7b2e2fe27bd591](../../evidence/state_effects-sets-020.md#s-5c7b2e2fe27bd591)

### path-002345

```text
(exec)# show ipv6 mtu <cr>
```

Handler ` RVA 0x12306750 `；selector ` 0 `；EOL ` RVA 0x357E5568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-9ade58edff80c14e](../../evidence/state_effects-sets-033.md#s-9ade58edff80c14e)

### path-002562

```text
(exec)# show ipv6 multicast <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 28 `；EOL ` RVA 0x3555F478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c425fa2dd43dd3e](../../evidence/conditions-sets-017.md#c-2c425fa2dd43dd3e) · [状态效果 S-980e7f32ae4b353c](../../evidence/state_effects-sets-032.md#s-980e7f32ae4b353c)

### path-011342

```text
(exec)# show ipv6 multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 29 `；EOL ` RVA 0x3555F698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Overlay group address。

[条件 C-9d35ab13682ac8bd](../../evidence/conditions-sets-061.md#c-9d35ab13682ac8bd) · [参数 P-b95907093bfeb6e7](../../evidence/parameters-sets-014.md#p-b95907093bfeb6e7) · [状态效果 S-c7e3bfc372bb2220](../../evidence/state_effects-sets-042.md#s-c7e3bfc372bb2220)

### path-009719

```text
(exec)# show ipv6 multicast rpf monitored <cr>
```

Handler ` RVA 0x11757B10 `；selector ` 0 `；EOL ` RVA 0x3555FAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9d35ab13682ac8bd](../../evidence/conditions-sets-061.md#c-9d35ab13682ac8bd) · [状态效果 S-980e7f32ae4b353c](../../evidence/state_effects-sets-032.md#s-980e7f32ae4b353c)

### path-011848

```text
(exec)# show ipv6 multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 61 `；EOL ` RVA 0x33A5E878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-4a4b3b45291b2ba0](../../evidence/parameters-sets-006.md#p-4a4b3b45291b2ba0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009515

```text
(exec)# show ipv6 multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 71 `；EOL ` RVA 0x33A5EB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011851

```text
(exec)# show ipv6 multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 69 `；EOL ` RVA 0x33A5EBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-7a939613dde89531](../../evidence/parameters-sets-010.md#p-7a939613dde89531) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006494

```text
(exec)# show ipv6 nd destination <cr>
```

Handler ` RVA 0x1231A4C0 `；selector ` 0 `；EOL ` RVA 0x35804F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cb5248408498e9b8](../../evidence/conditions-sets-078.md#c-cb5248408498e9b8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018971

```text
(exec)# show ipv6 nd destination <interface> <cr>
```

Handler ` RVA 0x1231A4C0 `；selector ` 0 `；EOL ` RVA 0x35804F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b0301100bac39bc8](../../evidence/conditions-sets-068.md#c-b0301100bac39bc8) · [缺口 G-4381617f18719c85](../../evidence/gaps-sets-003.md#g-4381617f18719c85) · [参数 P-7ae0df22657e867a](../../evidence/parameters-sets-010.md#p-7ae0df22657e867a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009522

```text
(exec)# show ipv6 nd on-link prefix <cr>
```

Handler ` RVA 0x1231A0A0 `；selector ` 0 `；EOL ` RVA 0x35804B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-192e142b809c1172](../../evidence/conditions-sets-010.md#c-192e142b809c1172) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022272

```text
(exec)# show ipv6 nd on-link prefix <interface> <cr>
```

Handler ` RVA 0x1231A0A0 `；selector ` 0 `；EOL ` RVA 0x35804B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70e285f4c743d66c](../../evidence/conditions-sets-044.md#c-70e285f4c743d66c) · [缺口 G-18e902eade06f31f](../../evidence/gaps-sets-001.md#g-18e902eade06f31f) · [参数 P-dfc0696ce9a77d8d](../../evidence/parameters-sets-017.md#p-dfc0696ce9a77d8d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011261

```text
(exec)# show ipv6 nd ra dns server <cr>
```

Handler ` RVA 0x1231C740 `；selector ` 0 `；EOL ` RVA 0x357F91E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fbb2f549eea15d00](../../evidence/conditions-sets-097.md#c-fbb2f549eea15d00) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024174

```text
(exec)# show ipv6 nd ra dns server <interface> <cr>
```

Handler ` RVA 0x1231C740 `；selector ` 0 `；EOL ` RVA 0x357F91E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f2faa34c3f7808c](../../evidence/conditions-sets-024.md#c-3f2faa34c3f7808c) · [缺口 G-78b0e01a2be3f8c3](../../evidence/gaps-sets-005.md#g-78b0e01a2be3f8c3) · [参数 P-e7a8dd76ed3149d2](../../evidence/parameters-sets-017.md#p-e7a8dd76ed3149d2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009521

```text
(exec)# show ipv6 nd ra dns-search-list <cr>
```

Handler ` RVA 0x1231C960 `；selector ` 0 `；EOL ` RVA 0x357F95A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18b33b177d6626a4](../../evidence/conditions-sets-010.md#c-18b33b177d6626a4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022271

```text
(exec)# show ipv6 nd ra dns-search-list <interface> <cr>
```

Handler ` RVA 0x1231C960 `；selector ` 0 `；EOL ` RVA 0x357F95A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-73328bd0e1601996](../../evidence/conditions-sets-045.md#c-73328bd0e1601996) · [缺口 G-0dee2d38018c29e0](../../evidence/gaps-sets-001.md#g-0dee2d38018c29e0) · [参数 P-acb6d8efd5df2a1d](../../evidence/parameters-sets-013.md#p-acb6d8efd5df2a1d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009543

```text
(exec)# show ipv6 nd ra nat64-prefix <cr>
```

Handler ` RVA 0x1231CBF0 `；selector ` 0 `；EOL ` RVA 0x357F9958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e1c0e63ba8367dd9](../../evidence/conditions-sets-087.md#c-e1c0e63ba8367dd9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022294

```text
(exec)# show ipv6 nd ra nat64-prefix <interface> <cr>
```

Handler ` RVA 0x1231CBF0 `；selector ` 0 `；EOL ` RVA 0x357F9958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5cdac64e7354dfef](../../evidence/conditions-sets-036.md#c-5cdac64e7354dfef) · [缺口 G-65461dcd9960958b](../../evidence/gaps-sets-004.md#g-65461dcd9960958b) · [参数 P-3dbae635c9f21eb6](../../evidence/parameters-sets-005.md#p-3dbae635c9f21eb6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022262

```text
(exec)# show ipv6 nd ra sessions <interface> <cr>
```

Handler ` RVA 0x1231CD10 `；selector ` 0 `；EOL ` RVA 0x357F8DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98b331fc3378ab7c](../../evidence/conditions-sets-059.md#c-98b331fc3378ab7c) · [缺口 G-cb715bb75440d3f3](../../evidence/gaps-sets-007.md#g-cb715bb75440d3f3) · [参数 P-4565dc2cb57f5f83](../../evidence/parameters-sets-006.md#p-4565dc2cb57f5f83) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009560

```text
(exec)# show ipv6 nd ra specific-route <cr>
```

Handler ` RVA 0x1231CC80 `；selector ` 0 `；EOL ` RVA 0x357F9CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e63529119b22309](../../evidence/conditions-sets-012.md#c-1e63529119b22309) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022319

```text
(exec)# show ipv6 nd ra specific-route <interface> <cr>
```

Handler ` RVA 0x1231CC80 `；selector ` 0 `；EOL ` RVA 0x357F9CE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d34dda3830b897a2](../../evidence/conditions-sets-081.md#c-d34dda3830b897a2) · [缺口 G-cd9895ce2b1c9a9a](../../evidence/gaps-sets-007.md#g-cd9895ce2b1c9a9a) · [参数 P-f5816ff1baafe475](../../evidence/parameters-sets-018.md#p-f5816ff1baafe475) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006419

```text
(exec)# show ipv6 nd suppress <cr>
```

Handler ` RVA 0x136B3070 `；selector ` 0 `；EOL ` RVA 0x35C058E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06dab21e684c5791](../../evidence/conditions-sets-003.md#c-06dab21e684c5791) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002509

```text
(exec)# show ipv6 neighbors <cr>
```

Handler ` RVA 0x12312460 `；selector ` 0 `；EOL ` RVA 0x35802578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97ca6ad9cfbfa7d7](../../evidence/conditions-sets-059.md#c-97ca6ad9cfbfa7d7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014793

```text
(exec)# show ipv6 neighbors <interface> <cr>
```

Handler ` RVA 0x12312460 `；selector ` 0 `；EOL ` RVA 0x35802578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e8e68c117c2ef168](../../evidence/conditions-sets-090.md#c-e8e68c117c2ef168) · [缺口 G-edb29b1b5b952ecb](../../evidence/gaps-sets-008.md#g-edb29b1b5b952ecb) · [参数 P-ac9abd9e188fc46f](../../evidence/parameters-sets-013.md#p-ac9abd9e188fc46f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025400

```text
(exec)# show ipv6 neighbors binding bdid <number:dynamic> <cr>
```

Handler ` RVA 0x136862F0 `；selector ` 1048 `；EOL ` RVA 0x35BF49F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-a29eb82013b33a55](../../evidence/conditions-sets-063.md#c-a29eb82013b33a55) · [缺口 G-f6efde15ad6d544e](../../evidence/gaps-sets-009.md#g-f6efde15ad6d544e) · [参数 P-80cee61582ae6113](../../evidence/parameters-sets-010.md#p-80cee61582ae6113) · [状态效果 S-52fe8a4f6fbd7214](../../evidence/state_effects-sets-018.md#s-52fe8a4f6fbd7214)

### path-006429

```text
(exec)# show ipv6 neighbors ha <cr>
```

Handler ` RVA 0x12312380 `；selector ` 0 `；EOL ` RVA 0x35802280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7810b73dccdb84af](../../evidence/conditions-sets-047.md#c-7810b73dccdb84af) · [状态效果 S-dd63671673f24d7e](../../evidence/state_effects-sets-047.md#s-dd63671673f24d7e)

### path-002842

```text
(exec)# show ipv6 nhrp <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 0 `；EOL ` RVA 0x3556BAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05dc8306fe7a3034](../../evidence/conditions-sets-003.md#c-05dc8306fe7a3034) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015171

```text
(exec)# show ipv6 nhrp <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 0 `；EOL ` RVA 0x3556BAA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b14fcf646ecdcb7](../../evidence/conditions-sets-005.md#c-0b14fcf646ecdcb7) · [缺口 G-ae135edb5213a6a2](../../evidence/gaps-sets-006.md#g-ae135edb5213a6a2) · [参数 P-2709226bb4c8e330](../../evidence/parameters-sets-003.md#p-2709226bb4c8e330) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019501

```text
(exec)# show ipv6 nhrp <interface> shortcut <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 15 `；EOL ` RVA 0x3556BE38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b14fcf646ecdcb7](../../evidence/conditions-sets-005.md#c-0b14fcf646ecdcb7) · [缺口 G-ae135edb5213a6a2](../../evidence/gaps-sets-006.md#g-ae135edb5213a6a2) · [参数 P-2709226bb4c8e330](../../evidence/parameters-sets-003.md#p-2709226bb4c8e330) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006724

```text
(exec)# show ipv6 nhrp attribute <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 16 `；EOL ` RVA 0x3556AF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006767

```text
(exec)# show ipv6 nhrp instances <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 20 `；EOL ` RVA 0x3556B2A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41053804b2654dd5](../../evidence/conditions-sets-025.md#c-41053804b2654dd5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006752

```text
(exec)# show ipv6 nhrp map <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 17 `；EOL ` RVA 0x3556ACD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f8651d3ed952226](../../evidence/conditions-sets-049.md#c-7f8651d3ed952226) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019284

```text
(exec)# show ipv6 nhrp map <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 17 `；EOL ` RVA 0x3556ACD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d77f8d97d135d967](../../evidence/conditions-sets-083.md#c-d77f8d97d135d967) · [缺口 G-b2ad772a8651e01c](../../evidence/gaps-sets-006.md#g-b2ad772a8651e01c) · [参数 P-36d6f04409b44e1e](../../evidence/parameters-sets-005.md#p-36d6f04409b44e1e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006790

```text
(exec)# show ipv6 nhrp multicast <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 4 `；EOL ` RVA 0x3556A8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be71c914d6cc161d](../../evidence/conditions-sets-074.md#c-be71c914d6cc161d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019297

```text
(exec)# show ipv6 nhrp multicast <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 4 `；EOL ` RVA 0x3556A8B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8cf61fdf11179f0f](../../evidence/conditions-sets-055.md#c-8cf61fdf11179f0f) · [缺口 G-a11a8e4292a334bf](../../evidence/gaps-sets-006.md#g-a11a8e4292a334bf) · [参数 P-7aca9d4e591a67db](../../evidence/parameters-sets-010.md#p-7aca9d4e591a67db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006755

```text
(exec)# show ipv6 nhrp nhs <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 3 `；EOL ` RVA 0x355696B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cefd3aad122d1c6](../../evidence/conditions-sets-024.md#c-3cefd3aad122d1c6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019304

```text
(exec)# show ipv6 nhrp nhs <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 3 `；EOL ` RVA 0x355696B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3571dbee955d6af](../../evidence/conditions-sets-075.md#c-c3571dbee955d6af) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022596

```text
(exec)# show ipv6 nhrp nhs <interface> redundancy <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 10 `；EOL ` RVA 0x3556A218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3571dbee955d6af](../../evidence/conditions-sets-075.md#c-c3571dbee955d6af) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024860

```text
(exec)# show ipv6 nhrp nhs <interface> redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 14 `；EOL ` RVA 0x35569CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-c3571dbee955d6af](../../evidence/conditions-sets-075.md#c-c3571dbee955d6af) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-60da779d75ad7109](../../evidence/parameters-sets-008.md#p-60da779d75ad7109) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024292

```text
(exec)# show ipv6 nhrp nhs <interface> redundancy preempted <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 12 `；EOL ` RVA 0x35569F48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3571dbee955d6af](../../evidence/conditions-sets-075.md#c-c3571dbee955d6af) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024282

```text
(exec)# show ipv6 nhrp nhs <interface> redundancy running <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 11 `；EOL ` RVA 0x355699B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3571dbee955d6af](../../evidence/conditions-sets-075.md#c-c3571dbee955d6af) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024294

```text
(exec)# show ipv6 nhrp nhs <interface> redundancy waiting <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 13 `；EOL ` RVA 0x3556A1F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3571dbee955d6af](../../evidence/conditions-sets-075.md#c-c3571dbee955d6af) · [缺口 G-3367dcc1c019d9a0](../../evidence/gaps-sets-002.md#g-3367dcc1c019d9a0) · [参数 P-ae094440659cfe2d](../../evidence/parameters-sets-013.md#p-ae094440659cfe2d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009803

```text
(exec)# show ipv6 nhrp nhs redundancy <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 10 `；EOL ` RVA 0x3556A218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cefd3aad122d1c6](../../evidence/conditions-sets-024.md#c-3cefd3aad122d1c6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011872

```text
(exec)# show ipv6 nhrp nhs redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 14 `；EOL ` RVA 0x35569CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-3cefd3aad122d1c6](../../evidence/conditions-sets-024.md#c-3cefd3aad122d1c6) · [参数 P-f03a6f61f88c6974](../../evidence/parameters-sets-018.md#p-f03a6f61f88c6974) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011354

```text
(exec)# show ipv6 nhrp nhs redundancy preempted <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 12 `；EOL ` RVA 0x35569F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cefd3aad122d1c6](../../evidence/conditions-sets-024.md#c-3cefd3aad122d1c6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011345

```text
(exec)# show ipv6 nhrp nhs redundancy running <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 11 `；EOL ` RVA 0x355699B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cefd3aad122d1c6](../../evidence/conditions-sets-024.md#c-3cefd3aad122d1c6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011359

```text
(exec)# show ipv6 nhrp nhs redundancy waiting <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 13 `；EOL ` RVA 0x3556A1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3cefd3aad122d1c6](../../evidence/conditions-sets-024.md#c-3cefd3aad122d1c6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006635

```text
(exec)# show ipv6 nhrp purge <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 2 `；EOL ` RVA 0x355692E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006798

```text
(exec)# show ipv6 nhrp redirect <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 6 `；EOL ` RVA 0x3556B620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006946

```text
(exec)# show ipv6 nhrp shortcut <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 15 `；EOL ` RVA 0x3556BE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05dc8306fe7a3034](../../evidence/conditions-sets-003.md#c-05dc8306fe7a3034) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006759

```text
(exec)# show ipv6 nhrp stats <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 18 `；EOL ` RVA 0x35568EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-447afffa2ab9db5d](../../evidence/conditions-sets-027.md#c-447afffa2ab9db5d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019309

```text
(exec)# show ipv6 nhrp stats <interface> <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 18 `；EOL ` RVA 0x35568EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eccf767435a57d3c](../../evidence/conditions-sets-091.md#c-eccf767435a57d3c) · [缺口 G-fd22e53b7a28fc48](../../evidence/gaps-sets-009.md#g-fd22e53b7a28fc48) · [参数 P-b60092aad0a805e6](../../evidence/parameters-sets-014.md#p-b60092aad0a805e6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006671

```text
(exec)# show ipv6 nhrp traffic <cr>
```

Handler ` RVA 0x1186E4D0 `；selector ` 1 `；EOL ` RVA 0x355689D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009643

```text
(exec)# show ipv6 pim all-vrfs traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 17 `；EOL ` RVA 0x3555DF70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e3aef5a38ae89c70](../../evidence/conditions-sets-088.md#c-e3aef5a38ae89c70) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006862

```text
(exec)# show ipv6 pim anycast-rp <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 20 `；EOL ` RVA 0x3555D920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0dbf75005d0c9c9b](../../evidence/conditions-sets-006.md#c-0dbf75005d0c9c9b) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-024357

```text
(exec)# show ipv6 pim bfd neighbor <interface> inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9D680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ef0d36988724bb95](../../evidence/conditions-sets-092.md#c-ef0d36988724bb95) · [缺口 G-c3d5f5b8c8e0caa5](../../evidence/gaps-sets-007.md#g-c3d5f5b8c8e0caa5) · [参数 P-9f1575569e0001bf](../../evidence/parameters-sets-012.md#p-9f1575569e0001bf) · [状态效果 S-a03d7a2b83fb250b](../../evidence/state_effects-sets-034.md#s-a03d7a2b83fb250b)

### path-011423

```text
(exec)# show ipv6 pim bfd neighbor inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9D680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b8e53924bc41724](../../evidence/conditions-sets-060.md#c-9b8e53924bc41724) · [状态效果 S-a03d7a2b83fb250b](../../evidence/state_effects-sets-034.md#s-a03d7a2b83fb250b)

### path-009871

```text
(exec)# show ipv6 pim bsr candidate-rp <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 13 `；EOL ` RVA 0x35551E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-5e65cc69f3319d94](../../evidence/state_effects-sets-020.md#s-5e65cc69f3319d94)

### path-009888

```text
(exec)# show ipv6 pim bsr election <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 12 `；EOL ` RVA 0x35552360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-5e65cc69f3319d94](../../evidence/state_effects-sets-020.md#s-5e65cc69f3319d94)

### path-009881

```text
(exec)# show ipv6 pim bsr rp-cache <cr>
```

Handler ` RVA 0x11843E00 `；selector ` 14 `；EOL ` RVA 0x355520B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-5e65cc69f3319d94](../../evidence/state_effects-sets-020.md#s-5e65cc69f3319d94)

### path-006808

```text
(exec)# show ipv6 pim df <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 5 `；EOL ` RVA 0x3555AA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-81c1da527a6ae5e0](../../evidence/conditions-sets-050.md#c-81c1da527a6ae5e0) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019356

```text
(exec)# show ipv6 pim df <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 5 `；EOL ` RVA 0x3555AA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-987ee70d63f1ba5e](../../evidence/conditions-sets-059.md#c-987ee70d63f1ba5e) · [缺口 G-08257c1e2ce81d6b](../../evidence/gaps-sets-001.md#g-08257c1e2ce81d6b) · [参数 P-b0e5d0b436638c5a](../../evidence/parameters-sets-013.md#p-b0e5d0b436638c5a) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009850

```text
(exec)# show ipv6 pim drlb gdr-candidates <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 22 `；EOL ` RVA 0x3555D3A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9dc51ee7b537cc84](../../evidence/conditions-sets-061.md#c-9dc51ee7b537cc84) · [状态效果 S-0dbace024f261ac1](../../evidence/state_effects-sets-003.md#s-0dbace024f261ac1)

### path-022645

```text
(exec)# show ipv6 pim drlb gdr-candidates <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 22 `；EOL ` RVA 0x3555D3A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-835b5f9f0946c3a8](../../evidence/conditions-sets-051.md#c-835b5f9f0946c3a8) · [缺口 G-0e5d9a2cc1bb8dee](../../evidence/gaps-sets-001.md#g-0e5d9a2cc1bb8dee) · [参数 P-09e1a72196ef41d4](../../evidence/parameters-sets-001.md#p-09e1a72196ef41d4) · [状态效果 S-0dbace024f261ac1](../../evidence/state_effects-sets-003.md#s-0dbace024f261ac1)

### path-006857

```text
(exec)# show ipv6 pim gir <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 26 `；EOL ` RVA 0x3555DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3768dcdfafbac72b](../../evidence/conditions-sets-022.md#c-3768dcdfafbac72b) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006756

```text
(exec)# show ipv6 pim group-map <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 3 `；EOL ` RVA 0x3555A068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f602872f72488562](../../evidence/conditions-sets-095.md#c-f602872f72488562) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019308

```text
(exec)# show ipv6 pim group-map <prefix:dynamic> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 3 `；EOL ` RVA 0x3555A068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` group prefix/mask。

[条件 C-dc866aaf1ccedc5a](../../evidence/conditions-sets-085.md#c-dc866aaf1ccedc5a) · [缺口 G-535e8c549d987339](../../evidence/gaps-sets-003.md#g-535e8c549d987339) · [参数 P-03b2d0d72e8e8207](../../evidence/parameters-sets-001.md#p-03b2d0d72e8e8207) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006738

```text
(exec)# show ipv6 pim interface <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 0 `；EOL ` RVA 0x35558B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-992fb269d922b5d8](../../evidence/conditions-sets-059.md#c-992fb269d922b5d8) · [状态效果 S-4ccffd85282b2b2e](../../evidence/state_effects-sets-017.md#s-4ccffd85282b2b2e)

### path-019275

```text
(exec)# show ipv6 pim interface <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 0 `；EOL ` RVA 0x35558B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cb8802d65ee805a5](../../evidence/conditions-sets-078.md#c-cb8802d65ee805a5) · [缺口 G-67e9709bd8c74ca4](../../evidence/gaps-sets-004.md#g-67e9709bd8c74ca4) · [参数 P-08515242a93c3f65](../../evidence/parameters-sets-001.md#p-08515242a93c3f65) · [状态效果 S-4ccffd85282b2b2e](../../evidence/state_effects-sets-017.md#s-4ccffd85282b2b2e)

### path-022592

```text
(exec)# show ipv6 pim interface <interface> bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9DA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4dba785c8a33156](../../evidence/conditions-sets-094.md#c-f4dba785c8a33156) · [缺口 G-67e9709bd8c74ca4](../../evidence/gaps-sets-004.md#g-67e9709bd8c74ca4) · [参数 P-08515242a93c3f65](../../evidence/parameters-sets-001.md#p-08515242a93c3f65) · [状态效果 S-d3f905d6f9e0429e](../../evidence/state_effects-sets-045.md#s-d3f905d6f9e0429e)

### path-009800

```text
(exec)# show ipv6 pim interface bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9DA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6eb11e3d2c4c8054](../../evidence/conditions-sets-043.md#c-6eb11e3d2c4c8054) · [状态效果 S-d3f905d6f9e0429e](../../evidence/state_effects-sets-045.md#s-d3f905d6f9e0429e)

### path-006851

```text
(exec)# show ipv6 pim internal <cr>
```

Handler ` RVA 0x1175D2F0 `；selector ` 0 `；EOL ` RVA 0x3555CF28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e269434a04dbe2bc](../../evidence/conditions-sets-087.md#c-e269434a04dbe2bc) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019407

```text
(exec)# show ipv6 pim internal <interface> <cr>
```

Handler ` RVA 0x1175D2F0 `；selector ` 0 `；EOL ` RVA 0x3555CF28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-124fe0c65813ee4e](../../evidence/conditions-sets-007.md#c-124fe0c65813ee4e) · [缺口 G-3dda9baeb37b261f](../../evidence/gaps-sets-003.md#g-3dda9baeb37b261f) · [参数 P-073220dee3ba98b7](../../evidence/parameters-sets-001.md#p-073220dee3ba98b7) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009815

```text
(exec)# show ipv6 pim join-prune statistic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 15 `；EOL ` RVA 0x3555C028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-226883bf8df5ffda](../../evidence/conditions-sets-013.md#c-226883bf8df5ffda) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-022597

```text
(exec)# show ipv6 pim join-prune statistic <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 15 `；EOL ` RVA 0x3555C028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-033e12e416a3a5b1](../../evidence/conditions-sets-002.md#c-033e12e416a3a5b1) · [缺口 G-4e468cab5acd1bc7](../../evidence/gaps-sets-003.md#g-4e468cab5acd1bc7) · [参数 P-2a28748aeaef974d](../../evidence/parameters-sets-004.md#p-2a28748aeaef974d) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006806

```text
(exec)# show ipv6 pim limit <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 7 `；EOL ` RVA 0x3555B988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09f725f041155854](../../evidence/conditions-sets-004.md#c-09f725f041155854) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019344

```text
(exec)# show ipv6 pim limit <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 7 `；EOL ` RVA 0x3555B988 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-09ef1128ccd52568](../../evidence/conditions-sets-004.md#c-09ef1128ccd52568) · [缺口 G-0b16c7a32442baa7](../../evidence/gaps-sets-001.md#g-0b16c7a32442baa7) · [参数 P-5be80ea061bfce4c](../../evidence/parameters-sets-007.md#p-5be80ea061bfce4c) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009816

```text
(exec)# show ipv6 pim limit reservation <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 8 `；EOL ` RVA 0x3555B618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-333e558d2ffb0710](../../evidence/conditions-sets-020.md#c-333e558d2ffb0710) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-022608

```text
(exec)# show ipv6 pim limit reservation <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 8 `；EOL ` RVA 0x3555B618 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f195ae7995cf8371](../../evidence/conditions-sets-093.md#c-f195ae7995cf8371) · [缺口 G-4946b21c0f6e7b28](../../evidence/gaps-sets-003.md#g-4946b21c0f6e7b28) · [参数 P-5bb5850ec768b0a2](../../evidence/parameters-sets-007.md#p-5bb5850ec768b0a2) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011363

```text
(exec)# show ipv6 pim limit reservation required <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 9 `；EOL ` RVA 0x3555B278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-04d6172fbbd4dc53](../../evidence/conditions-sets-002.md#c-04d6172fbbd4dc53) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-024298

```text
(exec)# show ipv6 pim limit reservation required <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 9 `；EOL ` RVA 0x3555B278 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0d682afa5b6d9536](../../evidence/conditions-sets-005.md#c-0d682afa5b6d9536) · [缺口 G-153d6d4467a394e4](../../evidence/gaps-sets-001.md#g-153d6d4467a394e4) · [参数 P-51c476775a0d6c96](../../evidence/parameters-sets-007.md#p-51c476775a0d6c96) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006764

```text
(exec)# show ipv6 pim lisp-rloc-state <cr>
```

Handler ` RVA 0x11757BB0 `；selector ` 27 `；EOL ` RVA 0x3555BC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83cc795f397f9ed1](../../evidence/conditions-sets-051.md#c-83cc795f397f9ed1) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006959

```text
(exec)# show ipv6 pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478A808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009927

```text
(exec)# show ipv6 pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x347886B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011424

```text
(exec)# show ipv6 pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x34788378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0f4a562bd79631e](../../evidence/conditions-sets-087.md#c-e0f4a562bd79631e) · [状态效果 S-fc891d9ce5e2071b](../../evidence/state_effects-sets-053.md#s-fc891d9ce5e2071b)

### path-011882

```text
(exec)# show ipv6 pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x34787F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [参数 P-957dcedf315a82c2](../../evidence/parameters-sets-011.md#p-957dcedf315a82c2) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011426

```text
(exec)# show ipv6 pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x34788F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84219efcdabebf50](../../evidence/conditions-sets-051.md#c-84219efcdabebf50) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011439

```text
(exec)# show ipv6 pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x34789A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-346446207ebbe9b4](../../evidence/conditions-sets-020.md#c-346446207ebbe9b4) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011421

```text
(exec)# show ipv6 pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x34788CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29502a8ccf617563](../../evidence/conditions-sets-016.md#c-29502a8ccf617563) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011429

```text
(exec)# show ipv6 pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x34789228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c45a96432149cd82](../../evidence/conditions-sets-076.md#c-c45a96432149cd82) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011433

```text
(exec)# show ipv6 pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x347894D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa3aee4f006bc09f](../../evidence/conditions-sets-097.md#c-fa3aee4f006bc09f) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011436

```text
(exec)# show ipv6 pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x34789778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4d737908cf7e75f6](../../evidence/conditions-sets-030.md#c-4d737908cf7e75f6) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011443

```text
(exec)# show ipv6 pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x34789FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6cfe596c8a5efa8b](../../evidence/conditions-sets-042.md#c-6cfe596c8a5efa8b) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011896

```text
(exec)# show ipv6 pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478A280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5544abd3a64524b3](../../evidence/conditions-sets-033.md#c-5544abd3a64524b3) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011441

```text
(exec)# show ipv6 pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x34789CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a2ecbf7d3a478420](../../evidence/conditions-sets-063.md#c-a2ecbf7d3a478420) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011442

```text
(exec)# show ipv6 pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f1aafbd453847f3](../../evidence/conditions-sets-043.md#c-6f1aafbd453847f3) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011416

```text
(exec)# show ipv6 pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x34788A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dcda79b17efe1870](../../evidence/conditions-sets-085.md#c-dcda79b17efe1870) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009883

```text
(exec)# show ipv6 pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x34787A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-011400

```text
(exec)# show ipv6 pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x347879E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009862

```text
(exec)# show ipv6 pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x347876D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b4444ce0bf724afb](../../evidence/conditions-sets-070.md#c-b4444ce0bf724afb) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006757

```text
(exec)# show ipv6 pim neighbor <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 11 `；EOL ` RVA 0x355599F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aad74c82049dddf5](../../evidence/conditions-sets-066.md#c-aad74c82049dddf5) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006758

```text
(exec)# show ipv6 pim neighbor <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 2 `；EOL ` RVA 0x35559C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b53afb6d866bc021](../../evidence/conditions-sets-070.md#c-b53afb6d866bc021) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019298

```text
(exec)# show ipv6 pim neighbor <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 11 `；EOL ` RVA 0x355599F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e7e7dc9d04c3231](../../evidence/conditions-sets-043.md#c-6e7e7dc9d04c3231) · [缺口 G-848b6056a4643eab](../../evidence/gaps-sets-005.md#g-848b6056a4643eab) · [参数 P-0a6e9ba5a4647764](../../evidence/parameters-sets-001.md#p-0a6e9ba5a4647764) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019299

```text
(exec)# show ipv6 pim neighbor <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 2 `；EOL ` RVA 0x35559C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3649307d91ae53ba](../../evidence/conditions-sets-021.md#c-3649307d91ae53ba) · [缺口 G-848b6056a4643eab](../../evidence/gaps-sets-005.md#g-848b6056a4643eab) · [参数 P-0a6e9ba5a4647764](../../evidence/parameters-sets-001.md#p-0a6e9ba5a4647764) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009805

```text
(exec)# show ipv6 pim pfp-sa announcements <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 23 `；EOL ` RVA 0x3555C3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be731d8b3d956a00](../../evidence/conditions-sets-074.md#c-be731d8b3d956a00) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009831

```text
(exec)# show ipv6 pim pfp-sa cache <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 25 `；EOL ` RVA 0x3555C8F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be731d8b3d956a00](../../evidence/conditions-sets-074.md#c-be731d8b3d956a00) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009822

```text
(exec)# show ipv6 pim pfp-sa originator <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 24 `；EOL ` RVA 0x3555C648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be731d8b3d956a00](../../evidence/conditions-sets-074.md#c-be731d8b3d956a00) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006753

```text
(exec)# show ipv6 pim range-list <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 4 `；EOL ` RVA 0x3555A5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b15f72033f3eb0ae](../../evidence/conditions-sets-069.md#c-b15f72033f3eb0ae) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006695

```text
(exec)# show ipv6 pim topology <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 1 `；EOL ` RVA 0x355592E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d057d950e6e2e7c](../../evidence/conditions-sets-005.md#c-0d057d950e6e2e7c) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-009680

```text
(exec)# show ipv6 pim topology route-count <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 6 `；EOL ` RVA 0x35559040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7ab8ff6af774007](../../evidence/conditions-sets-065.md#c-a7ab8ff6af774007) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006811

```text
(exec)# show ipv6 pim traffic <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 16 `；EOL ` RVA 0x3555CB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6ee2bcbe1a78785](../../evidence/conditions-sets-064.md#c-a6ee2bcbe1a78785) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-006768

```text
(exec)# show ipv6 pim tunnel <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 10 `；EOL ` RVA 0x3555ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b437b896136f8ea6](../../evidence/conditions-sets-070.md#c-b437b896136f8ea6) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-019316

```text
(exec)# show ipv6 pim tunnel <interface> <cr>
```

Handler ` RVA 0x1175C6E0 `；selector ` 10 `；EOL ` RVA 0x3555ADC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd2292d4474b6721](../../evidence/conditions-sets-085.md#c-dd2292d4474b6721) · [缺口 G-6e07848da81fff95](../../evidence/gaps-sets-004.md#g-6e07848da81fff95) · [参数 P-b3e762b644a81f9b](../../evidence/parameters-sets-014.md#p-b3e762b644a81f9b) · [状态效果 S-4147db064d8eeede](../../evidence/state_effects-sets-014.md#s-4147db064d8eeede)

### path-002672

```text
(exec)# show ipv6 policy <cr>
```

Handler ` RVA 0x118BA0F0 `；selector ` 0 `；EOL ` RVA 0x3559C548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015046

```text
(exec)# show ipv6 prefix <?match_ipv6_pfxinfo_action@55558ad32948> <cr>
```

Handler ` RVA 0x12300A90 `；selector ` 0 `；EOL ` RVA 0x357DE9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-193c62e72d220144](../../evidence/conditions-sets-010.md#c-193c62e72d220144) · [缺口 G-7d074174f3f780b6](../../evidence/gaps-sets-005.md#g-7d074174f3f780b6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006841

```text
(exec)# show ipv6 prefix reserved <cr>
```

Handler ` RVA 0x12300A90 `；selector ` 0 `；EOL ` RVA 0x357DE9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-193c62e72d220144](../../evidence/conditions-sets-010.md#c-193c62e72d220144) · [状态效果 S-13c82f4f3f909ee6](../../evidence/state_effects-sets-005.md#s-13c82f4f3f909ee6)

### path-002662

```text
(exec)# show ipv6 prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x3557F168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94db62ffb44ba997](../../evidence/conditions-sets-058.md#c-94db62ffb44ba997) · [状态效果 S-bb652d416c4e07cf](../../evidence/state_effects-sets-040.md#s-bb652d416c4e07cf)

### path-019423

```text
(exec)# show ipv6 prefix-list <string> <prefix:dynamic> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 4 `；EOL ` RVA 0x3557F540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of a prefix list；` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-d31694fca73ee771](../../evidence/conditions-sets-081.md#c-d31694fca73ee771) · [缺口 G-c72ac1d990c03bb5](../../evidence/gaps-sets-007.md#g-c72ac1d990c03bb5) · [参数 P-7cf8c3bf40aa5c59](../../evidence/parameters-sets-010.md#p-7cf8c3bf40aa5c59) · [状态效果 S-bb652d416c4e07cf](../../evidence/state_effects-sets-040.md#s-bb652d416c4e07cf)

### path-011364

```text
(exec)# show ipv6 prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x3557F210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-94db62ffb44ba997](../../evidence/conditions-sets-058.md#c-94db62ffb44ba997) · [参数 P-46df89ae42bf78b4](../../evidence/parameters-sets-006.md#p-46df89ae42bf78b4) · [状态效果 S-bb652d416c4e07cf](../../evidence/state_effects-sets-040.md#s-bb652d416c4e07cf)

### path-006803

```text
(exec)# show ipv6 prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x3557EE68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-bb652d416c4e07cf](../../evidence/state_effects-sets-040.md#s-bb652d416c4e07cf)

### path-006783

```text
(exec)# show ipv6 prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x3557EB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-bb652d416c4e07cf](../../evidence/state_effects-sets-040.md#s-bb652d416c4e07cf)

### path-002364

```text
(exec)# show ipv6 protocols <cr>
```

Handler ` RVA 0x1230B1E0 `；selector ` 0 `；EOL ` RVA 0x357EAF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014983

```text
(exec)# show ipv6 reassembly <interface> <cr>
```

Handler ` RVA 0xC78A5E0 `；selector ` 0 `；EOL ` RVA 0x33AE9230 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c6fc77574a7767d1](../../evidence/conditions-sets-077.md#c-c6fc77574a7767d1) · [缺口 G-977771d0856f9f40](../../evidence/gaps-sets-006.md#g-977771d0856f9f40) · [参数 P-dff3f5e0b6ccd83c](../../evidence/parameters-sets-017.md#p-dff3f5e0b6ccd83c) · [状态效果 S-0ce31961b59a6cb0](../../evidence/state_effects-sets-003.md#s-0ce31961b59a6cb0)

### path-002608

```text
(exec)# show ipv6 rip <cr>
```

Handler ` RVA 0x118A5B90 `；selector ` 0 `；EOL ` RVA 0x3557C408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa703e0f0a1553a9](../../evidence/conditions-sets-066.md#c-aa703e0f0a1553a9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006660

```text
(exec)# show ipv6 rip database <cr>
```

Handler ` RVA 0x118A4C60 `；selector ` 0 `；EOL ` RVA 0x3557BDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83b1b03eac7a0904](../../evidence/conditions-sets-051.md#c-83b1b03eac7a0904) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006680

```text
(exec)# show ipv6 rip next-hops <cr>
```

Handler ` RVA 0x118A5450 `；selector ` 0 `；EOL ` RVA 0x3557C0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83b1b03eac7a0904](../../evidence/conditions-sets-051.md#c-83b1b03eac7a0904) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019330

```text
(exec)# show ipv6 route <?match_ipv6_pfxinfo_action@55558ad3cec8> longer-prefixes <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5eecad73a55407dd](../../evidence/conditions-sets-037.md#c-5eecad73a55407dd) · [缺口 G-27354695592d47c8](../../evidence/gaps-sets-002.md#g-27354695592d47c8) · [状态效果 S-a12fce82c1f18c39](../../evidence/state_effects-sets-034.md#s-a12fce82c1f18c39)

### path-006786

```text
(exec)# show ipv6 route <address> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 name or address。

[条件 C-cb382d9985cbc9fa](../../evidence/conditions-sets-078.md#c-cb382d9985cbc9fa) · [参数 P-43b1e41b4080817f](../../evidence/parameters-sets-006.md#p-43b1e41b4080817f) · [状态效果 S-c8dd94d71b96ea87](../../evidence/state_effects-sets-043.md#s-c8dd94d71b96ea87)

### path-002542

```text
(exec)# show ipv6 route <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E8B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [状态效果 S-617b5daa73d2a8e5](../../evidence/state_effects-sets-021.md#s-617b5daa73d2a8e5)

### path-019040

```text
(exec)# show ipv6 route interface <interface> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EAAF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3acf4db0ad3dfebf](../../evidence/conditions-sets-023.md#c-3acf4db0ad3dfebf) · [缺口 G-7c537eefa5359b97](../../evidence/gaps-sets-005.md#g-7c537eefa5359b97) · [参数 P-72f91cdc047fd03b](../../evidence/parameters-sets-009.md#p-72f91cdc047fd03b) · [状态效果 S-12206ac619a0463d](../../evidence/state_effects-sets-004.md#s-12206ac619a0463d)

### path-014884

```text
(exec)# show ipv6 route multicast <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E8B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-4b8296b560b4a207](../../evidence/state_effects-sets-017.md#s-4b8296b560b4a207)

### path-018943

```text
(exec)# show ipv6 route multicast nsf <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA488 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-5875d90a776a7dc9](../../evidence/state_effects-sets-019.md#s-5875d90a776a7dc9)

### path-018957

```text
(exec)# show ipv6 route multicast summary <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA1E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-41c3ab9004cddb6e](../../evidence/state_effects-sets-014.md#s-41c3ab9004cddb6e)

### path-018891

```text
(exec)# show ipv6 route multicast table <cr>
```

Handler ` RVA 0x1230A240 `；selector ` 0 `；EOL ` RVA 0x357E9DE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-4b8296b560b4a207](../../evidence/state_effects-sets-017.md#s-4b8296b560b4a207)

### path-022194

```text
(exec)# show ipv6 route multicast table <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9B38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Table id (hex)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [参数 P-c8a0d4a105edec77](../../evidence/parameters-sets-015.md#p-c8a0d4a105edec77) · [状态效果 S-4b8296b560b4a207](../../evidence/state_effects-sets-017.md#s-4b8296b560b4a207)

### path-022399

```text
(exec)# show ipv6 route multicast tag <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357F2C48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [参数 P-49e39b5d6941be33](../../evidence/parameters-sets-006.md#p-49e39b5d6941be33) · [状态效果 S-e7b9a73632ca78ae](../../evidence/state_effects-sets-049.md#s-e7b9a73632ca78ae)

### path-018987

```text
(exec)# show ipv6 route multicast watch <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA740 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [缺口 G-a2cbbd8135b6f598](../../evidence/gaps-sets-006.md#g-a2cbbd8135b6f598) · [状态效果 S-bb21b0708278044a](../../evidence/state_effects-sets-040.md#s-bb21b0708278044a)

### path-006408

```text
(exec)# show ipv6 route nsf <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [状态效果 S-a22557c3a60a7114](../../evidence/state_effects-sets-034.md#s-a22557c3a60a7114)

### path-006420

```text
(exec)# show ipv6 route summary <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [状态效果 S-3bba78392dd85ebd](../../evidence/state_effects-sets-013.md#s-3bba78392dd85ebd)

### path-006359

```text
(exec)# show ipv6 route table <cr>
```

Handler ` RVA 0x1230A240 `；selector ` 0 `；EOL ` RVA 0x357E9DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-617b5daa73d2a8e5](../../evidence/state_effects-sets-021.md#s-617b5daa73d2a8e5)

### path-009404

```text
(exec)# show ipv6 route table <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357E9B38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Table id (hex)。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-c8a0d4a105edec77](../../evidence/parameters-sets-015.md#p-c8a0d4a105edec77) · [状态效果 S-617b5daa73d2a8e5](../../evidence/state_effects-sets-021.md#s-617b5daa73d2a8e5)

### path-009601

```text
(exec)# show ipv6 route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357F2C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [参数 P-49e39b5d6941be33](../../evidence/parameters-sets-006.md#p-49e39b5d6941be33) · [状态效果 S-646c7ecbe7d416ba](../../evidence/state_effects-sets-021.md#s-646c7ecbe7d416ba)

### path-006446

```text
(exec)# show ipv6 route watch <cr>
```

Handler ` RVA 0x1230A670 `；selector ` 0 `；EOL ` RVA 0x357EA740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc1df9382255504f](../../evidence/conditions-sets-097.md#c-fc1df9382255504f) · [状态效果 S-e77e9477b4c45356](../../evidence/state_effects-sets-049.md#s-e77e9477b4c45356)

### path-002461

```text
(exec)# show ipv6 routers <cr>
```

Handler ` RVA 0x12312D70 `；selector ` 0 `；EOL ` RVA 0x357FA910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-20f398c895f60c2f](../../evidence/conditions-sets-013.md#c-20f398c895f60c2f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014788

```text
(exec)# show ipv6 routers <interface> <cr>
```

Handler ` RVA 0x12312D70 `；selector ` 0 `；EOL ` RVA 0x357FA910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad6b4b18cd1eb369](../../evidence/conditions-sets-067.md#c-ad6b4b18cd1eb369) · [缺口 G-57972797f16c9176](../../evidence/gaps-sets-004.md#g-57972797f16c9176) · [参数 P-626059d4e05be74e](../../evidence/parameters-sets-008.md#p-626059d4e05be74e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006861

```text
(exec)# show ipv6 rpf <address> <cr>
```

Handler ` RVA 0x118E47F0 `；selector ` 0 `；EOL ` RVA 0x35538420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` RP/Source address。

[条件 C-713c859374191240](../../evidence/conditions-sets-044.md#c-713c859374191240) · [参数 P-45778e765de8f2c0](../../evidence/parameters-sets-006.md#p-45778e765de8f2c0) · [状态效果 S-252f1501fa88c966](../../evidence/state_effects-sets-008.md#s-252f1501fa88c966)

### path-006835

```text
(exec)# show ipv6 rpf select <cr>
```

Handler ` RVA 0x118E47F0 `；selector ` 1 `；EOL ` RVA 0x355380F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c84d32681a469f44](../../evidence/conditions-sets-077.md#c-c84d32681a469f44) · [状态效果 S-252f1501fa88c966](../../evidence/state_effects-sets-008.md#s-252f1501fa88c966)

### path-025406

```text
(exec)# show ipv6 snooping capture-policy bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1043 `；EOL ` RVA 0x35BEE0B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-d91202bcd175dbf0](../../evidence/conditions-sets-084.md#c-d91202bcd175dbf0) · [缺口 G-645338896b1f7df3](../../evidence/gaps-sets-004.md#g-645338896b1f7df3) · [参数 P-8a4c8fa6fd4c88b5](../../evidence/parameters-sets-011.md#p-8a4c8fa6fd4c88b5) · [状态效果 S-434514280094031c](../../evidence/state_effects-sets-015.md#s-434514280094031c)

### path-025405

```text
(exec)# show ipv6 snooping counters bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1044 `；EOL ` RVA 0x35BEDB18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-ba1b0f2269eb0405](../../evidence/conditions-sets-072.md#c-ba1b0f2269eb0405) · [缺口 G-7d4eb9ffb7d69854](../../evidence/gaps-sets-005.md#g-7d4eb9ffb7d69854) · [参数 P-3b9082e9e85b7c94](../../evidence/parameters-sets-005.md#p-3b9082e9e85b7c94) · [状态效果 S-135f38433f62a36e](../../evidence/state_effects-sets-005.md#s-135f38433f62a36e)

### path-006778

```text
(exec)# show ipv6 snooping events <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1046 `；EOL ` RVA 0x35BED058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2248d99683b228a0](../../evidence/conditions-sets-013.md#c-2248d99683b228a0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006810

```text
(exec)# show ipv6 snooping features <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1045 `；EOL ` RVA 0x35BED640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2248d99683b228a0](../../evidence/conditions-sets-013.md#c-2248d99683b228a0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024326

```text
(exec)# show ipv6 snooping internal access-list interface <interface> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1041 `；EOL ` RVA 0x35BEEF80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d8112348004e317](../../evidence/conditions-sets-018.md#c-2d8112348004e317) · [缺口 G-1a33376769b2afc5](../../evidence/gaps-sets-001.md#g-1a33376769b2afc5) · [参数 P-f36250a0072309b8](../../evidence/parameters-sets-018.md#p-f36250a0072309b8) · [状态效果 S-346b6e1778f9a23c](../../evidence/state_effects-sets-012.md#s-346b6e1778f9a23c)

### path-009845

```text
(exec)# show ipv6 snooping internal counters <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1040 `；EOL ` RVA 0x35BEEBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67a686eea3248185](../../evidence/conditions-sets-040.md#c-67a686eea3248185) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006814

```text
(exec)# show ipv6 snooping messages <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1047 `；EOL ` RVA 0x35BED390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2248d99683b228a0](../../evidence/conditions-sets-013.md#c-2248d99683b228a0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025407

```text
(exec)# show ipv6 snooping policies bd <number:dynamic> <cr>
```

Handler ` RVA 0x13688090 `；selector ` 1042 `；EOL ` RVA 0x35BEE7B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-46994fc6e09fa5ee](../../evidence/conditions-sets-028.md#c-46994fc6e09fa5ee) · [缺口 G-574799d07bf7ca1f](../../evidence/gaps-sets-004.md#g-574799d07bf7ca1f) · [参数 P-de55dd4fc12c6a87](../../evidence/parameters-sets-017.md#p-de55dd4fc12c6a87) · [状态效果 S-767a079b3c097e95](../../evidence/state_effects-sets-025.md#s-767a079b3c097e95)

### path-006815

```text
(exec)# show ipv6 snooping policy <cr>
```

Handler ` RVA 0x1368B750 `；selector ` 0 `；EOL ` RVA 0x35BCC410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee2a910a2f062bce](../../evidence/conditions-sets-092.md#c-ee2a910a2f062bce) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006749

```text
(exec)# show ipv6 source-guard policy <cr>
```

Handler ` RVA 0x136C03A0 `；selector ` 0 `；EOL ` RVA 0x35C08A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002646

```text
(exec)# show ipv6 spd <cr>
```

Handler ` RVA 0x12328600 `；selector ` 0 `；EOL ` RVA 0x358101A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014839

```text
(exec)# show ipv6 static <?match_ipv6_pfxinfo_action@55558ad3fdb8> <cr>
```

Handler ` RVA 0x1230F810 `；selector ` 0 `；EOL ` RVA 0x357EBA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0c952135e474b875](../../evidence/conditions-sets-005.md#c-0c952135e474b875) · [缺口 G-c4ce9b0a3578f244](../../evidence/gaps-sets-007.md#g-c4ce9b0a3578f244) · [状态效果 S-60bb7f56b2f0d703](../../evidence/state_effects-sets-021.md#s-60bb7f56b2f0d703)

### path-002508

```text
(exec)# show ipv6 static <cr>
```

Handler ` RVA 0x1230F810 `；selector ` 0 `；EOL ` RVA 0x357EBA98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f5e6af3088a669d](../../evidence/conditions-sets-062.md#c-9f5e6af3088a669d) · [状态效果 S-60bb7f56b2f0d703](../../evidence/state_effects-sets-021.md#s-60bb7f56b2f0d703)

### path-006454

```text
(exec)# show ipv6 static bfd <cr>
```

Handler ` RVA 0x12310780 `；selector ` 0 `；EOL ` RVA 0x357EB4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-60bb7f56b2f0d703](../../evidence/state_effects-sets-021.md#s-60bb7f56b2f0d703)

### path-018994

```text
(exec)# show ipv6 static multicast bfd <cr>
```

Handler ` RVA 0x12310780 `；selector ` 0 `；EOL ` RVA 0x357EB4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-66db1908cb612aa8](../../evidence/gaps-sets-004.md#g-66db1908cb612aa8) · [状态效果 S-7ca83cdad0b5768a](../../evidence/state_effects-sets-026.md#s-7ca83cdad0b5768a)

### path-002360

```text
(exec)# show ipv6 traffic <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 0 `；EOL ` RVA 0x3580B3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006358

```text
(exec)# show ipv6 traffic interface <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 1 `；EOL ` RVA 0x3580B490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8e83abb6943a984f](../../evidence/conditions-sets-055.md#c-8e83abb6943a984f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-018834

```text
(exec)# show ipv6 traffic interface <interface> <cr>
```

Handler ` RVA 0x1231EF70 `；selector ` 1 `；EOL ` RVA 0x3580B490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e7f098d38a4f2aa1](../../evidence/conditions-sets-090.md#c-e7f098d38a4f2aa1) · [缺口 G-fb672dd6354a3daa](../../evidence/gaps-sets-009.md#g-fb672dd6354a3daa) · [参数 P-c3153726aeadeceb](../../evidence/parameters-sets-015.md#p-c3153726aeadeceb) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002399

```text
(exec)# show ipv6 tunnel <cr>
```

Handler ` RVA 0x12321E20 `；selector ` 0 `；EOL ` RVA 0x3580EC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-cb2f2a8d365d7214](../../evidence/state_effects-sets-043.md#s-cb2f2a8d365d7214)

### path-002661

```text
(exec)# show ipv6 virtual-reassembly <cr>
```

Handler ` RVA 0xC78A5E0 `；selector ` 0 `；EOL ` RVA 0x33AE9230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-61bc91799fc6ba42](../../evidence/conditions-sets-038.md#c-61bc91799fc6ba42) · [状态效果 S-d655856c345dc3cd](../../evidence/state_effects-sets-045.md#s-d655856c345dc3cd)

### path-025317

```text
(exec)# show isdn <?test_int_action@55558ce1c950> <?test_int_action@55558ce1dd80> call-rate <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 8 `；EOL ` RVA 0x378CA770 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd27be2745885a21](../../evidence/conditions-sets-085.md#c-dd27be2745885a21) · [缺口 G-1c0ea94d2418f038](../../evidence/gaps-sets-001.md#g-1c0ea94d2418f038) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025349

```text
(exec)# show isdn <?test_int_action@55558ce1c950> <?test_int_action@55558ce1dd80> variables statistics <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 7 `；EOL ` RVA 0x378CA210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd27be2745885a21](../../evidence/conditions-sets-085.md#c-dd27be2745885a21) · [缺口 G-1c0ea94d2418f038](../../evidence/gaps-sets-001.md#g-1c0ea94d2418f038) · [状态效果 S-b1adda8439cf1fdd](../../evidence/state_effects-sets-038.md#s-b1adda8439cf1fdd)

### path-016010

```text
(exec)# show isdn <?test_int_action@55558ce1c950> active <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 5 `；EOL ` RVA 0x378C9DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-20beb5318a12f341](../../evidence/conditions-sets-013.md#c-20beb5318a12f341) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-2507608b18b0dc88](../../evidence/state_effects-sets-008.md#s-2507608b18b0dc88)

### path-016004

```text
(exec)# show isdn <?test_int_action@55558ce1c950> history <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 4 `；EOL ` RVA 0x378C99D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ac7ebc82f0da3b4a](../../evidence/conditions-sets-067.md#c-ac7ebc82f0da3b4a) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-6da03583014258e4](../../evidence/state_effects-sets-023.md#s-6da03583014258e4)

### path-015969

```text
(exec)# show isdn <?test_int_action@55558ce1c950> memory <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 1 `；EOL ` RVA 0x378C8E00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd27be2745885a21](../../evidence/conditions-sets-085.md#c-dd27be2745885a21) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016005

```text
(exec)# show isdn <?test_int_action@55558ce1c950> status <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 3 `；EOL ` RVA 0x378C95E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea2ad1e771c51411](../../evidence/conditions-sets-090.md#c-ea2ad1e771c51411) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-80857b372d6bc5fe](../../evidence/state_effects-sets-027.md#s-80857b372d6bc5fe)

### path-015988

```text
(exec)# show isdn <?test_int_action@55558ce1c950> timers <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 2 `；EOL ` RVA 0x378C9170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4203b5fe4f74861](../../evidence/conditions-sets-063.md#c-a4203b5fe4f74861) · [缺口 G-4fe0ddbfc26b9408](../../evidence/gaps-sets-003.md#g-4fe0ddbfc26b9408) · [状态效果 S-0dfd67072af468c8](../../evidence/state_effects-sets-003.md#s-0dfd67072af468c8)

### path-020123

```text
(exec)# show isdn answer <interface> <string> <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 9 `；EOL ` RVA 0x378C8A00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` callingnumber:subaddr。

[条件 C-05617a6c91115de6](../../evidence/conditions-sets-002.md#c-05617a6c91115de6) · [缺口 G-3679ac6450d690bd](../../evidence/gaps-sets-002.md#g-3679ac6450d690bd) · [参数 P-aeb4cf28cd4ab242](../../evidence/parameters-sets-013.md#p-aeb4cf28cd4ab242) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010195

```text
(exec)# show isdn answer <number:0..95> <string> <cr>
```

Handler ` RVA 0x1E0319F0 `；selector ` 9 `；EOL ` RVA 0x378C8A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` List of DSL's；` string ` callingnumber:subaddr。

[条件 C-dd27be2745885a21](../../evidence/conditions-sets-085.md#c-dd27be2745885a21) · [参数 P-a1270995903425ab](../../evidence/parameters-sets-012.md#p-a1270995903425ab) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019922

```text
(exec)# show isis * adjacency stagger <cr>
```

Handler ` RVA 0x106F9DE0 `；selector ` 13 `；EOL ` RVA 0x34B69630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b126b48d2ec72069](../../evidence/conditions-sets-068.md#c-b126b48d2ec72069) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015682

```text
(exec)# show isis * mesh-groups <cr>
```

Handler ` RVA 0x10769310 `；selector ` 14 `；EOL ` RVA 0x34B69290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b126b48d2ec72069](../../evidence/conditions-sets-068.md#c-b126b48d2ec72069) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015689

```text
(exec)# show isis * mt <cr>
```

Handler ` RVA 0x1076C920 `；selector ` 20 `；EOL ` RVA 0x34B68F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d497b3aa9de76634](../../evidence/conditions-sets-082.md#c-d497b3aa9de76634) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015764

```text
(exec)# show isis * nsf <cr>
```

Handler ` RVA 0x1076C1B0 `；selector ` 19 `；EOL ` RVA 0x33FCAB48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b126b48d2ec72069](../../evidence/conditions-sets-068.md#c-b126b48d2ec72069) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015711

```text
(exec)# show isis * protocol <cr>
```

Handler ` RVA 0x10769A20 `；selector ` 12 `；EOL ` RVA 0x34B698E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b126b48d2ec72069](../../evidence/conditions-sets-068.md#c-b126b48d2ec72069) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015705

```text
(exec)# show isis * rib <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 17 `；EOL ` RVA 0x34B67E38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-29d9007a19cce439](../../evidence/conditions-sets-016.md#c-29d9007a19cce439) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-019897

```text
(exec)# show isis * rib prefix-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 34 `；EOL ` RVA 0x34B68540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-35fdffa7dd378760](../../evidence/conditions-sets-021.md#c-35fdffa7dd378760) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-b0748efddf77a62c](../../evidence/state_effects-sets-037.md#s-b0748efddf77a62c)

### path-019898

```text
(exec)# show isis * rib redistribution <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 18 `；EOL ` RVA 0x34B67AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8e6d6d4a9f67e1a1](../../evidence/conditions-sets-055.md#c-8e6d6d4a9f67e1a1) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-019910

```text
(exec)# show isis * rib strict-spf-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 35 `；EOL ` RVA 0x34B68880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-35fdffa7dd378760](../../evidence/conditions-sets-021.md#c-35fdffa7dd378760) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-05042ae034b6d339](../../evidence/state_effects-sets-002.md#s-05042ae034b6d339)

### path-015738

```text
(exec)# show isis * route <cr>
```

Handler ` RVA 0xFD35BD0 `；selector ` 2 `；EOL ` RVA 0x34B69BD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b126b48d2ec72069](../../evidence/conditions-sets-068.md#c-b126b48d2ec72069) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015644

```text
(exec)# show isis * spf-log <cr>
```

Handler ` RVA 0x10768B40 `；selector ` 3 `；EOL ` RVA 0x34B674B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-860246af44355d94](../../evidence/conditions-sets-052.md#c-860246af44355d94) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-14bd95c259d1df8f](../../evidence/state_effects-sets-005.md#s-14bd95c259d1df8f)

### path-015617

```text
(exec)# show isis * topology <cr>
```

Handler ` RVA 0x106B8970 `；selector ` 1 `；EOL ` RVA 0x34B66B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-860246af44355d94](../../evidence/conditions-sets-052.md#c-860246af44355d94) · [缺口 G-d37556bc956284ee](../../evidence/gaps-sets-007.md#g-d37556bc956284ee) · [状态效果 S-9a24405c69066f25](../../evidence/state_effects-sets-033.md#s-9a24405c69066f25)

### path-007323

```text
(exec)# show isis adjacency stagger <cr>
```

Handler ` RVA 0x106F9DE0 `；selector ` 13 `；EOL ` RVA 0x34B69630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d34f9eae4ddd8e97](../../evidence/conditions-sets-081.md#c-d34f9eae4ddd8e97) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003192

```text
(exec)# show isis database <cr>
```

Handler ` RVA 0x106B7B10 `；selector ` 0 `；EOL ` RVA 0x34B630A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-69f230da6e590a90](../../evidence/state_effects-sets-023.md#s-69f230da6e590a90)

### path-003115

```text
(exec)# show isis hostname <cr>
```

Handler ` RVA 0x10768F10 `；selector ` 10 `；EOL ` RVA 0x34B62158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d965e319e53f7d6](../../evidence/conditions-sets-018.md#c-2d965e319e53f7d6) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-003140

```text
(exec)# show isis lsp-log <cr>
```

Handler ` RVA 0x107666B0 `；selector ` 9 `；EOL ` RVA 0x34B62400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d965e319e53f7d6](../../evidence/conditions-sets-018.md#c-2d965e319e53f7d6) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-010022

```text
(exec)# show isis lspgen tlv neighbor <cr>
```

Handler ` RVA 0x10780F80 `；selector ` 43 `；EOL ` RVA 0x34B652D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-e30cf45064a95909](../../evidence/state_effects-sets-048.md#s-e30cf45064a95909)

### path-003336

```text
(exec)# show isis mesh-groups <cr>
```

Handler ` RVA 0x10769310 `；selector ` 14 `；EOL ` RVA 0x34B69290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d34f9eae4ddd8e97](../../evidence/conditions-sets-081.md#c-d34f9eae4ddd8e97) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003223

```text
(exec)# show isis mpls <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 21 `；EOL ` RVA 0x34B66288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-010021

```text
(exec)# show isis mpls ldp igp-shortcuts <cr>
```

Handler ` RVA 0x1E6FEF60 `；selector ` 27 `；EOL ` RVA 0x34B66358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-010011

```text
(exec)# show isis mpls traffic-eng adjacency-log <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 6 `；EOL ` RVA 0x34B65968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-010006

```text
(exec)# show isis mpls traffic-eng advertisements <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 5 `；EOL ` RVA 0x34B656C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-011459

```text
(exec)# show isis mpls traffic-eng downstream-tree <string> <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 7 `；EOL ` RVA 0x34B65CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` System ID in hostname or in the form of xxxx.xxxx.xxxx。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [参数 P-eb90314b48b3b746](../../evidence/parameters-sets-018.md#p-eb90314b48b3b746) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-010029

```text
(exec)# show isis mpls traffic-eng tunnel <cr>
```

Handler ` RVA 0x1E6FECE0 `；selector ` 8 `；EOL ` RVA 0x34B65FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-003339

```text
(exec)# show isis mt <cr>
```

Handler ` RVA 0x1076C920 `；selector ` 20 `；EOL ` RVA 0x34B68F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fda352b96b6f172e](../../evidence/conditions-sets-098.md#c-fda352b96b6f172e) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003123

```text
(exec)# show isis neighbors <cr>
```

Handler ` RVA 0x1076CB60 `；selector ` 4 `；EOL ` RVA 0x34B62738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-003261

```text
(exec)# show isis node <cr>
```

Handler ` RVA 0x106D25B0 `；selector ` 42 `；EOL ` RVA 0x34B64460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-00b2b241c602c3e3](../../evidence/state_effects-sets-001.md#s-00b2b241c602c3e3)

### path-003401

```text
(exec)# show isis nsf <cr>
```

Handler ` RVA 0x1076C1B0 `；selector ` 19 `；EOL ` RVA 0x33FCAB48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d34f9eae4ddd8e97](../../evidence/conditions-sets-081.md#c-d34f9eae4ddd8e97) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003159

```text
(exec)# show isis private <cr>
```

Handler ` RVA 0x1076B790 `；selector ` 16 `；EOL ` RVA 0x34B62D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-003354

```text
(exec)# show isis protocol <cr>
```

Handler ` RVA 0x10769A20 `；selector ` 12 `；EOL ` RVA 0x34B698E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d34f9eae4ddd8e97](../../evidence/conditions-sets-081.md#c-d34f9eae4ddd8e97) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003350

```text
(exec)# show isis rib <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 17 `；EOL ` RVA 0x34B67E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ac54b4794fb5ef4](../../evidence/conditions-sets-017.md#c-2ac54b4794fb5ef4) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-007302

```text
(exec)# show isis rib prefix-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 34 `；EOL ` RVA 0x34B68540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8855f184e6b2ccca](../../evidence/conditions-sets-053.md#c-8855f184e6b2ccca) · [状态效果 S-2087673e8fcb024c](../../evidence/state_effects-sets-007.md#s-2087673e8fcb024c)

### path-007303

```text
(exec)# show isis rib redistribution <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 18 `；EOL ` RVA 0x34B67AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1fe18653b9ad4336](../../evidence/conditions-sets-012.md#c-1fe18653b9ad4336) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-007313

```text
(exec)# show isis rib strict-spf-sid <cr>
```

Handler ` RVA 0x1076C3C0 `；selector ` 35 `；EOL ` RVA 0x34B68880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8855f184e6b2ccca](../../evidence/conditions-sets-053.md#c-8855f184e6b2ccca) · [状态效果 S-78d1dcee462900c1](../../evidence/state_effects-sets-026.md#s-78d1dcee462900c1)

### path-003374

```text
(exec)# show isis route <cr>
```

Handler ` RVA 0xFD35BD0 `；selector ` 2 `；EOL ` RVA 0x34B69BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d34f9eae4ddd8e97](../../evidence/conditions-sets-081.md#c-d34f9eae4ddd8e97) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003302

```text
(exec)# show isis spf-log <cr>
```

Handler ` RVA 0x10768B40 `；selector ` 3 `；EOL ` RVA 0x34B674B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-60123fe2acc90a3e](../../evidence/state_effects-sets-021.md#s-60123fe2acc90a3e)

### path-003116

```text
(exec)# show isis timers <cr>
```

Handler ` RVA 0x10769C20 `；selector ` 11 `；EOL ` RVA 0x34B62A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-856d8ed1bce8c599](../../evidence/state_effects-sets-028.md#s-856d8ed1bce8c599)

### path-003272

```text
(exec)# show isis topology <cr>
```

Handler ` RVA 0x106B8970 `；selector ` 1 `；EOL ` RVA 0x34B66B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91c21b0044adc86e](../../evidence/conditions-sets-056.md#c-91c21b0044adc86e) · [状态效果 S-ff400c60f9b9cd2e](../../evidence/state_effects-sets-054.md#s-ff400c60f9b9cd2e)

### path-003180

```text
(exec)# show isis tree <cr>
```

Handler ` RVA 0x106B8630 `；selector ` 0 `；EOL ` RVA 0x34B61DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d965e319e53f7d6](../../evidence/conditions-sets-018.md#c-2d965e319e53f7d6) · [状态效果 S-b193120a07fa126f](../../evidence/state_effects-sets-038.md#s-b193120a07fa126f)

### path-003786

```text
(exec)# show issu FSM <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 16 `；EOL ` RVA 0x33E5DFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007648

```text
(exec)# show issu FSM <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 17 `；EOL ` RVA 0x33E5DFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-3786898db2265749](../../evidence/parameters-sets-005.md#p-3786898db2265749) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007633

```text
(exec)# show issu capability types <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 8 `；EOL ` RVA 0x33E5C858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-ecb96c55e0a1b00e](../../evidence/state_effects-sets-050.md#s-ecb96c55e0a1b00e)

### path-010264

```text
(exec)# show issu capability types <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 9 `；EOL ` RVA 0x33E5C8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-7a8151b894eb0d6b](../../evidence/parameters-sets-010.md#p-7a8151b894eb0d6b) · [状态效果 S-ecb96c55e0a1b00e](../../evidence/state_effects-sets-050.md#s-ecb96c55e0a1b00e)

### path-011573

```text
(exec)# show issu capability types <number:1..8035> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 10 `；EOL ` RVA 0x33E5C8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID；` unsigned_number ` Entity ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-2e4be3649c0d169e](../../evidence/parameters-sets-004.md#p-2e4be3649c0d169e) · [状态效果 S-ecb96c55e0a1b00e](../../evidence/state_effects-sets-050.md#s-ecb96c55e0a1b00e)

### path-003728

```text
(exec)# show issu clients <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 1 `；EOL ` RVA 0x33E5B758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016118

```text
(exec)# show issu clients <number:dynamic> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 1 `；EOL ` RVA 0x33E5B758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` peer uid。

[条件 C-b89124dc189dae39](../../evidence/conditions-sets-071.md#c-b89124dc189dae39) · [缺口 G-614b46b29da7c1f5](../../evidence/gaps-sets-004.md#g-614b46b29da7c1f5) · [参数 P-0742ad430ad11dfe](../../evidence/parameters-sets-001.md#p-0742ad430ad11dfe) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007584

```text
(exec)# show issu clients distributed <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 2 `；EOL ` RVA 0x33E5B4B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007661

```text
(exec)# show issu comp-matrix stored <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 18 `；EOL ` RVA 0x33E5E500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-f6017354a30790f2](../../evidence/state_effects-sets-052.md#s-f6017354a30790f2)

### path-003686

```text
(exec)# show issu endpoints <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 0 `；EOL ` RVA 0x33E5B1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003726

```text
(exec)# show issu entities <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 3 `；EOL ` RVA 0x33E5BA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007592

```text
(exec)# show issu entities <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 4 `；EOL ` RVA 0x33E5BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-95068abb77fab82f](../../evidence/parameters-sets-011.md#p-95068abb77fab82f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007585

```text
(exec)# show issu image-version compatibility <cr>
```

Handler ` RVA 0xC795B00 `；selector ` 0 `；EOL ` RVA 0x33AEEA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007646

```text
(exec)# show issu message types <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 11 `；EOL ` RVA 0x33E5D178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-faa41cee641e2660](../../evidence/state_effects-sets-053.md#s-faa41cee641e2660)

### path-010269

```text
(exec)# show issu message types <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 12 `；EOL ` RVA 0x33E5D1E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-35ab82c68173873e](../../evidence/parameters-sets-005.md#p-35ab82c68173873e) · [状态效果 S-faa41cee641e2660](../../evidence/state_effects-sets-053.md#s-faa41cee641e2660)

### path-011575

```text
(exec)# show issu message types <number:1..8035> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 13 `；EOL ` RVA 0x33E5D1C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID；` unsigned_number ` Entity ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-9d748ae178a27ee3](../../evidence/parameters-sets-012.md#p-9d748ae178a27ee3) · [状态效果 S-faa41cee641e2660](../../evidence/state_effects-sets-053.md#s-faa41cee641e2660)

### path-007659

```text
(exec)# show issu negotiated capability <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 14 `；EOL ` RVA 0x33E5DA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3f0231d090249294](../../evidence/state_effects-sets-014.md#s-3f0231d090249294)

### path-010265

```text
(exec)# show issu negotiated capability <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 15 `；EOL ` RVA 0x33E5DA10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-a550057b702b975a](../../evidence/parameters-sets-013.md#p-a550057b702b975a) · [状态效果 S-3f0231d090249294](../../evidence/state_effects-sets-014.md#s-3f0231d090249294)

### path-003741

```text
(exec)# show issu sessions <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 5 `；EOL ` RVA 0x33E5BFD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007619

```text
(exec)# show issu sessions <number:1..8035> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 6 `；EOL ` RVA 0x33E5C048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-cc85f03b59e13e56](../../evidence/parameters-sets-015.md#p-cc85f03b59e13e56) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010251

```text
(exec)# show issu sessions <number:1..8035> <number:1..4294967295> <cr>
```

Handler ` RVA 0xD4B3A40 `；selector ` 7 `；EOL ` RVA 0x33E5C020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client ID；` unsigned_number ` Entity ID。

[条件 C-a7b38c09c785f353](../../evidence/conditions-sets-065.md#c-a7b38c09c785f353) · [参数 P-bd364dc6ecbe4858](../../evidence/parameters-sets-014.md#p-bd364dc6ecbe4858) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001577

```text
(exec)# show kerberos creds <cr>
```

Handler ` RVA 0xC3E3030 `；selector ` 5 `；EOL ` RVA 0x33A6AFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003438

```text
(exec)# show key chain <cr>
```

Handler ` RVA 0xFDBAB60 `；selector ` 0 `；EOL ` RVA 0x348CE238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000315

```text
(exec)# show keystore <cr>
```

Handler ` RVA 0x136EAC70 `；selector ` 0 `；EOL ` RVA 0x35C0BDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003952

```text
(exec)# show kron schedule <cr>
```

Handler ` RVA 0xF3BA710 `；selector ` 0 `；EOL ` RVA 0x34624D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014105

```text
(exec)# show l2fib bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 0 `；EOL ` RVA 0x33AFC170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-024768

```text
(exec)# show l2fib bridge-domain <number:dynamic> address multicast <address> <address> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 3 `；EOL ` RVA 0x33AF9DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number；` address ` Source or Group IPv4 address；` address ` Group IPv4 address。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-3f5c4381a447f58d](../../evidence/parameters-sets-005.md#p-3f5c4381a447f58d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-023972

```text
(exec)# show l2fib bridge-domain <number:dynamic> address unicast <address> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 4 `；EOL ` RVA 0x33AF9A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number；` address ` MAC Address。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-2886aca62db9b90e](../../evidence/parameters-sets-003.md#p-2886aca62db9b90e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021836

```text
(exec)# show l2fib bridge-domain <number:dynamic> lisp decap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 22 `；EOL ` RVA 0x33AFB0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021830

```text
(exec)# show l2fib bridge-domain <number:dynamic> lisp encap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 23 `；EOL ` RVA 0x33AFAE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021843

```text
(exec)# show l2fib bridge-domain <number:dynamic> lisp mac_oce <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 21 `；EOL ` RVA 0x33AFB370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021841

```text
(exec)# show l2fib bridge-domain <number:dynamic> mpls mac_oce <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 15 `；EOL ` RVA 0x33AFBEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021833

```text
(exec)# show l2fib bridge-domain <number:dynamic> otv decap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 11 `；EOL ` RVA 0x33AFAB20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-023975

```text
(exec)# show l2fib bridge-domain <number:dynamic> otv encap <address> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 10 `；EOL ` RVA 0x33AFA860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number；` address ` Encap IPv4 address。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-02cee063ecfb9acb](../../evidence/parameters-sets-001.md#p-02cee063ecfb9acb) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017921

```text
(exec)# show l2fib bridge-domain <number:dynamic> port <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 5 `；EOL ` RVA 0x33AF9658 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021826

```text
(exec)# show l2fib bridge-domain <number:dynamic> table multicast <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 2 `；EOL ` RVA 0x33AFA4F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021817

```text
(exec)# show l2fib bridge-domain <number:dynamic> table unicast <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 1 `；EOL ` RVA 0x33AFA250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021842

```text
(exec)# show l2fib bridge-domain <number:dynamic> vxlan decap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 13 `；EOL ` RVA 0x33AFB928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021835

```text
(exec)# show l2fib bridge-domain <number:dynamic> vxlan encap <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 12 `；EOL ` RVA 0x33AFB680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021851

```text
(exec)# show l2fib bridge-domain <number:dynamic> vxlan mac_oce <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 14 `；EOL ` RVA 0x33AFBBD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-c681c595d70b2f73](../../evidence/conditions-sets-076.md#c-c681c595d70b2f73) · [缺口 G-755f15eff51ac4b4](../../evidence/gaps-sets-005.md#g-755f15eff51ac4b4) · [参数 P-ef791d15f6aedcba](../../evidence/parameters-sets-018.md#p-ef791d15f6aedcba) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005407

```text
(exec)# show l2fib bridge-domain detail <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 8 `；EOL ` RVA 0x33AF92D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005384

```text
(exec)# show l2fib bridge-domain summary <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 7 `；EOL ` RVA 0x33AF9030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009054

```text
(exec)# show l2fib evpn ead local <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 24 `；EOL ` RVA 0x33AFDEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009062

```text
(exec)# show l2fib evpn ead remote <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 25 `；EOL ` RVA 0x33AFE1D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005402

```text
(exec)# show l2fib log event <cr>
```

Handler ` RVA 0xC7A3F10 `；selector ` 0 `；EOL ` RVA 0x33AF8650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2526630454c71793](../../evidence/state_effects-sets-008.md#s-2526630454c71793)

### path-001681

```text
(exec)# show l2fib next-hop-list <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 27 `；EOL ` RVA 0x33AFCBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001661

```text
(exec)# show l2fib output-list <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 9 `；EOL ` RVA 0x33AFC4E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001682

```text
(exec)# show l2fib path-list <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 26 `；EOL ` RVA 0x33AFC878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017964

```text
(exec)# show l2fib statistics bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 18 `；EOL ` RVA 0x33AFDB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge domain number。

[条件 C-89db18b42f7f0bd9](../../evidence/conditions-sets-053.md#c-89db18b42f7f0bd9) · [缺口 G-cafa7f697b4ecabd](../../evidence/gaps-sets-007.md#g-cafa7f697b4ecabd) · [参数 P-7a4937dc4a997b07](../../evidence/parameters-sets-010.md#p-7a4937dc4a997b07) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005455

```text
(exec)# show l2fib statistics detail <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 17 `；EOL ` RVA 0x33AFD348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005478

```text
(exec)# show l2fib statistics events <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 19 `；EOL ` RVA 0x33AFD680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009058

```text
(exec)# show l2fib statistics events history <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 20 `；EOL ` RVA 0x33AFD658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005439

```text
(exec)# show l2fib statistics summary <cr>
```

Handler ` RVA 0xC7A6090 `；selector ` 16 `；EOL ` RVA 0x33AFD0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000508

```text
(exec)# show l2protocol-forward <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 29 `；EOL ` RVA 0x35E8EAA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000507

```text
(exec)# show l2protocol-tunnel <cr>
```

Handler ` RVA 0x15FDB140 `；selector ` 12 `；EOL ` RVA 0x35E8E678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002384

```text
(exec)# show l2rib clients <cr>
```

Handler ` RVA 0x12566CD0 `；selector ` 0 `；EOL ` RVA 0x358B3B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-bc1596ef92c89df2](../../evidence/state_effects-sets-040.md#s-bc1596ef92c89df2)

### path-002378

```text
(exec)# show l2rib counters <cr>
```

Handler ` RVA 0x12567A60 `；selector ` 0 `；EOL ` RVA 0x358B4888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-935346406ba41e9b](../../evidence/conditions-sets-057.md#c-935346406ba41e9b) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002381

```text
(exec)# show l2rib deletions <cr>
```

Handler ` RVA 0x125677B0 `；selector ` 0 `；EOL ` RVA 0x358B45F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93f75654e0185b22](../../evidence/conditions-sets-057.md#c-93f75654e0185b22) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006863

```text
(exec)# show l2rib multicast route <cr>
```

Handler ` RVA 0xC88D6E0 `；selector ` 1 `；EOL ` RVA 0x33B08858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd91832d34195f99](../../evidence/conditions-sets-098.md#c-fd91832d34195f99) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002359

```text
(exec)# show l2rib notifications <cr>
```

Handler ` RVA 0x12567680 `；selector ` 0 `；EOL ` RVA 0x358B42C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fa6fdcf9660e4d3f](../../evidence/conditions-sets-097.md#c-fa6fdcf9660e4d3f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002383

```text
(exec)# show l2rib producers <cr>
```

Handler ` RVA 0x125672F0 `；selector ` 0 `；EOL ` RVA 0x358B3F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-bb2e50ad5811ada0](../../evidence/state_effects-sets-040.md#s-bb2e50ad5811ada0)

### path-002385

```text
(exec)# show l2rib registrations <cr>
```

Handler ` RVA 0x125666A0 `；selector ` 0 `；EOL ` RVA 0x358B3760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-8de202eeff187542](../../evidence/state_effects-sets-030.md#s-8de202eeff187542)

### path-009537

```text
(exec)# show l2rib test <string> msg-buffer <cr>
```

Handler ` RVA 0x125CDA60 `；selector ` 0 `；EOL ` RVA 0x358BF148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-9395b657dd675530](../../evidence/conditions-sets-057.md#c-9395b657dd675530) · [参数 P-56c359cd28967776](../../evidence/parameters-sets-007.md#p-56c359cd28967776) · [状态效果 S-078b85622e70ff40](../../evidence/state_effects-sets-002.md#s-078b85622e70ff40)

### path-002346

```text
(exec)# show l2rib topologies <cr>
```

Handler ` RVA 0x12566200 `；selector ` 0 `；EOL ` RVA 0x358B2FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-c95d61022e2de6ac](../../evidence/state_effects-sets-043.md#s-c95d61022e2de6ac)

### path-006852

```text
(exec)# show l2rib unicast route <cr>
```

Handler ` RVA 0xC88D6E0 `；selector ` 0 `；EOL ` RVA 0x33B08588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd91832d34195f99](../../evidence/conditions-sets-098.md#c-fd91832d34195f99) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006448

```text
(exec)# show l2route evpn summary <cr>
```

Handler ` RVA 0x125C8E60 `；selector ` 0 `；EOL ` RVA 0x358B6C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-467b3b729f2e938b](../../evidence/state_effects-sets-015.md#s-467b3b729f2e938b)

### path-016623

```text
(exec)# show lacp <number:dynamic> counters <cr>
```

Handler ` RVA 0xC8D30C0 `；selector ` 0 `；EOL ` RVA 0x33B143B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-f65999b957bee6e8](../../evidence/conditions-sets-095.md#c-f65999b957bee6e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016633

```text
(exec)# show lacp <number:dynamic> internal <cr>
```

Handler ` RVA 0xC8D3050 `；selector ` 0 `；EOL ` RVA 0x33B146C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-f65999b957bee6e8](../../evidence/conditions-sets-095.md#c-f65999b957bee6e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016625

```text
(exec)# show lacp <number:dynamic> neighbor <cr>
```

Handler ` RVA 0xC8D2FE0 `；selector ` 0 `；EOL ` RVA 0x33B14118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-f65999b957bee6e8](../../evidence/conditions-sets-095.md#c-f65999b957bee6e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016631

```text
(exec)# show lacp <number:dynamic> sm-state <cr>
```

Handler ` RVA 0xC8D3260 `；selector ` 0 `；EOL ` RVA 0x33B14968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Channel group number。

[条件 C-f65999b957bee6e8](../../evidence/conditions-sets-095.md#c-f65999b957bee6e8) · [缺口 G-75d44ae2cde48e14](../../evidence/gaps-sets-005.md#g-75d44ae2cde48e14) · [参数 P-0f3d8edd9bac5de5](../../evidence/parameters-sets-002.md#p-0f3d8edd9bac5de5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004201

```text
(exec)# show lacp counters <cr>
```

Handler ` RVA 0xC8D30C0 `；selector ` 0 `；EOL ` RVA 0x33B143B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004208

```text
(exec)# show lacp internal <cr>
```

Handler ` RVA 0xC8D3050 `；selector ` 0 `；EOL ` RVA 0x33B146C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008037

```text
(exec)# show lacp multi-chassis group <cr>
```

Handler ` RVA 0xC961EC0 `；selector ` 0 `；EOL ` RVA 0x33B33CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010450

```text
(exec)# show lacp multi-chassis load-balance group <cr>
```

Handler ` RVA 0xC963BC0 `；selector ` 0 `；EOL ` RVA 0x33B34660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f4fdb74b2e125cbd](../../evidence/conditions-sets-094.md#c-f4fdb74b2e125cbd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010453

```text
(exec)# show lacp multi-chassis load-balance port-channel <cr>
```

Handler ` RVA 0xC963BC0 `；selector ` 2 `；EOL ` RVA 0x33B349D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1b442a5d33a8aa33](../../evidence/conditions-sets-011.md#c-1b442a5d33a8aa33) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-023295

```text
(exec)# show lacp multi-chassis load-balance port-channel <interface> <cr>
```

Handler ` RVA 0xC963BC0 `；selector ` 1 `；EOL ` RVA 0x33B349A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-16031248c8823d65](../../evidence/conditions-sets-009.md#c-16031248c8823d65) · [缺口 G-a78e54fbf9c0bec8](../../evidence/gaps-sets-006.md#g-a78e54fbf9c0bec8) · [参数 P-627606ef8ad93af2](../../evidence/parameters-sets-008.md#p-627606ef8ad93af2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008040

```text
(exec)# show lacp multi-chassis port-channel <cr>
```

Handler ` RVA 0xC961EC0 `；selector ` 2 `；EOL ` RVA 0x33B34078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05d7c47003e6d723](../../evidence/conditions-sets-003.md#c-05d7c47003e6d723) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-020690

```text
(exec)# show lacp multi-chassis port-channel <interface> <cr>
```

Handler ` RVA 0xC961EC0 `；selector ` 1 `；EOL ` RVA 0x33B34050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0f0924f254926f8d](../../evidence/conditions-sets-006.md#c-0f0924f254926f8d) · [缺口 G-6b74398a5042923d](../../evidence/gaps-sets-004.md#g-6b74398a5042923d) · [参数 P-fdc0d7a33fc2633d](../../evidence/parameters-sets-019.md#p-fdc0d7a33fc2633d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004203

```text
(exec)# show lacp neighbor <cr>
```

Handler ` RVA 0xC8D2FE0 `；selector ` 0 `；EOL ` RVA 0x33B14118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004207

```text
(exec)# show lacp sm-state <cr>
```

Handler ` RVA 0xC8D3260 `；selector ` 0 `；EOL ` RVA 0x33B14968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004190

```text
(exec)# show lacp sys-id <cr>
```

Handler ` RVA 0xC8D31D0 `；selector ` 0 `；EOL ` RVA 0x33B11658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003520

```text
(exec)# show ldap attributes <cr>
```

Handler ` RVA 0x11ABB210 `；selector ` 22 `；EOL ` RVA 0x3560D6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c607d93f990fb8f](../../evidence/conditions-sets-023.md#c-3c607d93f990fb8f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007462

```text
(exec)# show ldap server all <cr>
```

Handler ` RVA 0x11ABAFB0 `；selector ` 23 `；EOL ` RVA 0x3560D298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c607d93f990fb8f](../../evidence/conditions-sets-023.md#c-3c607d93f990fb8f) · [状态效果 S-91ee0a5573625510](../../evidence/state_effects-sets-031.md#s-91ee0a5573625510)

### path-001288

```text
(exec)# show license udi <cr>
```

Handler ` RVA 0xBB467A0 `；selector ` 0 `；EOL ` RVA 0x33854DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f555b39f930d780](../../evidence/conditions-sets-037.md#c-5f555b39f930d780) · [状态效果 S-382eb02cde83b222](../../evidence/state_effects-sets-012.md#s-382eb02cde83b222)

### path-012822

```text
(exec)# show line <?ttyline_action@5555896d0f80> <cr>
```

Handler ` RVA 0xE2CC610 `；selector ` 0 `；EOL ` RVA 0x3417D010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-255b2083e4794b1d](../../evidence/gaps-sets-002.md#g-255b2083e4794b1d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016646

```text
(exec)# show line <?ttyline_action@5555896d0f80> history <cr>
```

Handler ` RVA 0xE2CC3F0 `；selector ` 0 `；EOL ` RVA 0x3417D2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-255b2083e4794b1d](../../evidence/gaps-sets-002.md#g-255b2083e4794b1d) · [状态效果 S-df5cbb485b43d657](../../evidence/state_effects-sets-047.md#s-df5cbb485b43d657)

### path-004231

```text
(exec)# show line async-queue <cr>
```

Handler ` RVA 0xCCFA910 `；selector ` 0 `；EOL ` RVA 0x33C67D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2b8981fda30c24da](../../evidence/state_effects-sets-010.md#s-2b8981fda30c24da)

### path-004218

```text
(exec)# show line x121-address <cr>
```

Handler ` RVA 0xFE59A10 `；selector ` 0 `；EOL ` RVA 0x34903960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000447

```text
(exec)# show list <cr>
```

Handler ` RVA 0xDEC7820 `；selector ` 0 `；EOL ` RVA 0x34092988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000513

```text
(exec)# show llc2 <cr>
```

Handler ` RVA 0xFDDE720 `；selector ` 0 `；EOL ` RVA 0x348DF260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000323

```text
(exec)# show lldp <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 0 `；EOL ` RVA 0x35DA0DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-063e175de48badf4](../../evidence/conditions-sets-003.md#c-063e175de48badf4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002535

```text
(exec)# show lldp custom-information <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 7 `；EOL ` RVA 0x35DA0D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcd9d48382f9f870](../../evidence/conditions-sets-098.md#c-fcd9d48382f9f870) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-006593

```text
(exec)# show lldp entry <string> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 3 `；EOL ` RVA 0x35DA0AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of LLDP neighbor entry。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-3b6d72de4a6a3586](../../evidence/parameters-sets-005.md#p-3b6d72de4a6a3586) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002466

```text
(exec)# show lldp errors <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 1 `；EOL ` RVA 0x35DA0328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002476

```text
(exec)# show lldp interface <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 4 `；EOL ` RVA 0x35D9FAE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3875d945466392b5](../../evidence/conditions-sets-022.md#c-3875d945466392b5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014817

```text
(exec)# show lldp interface <interface> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 4 `；EOL ` RVA 0x35D9FAE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ade62bab20ceab3](../../evidence/conditions-sets-005.md#c-0ade62bab20ceab3) · [缺口 G-dbf9e654ab69a040](../../evidence/gaps-sets-008.md#g-dbf9e654ab69a040) · [参数 P-907042f9602b04c9](../../evidence/parameters-sets-011.md#p-907042f9602b04c9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-022340

```text
(exec)# show lldp interface <interface> service-instance <number:1..8000> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 6 `；EOL ` RVA 0x35D9FB68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Service instance ID。

[条件 C-0ade62bab20ceab3](../../evidence/conditions-sets-005.md#c-0ade62bab20ceab3) · [缺口 G-dbf9e654ab69a040](../../evidence/gaps-sets-008.md#g-dbf9e654ab69a040) · [参数 P-385adecdcbe4e02a](../../evidence/parameters-sets-005.md#p-385adecdcbe4e02a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002541

```text
(exec)# show lldp neighbors <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 5 `；EOL ` RVA 0x35DA0720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-96bea1d405be8d50](../../evidence/conditions-sets-058.md#c-96bea1d405be8d50) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014860

```text
(exec)# show lldp neighbors <interface> <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 5 `；EOL ` RVA 0x35DA0720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a660d0b8f1c968f3](../../evidence/conditions-sets-064.md#c-a660d0b8f1c968f3) · [缺口 G-0fcf6a92b14704e7](../../evidence/gaps-sets-001.md#g-0fcf6a92b14704e7) · [参数 P-60a71d44b1209092](../../evidence/parameters-sets-008.md#p-60a71d44b1209092) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002450

```text
(exec)# show lldp traffic <cr>
```

Handler ` RVA 0x158A0DC0 `；selector ` 2 `；EOL ` RVA 0x35DA0080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007074

```text
(exec)# show llp nhrp multicast <cr>
```

Handler ` RVA 0x108D5B20 `；selector ` 4 `；EOL ` RVA 0x34BF3A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-499b0aef67aa9fe8](../../evidence/conditions-sets-029.md#c-499b0aef67aa9fe8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019621

```text
(exec)# show llp nhrp multicast <interface> <cr>
```

Handler ` RVA 0x108D5B20 `；selector ` 4 `；EOL ` RVA 0x34BF3A28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11f96da6ae2ad225](../../evidence/conditions-sets-007.md#c-11f96da6ae2ad225) · [缺口 G-156a48b5df198e8b](../../evidence/gaps-sets-001.md#g-156a48b5df198e8b) · [参数 P-09f6060c19ea1e59](../../evidence/parameters-sets-001.md#p-09f6060c19ea1e59) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004217

```text
(exec)# show lnm bridge <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 0 `；EOL ` RVA 0x358130F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e540daa4336ac954](../../evidence/conditions-sets-088.md#c-e540daa4336ac954) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016640

```text
(exec)# show lnm bridge <interface> <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 0 `；EOL ` RVA 0x358130F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-31bff4c039255d0c](../../evidence/conditions-sets-020.md#c-31bff4c039255d0c) · [缺口 G-8de02418a8b4cb45](../../evidence/gaps-sets-005.md#g-8de02418a8b4cb45) · [参数 P-9cede3b9f0a6cff9](../../evidence/parameters-sets-012.md#p-9cede3b9f0a6cff9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004213

```text
(exec)# show lnm config <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 1 `；EOL ` RVA 0x358133B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aad82b05e4a98db](../../evidence/conditions-sets-048.md#c-7aad82b05e4a98db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004225

```text
(exec)# show lnm interface <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 2 `；EOL ` RVA 0x35813748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2588d9dd1bc8db5c](../../evidence/conditions-sets-015.md#c-2588d9dd1bc8db5c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016645

```text
(exec)# show lnm interface <interface> <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 2 `；EOL ` RVA 0x35813748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b0e7ba0ded1c097](../../evidence/conditions-sets-023.md#c-3b0e7ba0ded1c097) · [缺口 G-6942553203c46ef5](../../evidence/gaps-sets-004.md#g-6942553203c46ef5) · [参数 P-f4fafee86455cf57](../../evidence/parameters-sets-018.md#p-f4fafee86455cf57) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004223

```text
(exec)# show lnm ring <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 3 `；EOL ` RVA 0x35813A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aad82b05e4a98db](../../evidence/conditions-sets-048.md#c-7aad82b05e4a98db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016654

```text
(exec)# show lnm station * <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 4 `；EOL ` RVA 0x35813DC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d0701d1f03e9ebd](../../evidence/conditions-sets-018.md#c-2d0701d1f03e9ebd) · [缺口 G-99894fa3a7b75931](../../evidence/gaps-sets-006.md#g-99894fa3a7b75931) · [状态效果 S-aad54a862692b207](../../evidence/state_effects-sets-036.md#s-aad54a862692b207)

### path-004232

```text
(exec)# show lnm station <cr>
```

Handler ` RVA 0x1233AF00 `；selector ` 4 `；EOL ` RVA 0x35813DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7aad82b05e4a98db](../../evidence/conditions-sets-048.md#c-7aad82b05e4a98db) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000496

```text
(exec)# show local-ack <cr>
```

Handler ` RVA 0x114A98F0 `；selector ` 0 `；EOL ` RVA 0x354FA698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8257e4ef4b603204](../../evidence/conditions-sets-051.md#c-8257e4ef4b603204) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000093

```text
(exec)# show location <cr>
```

Handler ` RVA 0xD7987F0 `；selector ` 0 `；EOL ` RVA 0x34126998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000601

```text
(exec)# show location admin-tag <cr>
```

Handler ` RVA 0xC916150 `；selector ` 1 `；EOL ` RVA 0x33B1E920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000694

```text
(exec)# show location ap-proximity <cr>
```

Handler ` RVA 0xC916150 `；selector ` 8 `；EOL ` RVA 0x33B20990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7da677db4e6a9ad3](../../evidence/conditions-sets-049.md#c-7da677db4e6a9ad3) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004373

```text
(exec)# show location civic-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 2 `；EOL ` RVA 0x33B1ED58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-29e2a9430e39872e](../../evidence/state_effects-sets-009.md#s-29e2a9430e39872e)

### path-004394

```text
(exec)# show location custom-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 4 `；EOL ` RVA 0x33B1F8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-a848873faba86ca8](../../evidence/state_effects-sets-036.md#s-a848873faba86ca8)

### path-004381

```text
(exec)# show location elin-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 3 `；EOL ` RVA 0x33B1F318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-79b77aa5d7a278c2](../../evidence/state_effects-sets-026.md#s-79b77aa5d7a278c2)

### path-004449

```text
(exec)# show location fex all <cr>
```

Handler ` RVA 0xC916150 `；selector ` 7 `；EOL ` RVA 0x33B20650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5b1d9e52302b903](../../evidence/conditions-sets-089.md#c-e5b1d9e52302b903) · [状态效果 S-eb86aa9c3461a4cc](../../evidence/state_effects-sets-050.md#s-eb86aa9c3461a4cc)

### path-004412

```text
(exec)# show location geo-location static <cr>
```

Handler ` RVA 0xC916150 `；selector ` 6 `；EOL ` RVA 0x33B1FE98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-4c88f63a6178f806](../../evidence/state_effects-sets-017.md#s-4c88f63a6178f806)

### path-000657

```text
(exec)# show location host <cr>
```

Handler ` RVA 0xC916150 `；selector ` 5 `；EOL ` RVA 0x33B202C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000171

```text
(exec)# show logging <cr>
```

Handler ` RVA 0xE0737A0 `；selector ` 0 `；EOL ` RVA 0x341908E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000834

```text
(exec)# show logging count <cr>
```

Handler ` RVA 0xE073560 `；selector ` 0 `；EOL ` RVA 0x34190370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000835

```text
(exec)# show logging history <cr>
```

Handler ` RVA 0x123A1530 `；selector ` 0 `；EOL ` RVA 0x358327C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004560

```text
(exec)# show logging last <number:1..214748364> <cr>
```

Handler ` RVA 0xE0732A0 `；selector ` 0 `；EOL ` RVA 0x341900E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of lines。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-751e6c29ba38d6bd](../../evidence/parameters-sets-009.md#p-751e6c29ba38d6bd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000919

```text
(exec)# show logging persistent <cr>
```

Handler ` RVA 0xE06B420 `；selector ` 0 `；EOL ` RVA 0x341909E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000861

```text
(exec)# show logging xml <cr>
```

Handler ` RVA 0xE0735C0 `；selector ` 0 `；EOL ` RVA 0x34190618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000275

```text
(exec)# show login <cr>
```

Handler ` RVA 0xCFD4180 `；selector ` 0 `；EOL ` RVA 0x33D76290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001733

```text
(exec)# show login failures <cr>
```

Handler ` RVA 0xCFD4550 `；selector ` 0 `；EOL ` RVA 0x33D76268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004198

```text
(exec)# show mac address-table <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 4 `；EOL ` RVA 0x35E53230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c89eeeb9b7f10004](../../evidence/conditions-sets-077.md#c-c89eeeb9b7f10004) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008010

```text
(exec)# show mac address-table aging-time <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 3 `；EOL ` RVA 0x35E552A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008007

```text
(exec)# show mac address-table control-packet-learn <cr>
```

Handler ` RVA 0x15C438F0 `；selector ` 0 `；EOL ` RVA 0x35E555B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7735f227e587064a](../../evidence/conditions-sets-046.md#c-7735f227e587064a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008005

```text
(exec)# show mac address-table count <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 1 `；EOL ` RVA 0x35E54988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008017

```text
(exec)# show mac address-table multicast <cr>
```

Handler ` RVA 0x15E77B60 `；selector ` 2 `；EOL ` RVA 0x35E54E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbcfde8155b652a7](../../evidence/conditions-sets-085.md#c-dbcfde8155b652a7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000322

```text
(exec)# show macdb <cr>
```

Handler ` RVA 0x1339C500 `；selector ` 0 `；EOL ` RVA 0x35A7C198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce1553fe7d308f85](../../evidence/conditions-sets-079.md#c-ce1553fe7d308f85) · [状态效果 S-b71a6d04016112d1](../../evidence/state_effects-sets-039.md#s-b71a6d04016112d1)

### path-001480

```text
(exec)# show macsec hw <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 8 `；EOL ` RVA 0x35ED5AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8053662e73b63e6d](../../evidence/conditions-sets-050.md#c-8053662e73b63e6d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005273

```text
(exec)# show macsec hw detail <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 9 `；EOL ` RVA 0x35ED5A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8053662e73b63e6d](../../evidence/conditions-sets-050.md#c-8053662e73b63e6d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001509

```text
(exec)# show macsec mka-request-notify <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 6 `；EOL ` RVA 0x35ED62A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8053662e73b63e6d](../../evidence/conditions-sets-050.md#c-8053662e73b63e6d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005309

```text
(exec)# show macsec mka-request-notify clear <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 7 `；EOL ` RVA 0x35ED6280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8053662e73b63e6d](../../evidence/conditions-sets-050.md#c-8053662e73b63e6d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001476

```text
(exec)# show macsec post <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 10 `；EOL ` RVA 0x35ED5F70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8053662e73b63e6d](../../evidence/conditions-sets-050.md#c-8053662e73b63e6d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017818

```text
(exec)# show macsec statistics interface <interface> <cr>
```

Handler ` RVA 0x1610BE60 `；selector ` 2 `；EOL ` RVA 0x35ED7030 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c4bf4f7664ab4f46](../../evidence/conditions-sets-076.md#c-c4bf4f7664ab4f46) · [缺口 G-2f015fa58f5a94fa](../../evidence/gaps-sets-002.md#g-2f015fa58f5a94fa) · [参数 P-4310063a2b8ba071](../../evidence/parameters-sets-006.md#p-4310063a2b8ba071) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017834

```text
(exec)# show macsec statistics interface <interface> <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 2 `；EOL ` RVA 0x35ED72D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-254495a7a5f02362](../../evidence/conditions-sets-014.md#c-254495a7a5f02362) · [缺口 G-2f015fa58f5a94fa](../../evidence/gaps-sets-002.md#g-2f015fa58f5a94fa) · [参数 P-4310063a2b8ba071](../../evidence/parameters-sets-006.md#p-4310063a2b8ba071) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025359

```text
(exec)# show macsec statistics interface <interface> rx-sci <hex-string> <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 5 `；EOL ` RVA 0x35ED78F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` 64-bit Hexadecimal Local Rx-SCI。

[条件 C-1736dfb449b882b7](../../evidence/conditions-sets-009.md#c-1736dfb449b882b7) · [缺口 G-2f47edcd6919fc57](../../evidence/gaps-sets-002.md#g-2f47edcd6919fc57) · [参数 P-51a640767f0406f1](../../evidence/parameters-sets-007.md#p-51a640767f0406f1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-021776

```text
(exec)# show macsec statistics interface <interface> secy <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 4 `；EOL ` RVA 0x35ED7608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b646814bff406e29](../../evidence/conditions-sets-070.md#c-b646814bff406e29) · [缺口 G-2f015fa58f5a94fa](../../evidence/gaps-sets-002.md#g-2f015fa58f5a94fa) · [参数 P-4310063a2b8ba071](../../evidence/parameters-sets-006.md#p-4310063a2b8ba071) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017808

```text
(exec)# show macsec status interface <interface> <cr>
```

Handler ` RVA 0x1610BE60 `；selector ` 1 `；EOL ` RVA 0x35ED68E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e1013702eb9c9580](../../evidence/conditions-sets-087.md#c-e1013702eb9c9580) · [缺口 G-696d0ffad6951acc](../../evidence/gaps-sets-004.md#g-696d0ffad6951acc) · [参数 P-586f1128f4d7527e](../../evidence/parameters-sets-007.md#p-586f1128f4d7527e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017822

```text
(exec)# show macsec status interface <interface> <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 1 `；EOL ` RVA 0x35ED6B88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80c4e13de204ba18](../../evidence/conditions-sets-050.md#c-80c4e13de204ba18) · [缺口 G-696d0ffad6951acc](../../evidence/gaps-sets-004.md#g-696d0ffad6951acc) · [参数 P-586f1128f4d7527e](../../evidence/parameters-sets-007.md#p-586f1128f4d7527e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001453

```text
(exec)# show macsec summary <cr>
```

Handler ` RVA 0x16104EA0 `；selector ` 3 `；EOL ` RVA 0x35ED5768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8053662e73b63e6d](../../evidence/conditions-sets-050.md#c-8053662e73b63e6d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004053

```text
(exec)# show management event <cr>
```

Handler ` RVA 0x11304A30 `；selector ` 0 `；EOL ` RVA 0x35492578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004043

```text
(exec)# show management expression <cr>
```

Handler ` RVA 0x11324900 `；selector ` 0 `；EOL ` RVA 0x354922D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002539

```text
(exec)# show mdns-sd location-filter <cr>
```

Handler ` RVA 0x1434AC40 `；selector ` 0 `；EOL ` RVA 0x35D324B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-274e22132a082f07](../../evidence/conditions-sets-015.md#c-274e22132a082f07) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002591

```text
(exec)# show mdns-sd remote-cache <cr>
```

Handler ` RVA 0x142A9940 `；selector ` 0 `；EOL ` RVA 0x35D0C0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8528b8314f4e9749](../../evidence/conditions-sets-052.md#c-8528b8314f4e9749) · [状态效果 S-3e3dddc8f98dde58](../../evidence/state_effects-sets-014.md#s-3e3dddc8f98dde58)

### path-009563

```text
(exec)# show mdns-sd sdg service-peer summary <cr>
```

Handler ` RVA 0x1434BF30 `；selector ` 0 `；EOL ` RVA 0x35D318A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea6ca5d33381bdf4](../../evidence/conditions-sets-091.md#c-ea6ca5d33381bdf4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002491

```text
(exec)# show mdns-sd service-definition <cr>
```

Handler ` RVA 0x1434A990 `；selector ` 0 `；EOL ` RVA 0x35D31488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea6ca5d33381bdf4](../../evidence/conditions-sets-091.md#c-ea6ca5d33381bdf4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002493

```text
(exec)# show mdns-sd service-list <cr>
```

Handler ` RVA 0x1434A6E0 `；selector ` 0 `；EOL ` RVA 0x35D30FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea6ca5d33381bdf4](../../evidence/conditions-sets-091.md#c-ea6ca5d33381bdf4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002554

```text
(exec)# show mdns-sd service-policy <cr>
```

Handler ` RVA 0x1434B0D0 `；selector ` 0 `；EOL ` RVA 0x35D31C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea6ca5d33381bdf4](../../evidence/conditions-sets-091.md#c-ea6ca5d33381bdf4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009641

```text
(exec)# show mdns-sd service-policy association vlan <cr>
```

Handler ` RVA 0x14345BD0 `；selector ` 0 `；EOL ` RVA 0x35D32088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea6ca5d33381bdf4](../../evidence/conditions-sets-091.md#c-ea6ca5d33381bdf4) · [状态效果 S-e685f3f40627a3b6](../../evidence/state_effects-sets-049.md#s-e685f3f40627a3b6)

### path-002553

```text
(exec)# show mdns-sd summary <cr>
```

Handler ` RVA 0x1434C470 `；selector ` 0 `；EOL ` RVA 0x35D32870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6946bf741da77789](../../evidence/conditions-sets-041.md#c-6946bf741da77789) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003974

```text
(exec)# show media access-lists <cr>
```

Handler ` RVA 0xF290D50 `；selector ` 0 `；EOL ` RVA 0x345E7860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016372

```text
(exec)# show media access-lists <number:1..100> <cr>
```

Handler ` RVA 0xF290D50 `；selector ` 0 `；EOL ` RVA 0x345E7860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-27d9c632b3d9c124](../../evidence/gaps-sets-002.md#g-27d9c632b3d9c124) · [参数 P-aa0d6b1fb8603c26](../../evidence/parameters-sets-013.md#p-aa0d6b1fb8603c26) · [状态效果 S-13f7d5d1c2156180](../../evidence/state_effects-sets-005.md#s-13f7d5d1c2156180)

### path-000495

```text
(exec)# show memory <cr>
```

Handler ` RVA 0xE08F580 `；selector ` 0 `；EOL ` RVA 0x341E8370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b82f596e24baafe0](../../evidence/conditions-sets-071.md#c-b82f596e24baafe0) · [状态效果 S-488ea10e8cbea090](../../evidence/state_effects-sets-016.md#s-488ea10e8cbea090)

### path-007791

```text
(exec)# show memory console reserved <cr>
```

Handler ` RVA 0xE043790 `；selector ` 0 `；EOL ` RVA 0x341E7F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df6800a55fec3da9](../../evidence/conditions-sets-086.md#c-df6800a55fec3da9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010336

```text
(exec)# show memory debug incremental allocations <cr>
```

Handler ` RVA 0xE08DDF0 `；selector ` 0 `；EOL ` RVA 0x341E6E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010337

```text
(exec)# show memory debug incremental leaks <cr>
```

Handler ` RVA 0xE08DED0 `；selector ` 0 `；EOL ` RVA 0x341E6BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010331

```text
(exec)# show memory debug incremental status <cr>
```

Handler ` RVA 0xE08DAE0 `；selector ` 0 `；EOL ` RVA 0x341E68C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007822

```text
(exec)# show memory debug leaks <cr>
```

Handler ` RVA 0xE08D530 `；selector ` 0 `；EOL ` RVA 0x341E64B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025421

```text
(exec)# show memory debug references <?general_pointer_number_action@55558973b430> <?general_pointer_number_action@55558973b700> <cr>
```

Handler ` RVA 0xE08EE90 `；selector ` 0 `；EOL ` RVA 0x341E7788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-8814d502d53d5620](../../evidence/gaps-sets-005.md#g-8814d502d53d5620) · [状态效果 S-20f8b7b8ae386a45](../../evidence/state_effects-sets-007.md#s-20f8b7b8ae386a45)

### path-010334

```text
(exec)# show memory debug references dangling <cr>
```

Handler ` RVA 0xE08E430 `；selector ` 0 `；EOL ` RVA 0x341E7408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007807

```text
(exec)# show memory debug unused <cr>
```

Handler ` RVA 0xE08E7A0 `；selector ` 0 `；EOL ` RVA 0x341E7120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003993

```text
(exec)# show memory events <cr>
```

Handler ` RVA 0xE092F40 `；selector ` 0 `；EOL ` RVA 0x341E9620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da56f1da08b1589f](../../evidence/conditions-sets-084.md#c-da56f1da08b1589f) · [状态效果 S-375bac41795a655d](../../evidence/state_effects-sets-012.md#s-375bac41795a655d)

### path-007771

```text
(exec)# show memory failures alloc <cr>
```

Handler ` RVA 0xE041EB0 `；selector ` 0 `；EOL ` RVA 0x341E60E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007758

```text
(exec)# show memory lite-chunks statistics <cr>
```

Handler ` RVA 0xE045320 `；selector ` 0 `；EOL ` RVA 0x341E5CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-318ac51ccc2328fb](../../evidence/state_effects-sets-011.md#s-318ac51ccc2328fb)

### path-003956

```text
(exec)# show memory overflow <cr>
```

Handler ` RVA 0xE03E380 `；selector ` 0 `；EOL ` RVA 0x341E8F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-42d384f090b27b2c](../../evidence/conditions-sets-026.md#c-42d384f090b27b2c) · [状态效果 S-488ea10e8cbea090](../../evidence/state_effects-sets-016.md#s-488ea10e8cbea090)

### path-007827

```text
(exec)# show memory overflow poisoning <cr>
```

Handler ` RVA 0xE041FD0 `；selector ` 0 `；EOL ` RVA 0x341E8F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3abccbf387ee03a2](../../evidence/conditions-sets-023.md#c-3abccbf387ee03a2) · [状态效果 S-488ea10e8cbea090](../../evidence/state_effects-sets-016.md#s-488ea10e8cbea090)

### path-007842

```text
(exec)# show memory traceback <number:1..4294967294> <cr>
```

Handler ` RVA 0xE08FE60 `；selector ` 0 `；EOL ` RVA 0x341E8C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Traceback ID。

[条件 C-436a68da53795db0](../../evidence/conditions-sets-026.md#c-436a68da53795db0) · [参数 P-7097096138595854](../../evidence/parameters-sets-009.md#p-7097096138595854) · [状态效果 S-11bb50063385cb5f](../../evidence/state_effects-sets-004.md#s-11bb50063385cb5f)

### path-007826

```text
(exec)# show memory traceback exclusive <cr>
```

Handler ` RVA 0xE090130 `；selector ` 0 `；EOL ` RVA 0x341E86C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-436a68da53795db0](../../evidence/conditions-sets-026.md#c-436a68da53795db0) · [状态效果 S-11bb50063385cb5f](../../evidence/state_effects-sets-004.md#s-11bb50063385cb5f)

### path-007835

```text
(exec)# show memory traceback totals <cr>
```

Handler ` RVA 0xE08FC30 `；selector ` 0 `；EOL ` RVA 0x341E8970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-436a68da53795db0](../../evidence/conditions-sets-026.md#c-436a68da53795db0) · [状态效果 S-11bb50063385cb5f](../../evidence/state_effects-sets-004.md#s-11bb50063385cb5f)

### path-003065

```text
(exec)# show mfib background <cr>
```

Handler ` RVA 0x119469C0 `；selector ` 0 `；EOL ` RVA 0x355ABB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

