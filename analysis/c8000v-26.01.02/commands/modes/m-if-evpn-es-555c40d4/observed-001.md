# if-evpn-es · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009287

```text
(config-if-evpn-es)# default df-election preempt-time <cr>
```

Handler ` RVA 0x12524280 `；selector ` 0 `；EOL ` RVA 0x3588BE38 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a305cd2bfe1469e7](../../evidence/conditions-sets-063.md#c-a305cd2bfe1469e7) · [状态效果 S-6167a1e6861e5f2d](../../evidence/state_effects-sets-021.md#s-6167a1e6861e5f2d)

### observed_connections-009281

```text
(config-if-evpn-es)# default identifier <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588B3A8 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-da189f93626a6559](../../evidence/conditions-sets-084.md#c-da189f93626a6559) · [状态效果 S-a1465c041efb23b4](../../evidence/state_effects-sets-034.md#s-a1465c041efb23b4)

### observed_connections-009283

```text
(config-if-evpn-es)# default redundancy <cr>
```

Handler ` RVA 0x12523FC0 `；selector ` 0 `；EOL ` RVA 0x3588B9E0 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f08ff296f6a83e6c](../../evidence/conditions-sets-093.md#c-f08ff296f6a83e6c) · [状态效果 S-a1465c041efb23b4](../../evidence/state_effects-sets-034.md#s-a1465c041efb23b4)

### observed_connections-009279

```text
(config-if-evpn-es)# default system-mac <cr>
```

Handler ` RVA 0x12523560 `；selector ` 0 `；EOL ` RVA 0x3588B098 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-467b543a046f0972](../../evidence/conditions-sets-028.md#c-467b543a046f0972) · [状态效果 S-a1465c041efb23b4](../../evidence/state_effects-sets-034.md#s-a1465c041efb23b4)

### observed_connections-009286

```text
(config-if-evpn-es)# df-election preempt-time <number:1..3600> <cr>
```

Handler ` RVA 0x12524280 `；selector ` 0 `；EOL ` RVA 0x3588BE38 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of seconds to wait before advertising Ethernet Segment routes。

[条件 C-ffacc13fe07ad4ab](../../evidence/conditions-sets-099.md#c-ffacc13fe07ad4ab) · [参数 P-c9944c5eae02a360](../../evidence/parameters-sets-015.md#p-c9944c5eae02a360) · [状态效果 S-9376a7ed5c8b50a6](../../evidence/state_effects-sets-031.md#s-9376a7ed5c8b50a6)

### observed_connections-009276

```text
(config-if-evpn-es)# exit <cr>
```

Handler ` RVA 0x1251A950 `；selector ` 0 `；EOL ` RVA 0x3587C9D8 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-406c1bbdafc8c87d](../../evidence/conditions-sets-025.md#c-406c1bbdafc8c87d)

### observed_connections-009289

```text
(config-if-evpn-es)# identifier type 0 <number:0..255> <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588B3A8 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-77a5e9d278a59366](../../evidence/conditions-sets-047.md#c-77a5e9d278a59366) · [缺口 G-5e4ffdeb10ec54aa](../../evidence/gaps-sets-004.md#g-5e4ffdeb10ec54aa) · [参数 P-03d20fc75b23930f](../../evidence/parameters-sets-001.md#p-03d20fc75b23930f) · [状态效果 S-3b89a105f0b8e9f1](../../evidence/state_effects-sets-013.md#s-3b89a105f0b8e9f1)

### observed_connections-009288

```text
(config-if-evpn-es)# identifier type 3 system-mac <address> <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588B3A8 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-d72505348664b3c2](../../evidence/conditions-sets-083.md#c-d72505348664b3c2) · [参数 P-b88d07e8cc85ebf0](../../evidence/parameters-sets-014.md#p-b88d07e8cc85ebf0) · [状态效果 S-344afc5a2c68511f](../../evidence/state_effects-sets-012.md#s-344afc5a2c68511f)

### observed_connections-009285

```text
(config-if-evpn-es)# no df-election preempt-time <cr>
```

Handler ` RVA 0x12524280 `；selector ` 0 `；EOL ` RVA 0x3588BE38 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ea1c50edd219cb19](../../evidence/conditions-sets-090.md#c-ea1c50edd219cb19) · [状态效果 S-fc9f84b472dd57ce](../../evidence/state_effects-sets-054.md#s-fc9f84b472dd57ce)

### observed_connections-009280

```text
(config-if-evpn-es)# no identifier <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588B3A8 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1ea4babfb12b200f](../../evidence/conditions-sets-012.md#c-1ea4babfb12b200f) · [状态效果 S-20781b6b080d42b2](../../evidence/state_effects-sets-007.md#s-20781b6b080d42b2)

### observed_connections-009282

```text
(config-if-evpn-es)# no redundancy <cr>
```

Handler ` RVA 0x12523FC0 `；selector ` 0 `；EOL ` RVA 0x3588B9E0 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7b9442231201e322](../../evidence/conditions-sets-048.md#c-7b9442231201e322) · [状态效果 S-20781b6b080d42b2](../../evidence/state_effects-sets-007.md#s-20781b6b080d42b2)

### observed_connections-009277

```text
(config-if-evpn-es)# no system-mac <cr>
```

Handler ` RVA 0x12523560 `；selector ` 0 `；EOL ` RVA 0x3588B098 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-00ac42010316a454](../../evidence/conditions-sets-001.md#c-00ac42010316a454) · [状态效果 S-20781b6b080d42b2](../../evidence/state_effects-sets-007.md#s-20781b6b080d42b2)

### observed_connections-009284

```text
(config-if-evpn-es)# redundancy all-active <cr>
```

Handler ` RVA 0x12523FC0 `；selector ` 0 `；EOL ` RVA 0x3588B9E0 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8219fe2f463c5374](../../evidence/conditions-sets-050.md#c-8219fe2f463c5374) · [状态效果 S-7460c271e3622030](../../evidence/state_effects-sets-025.md#s-7460c271e3622030)

### observed_connections-009278

```text
(config-if-evpn-es)# system-mac <address> <cr>
```

Handler ` RVA 0x12523560 `；selector ` 0 `；EOL ` RVA 0x3588B098 `。

模式根 ` RVA 0x3587BB78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-ae0d56e841166da6](../../evidence/conditions-sets-067.md#c-ae0d56e841166da6) · [参数 P-55d52e598cd1ada5](../../evidence/parameters-sets-007.md#p-55d52e598cd1ada5)
