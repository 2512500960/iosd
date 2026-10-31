# ethernet-mac-tunnel-config · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007735

```text
(config-tunnel-minm)# bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-4e93df83155b5a25](../../evidence/conditions-sets-031.md#c-4e93df83155b5a25) · [缺口 G-b993303d8a3e9924](../../evidence/gaps-sets-007.md#g-b993303d8a3e9924) · [参数 P-735c645cccdd523e](../../evidence/parameters-sets-009.md#p-735c645cccdd523e) · [状态效果 S-59bea50fdc0db030](../../evidence/state_effects-sets-019.md#s-59bea50fdc0db030)

### observed_connections-007701

```text
(config-tunnel-minm)# bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-bcdc24a59e9ee46e](../../evidence/state_effects-sets-040.md#s-bcdc24a59e9ee46e)

### observed_connections-007706

```text
(config-tunnel-minm)# bvlan dot1ad <number:1..4094> <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 3 `；EOL ` RVA 0x3397FA20 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` B-VLAN to be used in the tunnel。

[条件 C-3d9aea83394566b9](../../evidence/conditions-sets-024.md#c-3d9aea83394566b9) · [参数 P-6b47cbfc36a1bd10](../../evidence/parameters-sets-008.md#p-6b47cbfc36a1bd10) · [状态效果 S-be46468e85d83165](../../evidence/state_effects-sets-040.md#s-be46468e85d83165)

### observed_connections-007708

```text
(config-tunnel-minm)# default bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-de1b7e209d94ad0d](../../evidence/state_effects-sets-047.md#s-de1b7e209d94ad0d)

### observed_connections-007714

```text
(config-tunnel-minm)# default bvlan dot1ad <number:1..4094> <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 3 `；EOL ` RVA 0x3397FA20 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` B-VLAN to be used in the tunnel。

[条件 C-3d9aea83394566b9](../../evidence/conditions-sets-024.md#c-3d9aea83394566b9) · [参数 P-6b47cbfc36a1bd10](../../evidence/parameters-sets-008.md#p-6b47cbfc36a1bd10) · [状态效果 S-5f6a5ae2fc75a1d9](../../evidence/state_effects-sets-020.md#s-5f6a5ae2fc75a1d9)

### observed_connections-007700

```text
(config-tunnel-minm)# default description <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 6 `；EOL ` RVA 0x33980178 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2d80db026d761b24](../../evidence/conditions-sets-018.md#c-2d80db026d761b24) · [状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007712

```text
(config-tunnel-minm)# default ethernet egress-filter <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8753624b0239f673](../../evidence/conditions-sets-052.md#c-8753624b0239f673) · [状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007697

```text
(config-tunnel-minm)# default exit <cr>
```

Handler ` RVA 0xC00EF40 `；selector ` 0 `；EOL ` RVA 0x3397F540 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007723

```text
(config-tunnel-minm)# default ip access-group in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007726

```text
(config-tunnel-minm)# default ip access-group out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007728

```text
(config-tunnel-minm)# default ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-27c0dc5a1b006952](../../evidence/state_effects-sets-009.md#s-27c0dc5a1b006952)

### observed_connections-007730

```text
(config-tunnel-minm)# default ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-63ed071d7ae4eda9](../../evidence/state_effects-sets-021.md#s-63ed071d7ae4eda9)

### observed_connections-007732

```text
(config-tunnel-minm)# default mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-fd95eaf0aa6adaeb](../../evidence/state_effects-sets-054.md#s-fd95eaf0aa6adaeb)

### observed_connections-007734

```text
(config-tunnel-minm)# default mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-8f74bae3fbd82fc8](../../evidence/state_effects-sets-030.md#s-8f74bae3fbd82fc8)

### observed_connections-007720

```text
(config-tunnel-minm)# default storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-e54c7289ec206744](../../evidence/state_effects-sets-048.md#s-e54c7289ec206744)

### observed_connections-007703

```text
(config-tunnel-minm)# default transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007705

```text
(config-tunnel-minm)# default untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-38cad10aa1231666](../../evidence/state_effects-sets-013.md#s-38cad10aa1231666)

### observed_connections-007699

```text
(config-tunnel-minm)# description <string> <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 6 `；EOL ` RVA 0x33980178 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 240 characters describing this mac tunnel。

[条件 C-468187c29b0233c4](../../evidence/conditions-sets-028.md#c-468187c29b0233c4) · [参数 P-da2c975509d9f328](../../evidence/parameters-sets-016.md#p-da2c975509d9f328)

### observed_connections-007711

```text
(config-tunnel-minm)# ethernet egress-filter disable <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1be6c7d7f6ba41c](../../evidence/conditions-sets-081.md#c-d1be6c7d7f6ba41c) · [状态效果 S-5c85aab71f02acf9](../../evidence/state_effects-sets-020.md#s-5c85aab71f02acf9)

### observed_connections-007693

```text
(config-tunnel-minm)# exit <cr>
```

Handler ` RVA 0xC00EF40 `；selector ` 0 `；EOL ` RVA 0x3397F540 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007716

```text
(config-tunnel-minm)# ip access-group <number:1..199> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-263551246ce1417a](../../evidence/conditions-sets-015.md#c-263551246ce1417a) · [参数 P-39ee2607d399f61c](../../evidence/parameters-sets-005.md#p-39ee2607d399f61c)

### observed_connections-007719

```text
(config-tunnel-minm)# ip access-group <number:1..199> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-263551246ce1417a](../../evidence/conditions-sets-015.md#c-263551246ce1417a) · [参数 P-39ee2607d399f61c](../../evidence/parameters-sets-005.md#p-39ee2607d399f61c)

### observed_connections-007740

```text
(config-tunnel-minm)# ip flow monitor <?option@555588f5efa0> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0B1C8 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2680cb17110d020b](../../evidence/conditions-sets-015.md#c-2680cb17110d020b) · [缺口 G-576c1b7539f300fa](../../evidence/gaps-sets-004.md#g-576c1b7539f300fa) · [状态效果 S-0801271744601689](../../evidence/state_effects-sets-002.md#s-0801271744601689)

### observed_connections-007737

```text
(config-tunnel-minm)# ip flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0B480 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2fecafea42d2c258](../../evidence/conditions-sets-019.md#c-2fecafea42d2c258) · [缺口 G-df678120ccaad078](../../evidence/gaps-sets-008.md#g-df678120ccaad078) · [状态效果 S-0801271744601689](../../evidence/state_effects-sets-002.md#s-0801271744601689)

### observed_connections-007741

```text
(config-tunnel-minm)# ipv6 flow monitor <?option@555588f60368> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0C590 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b266e79d8a56d625](../../evidence/conditions-sets-069.md#c-b266e79d8a56d625) · [缺口 G-43bf3f2e95a39d33](../../evidence/gaps-sets-003.md#g-43bf3f2e95a39d33) · [状态效果 S-4cdc4859765332db](../../evidence/state_effects-sets-017.md#s-4cdc4859765332db)

### observed_connections-007738

```text
(config-tunnel-minm)# ipv6 flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0C848 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-514b1dbe27318167](../../evidence/conditions-sets-032.md#c-514b1dbe27318167) · [缺口 G-bd9f1399044c9607](../../evidence/gaps-sets-007.md#g-bd9f1399044c9607) · [状态效果 S-4cdc4859765332db](../../evidence/state_effects-sets-017.md#s-4cdc4859765332db)

### observed_connections-007715

```text
(config-tunnel-minm)# ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-65edf759217be011](../../evidence/state_effects-sets-022.md#s-65edf759217be011)

### observed_connections-007717

```text
(config-tunnel-minm)# ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-e966d382facb092a](../../evidence/state_effects-sets-049.md#s-e966d382facb092a)

### observed_connections-007722

```text
(config-tunnel-minm)# mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-176bedc2b4cf0dde](../../evidence/state_effects-sets-005.md#s-176bedc2b4cf0dde)

### observed_connections-007725

```text
(config-tunnel-minm)# mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-902240c08c9220e1](../../evidence/state_effects-sets-031.md#s-902240c08c9220e1)

### observed_connections-007707

```text
(config-tunnel-minm)# no bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-b3dace267e83b9f3](../../evidence/state_effects-sets-038.md#s-b3dace267e83b9f3)

### observed_connections-007713

```text
(config-tunnel-minm)# no bvlan dot1ad <number:1..4094> <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 3 `；EOL ` RVA 0x3397FA20 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` B-VLAN to be used in the tunnel。

[条件 C-3d9aea83394566b9](../../evidence/conditions-sets-024.md#c-3d9aea83394566b9) · [参数 P-6b47cbfc36a1bd10](../../evidence/parameters-sets-008.md#p-6b47cbfc36a1bd10) · [状态效果 S-b23e5b61069efbb8](../../evidence/state_effects-sets-038.md#s-b23e5b61069efbb8)

### observed_connections-007698

```text
(config-tunnel-minm)# no description <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 6 `；EOL ` RVA 0x33980178 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-652127ec55dfbb9d](../../evidence/conditions-sets-039.md#c-652127ec55dfbb9d) · [状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007710

```text
(config-tunnel-minm)# no ethernet egress-filter <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-68bb9ff2ac578743](../../evidence/conditions-sets-041.md#c-68bb9ff2ac578743) · [状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007696

```text
(config-tunnel-minm)# no exit <cr>
```

Handler ` RVA 0xC00EF40 `；selector ` 0 `；EOL ` RVA 0x3397F540 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007721

```text
(config-tunnel-minm)# no ip access-group in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007724

```text
(config-tunnel-minm)# no ip access-group out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007727

```text
(config-tunnel-minm)# no ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-56d33909da948abf](../../evidence/state_effects-sets-019.md#s-56d33909da948abf)

### observed_connections-007729

```text
(config-tunnel-minm)# no ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-4fd46f86f6a2e874](../../evidence/state_effects-sets-017.md#s-4fd46f86f6a2e874)

### observed_connections-007731

```text
(config-tunnel-minm)# no mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-2c3ec0c13eb187e5](../../evidence/state_effects-sets-010.md#s-2c3ec0c13eb187e5)

### observed_connections-007733

```text
(config-tunnel-minm)# no mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-7081e95e8ecd7225](../../evidence/state_effects-sets-024.md#s-7081e95e8ecd7225)

### observed_connections-007718

```text
(config-tunnel-minm)# no storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-01eec1c37ce5c2dc](../../evidence/state_effects-sets-001.md#s-01eec1c37ce5c2dc)

### observed_connections-007702

```text
(config-tunnel-minm)# no transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007704

```text
(config-tunnel-minm)# no untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-e511f13aa84235f8](../../evidence/state_effects-sets-048.md#s-e511f13aa84235f8)

### observed_connections-007736

```text
(config-tunnel-minm)# service instance <number:dynamic> <cr>
```

Handler ` RVA 0xC00EFB0 `；selector ` 4 `；EOL ` RVA 0x3397FE38 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Service Instance Identifier。

[条件 C-61b2f9fdc5f0476b](../../evidence/conditions-sets-038.md#c-61b2f9fdc5f0476b) · [缺口 G-538cce94849a91c9](../../evidence/gaps-sets-003.md#g-538cce94849a91c9) · [参数 P-5839aadef7a13e02](../../evidence/parameters-sets-007.md#p-5839aadef7a13e02)

### observed_connections-007709

```text
(config-tunnel-minm)# storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-1bad276c4f6a14a3](../../evidence/state_effects-sets-006.md#s-1bad276c4f6a14a3)

### observed_connections-007739

```text
(config-tunnel-minm)# storm-control unicast cir <?general_to_number_func_action@555588ee10a0> <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-81e4e72d927af137](../../evidence/conditions-sets-050.md#c-81e4e72d927af137) · [缺口 G-0787c61e0cde9f17](../../evidence/gaps-sets-001.md#g-0787c61e0cde9f17) · [状态效果 S-e9d4e5737149ddcc](../../evidence/state_effects-sets-049.md#s-e9d4e5737149ddcc)

### observed_connections-007694

```text
(config-tunnel-minm)# transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527)

### observed_connections-007695

```text
(config-tunnel-minm)# untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x3397F4F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527)
