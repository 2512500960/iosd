# policymap-service · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007119

```text
(config-service-policymap)# aaa attribute list <string> <cr>
```

Handler ` RVA 0x10A493D0 `；selector ` 3 `；EOL ` RVA 0x34C350B0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` AAA attribute list name。

[条件 C-f3d41eed682fefab](../../evidence/conditions-sets-094.md#c-f3d41eed682fefab) · [缺口 G-9536a252e4539ba4](../../evidence/gaps-sets-005.md#g-9536a252e4539ba4) · [参数 P-51271a612451d7a4](../../evidence/parameters-sets-007.md#p-51271a612451d7a4) · [状态效果 S-4aca4f2df1253154](../../evidence/state_effects-sets-016.md#s-4aca4f2df1253154)

### observed_connections-007070

```text
(config-service-policymap)# authenticate aaa list <string> <cr>
```

Handler ` RVA 0x10AA40F0 `；selector ` 0 `；EOL ` RVA 0x34C36138 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AAA method-list name。

[条件 C-c548c0c6c02f8a81](../../evidence/conditions-sets-076.md#c-c548c0c6c02f8a81) · [参数 P-0942aaa3fdefd1ce](../../evidence/parameters-sets-001.md#p-0942aaa3fdefd1ce)

### observed_connections-007085

```text
(config-service-policymap)# class type traffic <string> <cr>
```

Handler ` RVA 0x10A63FC0 `；selector ` 0 `；EOL ` RVA 0x34C35DD0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name of class-map to reference。

[条件 C-64cc414d61659144](../../evidence/conditions-sets-039.md#c-64cc414d61659144) · [参数 P-b7344bd1336bc7f8](../../evidence/parameters-sets-014.md#p-b7344bd1336bc7f8) · [状态效果 S-0399e19efed8d32a](../../evidence/state_effects-sets-001.md#s-0399e19efed8d32a)

### observed_connections-007110

```text
(config-service-policymap)# class type traffic default input <cr>
```

Handler ` RVA 0x10A636A0 `；selector ` 0 `；EOL ` RVA 0x34C35A20 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f59226041e280bee](../../evidence/conditions-sets-095.md#c-f59226041e280bee) · [状态效果 S-2997796020ed8add](../../evidence/state_effects-sets-009.md#s-2997796020ed8add)

### observed_connections-007060

```text
(config-service-policymap)# classname <string> <cr>
```

Handler ` RVA 0x10AA4340 `；selector ` 0 `；EOL ` RVA 0x34C37370 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DHCP classname。

[条件 C-3a1f8d53db1b4bb4](../../evidence/conditions-sets-022.md#c-3a1f8d53db1b4bb4) · [参数 P-1cd10ce8c5cc9b98](../../evidence/parameters-sets-003.md#p-1cd10ce8c5cc9b98)

### observed_connections-007042

```text
(config-service-policymap)# default authenticate <cr>
```

Handler ` RVA 0x10AA40F0 `；selector ` 0 `；EOL ` RVA 0x34C36138 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-97d55993278433d6](../../evidence/conditions-sets-059.md#c-97d55993278433d6) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007111

```text
(config-service-policymap)# default class type traffic <string> <cr>
```

Handler ` RVA 0x10A63FC0 `；selector ` 0 `；EOL ` RVA 0x34C35DD0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` name of class-map to reference。

[条件 C-64cc414d61659144](../../evidence/conditions-sets-039.md#c-64cc414d61659144) · [参数 P-b7344bd1336bc7f8](../../evidence/parameters-sets-014.md#p-b7344bd1336bc7f8) · [状态效果 S-fa0fb738ac1b0c91](../../evidence/state_effects-sets-053.md#s-fa0fb738ac1b0c91)

### observed_connections-007112

```text
(config-service-policymap)# default class type traffic default <cr>
```

Handler ` RVA 0x10A636A0 `；selector ` 0 `；EOL ` RVA 0x34C35A20 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-acac582d75e9594f](../../evidence/conditions-sets-067.md#c-acac582d75e9594f) · [状态效果 S-0ff9e0fa39ec2162](../../evidence/state_effects-sets-004.md#s-0ff9e0fa39ec2162)

### observed_connections-007059

```text
(config-service-policymap)# default classname <cr>
```

Handler ` RVA 0x10AA4340 `；selector ` 0 `；EOL ` RVA 0x34C37370 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ef5b9e9cac5da86](../../evidence/conditions-sets-055.md#c-8ef5b9e9cac5da86) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007094

```text
(config-service-policymap)# default ip access-group in <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 0 `；EOL ` RVA 0x34BDBB28 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f077dbd1d8e0798d](../../evidence/conditions-sets-093.md#c-f077dbd1d8e0798d) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007096

```text
(config-service-policymap)# default ip access-group out <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 0 `；EOL ` RVA 0x34BDBDE0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f077dbd1d8e0798d](../../evidence/conditions-sets-093.md#c-f077dbd1d8e0798d) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007072

```text
(config-service-policymap)# default ip address peer <cr>
```

Handler ` RVA 0x10A3B7A0 `；selector ` 0 `；EOL ` RVA 0x34C6B5B8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f41141bf4ef3e73c](../../evidence/conditions-sets-094.md#c-f41141bf4ef3e73c) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007078

```text
(config-service-policymap)# default ip address pool <cr>
```

Handler ` RVA 0x10A3B950 `；selector ` 0 `；EOL ` RVA 0x34C6B8D8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ad2c7d2fefe12492](../../evidence/conditions-sets-067.md#c-ad2c7d2fefe12492) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007062

```text
(config-service-policymap)# default ip portbundle <cr>
```

Handler ` RVA 0x11C30260 `；selector ` 4 `；EOL ` RVA 0x356A5A90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007064

```text
(config-service-policymap)# default ip unnumbered <cr>
```

Handler ` RVA 0x10A3B5B0 `；selector ` 0 `；EOL ` RVA 0x34C6BC10 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-62b13c7d2a00a9f1](../../evidence/conditions-sets-038.md#c-62b13c7d2a00a9f1) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007083

```text
(config-service-policymap)# default ip vrf forwarding <cr>
```

Handler ` RVA 0xE251580 `；selector ` 0 `；EOL ` RVA 0x34287F20 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52b586bb4983de37](../../evidence/conditions-sets-032.md#c-52b586bb4983de37) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007100

```text
(config-service-policymap)# default ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 1 `；EOL ` RVA 0x34BDC408 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Access-list name。

[参数 P-9d79f118372a5871](../../evidence/parameters-sets-012.md#p-9d79f118372a5871) · [状态效果 S-23ad26e2685f6baa](../../evidence/state_effects-sets-008.md#s-23ad26e2685f6baa)

### observed_connections-007108

```text
(config-service-policymap)# default ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 1 `；EOL ` RVA 0x34BDC6C0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Access-list name。

[参数 P-9d79f118372a5871](../../evidence/parameters-sets-012.md#p-9d79f118372a5871) · [状态效果 S-e492e06168186c8c](../../evidence/state_effects-sets-048.md#s-e492e06168186c8c)

### observed_connections-007054

```text
(config-service-policymap)# default keepalive <cr>
```

Handler ` RVA 0x11D036A0 `；selector ` 291 `；EOL ` RVA 0x356C9F90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f519b570450a9a3](../../evidence/conditions-sets-037.md#c-5f519b570450a9a3) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007113

```text
(config-service-policymap)# default mac access-group <string> in <cr>
```

Handler ` RVA 0xEF28550 `；selector ` 1 `；EOL ` RVA 0x3447D908 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ACL name。

[参数 P-b680689ad51a79a7](../../evidence/parameters-sets-014.md#p-b680689ad51a79a7) · [状态效果 S-3b4dfbb337702e1f](../../evidence/state_effects-sets-013.md#s-3b4dfbb337702e1f)

### observed_connections-007052

```text
(config-service-policymap)# default policy-name <cr>
```

Handler ` RVA 0x10AA4910 `；selector ` 0 `；EOL ` RVA 0x34C36C80 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-104366feac43fe9b](../../evidence/conditions-sets-006.md#c-104366feac43fe9b) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007091

```text
(config-service-policymap)# default pppoe service <string> <cr>
```

Handler ` RVA 0x11C8D2A0 `；selector ` 0 `；EOL ` RVA 0x356B6D58 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of service policy-map。

[参数 P-b444ae57b78d3a5f](../../evidence/parameters-sets-014.md#p-b444ae57b78d3a5f) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007056

```text
(config-service-policymap)# default service-monitor <cr>
```

Handler ` RVA 0x10AA4660 `；selector ` 0 `；EOL ` RVA 0x34C36FD0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d7395535f3881ed](../../evidence/conditions-sets-055.md#c-8d7395535f3881ed) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007079

```text
(config-service-policymap)# default service-policy input <string> <cr>
```

Handler ` RVA 0xD88B110 `；selector ` 0 `；EOL ` RVA 0x33F13B58 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy-map name。

[参数 P-54851e7104d7e7d5](../../evidence/parameters-sets-007.md#p-54851e7104d7e7d5) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007084

```text
(config-service-policymap)# default service-policy output <string> <cr>
```

Handler ` RVA 0xD88B110 `；selector ` 1 `；EOL ` RVA 0x33F13E18 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy-map name。

[参数 P-ed1bd76e5d208016](../../evidence/parameters-sets-018.md#p-ed1bd76e5d208016) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007045

```text
(config-service-policymap)# default sg-service-group <cr>
```

Handler ` RVA 0x10AA4C20 `；selector ` 0 `；EOL ` RVA 0x34C36518 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-624eac8ef04d7c79](../../evidence/conditions-sets-038.md#c-624eac8ef04d7c79) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007048

```text
(config-service-policymap)# default sg-service-type <cr>
```

Handler ` RVA 0x10AA4FA0 `；selector ` 0 `；EOL ` RVA 0x34C36860 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff1e242b6287efad](../../evidence/conditions-sets-098.md#c-ff1e242b6287efad) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007093

```text
(config-service-policymap)# default sub testing <string> <cr>
```

Handler ` RVA 0xE0757A0 `；selector ` 63 `；EOL ` RVA 0x341B0C00 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` aaa subscriber testing name。

[参数 P-f724d3b9dee9a9bf](../../evidence/parameters-sets-018.md#p-f724d3b9dee9a9bf) · [状态效果 S-9e270581e2ed12eb](../../evidence/state_effects-sets-034.md#s-9e270581e2ed12eb)

### observed_connections-007099

```text
(config-service-policymap)# default traffic class input access-group <cr>
```

Handler ` RVA 0x1094D1F0 `；selector ` 2 `；EOL ` RVA 0x34C46690 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c842ae055b6fe7c](../../evidence/conditions-sets-023.md#c-3c842ae055b6fe7c) · [状态效果 S-b91894338603431c](../../evidence/state_effects-sets-039.md#s-b91894338603431c)

### observed_connections-007107

```text
(config-service-policymap)# default traffic class input default <cr>
```

Handler ` RVA 0x1094D1F0 `；selector ` 3 `；EOL ` RVA 0x34C46AA8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b70c096687e656f5](../../evidence/conditions-sets-071.md#c-b70c096687e656f5) · [状态效果 S-b91894338603431c](../../evidence/state_effects-sets-039.md#s-b91894338603431c)

### observed_connections-007039

```text
(config-service-policymap)# exit <cr>
```

Handler ` RVA 0x10A49AB0 `；selector ` 0 `；EOL ` RVA 0x34C34C08 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-81ab0512244906d4](../../evidence/conditions-sets-050.md#c-81ab0512244906d4)

### observed_connections-007086

```text
(config-service-policymap)# ip access-group <number:1..199> in <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 0 `；EOL ` RVA 0x34BDBB28 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[参数 P-3a5f2b1389adfc32](../../evidence/parameters-sets-005.md#p-3a5f2b1389adfc32) · [状态效果 S-b8a3fc644e419373](../../evidence/state_effects-sets-039.md#s-b8a3fc644e419373)

### observed_connections-007092

```text
(config-service-policymap)# ip access-group <number:1..199> out <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 0 `；EOL ` RVA 0x34BDBDE0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list (standard or extended)。

[参数 P-3a5f2b1389adfc32](../../evidence/parameters-sets-005.md#p-3a5f2b1389adfc32) · [状态效果 S-82264a97b7d6ba63](../../evidence/state_effects-sets-028.md#s-82264a97b7d6ba63)

### observed_connections-007071

```text
(config-service-policymap)# ip address peer <address> <cr>
```

Handler ` RVA 0x10A3B7A0 `；selector ` 0 `；EOL ` RVA 0x34C6B5B8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for remote end (peer)。

[条件 C-2a6a9dbb19f0faf7](../../evidence/conditions-sets-017.md#c-2a6a9dbb19f0faf7) · [参数 P-37062863863e3d61](../../evidence/parameters-sets-005.md#p-37062863863e3d61)

### observed_connections-007075

```text
(config-service-policymap)# ip address pool <string> <cr>
```

Handler ` RVA 0x10A3B950 `；selector ` 0 `；EOL ` RVA 0x34C6B8D8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-8cdf8c204a495625](../../evidence/conditions-sets-055.md#c-8cdf8c204a495625) · [参数 P-cd99f0d17771c72f](../../evidence/parameters-sets-016.md#p-cd99f0d17771c72f)

### observed_connections-007044

```text
(config-service-policymap)# ip portbundle <cr>
```

Handler ` RVA 0x11C30260 `；selector ` 4 `；EOL ` RVA 0x356A5A90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007114

```text
(config-service-policymap)# ip unnumbered <interface> <cr>
```

Handler ` RVA 0x10A3B5B0 `；selector ` 0 `；EOL ` RVA 0x34C6BC10 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-860db07252cbbf6c](../../evidence/conditions-sets-052.md#c-860db07252cbbf6c) · [缺口 G-3f5417793193f4b1](../../evidence/gaps-sets-003.md#g-3f5417793193f4b1) · [参数 P-ed69fff39074aef5](../../evidence/parameters-sets-018.md#p-ed69fff39074aef5)

### observed_connections-007081

```text
(config-service-policymap)# ip vrf forwarding <string> <cr>
```

Handler ` RVA 0xE251580 `；selector ` 0 `；EOL ` RVA 0x34287F20 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Table name。

[条件 C-366d36498d27a0f6](../../evidence/conditions-sets-021.md#c-366d36498d27a0f6) · [参数 P-b64339daa092fcf2](../../evidence/parameters-sets-014.md#p-b64339daa092fcf2)

### observed_connections-007076

```text
(config-service-policymap)# ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 1 `；EOL ` RVA 0x34BDC408 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name。

[参数 P-9d79f118372a5871](../../evidence/parameters-sets-012.md#p-9d79f118372a5871) · [状态效果 S-120a233f9c188e0c](../../evidence/state_effects-sets-004.md#s-120a233f9c188e0c)

### observed_connections-007082

```text
(config-service-policymap)# ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 1 `；EOL ` RVA 0x34BDC6C0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name。

[参数 P-9d79f118372a5871](../../evidence/parameters-sets-012.md#p-9d79f118372a5871) · [状态效果 S-a92258d98309b700](../../evidence/state_effects-sets-036.md#s-a92258d98309b700)

### observed_connections-007118

```text
(config-service-policymap)# keepalive <?option@55558ac1dff0> <?number_help_func_action@55558ac1e0f0> <cr>
```

Handler ` RVA 0x11D036A0 `；selector ` 291 `；EOL ` RVA 0x356C9F90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c2335eeedcf7faca](../../evidence/conditions-sets-075.md#c-c2335eeedcf7faca) · [缺口 G-24e723fe386572b8](../../evidence/gaps-sets-002.md#g-24e723fe386572b8) · [状态效果 S-7facb250247462ca](../../evidence/state_effects-sets-027.md#s-7facb250247462ca)

### observed_connections-007040

```text
(config-service-policymap)# keepalive <cr>
```

Handler ` RVA 0x11D036A0 `；selector ` 291 `；EOL ` RVA 0x356C9F90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-924e1589ec858663](../../evidence/conditions-sets-056.md#c-924e1589ec858663) · [状态效果 S-49641e45683c2f59](../../evidence/state_effects-sets-016.md#s-49641e45683c2f59)

### observed_connections-007088

```text
(config-service-policymap)# mac access-group <string> in <cr>
```

Handler ` RVA 0xEF28550 `；selector ` 1 `；EOL ` RVA 0x3447D908 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ACL name。

[参数 P-b680689ad51a79a7](../../evidence/parameters-sets-014.md#p-b680689ad51a79a7) · [状态效果 S-c657a68b0edb4606](../../evidence/state_effects-sets-042.md#s-c657a68b0edb4606)

### observed_connections-007041

```text
(config-service-policymap)# no authenticate <cr>
```

Handler ` RVA 0x10AA40F0 `；selector ` 0 `；EOL ` RVA 0x34C36138 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b31ece9b3253f007](../../evidence/conditions-sets-069.md#c-b31ece9b3253f007) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007104

```text
(config-service-policymap)# no class type traffic <string> <cr>
```

Handler ` RVA 0x10A63FC0 `；selector ` 0 `；EOL ` RVA 0x34C35DD0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` name of class-map to reference。

[条件 C-64cc414d61659144](../../evidence/conditions-sets-039.md#c-64cc414d61659144) · [参数 P-b7344bd1336bc7f8](../../evidence/parameters-sets-014.md#p-b7344bd1336bc7f8) · [状态效果 S-73c1a3cf8159590e](../../evidence/state_effects-sets-025.md#s-73c1a3cf8159590e)

### observed_connections-007106

```text
(config-service-policymap)# no class type traffic default <cr>
```

Handler ` RVA 0x10A636A0 `；selector ` 0 `；EOL ` RVA 0x34C35A20 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-58feb2782fdf5116](../../evidence/conditions-sets-035.md#c-58feb2782fdf5116) · [状态效果 S-ab569c76519eebd8](../../evidence/state_effects-sets-036.md#s-ab569c76519eebd8)

### observed_connections-007057

```text
(config-service-policymap)# no classname <cr>
```

Handler ` RVA 0x10AA4340 `；selector ` 0 `；EOL ` RVA 0x34C37370 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-84d590d812738685](../../evidence/conditions-sets-051.md#c-84d590d812738685) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007090

```text
(config-service-policymap)# no ip access-group in <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 0 `；EOL ` RVA 0x34BDBB28 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f077dbd1d8e0798d](../../evidence/conditions-sets-093.md#c-f077dbd1d8e0798d) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007095

```text
(config-service-policymap)# no ip access-group out <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 0 `；EOL ` RVA 0x34BDBDE0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f077dbd1d8e0798d](../../evidence/conditions-sets-093.md#c-f077dbd1d8e0798d) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007069

```text
(config-service-policymap)# no ip address peer <cr>
```

Handler ` RVA 0x10A3B7A0 `；selector ` 0 `；EOL ` RVA 0x34C6B5B8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d02a579498022243](../../evidence/conditions-sets-080.md#c-d02a579498022243) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007073

```text
(config-service-policymap)# no ip address pool <cr>
```

Handler ` RVA 0x10A3B950 `；selector ` 0 `；EOL ` RVA 0x34C6B8D8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e243de5f898825b0](../../evidence/conditions-sets-087.md#c-e243de5f898825b0) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007061

```text
(config-service-policymap)# no ip portbundle <cr>
```

Handler ` RVA 0x11C30260 `；selector ` 4 `；EOL ` RVA 0x356A5A90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007063

```text
(config-service-policymap)# no ip unnumbered <cr>
```

Handler ` RVA 0x10A3B5B0 `；selector ` 0 `；EOL ` RVA 0x34C6BC10 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-583438c9fedefdb5](../../evidence/conditions-sets-035.md#c-583438c9fedefdb5) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007077

```text
(config-service-policymap)# no ip vrf forwarding <cr>
```

Handler ` RVA 0xE251580 `；selector ` 0 `；EOL ` RVA 0x34287F20 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-84422f3d50d83cc2](../../evidence/conditions-sets-051.md#c-84422f3d50d83cc2) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007098

```text
(config-service-policymap)# no ipv6 traffic-filter <string> in <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 1 `；EOL ` RVA 0x34BDC408 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Access-list name。

[参数 P-9d79f118372a5871](../../evidence/parameters-sets-012.md#p-9d79f118372a5871) · [状态效果 S-5723c7fee735bbec](../../evidence/state_effects-sets-019.md#s-5723c7fee735bbec)

### observed_connections-007102

```text
(config-service-policymap)# no ipv6 traffic-filter <string> out <cr>
```

Handler ` RVA 0x10663A00 `；selector ` 1 `；EOL ` RVA 0x34BDC6C0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Access-list name。

[参数 P-9d79f118372a5871](../../evidence/parameters-sets-012.md#p-9d79f118372a5871) · [状态效果 S-c4d041d8531b3e35](../../evidence/state_effects-sets-042.md#s-c4d041d8531b3e35)

### observed_connections-007050

```text
(config-service-policymap)# no keepalive <cr>
```

Handler ` RVA 0x11D036A0 `；selector ` 291 `；EOL ` RVA 0x356C9F90 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-968651c90b12d183](../../evidence/conditions-sets-058.md#c-968651c90b12d183) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007109

```text
(config-service-policymap)# no mac access-group <string> in <cr>
```

Handler ` RVA 0xEF28550 `；selector ` 1 `；EOL ` RVA 0x3447D908 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` ACL name。

[参数 P-b680689ad51a79a7](../../evidence/parameters-sets-014.md#p-b680689ad51a79a7) · [状态效果 S-cfa983deccd619bc](../../evidence/state_effects-sets-044.md#s-cfa983deccd619bc)

### observed_connections-007049

```text
(config-service-policymap)# no policy-name <cr>
```

Handler ` RVA 0x10AA4910 `；selector ` 0 `；EOL ` RVA 0x34C36C80 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fbaaf10c91e496e7](../../evidence/conditions-sets-097.md#c-fbaaf10c91e496e7) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007087

```text
(config-service-policymap)# no pppoe service <string> <cr>
```

Handler ` RVA 0x11C8D2A0 `；selector ` 0 `；EOL ` RVA 0x356B6D58 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Name of service policy-map。

[参数 P-b444ae57b78d3a5f](../../evidence/parameters-sets-014.md#p-b444ae57b78d3a5f) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007053

```text
(config-service-policymap)# no service-monitor <cr>
```

Handler ` RVA 0x10AA4660 `；selector ` 0 `；EOL ` RVA 0x34C36FD0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d3db2f2b2d3057b3](../../evidence/conditions-sets-082.md#c-d3db2f2b2d3057b3) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007074

```text
(config-service-policymap)# no service-policy input <string> <cr>
```

Handler ` RVA 0xD88B110 `；selector ` 0 `；EOL ` RVA 0x33F13B58 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` policy-map name。

[参数 P-54851e7104d7e7d5](../../evidence/parameters-sets-007.md#p-54851e7104d7e7d5) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007080

```text
(config-service-policymap)# no service-policy output <string> <cr>
```

Handler ` RVA 0xD88B110 `；selector ` 1 `；EOL ` RVA 0x33F13E18 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` policy-map name。

[参数 P-ed1bd76e5d208016](../../evidence/parameters-sets-018.md#p-ed1bd76e5d208016) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007043

```text
(config-service-policymap)# no sg-service-group <cr>
```

Handler ` RVA 0x10AA4C20 `；selector ` 0 `；EOL ` RVA 0x34C36518 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-682d8a2a5e03b7ef](../../evidence/conditions-sets-040.md#c-682d8a2a5e03b7ef) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007046

```text
(config-service-policymap)# no sg-service-type <cr>
```

Handler ` RVA 0x10AA4FA0 `；selector ` 0 `；EOL ` RVA 0x34C36860 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50c5d7eb912c2625](../../evidence/conditions-sets-032.md#c-50c5d7eb912c2625) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007089

```text
(config-service-policymap)# no sub testing <string> <cr>
```

Handler ` RVA 0xE0757A0 `；selector ` 63 `；EOL ` RVA 0x341B0C00 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` aaa subscriber testing name。

[参数 P-f724d3b9dee9a9bf](../../evidence/parameters-sets-018.md#p-f724d3b9dee9a9bf) · [状态效果 S-4d7e0770dec17c9b](../../evidence/state_effects-sets-017.md#s-4d7e0770dec17c9b)

### observed_connections-007097

```text
(config-service-policymap)# no traffic class input access-group <cr>
```

Handler ` RVA 0x1094D1F0 `；selector ` 2 `；EOL ` RVA 0x34C46690 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-01c974831b961af6](../../evidence/conditions-sets-001.md#c-01c974831b961af6) · [状态效果 S-366bb62f526fe800](../../evidence/state_effects-sets-012.md#s-366bb62f526fe800)

### observed_connections-007101

```text
(config-service-policymap)# no traffic class input default <cr>
```

Handler ` RVA 0x1094D1F0 `；selector ` 3 `；EOL ` RVA 0x34C46AA8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-26a3730692fc1ad6](../../evidence/conditions-sets-015.md#c-26a3730692fc1ad6) · [状态效果 S-366bb62f526fe800](../../evidence/state_effects-sets-012.md#s-366bb62f526fe800)

### observed_connections-007055

```text
(config-service-policymap)# policy-name <string> <cr>
```

Handler ` RVA 0x10AA4910 `；selector ` 0 `；EOL ` RVA 0x34C36C80 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` External policy name。

[条件 C-28e3e8474681e9ca](../../evidence/conditions-sets-016.md#c-28e3e8474681e9ca) · [参数 P-0c3a905a330c10e9](../../evidence/parameters-sets-001.md#p-0c3a905a330c10e9)

### observed_connections-007067

```text
(config-service-policymap)# pppoe service <string> <cr>
```

Handler ` RVA 0x11C8D2A0 `；selector ` 0 `；EOL ` RVA 0x356B6D58 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of service policy-map。

[参数 P-b444ae57b78d3a5f](../../evidence/parameters-sets-014.md#p-b444ae57b78d3a5f)

### observed_connections-007115

```text
(config-service-policymap)# service local <cr>
```

Handler ` RVA 0x10A493D0 `；selector ` 2 `；EOL ` RVA 0x34C35398 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-71d742b057cfdc89](../../evidence/conditions-sets-044.md#c-71d742b057cfdc89) · [缺口 G-9536a252e4539ba4](../../evidence/gaps-sets-005.md#g-9536a252e4539ba4) · [状态效果 S-f75b4d85ac984357](../../evidence/state_effects-sets-052.md#s-f75b4d85ac984357)

### observed_connections-007117

```text
(config-service-policymap)# service none <string> <cr>
```

Handler ` RVA 0xFFD2270 `；selector ` 61 `；EOL ` RVA 0x349675D0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` none directive type。

[条件 C-71d742b057cfdc89](../../evidence/conditions-sets-044.md#c-71d742b057cfdc89) · [缺口 G-9536a252e4539ba4](../../evidence/gaps-sets-005.md#g-9536a252e4539ba4) · [参数 P-d0f0a69d9dc86d3a](../../evidence/parameters-sets-016.md#p-d0f0a69d9dc86d3a) · [状态效果 S-2d727094bc670ad6](../../evidence/state_effects-sets-010.md#s-2d727094bc670ad6)

### observed_connections-007116

```text
(config-service-policymap)# service vpdn <cr>
```

Handler ` RVA 0x11D58480 `；selector ` 134 `；EOL ` RVA 0x356FEE88 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ca1ef49fb90d8a16](../../evidence/conditions-sets-078.md#c-ca1ef49fb90d8a16) · [缺口 G-9536a252e4539ba4](../../evidence/gaps-sets-005.md#g-9536a252e4539ba4) · [状态效果 S-23d2b181c577e856](../../evidence/state_effects-sets-008.md#s-23d2b181c577e856)

### observed_connections-007058

```text
(config-service-policymap)# service-monitor enable <cr>
```

Handler ` RVA 0x10AA4660 `；selector ` 0 `；EOL ` RVA 0x34C36FD0 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3587c1360d100bb3](../../evidence/conditions-sets-021.md#c-3587c1360d100bb3) · [状态效果 S-de6a0f0b540012fe](../../evidence/state_effects-sets-047.md#s-de6a0f0b540012fe)

### observed_connections-007065

```text
(config-service-policymap)# service-policy input <string> <cr>
```

Handler ` RVA 0xD88B110 `；selector ` 0 `；EOL ` RVA 0x33F13B58 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` policy-map name。

[参数 P-54851e7104d7e7d5](../../evidence/parameters-sets-007.md#p-54851e7104d7e7d5)

### observed_connections-007066

```text
(config-service-policymap)# service-policy output <string> <cr>
```

Handler ` RVA 0xD88B110 `；selector ` 1 `；EOL ` RVA 0x33F13E18 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` policy-map name。

[参数 P-ed1bd76e5d208016](../../evidence/parameters-sets-018.md#p-ed1bd76e5d208016)

### observed_connections-007047

```text
(config-service-policymap)# sg-service-group <string> <cr>
```

Handler ` RVA 0x10AA4C20 `；selector ` 0 `；EOL ` RVA 0x34C36518 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SG Service Group name。

[条件 C-ecb37be564d7aa0b](../../evidence/conditions-sets-091.md#c-ecb37be564d7aa0b) · [参数 P-bc63c855183ae1a1](../../evidence/parameters-sets-014.md#p-bc63c855183ae1a1)

### observed_connections-007051

```text
(config-service-policymap)# sg-service-type primary <cr>
```

Handler ` RVA 0x10AA4FA0 `；selector ` 0 `；EOL ` RVA 0x34C36860 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2f835c8aafb4d1f5](../../evidence/conditions-sets-019.md#c-2f835c8aafb4d1f5) · [状态效果 S-15c8f70db19bf65b](../../evidence/state_effects-sets-005.md#s-15c8f70db19bf65b)

### observed_connections-007068

```text
(config-service-policymap)# sub testing <string> <cr>
```

Handler ` RVA 0xE0757A0 `；selector ` 63 `；EOL ` RVA 0x341B0C00 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` aaa subscriber testing name。

[参数 P-f724d3b9dee9a9bf](../../evidence/parameters-sets-018.md#p-f724d3b9dee9a9bf)

### observed_connections-007105

```text
(config-service-policymap)# traffic class input access-group <number:1..2799> <cr>
```

Handler ` RVA 0x1094D1F0 `；selector ` 2 `；EOL ` RVA 0x34C46690 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access List number。

[条件 C-7fa583355a936ba3](../../evidence/conditions-sets-049.md#c-7fa583355a936ba3) · [参数 P-bb3857eca48b09e4](../../evidence/parameters-sets-014.md#p-bb3857eca48b09e4) · [状态效果 S-d8d5f8a6ebaef5a8](../../evidence/state_effects-sets-046.md#s-d8d5f8a6ebaef5a8)

### observed_connections-007103

```text
(config-service-policymap)# traffic class input default drop <cr>
```

Handler ` RVA 0x1094D1F0 `；selector ` 3 `；EOL ` RVA 0x34C46AA8 `。

模式根 ` RVA 0x34C34B60 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-743e1c176c866a1d](../../evidence/conditions-sets-045.md#c-743e1c176c866a1d) · [状态效果 S-d8d5f8a6ebaef5a8](../../evidence/state_effects-sets-046.md#s-d8d5f8a6ebaef5a8)

