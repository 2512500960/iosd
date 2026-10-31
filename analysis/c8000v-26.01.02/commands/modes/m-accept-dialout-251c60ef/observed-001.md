# accept-dialout · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009626

```text
(config-vpdn-acc-out)# default dialer <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 112 `；EOL ` RVA 0x356FD6F8 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1effcb079297321f](../../evidence/conditions-sets-012.md#c-1effcb079297321f) · [状态效果 S-1aec532ff77ffada](../../evidence/state_effects-sets-006.md#s-1aec532ff77ffada)

### observed_connections-009623

```text
(config-vpdn-acc-out)# default protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 111 `；EOL ` RVA 0x356FD3B0 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-960ba21fcccaa353](../../evidence/conditions-sets-058.md#c-960ba21fcccaa353) · [状态效果 S-1aec532ff77ffada](../../evidence/state_effects-sets-006.md#s-1aec532ff77ffada)

### observed_connections-009625

```text
(config-vpdn-acc-out)# dialer <number:0..255> <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 112 `；EOL ` RVA 0x356FD6F8 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer interface number。

[条件 C-5ece2f7b56d10b45](../../evidence/conditions-sets-037.md#c-5ece2f7b56d10b45) · [参数 P-8a0d887dbb93d01f](../../evidence/parameters-sets-011.md#p-8a0d887dbb93d01f)

### observed_connections-009620

```text
(config-vpdn-acc-out)# exit <cr>
```

Handler ` RVA 0x11D54950 `；selector ` 0 `；EOL ` RVA 0x356DF1E8 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18b21da3b48842aa](../../evidence/conditions-sets-010.md#c-18b21da3b48842aa)

### observed_connections-009624

```text
(config-vpdn-acc-out)# no dialer <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 112 `；EOL ` RVA 0x356FD6F8 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ad1a8025457ade3e](../../evidence/conditions-sets-067.md#c-ad1a8025457ade3e) · [状态效果 S-069822e965e0a3f4](../../evidence/state_effects-sets-002.md#s-069822e965e0a3f4)

### observed_connections-009621

```text
(config-vpdn-acc-out)# no protocol <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 111 `；EOL ` RVA 0x356FD3B0 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a34eabe204ff6778](../../evidence/conditions-sets-063.md#c-a34eabe204ff6778) · [状态效果 S-069822e965e0a3f4](../../evidence/state_effects-sets-002.md#s-069822e965e0a3f4)

### observed_connections-009622

```text
(config-vpdn-acc-out)# protocol l2tp <cr>
```

Handler ` RVA 0x11D4F780 `；selector ` 111 `；EOL ` RVA 0x356FD3B0 `。

模式根 ` RVA 0x356DE4E8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d2245f5b04bfda2](../../evidence/conditions-sets-011.md#c-1d2245f5b04bfda2) · [状态效果 S-4619543f9cbb5981](../../evidence/state_effects-sets-015.md#s-4619543f9cbb5981)
