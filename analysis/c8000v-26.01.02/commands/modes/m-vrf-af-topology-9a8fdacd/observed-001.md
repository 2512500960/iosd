# vrf-af-topology · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007525

```text
(config-vrf-af-topology)# all-interfaces <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 0 `；EOL ` RVA 0x33FDF080 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7417b2a6c03df361](../../evidence/conditions-sets-045.md#c-7417b2a6c03df361) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007539

```text
(config-vrf-af-topology)# bgp next-hop <cr>
```

Handler ` RVA 0xDC24530 `；selector ` 0 `；EOL ` RVA 0x34015B70 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5cb63fe35538429a](../../evidence/conditions-sets-036.md#c-5cb63fe35538429a) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007523

```text
(config-vrf-af-topology)# context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f84d853ea079da01](../../evidence/conditions-sets-096.md#c-f84d853ea079da01) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007535

```text
(config-vrf-af-topology)# default all-interfaces <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 0 `；EOL ` RVA 0x33FDF080 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7417b2a6c03df361](../../evidence/conditions-sets-045.md#c-7417b2a6c03df361) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007555

```text
(config-vrf-af-topology)# default bgp next-hop <cr>
```

Handler ` RVA 0xDC24530 `；selector ` 0 `；EOL ` RVA 0x34015B70 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2dc9cd38509cdc14](../../evidence/conditions-sets-018.md#c-2dc9cd38509cdc14) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007531

```text
(config-vrf-af-topology)# default context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada418e0516d363b](../../evidence/conditions-sets-067.md#c-ada418e0516d363b) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007529

```text
(config-vrf-af-topology)# default exit-topology <cr>
```

Handler ` RVA 0xDC44A80 `；selector ` 0 `；EOL ` RVA 0x34016578 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61649310d998c606](../../evidence/conditions-sets-038.md#c-61649310d998c606) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007565

```text
(config-vrf-af-topology)# default export map <string> <cr>
```

Handler ` RVA 0xF21DBB0 `；selector ` 0 `；EOL ` RVA 0x345D7E40 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF export route-map name。

[条件 C-d52ea24b11a5e529](../../evidence/conditions-sets-082.md#c-d52ea24b11a5e529) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-3b9944ac5689dcd9](../../evidence/parameters-sets-005.md#p-3b9944ac5689dcd9) · [状态效果 S-071fb4b594fee58e](../../evidence/state_effects-sets-002.md#s-071fb4b594fee58e)

### observed_connections-007533

```text
(config-vrf-af-topology)# default forward-base <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 1 `；EOL ` RVA 0x33FDED88 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fcf4f050a64b657e](../../evidence/conditions-sets-098.md#c-fcf4f050a64b657e) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007566

```text
(config-vrf-af-topology)# default import map <string> <cr>
```

Handler ` RVA 0xF21E930 `；selector ` 0 `；EOL ` RVA 0x345D76D8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF import route-map name。

[条件 C-fa1edee282630448](../../evidence/conditions-sets-097.md#c-fa1edee282630448) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-fbb4d64ba680570f](../../evidence/parameters-sets-019.md#p-fbb4d64ba680570f) · [状态效果 S-405b4ff338e2afad](../../evidence/state_effects-sets-014.md#s-405b4ff338e2afad)

### observed_connections-007543

```text
(config-vrf-af-topology)# default inter-as-hybrid <cr>
```

Handler ` RVA 0xDC28920 `；selector ` 0 `；EOL ` RVA 0x340155E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7dfd699890a22ec4](../../evidence/conditions-sets-049.md#c-7dfd699890a22ec4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007547

```text
(config-vrf-af-topology)# default maximum routes <cr>
```

Handler ` RVA 0xDC21C20 `；selector ` 0 `；EOL ` RVA 0x340150A8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14aec860ea5bac17](../../evidence/conditions-sets-008.md#c-14aec860ea5bac17) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007556

```text
(config-vrf-af-topology)# default maximum routes <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 2 `；EOL ` RVA 0x33FDF458 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-62ea830f7edc7c3f](../../evidence/conditions-sets-038.md#c-62ea830f7edc7c3f) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007559

```text
(config-vrf-af-topology)# default protection local-prefixes <cr>
```

Handler ` RVA 0xDC24DE0 `；selector ` 0 `；EOL ` RVA 0x34016278 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d60e511dbad85dc](../../evidence/conditions-sets-055.md#c-8d60e511dbad85dc) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007572

```text
(config-vrf-af-topology)# default route-replicate from unicast all <cr>
```

Handler ` RVA 0xDBECBC0 `；selector ` 0 `；EOL ` RVA 0x340087D0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98a0e3cac8c7eca6](../../evidence/conditions-sets-059.md#c-98a0e3cac8c7eca6) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-72b37d36ed0bce1f](../../evidence/state_effects-sets-024.md#s-72b37d36ed0bce1f)

### observed_connections-007561

```text
(config-vrf-af-topology)# default route-replicate recursion-policy destination <cr>
```

Handler ` RVA 0xDBF1CA0 `；selector ` 0 `；EOL ` RVA 0x34008D28 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b99d3d743fa27f0d](../../evidence/conditions-sets-072.md#c-b99d3d743fa27f0d) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-361ef2e1b10cedde](../../evidence/state_effects-sets-012.md#s-361ef2e1b10cedde)

### observed_connections-007568

```text
(config-vrf-af-topology)# default route-replicate-distance from unicast <cr>
```

Handler ` RVA 0xDBED720 `；selector ` 0 `；EOL ` RVA 0x34009360 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b8876c57d781c14](../../evidence/conditions-sets-060.md#c-9b8876c57d781c14) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-818f4326333dc8dd](../../evidence/state_effects-sets-027.md#s-818f4326333dc8dd)

### observed_connections-007542

```text
(config-vrf-af-topology)# default shutdown <cr>
```

Handler ` RVA 0xDB662D0 `；selector ` 0 `；EOL ` RVA 0x33FDF8E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f39c0832ea5b5cef](../../evidence/conditions-sets-094.md#c-f39c0832ea5b5cef) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007553

```text
(config-vrf-af-topology)# default snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-94bfe0943512f6e0](../../evidence/state_effects-sets-032.md#s-94bfe0943512f6e0)

### observed_connections-007578

```text
(config-vrf-af-topology)# default snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2573c969c66067b6](../../evidence/conditions-sets-015.md#c-2573c969c66067b6) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-1703ee4d1a715bb7](../../evidence/state_effects-sets-005.md#s-1703ee4d1a715bb7)

### observed_connections-007577

```text
(config-vrf-af-topology)# default snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-67e2e80e2c1c144d](../../evidence/conditions-sets-040.md#c-67e2e80e2c1c144d) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-e6dff938119bb0cd](../../evidence/state_effects-sets-049.md#s-e6dff938119bb0cd)

### observed_connections-007570

```text
(config-vrf-af-topology)# default use-topology unicast base <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 3 `；EOL ` RVA 0x33FDFC68 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6f7a3e8d5c7806a4](../../evidence/conditions-sets-043.md#c-6f7a3e8d5c7806a4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-ceed331f29b93bbc](../../evidence/state_effects-sets-044.md#s-ceed331f29b93bbc)

### observed_connections-007522

```text
(config-vrf-af-topology)# exit-topology <cr>
```

Handler ` RVA 0xDC44A80 `；selector ` 0 `；EOL ` RVA 0x34016578 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-61649310d998c606](../../evidence/conditions-sets-038.md#c-61649310d998c606) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007549

```text
(config-vrf-af-topology)# export map <string> <cr>
```

Handler ` RVA 0xF21DBB0 `；selector ` 0 `；EOL ` RVA 0x345D7E40 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF export route-map name。

[条件 C-d52ea24b11a5e529](../../evidence/conditions-sets-082.md#c-d52ea24b11a5e529) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-3b9944ac5689dcd9](../../evidence/parameters-sets-005.md#p-3b9944ac5689dcd9) · [状态效果 S-2faa773eb698a28d](../../evidence/state_effects-sets-011.md#s-2faa773eb698a28d)

### observed_connections-007524

```text
(config-vrf-af-topology)# forward-base <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 1 `；EOL ` RVA 0x33FDED88 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fcf4f050a64b657e](../../evidence/conditions-sets-098.md#c-fcf4f050a64b657e) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007550

```text
(config-vrf-af-topology)# import map <string> <cr>
```

Handler ` RVA 0xF21E930 `；selector ` 0 `；EOL ` RVA 0x345D76D8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF import route-map name。

[条件 C-fa1edee282630448](../../evidence/conditions-sets-097.md#c-fa1edee282630448) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-fbb4d64ba680570f](../../evidence/parameters-sets-019.md#p-fbb4d64ba680570f) · [状态效果 S-0a998af21429b11b](../../evidence/state_effects-sets-003.md#s-0a998af21429b11b)

### observed_connections-007527

```text
(config-vrf-af-topology)# inter-as-hybrid <cr>
```

Handler ` RVA 0xDC28920 `；selector ` 0 `；EOL ` RVA 0x340155E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7dfd699890a22ec4](../../evidence/conditions-sets-049.md#c-7dfd699890a22ec4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007536

```text
(config-vrf-af-topology)# maximum routes <cr>
```

Handler ` RVA 0xDC21C20 `；selector ` 0 `；EOL ` RVA 0x340150A8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-02271a4ccccf01df](../../evidence/conditions-sets-001.md#c-02271a4ccccf01df) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007541

```text
(config-vrf-af-topology)# maximum routes <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 2 `；EOL ` RVA 0x33FDF458 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c49573f64c052d25](../../evidence/conditions-sets-076.md#c-c49573f64c052d25) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007534

```text
(config-vrf-af-topology)# no all-interfaces <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 0 `；EOL ` RVA 0x33FDF080 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-7417b2a6c03df361](../../evidence/conditions-sets-045.md#c-7417b2a6c03df361) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007551

```text
(config-vrf-af-topology)# no bgp next-hop <cr>
```

Handler ` RVA 0xDC24530 `；selector ` 0 `；EOL ` RVA 0x34015B70 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-28a97ff350e24c66](../../evidence/conditions-sets-016.md#c-28a97ff350e24c66) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007530

```text
(config-vrf-af-topology)# no context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C44A60 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-d4212b9e9ec28c6e](../../evidence/conditions-sets-082.md#c-d4212b9e9ec28c6e) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007528

```text
(config-vrf-af-topology)# no exit-topology <cr>
```

Handler ` RVA 0xDC44A80 `；selector ` 0 `；EOL ` RVA 0x34016578 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-61649310d998c606](../../evidence/conditions-sets-038.md#c-61649310d998c606) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007562

```text
(config-vrf-af-topology)# no export map <string> <cr>
```

Handler ` RVA 0xF21DBB0 `；selector ` 0 `；EOL ` RVA 0x345D7E40 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` VRF export route-map name。

[条件 C-d52ea24b11a5e529](../../evidence/conditions-sets-082.md#c-d52ea24b11a5e529) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-3b9944ac5689dcd9](../../evidence/parameters-sets-005.md#p-3b9944ac5689dcd9) · [状态效果 S-f8fc79da915a91a6](../../evidence/state_effects-sets-053.md#s-f8fc79da915a91a6)

### observed_connections-007532

```text
(config-vrf-af-topology)# no forward-base <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 1 `；EOL ` RVA 0x33FDED88 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-fcf4f050a64b657e](../../evidence/conditions-sets-098.md#c-fcf4f050a64b657e) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007563

```text
(config-vrf-af-topology)# no import map <string> <cr>
```

Handler ` RVA 0xF21E930 `；selector ` 0 `；EOL ` RVA 0x345D76D8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` VRF import route-map name。

[条件 C-fa1edee282630448](../../evidence/conditions-sets-097.md#c-fa1edee282630448) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-fbb4d64ba680570f](../../evidence/parameters-sets-019.md#p-fbb4d64ba680570f) · [状态效果 S-15414d9e84242f34](../../evidence/state_effects-sets-005.md#s-15414d9e84242f34)

### observed_connections-007540

```text
(config-vrf-af-topology)# no inter-as-hybrid <cr>
```

Handler ` RVA 0xDC28920 `；selector ` 0 `；EOL ` RVA 0x340155E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-7dfd699890a22ec4](../../evidence/conditions-sets-049.md#c-7dfd699890a22ec4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007546

```text
(config-vrf-af-topology)# no maximum routes <cr>
```

Handler ` RVA 0xDC21C20 `；selector ` 0 `；EOL ` RVA 0x340150A8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-1d720e74394344b4](../../evidence/conditions-sets-011.md#c-1d720e74394344b4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007554

```text
(config-vrf-af-topology)# no maximum routes <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 2 `；EOL ` RVA 0x33FDF458 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-dd15b6e6c7b45e41](../../evidence/conditions-sets-085.md#c-dd15b6e6c7b45e41) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007558

```text
(config-vrf-af-topology)# no protection local-prefixes <cr>
```

Handler ` RVA 0xDC24DE0 `；selector ` 0 `；EOL ` RVA 0x34016278 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-050f7dfe46c8a465](../../evidence/conditions-sets-002.md#c-050f7dfe46c8a465) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007571

```text
(config-vrf-af-topology)# no route-replicate from unicast all <cr>
```

Handler ` RVA 0xDBECBC0 `；selector ` 0 `；EOL ` RVA 0x340087D0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-98a0e3cac8c7eca6](../../evidence/conditions-sets-059.md#c-98a0e3cac8c7eca6) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-b050f6e82d8d437b](../../evidence/state_effects-sets-037.md#s-b050f6e82d8d437b)

### observed_connections-007560

```text
(config-vrf-af-topology)# no route-replicate recursion-policy destination <cr>
```

Handler ` RVA 0xDBF1CA0 `；selector ` 0 `；EOL ` RVA 0x34008D28 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-b99d3d743fa27f0d](../../evidence/conditions-sets-072.md#c-b99d3d743fa27f0d) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-9a0d2a9b26c0394c](../../evidence/state_effects-sets-033.md#s-9a0d2a9b26c0394c)

### observed_connections-007564

```text
(config-vrf-af-topology)# no route-replicate-distance from unicast <cr>
```

Handler ` RVA 0xDBED720 `；selector ` 0 `；EOL ` RVA 0x34009360 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-801d5b18465bef19](../../evidence/conditions-sets-050.md#c-801d5b18465bef19) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-a9edf0174e3335f2](../../evidence/state_effects-sets-036.md#s-a9edf0174e3335f2)

### observed_connections-007538

```text
(config-vrf-af-topology)# no shutdown <cr>
```

Handler ` RVA 0xDB662D0 `；selector ` 0 `；EOL ` RVA 0x33FDF8E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-f39c0832ea5b5cef](../../evidence/conditions-sets-094.md#c-f39c0832ea5b5cef) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007548

```text
(config-vrf-af-topology)# no snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-37da96bf7f09169c](../../evidence/state_effects-sets-012.md#s-37da96bf7f09169c)

### observed_connections-007576

```text
(config-vrf-af-topology)# no snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-de2a98e84f720b41](../../evidence/conditions-sets-086.md#c-de2a98e84f720b41) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-d16ccf665890b6a4](../../evidence/state_effects-sets-044.md#s-d16ccf665890b6a4)

### observed_connections-007575

```text
(config-vrf-af-topology)# no snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-47be03f8e6c2b97f](../../evidence/conditions-sets-028.md#c-47be03f8e6c2b97f) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-381602351ac9332b](../../evidence/state_effects-sets-012.md#s-381602351ac9332b)

### observed_connections-007569

```text
(config-vrf-af-topology)# no use-topology unicast base <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 3 `；EOL ` RVA 0x33FDFC68 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,null,0] `。

[条件 C-6f7a3e8d5c7806a4](../../evidence/conditions-sets-043.md#c-6f7a3e8d5c7806a4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-1d667ec8ab2a1994](../../evidence/state_effects-sets-007.md#s-1d667ec8ab2a1994)

### observed_connections-007544

```text
(config-vrf-af-topology)# protection local-prefixes <cr>
```

Handler ` RVA 0xDC24DE0 `；selector ` 0 `；EOL ` RVA 0x34016278 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6beff91b2a1ae82e](../../evidence/conditions-sets-042.md#c-6beff91b2a1ae82e) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007567

```text
(config-vrf-af-topology)# route-replicate from unicast all <cr>
```

Handler ` RVA 0xDBECBC0 `；selector ` 0 `；EOL ` RVA 0x340087D0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98a0e3cac8c7eca6](../../evidence/conditions-sets-059.md#c-98a0e3cac8c7eca6) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-e27f4d2d3beb31a4](../../evidence/state_effects-sets-048.md#s-e27f4d2d3beb31a4)

### observed_connections-007545

```text
(config-vrf-af-topology)# route-replicate recursion-policy destination <cr>
```

Handler ` RVA 0xDBF1CA0 `；selector ` 0 `；EOL ` RVA 0x34008D28 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b99d3d743fa27f0d](../../evidence/conditions-sets-072.md#c-b99d3d743fa27f0d) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-b749aaf3c339ef01](../../evidence/state_effects-sets-039.md#s-b749aaf3c339ef01)

### observed_connections-007552

```text
(config-vrf-af-topology)# route-replicate-distance from unicast <cr>
```

Handler ` RVA 0xDBED720 `；selector ` 0 `；EOL ` RVA 0x34009360 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e6c708e1be294c23](../../evidence/conditions-sets-089.md#c-e6c708e1be294c23) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-7c50d5a1a7ca5846](../../evidence/state_effects-sets-026.md#s-7c50d5a1a7ca5846)

### observed_connections-007579

```text
(config-vrf-af-topology)# route-target <?bgp_extcomm_action@555589568bc0> <cr>
```

Handler ` RVA 0xDC21FB0 `；selector ` 0 `；EOL ` RVA 0x34014C50 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9a53e96d858d8adc](../../evidence/conditions-sets-060.md#c-9a53e96d858d8adc) · [缺口 G-e1b82b20114243eb](../../evidence/gaps-sets-008.md#g-e1b82b20114243eb) · [状态效果 S-581e7776137c7d8c](../../evidence/state_effects-sets-019.md#s-581e7776137c7d8c)

### observed_connections-007580

```text
(config-vrf-af-topology)# route-target <?bgp_extcomm_action@555589568bc0> stitching <cr>
```

Handler ` RVA 0xF1B7290 `；selector ` 0 `；EOL ` RVA 0x3451E0E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-51f45bcb37b79b12](../../evidence/conditions-sets-032.md#c-51f45bcb37b79b12) · [缺口 G-e1b82b20114243eb](../../evidence/gaps-sets-008.md#g-e1b82b20114243eb) · [状态效果 S-581e7776137c7d8c](../../evidence/state_effects-sets-019.md#s-581e7776137c7d8c)

### observed_connections-007526

```text
(config-vrf-af-topology)# shutdown <cr>
```

Handler ` RVA 0xDB662D0 `；selector ` 0 `；EOL ` RVA 0x33FDF8E8 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f39c0832ea5b5cef](../../evidence/conditions-sets-094.md#c-f39c0832ea5b5cef) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007537

```text
(config-vrf-af-topology)# snmp context <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 0 `；EOL ` RVA 0x33C455F0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7598dc8aeb3669dc](../../evidence/conditions-sets-046.md#c-7598dc8aeb3669dc) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-c6d3e90876fe25b2](../../evidence/state_effects-sets-042.md#s-c6d3e90876fe25b2)

### observed_connections-007574

```text
(config-vrf-af-topology)# snmp context <string> community <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 2 `；EOL ` RVA 0x33C45118 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Context Name；` string ` SNMP community string。

[条件 C-2b7b8f921c6a1bbf](../../evidence/conditions-sets-017.md#c-2b7b8f921c6a1bbf) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-9b6eb89831feec60](../../evidence/parameters-sets-012.md#p-9b6eb89831feec60) · [状态效果 S-91bae50d12652141](../../evidence/state_effects-sets-031.md#s-91bae50d12652141)

### observed_connections-007573

```text
(config-vrf-af-topology)# snmp context <string> user <string> <cr>
```

Handler ` RVA 0xCC8CD70 `；selector ` 23 `；EOL ` RVA 0x33C456D0 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Context Name；` string ` Name of the user。

[条件 C-c1c20b2240edac5d](../../evidence/conditions-sets-075.md#c-c1c20b2240edac5d) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [参数 P-cfc42ec8ad667e32](../../evidence/parameters-sets-016.md#p-cfc42ec8ad667e32) · [状态效果 S-17ace491bd8d171d](../../evidence/state_effects-sets-005.md#s-17ace491bd8d171d)

### observed_connections-007557

```text
(config-vrf-af-topology)# use-topology unicast base <cr>
```

Handler ` RVA 0xDB66530 `；selector ` 3 `；EOL ` RVA 0x33FDFC68 `。

模式根 ` RVA 0x34011C00 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6f7a3e8d5c7806a4](../../evidence/conditions-sets-043.md#c-6f7a3e8d5c7806a4) · [缺口 G-f16ecbc6c86e680e](../../evidence/gaps-sets-008.md#g-f16ecbc6c86e680e) · [状态效果 S-b81417b87dd348d0](../../evidence/state_effects-sets-039.md#s-b81417b87dd348d0)

