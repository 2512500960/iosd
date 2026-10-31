# request-dialin · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009135

```text
(config-vpdn-req-in)# default dnis <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 113 `；EOL ` RVA 0x356FE7E8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS number or DNIS group name。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-b62459706e225098](../../evidence/parameters-sets-014.md#p-b62459706e225098) · [状态效果 S-7033c4c9d5579c4e](../../evidence/state_effects-sets-024.md#s-7033c4c9d5579c4e)

### observed_connections-009133

```text
(config-vpdn-req-in)# default domain <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 114 `；EOL ` RVA 0x356FE500 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Domain name string。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-a2ebdb196a83fa26](../../evidence/parameters-sets-012.md#p-a2ebdb196a83fa26) · [状态效果 S-7033c4c9d5579c4e](../../evidence/state_effects-sets-024.md#s-7033c4c9d5579c4e)

### observed_connections-009138

```text
(config-vpdn-req-in)# default multihop hostname <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 115 `；EOL ` RVA 0x356FEAE8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Remote hostname or tunnel ID。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-20f0ac10cce8aa8e](../../evidence/parameters-sets-003.md#p-20f0ac10cce8aa8e) · [状态效果 S-7033c4c9d5579c4e](../../evidence/state_effects-sets-024.md#s-7033c4c9d5579c4e)

### observed_connections-009126

```text
(config-vpdn-req-in)# default pool-member <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 107 `；EOL ` RVA 0x356FDEF8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a682d9789a0224b9](../../evidence/conditions-sets-064.md#c-a682d9789a0224b9) · [状态效果 S-7033c4c9d5579c4e](../../evidence/state_effects-sets-024.md#s-7033c4c9d5579c4e)

### observed_connections-009123

```text
(config-vpdn-req-in)# default protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 108 `；EOL ` RVA 0x356FDA90 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf0a60ae55111505](../../evidence/conditions-sets-080.md#c-cf0a60ae55111505) · [状态效果 S-7033c4c9d5579c4e](../../evidence/state_effects-sets-024.md#s-7033c4c9d5579c4e)

### observed_connections-009130

```text
(config-vpdn-req-in)# default rotary-group <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 106 `；EOL ` RVA 0x356FE210 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-978219a02c349ca6](../../evidence/conditions-sets-058.md#c-978219a02c349ca6) · [状态效果 S-7033c4c9d5579c4e](../../evidence/state_effects-sets-024.md#s-7033c4c9d5579c4e)

### observed_connections-009131

```text
(config-vpdn-req-in)# dnis <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 113 `；EOL ` RVA 0x356FE7E8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS number or DNIS group name。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-b62459706e225098](../../evidence/parameters-sets-014.md#p-b62459706e225098)

### observed_connections-009128

```text
(config-vpdn-req-in)# domain <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 114 `；EOL ` RVA 0x356FE500 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Domain name string。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-a2ebdb196a83fa26](../../evidence/parameters-sets-012.md#p-a2ebdb196a83fa26)

### observed_connections-009120

```text
(config-vpdn-req-in)# exit <cr>
```

Handler ` RVA 0x11D547D0 `；selector ` 0 `；EOL ` RVA 0x356DF510 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17e607c9c4a1e84b](../../evidence/conditions-sets-009.md#c-17e607c9c4a1e84b)

### observed_connections-009136

```text
(config-vpdn-req-in)# multihop hostname <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 115 `；EOL ` RVA 0x356FEAE8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Remote hostname or tunnel ID。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-20f0ac10cce8aa8e](../../evidence/parameters-sets-003.md#p-20f0ac10cce8aa8e)

### observed_connections-009134

```text
(config-vpdn-req-in)# no dnis <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 113 `；EOL ` RVA 0x356FE7E8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` DNIS number or DNIS group name。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-b62459706e225098](../../evidence/parameters-sets-014.md#p-b62459706e225098) · [状态效果 S-de36ef17efc77450](../../evidence/state_effects-sets-047.md#s-de36ef17efc77450)

### observed_connections-009132

```text
(config-vpdn-req-in)# no domain <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 114 `；EOL ` RVA 0x356FE500 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Domain name string。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-a2ebdb196a83fa26](../../evidence/parameters-sets-012.md#p-a2ebdb196a83fa26) · [状态效果 S-de36ef17efc77450](../../evidence/state_effects-sets-047.md#s-de36ef17efc77450)

### observed_connections-009137

```text
(config-vpdn-req-in)# no multihop hostname <string> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 115 `；EOL ` RVA 0x356FEAE8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Remote hostname or tunnel ID。

[条件 C-866865e8a3da90f6](../../evidence/conditions-sets-052.md#c-866865e8a3da90f6) · [参数 P-20f0ac10cce8aa8e](../../evidence/parameters-sets-003.md#p-20f0ac10cce8aa8e) · [状态效果 S-de36ef17efc77450](../../evidence/state_effects-sets-047.md#s-de36ef17efc77450)

### observed_connections-009124

```text
(config-vpdn-req-in)# no pool-member <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 107 `；EOL ` RVA 0x356FDEF8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-17a218e6339326e0](../../evidence/conditions-sets-009.md#c-17a218e6339326e0) · [状态效果 S-de36ef17efc77450](../../evidence/state_effects-sets-047.md#s-de36ef17efc77450)

### observed_connections-009121

```text
(config-vpdn-req-in)# no protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 108 `；EOL ` RVA 0x356FDA90 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f48e2e811a28a03c](../../evidence/conditions-sets-094.md#c-f48e2e811a28a03c) · [状态效果 S-de36ef17efc77450](../../evidence/state_effects-sets-047.md#s-de36ef17efc77450)

### observed_connections-009127

```text
(config-vpdn-req-in)# no rotary-group <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 106 `；EOL ` RVA 0x356FE210 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6f380e1f4dfc82eb](../../evidence/conditions-sets-043.md#c-6f380e1f4dfc82eb) · [状态效果 S-de36ef17efc77450](../../evidence/state_effects-sets-047.md#s-de36ef17efc77450)

### observed_connections-009125

```text
(config-vpdn-req-in)# pool-member <number:1..255> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 107 `；EOL ` RVA 0x356FDEF8 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer Profile pool number。

[条件 C-b5613214036303ae](../../evidence/conditions-sets-070.md#c-b5613214036303ae) · [参数 P-2f06a9e25326cc0d](../../evidence/parameters-sets-004.md#p-2f06a9e25326cc0d)

### observed_connections-009122

```text
(config-vpdn-req-in)# protocol l2tp <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 108 `；EOL ` RVA 0x356FDA90 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ea7b9e10cb773de](../../evidence/conditions-sets-006.md#c-0ea7b9e10cb773de) · [状态效果 S-3ca4afbbfbfb2626](../../evidence/state_effects-sets-013.md#s-3ca4afbbfbfb2626)

### observed_connections-009129

```text
(config-vpdn-req-in)# rotary-group <number:0..255> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 106 `；EOL ` RVA 0x356FE210 `。

模式根 ` RVA 0x356DE470 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer Rotary group number。

[条件 C-5ac15868eb23c9e5](../../evidence/conditions-sets-036.md#c-5ac15868eb23c9e5) · [参数 P-dae2d201d070b1d5](../../evidence/parameters-sets-016.md#p-dae2d201d070b1d5)

