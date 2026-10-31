# vpdn-group · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-005208

```text
(config-vpdn)# accept dialin l2tp virtual-template <number:1..25> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 32 `；EOL ` RVA 0x356EAC38 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc549aac856fce08](../../evidence/conditions-sets-085.md#c-dc549aac856fce08) · [参数 P-f8aff2610066a66b](../../evidence/parameters-sets-019.md#p-f8aff2610066a66b) · [状态效果 S-b98dfd564b201bd1](../../evidence/state_effects-sets-039.md#s-b98dfd564b201bd1)

### observed_connections-005209

```text
(config-vpdn)# accept dialout l2tp dialer <number:0..255> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 34 `；EOL ` RVA 0x356EB2D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b0c8e68cbe5c4b4b](../../evidence/conditions-sets-068.md#c-b0c8e68cbe5c4b4b) · [参数 P-44af428cd5664f79](../../evidence/parameters-sets-006.md#p-44af428cd5664f79) · [状态效果 S-7f9f2d8310d2954a](../../evidence/state_effects-sets-027.md#s-7f9f2d8310d2954a)

### observed_connections-005043

```text
(config-vpdn)# accept-dialin <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 102 `；EOL ` RVA 0x356FB978 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-40ce85a68169c16d](../../evidence/conditions-sets-025.md#c-40ce85a68169c16d)

### observed_connections-005041

```text
(config-vpdn)# accept-dialout <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 103 `；EOL ` RVA 0x356FB3D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f43e484ae00cdae](../../evidence/conditions-sets-025.md#c-3f43e484ae00cdae)

### observed_connections-005049

```text
(config-vpdn)# authen-before-forward <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 45 `；EOL ` RVA 0x356FA100 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-75fc6b5374632cb9](../../evidence/conditions-sets-046.md#c-75fc6b5374632cb9)

### observed_connections-005105

```text
(config-vpdn)# backup ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356EC6C0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba242b49066645e7](../../evidence/conditions-sets-072.md#c-ba242b49066645e7) · [参数 P-fb1857781f83d0e3](../../evidence/parameters-sets-019.md#p-fb1857781f83d0e3) · [状态效果 S-3a0ffe002957762a](../../evidence/state_effects-sets-013.md#s-3a0ffe002957762a)

### observed_connections-005061

```text
(config-vpdn)# default accept <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 32 `；EOL ` RVA 0x356EAC38 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2d75dc82ff6b1f91](../../evidence/conditions-sets-018.md#c-2d75dc82ff6b1f91) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005066

```text
(config-vpdn)# default accept <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 34 `；EOL ` RVA 0x356EB2D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ada558494e2aa832](../../evidence/conditions-sets-067.md#c-ada558494e2aa832) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005060

```text
(config-vpdn)# default accept-dialin <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 102 `；EOL ` RVA 0x356FB978 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-40ce85a68169c16d](../../evidence/conditions-sets-025.md#c-40ce85a68169c16d) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005058

```text
(config-vpdn)# default accept-dialout <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 103 `；EOL ` RVA 0x356FB3D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3f43e484ae00cdae](../../evidence/conditions-sets-025.md#c-3f43e484ae00cdae) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005096

```text
(config-vpdn)# default authen-before-forward <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 45 `；EOL ` RVA 0x356FA100 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-75fc6b5374632cb9](../../evidence/conditions-sets-046.md#c-75fc6b5374632cb9) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005155

```text
(config-vpdn)# default backup ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356EC6C0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ba242b49066645e7](../../evidence/conditions-sets-072.md#c-ba242b49066645e7) · [参数 P-fb1857781f83d0e3](../../evidence/parameters-sets-019.md#p-fb1857781f83d0e3) · [状态效果 S-86288e2e9ce6f4b8](../../evidence/state_effects-sets-028.md#s-86288e2e9ce6f4b8)

### observed_connections-005085

```text
(config-vpdn)# default description <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 29 `；EOL ` RVA 0x356F58D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c780e1b1ab80ae0](../../evidence/conditions-sets-054.md#c-8c780e1b1ab80ae0) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005100

```text
(config-vpdn)# default dnis <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 113 `；EOL ` RVA 0x356EBD40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-90a41ca4bad530f6](../../evidence/conditions-sets-056.md#c-90a41ca4bad530f6) · [参数 P-2bf294a4c91b004b](../../evidence/parameters-sets-004.md#p-2bf294a4c91b004b) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005098

```text
(config-vpdn)# default domain <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 114 `；EOL ` RVA 0x356EBA18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bd0c10e3b2026958](../../evidence/conditions-sets-073.md#c-bd0c10e3b2026958) · [参数 P-b99f81b856869249](../../evidence/parameters-sets-014.md#p-b99f81b856869249) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005080

```text
(config-vpdn)# default dsl-line-info-forwarding <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 136 `；EOL ` RVA 0x356F55A0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5adf7485e4859914](../../evidence/conditions-sets-036.md#c-5adf7485e4859914) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005095

```text
(config-vpdn)# default force-local-chap <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 42 `；EOL ` RVA 0x356F9A50 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c6e2a4767ca93a44](../../evidence/conditions-sets-077.md#c-c6e2a4767ca93a44) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005151

```text
(config-vpdn)# default group session-limit <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 31 `；EOL ` RVA 0x356F9DE0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1161be5a04b44f65](../../evidence/conditions-sets-007.md#c-1161be5a04b44f65) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005157

```text
(config-vpdn)# default initiate-to ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356ECBD0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Endpoint's IP address。

[条件 C-88588392c1a6279e](../../evidence/conditions-sets-053.md#c-88588392c1a6279e) · [参数 P-ccc52251ec691edb](../../evidence/parameters-sets-016.md#p-ccc52251ec691edb) · [状态效果 S-9f538378335693bf](../../evidence/state_effects-sets-034.md#s-9f538378335693bf)

### observed_connections-005169

```text
(config-vpdn)# default ip mtu adjust <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 121 `；EOL ` RVA 0x356F6CE8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005135

```text
(config-vpdn)# default ip pmtu <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 122 `；EOL ` RVA 0x356F6F78 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005164

```text
(config-vpdn)# default ip precedence <number:0..7> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 120 `；EOL ` RVA 0x356F5FA0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Precedence value。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [参数 P-3fd9ec3b03745642](../../evidence/parameters-sets-005.md#p-3fd9ec3b03745642) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005167

```text
(config-vpdn)# default ip tos <number:0..15> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 119 `；EOL ` RVA 0x356F6578 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Type of service value。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [参数 P-1657d867c8572a68](../../evidence/parameters-sets-002.md#p-1657d867c8572a68) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005190

```text
(config-vpdn)# default ip tos reflect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 69 `；EOL ` RVA 0x356F69B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005243

```text
(config-vpdn)# default l2tp attribute clid mask-method remove <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 58 `；EOL ` RVA 0x356EE940 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-2761d53c6c29c6ad](../../evidence/state_effects-sets-009.md#s-2761d53c6c29c6ad)

### observed_connections-005166

```text
(config-vpdn)# default l2tp drop out-of-order <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 60 `；EOL ` RVA 0x356EF548 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005118

```text
(config-vpdn)# default l2tp hidden <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 56 `；EOL ` RVA 0x356EEC98 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005162

```text
(config-vpdn)# default l2tp ignore tx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 59 `；EOL ` RVA 0x356EF250 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005213

```text
(config-vpdn)# default l2tp ip tos reflect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 69 `；EOL ` RVA 0x356EE418 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005211

```text
(config-vpdn)# default l2tp ip udp checksum <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 68 `；EOL ` RVA 0x356EE148 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005139

```text
(config-vpdn)# default l2tp rx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 88 `；EOL ` RVA 0x356EFCF0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1ebc72b206b8a0e3](../../evidence/conditions-sets-012.md#c-1ebc72b206b8a0e3) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005198

```text
(config-vpdn)# default l2tp security crypto-profile <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 84 `；EOL ` RVA 0x356F4710 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89b438072b7f9ef8](../../evidence/conditions-sets-053.md#c-89b438072b7f9ef8) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005193

```text
(config-vpdn)# default l2tp security ip <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 86 `；EOL ` RVA 0x356F43D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb1f7d3d0ab48554](../../evidence/conditions-sets-097.md#c-fb1f7d3d0ab48554) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005120

```text
(config-vpdn)# default l2tp sequencing <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 57 `；EOL ` RVA 0x356EEF40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005180

```text
(config-vpdn)# default l2tp tunnel authentication <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 55 `；EOL ` RVA 0x356F1C18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005240

```text
(config-vpdn)# default l2tp tunnel bearer capabilities <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 83 `；EOL ` RVA 0x356F3B38 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c8009b4da54db93b](../../evidence/conditions-sets-077.md#c-c8009b4da54db93b) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005234

```text
(config-vpdn)# default l2tp tunnel busy timeout <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 81 `；EOL ` RVA 0x356F32E8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f3ccb5565e1e7db](../../evidence/conditions-sets-049.md#c-7f3ccb5565e1e7db) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005189

```text
(config-vpdn)# default l2tp tunnel busy-disconnect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 73 `；EOL ` RVA 0x356F1EC0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005237

```text
(config-vpdn)# default l2tp tunnel framing capabilities <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 82 `；EOL ` RVA 0x356F36A8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-73360a0d4363b504](../../evidence/conditions-sets-045.md#c-73360a0d4363b504) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005177

```text
(config-vpdn)# default l2tp tunnel hello <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 62 `；EOL ` RVA 0x356F15E0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-482602bcc01d1814](../../evidence/conditions-sets-028.md#c-482602bcc01d1814) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005203

```text
(config-vpdn)# default l2tp tunnel nosession-timeout <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 71 `；EOL ` RVA 0x356F2518 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4ff0e1b050d130e](../../evidence/conditions-sets-082.md#c-d4ff0e1b050d130e) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005186

```text
(config-vpdn)# default l2tp tunnel password <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 63 `；EOL ` RVA 0x356F18F8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c951d8e129aee7a](../../evidence/conditions-sets-054.md#c-8c951d8e129aee7a) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005200

```text
(config-vpdn)# default l2tp tunnel receive-window <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 61 `；EOL ` RVA 0x356F2200 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83ecdebdb82bd30c](../../evidence/conditions-sets-051.md#c-83ecdebdb82bd30c) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005207

```text
(config-vpdn)# default l2tp tunnel resync <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 141 `；EOL ` RVA 0x356F3F60 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e04a110cb47d23ef](../../evidence/conditions-sets-086.md#c-e04a110cb47d23ef) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005251

```text
(config-vpdn)# default l2tp tunnel retransmit initial retries <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 80 `；EOL ` RVA 0x356F0C28 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fbdefd71045fda38](../../evidence/conditions-sets-097.md#c-fbdefd71045fda38) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005259

```text
(config-vpdn)# default l2tp tunnel retransmit initial timeout max <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 79 `；EOL ` RVA 0x356F1270 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a2c17afee84f902](../../evidence/conditions-sets-035.md#c-5a2c17afee84f902) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005256

```text
(config-vpdn)# default l2tp tunnel retransmit initial timeout min <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 78 `；EOL ` RVA 0x356F0F80 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-313e1d09459710b1](../../evidence/conditions-sets-019.md#c-313e1d09459710b1) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005217

```text
(config-vpdn)# default l2tp tunnel retransmit retries <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 72 `；EOL ` RVA 0x356F0248 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-904079452a1edbd4](../../evidence/conditions-sets-056.md#c-904079452a1edbd4) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005252

```text
(config-vpdn)# default l2tp tunnel retransmit timeout max <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 75 `；EOL ` RVA 0x356F08B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e229a247e7f15bea](../../evidence/conditions-sets-087.md#c-e229a247e7f15bea) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005246

```text
(config-vpdn)# default l2tp tunnel retransmit timeout min <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 74 `；EOL ` RVA 0x356F05C8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5484fb009c468214](../../evidence/conditions-sets-033.md#c-5484fb009c468214) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005233

```text
(config-vpdn)# default l2tp tunnel timeout no-session <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 71 `；EOL ` RVA 0x356F2B88 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5d191d936fc405fb](../../evidence/conditions-sets-036.md#c-5d191d936fc405fb) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005226

```text
(config-vpdn)# default l2tp tunnel timeout setup <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 76 `；EOL ` RVA 0x356F2898 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5632d838bbfb0c7e](../../evidence/conditions-sets-034.md#c-5632d838bbfb0c7e) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005231

```text
(config-vpdn)# default l2tp tunnel zlb delay <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 77 `；EOL ` RVA 0x356F2F58 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3fbd693a990f933e](../../evidence/conditions-sets-025.md#c-3fbd693a990f933e) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005131

```text
(config-vpdn)# default l2tp tx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 87 `；EOL ` RVA 0x356EF868 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f70e33d72016553](../../evidence/conditions-sets-037.md#c-5f70e33d72016553) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005148

```text
(config-vpdn)# default lcp renegotiation <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 50 `；EOL ` RVA 0x356F9748 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c26b50ad9745025](../../evidence/conditions-sets-023.md#c-3c26b50ad9745025) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005153

```text
(config-vpdn)# default loadsharing ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356EC1A8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64582bf267ff0212](../../evidence/conditions-sets-039.md#c-64582bf267ff0212) · [参数 P-a57386f326aa6a37](../../evidence/parameters-sets-013.md#p-a57386f326aa6a37) · [状态效果 S-1190980fa8c5196a](../../evidence/state_effects-sets-004.md#s-1190980fa8c5196a)

### observed_connections-005136

```text
(config-vpdn)# default local name <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 49 `；EOL ` RVA 0x356F7338 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3063b3067297cfaf](../../evidence/conditions-sets-019.md#c-3063b3067297cfaf) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005108

```text
(config-vpdn)# default multilink bundle <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 23 `；EOL ` RVA 0x356ED6C8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9f8bebbd9813fbda](../../evidence/conditions-sets-062.md#c-9f8bebbd9813fbda) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005112

```text
(config-vpdn)# default multilink link <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 24 `；EOL ` RVA 0x356ED9B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1c89bfa809cca65e](../../evidence/conditions-sets-011.md#c-1c89bfa809cca65e) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005197

```text
(config-vpdn)# default pptp flow-control receive-window <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 91 `；EOL ` RVA 0x356F9380 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-317aee0e0dd90e42](../../evidence/conditions-sets-019.md#c-317aee0e0dd90e42) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005191

```text
(config-vpdn)# default pptp flow-control static-rtt <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 90 `；EOL ` RVA 0x356F9090 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a63c2f64c15e1ad9](../../evidence/conditions-sets-064.md#c-a63c2f64c15e1ad9) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005183

```text
(config-vpdn)# default pptp tunnel echo <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 89 `；EOL ` RVA 0x356F86C0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-27881b76c4a566eb](../../evidence/conditions-sets-016.md#c-27881b76c4a566eb) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005220

```text
(config-vpdn)# default pptp tunnel timeout setup <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 92 `；EOL ` RVA 0x356F8A18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e922701a0d205505](../../evidence/conditions-sets-090.md#c-e922701a0d205505) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005223

```text
(config-vpdn)# default pptp tunnel timeout teardown <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 93 `；EOL ` RVA 0x356F8D08 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e3b25b5439e0371](../../evidence/conditions-sets-055.md#c-8e3b25b5439e0371) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005116

```text
(config-vpdn)# default redirect identifier <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 123 `；EOL ` RVA 0x356F4F08 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8611b1010cdac3d3](../../evidence/conditions-sets-052.md#c-8611b1010cdac3d3) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005172

```text
(config-vpdn)# default relay pppoe bba-group <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 131 `；EOL ` RVA 0x356F7718 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e6c713ae52fa539](../../evidence/conditions-sets-061.md#c-9e6c713ae52fa539) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005054

```text
(config-vpdn)# default request <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 33 `；EOL ` RVA 0x356E9F80 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c368a6476b86f059](../../evidence/conditions-sets-075.md#c-c368a6476b86f059) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005062

```text
(config-vpdn)# default request <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 35 `；EOL ` RVA 0x356EA458 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4744d914b8c3c43f](../../evidence/conditions-sets-028.md#c-4744d914b8c3c43f) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005059

```text
(config-vpdn)# default request-dialin <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 100 `；EOL ` RVA 0x356FB688 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fd39122bb69cabfc](../../evidence/conditions-sets-098.md#c-fd39122bb69cabfc) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005067

```text
(config-vpdn)# default request-dialout <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 101 `；EOL ` RVA 0x356FBC68 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aa80a94c9e27f942](../../evidence/conditions-sets-066.md#c-aa80a94c9e27f942) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005094

```text
(config-vpdn)# default scalability call-drops <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 99 `；EOL ` RVA 0x356F7FD8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-964431eafb9651e9](../../evidence/conditions-sets-058.md#c-964431eafb9651e9) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005090

```text
(config-vpdn)# default scalability multilink-num <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 98 `；EOL ` RVA 0x356F7D58 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1e2d200250b0af9e](../../evidence/conditions-sets-012.md#c-1e2d200250b0af9e) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005140

```text
(config-vpdn)# default scalability one-session-per-tunnel <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 97 `；EOL ` RVA 0x356F7D30 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e35b3e8c0b633b76](../../evidence/conditions-sets-088.md#c-e35b3e8c0b633b76) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005141

```text
(config-vpdn)# default scalability virtual-template <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 96 `；EOL ` RVA 0x356F7AA8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ae95087e851f386f](../../evidence/conditions-sets-067.md#c-ae95087e851f386f) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005072

```text
(config-vpdn)# default session-limit <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 25 `；EOL ` RVA 0x356ED308 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c6640458c4e448c0](../../evidence/conditions-sets-076.md#c-c6640458c4e448c0) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005126

```text
(config-vpdn)# default source vpdn-template <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 30 `；EOL ` RVA 0x356F5C40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2a55a6aab6ad5c31](../../evidence/conditions-sets-017.md#c-2a55a6aab6ad5c31) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005077

```text
(config-vpdn)# default source-ip <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 70 `；EOL ` RVA 0x356F4BB8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e20ffcf034032f8](../../evidence/conditions-sets-055.md#c-8e20ffcf034032f8) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005106

```text
(config-vpdn)# default sso enable <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 135 `；EOL ` RVA 0x356EDD00 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-227dfe0127eda54f](../../evidence/conditions-sets-014.md#c-227dfe0127eda54f) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005069

```text
(config-vpdn)# default terminate-from <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 117 `；EOL ` RVA 0x356ECF68 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ace1d741e4169f57](../../evidence/conditions-sets-067.md#c-ace1d741e4169f57) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005081

```text
(config-vpdn)# default vpn <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 125 `；EOL ` RVA 0x356F5228 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3fdacb5158b75288](../../evidence/conditions-sets-025.md#c-3fdacb5158b75288) · [状态效果 S-8c8d1bb8a19ead0f](../../evidence/state_effects-sets-030.md#s-8c8d1bb8a19ead0f)

### observed_connections-005084

```text
(config-vpdn)# description <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 29 `；EOL ` RVA 0x356F58D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 60 characters describing this VPDN group。

[条件 C-a9aa9d44d74fab72](../../evidence/conditions-sets-065.md#c-a9aa9d44d74fab72) · [参数 P-c0f64b15baf8f246](../../evidence/parameters-sets-015.md#p-c0f64b15baf8f246)

### observed_connections-005064

```text
(config-vpdn)# dnis <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 113 `；EOL ` RVA 0x356EBD40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-90a41ca4bad530f6](../../evidence/conditions-sets-056.md#c-90a41ca4bad530f6) · [参数 P-2bf294a4c91b004b](../../evidence/parameters-sets-004.md#p-2bf294a4c91b004b)

### observed_connections-005057

```text
(config-vpdn)# domain <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 114 `；EOL ` RVA 0x356EBA18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bd0c10e3b2026958](../../evidence/conditions-sets-073.md#c-bd0c10e3b2026958) · [参数 P-b99f81b856869249](../../evidence/parameters-sets-014.md#p-b99f81b856869249)

### observed_connections-005045

```text
(config-vpdn)# dsl-line-info-forwarding <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 136 `；EOL ` RVA 0x356F55A0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5adf7485e4859914](../../evidence/conditions-sets-036.md#c-5adf7485e4859914)

### observed_connections-005040

```text
(config-vpdn)# exit <cr>
```

Handler ` RVA 0x11D53BA0 `；selector ` 0 `；EOL ` RVA 0x356DE930 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a03a7cb2f030cbf7](../../evidence/conditions-sets-062.md#c-a03a7cb2f030cbf7)

### observed_connections-005048

```text
(config-vpdn)# force-local-chap <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 42 `；EOL ` RVA 0x356F9A50 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c6e2a4767ca93a44](../../evidence/conditions-sets-077.md#c-c6e2a4767ca93a44)

### observed_connections-005150

```text
(config-vpdn)# group session-limit <number:1..65535> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 31 `；EOL ` RVA 0x356F9DE0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of sessions。

[条件 C-d7d941ffee5f5b78](../../evidence/conditions-sets-083.md#c-d7d941ffee5f5b78) · [参数 P-0511994b44e920e1](../../evidence/parameters-sets-001.md#p-0511994b44e920e1)

### observed_connections-005110

```text
(config-vpdn)# initiate-to ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356ECBD0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Endpoint's IP address。

[条件 C-88588392c1a6279e](../../evidence/conditions-sets-053.md#c-88588392c1a6279e) · [参数 P-ccc52251ec691edb](../../evidence/parameters-sets-016.md#p-ccc52251ec691edb) · [状态效果 S-f555576e96141f6b](../../evidence/state_effects-sets-052.md#s-f555576e96141f6b)

### observed_connections-005128

```text
(config-vpdn)# ip mtu adjust <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 121 `；EOL ` RVA 0x356F6CE8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085)

### observed_connections-005087

```text
(config-vpdn)# ip pmtu <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 122 `；EOL ` RVA 0x356F6F78 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085)

### observed_connections-005122

```text
(config-vpdn)# ip precedence <number:0..7> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 120 `；EOL ` RVA 0x356F5FA0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Precedence value。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [参数 P-3fd9ec3b03745642](../../evidence/parameters-sets-005.md#p-3fd9ec3b03745642)

### observed_connections-005125

```text
(config-vpdn)# ip tos <number:0..15> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 119 `；EOL ` RVA 0x356F6578 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Type of service value。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [参数 P-1657d867c8572a68](../../evidence/parameters-sets-002.md#p-1657d867c8572a68)

### observed_connections-005147

```text
(config-vpdn)# ip tos reflect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 69 `；EOL ` RVA 0x356F69B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085)

### observed_connections-005214

```text
(config-vpdn)# l2tp attribute clid mask-method remove <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 58 `；EOL ` RVA 0x356EE940 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-9355d40524f3176d](../../evidence/state_effects-sets-031.md#s-9355d40524f3176d)

### observed_connections-005123

```text
(config-vpdn)# l2tp drop out-of-order <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 60 `；EOL ` RVA 0x356EF548 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005079

```text
(config-vpdn)# l2tp hidden <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 56 `；EOL ` RVA 0x356EEC98 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005121

```text
(config-vpdn)# l2tp ignore tx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 59 `；EOL ` RVA 0x356EF250 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005159

```text
(config-vpdn)# l2tp ip tos reflect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 69 `；EOL ` RVA 0x356EE418 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005158

```text
(config-vpdn)# l2tp ip udp checksum <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 68 `；EOL ` RVA 0x356EE148 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005142

```text
(config-vpdn)# l2tp rx-speed ANCP <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 88 `；EOL ` RVA 0x356EFCF0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41c03de97827b741](../../evidence/conditions-sets-026.md#c-41c03de97827b741) · [状态效果 S-c6abe3a0964ac268](../../evidence/state_effects-sets-042.md#s-c6abe3a0964ac268)

### observed_connections-005204

```text
(config-vpdn)# l2tp security crypto-profile <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 84 `；EOL ` RVA 0x356F4710 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Crypto profile name。

[条件 C-f0f0c1cc11ca23c7](../../evidence/conditions-sets-093.md#c-f0f0c1cc11ca23c7) · [参数 P-845ae1b03fa0ce9a](../../evidence/parameters-sets-010.md#p-845ae1b03fa0ce9a) · [状态效果 S-a65df3267c5efafe](../../evidence/state_effects-sets-035.md#s-a65df3267c5efafe)

### observed_connections-005188

```text
(config-vpdn)# l2tp security ip address-check <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 86 `；EOL ` RVA 0x356F43D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf2779f4bbf1c518](../../evidence/conditions-sets-080.md#c-cf2779f4bbf1c518)

### observed_connections-005082

```text
(config-vpdn)# l2tp sequencing <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 57 `；EOL ` RVA 0x356EEF40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005143

```text
(config-vpdn)# l2tp tunnel authentication <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 55 `；EOL ` RVA 0x356F1C18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005239

```text
(config-vpdn)# l2tp tunnel bearer capabilities none <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 83 `；EOL ` RVA 0x356F3B38 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4a920a1b40abcf6f](../../evidence/conditions-sets-029.md#c-4a920a1b40abcf6f) · [状态效果 S-63b49c8664ead04a](../../evidence/state_effects-sets-021.md#s-63b49c8664ead04a)

### observed_connections-005205

```text
(config-vpdn)# l2tp tunnel busy 0 <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 81 `；EOL ` RVA 0x356F32E8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4cf872b843166b7f](../../evidence/state_effects-sets-017.md#s-4cf872b843166b7f)

### observed_connections-005146

```text
(config-vpdn)# l2tp tunnel busy-disconnect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 73 `；EOL ` RVA 0x356F1EC0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7)

### observed_connections-005236

```text
(config-vpdn)# l2tp tunnel framing capabilities none <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 82 `；EOL ` RVA 0x356F36A8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4af1e24f532d6513](../../evidence/conditions-sets-029.md#c-4af1e24f532d6513) · [状态效果 S-f7996cda3af23c54](../../evidence/state_effects-sets-052.md#s-f7996cda3af23c54)

### observed_connections-005174

```text
(config-vpdn)# l2tp tunnel hello <number:0..1000> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 62 `；EOL ` RVA 0x356F15E0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds, default is 60。

[条件 C-e0ce3d5af1e97de2](../../evidence/conditions-sets-087.md#c-e0ce3d5af1e97de2) · [参数 P-ab1689f8eb677aff](../../evidence/parameters-sets-013.md#p-ab1689f8eb677aff)

### observed_connections-005202

```text
(config-vpdn)# l2tp tunnel nosession-timeout <number:0..86400> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 71 `；EOL ` RVA 0x356F2518 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-be1a83fa3e11d78c](../../evidence/conditions-sets-073.md#c-be1a83fa3e11d78c) · [参数 P-d990a6e7aad99234](../../evidence/parameters-sets-016.md#p-d990a6e7aad99234)

### observed_connections-005196

```text
(config-vpdn)# l2tp tunnel password <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 63 `；EOL ` RVA 0x356F18F8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tunnel password string。

[条件 C-26e222bb0080edc6](../../evidence/conditions-sets-015.md#c-26e222bb0080edc6) · [参数 P-9dac2c772d93b063](../../evidence/parameters-sets-012.md#p-9dac2c772d93b063)

### observed_connections-005261

```text
(config-vpdn)# l2tp tunnel receive-window <number:dynamic> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 61 `；EOL ` RVA 0x356F2200 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of packets。

[条件 C-cad55c345971e96d](../../evidence/conditions-sets-078.md#c-cad55c345971e96d) · [缺口 G-931c50edf8bf58c9](../../evidence/gaps-sets-005.md#g-931c50edf8bf58c9) · [参数 P-8d1eb3f6c7eeadfc](../../evidence/parameters-sets-011.md#p-8d1eb3f6c7eeadfc)

### observed_connections-005262

```text
(config-vpdn)# l2tp tunnel resync <number:dynamic> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 141 `；EOL ` RVA 0x356F3F60 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of packets。

[条件 C-9c667c638a260c95](../../evidence/conditions-sets-060.md#c-9c667c638a260c95) · [缺口 G-c09ba633e83229fd](../../evidence/gaps-sets-007.md#g-c09ba633e83229fd) · [参数 P-0e6f9d74ebd3f206](../../evidence/parameters-sets-002.md#p-0e6f9d74ebd3f206)

### observed_connections-005249

```text
(config-vpdn)# l2tp tunnel retransmit initial retries <number:1..1000> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 80 `；EOL ` RVA 0x356F0C28 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum SCCRQ retransmissions。

[条件 C-18a9e8973b947130](../../evidence/conditions-sets-010.md#c-18a9e8973b947130) · [参数 P-c76942e659ec55e1](../../evidence/parameters-sets-015.md#p-c76942e659ec55e1)

### observed_connections-005258

```text
(config-vpdn)# l2tp tunnel retransmit initial timeout max <number:1..8> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 79 `；EOL ` RVA 0x356F1270 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-2c8f8c339232388a](../../evidence/conditions-sets-017.md#c-2c8f8c339232388a) · [参数 P-b199e35fbc641880](../../evidence/parameters-sets-013.md#p-b199e35fbc641880)

### observed_connections-005255

```text
(config-vpdn)# l2tp tunnel retransmit initial timeout min <number:1..8> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 78 `；EOL ` RVA 0x356F0F80 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-66478555eba26158](../../evidence/conditions-sets-040.md#c-66478555eba26158) · [参数 P-67e217811a31b2b8](../../evidence/parameters-sets-008.md#p-67e217811a31b2b8)

### observed_connections-005216

```text
(config-vpdn)# l2tp tunnel retransmit retries <number:5..1000> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 72 `；EOL ` RVA 0x356F0248 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum retransmissions。

[条件 C-a1bd8927155815fa](../../evidence/conditions-sets-062.md#c-a1bd8927155815fa) · [参数 P-b2168936c6f6f7e5](../../evidence/parameters-sets-014.md#p-b2168936c6f6f7e5)

### observed_connections-005250

```text
(config-vpdn)# l2tp tunnel retransmit timeout max <number:1..8> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 75 `；EOL ` RVA 0x356F08B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-a959c4f27b7c1c3f](../../evidence/conditions-sets-065.md#c-a959c4f27b7c1c3f) · [参数 P-d009e4a0b4974d22](../../evidence/parameters-sets-016.md#p-d009e4a0b4974d22)

### observed_connections-005245

```text
(config-vpdn)# l2tp tunnel retransmit timeout min <number:1..8> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 74 `；EOL ` RVA 0x356F05C8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-4a126279fa211243](../../evidence/conditions-sets-029.md#c-4a126279fa211243) · [参数 P-54d6741f57ba3105](../../evidence/parameters-sets-007.md#p-54d6741f57ba3105)

### observed_connections-005230

```text
(config-vpdn)# l2tp tunnel timeout no-session <number:0..86400> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 71 `；EOL ` RVA 0x356F2B88 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-7acdff43f9649d6c](../../evidence/conditions-sets-048.md#c-7acdff43f9649d6c) · [参数 P-5372e786cabe7954](../../evidence/parameters-sets-007.md#p-5372e786cabe7954)

### observed_connections-005225

```text
(config-vpdn)# l2tp tunnel timeout setup <number:60..6000> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 76 `；EOL ` RVA 0x356F2898 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-3549e8073acf1685](../../evidence/conditions-sets-021.md#c-3549e8073acf1685) · [参数 P-20035ef8bd9a01f2](../../evidence/parameters-sets-003.md#p-20035ef8bd9a01f2)

### observed_connections-005229

```text
(config-vpdn)# l2tp tunnel zlb delay <number:1..5> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 77 `；EOL ` RVA 0x356F2F58 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-f4a2443ef9e0b850](../../evidence/conditions-sets-094.md#c-f4a2443ef9e0b850) · [参数 P-259cd913318bd1d6](../../evidence/parameters-sets-003.md#p-259cd913318bd1d6)

### observed_connections-005138

```text
(config-vpdn)# l2tp tx-speed ANCP <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 87 `；EOL ` RVA 0x356EF868 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97dfff7fa76030a1](../../evidence/conditions-sets-059.md#c-97dfff7fa76030a1) · [状态效果 S-efb5c5eeb7ade9ae](../../evidence/state_effects-sets-051.md#s-efb5c5eeb7ade9ae)

### observed_connections-005145

```text
(config-vpdn)# lcp renegotiation always <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 50 `；EOL ` RVA 0x356F9748 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bdecc995f099eefc](../../evidence/conditions-sets-073.md#c-bdecc995f099eefc) · [状态效果 S-ee57b420ec5d6393](../../evidence/state_effects-sets-050.md#s-ee57b420ec5d6393)

### observed_connections-005101

```text
(config-vpdn)# loadsharing ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356EC1A8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64582bf267ff0212](../../evidence/conditions-sets-039.md#c-64582bf267ff0212) · [参数 P-a57386f326aa6a37](../../evidence/parameters-sets-013.md#p-a57386f326aa6a37) · [状态效果 S-8282d9ea71848a63](../../evidence/state_effects-sets-028.md#s-8282d9ea71848a63)

### observed_connections-005133

```text
(config-vpdn)# local name <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 49 `；EOL ` RVA 0x356F7338 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Local name string。

[条件 C-12e4db42415ed5f1](../../evidence/conditions-sets-007.md#c-12e4db42415ed5f1) · [参数 P-c8b0494eabe021ae](../../evidence/parameters-sets-015.md#p-c8b0494eabe021ae)

### observed_connections-005107

```text
(config-vpdn)# multilink bundle <number:0..65535> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 23 `；EOL ` RVA 0x356ED6C8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of bundles per VPDN group。

[条件 C-c5db8334d5be38c2](../../evidence/conditions-sets-076.md#c-c5db8334d5be38c2) · [参数 P-7ce2f2e70565c197](../../evidence/parameters-sets-010.md#p-7ce2f2e70565c197)

### observed_connections-005111

```text
(config-vpdn)# multilink link <number:0..65535> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 24 `；EOL ` RVA 0x356ED9B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of links per bundle。

[条件 C-3899d754558083a3](../../evidence/conditions-sets-022.md#c-3899d754558083a3) · [参数 P-293c907d1305ba1f](../../evidence/parameters-sets-004.md#p-293c907d1305ba1f)

### observed_connections-005055

```text
(config-vpdn)# no accept <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 32 `；EOL ` RVA 0x356EAC38 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-de5697535f3b7b2f](../../evidence/conditions-sets-086.md#c-de5697535f3b7b2f) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005063

```text
(config-vpdn)# no accept <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 34 `；EOL ` RVA 0x356EB2D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7726bef4a8b3ceb3](../../evidence/conditions-sets-046.md#c-7726bef4a8b3ceb3) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005053

```text
(config-vpdn)# no accept-dialin <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 102 `；EOL ` RVA 0x356FB978 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-40ce85a68169c16d](../../evidence/conditions-sets-025.md#c-40ce85a68169c16d) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005051

```text
(config-vpdn)# no accept-dialout <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 103 `；EOL ` RVA 0x356FB3D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3f43e484ae00cdae](../../evidence/conditions-sets-025.md#c-3f43e484ae00cdae) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005093

```text
(config-vpdn)# no authen-before-forward <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 45 `；EOL ` RVA 0x356FA100 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75fc6b5374632cb9](../../evidence/conditions-sets-046.md#c-75fc6b5374632cb9) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005154

```text
(config-vpdn)# no backup ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356EC6C0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ba242b49066645e7](../../evidence/conditions-sets-072.md#c-ba242b49066645e7) · [参数 P-fb1857781f83d0e3](../../evidence/parameters-sets-019.md#p-fb1857781f83d0e3) · [状态效果 S-af28d254e559b82d](../../evidence/state_effects-sets-037.md#s-af28d254e559b82d)

### observed_connections-005083

```text
(config-vpdn)# no description <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 29 `；EOL ` RVA 0x356F58D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f4a17276e3cadf7b](../../evidence/conditions-sets-094.md#c-f4a17276e3cadf7b) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005099

```text
(config-vpdn)# no dnis <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 113 `；EOL ` RVA 0x356EBD40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-90a41ca4bad530f6](../../evidence/conditions-sets-056.md#c-90a41ca4bad530f6) · [参数 P-2bf294a4c91b004b](../../evidence/parameters-sets-004.md#p-2bf294a4c91b004b) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005097

```text
(config-vpdn)# no domain <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 114 `；EOL ` RVA 0x356EBA18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bd0c10e3b2026958](../../evidence/conditions-sets-073.md#c-bd0c10e3b2026958) · [参数 P-b99f81b856869249](../../evidence/parameters-sets-014.md#p-b99f81b856869249) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005076

```text
(config-vpdn)# no dsl-line-info-forwarding <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 136 `；EOL ` RVA 0x356F55A0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5adf7485e4859914](../../evidence/conditions-sets-036.md#c-5adf7485e4859914) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005092

```text
(config-vpdn)# no force-local-chap <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 42 `；EOL ` RVA 0x356F9A50 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c6e2a4767ca93a44](../../evidence/conditions-sets-077.md#c-c6e2a4767ca93a44) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005149

```text
(config-vpdn)# no group session-limit <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 31 `；EOL ` RVA 0x356F9DE0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b7ea6bf04a641449](../../evidence/conditions-sets-071.md#c-b7ea6bf04a641449) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005156

```text
(config-vpdn)# no initiate-to ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356ECBD0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Endpoint's IP address。

[条件 C-88588392c1a6279e](../../evidence/conditions-sets-053.md#c-88588392c1a6279e) · [参数 P-ccc52251ec691edb](../../evidence/parameters-sets-016.md#p-ccc52251ec691edb) · [状态效果 S-92dd26cb35d5a5c8](../../evidence/state_effects-sets-031.md#s-92dd26cb35d5a5c8)

### observed_connections-005168

```text
(config-vpdn)# no ip mtu adjust <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 121 `；EOL ` RVA 0x356F6CE8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005129

```text
(config-vpdn)# no ip pmtu <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 122 `；EOL ` RVA 0x356F6F78 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005161

```text
(config-vpdn)# no ip precedence <number:0..7> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 120 `；EOL ` RVA 0x356F5FA0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Precedence value。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [参数 P-3fd9ec3b03745642](../../evidence/parameters-sets-005.md#p-3fd9ec3b03745642) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005165

```text
(config-vpdn)# no ip tos <number:0..15> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 119 `；EOL ` RVA 0x356F6578 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Type of service value。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [参数 P-1657d867c8572a68](../../evidence/parameters-sets-002.md#p-1657d867c8572a68) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005182

```text
(config-vpdn)# no ip tos reflect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 69 `；EOL ` RVA 0x356F69B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4a5c0087e7d87085](../../evidence/conditions-sets-029.md#c-4a5c0087e7d87085) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005242

```text
(config-vpdn)# no l2tp attribute clid mask-method remove <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 58 `；EOL ` RVA 0x356EE940 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-0a14606d88447f89](../../evidence/state_effects-sets-003.md#s-0a14606d88447f89)

### observed_connections-005163

```text
(config-vpdn)# no l2tp drop out-of-order <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 60 `；EOL ` RVA 0x356EF548 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005115

```text
(config-vpdn)# no l2tp hidden <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 56 `；EOL ` RVA 0x356EEC98 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005160

```text
(config-vpdn)# no l2tp ignore tx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 59 `；EOL ` RVA 0x356EF250 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005212

```text
(config-vpdn)# no l2tp ip tos reflect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 69 `；EOL ` RVA 0x356EE418 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005210

```text
(config-vpdn)# no l2tp ip udp checksum <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 68 `；EOL ` RVA 0x356EE148 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005132

```text
(config-vpdn)# no l2tp rx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 88 `；EOL ` RVA 0x356EFCF0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8a6d2b74a91ae037](../../evidence/conditions-sets-054.md#c-8a6d2b74a91ae037) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005194

```text
(config-vpdn)# no l2tp security crypto-profile <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 84 `；EOL ` RVA 0x356F4710 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7b42b1036a0876d2](../../evidence/conditions-sets-048.md#c-7b42b1036a0876d2) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005185

```text
(config-vpdn)# no l2tp security ip <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 86 `；EOL ` RVA 0x356F43D8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-76ba5b03febcf1ac](../../evidence/conditions-sets-046.md#c-76ba5b03febcf1ac) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005119

```text
(config-vpdn)# no l2tp sequencing <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 57 `；EOL ` RVA 0x356EEF40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005175

```text
(config-vpdn)# no l2tp tunnel authentication <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 55 `；EOL ` RVA 0x356F1C18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005238

```text
(config-vpdn)# no l2tp tunnel bearer capabilities <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 83 `；EOL ` RVA 0x356F3B38 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a5d103ae1d572423](../../evidence/conditions-sets-064.md#c-a5d103ae1d572423) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005232

```text
(config-vpdn)# no l2tp tunnel busy timeout <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 81 `；EOL ` RVA 0x356F32E8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74bf54221da40177](../../evidence/conditions-sets-045.md#c-74bf54221da40177) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005181

```text
(config-vpdn)# no l2tp tunnel busy-disconnect <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 73 `；EOL ` RVA 0x356F1EC0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a79c32df5b81ccb7](../../evidence/conditions-sets-065.md#c-a79c32df5b81ccb7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005235

```text
(config-vpdn)# no l2tp tunnel framing capabilities <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 82 `；EOL ` RVA 0x356F36A8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5f1c89866de1901e](../../evidence/conditions-sets-037.md#c-5f1c89866de1901e) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005173

```text
(config-vpdn)# no l2tp tunnel hello <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 62 `；EOL ` RVA 0x356F15E0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-19c859035cf20ce7](../../evidence/conditions-sets-010.md#c-19c859035cf20ce7) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005201

```text
(config-vpdn)# no l2tp tunnel nosession-timeout <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 71 `；EOL ` RVA 0x356F2518 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0bcff23c5c43e222](../../evidence/conditions-sets-005.md#c-0bcff23c5c43e222) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005178

```text
(config-vpdn)# no l2tp tunnel password <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 63 `；EOL ` RVA 0x356F18F8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f745df380c9e13c1](../../evidence/conditions-sets-095.md#c-f745df380c9e13c1) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005199

```text
(config-vpdn)# no l2tp tunnel receive-window <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 61 `；EOL ` RVA 0x356F2200 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0d167e6b3d6c2e41](../../evidence/conditions-sets-005.md#c-0d167e6b3d6c2e41) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005206

```text
(config-vpdn)# no l2tp tunnel resync <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 141 `；EOL ` RVA 0x356F3F60 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f1f51d34669f8ae5](../../evidence/conditions-sets-093.md#c-f1f51d34669f8ae5) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005247

```text
(config-vpdn)# no l2tp tunnel retransmit initial retries <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 80 `；EOL ` RVA 0x356F0C28 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-025788d4ac0c726e](../../evidence/conditions-sets-001.md#c-025788d4ac0c726e) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005257

```text
(config-vpdn)# no l2tp tunnel retransmit initial timeout max <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 79 `；EOL ` RVA 0x356F1270 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-50e3a3a218fd8c53](../../evidence/conditions-sets-032.md#c-50e3a3a218fd8c53) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005254

```text
(config-vpdn)# no l2tp tunnel retransmit initial timeout min <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 78 `；EOL ` RVA 0x356F0F80 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-105dcd44d76bbec3](../../evidence/conditions-sets-006.md#c-105dcd44d76bbec3) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005215

```text
(config-vpdn)# no l2tp tunnel retransmit retries <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 72 `；EOL ` RVA 0x356F0248 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fd648b646bafef2b](../../evidence/conditions-sets-098.md#c-fd648b646bafef2b) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005248

```text
(config-vpdn)# no l2tp tunnel retransmit timeout max <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 75 `；EOL ` RVA 0x356F08B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b361b416850ad8a2](../../evidence/conditions-sets-069.md#c-b361b416850ad8a2) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005244

```text
(config-vpdn)# no l2tp tunnel retransmit timeout min <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 74 `；EOL ` RVA 0x356F05C8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-49427a293e65e961](../../evidence/conditions-sets-029.md#c-49427a293e65e961) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005228

```text
(config-vpdn)# no l2tp tunnel timeout no-session <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 71 `；EOL ` RVA 0x356F2B88 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-331d8a61b9251310](../../evidence/conditions-sets-020.md#c-331d8a61b9251310) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005224

```text
(config-vpdn)# no l2tp tunnel timeout setup <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 76 `；EOL ` RVA 0x356F2898 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a1d9e40e33c81b44](../../evidence/conditions-sets-062.md#c-a1d9e40e33c81b44) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005227

```text
(config-vpdn)# no l2tp tunnel zlb delay <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 77 `；EOL ` RVA 0x356F2F58 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c7c122592e7a8401](../../evidence/conditions-sets-077.md#c-c7c122592e7a8401) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005127

```text
(config-vpdn)# no l2tp tx-speed <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 87 `；EOL ` RVA 0x356EF868 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-28c4c09e7b661291](../../evidence/conditions-sets-016.md#c-28c4c09e7b661291) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005144

```text
(config-vpdn)# no lcp renegotiation <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 50 `；EOL ` RVA 0x356F9748 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f203387a943a0b8c](../../evidence/conditions-sets-093.md#c-f203387a943a0b8c) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005152

```text
(config-vpdn)# no loadsharing ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 116 `；EOL ` RVA 0x356EC1A8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-64582bf267ff0212](../../evidence/conditions-sets-039.md#c-64582bf267ff0212) · [参数 P-a57386f326aa6a37](../../evidence/parameters-sets-013.md#p-a57386f326aa6a37) · [状态效果 S-232bf99abcd46982](../../evidence/state_effects-sets-008.md#s-232bf99abcd46982)

### observed_connections-005130

```text
(config-vpdn)# no local name <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 49 `；EOL ` RVA 0x356F7338 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9600af7590081977](../../evidence/conditions-sets-058.md#c-9600af7590081977) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005104

```text
(config-vpdn)# no multilink bundle <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 23 `；EOL ` RVA 0x356ED6C8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-17ab9dd46e2f669e](../../evidence/conditions-sets-009.md#c-17ab9dd46e2f669e) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005109

```text
(config-vpdn)# no multilink link <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 24 `；EOL ` RVA 0x356ED9B8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-82aeed6c9c29b50f](../../evidence/conditions-sets-051.md#c-82aeed6c9c29b50f) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005192

```text
(config-vpdn)# no pptp flow-control receive-window <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 91 `；EOL ` RVA 0x356F9380 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e0803f8f083c81fc](../../evidence/conditions-sets-086.md#c-e0803f8f083c81fc) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005184

```text
(config-vpdn)# no pptp flow-control static-rtt <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 90 `；EOL ` RVA 0x356F9090 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1aaa4083ec4e7a89](../../evidence/conditions-sets-010.md#c-1aaa4083ec4e7a89) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005176

```text
(config-vpdn)# no pptp tunnel echo <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 89 `；EOL ` RVA 0x356F86C0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9c291dc6ca354847](../../evidence/conditions-sets-060.md#c-9c291dc6ca354847) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005218

```text
(config-vpdn)# no pptp tunnel timeout setup <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 92 `；EOL ` RVA 0x356F8A18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-03dbfc25e4f9cc8c](../../evidence/conditions-sets-002.md#c-03dbfc25e4f9cc8c) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005221

```text
(config-vpdn)# no pptp tunnel timeout teardown <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 93 `；EOL ` RVA 0x356F8D08 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-193aeecd968056e9](../../evidence/conditions-sets-010.md#c-193aeecd968056e9) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005113

```text
(config-vpdn)# no redirect identifier <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 123 `；EOL ` RVA 0x356F4F08 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0deac54b21d3102c](../../evidence/conditions-sets-006.md#c-0deac54b21d3102c) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005170

```text
(config-vpdn)# no relay pppoe bba-group <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 131 `；EOL ` RVA 0x356F7718 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d12ee06b5a910a11](../../evidence/conditions-sets-081.md#c-d12ee06b5a910a11) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005050

```text
(config-vpdn)# no request <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 33 `；EOL ` RVA 0x356E9F80 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7fe479a89a5aee5f](../../evidence/conditions-sets-050.md#c-7fe479a89a5aee5f) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005056

```text
(config-vpdn)# no request <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 35 `；EOL ` RVA 0x356EA458 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b09962767efc9914](../../evidence/conditions-sets-068.md#c-b09962767efc9914) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005052

```text
(config-vpdn)# no request-dialin <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 100 `；EOL ` RVA 0x356FB688 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fd39122bb69cabfc](../../evidence/conditions-sets-098.md#c-fd39122bb69cabfc) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005065

```text
(config-vpdn)# no request-dialout <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 101 `；EOL ` RVA 0x356FBC68 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aa80a94c9e27f942](../../evidence/conditions-sets-066.md#c-aa80a94c9e27f942) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005091

```text
(config-vpdn)# no scalability call-drops <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 99 `；EOL ` RVA 0x356F7FD8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-964431eafb9651e9](../../evidence/conditions-sets-058.md#c-964431eafb9651e9) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005089

```text
(config-vpdn)# no scalability multilink-num <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 98 `；EOL ` RVA 0x356F7D58 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1e2d200250b0af9e](../../evidence/conditions-sets-012.md#c-1e2d200250b0af9e) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005134

```text
(config-vpdn)# no scalability one-session-per-tunnel <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 97 `；EOL ` RVA 0x356F7D30 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e35b3e8c0b633b76](../../evidence/conditions-sets-088.md#c-e35b3e8c0b633b76) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005137

```text
(config-vpdn)# no scalability virtual-template <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 96 `；EOL ` RVA 0x356F7AA8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7a549c3f0596695d](../../evidence/conditions-sets-047.md#c-7a549c3f0596695d) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005070

```text
(config-vpdn)# no session-limit <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 25 `；EOL ` RVA 0x356ED308 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9bcaba582113fa8e](../../evidence/conditions-sets-060.md#c-9bcaba582113fa8e) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005124

```text
(config-vpdn)# no source vpdn-template <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 30 `；EOL ` RVA 0x356F5C40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2a55a6aab6ad5c31](../../evidence/conditions-sets-017.md#c-2a55a6aab6ad5c31) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005074

```text
(config-vpdn)# no source-ip <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 70 `；EOL ` RVA 0x356F4BB8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c4100674d9e28d3e](../../evidence/conditions-sets-076.md#c-c4100674d9e28d3e) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005103

```text
(config-vpdn)# no sso enable <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 135 `；EOL ` RVA 0x356EDD00 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-227dfe0127eda54f](../../evidence/conditions-sets-014.md#c-227dfe0127eda54f) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005068

```text
(config-vpdn)# no terminate-from <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 117 `；EOL ` RVA 0x356ECF68 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ab204281ce3b474c](../../evidence/conditions-sets-066.md#c-ab204281ce3b474c) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005078

```text
(config-vpdn)# no vpn <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 125 `；EOL ` RVA 0x356F5228 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ddb2614aa41e1431](../../evidence/conditions-sets-085.md#c-ddb2614aa41e1431) · [状态效果 S-4bc2b2ebaa3c8b86](../../evidence/state_effects-sets-017.md#s-4bc2b2ebaa3c8b86)

### observed_connections-005195

```text
(config-vpdn)# pptp flow-control receive-window <number:1..64> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 91 `；EOL ` RVA 0x356F9380 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` packets。

[条件 C-c4cf8619f41e72c6](../../evidence/conditions-sets-076.md#c-c4cf8619f41e72c6) · [参数 P-43fb8406ff33f7aa](../../evidence/parameters-sets-006.md#p-43fb8406ff33f7aa)

### observed_connections-005187

```text
(config-vpdn)# pptp flow-control static-rtt <number:100..5000> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 90 `；EOL ` RVA 0x356F9090 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` milliseconds。

[条件 C-b38c0b4a47cd7ea2](../../evidence/conditions-sets-069.md#c-b38c0b4a47cd7ea2) · [参数 P-48ce1b837830b980](../../evidence/parameters-sets-006.md#p-48ce1b837830b980)

### observed_connections-005179

```text
(config-vpdn)# pptp tunnel echo <number:0..1000> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 89 `；EOL ` RVA 0x356F86C0 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds, default is 60。

[条件 C-429bdc037e73a3fd](../../evidence/conditions-sets-026.md#c-429bdc037e73a3fd) · [参数 P-95e68354ce5ab067](../../evidence/parameters-sets-012.md#p-95e68354ce5ab067)

### observed_connections-005219

```text
(config-vpdn)# pptp tunnel timeout setup <number:1..300> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 92 `；EOL ` RVA 0x356F8A18 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7f631b8146b2202](../../evidence/conditions-sets-071.md#c-b7f631b8146b2202) · [参数 P-dc1884ac42e822fb](../../evidence/parameters-sets-017.md#p-dc1884ac42e822fb)

### observed_connections-005222

```text
(config-vpdn)# pptp tunnel timeout teardown <number:1..300> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 93 `；EOL ` RVA 0x356F8D08 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6fefdc452035e240](../../evidence/conditions-sets-043.md#c-6fefdc452035e240) · [参数 P-0dfcb5c5971cac7e](../../evidence/parameters-sets-002.md#p-0dfcb5c5971cac7e)

### observed_connections-005114

```text
(config-vpdn)# redirect identifier <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 123 `；EOL ` RVA 0x356F4F08 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Redirect identifier name (31 chars max)。

[条件 C-61b1ed02f19222af](../../evidence/conditions-sets-038.md#c-61b1ed02f19222af) · [参数 P-39f40ed60f7bb01a](../../evidence/parameters-sets-005.md#p-39f40ed60f7bb01a)

### observed_connections-005171

```text
(config-vpdn)# relay pppoe bba-group <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 131 `；EOL ` RVA 0x356F7718 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` bba-group name for protocol PPPoE。

[条件 C-5cea587fcacec9cc](../../evidence/conditions-sets-036.md#c-5cea587fcacec9cc) · [参数 P-17daa55fa2275eef](../../evidence/parameters-sets-002.md#p-17daa55fa2275eef)

### observed_connections-005241

```text
(config-vpdn)# request dialin ip <address> domain <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 33 `；EOL ` RVA 0x356E9F80 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3aebde91d4fd336](../../evidence/conditions-sets-076.md#c-c3aebde91d4fd336) · [参数 P-b868f0568b639073](../../evidence/parameters-sets-014.md#p-b868f0568b639073) · [状态效果 S-3b7cdefdd6a0d80d](../../evidence/state_effects-sets-013.md#s-3b7cdefdd6a0d80d)

### observed_connections-005253

```text
(config-vpdn)# request dialout l2tp ip <address> pool-member <number:1..255> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 35 `；EOL ` RVA 0x356EA458 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-75e8af5015242f9e](../../evidence/conditions-sets-046.md#c-75e8af5015242f9e) · [参数 P-b5c15b1e6c684de5](../../evidence/parameters-sets-014.md#p-b5c15b1e6c684de5) · [状态效果 S-956e6770a0a604a5](../../evidence/state_effects-sets-032.md#s-956e6770a0a604a5)

### observed_connections-005042

```text
(config-vpdn)# request-dialin <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 100 `；EOL ` RVA 0x356FB688 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd39122bb69cabfc](../../evidence/conditions-sets-098.md#c-fd39122bb69cabfc)

### observed_connections-005044

```text
(config-vpdn)# request-dialout <cr>
```

Handler ` RVA 0x11D53E00 `；selector ` 101 `；EOL ` RVA 0x356FBC68 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aa80a94c9e27f942](../../evidence/conditions-sets-066.md#c-aa80a94c9e27f942)

### observed_connections-005047

```text
(config-vpdn)# scalability call-drops <number:1..100> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 99 `；EOL ` RVA 0x356F7FD8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of session to be dropped per second。

[条件 C-a11366dced79a75c](../../evidence/conditions-sets-062.md#c-a11366dced79a75c) · [参数 P-8474e7a525dd8fc6](../../evidence/parameters-sets-010.md#p-8474e7a525dd8fc6)

### observed_connections-005046

```text
(config-vpdn)# scalability multilink-num <number:1..8> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 98 `；EOL ` RVA 0x356F7D58 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of link interfaces to simulate per bundle。

[条件 C-356d9a1da2afba28](../../evidence/conditions-sets-021.md#c-356d9a1da2afba28) · [参数 P-53bf01b7b8b47893](../../evidence/parameters-sets-007.md#p-53bf01b7b8b47893)

### observed_connections-005088

```text
(config-vpdn)# scalability one-session-per-tunnel <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 97 `；EOL ` RVA 0x356F7D30 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e35b3e8c0b633b76](../../evidence/conditions-sets-088.md#c-e35b3e8c0b633b76)

### observed_connections-005260

```text
(config-vpdn)# scalability virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 96 `；EOL ` RVA 0x356F7AA8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Virtual Template number to clone。

[条件 C-ae340ef69cfd6913](../../evidence/conditions-sets-067.md#c-ae340ef69cfd6913) · [缺口 G-d83dd2b14580e461](../../evidence/gaps-sets-008.md#g-d83dd2b14580e461) · [参数 P-672c5dcab3e937d8](../../evidence/parameters-sets-008.md#p-672c5dcab3e937d8)

### observed_connections-005071

```text
(config-vpdn)# session-limit <number:0..65535> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 25 `；EOL ` RVA 0x356ED308 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of sessions。

[条件 C-0b0bdb2d11cd842d](../../evidence/conditions-sets-005.md#c-0b0bdb2d11cd842d) · [参数 P-a4f89b275acae104](../../evidence/parameters-sets-013.md#p-a4f89b275acae104)

### observed_connections-005086

```text
(config-vpdn)# source vpdn-template <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 30 `；EOL ` RVA 0x356F5C40 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a55a6aab6ad5c31](../../evidence/conditions-sets-017.md#c-2a55a6aab6ad5c31)

### observed_connections-005075

```text
(config-vpdn)# source-ip <address> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 70 `；EOL ` RVA 0x356F4BB8 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Source IP address。

[条件 C-539b81a4877ea213](../../evidence/conditions-sets-033.md#c-539b81a4877ea213) · [参数 P-7292032da8683166](../../evidence/parameters-sets-009.md#p-7292032da8683166)

### observed_connections-005073

```text
(config-vpdn)# sso enable <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 135 `；EOL ` RVA 0x356EDD00 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-227dfe0127eda54f](../../evidence/conditions-sets-014.md#c-227dfe0127eda54f)

### observed_connections-005102

```text
(config-vpdn)# terminate-from hostname <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 117 `；EOL ` RVA 0x356ECF68 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Remote name string。

[条件 C-371a4deec70bcf5a](../../evidence/conditions-sets-021.md#c-371a4deec70bcf5a) · [参数 P-c2fb6de2b5b1caf4](../../evidence/parameters-sets-015.md#p-c2fb6de2b5b1caf4)

### observed_connections-005117

```text
(config-vpdn)# vpn vrf <string> <cr>
```

Handler ` RVA 0x11D4B620 `；selector ` 125 `；EOL ` RVA 0x356F5228 `。

模式根 ` RVA 0x356DE448 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-e1c479ce189f8c89](../../evidence/conditions-sets-087.md#c-e1c479ce189f8c89) · [参数 P-3cf1562a011b54d3](../../evidence/parameters-sets-005.md#p-3cf1562a011b54d3) · [状态效果 S-32a8a1303db058af](../../evidence/state_effects-sets-011.md#s-32a8a1303db058af)
