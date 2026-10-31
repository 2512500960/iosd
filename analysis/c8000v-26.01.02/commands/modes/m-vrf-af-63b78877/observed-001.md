# vrf-af · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-006187

```text
(config-vrf-af)# bgp next-hop <cr>
```

Handler ` RVA 0xDC24530 `；selector ` 0 `；EOL ` RVA 0x34015B70 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0d1a1a5390315bdc](../../evidence/conditions-sets-005.md#c-0d1a1a5390315bdc) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006172

```text
(config-vrf-af)# context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c3baabb6194ef46](../../evidence/conditions-sets-054.md#c-8c3baabb6194ef46) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006209

```text
(config-vrf-af)# default bgp next-hop <cr>
```

Handler ` RVA 0xDC24530 `；selector ` 0 `；EOL ` RVA 0x34015B70 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5dd23de95a6da53e](../../evidence/conditions-sets-037.md#c-5dd23de95a6da53e) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006182

```text
(config-vrf-af)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a382541877c4048a](../../evidence/conditions-sets-063.md#c-a382541877c4048a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006178

```text
(config-vrf-af)# default exit-address-family <cr>
```

Handler ` RVA 0xDC44910 `；selector ` 0 `；EOL ` RVA 0x34016860 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4e50b30edda8a31](../../evidence/conditions-sets-082.md#c-d4e50b30edda8a31) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006230

```text
(config-vrf-af)# default export map <string> <cr>
```

Handler ` RVA 0xF21DBB0 `；selector ` 0 `；EOL ` RVA 0x345D7E40 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF export route-map name。

[条件 C-a317cb35b958002a](../../evidence/conditions-sets-063.md#c-a317cb35b958002a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-3b9944ac5689dcd9](../../evidence/parameters-sets-005.md#p-3b9944ac5689dcd9) · [状态效果 S-79b728af95adfd29](../../evidence/state_effects-sets-026.md#s-79b728af95adfd29)

### observed_connections-006175

```text
(config-vrf-af)# default help <cr>
```

Handler ` RVA 0xE006150 `；selector ` 0 `；EOL ` RVA 0x34016B48 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006231

```text
(config-vrf-af)# default import map <string> <cr>
```

Handler ` RVA 0xF21E930 `；selector ` 0 `；EOL ` RVA 0x345D76D8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF import route-map name。

[条件 C-f68710399edf2447](../../evidence/conditions-sets-095.md#c-f68710399edf2447) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-fbb4d64ba680570f](../../evidence/parameters-sets-019.md#p-fbb4d64ba680570f) · [状态效果 S-fa865c2ee0734f1f](../../evidence/state_effects-sets-053.md#s-fa865c2ee0734f1f)

### observed_connections-006189

```text
(config-vrf-af)# default inter-as-hybrid <cr>
```

Handler ` RVA 0xDC28920 `；selector ` 0 `；EOL ` RVA 0x340155E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-598c06253088e24e](../../evidence/conditions-sets-035.md#c-598c06253088e24e) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006206

```text
(config-vrf-af)# default maximum routes <cr>
```

Handler ` RVA 0xDC21C20 `；selector ` 0 `；EOL ` RVA 0x340150A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a223b8220a7f686d](../../evidence/conditions-sets-063.md#c-a223b8220a7f686d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006258

```text
(config-vrf-af)# default mdt auto-discovery pim <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 11 `；EOL ` RVA 0x34786F80 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9b0515bf1d24d72](../../evidence/conditions-sets-090.md#c-e9b0515bf1d24d72) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2a60f37074106e69](../../evidence/state_effects-sets-009.md#s-2a60f37074106e69)

### observed_connections-006253

```text
(config-vrf-af)# default mdt auto-discovery receiver-site <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 18 `；EOL ` RVA 0x34786B70 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8486ad4f4a8b734d](../../evidence/conditions-sets-051.md#c-8486ad4f4a8b734d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-9e6c73b861cd9441](../../evidence/state_effects-sets-034.md#s-9e6c73b861cd9441)

### observed_connections-006274

```text
(config-vrf-af)# default mdt data <address> <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 8 `；EOL ` RVA 0x34785128 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP multicast group address；` address ` Wildcard bits。

[条件 C-d3bbdada95ccee11](../../evidence/conditions-sets-082.md#c-d3bbdada95ccee11) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-2f72ff0fb7155fbf](../../evidence/parameters-sets-004.md#p-2f72ff0fb7155fbf) · [状态效果 S-a277582a8eee7aec](../../evidence/state_effects-sets-034.md#s-a277582a8eee7aec)

### observed_connections-006223

```text
(config-vrf-af)# default mdt data <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 2 `；EOL ` RVA 0x34784D28 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b24dd40db6d9a4e9](../../evidence/conditions-sets-069.md#c-b24dd40db6d9a4e9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-a277582a8eee7aec](../../evidence/state_effects-sets-034.md#s-a277582a8eee7aec)

### observed_connections-006273

```text
(config-vrf-af)# default mdt data threshold <number:1..4294967> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 7 `；EOL ` RVA 0x34785958 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Traffic rate in kilobits per second。

[条件 C-ebdd3b82cd135c2c](../../evidence/conditions-sets-091.md#c-ebdd3b82cd135c2c) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-8d1d11e55738adff](../../evidence/parameters-sets-011.md#p-8d1d11e55738adff) · [状态效果 S-a277582a8eee7aec](../../evidence/state_effects-sets-034.md#s-a277582a8eee7aec)

### observed_connections-006237

```text
(config-vrf-af)# default mdt default <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 0 `；EOL ` RVA 0x347828A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP multicast group address。

[条件 C-391517c39544dbfa](../../evidence/conditions-sets-022.md#c-391517c39544dbfa) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-7fe7d102d8771798](../../evidence/parameters-sets-010.md#p-7fe7d102d8771798) · [状态效果 S-baa1e6ff226a74eb](../../evidence/state_effects-sets-039.md#s-baa1e6ff226a74eb)

### observed_connections-006244

```text
(config-vrf-af)# default mdt default bier <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 20 `；EOL ` RVA 0x34782C08 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b37eacde2f2242d4](../../evidence/conditions-sets-069.md#c-b37eacde2f2242d4) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-6cbe63a076615f86](../../evidence/state_effects-sets-023.md#s-6cbe63a076615f86)

### observed_connections-006246

```text
(config-vrf-af)# default mdt default ingress-replication <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 19 `；EOL ` RVA 0x34783580 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4080c3014204bc3b](../../evidence/conditions-sets-025.md#c-4080c3014204bc3b) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-a0a6595186fce953](../../evidence/state_effects-sets-034.md#s-a0a6595186fce953)

### observed_connections-006282

```text
(config-vrf-af)# default mdt default mpls mldp <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 5 `；EOL ` RVA 0x347832B0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MP2MP LSP root address。

[条件 C-5ec372947645b7b2](../../evidence/conditions-sets-037.md#c-5ec372947645b7b2) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-5d0de5a1d27c5b8a](../../evidence/parameters-sets-007.md#p-5d0de5a1d27c5b8a) · [状态效果 S-70b0e110051cd81b](../../evidence/state_effects-sets-024.md#s-70b0e110051cd81b)

### observed_connections-006280

```text
(config-vrf-af)# default mdt default mpls mldp p2mp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 16 `；EOL ` RVA 0x34782FB8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eb842fbc7024f8b](../../evidence/conditions-sets-018.md#c-2eb842fbc7024f8b) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-ab0a5cb7d9f595ca](../../evidence/state_effects-sets-036.md#s-ab0a5cb7d9f595ca)

### observed_connections-006204

```text
(config-vrf-af)# default mdt direct <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 6 `；EOL ` RVA 0x347821E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d36ca62d72aff0f6](../../evidence/conditions-sets-082.md#c-d36ca62d72aff0f6) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-baa1e6ff226a74eb](../../evidence/state_effects-sets-039.md#s-baa1e6ff226a74eb)

### observed_connections-006218

```text
(config-vrf-af)# default mdt log-reuse <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 4 `；EOL ` RVA 0x347846F8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94bc8411fccb6144](../../evidence/conditions-sets-058.md#c-94bc8411fccb6144) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7c02ed331424dec0](../../evidence/state_effects-sets-026.md#s-7c02ed331424dec0)

### observed_connections-006243

```text
(config-vrf-af)# default mdt mode gre <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 1 `；EOL ` RVA 0x34784408 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94bc8411fccb6144](../../evidence/conditions-sets-058.md#c-94bc8411fccb6144) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-96f3528215381447](../../evidence/state_effects-sets-032.md#s-96f3528215381447)

### observed_connections-006205

```text
(config-vrf-af)# default mdt mtu <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 3 `；EOL ` RVA 0x34781F60 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a2672a7bdb25d24e](../../evidence/conditions-sets-063.md#c-a2672a7bdb25d24e) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-baa1e6ff226a74eb](../../evidence/state_effects-sets-039.md#s-baa1e6ff226a74eb)

### observed_connections-006268

```text
(config-vrf-af)# default mdt overlay bgp shared-tree-prune-delay <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 14 `；EOL ` RVA 0x34786508 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d329f3e5606d01e9](../../evidence/conditions-sets-081.md#c-d329f3e5606d01e9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-baa1e6ff226a74eb](../../evidence/state_effects-sets-039.md#s-baa1e6ff226a74eb)

### observed_connections-006271

```text
(config-vrf-af)# default mdt overlay bgp source-tree-prune-delay <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 15 `；EOL ` RVA 0x347867F8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41f690b0c12910ee](../../evidence/conditions-sets-026.md#c-41f690b0c12910ee) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-baa1e6ff226a74eb](../../evidence/state_effects-sets-039.md#s-baa1e6ff226a74eb)

### observed_connections-006250

```text
(config-vrf-af)# default mdt overlay use-bgp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 10 `；EOL ` RVA 0x34786198 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e5fb66eab550fc1d](../../evidence/conditions-sets-089.md#c-e5fb66eab550fc1d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-c98cee304dbed4b7](../../evidence/state_effects-sets-043.md#s-c98cee304dbed4b7)

### observed_connections-006245

```text
(config-vrf-af)# default mdt partitioned ingress-replication <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 17 `；EOL ` RVA 0x347840A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fadf526575b92e64](../../evidence/conditions-sets-097.md#c-fadf526575b92e64) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-5593c388b3f7f6f8](../../evidence/state_effects-sets-019.md#s-5593c388b3f7f6f8)

### observed_connections-006264

```text
(config-vrf-af)# default mdt partitioned mldp p2mp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 12 `；EOL ` RVA 0x34783D30 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d9ead463e2d65343](../../evidence/conditions-sets-084.md#c-d9ead463e2d65343) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-b423902e3058e46a](../../evidence/state_effects-sets-038.md#s-b423902e3058e46a)

### observed_connections-006248

```text
(config-vrf-af)# default mdt preference pim <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 9 `；EOL ` RVA 0x34785D38 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fbbe6d6fe8b236ae](../../evidence/conditions-sets-097.md#c-fbbe6d6fe8b236ae) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-ac701853d4a505f6](../../evidence/state_effects-sets-036.md#s-ac701853d4a505f6)

### observed_connections-006235

```text
(config-vrf-af)# default mdt strict-rpf interface <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 13 `；EOL ` RVA 0x34782538 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bb4a3d2d1a55614f](../../evidence/conditions-sets-072.md#c-bb4a3d2d1a55614f) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-cf79fdfc5f94e07e](../../evidence/state_effects-sets-044.md#s-cf79fdfc5f94e07e)

### observed_connections-006215

```text
(config-vrf-af)# default protection local-prefixes <cr>
```

Handler ` RVA 0xDC24DE0 `；selector ` 0 `；EOL ` RVA 0x34016278 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9acc4671e5787896](../../evidence/conditions-sets-060.md#c-9acc4671e5787896) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006260

```text
(config-vrf-af)# default route-replicate from unicast all <cr>
```

Handler ` RVA 0xDBECBC0 `；selector ` 0 `；EOL ` RVA 0x340087D0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8fdd3e35ae92a968](../../evidence/conditions-sets-056.md#c-8fdd3e35ae92a968) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-bee0c93c50de838d](../../evidence/state_effects-sets-040.md#s-bee0c93c50de838d)

### observed_connections-006226

```text
(config-vrf-af)# default route-replicate recursion-policy destination <cr>
```

Handler ` RVA 0xDBF1CA0 `；selector ` 0 `；EOL ` RVA 0x34008D28 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa26a9d12a8d88ac](../../evidence/conditions-sets-097.md#c-fa26a9d12a8d88ac) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-04ae8fe0b0f34400](../../evidence/state_effects-sets-001.md#s-04ae8fe0b0f34400)

### observed_connections-006233

```text
(config-vrf-af)# default route-replicate-distance from unicast <cr>
```

Handler ` RVA 0xDBED720 `；selector ` 0 `；EOL ` RVA 0x34009360 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-00cae5ac6f3dba35](../../evidence/conditions-sets-001.md#c-00cae5ac6f3dba35) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-0c2b9ca5845c621e](../../evidence/state_effects-sets-003.md#s-0c2b9ca5845c621e)

### observed_connections-006203

```text
(config-vrf-af)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c013b0ea53bdd8d9](../../evidence/conditions-sets-074.md#c-c013b0ea53bdd8d9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006278

```text
(config-vrf-af)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-4402b29d9af257d6](../../evidence/conditions-sets-027.md#c-4402b29d9af257d6) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-10b81e1af461f93b](../../evidence/state_effects-sets-004.md#s-10b81e1af461f93b)

### observed_connections-006277

```text
(config-vrf-af)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-6b50f45ddb6192d0](../../evidence/conditions-sets-042.md#c-6b50f45ddb6192d0) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-d8ee114567302237](../../evidence/state_effects-sets-046.md#s-d8ee114567302237)

### observed_connections-006194

```text
(config-vrf-af)# default topology base <cr>
```

Handler ` RVA 0xDB65440 `；selector ` 0 `；EOL ` RVA 0x33FDE970 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3e91878f3e6d1c0](../../evidence/conditions-sets-076.md#c-c3e91878f3e6d1c0) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-f14892070668bd1c](../../evidence/state_effects-sets-051.md#s-f14892070668bd1c)

### observed_connections-006179

```text
(config-vrf-af)# default topology-accounting <cr>
```

Handler ` RVA 0xDB69860 `；selector ` 0 `；EOL ` RVA 0x33FDE5E0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-457dd526ba06298a](../../evidence/conditions-sets-027.md#c-457dd526ba06298a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-7350e5473674f2fc](../../evidence/state_effects-sets-025.md#s-7350e5473674f2fc)

### observed_connections-006284

```text
(config-vrf-af)# evpn-mcast <?ipv4orv6_addr_action@555589cd5678> <cr>
```

Handler ` RVA 0xF974430 `；selector ` 0 `；EOL ` RVA 0x34781948 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-645d2c716c464e81](../../evidence/conditions-sets-039.md#c-645d2c716c464e81) · [缺口 G-4a4d42286aca515e](../../evidence/gaps-sets-003.md#g-4a4d42286aca515e) · [状态效果 S-fca0254aa3a57907](../../evidence/state_effects-sets-054.md#s-fca0254aa3a57907)

### observed_connections-006170

```text
(config-vrf-af)# exit-address-family <cr>
```

Handler ` RVA 0xDC44910 `；selector ` 0 `；EOL ` RVA 0x34016860 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d4e50b30edda8a31](../../evidence/conditions-sets-082.md#c-d4e50b30edda8a31) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006198

```text
(config-vrf-af)# export map <string> <cr>
```

Handler ` RVA 0xF21DBB0 `；selector ` 0 `；EOL ` RVA 0x345D7E40 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF export route-map name。

[条件 C-a317cb35b958002a](../../evidence/conditions-sets-063.md#c-a317cb35b958002a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-3b9944ac5689dcd9](../../evidence/parameters-sets-005.md#p-3b9944ac5689dcd9) · [状态效果 S-d7fc02053093f315](../../evidence/state_effects-sets-046.md#s-d7fc02053093f315)

### observed_connections-006169

```text
(config-vrf-af)# help <cr>
```

Handler ` RVA 0xE006150 `；selector ` 0 `；EOL ` RVA 0x34016B48 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006199

```text
(config-vrf-af)# import map <string> <cr>
```

Handler ` RVA 0xF21E930 `；selector ` 0 `；EOL ` RVA 0x345D76D8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF import route-map name。

[条件 C-f68710399edf2447](../../evidence/conditions-sets-095.md#c-f68710399edf2447) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-fbb4d64ba680570f](../../evidence/parameters-sets-019.md#p-fbb4d64ba680570f) · [状态效果 S-7a74682d6ffab823](../../evidence/state_effects-sets-026.md#s-7a74682d6ffab823)

### observed_connections-006173

```text
(config-vrf-af)# inter-as-hybrid <cr>
```

Handler ` RVA 0xDC28920 `；selector ` 0 `；EOL ` RVA 0x340155E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-598c06253088e24e](../../evidence/conditions-sets-035.md#c-598c06253088e24e) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006186

```text
(config-vrf-af)# maximum routes <cr>
```

Handler ` RVA 0xDC21C20 `；selector ` 0 `；EOL ` RVA 0x340150A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9b52772c3da300c2](../../evidence/conditions-sets-060.md#c-9b52772c3da300c2) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006224

```text
(config-vrf-af)# mdt auto-discovery pim <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 11 `；EOL ` RVA 0x34786F80 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e9b0515bf1d24d72](../../evidence/conditions-sets-090.md#c-e9b0515bf1d24d72) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-d3f2086f3a85a839](../../evidence/state_effects-sets-045.md#s-d3f2086f3a85a839)

### observed_connections-006221

```text
(config-vrf-af)# mdt auto-discovery receiver-site <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 18 `；EOL ` RVA 0x34786B70 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8486ad4f4a8b734d](../../evidence/conditions-sets-051.md#c-8486ad4f4a8b734d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-fe72923e80413aa6](../../evidence/state_effects-sets-054.md#s-fe72923e80413aa6)

### observed_connections-006256

```text
(config-vrf-af)# mdt data <address> <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 8 `；EOL ` RVA 0x34785128 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP multicast group address；` address ` Wildcard bits。

[条件 C-d3bbdada95ccee11](../../evidence/conditions-sets-082.md#c-d3bbdada95ccee11) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-2f72ff0fb7155fbf](../../evidence/parameters-sets-004.md#p-2f72ff0fb7155fbf) · [状态效果 S-31796889efa758ed](../../evidence/state_effects-sets-011.md#s-31796889efa758ed)

### observed_connections-006192

```text
(config-vrf-af)# mdt data <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 2 `；EOL ` RVA 0x34784D28 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b24dd40db6d9a4e9](../../evidence/conditions-sets-069.md#c-b24dd40db6d9a4e9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-31796889efa758ed](../../evidence/state_effects-sets-011.md#s-31796889efa758ed)

### observed_connections-006255

```text
(config-vrf-af)# mdt data threshold <number:1..4294967> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 7 `；EOL ` RVA 0x34785958 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Traffic rate in kilobits per second。

[条件 C-ebdd3b82cd135c2c](../../evidence/conditions-sets-091.md#c-ebdd3b82cd135c2c) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-8d1d11e55738adff](../../evidence/parameters-sets-011.md#p-8d1d11e55738adff) · [状态效果 S-31796889efa758ed](../../evidence/state_effects-sets-011.md#s-31796889efa758ed)

### observed_connections-006210

```text
(config-vrf-af)# mdt default <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 0 `；EOL ` RVA 0x347828A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP multicast group address。

[条件 C-391517c39544dbfa](../../evidence/conditions-sets-022.md#c-391517c39544dbfa) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-7fe7d102d8771798](../../evidence/parameters-sets-010.md#p-7fe7d102d8771798) · [状态效果 S-0b73e06834d9c0f6](../../evidence/state_effects-sets-003.md#s-0b73e06834d9c0f6)

### observed_connections-006213

```text
(config-vrf-af)# mdt default bier <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 20 `；EOL ` RVA 0x34782C08 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d9f09c74bbce67d](../../evidence/conditions-sets-030.md#c-4d9f09c74bbce67d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-bbf4981ac5fa0159](../../evidence/state_effects-sets-040.md#s-bbf4981ac5fa0159)

### observed_connections-006217

```text
(config-vrf-af)# mdt default ingress-replication <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 19 `；EOL ` RVA 0x34783580 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4080c3014204bc3b](../../evidence/conditions-sets-025.md#c-4080c3014204bc3b) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-5a9a020bb993cd6f](../../evidence/state_effects-sets-020.md#s-5a9a020bb993cd6f)

### observed_connections-006266

```text
(config-vrf-af)# mdt default mpls mldp <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 5 `；EOL ` RVA 0x347832B0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MP2MP LSP root address。

[条件 C-5ec372947645b7b2](../../evidence/conditions-sets-037.md#c-5ec372947645b7b2) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-5d0de5a1d27c5b8a](../../evidence/parameters-sets-007.md#p-5d0de5a1d27c5b8a) · [状态效果 S-d5da92f86eead10e](../../evidence/state_effects-sets-045.md#s-d5da92f86eead10e)

### observed_connections-006265

```text
(config-vrf-af)# mdt default mpls mldp p2mp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 16 `；EOL ` RVA 0x34782FB8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2eb842fbc7024f8b](../../evidence/conditions-sets-018.md#c-2eb842fbc7024f8b) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-5130f12c81d45a00](../../evidence/state_effects-sets-018.md#s-5130f12c81d45a00)

### observed_connections-006286

```text
(config-vrf-af)# mdt default vxlan <?ipv4orv6_addr_action@555589cd7878> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 21 `；EOL ` RVA 0x34783938 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bea87115b3ee760a](../../evidence/conditions-sets-074.md#c-bea87115b3ee760a) · [缺口 G-8a713e277c3a8a5a](../../evidence/gaps-sets-005.md#g-8a713e277c3a8a5a) · [状态效果 S-93a19791392372b6](../../evidence/state_effects-sets-031.md#s-93a19791392372b6)

### observed_connections-006184

```text
(config-vrf-af)# mdt direct <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 6 `；EOL ` RVA 0x347821E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d36ca62d72aff0f6](../../evidence/conditions-sets-082.md#c-d36ca62d72aff0f6) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-0b73e06834d9c0f6](../../evidence/state_effects-sets-003.md#s-0b73e06834d9c0f6)

### observed_connections-006191

```text
(config-vrf-af)# mdt log-reuse <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 4 `；EOL ` RVA 0x347846F8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94bc8411fccb6144](../../evidence/conditions-sets-058.md#c-94bc8411fccb6144) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-6ad4d584ea67498d](../../evidence/state_effects-sets-023.md#s-6ad4d584ea67498d)

### observed_connections-006212

```text
(config-vrf-af)# mdt mode gre <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 1 `；EOL ` RVA 0x34784408 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94bc8411fccb6144](../../evidence/conditions-sets-058.md#c-94bc8411fccb6144) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-06bf0a99013cfffb](../../evidence/state_effects-sets-002.md#s-06bf0a99013cfffb)

### observed_connections-006185

```text
(config-vrf-af)# mdt mtu <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 3 `；EOL ` RVA 0x34781F60 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f419b65363eb9a7](../../evidence/conditions-sets-025.md#c-3f419b65363eb9a7) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-0b73e06834d9c0f6](../../evidence/state_effects-sets-003.md#s-0b73e06834d9c0f6)

### observed_connections-006252

```text
(config-vrf-af)# mdt overlay bgp shared-tree-prune-delay <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 14 `；EOL ` RVA 0x34786508 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4e55cccee264a4c2](../../evidence/conditions-sets-031.md#c-4e55cccee264a4c2) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-0b73e06834d9c0f6](../../evidence/state_effects-sets-003.md#s-0b73e06834d9c0f6)

### observed_connections-006254

```text
(config-vrf-af)# mdt overlay bgp source-tree-prune-delay <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 15 `；EOL ` RVA 0x347867F8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-40297f3055d382fc](../../evidence/conditions-sets-025.md#c-40297f3055d382fc) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-0b73e06834d9c0f6](../../evidence/state_effects-sets-003.md#s-0b73e06834d9c0f6)

### observed_connections-006220

```text
(config-vrf-af)# mdt overlay use-bgp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 10 `；EOL ` RVA 0x34786198 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5fb66eab550fc1d](../../evidence/conditions-sets-089.md#c-e5fb66eab550fc1d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-ab26a17617743254](../../evidence/state_effects-sets-036.md#s-ab26a17617743254)

### observed_connections-006216

```text
(config-vrf-af)# mdt partitioned ingress-replication <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 17 `；EOL ` RVA 0x347840A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fadf526575b92e64](../../evidence/conditions-sets-097.md#c-fadf526575b92e64) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-5029b2091107d918](../../evidence/state_effects-sets-018.md#s-5029b2091107d918)

### observed_connections-006240

```text
(config-vrf-af)# mdt partitioned mldp p2mp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 12 `；EOL ` RVA 0x34783D30 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9ead463e2d65343](../../evidence/conditions-sets-084.md#c-d9ead463e2d65343) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-b33f3ed976e3b897](../../evidence/state_effects-sets-038.md#s-b33f3ed976e3b897)

### observed_connections-006219

```text
(config-vrf-af)# mdt preference pim <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 9 `；EOL ` RVA 0x34785D38 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fbbe6d6fe8b236ae](../../evidence/conditions-sets-097.md#c-fbbe6d6fe8b236ae) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-bee5348fa0304322](../../evidence/state_effects-sets-040.md#s-bee5348fa0304322)

### observed_connections-006208

```text
(config-vrf-af)# mdt strict-rpf interface <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 13 `；EOL ` RVA 0x34782538 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb4a3d2d1a55614f](../../evidence/conditions-sets-072.md#c-bb4a3d2d1a55614f) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-d4bdae7f0640d42c](../../evidence/state_effects-sets-045.md#s-d4bdae7f0640d42c)

### observed_connections-006207

```text
(config-vrf-af)# no bgp next-hop <cr>
```

Handler ` RVA 0xDC24530 `；selector ` 0 `；EOL ` RVA 0x34015B70 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-1376605240a282e4](../../evidence/conditions-sets-008.md#c-1376605240a282e4) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006180

```text
(config-vrf-af)# no context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-287ab06914710a47](../../evidence/conditions-sets-016.md#c-287ab06914710a47) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006176

```text
(config-vrf-af)# no exit-address-family <cr>
```

Handler ` RVA 0xDC44910 `；selector ` 0 `；EOL ` RVA 0x34016860 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d4e50b30edda8a31](../../evidence/conditions-sets-082.md#c-d4e50b30edda8a31) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006227

```text
(config-vrf-af)# no export map <string> <cr>
```

Handler ` RVA 0xF21DBB0 `；selector ` 0 `；EOL ` RVA 0x345D7E40 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` VRF export route-map name。

[条件 C-a317cb35b958002a](../../evidence/conditions-sets-063.md#c-a317cb35b958002a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-3b9944ac5689dcd9](../../evidence/parameters-sets-005.md#p-3b9944ac5689dcd9) · [状态效果 S-bcaa419e6cac2a41](../../evidence/state_effects-sets-040.md#s-bcaa419e6cac2a41)

### observed_connections-006174

```text
(config-vrf-af)# no help <cr>
```

Handler ` RVA 0xE006150 `；selector ` 0 `；EOL ` RVA 0x34016B48 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006228

```text
(config-vrf-af)# no import map <string> <cr>
```

Handler ` RVA 0xF21E930 `；selector ` 0 `；EOL ` RVA 0x345D76D8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` VRF import route-map name。

[条件 C-f68710399edf2447](../../evidence/conditions-sets-095.md#c-f68710399edf2447) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-fbb4d64ba680570f](../../evidence/parameters-sets-019.md#p-fbb4d64ba680570f) · [状态效果 S-9e74b3e88900d929](../../evidence/state_effects-sets-034.md#s-9e74b3e88900d929)

### observed_connections-006188

```text
(config-vrf-af)# no inter-as-hybrid <cr>
```

Handler ` RVA 0xDC28920 `；selector ` 0 `；EOL ` RVA 0x340155E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-598c06253088e24e](../../evidence/conditions-sets-035.md#c-598c06253088e24e) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006201

```text
(config-vrf-af)# no maximum routes <cr>
```

Handler ` RVA 0xDC21C20 `；selector ` 0 `；EOL ` RVA 0x340150A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-50d62908dfefe9f6](../../evidence/conditions-sets-032.md#c-50d62908dfefe9f6) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006257

```text
(config-vrf-af)# no mdt auto-discovery pim <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 11 `；EOL ` RVA 0x34786F80 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-e9b0515bf1d24d72](../../evidence/conditions-sets-090.md#c-e9b0515bf1d24d72) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2ddfd323c33f2185](../../evidence/state_effects-sets-010.md#s-2ddfd323c33f2185)

### observed_connections-006251

```text
(config-vrf-af)# no mdt auto-discovery receiver-site <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 18 `；EOL ` RVA 0x34786B70 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-8486ad4f4a8b734d](../../evidence/conditions-sets-051.md#c-8486ad4f4a8b734d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-a3031614cbd3e723](../../evidence/state_effects-sets-035.md#s-a3031614cbd3e723)

### observed_connections-006272

```text
(config-vrf-af)# no mdt data <address> <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 8 `；EOL ` RVA 0x34785128 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` IP multicast group address；` address ` Wildcard bits。

[条件 C-d3bbdada95ccee11](../../evidence/conditions-sets-082.md#c-d3bbdada95ccee11) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-2f72ff0fb7155fbf](../../evidence/parameters-sets-004.md#p-2f72ff0fb7155fbf) · [状态效果 S-99d90f7966aeb422](../../evidence/state_effects-sets-033.md#s-99d90f7966aeb422)

### observed_connections-006222

```text
(config-vrf-af)# no mdt data <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 2 `；EOL ` RVA 0x34784D28 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b24dd40db6d9a4e9](../../evidence/conditions-sets-069.md#c-b24dd40db6d9a4e9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-99d90f7966aeb422](../../evidence/state_effects-sets-033.md#s-99d90f7966aeb422)

### observed_connections-006270

```text
(config-vrf-af)# no mdt data threshold <number:1..4294967> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 7 `；EOL ` RVA 0x34785958 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` unsigned_number ` Traffic rate in kilobits per second。

[条件 C-ebdd3b82cd135c2c](../../evidence/conditions-sets-091.md#c-ebdd3b82cd135c2c) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-8d1d11e55738adff](../../evidence/parameters-sets-011.md#p-8d1d11e55738adff) · [状态效果 S-99d90f7966aeb422](../../evidence/state_effects-sets-033.md#s-99d90f7966aeb422)

### observed_connections-006236

```text
(config-vrf-af)# no mdt default <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 0 `；EOL ` RVA 0x347828A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` IP multicast group address。

[条件 C-391517c39544dbfa](../../evidence/conditions-sets-022.md#c-391517c39544dbfa) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-7fe7d102d8771798](../../evidence/parameters-sets-010.md#p-7fe7d102d8771798) · [状态效果 S-2906f4f93ffbc1a9](../../evidence/state_effects-sets-009.md#s-2906f4f93ffbc1a9)

### observed_connections-006239

```text
(config-vrf-af)# no mdt default bier <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 20 `；EOL ` RVA 0x34782C08 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b19b15d483f62fe4](../../evidence/conditions-sets-069.md#c-b19b15d483f62fe4) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-4df8d70bb8464af6](../../evidence/state_effects-sets-017.md#s-4df8d70bb8464af6)

### observed_connections-006242

```text
(config-vrf-af)# no mdt default ingress-replication <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 19 `；EOL ` RVA 0x34783580 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-4080c3014204bc3b](../../evidence/conditions-sets-025.md#c-4080c3014204bc3b) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-cc5217b31eac5a11](../../evidence/state_effects-sets-043.md#s-cc5217b31eac5a11)

### observed_connections-006281

```text
(config-vrf-af)# no mdt default mpls mldp <address> <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 5 `；EOL ` RVA 0x347832B0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` address ` MP2MP LSP root address。

[条件 C-5ec372947645b7b2](../../evidence/conditions-sets-037.md#c-5ec372947645b7b2) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-5d0de5a1d27c5b8a](../../evidence/parameters-sets-007.md#p-5d0de5a1d27c5b8a) · [状态效果 S-62bcf968cf3e25b4](../../evidence/state_effects-sets-021.md#s-62bcf968cf3e25b4)

### observed_connections-006279

```text
(config-vrf-af)# no mdt default mpls mldp p2mp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 16 `；EOL ` RVA 0x34782FB8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-2eb842fbc7024f8b](../../evidence/conditions-sets-018.md#c-2eb842fbc7024f8b) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-42e0290691fbe3b6](../../evidence/state_effects-sets-015.md#s-42e0290691fbe3b6)

### observed_connections-006197

```text
(config-vrf-af)# no mdt direct <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 6 `；EOL ` RVA 0x347821E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d36ca62d72aff0f6](../../evidence/conditions-sets-082.md#c-d36ca62d72aff0f6) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2906f4f93ffbc1a9](../../evidence/state_effects-sets-009.md#s-2906f4f93ffbc1a9)

### observed_connections-006214

```text
(config-vrf-af)# no mdt log-reuse <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 4 `；EOL ` RVA 0x347846F8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-94bc8411fccb6144](../../evidence/conditions-sets-058.md#c-94bc8411fccb6144) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-67258ef77182cebc](../../evidence/state_effects-sets-022.md#s-67258ef77182cebc)

### observed_connections-006238

```text
(config-vrf-af)# no mdt mode gre <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 1 `；EOL ` RVA 0x34784408 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-94bc8411fccb6144](../../evidence/conditions-sets-058.md#c-94bc8411fccb6144) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-678312d489388a4a](../../evidence/state_effects-sets-022.md#s-678312d489388a4a)

### observed_connections-006200

```text
(config-vrf-af)# no mdt mtu <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 3 `；EOL ` RVA 0x34781F60 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-e0f7e67fc8d425fd](../../evidence/conditions-sets-087.md#c-e0f7e67fc8d425fd) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2906f4f93ffbc1a9](../../evidence/state_effects-sets-009.md#s-2906f4f93ffbc1a9)

### observed_connections-006267

```text
(config-vrf-af)# no mdt overlay bgp shared-tree-prune-delay <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 14 `；EOL ` RVA 0x34786508 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a7db0eb1a9bba588](../../evidence/conditions-sets-065.md#c-a7db0eb1a9bba588) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2906f4f93ffbc1a9](../../evidence/state_effects-sets-009.md#s-2906f4f93ffbc1a9)

### observed_connections-006269

```text
(config-vrf-af)# no mdt overlay bgp source-tree-prune-delay <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 15 `；EOL ` RVA 0x347867F8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-a9c9a5f5cebb5354](../../evidence/conditions-sets-066.md#c-a9c9a5f5cebb5354) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2906f4f93ffbc1a9](../../evidence/state_effects-sets-009.md#s-2906f4f93ffbc1a9)

### observed_connections-006249

```text
(config-vrf-af)# no mdt overlay use-bgp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 10 `；EOL ` RVA 0x34786198 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-e5fb66eab550fc1d](../../evidence/conditions-sets-089.md#c-e5fb66eab550fc1d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-43572e8cf2724fa7](../../evidence/state_effects-sets-015.md#s-43572e8cf2724fa7)

### observed_connections-006241

```text
(config-vrf-af)# no mdt partitioned ingress-replication <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 17 `；EOL ` RVA 0x347840A8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fadf526575b92e64](../../evidence/conditions-sets-097.md#c-fadf526575b92e64) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-f9222545ef59e3c0](../../evidence/state_effects-sets-053.md#s-f9222545ef59e3c0)

### observed_connections-006263

```text
(config-vrf-af)# no mdt partitioned mldp p2mp <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 12 `；EOL ` RVA 0x34783D30 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d9ead463e2d65343](../../evidence/conditions-sets-084.md#c-d9ead463e2d65343) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-5e65e2875433981f](../../evidence/state_effects-sets-020.md#s-5e65e2875433981f)

### observed_connections-006247

```text
(config-vrf-af)# no mdt preference pim <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 9 `；EOL ` RVA 0x34785D38 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fbbe6d6fe8b236ae](../../evidence/conditions-sets-097.md#c-fbbe6d6fe8b236ae) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-2f974e79de0761fc](../../evidence/state_effects-sets-011.md#s-2f974e79de0761fc)

### observed_connections-006234

```text
(config-vrf-af)# no mdt strict-rpf interface <cr>
```

Handler ` RVA 0xF8C8970 `；selector ` 13 `；EOL ` RVA 0x34782538 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-bb4a3d2d1a55614f](../../evidence/conditions-sets-072.md#c-bb4a3d2d1a55614f) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-ce669aeb4fad035f](../../evidence/state_effects-sets-044.md#s-ce669aeb4fad035f)

### observed_connections-006211

```text
(config-vrf-af)# no protection local-prefixes <cr>
```

Handler ` RVA 0xDC24DE0 `；selector ` 0 `；EOL ` RVA 0x34016278 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-f9fe56ddcd63f459](../../evidence/conditions-sets-097.md#c-f9fe56ddcd63f459) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006259

```text
(config-vrf-af)# no route-replicate from unicast all <cr>
```

Handler ` RVA 0xDBECBC0 `；selector ` 0 `；EOL ` RVA 0x340087D0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-8fdd3e35ae92a968](../../evidence/conditions-sets-056.md#c-8fdd3e35ae92a968) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-25459b0455a3bf3b](../../evidence/state_effects-sets-008.md#s-25459b0455a3bf3b)

### observed_connections-006225

```text
(config-vrf-af)# no route-replicate recursion-policy destination <cr>
```

Handler ` RVA 0xDBF1CA0 `；selector ` 0 `；EOL ` RVA 0x34008D28 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fa26a9d12a8d88ac](../../evidence/conditions-sets-097.md#c-fa26a9d12a8d88ac) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-87dff8312413daff](../../evidence/state_effects-sets-029.md#s-87dff8312413daff)

### observed_connections-006229

```text
(config-vrf-af)# no route-replicate-distance from unicast <cr>
```

Handler ` RVA 0xDBED720 `；selector ` 0 `；EOL ` RVA 0x34009360 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c1139a7468b23af6](../../evidence/conditions-sets-075.md#c-c1139a7468b23af6) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-8dc6405f83971357](../../evidence/state_effects-sets-030.md#s-8dc6405f83971357)

### observed_connections-006196

```text
(config-vrf-af)# no snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c013b0ea53bdd8d9](../../evidence/conditions-sets-074.md#c-c013b0ea53bdd8d9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006276

```text
(config-vrf-af)# no snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-e5e1ab3f9850ee01](../../evidence/conditions-sets-089.md#c-e5e1ab3f9850ee01) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-949b481ccd6771ab](../../evidence/state_effects-sets-032.md#s-949b481ccd6771ab)

### observed_connections-006275

```text
(config-vrf-af)# no snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-e8146f6702e7ca7d](../../evidence/conditions-sets-090.md#c-e8146f6702e7ca7d) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-47d5da9a31106e8d](../../evidence/state_effects-sets-016.md#s-47d5da9a31106e8d)

### observed_connections-006193

```text
(config-vrf-af)# no topology base <cr>
```

Handler ` RVA 0xDB65440 `；selector ` 0 `；EOL ` RVA 0x33FDE970 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-c3e91878f3e6d1c0](../../evidence/conditions-sets-076.md#c-c3e91878f3e6d1c0) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-db552c3cdf9ac902](../../evidence/state_effects-sets-046.md#s-db552c3cdf9ac902)

### observed_connections-006177

```text
(config-vrf-af)# no topology-accounting <cr>
```

Handler ` RVA 0xDB69860 `；selector ` 0 `；EOL ` RVA 0x33FDE5E0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-457dd526ba06298a](../../evidence/conditions-sets-027.md#c-457dd526ba06298a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-3fd3177835599a71](../../evidence/state_effects-sets-014.md#s-3fd3177835599a71)

### observed_connections-006190

```text
(config-vrf-af)# protection local-prefixes <cr>
```

Handler ` RVA 0xDC24DE0 `；selector ` 0 `；EOL ` RVA 0x34016278 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b1f7bdce9bbe0a77](../../evidence/conditions-sets-069.md#c-b1f7bdce9bbe0a77) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006232

```text
(config-vrf-af)# route-replicate from unicast all <cr>
```

Handler ` RVA 0xDBECBC0 `；selector ` 0 `；EOL ` RVA 0x340087D0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8fdd3e35ae92a968](../../evidence/conditions-sets-056.md#c-8fdd3e35ae92a968) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-95c08ca985f5eb62](../../evidence/state_effects-sets-032.md#s-95c08ca985f5eb62)

### observed_connections-006195

```text
(config-vrf-af)# route-replicate recursion-policy destination <cr>
```

Handler ` RVA 0xDBF1CA0 `；selector ` 0 `；EOL ` RVA 0x34008D28 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fa26a9d12a8d88ac](../../evidence/conditions-sets-097.md#c-fa26a9d12a8d88ac) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-eb86692567594428](../../evidence/state_effects-sets-050.md#s-eb86692567594428)

### observed_connections-006202

```text
(config-vrf-af)# route-replicate-distance from unicast <cr>
```

Handler ` RVA 0xDBED720 `；selector ` 0 `；EOL ` RVA 0x34009360 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97f6f84ff7f8763e](../../evidence/conditions-sets-059.md#c-97f6f84ff7f8763e) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-8dfb7b3db51d081d](../../evidence/state_effects-sets-030.md#s-8dfb7b3db51d081d)

### observed_connections-006283

```text
(config-vrf-af)# route-target <?bgp_extcomm_action@555589568bc0> <cr>
```

Handler ` RVA 0xDC21FB0 `；selector ` 0 `；EOL ` RVA 0x34014C50 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4b9cd4636a14021c](../../evidence/conditions-sets-030.md#c-4b9cd4636a14021c) · [缺口 G-38595d591856e068](../../evidence/gaps-sets-002.md#g-38595d591856e068) · [状态效果 S-bdc17c4843a1ee34](../../evidence/state_effects-sets-040.md#s-bdc17c4843a1ee34)

### observed_connections-006285

```text
(config-vrf-af)# route-target <?bgp_extcomm_action@555589568bc0> stitching <cr>
```

Handler ` RVA 0xF1B7290 `；selector ` 0 `；EOL ` RVA 0x3451E0E8 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-92608744d73b5a95](../../evidence/conditions-sets-056.md#c-92608744d73b5a95) · [缺口 G-38595d591856e068](../../evidence/gaps-sets-002.md#g-38595d591856e068) · [状态效果 S-bdc17c4843a1ee34](../../evidence/state_effects-sets-040.md#s-bdc17c4843a1ee34)

### observed_connections-006183

```text
(config-vrf-af)# snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c013b0ea53bdd8d9](../../evidence/conditions-sets-074.md#c-c013b0ea53bdd8d9) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)

### observed_connections-006262

```text
(config-vrf-af)# snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-fe77d1c4cf07f3f1](../../evidence/conditions-sets-098.md#c-fe77d1c4cf07f3f1) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-b94b83aa9d2edde3](../../evidence/state_effects-sets-039.md#s-b94b83aa9d2edde3)

### observed_connections-006261

```text
(config-vrf-af)# snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-a175d0760c57bc75](../../evidence/conditions-sets-062.md#c-a175d0760c57bc75) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-abb6ead11e63404e](../../evidence/state_effects-sets-036.md#s-abb6ead11e63404e)

### observed_connections-006181

```text
(config-vrf-af)# topology base <cr>
```

Handler ` RVA 0xDB65440 `；selector ` 0 `；EOL ` RVA 0x33FDE970 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3e91878f3e6d1c0](../../evidence/conditions-sets-076.md#c-c3e91878f3e6d1c0) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-b3655064448dface](../../evidence/state_effects-sets-038.md#s-b3655064448dface)

### observed_connections-006171

```text
(config-vrf-af)# topology-accounting <cr>
```

Handler ` RVA 0xDB69860 `；selector ` 0 `；EOL ` RVA 0x33FDE5E0 `。

模式根 ` RVA 0x34011BD8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-457dd526ba06298a](../../evidence/conditions-sets-027.md#c-457dd526ba06298a) · [缺口 G-bdd271197f336de8](../../evidence/gaps-sets-007.md#g-bdd271197f336de8) · [状态效果 S-327d5a22bb0181b5](../../evidence/state_effects-sets-011.md#s-327d5a22bb0181b5)
