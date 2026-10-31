# config-mac-tunnel-service-instance · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007687

```text
(config-tunnel-srv)# bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bridge-domain number。

[条件 C-4e93df83155b5a25](../../evidence/conditions-sets-031.md#c-4e93df83155b5a25) · [缺口 G-b993303d8a3e9924](../../evidence/gaps-sets-007.md#g-b993303d8a3e9924) · [参数 P-735c645cccdd523e](../../evidence/parameters-sets-009.md#p-735c645cccdd523e) · [状态效果 S-59bea50fdc0db030](../../evidence/state_effects-sets-019.md#s-59bea50fdc0db030)

### observed_connections-007647

```text
(config-tunnel-srv)# bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-bcdc24a59e9ee46e](../../evidence/state_effects-sets-040.md#s-bcdc24a59e9ee46e)

### observed_connections-007654

```text
(config-tunnel-srv)# default bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-48f176535026b3fd](../../evidence/state_effects-sets-016.md#s-48f176535026b3fd)

### observed_connections-007646

```text
(config-tunnel-srv)# default description <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 4 `；EOL ` RVA 0x33983798 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d98703c825ce1da3](../../evidence/conditions-sets-084.md#c-d98703c825ce1da3) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007675

```text
(config-tunnel-srv)# default encapsulation dot1ah isid <number:1..16777215> <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 1 `；EOL ` RVA 0x33983430 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IEEE 802.1ah I-SID value。

[条件 C-ed5e26dbd731d658](../../evidence/conditions-sets-092.md#c-ed5e26dbd731d658) · [参数 P-2b357c5eaabeb96b](../../evidence/parameters-sets-004.md#p-2b357c5eaabeb96b) · [状态效果 S-b4a8e6e0fa302d8b](../../evidence/state_effects-sets-038.md#s-b4a8e6e0fa302d8b)

### observed_connections-007658

```text
(config-tunnel-srv)# default ethernet egress-filter <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8753624b0239f673](../../evidence/conditions-sets-052.md#c-8753624b0239f673) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007643

```text
(config-tunnel-srv)# default exit <cr>
```

Handler ` RVA 0xC00E110 `；selector ` 0 `；EOL ` RVA 0x33982FE0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007670

```text
(config-tunnel-srv)# default ip access-group in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007673

```text
(config-tunnel-srv)# default ip access-group out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007680

```text
(config-tunnel-srv)# default ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-fb4e84af2e7fa3c2](../../evidence/state_effects-sets-053.md#s-fb4e84af2e7fa3c2)

### observed_connections-007682

```text
(config-tunnel-srv)# default ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-b1f848dbc4a366ae](../../evidence/state_effects-sets-038.md#s-b1f848dbc4a366ae)

### observed_connections-007684

```text
(config-tunnel-srv)# default mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-220fca76c3274e92](../../evidence/state_effects-sets-008.md#s-220fca76c3274e92)

### observed_connections-007686

```text
(config-tunnel-srv)# default mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-683bcdb8b22a9e17](../../evidence/state_effects-sets-022.md#s-683bcdb8b22a9e17)

### observed_connections-007661

```text
(config-tunnel-srv)# default mac-flush notification mirp <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 5 `；EOL ` RVA 0x33983B08 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed5e26dbd731d658](../../evidence/conditions-sets-092.md#c-ed5e26dbd731d658) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007678

```text
(config-tunnel-srv)# default mac-flush notification mirp cos <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 6 `；EOL ` RVA 0x33983B70 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84939b0633a9f462](../../evidence/conditions-sets-051.md#c-84939b0633a9f462) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007667

```text
(config-tunnel-srv)# default storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-684557b52adb7ab8](../../evidence/state_effects-sets-022.md#s-684557b52adb7ab8)

### observed_connections-007649

```text
(config-tunnel-srv)# default transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007651

```text
(config-tunnel-srv)# default untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-c18d7f0b2c4b025a](../../evidence/state_effects-sets-041.md#s-c18d7f0b2c4b025a)

### observed_connections-007645

```text
(config-tunnel-srv)# description <string> <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 4 `；EOL ` RVA 0x33983798 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 240 characters describing this mac_tunnel。

[条件 C-96193467600e6892](../../evidence/conditions-sets-058.md#c-96193467600e6892) · [参数 P-960198cb886f3554](../../evidence/parameters-sets-012.md#p-960198cb886f3554)

### observed_connections-007659

```text
(config-tunnel-srv)# encapsulation dot1ah isid <number:1..16777215> <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 1 `；EOL ` RVA 0x33983430 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IEEE 802.1ah I-SID value。

[条件 C-ed5e26dbd731d658](../../evidence/conditions-sets-092.md#c-ed5e26dbd731d658) · [参数 P-2b357c5eaabeb96b](../../evidence/parameters-sets-004.md#p-2b357c5eaabeb96b) · [状态效果 S-19f1dae93a883255](../../evidence/state_effects-sets-006.md#s-19f1dae93a883255)

### observed_connections-007657

```text
(config-tunnel-srv)# ethernet egress-filter disable <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1be6c7d7f6ba41c](../../evidence/conditions-sets-081.md#c-d1be6c7d7f6ba41c) · [状态效果 S-5c85aab71f02acf9](../../evidence/state_effects-sets-020.md#s-5c85aab71f02acf9)

### observed_connections-007639

```text
(config-tunnel-srv)# exit <cr>
```

Handler ` RVA 0xC00E110 `；selector ` 0 `；EOL ` RVA 0x33982FE0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007663

```text
(config-tunnel-srv)# ip access-group <number:1..199> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-263551246ce1417a](../../evidence/conditions-sets-015.md#c-263551246ce1417a) · [参数 P-39ee2607d399f61c](../../evidence/parameters-sets-005.md#p-39ee2607d399f61c)

### observed_connections-007666

```text
(config-tunnel-srv)# ip access-group <number:1..199> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[条件 C-263551246ce1417a](../../evidence/conditions-sets-015.md#c-263551246ce1417a) · [参数 P-39ee2607d399f61c](../../evidence/parameters-sets-005.md#p-39ee2607d399f61c)

### observed_connections-007691

```text
(config-tunnel-srv)# ip flow monitor <?option@555588f5efa0> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0B1C8 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2680cb17110d020b](../../evidence/conditions-sets-015.md#c-2680cb17110d020b) · [缺口 G-576c1b7539f300fa](../../evidence/gaps-sets-004.md#g-576c1b7539f300fa) · [状态效果 S-0801271744601689](../../evidence/state_effects-sets-002.md#s-0801271744601689)

### observed_connections-007688

```text
(config-tunnel-srv)# ip flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0B480 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2fecafea42d2c258](../../evidence/conditions-sets-019.md#c-2fecafea42d2c258) · [缺口 G-df678120ccaad078](../../evidence/gaps-sets-008.md#g-df678120ccaad078) · [状态效果 S-0801271744601689](../../evidence/state_effects-sets-002.md#s-0801271744601689)

### observed_connections-007692

```text
(config-tunnel-srv)# ipv6 flow monitor <?option@555588f60368> sampler <cr>
```

Handler ` RVA 0xC1F7CA0 `；selector ` 0 `；EOL ` RVA 0x33A0C590 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b266e79d8a56d625](../../evidence/conditions-sets-069.md#c-b266e79d8a56d625) · [缺口 G-43bf3f2e95a39d33](../../evidence/gaps-sets-003.md#g-43bf3f2e95a39d33) · [状态效果 S-4cdc4859765332db](../../evidence/state_effects-sets-017.md#s-4cdc4859765332db)

### observed_connections-007689

```text
(config-tunnel-srv)# ipv6 flow monitor <cr>
```

Handler ` RVA 0xC1F7D50 `；selector ` 0 `；EOL ` RVA 0x33A0C848 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-514b1dbe27318167](../../evidence/conditions-sets-032.md#c-514b1dbe27318167) · [缺口 G-bd9f1399044c9607](../../evidence/gaps-sets-007.md#g-bd9f1399044c9607) · [状态效果 S-4cdc4859765332db](../../evidence/state_effects-sets-017.md#s-4cdc4859765332db)

### observed_connections-007662

```text
(config-tunnel-srv)# ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-65edf759217be011](../../evidence/state_effects-sets-022.md#s-65edf759217be011)

### observed_connections-007664

```text
(config-tunnel-srv)# ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-e966d382facb092a](../../evidence/state_effects-sets-049.md#s-e966d382facb092a)

### observed_connections-007669

```text
(config-tunnel-srv)# mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-176bedc2b4cf0dde](../../evidence/state_effects-sets-005.md#s-176bedc2b4cf0dde)

### observed_connections-007672

```text
(config-tunnel-srv)# mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-902240c08c9220e1](../../evidence/state_effects-sets-031.md#s-902240c08c9220e1)

### observed_connections-007652

```text
(config-tunnel-srv)# mac-flush notification mirp <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 5 `；EOL ` RVA 0x33983B08 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ed5e26dbd731d658](../../evidence/conditions-sets-092.md#c-ed5e26dbd731d658)

### observed_connections-007677

```text
(config-tunnel-srv)# mac-flush notification mirp cos <number:0..7> <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 6 `；EOL ` RVA 0x33983B70 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MIRP message cos value。

[条件 C-50d71f5152b7f16d](../../evidence/conditions-sets-032.md#c-50d71f5152b7f16d) · [参数 P-54876f42cb968400](../../evidence/parameters-sets-007.md#p-54876f42cb968400)

### observed_connections-007653

```text
(config-tunnel-srv)# no bridge-domain from-encapsulation <cr>
```

Handler ` RVA 0xBF7FCB0 `；selector ` 0 `；EOL ` RVA 0x33958EF8 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e7f8789eecbd2bd1](../../evidence/conditions-sets-090.md#c-e7f8789eecbd2bd1) · [状态效果 S-c88c36b79389d278](../../evidence/state_effects-sets-042.md#s-c88c36b79389d278)

### observed_connections-007644

```text
(config-tunnel-srv)# no description <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 4 `；EOL ` RVA 0x33983798 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d543b518f96ca26a](../../evidence/conditions-sets-082.md#c-d543b518f96ca26a) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007674

```text
(config-tunnel-srv)# no encapsulation dot1ah isid <number:1..16777215> <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 1 `；EOL ` RVA 0x33983430 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` IEEE 802.1ah I-SID value。

[条件 C-ed5e26dbd731d658](../../evidence/conditions-sets-092.md#c-ed5e26dbd731d658) · [参数 P-2b357c5eaabeb96b](../../evidence/parameters-sets-004.md#p-2b357c5eaabeb96b) · [状态效果 S-0042739eb8a2ecbc](../../evidence/state_effects-sets-001.md#s-0042739eb8a2ecbc)

### observed_connections-007656

```text
(config-tunnel-srv)# no ethernet egress-filter <cr>
```

Handler ` RVA 0xC03E6B0 `；selector ` 14 `；EOL ` RVA 0x339895B0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-68bb9ff2ac578743](../../evidence/conditions-sets-041.md#c-68bb9ff2ac578743) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007642

```text
(config-tunnel-srv)# no exit <cr>
```

Handler ` RVA 0xC00E110 `；selector ` 0 `；EOL ` RVA 0x33982FE0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007668

```text
(config-tunnel-srv)# no ip access-group in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 0 `；EOL ` RVA 0x3447C370 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007671

```text
(config-tunnel-srv)# no ip access-group out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 1 `；EOL ` RVA 0x3447C618 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-81dcf23d5e969725](../../evidence/conditions-sets-050.md#c-81dcf23d5e969725) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007679

```text
(config-tunnel-srv)# no ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 2 `；EOL ` RVA 0x3447CC60 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-fa8497fb7072d125](../../evidence/state_effects-sets-053.md#s-fa8497fb7072d125)

### observed_connections-007681

```text
(config-tunnel-srv)# no ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 3 `；EOL ` RVA 0x3447CF18 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-823531dbc725f732](../../evidence/conditions-sets-050.md#c-823531dbc725f732) · [参数 P-a815cd73ebdcbb17](../../evidence/parameters-sets-013.md#p-a815cd73ebdcbb17) · [状态效果 S-3f15ec30e4100801](../../evidence/state_effects-sets-014.md#s-3f15ec30e4100801)

### observed_connections-007683

```text
(config-tunnel-srv)# no mac access-group <string> in <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 6 `；EOL ` RVA 0x3447BC30 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-c3dc22356a421d71](../../evidence/conditions-sets-076.md#c-c3dc22356a421d71) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-b8bfa63c425ecc2c](../../evidence/state_effects-sets-039.md#s-b8bfa63c425ecc2c)

### observed_connections-007685

```text
(config-tunnel-srv)# no mac access-group <string> out <cr>
```

Handler ` RVA 0xEF287D0 `；selector ` 7 `；EOL ` RVA 0x3447BF28 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[条件 C-aa9a0f673742b015](../../evidence/conditions-sets-066.md#c-aa9a0f673742b015) · [参数 P-412d305d445a2b42](../../evidence/parameters-sets-005.md#p-412d305d445a2b42) · [状态效果 S-02a0fd9299f06c4e](../../evidence/state_effects-sets-001.md#s-02a0fd9299f06c4e)

### observed_connections-007660

```text
(config-tunnel-srv)# no mac-flush notification mirp <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 5 `；EOL ` RVA 0x33983B08 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ed5e26dbd731d658](../../evidence/conditions-sets-092.md#c-ed5e26dbd731d658) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007676

```text
(config-tunnel-srv)# no mac-flush notification mirp cos <cr>
```

Handler ` RVA 0xC00E180 `；selector ` 6 `；EOL ` RVA 0x33983B70 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-85bca44185ff59fa](../../evidence/conditions-sets-052.md#c-85bca44185ff59fa) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007665

```text
(config-tunnel-srv)# no storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-67b0995b2897da0d](../../evidence/state_effects-sets-022.md#s-67b0995b2897da0d)

### observed_connections-007648

```text
(config-tunnel-srv)# no transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007650

```text
(config-tunnel-srv)# no untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527) · [状态效果 S-facafeac1c0d8e1b](../../evidence/state_effects-sets-053.md#s-facafeac1c0d8e1b)

### observed_connections-007655

```text
(config-tunnel-srv)# storm-control action shutdown <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b565d085ab24399](../../evidence/conditions-sets-030.md#c-4b565d085ab24399) · [状态效果 S-1bad276c4f6a14a3](../../evidence/state_effects-sets-006.md#s-1bad276c4f6a14a3)

### observed_connections-007690

```text
(config-tunnel-srv)# storm-control unicast cir <?general_to_number_func_action@555588ee10a0> <cr>
```

Handler ` RVA 0xC069820 `；selector ` 0 `；EOL ` RVA 0x3398CC48 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-81e4e72d927af137](../../evidence/conditions-sets-050.md#c-81e4e72d927af137) · [缺口 G-0787c61e0cde9f17](../../evidence/gaps-sets-001.md#g-0787c61e0cde9f17) · [状态效果 S-e9d4e5737149ddcc](../../evidence/state_effects-sets-049.md#s-e9d4e5737149ddcc)

### observed_connections-007640

```text
(config-tunnel-srv)# transparent-cfm <cr>
```

Handler ` RVA 0xBEB3720 `；selector ` 0 `；EOL ` RVA 0x3391EA18 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527)

### observed_connections-007641

```text
(config-tunnel-srv)# untagged-cfm <cr>
```

Handler ` RVA 0xBEB3A70 `；selector ` 0 `；EOL ` RVA 0x3391ECD0 `。

模式根 ` RVA 0x33982F90 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-702ec7acce632527](../../evidence/conditions-sets-043.md#c-702ec7acce632527)

