# router_eigrp_classic · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-006727

```text
(config-router)# address-family ipv4 vrf <string> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 119 `；EOL ` RVA 0x346E0228 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Virtual Routing/Forwarding instance name。

[参数 P-a340f179234f1a84](../../evidence/parameters-sets-012.md#p-a340f179234f1a84) · [状态效果 S-c6f3bbdebb53bf59](../../evidence/state_effects-sets-042.md#s-c6f3bbdebb53bf59)

### observed_connections-006645

```text
(config-router)# auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346E6560 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fcaf0b75cedef3a](../../evidence/conditions-sets-043.md#c-6fcaf0b75cedef3a)

### observed_connections-006655

```text
(config-router)# bfd all-interfaces <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346E16E0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-069ba5e8c5c023e6](../../evidence/state_effects-sets-002.md#s-069ba5e8c5c023e6)

### observed_connections-006755

```text
(config-router)# bfd interface <interface> <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346E16E0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e6a6734969289031](../../evidence/conditions-sets-089.md#c-e6a6734969289031) · [缺口 G-4b4793012b3785f8](../../evidence/gaps-sets-003.md#g-4b4793012b3785f8) · [参数 P-cbbfcfc76831dd96](../../evidence/parameters-sets-015.md#p-cbbfcfc76831dd96)

### observed_connections-006744

```text
(config-router)# default address-family ipv4 vrf <string> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 119 `；EOL ` RVA 0x346E0228 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Virtual Routing/Forwarding instance name。

[参数 P-a340f179234f1a84](../../evidence/parameters-sets-012.md#p-a340f179234f1a84) · [状态效果 S-4241856e6152f286](../../evidence/state_effects-sets-014.md#s-4241856e6152f286)

### observed_connections-006670

```text
(config-router)# default auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346E6560 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6fcaf0b75cedef3a](../../evidence/conditions-sets-043.md#c-6fcaf0b75cedef3a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006700

```text
(config-router)# default bfd all-interfaces <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346E16E0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-e2d253c9caf08b7a](../../evidence/state_effects-sets-048.md#s-e2d253c9caf08b7a)

### observed_connections-006712

```text
(config-router)# default default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346E3518 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9f9f96d95be184d5](../../evidence/conditions-sets-062.md#c-9f9f96d95be184d5) · [状态效果 S-802a4f7805f99532](../../evidence/state_effects-sets-027.md#s-802a4f7805f99532)

### observed_connections-006665

```text
(config-router)# default default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346E28E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1d08f2ad8f50ad8b](../../evidence/conditions-sets-011.md#c-1d08f2ad8f50ad8b) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006746

```text
(config-router)# default distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346E5E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-c278206191fe15ea](../../evidence/conditions-sets-075.md#c-c278206191fe15ea) · [参数 P-54e8f0c3a4e14b76](../../evidence/parameters-sets-007.md#p-54e8f0c3a4e14b76) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006714

```text
(config-router)# default distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346E61D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-834ea57f3f93683a](../../evidence/conditions-sets-051.md#c-834ea57f3f93683a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006706

```text
(config-router)# default distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346E0680 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-678b38e178ff0265](../../evidence/conditions-sets-040.md#c-678b38e178ff0265) · [状态效果 S-7b49506b41bcdef4](../../evidence/state_effects-sets-026.md#s-7b49506b41bcdef4)

### observed_connections-006722

```text
(config-router)# default eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x346E95C0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27fac1e71a6f94b0](../../evidence/conditions-sets-016.md#c-27fac1e71a6f94b0) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006742

```text
(config-router)# default eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x346E9AA0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-8428598050247ff8](../../evidence/conditions-sets-051.md#c-8428598050247ff8) · [参数 P-c4025b794cb514e7](../../evidence/parameters-sets-015.md#p-c4025b794cb514e7) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006689

```text
(config-router)# default event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346E91E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bf20b85c51008815](../../evidence/conditions-sets-074.md#c-bf20b85c51008815) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006685

```text
(config-router)# default event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346E8EA8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006677

```text
(config-router)# default kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x346E8150 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006686

```text
(config-router)# default log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346E8AC0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f4fd2d4f2302d0e](../../evidence/conditions-sets-019.md#c-2f4fd2d4f2302d0e) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006680

```text
(config-router)# default log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x346E8430 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006683

```text
(config-router)# default log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x346E8770 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1806440a77c3de5](../../evidence/conditions-sets-093.md#c-f1806440a77c3de5) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006660

```text
(config-router)# default maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x346E2240 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be3c5eece85cca69](../../evidence/conditions-sets-073.md#c-be3c5eece85cca69) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006659

```text
(config-router)# default maximum-secondary-paths <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x346E1EE8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-07b7110f17e5fc9c](../../evidence/conditions-sets-003.md#c-07b7110f17e5fc9c) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006698

```text
(config-router)# default metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346E0E28 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-566168da4fd292fa](../../evidence/conditions-sets-034.md#c-566168da4fd292fa) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006702

```text
(config-router)# default metric weights <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x346E1150 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6357873a21923fd2](../../evidence/conditions-sets-038.md#c-6357873a21923fd2) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006719

```text
(config-router)# default neighbor maximum-prefix <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346E69D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3cee576b96530915](../../evidence/conditions-sets-024.md#c-3cee576b96530915) · [状态效果 S-35c626f277f38f34](../../evidence/state_effects-sets-012.md#s-35c626f277f38f34)

### observed_connections-006707

```text
(config-router)# default network <address> <cr>
```

Handler ` RVA 0xF5DEBE0 `；selector ` 22 `；EOL ` RVA 0x346E39B0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Network number。

[条件 C-4ed971eba7375e9a](../../evidence/conditions-sets-031.md#c-4ed971eba7375e9a) · [参数 P-409dabef36da1baa](../../evidence/parameters-sets-005.md#p-409dabef36da1baa) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006654

```text
(config-router)# default nsf <cr>
```

Handler ` RVA 0xDB16C50 `；selector ` 7 `；EOL ` RVA 0x33FCD810 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e98ed7f30e87844](../../evidence/conditions-sets-061.md#c-9e98ed7f30e87844) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006739

```text
(config-router)# default offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346E57E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-d77d792620639cbd](../../evidence/conditions-sets-083.md#c-d77d792620639cbd) · [参数 P-1fd1e891d39ebbb8](../../evidence/parameters-sets-003.md#p-1fd1e891d39ebbb8) · [状态效果 S-041ee731d602d5f7](../../evidence/state_effects-sets-001.md#s-041ee731d602d5f7)

### observed_connections-006716

```text
(config-router)# default passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346E73A0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-57d5bf756c26bfb8](../../evidence/conditions-sets-034.md#c-57d5bf756c26bfb8) · [状态效果 S-c33e5a8c57a635b9](../../evidence/state_effects-sets-041.md#s-c33e5a8c57a635b9)

### observed_connections-006709

```text
(config-router)# default redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346E3D60 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70b2b7c969fd61e1](../../evidence/conditions-sets-044.md#c-70b2b7c969fd61e1) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006675

```text
(config-router)# default router-id <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x346E7790 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a51b8d5d5da8f046](../../evidence/conditions-sets-064.md#c-a51b8d5d5da8f046) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006690

```text
(config-router)# default shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x346E9DD8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006679

```text
(config-router)# default stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x346E7AD8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-544419271d519f80](../../evidence/conditions-sets-033.md#c-544419271d519f80) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006735

```text
(config-router)# default summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346E2E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-07f3d49374be7cbf](../../evidence/conditions-sets-003.md#c-07f3d49374be7cbf) · [参数 P-e2c6c9c3692fedf9](../../evidence/parameters-sets-017.md#p-e2c6c9c3692fedf9) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006694

```text
(config-router)# default timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346DF920 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a4359771d2373115](../../evidence/conditions-sets-063.md#c-a4359771d2373115) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006733

```text
(config-router)# default timers nsf converge <cr>
```

Handler ` RVA 0xDB171D0 `；selector ` 9 `；EOL ` RVA 0x33FCDF20 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-58305b406546624a](../../evidence/conditions-sets-035.md#c-58305b406546624a) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006726

```text
(config-router)# default timers nsf route-hold <cr>
```

Handler ` RVA 0xF57F070 `；selector ` 11 `；EOL ` RVA 0x346DFD00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c92bbd7050669702](../../evidence/conditions-sets-077.md#c-c92bbd7050669702) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006730

```text
(config-router)# default timers nsf signal <cr>
```

Handler ` RVA 0xDB16EC0 `；selector ` 8 `；EOL ` RVA 0x33FCDBF8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-abc51d127ba6eb2c](../../evidence/conditions-sets-066.md#c-abc51d127ba6eb2c) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006703

```text
(config-router)# default traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x346E1AF8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ed3aa13f1beaf3fa](../../evidence/state_effects-sets-050.md#s-ed3aa13f1beaf3fa)

### observed_connections-006663

```text
(config-router)# default variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x346E2590 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1209df034ff17c4](../../evidence/conditions-sets-062.md#c-a1209df034ff17c4) · [状态效果 S-9c9720556bc3536c](../../evidence/state_effects-sets-033.md#s-9c9720556bc3536c)

### observed_connections-006669

```text
(config-router)# default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346E3518 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f9f96d95be184d5](../../evidence/conditions-sets-062.md#c-9f9f96d95be184d5) · [状态效果 S-574c38c0dbf372f2](../../evidence/state_effects-sets-019.md#s-574c38c0dbf372f2)

### observed_connections-006747

```text
(config-router)# default-metric <number:1..4294967295> <number:0..4294967295> <number:0..255> <number:1..255> <number:1..65535> <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346E28E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in Kbits per second；` unsigned_number ` delay metric in 10 microsecond units；` unsigned_number ` Reliability metric where 255 is 100% reliable；` unsigned_number ` Effective bandwidth metric (Loading) where 255 is 100% loaded；` unsigned_number ` Maximum Transmission Unit metric of the path 。

[条件 C-70fab7ca86f81e80](../../evidence/conditions-sets-044.md#c-70fab7ca86f81e80) · [参数 P-bb374230dd761ca3](../../evidence/parameters-sets-014.md#p-bb374230dd761ca3)

### observed_connections-006740

```text
(config-router)# distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346E5E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-f9c6a59a48bc852e](../../evidence/conditions-sets-096.md#c-f9c6a59a48bc852e) · [参数 P-54e8f0c3a4e14b76](../../evidence/parameters-sets-007.md#p-54e8f0c3a4e14b76)

### observed_connections-006738

```text
(config-router)# distance eigrp <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346E61D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Distance for internal routes；` unsigned_number ` Distance for external routes。

[条件 C-99b9f01c269208f9](../../evidence/conditions-sets-059.md#c-99b9f01c269208f9) · [参数 P-2dd10a9a21a63008](../../evidence/parameters-sets-004.md#p-2dd10a9a21a63008)

### observed_connections-006666

```text
(config-router)# distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346E0680 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-678b38e178ff0265](../../evidence/conditions-sets-040.md#c-678b38e178ff0265) · [状态效果 S-dce958623471906f](../../evidence/state_effects-sets-047.md#s-dce958623471906f)

### observed_connections-006756

```text
(config-router)# distribute-list out <?router_action_proc_vpn@555589c34608> <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346E0680 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a8721e5e76479f94](../../evidence/conditions-sets-065.md#c-a8721e5e76479f94) · [缺口 G-1219eb9cc38b8663](../../evidence/gaps-sets-001.md#g-1219eb9cc38b8663) · [状态效果 S-1fd19fc38c3a79bc](../../evidence/state_effects-sets-007.md#s-1fd19fc38c3a79bc)

### observed_connections-006691

```text
(config-router)# eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x346E95C0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e5de8f587a32201](../../evidence/conditions-sets-037.md#c-5e5de8f587a32201)

### observed_connections-006723

```text
(config-router)# eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x346E9AA0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-8428598050247ff8](../../evidence/conditions-sets-051.md#c-8428598050247ff8) · [参数 P-c4025b794cb514e7](../../evidence/parameters-sets-015.md#p-c4025b794cb514e7)

### observed_connections-006754

```text
(config-router)# event-log-size <number:dynamic> <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346E91E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Max event log entries。

[条件 C-9e2f3184ab1edeaf](../../evidence/conditions-sets-061.md#c-9e2f3184ab1edeaf) · [缺口 G-50f7c05b665e8151](../../evidence/gaps-sets-003.md#g-50f7c05b665e8151) · [参数 P-642cd9975fbbdf05](../../evidence/parameters-sets-008.md#p-642cd9975fbbdf05)

### observed_connections-006648

```text
(config-router)# event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346E8EA8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a)

### observed_connections-006643

```text
(config-router)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x34696B28 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-519bc9c377ff2421](../../evidence/conditions-sets-032.md#c-519bc9c377ff2421)

### observed_connections-006646

```text
(config-router)# kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x346E8150 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a)

### observed_connections-006651

```text
(config-router)# log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346E8AC0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-140bd972eeb94647](../../evidence/conditions-sets-008.md#c-140bd972eeb94647)

### observed_connections-006647

```text
(config-router)# log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x346E8430 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a)

### observed_connections-006649

```text
(config-router)# log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x346E8770 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3d09170249b205a](../../evidence/conditions-sets-070.md#c-b3d09170249b205a)

### observed_connections-006750

```text
(config-router)# maximum-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x346E2240 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-ca76362c4e6a7718](../../evidence/conditions-sets-078.md#c-ca76362c4e6a7718) · [缺口 G-142c56a5cf6af3ae](../../evidence/gaps-sets-001.md#g-142c56a5cf6af3ae) · [参数 P-4d91f4d9bb751365](../../evidence/parameters-sets-006.md#p-4d91f4d9bb751365)

### observed_connections-006749

```text
(config-router)# maximum-secondary-paths <number:dynamic> <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x346E1EE8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of paths。

[条件 C-6d3fdbcf99af9e91](../../evidence/conditions-sets-042.md#c-6d3fdbcf99af9e91) · [缺口 G-1b18924e9a4699da](../../evidence/gaps-sets-001.md#g-1b18924e9a4699da) · [参数 P-789156578a6e2b70](../../evidence/parameters-sets-009.md#p-789156578a6e2b70)

### observed_connections-006696

```text
(config-router)# metric maximum-hops <number:1..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346E0E28 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-3128620c9ede5408](../../evidence/conditions-sets-019.md#c-3128620c9ede5408) · [参数 P-01906284d8e09007](../../evidence/parameters-sets-001.md#p-01906284d8e09007)

### observed_connections-006748

```text
(config-router)# metric weights <number:0..8> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x346E1150 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type (Only TOS 0 supported)；` unsigned_number ` K1；` unsigned_number ` K2；` unsigned_number ` K3；` unsigned_number ` K4；` unsigned_number ` K5。

[条件 C-a0532162d1984582](../../evidence/conditions-sets-062.md#c-a0532162d1984582) · [参数 P-afedfc050efe03b3](../../evidence/parameters-sets-013.md#p-afedfc050efe03b3)

### observed_connections-006757

```text
(config-router)# neighbor <address> <interface> <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346E69D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Neighbor address。

[条件 C-667fbd189c6f4b1a](../../evidence/conditions-sets-040.md#c-667fbd189c6f4b1a) · [缺口 G-67337e7b2bbcc277](../../evidence/gaps-sets-004.md#g-67337e7b2bbcc277) · [参数 P-84a8c7f939559b71](../../evidence/parameters-sets-010.md#p-84a8c7f939559b71) · [状态效果 S-11374a1e20186e4f](../../evidence/state_effects-sets-004.md#s-11374a1e20186e4f)

### observed_connections-006720

```text
(config-router)# neighbor maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346E69D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of prefixs for maximum-prefix limit。

[条件 C-467112c1c9f5fa27](../../evidence/conditions-sets-028.md#c-467112c1c9f5fa27) · [参数 P-c9188b3fad428fea](../../evidence/parameters-sets-015.md#p-c9188b3fad428fea) · [状态效果 S-2c5576e909364697](../../evidence/state_effects-sets-010.md#s-2c5576e909364697)

### observed_connections-006667

```text
(config-router)# network <address> <cr>
```

Handler ` RVA 0xF5DEBE0 `；selector ` 22 `；EOL ` RVA 0x346E39B0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network number。

[条件 C-4ed971eba7375e9a](../../evidence/conditions-sets-031.md#c-4ed971eba7375e9a) · [参数 P-409dabef36da1baa](../../evidence/parameters-sets-005.md#p-409dabef36da1baa)

### observed_connections-006743

```text
(config-router)# no address-family ipv4 vrf <string> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 119 `；EOL ` RVA 0x346E0228 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Virtual Routing/Forwarding instance name。

[参数 P-a340f179234f1a84](../../evidence/parameters-sets-012.md#p-a340f179234f1a84) · [状态效果 S-58bfc7beb97a59e2](../../evidence/state_effects-sets-019.md#s-58bfc7beb97a59e2)

### observed_connections-006668

```text
(config-router)# no auto-summary <cr>
```

Handler ` RVA 0xF575B20 `；selector ` 42 `；EOL ` RVA 0x346E6560 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6fcaf0b75cedef3a](../../evidence/conditions-sets-043.md#c-6fcaf0b75cedef3a) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006697

```text
(config-router)# no bfd all-interfaces <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x346E16E0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-82c55e4ad4f36b48](../../evidence/state_effects-sets-028.md#s-82c55e4ad4f36b48)

### observed_connections-006711

```text
(config-router)# no default-information in <cr>
```

Handler ` RVA 0xF5DB530 `；selector ` 48 `；EOL ` RVA 0x346E3518 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9f9f96d95be184d5](../../evidence/conditions-sets-062.md#c-9f9f96d95be184d5) · [状态效果 S-b3c479491306ac42](../../evidence/state_effects-sets-038.md#s-b3c479491306ac42)

### observed_connections-006664

```text
(config-router)# no default-metric <cr>
```

Handler ` RVA 0xF5756A0 `；selector ` 45 `；EOL ` RVA 0x346E28E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f410474d1fea607c](../../evidence/conditions-sets-094.md#c-f410474d1fea607c) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006745

```text
(config-router)# no distance <number:1..255> <address> <address> <cr>
```

Handler ` RVA 0xF596F40 `；selector ` 46 `；EOL ` RVA 0x346E5E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Set route administrative distance；` address ` IP Source address；` address ` Wildcard bits。

[条件 C-7e0e8005101c1262](../../evidence/conditions-sets-049.md#c-7e0e8005101c1262) · [参数 P-54e8f0c3a4e14b76](../../evidence/parameters-sets-007.md#p-54e8f0c3a4e14b76) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006713

```text
(config-router)# no distance eigrp <cr>
```

Handler ` RVA 0xF597490 `；selector ` 47 `；EOL ` RVA 0x346E61D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75773e5385d5718f](../../evidence/conditions-sets-046.md#c-75773e5385d5718f) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006704

```text
(config-router)# no distribute-list in <cr>
```

Handler ` RVA 0xF5DBC30 `；selector ` 29 `；EOL ` RVA 0x346E0680 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-678b38e178ff0265](../../evidence/conditions-sets-040.md#c-678b38e178ff0265) · [状态效果 S-2b0599909ab9f801](../../evidence/state_effects-sets-010.md#s-2b0599909ab9f801)

### observed_connections-006721

```text
(config-router)# no eigrp graceful-restart <cr>
```

Handler ` RVA 0xF57EE00 `；selector ` 10 `；EOL ` RVA 0x346E95C0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-db5f93199a00c6aa](../../evidence/conditions-sets-084.md#c-db5f93199a00c6aa) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006741

```text
(config-router)# no eigrp upgrade-cli <string> <cr>
```

Handler ` RVA 0xF5807E0 `；selector ` 142 `；EOL ` RVA 0x346E9AA0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` EIGRP Virtual-Instance Name。

[条件 C-8428598050247ff8](../../evidence/conditions-sets-051.md#c-8428598050247ff8) · [参数 P-c4025b794cb514e7](../../evidence/parameters-sets-015.md#p-c4025b794cb514e7) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006687

```text
(config-router)# no event-log-size <cr>
```

Handler ` RVA 0xF596700 `；selector ` 35 `；EOL ` RVA 0x346E91E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-53749707c7d53f2f](../../evidence/conditions-sets-033.md#c-53749707c7d53f2f) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006682

```text
(config-router)# no event-logging <cr>
```

Handler ` RVA 0xF596700 `；selector ` 36 `；EOL ` RVA 0x346E8EA8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006674

```text
(config-router)# no kill-everyone <cr>
```

Handler ` RVA 0xF57B0C0 `；selector ` 15 `；EOL ` RVA 0x346E8150 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006684

```text
(config-router)# no log-event-type <cr>
```

Handler ` RVA 0xF596700 `；selector ` 34 `；EOL ` RVA 0x346E8AC0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1480a953f2bbd72e](../../evidence/conditions-sets-008.md#c-1480a953f2bbd72e) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006678

```text
(config-router)# no log-neighbor-changes <cr>
```

Handler ` RVA 0xF57B3F0 `；selector ` 16 `；EOL ` RVA 0x346E8430 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006681

```text
(config-router)# no log-neighbor-warnings <cr>
```

Handler ` RVA 0xF57B570 `；selector ` 17 `；EOL ` RVA 0x346E8770 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-22d3ae01700820f5](../../evidence/conditions-sets-014.md#c-22d3ae01700820f5) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006658

```text
(config-router)# no maximum-paths <cr>
```

Handler ` RVA 0xF5985F0 `；selector ` 37 `；EOL ` RVA 0x346E2240 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f8398012b980acf7](../../evidence/conditions-sets-096.md#c-f8398012b980acf7) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006657

```text
(config-router)# no maximum-secondary-paths <cr>
```

Handler ` RVA 0xF5987B0 `；selector ` 38 `；EOL ` RVA 0x346E1EE8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-305c5b8093245792](../../evidence/conditions-sets-019.md#c-305c5b8093245792) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006695

```text
(config-router)# no metric maximum-hops <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 31 `；EOL ` RVA 0x346E0E28 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6107aa88d879197b](../../evidence/conditions-sets-038.md#c-6107aa88d879197b) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006699

```text
(config-router)# no metric weights <cr>
```

Handler ` RVA 0xF57D6C0 `；selector ` 12 `；EOL ` RVA 0x346E1150 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e3c71b72acf02db9](../../evidence/conditions-sets-088.md#c-e3c71b72acf02db9) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006717

```text
(config-router)# no neighbor maximum-prefix <cr>
```

Handler ` RVA 0xF57C0C0 `；selector ` 4 `；EOL ` RVA 0x346E69D0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-55dfa9010cc3103a](../../evidence/conditions-sets-034.md#c-55dfa9010cc3103a) · [状态效果 S-b6c4d3369769013e](../../evidence/state_effects-sets-039.md#s-b6c4d3369769013e)

### observed_connections-006705

```text
(config-router)# no network <address> <cr>
```

Handler ` RVA 0xF5DEBE0 `；selector ` 22 `；EOL ` RVA 0x346E39B0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Network number。

[条件 C-4ed971eba7375e9a](../../evidence/conditions-sets-031.md#c-4ed971eba7375e9a) · [参数 P-409dabef36da1baa](../../evidence/parameters-sets-005.md#p-409dabef36da1baa) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006653

```text
(config-router)# no nsf <cr>
```

Handler ` RVA 0xDB16C50 `；selector ` 7 `；EOL ` RVA 0x33FCD810 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ebb493205511d74b](../../evidence/conditions-sets-091.md#c-ebb493205511d74b) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006737

```text
(config-router)# no offset-list <number:0..99> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346E57E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)。

[条件 C-d77d792620639cbd](../../evidence/conditions-sets-083.md#c-d77d792620639cbd) · [参数 P-1fd1e891d39ebbb8](../../evidence/parameters-sets-003.md#p-1fd1e891d39ebbb8) · [状态效果 S-4e8d732aa441faaf](../../evidence/state_effects-sets-017.md#s-4e8d732aa441faaf)

### observed_connections-006715

```text
(config-router)# no passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346E73A0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-57d5bf756c26bfb8](../../evidence/conditions-sets-034.md#c-57d5bf756c26bfb8) · [状态效果 S-a71b273d42d9860d](../../evidence/state_effects-sets-035.md#s-a71b273d42d9860d)

### observed_connections-006708

```text
(config-router)# no redistribute maximum-prefix <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346E3D60 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb0c2813054b2022](../../evidence/conditions-sets-097.md#c-fb0c2813054b2022) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006671

```text
(config-router)# no router-id <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x346E7790 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-699f7e921546502f](../../evidence/conditions-sets-041.md#c-699f7e921546502f) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006688

```text
(config-router)# no shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x346E9DD8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006676

```text
(config-router)# no stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x346E7AD8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0007c7bba1fde82c](../../evidence/conditions-sets-001.md#c-0007c7bba1fde82c) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006734

```text
(config-router)# no summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346E2E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-5f32fad2178fba9c](../../evidence/conditions-sets-037.md#c-5f32fad2178fba9c) · [参数 P-e2c6c9c3692fedf9](../../evidence/parameters-sets-017.md#p-e2c6c9c3692fedf9) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006692

```text
(config-router)# no timers active-time <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346DF920 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6011885f94afc2c6](../../evidence/conditions-sets-037.md#c-6011885f94afc2c6) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006731

```text
(config-router)# no timers nsf converge <cr>
```

Handler ` RVA 0xDB171D0 `；selector ` 9 `；EOL ` RVA 0x33FCDF20 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5b0ed19d6abf7a5e](../../evidence/conditions-sets-036.md#c-5b0ed19d6abf7a5e) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006724

```text
(config-router)# no timers nsf route-hold <cr>
```

Handler ` RVA 0xF57F070 `；selector ` 11 `；EOL ` RVA 0x346DFD00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-46d5b758d86b226f](../../evidence/conditions-sets-028.md#c-46d5b758d86b226f) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006728

```text
(config-router)# no timers nsf signal <cr>
```

Handler ` RVA 0xDB16EC0 `；selector ` 8 `；EOL ` RVA 0x33FCDBF8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88ccafae0f02a838](../../evidence/conditions-sets-053.md#c-88ccafae0f02a838) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006701

```text
(config-router)# no traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x346E1AF8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d65db6886d6814c8](../../evidence/state_effects-sets-045.md#s-d65db6886d6814c8)

### observed_connections-006661

```text
(config-router)# no variance <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x346E2590 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-10a7afb1c4998c45](../../evidence/conditions-sets-007.md#c-10a7afb1c4998c45) · [状态效果 S-fb5bfe2df8b7e65b](../../evidence/state_effects-sets-053.md#s-fb5bfe2df8b7e65b)

### observed_connections-006644

```text
(config-router)# nsf <cr>
```

Handler ` RVA 0xDB16C50 `；selector ` 7 `；EOL ` RVA 0x33FCD810 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f7281957fe3bcc7](../../evidence/conditions-sets-012.md#c-1f7281957fe3bcc7)

### observed_connections-006736

```text
(config-router)# offset-list <number:0..99> in <number:0..2147483647> <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346E57E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list of networks to apply offset (0 selects all networks)；` unsigned_number ` Offset。

[条件 C-ad005c17b5f8c989](../../evidence/conditions-sets-067.md#c-ad005c17b5f8c989) · [参数 P-846111d0caa5363c](../../evidence/parameters-sets-010.md#p-846111d0caa5363c) · [状态效果 S-882b6f1675169414](../../evidence/state_effects-sets-029.md#s-882b6f1675169414)

### observed_connections-006758

```text
(config-router)# offset-list <string> in <cr>
```

Handler ` RVA 0xF597D70 `；selector ` 30 `；EOL ` RVA 0x346E57E8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Access-list name。

[条件 C-f5b6f5db99e5aa4f](../../evidence/conditions-sets-095.md#c-f5b6f5db99e5aa4f) · [缺口 G-31933b66b42efb72](../../evidence/gaps-sets-002.md#g-31933b66b42efb72) · [参数 P-a4a8bae904301d1b](../../evidence/parameters-sets-013.md#p-a4a8bae904301d1b) · [状态效果 S-b10be14f69b7ab2c](../../evidence/state_effects-sets-038.md#s-b10be14f69b7ab2c)

### observed_connections-006752

```text
(config-router)# passive-interface <interface> <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346E73A0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6979e830930f3331](../../evidence/conditions-sets-041.md#c-6979e830930f3331) · [缺口 G-6d1390e154e78fd4](../../evidence/gaps-sets-004.md#g-6d1390e154e78fd4) · [参数 P-f4ef801665eb6a8e](../../evidence/parameters-sets-018.md#p-f4ef801665eb6a8e)

### observed_connections-006673

```text
(config-router)# passive-interface default <cr>
```

Handler ` RVA 0xF58B500 `；selector ` 132 `；EOL ` RVA 0x346E73A0 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57d5bf756c26bfb8](../../evidence/conditions-sets-034.md#c-57d5bf756c26bfb8) · [状态效果 S-5a4f6aaad639b6c4](../../evidence/state_effects-sets-019.md#s-5a4f6aaad639b6c4)

### observed_connections-006753

```text
(config-router)# redistribute <?router_action_no_proc_vpn@555589c383a8> <cr>
```

Handler ` RVA 0xF5DE550 `；selector ` 32 `；EOL ` RVA 0x346E51F8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0ea046db25de9434](../../evidence/conditions-sets-006.md#c-0ea046db25de9434) · [缺口 G-ba3d506c217d2510](../../evidence/gaps-sets-007.md#g-ba3d506c217d2510)

### observed_connections-006718

```text
(config-router)# redistribute maximum-prefix <number:1..4294967295> <cr>
```

Handler ` RVA 0xF598EF0 `；selector ` 33 `；EOL ` RVA 0x346E3D60 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of IP prefixes redistributed。

[条件 C-f3ec681d04fbd234](../../evidence/conditions-sets-094.md#c-f3ec681d04fbd234) · [参数 P-009cce5d77b7c574](../../evidence/parameters-sets-001.md#p-009cce5d77b7c574)

### observed_connections-006672

```text
(config-router)# router-id <address> <cr>
```

Handler ` RVA 0xF57EB20 `；selector ` 5 `；EOL ` RVA 0x346E7790 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` EIGRP Router-ID in IP address format。

[条件 C-8329b9e63b8dafc4](../../evidence/conditions-sets-051.md#c-8329b9e63b8dafc4) · [参数 P-234bbd93d348959a](../../evidence/parameters-sets-003.md#p-234bbd93d348959a)

### observed_connections-006650

```text
(config-router)# shutdown <cr>
```

Handler ` RVA 0xF57D580 `；selector ` 6 `；EOL ` RVA 0x346E9DD8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89195b1357e9942a](../../evidence/conditions-sets-053.md#c-89195b1357e9942a)

### observed_connections-006652

```text
(config-router)# stub <cr>
```

Handler ` RVA 0xF57E6E0 `；selector ` 18 `；EOL ` RVA 0x346E7AD8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a3dbe9e8add4df57](../../evidence/conditions-sets-063.md#c-a3dbe9e8add4df57)

### observed_connections-006710

```text
(config-router)# summary-metric <address> <address> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346E2E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Summary to configure static metric；` address ` Network mask。

[条件 C-d5b19d3ef8370a29](../../evidence/conditions-sets-082.md#c-d5b19d3ef8370a29) · [参数 P-e2c6c9c3692fedf9](../../evidence/parameters-sets-017.md#p-e2c6c9c3692fedf9)

### observed_connections-006751

```text
(config-router)# summary-metric <prefix:dynamic> <cr>
```

Handler ` RVA 0xF599350 `；selector ` 41 `；EOL ` RVA 0x346E2E00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-26194ae4a5c01242](../../evidence/conditions-sets-015.md#c-26194ae4a5c01242) · [缺口 G-a7e89fb49d9890de](../../evidence/gaps-sets-006.md#g-a7e89fb49d9890de) · [参数 P-3ecca0a31dbe36e1](../../evidence/parameters-sets-005.md#p-3ecca0a31dbe36e1) · [状态效果 S-7535b544da2459e4](../../evidence/state_effects-sets-025.md#s-7535b544da2459e4)

### observed_connections-006693

```text
(config-router)# timers active-time disabled <cr>
```

Handler ` RVA 0xF597780 `；selector ` 28 `；EOL ` RVA 0x346DF920 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad0af78c755999e4](../../evidence/conditions-sets-067.md#c-ad0af78c755999e4)

### observed_connections-006732

```text
(config-router)# timers nsf converge <number:60..180> <cr>
```

Handler ` RVA 0xDB171D0 `；selector ` 9 `；EOL ` RVA 0x33FCDF20 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-7ffc079031c2d581](../../evidence/conditions-sets-050.md#c-7ffc079031c2d581) · [参数 P-9b5a8fb4a495e6ef](../../evidence/parameters-sets-012.md#p-9b5a8fb4a495e6ef)

### observed_connections-006725

```text
(config-router)# timers nsf route-hold <number:20..300> <cr>
```

Handler ` RVA 0xF57F070 `；selector ` 11 `；EOL ` RVA 0x346DFD00 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-efe5ed4defcb77b8](../../evidence/conditions-sets-093.md#c-efe5ed4defcb77b8) · [参数 P-fe8def5e7526b947](../../evidence/parameters-sets-019.md#p-fe8def5e7526b947)

### observed_connections-006729

```text
(config-router)# timers nsf signal <number:10..30> <cr>
```

Handler ` RVA 0xDB16EC0 `；selector ` 8 `；EOL ` RVA 0x33FCDBF8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-6afcad8b24851671](../../evidence/conditions-sets-041.md#c-6afcad8b24851671) · [参数 P-25430a659809aae2](../../evidence/parameters-sets-003.md#p-25430a659809aae2)

### observed_connections-006656

```text
(config-router)# traffic-share balanced <cr>
```

Handler ` RVA 0xF575880 `；selector ` 40 `；EOL ` RVA 0x346E1AF8 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-2edbc7c71718f79e](../../evidence/state_effects-sets-010.md#s-2edbc7c71718f79e)

### observed_connections-006662

```text
(config-router)# variance <number:1..128> <cr>
```

Handler ` RVA 0xF575390 `；selector ` 39 `；EOL ` RVA 0x346E2590 `。

模式根 ` RVA 0x34696920 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Metric variance multiplier。

[条件 C-32f3520bff0bcd8d](../../evidence/conditions-sets-020.md#c-32f3520bff0bcd8d) · [参数 P-5a91a60637246b0d](../../evidence/parameters-sets-007.md#p-5a91a60637246b0d)

