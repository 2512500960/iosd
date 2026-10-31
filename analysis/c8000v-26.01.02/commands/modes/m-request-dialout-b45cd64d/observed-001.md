# request-dialout · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009269

```text
(config-vpdn-req-out)# default pool-member <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 107 `；EOL ` RVA 0x356FC388 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c182e08e768c974](../../evidence/conditions-sets-005.md#c-0c182e08e768c974) · [状态效果 S-98dcadd23da22047](../../evidence/state_effects-sets-032.md#s-98dcadd23da22047)

### observed_connections-009266

```text
(config-vpdn-req-out)# default protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 109 `；EOL ` RVA 0x356FC018 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-29ba799f9f833c7c](../../evidence/conditions-sets-016.md#c-29ba799f9f833c7c) · [状态效果 S-98dcadd23da22047](../../evidence/state_effects-sets-032.md#s-98dcadd23da22047)

### observed_connections-009272

```text
(config-vpdn-req-out)# default rotary-group <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 106 `；EOL ` RVA 0x356FC6A0 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3785efedd2e36b05](../../evidence/conditions-sets-022.md#c-3785efedd2e36b05) · [状态效果 S-98dcadd23da22047](../../evidence/state_effects-sets-032.md#s-98dcadd23da22047)

### observed_connections-009274

```text
(config-vpdn-req-out)# default virtual-template <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 105 `；EOL ` RVA 0x356FC9E8 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d67a5fc9a5eaa18c](../../evidence/conditions-sets-083.md#c-d67a5fc9a5eaa18c) · [状态效果 S-98dcadd23da22047](../../evidence/state_effects-sets-032.md#s-98dcadd23da22047)

### observed_connections-009262

```text
(config-vpdn-req-out)# exit <cr>
```

Handler ` RVA 0x11D548D0 `；selector ` 0 `；EOL ` RVA 0x356DF838 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2afeb071a01edbde](../../evidence/conditions-sets-017.md#c-2afeb071a01edbde)

### observed_connections-009267

```text
(config-vpdn-req-out)# no pool-member <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 107 `；EOL ` RVA 0x356FC388 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-12d55f06f254747a](../../evidence/conditions-sets-007.md#c-12d55f06f254747a) · [状态效果 S-54e2396a00be3ee1](../../evidence/state_effects-sets-018.md#s-54e2396a00be3ee1)

### observed_connections-009264

```text
(config-vpdn-req-out)# no protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 109 `；EOL ` RVA 0x356FC018 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-992918dc3a739a1b](../../evidence/conditions-sets-059.md#c-992918dc3a739a1b) · [状态效果 S-54e2396a00be3ee1](../../evidence/state_effects-sets-018.md#s-54e2396a00be3ee1)

### observed_connections-009270

```text
(config-vpdn-req-out)# no rotary-group <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 106 `；EOL ` RVA 0x356FC6A0 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a5b01cff29266d1a](../../evidence/conditions-sets-064.md#c-a5b01cff29266d1a) · [状态效果 S-54e2396a00be3ee1](../../evidence/state_effects-sets-018.md#s-54e2396a00be3ee1)

### observed_connections-009273

```text
(config-vpdn-req-out)# no virtual-template <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 105 `；EOL ` RVA 0x356FC9E8 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d67a5fc9a5eaa18c](../../evidence/conditions-sets-083.md#c-d67a5fc9a5eaa18c) · [状态效果 S-54e2396a00be3ee1](../../evidence/state_effects-sets-018.md#s-54e2396a00be3ee1)

### observed_connections-009268

```text
(config-vpdn-req-out)# pool-member <number:1..255> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 107 `；EOL ` RVA 0x356FC388 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer Profile pool number。

[条件 C-4ac8132d3a79bd14](../../evidence/conditions-sets-029.md#c-4ac8132d3a79bd14) · [参数 P-1d3cd2f00e7520de](../../evidence/parameters-sets-003.md#p-1d3cd2f00e7520de)

### observed_connections-009265

```text
(config-vpdn-req-out)# protocol l2tp <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 109 `；EOL ` RVA 0x356FC018 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31ee772ac448f3b6](../../evidence/conditions-sets-020.md#c-31ee772ac448f3b6) · [状态效果 S-970bdf9af30ea1f3](../../evidence/state_effects-sets-032.md#s-970bdf9af30ea1f3)

### observed_connections-009271

```text
(config-vpdn-req-out)# rotary-group <number:0..255> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 106 `；EOL ` RVA 0x356FC6A0 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer Rotary group number。

[条件 C-1c292127545e131a](../../evidence/conditions-sets-011.md#c-1c292127545e131a) · [参数 P-10c86625808740fd](../../evidence/parameters-sets-002.md#p-10c86625808740fd)

### observed_connections-009263

```text
(config-vpdn-req-out)# virtual-template <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 105 `；EOL ` RVA 0x356FC9E8 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d67a5fc9a5eaa18c](../../evidence/conditions-sets-083.md#c-d67a5fc9a5eaa18c)

### observed_connections-009275

```text
(config-vpdn-req-out)# virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 105 `；EOL ` RVA 0x356FC9E8 `。

模式根 ` RVA 0x356DE498 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Virtual Template interface number。

[条件 C-cde931d77f354b74](../../evidence/conditions-sets-079.md#c-cde931d77f354b74) · [缺口 G-1d181ef4ef2d9323](../../evidence/gaps-sets-001.md#g-1d181ef4ef2d9323) · [参数 P-0c62e8cf5ccda37b](../../evidence/parameters-sets-001.md#p-0c62e8cf5ccda37b)
