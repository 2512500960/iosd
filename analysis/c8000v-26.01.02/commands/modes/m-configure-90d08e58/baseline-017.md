# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-058183

```text
(config)# default do-exec show ip multicast mpls mrib-client ipv4 <cr>
```

Handler ` RVA 0xF7114E0 `；selector ` 0 `；EOL ` RVA 0x3474C8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058199

```text
(config)# default do-exec show ip multicast mpls mrib-client ipv6 <cr>
```

Handler ` RVA 0xF711410 `；selector ` 0 `；EOL ` RVA 0x3474CB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054864

```text
(config)# default do-exec show ip multicast mpls vif <cr>
```

Handler ` RVA 0xF7113A0 `；selector ` 0 `；EOL ` RVA 0x3474CDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2992a11d1a58a09](../../evidence/conditions-sets-094.md#c-f2992a11d1a58a09) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058300

```text
(config)# default do-exec show ip multicast overlay-mapping lisp <address> <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 8 `；EOL ` RVA 0x3474E0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Overlay group address。

[条件 C-5d832276d20d451a](../../evidence/conditions-sets-036.md#c-5d832276d20d451a) · [参数 P-c33f2326c4cd42ed](../../evidence/parameters-sets-015.md#p-c33f2326c4cd42ed) · [状态效果 S-5d890238a650c920](../../evidence/state_effects-sets-020.md#s-5d890238a650c920)

### path-055422

```text
(config)# default do-exec show ip multicast redundancy ole <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 2 `；EOL ` RVA 0x33E52298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-46fb15a3338d2e2d](../../evidence/conditions-sets-028.md#c-46fb15a3338d2e2d) · [状态效果 S-5adefe4cff05a39c](../../evidence/state_effects-sets-020.md#s-5adefe4cff05a39c)

### path-058384

```text
(config)# default do-exec show ip multicast redundancy reachability summary <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 3 `；EOL ` RVA 0x33E51F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a278267a3443ff0](../../evidence/conditions-sets-029.md#c-4a278267a3443ff0) · [状态效果 S-db77665aa5f2bc75](../../evidence/state_effects-sets-046.md#s-db77665aa5f2bc75)

### path-055238

```text
(config)# default do-exec show ip multicast redundancy state <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 0 `；EOL ` RVA 0x33E51948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-5adefe4cff05a39c](../../evidence/state_effects-sets-020.md#s-5adefe4cff05a39c)

### path-055231

```text
(config)# default do-exec show ip multicast redundancy statistics <cr>
```

Handler ` RVA 0xD46FD80 `；selector ` 1 `；EOL ` RVA 0x33E51BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-5adefe4cff05a39c](../../evidence/state_effects-sets-020.md#s-5adefe4cff05a39c)

### path-054786

```text
(config)# default do-exec show ip multicast rpf monitored <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 3 `；EOL ` RVA 0x3474C188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059464

```text
(config)# default do-exec show ip multicast snooping limit vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 60 `；EOL ` RVA 0x33A5DEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [参数 P-236b3a3e749d1c7b](../../evidence/parameters-sets-003.md#p-236b3a3e749d1c7b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055209

```text
(config)# default do-exec show ip multicast snooping summary <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 70 `；EOL ` RVA 0x33A5E1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059472

```text
(config)# default do-exec show ip multicast snooping summary vlan <number:1..4095> <cr>
```

Handler ` RVA 0xC361C10 `；selector ` 68 `；EOL ` RVA 0x33A5E230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-5fc63bc3602ff48f](../../evidence/conditions-sets-037.md#c-5fc63bc3602ff48f) · [参数 P-0e6e0511934953b5](../../evidence/parameters-sets-002.md#p-0e6e0511934953b5) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048669

```text
(config)# default do-exec show ip multicast timer <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 7 `；EOL ` RVA 0x3474E490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-171912744b2da9bb](../../evidence/conditions-sets-009.md#c-171912744b2da9bb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048818

```text
(config)# default do-exec show ip multicast topology <cr>
```

Handler ` RVA 0xF710E60 `；selector ` 4 `；EOL ` RVA 0x3474D988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d4ef608d9b63ee89](../../evidence/conditions-sets-082.md#c-d4ef608d9b63ee89) · [状态效果 S-dc2fcb6dd3a12df5](../../evidence/state_effects-sets-047.md#s-dc2fcb6dd3a12df5)

### path-038274

```text
(config)# default do-exec show ip name-servers <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 2 `；EOL ` RVA 0x33D328D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055465

```text
(config)# default do-exec show ip nat aggregation top-100-allocator <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 9 `；EOL ` RVA 0x347DB178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0b4c84c7c32d7af9](../../evidence/conditions-sets-005.md#c-0b4c84c7c32d7af9) · [状态效果 S-3dd573aa404886c5](../../evidence/state_effects-sets-014.md#s-3dd573aa404886c5)

### path-049716

```text
(config)# default do-exec show ip nat alias-usecount <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 10 `；EOL ` RVA 0x347DC148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-38fb4afe68da981d](../../evidence/conditions-sets-022.md#c-38fb4afe68da981d) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049346

```text
(config)# default do-exec show ip nat bpa <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 5 `；EOL ` RVA 0x347DA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7028274df1d580ca](../../evidence/conditions-sets-043.md#c-7028274df1d580ca) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055580

```text
(config)# default do-exec show ip nat dia track <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 12 `；EOL ` RVA 0x347DBB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-54ffd23a7032a3ef](../../evidence/conditions-sets-033.md#c-54ffd23a7032a3ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049673

```text
(config)# default do-exec show ip nat entry-static <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 11 `；EOL ` RVA 0x347DBE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f84eae1da57a0881](../../evidence/conditions-sets-096.md#c-f84eae1da57a0881) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049794

```text
(config)# default do-exec show ip nat ha <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 0 `；EOL ` RVA 0x34CE8678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058501

```text
(config)# default do-exec show ip nat ha inside destination <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 7 `；EOL ` RVA 0x34CE71F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0e43a703bb752aad](../../evidence/conditions-sets-006.md#c-0e43a703bb752aad) · [状态效果 S-9e37be191d543471](../../evidence/state_effects-sets-034.md#s-9e37be191d543471)

### path-059909

```text
(config)# default do-exec show ip nat ha inside destination list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 6 `；EOL ` RVA 0x34CE7230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-0e43a703bb752aad](../../evidence/conditions-sets-006.md#c-0e43a703bb752aad) · [参数 P-9c7276b446f8ff6f](../../evidence/parameters-sets-012.md#p-9c7276b446f8ff6f) · [状态效果 S-9e37be191d543471](../../evidence/state_effects-sets-034.md#s-9e37be191d543471)

### path-058493

```text
(config)# default do-exec show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 3 `；EOL ` RVA 0x34CE5E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-760a5fe5ffc8a104](../../evidence/conditions-sets-046.md#c-760a5fe5ffc8a104) · [状态效果 S-af239fd7b9605453](../../evidence/state_effects-sets-037.md#s-af239fd7b9605453)

### path-058516

```text
(config)# default do-exec show ip nat ha inside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 5 `；EOL ` RVA 0x34CE6298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [状态效果 S-af239fd7b9605453](../../evidence/state_effects-sets-037.md#s-af239fd7b9605453)

### path-060103

```text
(config)# default do-exec show ip nat ha inside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 4 `；EOL ` RVA 0x34CE64A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Inside local IP address；` address ` Inside global IP address。

[条件 C-5047286dcd88b236](../../evidence/conditions-sets-031.md#c-5047286dcd88b236) · [参数 P-93cfcae875ad4313](../../evidence/parameters-sets-011.md#p-93cfcae875ad4313) · [状态效果 S-af239fd7b9605453](../../evidence/state_effects-sets-037.md#s-af239fd7b9605453)

### path-055660

```text
(config)# default do-exec show ip nat ha mappings <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 11 `；EOL ` RVA 0x34CE8650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058522

```text
(config)# default do-exec show ip nat ha outside source <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 10 `；EOL ` RVA 0x34CE7D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [状态效果 S-e98ce74ba41188dc](../../evidence/state_effects-sets-049.md#s-e98ce74ba41188dc)

### path-059911

```text
(config)# default do-exec show ip nat ha outside source list <number:1..2699> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 8 `；EOL ` RVA 0x34CE79C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Access list number for global addresses。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [参数 P-b102d76a95775281](../../evidence/parameters-sets-013.md#p-b102d76a95775281) · [状态效果 S-e98ce74ba41188dc](../../evidence/state_effects-sets-049.md#s-e98ce74ba41188dc)

### path-060101

```text
(config)# default do-exec show ip nat ha outside source static <address> <address> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 9 `；EOL ` RVA 0x34CE7F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Outside global IP address；` address ` Outside local IP address。

[条件 C-255475745bdb7c9b](../../evidence/conditions-sets-015.md#c-255475745bdb7c9b) · [参数 P-bac6837be306eb44](../../evidence/parameters-sets-014.md#p-bac6837be306eb44) · [状态效果 S-e98ce74ba41188dc](../../evidence/state_effects-sets-049.md#s-e98ce74ba41188dc)

### path-055591

```text
(config)# default do-exec show ip nat ha pool <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 2 `；EOL ` RVA 0x34CE57E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2a8a9262f1a89162](../../evidence/conditions-sets-017.md#c-2a8a9262f1a89162) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058466

```text
(config)# default do-exec show ip nat ha pool <string> <cr>
```

Handler ` RVA 0x10C06B70 `；selector ` 1 `；EOL ` RVA 0x34CE57C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Pool name。

[条件 C-2a8a9262f1a89162](../../evidence/conditions-sets-017.md#c-2a8a9262f1a89162) · [参数 P-9337e862cefa55d7](../../evidence/parameters-sets-011.md#p-9337e862cefa55d7) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055513

```text
(config)# default do-exec show ip nat limits all-host <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 4 `；EOL ` RVA 0x347DA148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-50b8bb48fe758e80](../../evidence/conditions-sets-032.md#c-50b8bb48fe758e80) · [状态效果 S-d55d9532bf9c3b6f](../../evidence/state_effects-sets-045.md#s-d55d9532bf9c3b6f)

### path-049552

```text
(config)# default do-exec show ip nat map <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 7 `；EOL ` RVA 0x347DB578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dc8f64116004688f](../../evidence/conditions-sets-085.md#c-dc8f64116004688f) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049195

```text
(config)# default do-exec show ip nat platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 3 `；EOL ` RVA 0x347D94C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055495

```text
(config)# default do-exec show ip nat pool platform <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 6 `；EOL ` RVA 0x347DADD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d794e298b82915c](../../evidence/conditions-sets-042.md#c-6d794e298b82915c) · [状态效果 S-628a569e1bd603a5](../../evidence/state_effects-sets-021.md#s-628a569e1bd603a5)

### path-055387

```text
(config)# default do-exec show ip nat portblock pat <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 2 `；EOL ` RVA 0x347D9910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aadf07f045e24108](../../evidence/conditions-sets-066.md#c-aadf07f045e24108) · [状态效果 S-c3b05c62bf2491b5](../../evidence/state_effects-sets-041.md#s-c3b05c62bf2491b5)

### path-049592

```text
(config)# default do-exec show ip nat route-dia <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 8 `；EOL ` RVA 0x347DB840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca48db494d58b37a](../../evidence/conditions-sets-078.md#c-ca48db494d58b37a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049303

```text
(config)# default do-exec show ip nat statistics <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 1 `；EOL ` RVA 0x347DA700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88bfb62346132430](../../evidence/conditions-sets-053.md#c-88bfb62346132430) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049899

```text
(config)# default do-exec show ip nat status <cr>
```

Handler ` RVA 0xFA2FB50 `；selector ` 0 `；EOL ` RVA 0x347DC440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c5343b7627bf42ff](../../evidence/conditions-sets-076.md#c-c5343b7627bf42ff) · [状态效果 S-cfa17570c39763d5](../../evidence/state_effects-sets-044.md#s-cfa17570c39763d5)

### path-049697

```text
(config)# default do-exec show ip nat translations <cr>
```

Handler ` RVA 0xFA2EB90 `；selector ` 0 `；EOL ` RVA 0x347D7750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3bb115fc3f9a9f89](../../evidence/conditions-sets-023.md#c-3bb115fc3f9a9f89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048805

```text
(config)# default do-exec show ip nbar attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 19 `；EOL ` RVA 0x35246A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049055

```text
(config)# default do-exec show ip nbar attribute-custom <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 36 `；EOL ` RVA 0x35248AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049064

```text
(config)# default do-exec show ip nbar attribute-map <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 26 `；EOL ` RVA 0x35248618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055189

```text
(config)# default do-exec show ip nbar attribute-map <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 25 `；EOL ` RVA 0x352485F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Attribute Map name。

[条件 C-15bbd038c1ed607a](../../evidence/conditions-sets-009.md#c-15bbd038c1ed607a) · [参数 P-00d2c85d1e33763e](../../evidence/parameters-sets-001.md#p-00d2c85d1e33763e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-060093

```text
(config)# default do-exec show ip nbar classification cache sync export format table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 54 `；EOL ` RVA 0x352440D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1b75c7a76044d989](../../evidence/conditions-sets-011.md#c-1b75c7a76044d989) · [状态效果 S-df40e80744a6e3ce](../../evidence/state_effects-sets-047.md#s-df40e80744a6e3ce)

### path-059890

```text
(config)# default do-exec show ip nbar classification cache sync import last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x35244498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3135ca154eb94d3](../../evidence/conditions-sets-094.md#c-f3135ca154eb94d3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058283

```text
(config)# default do-exec show ip nbar classification dns learning <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 44 `；EOL ` RVA 0x35243730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059893

```text
(config)# default do-exec show ip nbar classification dns learning cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 45 `；EOL ` RVA 0x352428C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-060086

```text
(config)# default do-exec show ip nbar classification dns learning cache <number:1..100000> unclassified <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 50 `；EOL ` RVA 0x352428A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-7e5a6912abbf67f4](../../evidence/parameters-sets-010.md#p-7e5a6912abbf67f4) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-060089

```text
(config)# default do-exec show ip nbar classification dns learning cache clients-servers <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 46 `；EOL ` RVA 0x35242E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c79de3b2a66f150c](../../evidence/parameters-sets-015.md#p-c79de3b2a66f150c) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-060088

```text
(config)# default do-exec show ip nbar classification dns learning cache ip-address <address> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 47 `；EOL ` RVA 0x35243470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d80f378e85a44dd1](../../evidence/parameters-sets-016.md#p-d80f378e85a44dd1) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059452

```text
(config)# default do-exec show ip nbar classification dns learning stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 51 `；EOL ` RVA 0x35243708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054983

```text
(config)# default do-exec show ip nbar classification granularity <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 38 `；EOL ` RVA 0x35241B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058249

```text
(config)# default do-exec show ip nbar classification granularity protocol <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 40 `；EOL ` RVA 0x35241BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058274

```text
(config)# default do-exec show ip nbar classification socket-cache <number:1..100000> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 52 `；EOL ` RVA 0x35244788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of sockets to show。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6099c4f0a96ec586](../../evidence/parameters-sets-008.md#p-6099c4f0a96ec586) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058315

```text
(config)# default do-exec show ip nbar classification socket-cache pl-sockets <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 53 `；EOL ` RVA 0x35244A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048433

```text
(config)# default do-exec show ip nbar control-plane <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 42 `；EOL ` RVA 0x35241228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055016

```text
(config)# default do-exec show ip nbar function <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 37 `；EOL ` RVA 0x35244E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Function name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d038cc713a4324ff](../../evidence/parameters-sets-016.md#p-d038cc713a4324ff) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048944

```text
(config)# default do-exec show ip nbar link-age <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 3 `；EOL ` RVA 0x35247FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054909

```text
(config)# default do-exec show ip nbar npc detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 64 `；EOL ` RVA 0x35241538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-854194c0c939e8a4](../../evidence/conditions-sets-052.md#c-854194c0c939e8a4) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054942

```text
(config)# default do-exec show ip nbar npc summary <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 65 `；EOL ` RVA 0x352417E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-72464d489fbf4778](../../evidence/conditions-sets-044.md#c-72464d489fbf4778) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055089

```text
(config)# default do-exec show ip nbar parameter extraction <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 34 `；EOL ` RVA 0x352459A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058276

```text
(config)# default do-exec show ip nbar parameter extraction activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 35 `；EOL ` RVA 0x35245980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055128

```text
(config)# default do-exec show ip nbar parameter subclassification <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 32 `；EOL ` RVA 0x352464E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058290

```text
(config)# default do-exec show ip nbar parameter subclassification activated <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 33 `；EOL ` RVA 0x352464C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048874

```text
(config)# default do-exec show ip nbar protocol-attribute <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 22 `；EOL ` RVA 0x352479E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049770

```text
(config)# default do-exec show ip nbar protocol-discovery <cr>
```

Handler ` RVA 0x10F338B0 `；selector ` 0 `；EOL ` RVA 0x3524DED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e6f7f47de2d1d824](../../evidence/conditions-sets-089.md#c-e6f7f47de2d1d824) · [状态效果 S-fcc2147b1c5361f9](../../evidence/state_effects-sets-054.md#s-fcc2147b1c5361f9)

### path-049193

```text
(config)# default do-exec show ip nbar protocol-id <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 0 `；EOL ` RVA 0x3524BA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c732dccb57f95a83](../../evidence/conditions-sets-077.md#c-c732dccb57f95a83) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055424

```text
(config)# default do-exec show ip nbar protocol-pack <string> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 12 `；EOL ` RVA 0x3524AEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058400

```text
(config)# default do-exec show ip nbar protocol-pack <string> detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 11 `；EOL ` RVA 0x3524AC10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058414

```text
(config)# default do-exec show ip nbar protocol-pack <string> taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 13 `；EOL ` RVA 0x3524AEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` NBAR protocol pack name。

[条件 C-cc4851d76a450c9a](../../evidence/conditions-sets-079.md#c-cc4851d76a450c9a) · [参数 P-ee2b771004345552](../../evidence/parameters-sets-018.md#p-ee2b771004345552) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055279

```text
(config)# default do-exec show ip nbar protocol-pack active <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 5 `；EOL ` RVA 0x35249130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058334

```text
(config)# default do-exec show ip nbar protocol-pack active detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 4 `；EOL ` RVA 0x35248E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058353

```text
(config)# default do-exec show ip nbar protocol-pack active taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 14 `；EOL ` RVA 0x35249108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055312

```text
(config)# default do-exec show ip nbar protocol-pack inactive <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 7 `；EOL ` RVA 0x35249940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058348

```text
(config)# default do-exec show ip nbar protocol-pack inactive detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 6 `；EOL ` RVA 0x35249670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058392

```text
(config)# default do-exec show ip nbar protocol-pack inactive taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 16 `；EOL ` RVA 0x352499A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059479

```text
(config)# default do-exec show ip nbar protocol-pack inactive taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 15 `；EOL ` RVA 0x35249980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` NBAR inactive protocol pack name。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [参数 P-677a9bb0ef608bac](../../evidence/parameters-sets-008.md#p-677a9bb0ef608bac) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055352

```text
(config)# default do-exec show ip nbar protocol-pack loaded <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 9 `；EOL ` RVA 0x3524A3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058367

```text
(config)# default do-exec show ip nbar protocol-pack loaded detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 8 `；EOL ` RVA 0x3524A128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058407

```text
(config)# default do-exec show ip nbar protocol-pack loaded taxonomy <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 18 `；EOL ` RVA 0x3524A460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059484

```text
(config)# default do-exec show ip nbar protocol-pack loaded taxonomy <string> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 17 `；EOL ` RVA 0x3524A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` NBAR loaded protocol pack name。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [参数 P-658de79b2d501530](../../evidence/parameters-sets-008.md#p-658de79b2d501530) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049361

```text
(config)# default do-exec show ip nbar resources <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 20 `；EOL ` RVA 0x3524C368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055399

```text
(config)# default do-exec show ip nbar resources flow <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 24 `；EOL ` RVA 0x3524C058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-85bd44377217f3f3](../../evidence/conditions-sets-052.md#c-85bd44377217f3f3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055512

```text
(config)# default do-exec show ip nbar resources status <cr>
```

Handler ` RVA 0x10F3B120 `；selector ` 19 `；EOL ` RVA 0x3524CE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058452

```text
(config)# default do-exec show ip nbar resources status <number:10..86400> <cr>
```

Handler ` RVA 0x10F219A0 `；selector ` 22 `；EOL ` RVA 0x3524CEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-49c60d7b54c4f3ee](../../evidence/parameters-sets-006.md#p-49c60d7b54c4f3ee) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059501

```text
(config)# default do-exec show ip nbar resources status <number:10..86400> <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 23 `；EOL ` RVA 0x3524CEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Specify age of links (to indicate which bucket)；` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-d71cbaf17a27d2ca](../../evidence/parameters-sets-016.md#p-d71cbaf17a27d2ca) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058443

```text
(config)# default do-exec show ip nbar resources status fadebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 24 `；EOL ` RVA 0x3524C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059496

```text
(config)# default do-exec show ip nbar resources status fadebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 25 `；EOL ` RVA 0x3524C968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-663e50933124a4cf](../../evidence/parameters-sets-008.md#p-663e50933124a4cf) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058431

```text
(config)# default do-exec show ip nbar resources status freebucket <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 26 `；EOL ` RVA 0x3524C438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059494

```text
(config)# default do-exec show ip nbar resources status freebucket <number:1..50> <cr>
```

Handler ` RVA 0x10F21F60 `；selector ` 27 `；EOL ` RVA 0x3524C410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of links to view。

[条件 C-7aaa3653baa5e431](../../evidence/conditions-sets-048.md#c-7aaa3653baa5e431) · [参数 P-911a5d92236ca3a7](../../evidence/parameters-sets-011.md#p-911a5d92236ca3a7) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049139

```text
(config)# default do-exec show ip nbar statistics <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 27 `；EOL ` RVA 0x3524B6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cbfce9c3d822aac3](../../evidence/conditions-sets-078.md#c-cbfce9c3d822aac3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049056

```text
(config)# default do-exec show ip nbar version <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 1 `；EOL ` RVA 0x3524B3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b60cb66f0ecc6c89](../../evidence/conditions-sets-070.md#c-b60cb66f0ecc6c89) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040876

```text
(config)# default do-exec show ip nhrp <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 0 `；EOL ` RVA 0x347F2000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-12bcabe6c53f20cb](../../evidence/conditions-sets-007.md#c-12bcabe6c53f20cb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049399

```text
(config)# default do-exec show ip nhrp attribute <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 16 `；EOL ` RVA 0x347F5C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049511

```text
(config)# default do-exec show ip nhrp instances <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 20 `；EOL ` RVA 0x347F5F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-770e74c752988f72](../../evidence/conditions-sets-046.md#c-770e74c752988f72) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049469

```text
(config)# default do-exec show ip nhrp map <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 17 `；EOL ` RVA 0x347F5968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a94bf2d8f05cab4e](../../evidence/conditions-sets-065.md#c-a94bf2d8f05cab4e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049566

```text
(config)# default do-exec show ip nhrp multicast <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 4 `；EOL ` RVA 0x347F5548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7e510ef18eef196c](../../evidence/conditions-sets-049.md#c-7e510ef18eef196c) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049476

```text
(config)# default do-exec show ip nhrp nhs <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 3 `；EOL ` RVA 0x347F4350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055575

```text
(config)# default do-exec show ip nhrp nhs redundancy <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 10 `；EOL ` RVA 0x347F4EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059502

```text
(config)# default do-exec show ip nhrp nhs redundancy cluster <number:0..10> <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 14 `；EOL ` RVA 0x347F4958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` NHS cluster number。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [参数 P-133a9e4b186bdac7](../../evidence/parameters-sets-002.md#p-133a9e4b186bdac7) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058455

```text
(config)# default do-exec show ip nhrp nhs redundancy preempted <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 12 `；EOL ` RVA 0x347F4BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058439

```text
(config)# default do-exec show ip nhrp nhs redundancy running <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 11 `；EOL ` RVA 0x347F4648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058462

```text
(config)# default do-exec show ip nhrp nhs redundancy waiting <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 13 `；EOL ` RVA 0x347F4E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dfc4c5caa34e67fb](../../evidence/conditions-sets-086.md#c-dfc4c5caa34e67fb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049178

```text
(config)# default do-exec show ip nhrp purge <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 2 `；EOL ` RVA 0x347F3F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049683

```text
(config)# default do-exec show ip nhrp redirect <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 6 `；EOL ` RVA 0x347F1958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055579

```text
(config)# default do-exec show ip nhrp redirect statistics <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 7 `；EOL ` RVA 0x347F1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049672

```text
(config)# default do-exec show ip nhrp shortcut <cr>
```

Handler ` RVA 0x108FE580 `；selector ` 0 `；EOL ` RVA 0x34BF8EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-85508f070ba2cbd4](../../evidence/state_effects-sets-028.md#s-85508f070ba2cbd4)

### path-049482

```text
(config)# default do-exec show ip nhrp stats <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 18 `；EOL ` RVA 0x347F3B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-50ed8a211b890947](../../evidence/conditions-sets-032.md#c-50ed8a211b890947) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049249

```text
(config)# default do-exec show ip nhrp traffic <cr>
```

Handler ` RVA 0xFAB4590 `；selector ` 1 `；EOL ` RVA 0x347F3670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040877

```text
(config)# default do-exec show ip ospf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 7 `；EOL ` RVA 0x34892168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a5803a3a1c9b578](../../evidence/conditions-sets-010.md#c-1a5803a3a1c9b578) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048841

```text
(config)# default do-exec show ip ospf bad-checksum <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 1 `；EOL ` RVA 0x3487AD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049474

```text
(config)# default do-exec show ip ospf border-routers <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 17 `；EOL ` RVA 0x348788A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050125

```text
(config)# default do-exec show ip ospf database <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 58 `；EOL ` RVA 0x34895630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-264cdf48d35a5449](../../evidence/conditions-sets-015.md#c-264cdf48d35a5449) · [状态效果 S-d31837c565ffbe5d](../../evidence/state_effects-sets-045.md#s-d31837c565ffbe5d)

### path-055823

```text
(config)# default do-exec show ip ospf database database-summary <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 60 `；EOL ` RVA 0x34896290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f09beff6301b7c5](../../evidence/conditions-sets-037.md#c-5f09beff6301b7c5) · [状态效果 S-d31837c565ffbe5d](../../evidence/state_effects-sets-045.md#s-d31837c565ffbe5d)

### path-058613

```text
(config)# default do-exec show ip ospf database database-summary detail <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 54 `；EOL ` RVA 0x348965B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a8c31475b28564f](../../evidence/conditions-sets-004.md#c-0a8c31475b28564f) · [状态效果 S-a0bb62c009b0cc94](../../evidence/state_effects-sets-034.md#s-a0bb62c009b0cc94)

### path-049731

```text
(config)# default do-exec show ip ospf delete-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 57 `；EOL ` RVA 0x34876370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049008

```text
(config)# default do-exec show ip ospf events <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 16 `；EOL ` RVA 0x348769F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d601d8d07dd98107](../../evidence/conditions-sets-083.md#c-d601d8d07dd98107) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049918

```text
(config)# default do-exec show ip ospf flood-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 66 `；EOL ` RVA 0x34890B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-654fe22627967429](../../evidence/conditions-sets-039.md#c-654fe22627967429) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049941

```text
(config)# default do-exec show ip ospf interface <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 65 `；EOL ` RVA 0x3488FEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64e9a11a490d9d30](../../evidence/conditions-sets-039.md#c-64e9a11a490d9d30) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055800

```text
(config)# default do-exec show ip ospf internal forwarding-addresses <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 23 `；EOL ` RVA 0x34891EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058572

```text
(config)# default do-exec show ip ospf internal memory cache <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 2 `；EOL ` RVA 0x34891C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049557

```text
(config)# default do-exec show ip ospf max-metric <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 10 `；EOL ` RVA 0x34879EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049504

```text
(config)# default do-exec show ip ospf maxage-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 9 `；EOL ` RVA 0x3487A410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058517

```text
(config)# default do-exec show ip ospf mpls traffic-eng link <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 61 `；EOL ` RVA 0x3488F830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-bacfb1d4eea55677](../../evidence/state_effects-sets-039.md#s-bacfb1d4eea55677)

### path-049136

```text
(config)# default do-exec show ip ospf multi-area <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 68 `；EOL ` RVA 0x348775F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b28cfdb94256e16e](../../evidence/conditions-sets-069.md#c-b28cfdb94256e16e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050090

```text
(config)# default do-exec show ip ospf neighbor <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 71 `；EOL ` RVA 0x34890EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e3d10944cffa4e82](../../evidence/conditions-sets-088.md#c-e3d10944cffa4e82) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049192

```text
(config)# default do-exec show ip ospf nsf <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 14 `；EOL ` RVA 0x34877900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049762

```text
(config)# default do-exec show ip ospf nsr <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 20 `；EOL ` RVA 0x33FC8EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055601

```text
(config)# default do-exec show ip ospf nsr objects <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 21 `；EOL ` RVA 0x33FC8C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055629

```text
(config)# default do-exec show ip ospf nsr statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 22 `；EOL ` RVA 0x33FC8EC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050013

```text
(config)# default do-exec show ip ospf request-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 73 `；EOL ` RVA 0x34891878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-116bd051b88ca966](../../evidence/conditions-sets-007.md#c-116bd051b88ca966) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049986

```text
(config)# default do-exec show ip ospf retransmission-list <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 72 `；EOL ` RVA 0x34891490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7a1c7bd5caef7f01](../../evidence/conditions-sets-047.md#c-7a1c7bd5caef7f01) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049651

```text
(config)# default do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 19 `；EOL ` RVA 0x34879088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9a2d99c305604a87](../../evidence/conditions-sets-060.md#c-9a2d99c305604a87) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049652

```text
(config)# default do-exec show ip ospf rib <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 18 `；EOL ` RVA 0x34879308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ea467d44a1139b0](../../evidence/conditions-sets-018.md#c-2ea467d44a1139b0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049050

```text
(config)# default do-exec show ip ospf sham-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 6 `；EOL ` RVA 0x34877308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049562

```text
(config)# default do-exec show ip ospf statistics <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 11 `；EOL ` RVA 0x34879890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049366

```text
(config)# default do-exec show ip ospf summary-address <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 8 `；EOL ` RVA 0x34878228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055330

```text
(config)# default do-exec show ip ospf timers lsa-group <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 12 `；EOL ` RVA 0x34877C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055372

```text
(config)# default do-exec show ip ospf timers rate-limit <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 13 `；EOL ` RVA 0x34877EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049647

```text
(config)# default do-exec show ip ospf topology-info <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 15 `；EOL ` RVA 0x3487A778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d236fddacacd7923](../../evidence/conditions-sets-081.md#c-d236fddacacd7923) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049920

```text
(config)# default do-exec show ip ospf traffic <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 67 `；EOL ` RVA 0x34890680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-174a88fc5073a64c](../../evidence/conditions-sets-009.md#c-174a88fc5073a64c) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049107

```text
(config)# default do-exec show ip ospf virtual-links <cr>
```

Handler ` RVA 0xFCD13D0 `；selector ` 5 `；EOL ` RVA 0x34876DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048783

```text
(config)# default do-exec show ip pim autorp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 46 `；EOL ` RVA 0x34753198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058470

```text
(config)# default do-exec show ip pim bfd neighbor inactive <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 0 `；EOL ` RVA 0x33A9C0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ddaf11059e672b92](../../evidence/conditions-sets-085.md#c-ddaf11059e672b92) · [状态效果 S-80c0a1a04a51fa93](../../evidence/state_effects-sets-027.md#s-80c0a1a04a51fa93)

### path-048850

```text
(config)# default do-exec show ip pim bsr-router <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 20 `；EOL ` RVA 0x34753440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055311

```text
(config)# default do-exec show ip pim drlb gdr-candidates <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 79 `；EOL ` RVA 0x34754128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-434c17223087681a](../../evidence/conditions-sets-026.md#c-434c17223087681a) · [状态效果 S-018a603421c8950e](../../evidence/state_effects-sets-001.md#s-018a603421c8950e)

### path-049351

```text
(config)# default do-exec show ip pim gir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 87 `；EOL ` RVA 0x34756200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c79cdeeb16a0a23a](../../evidence/conditions-sets-077.md#c-c79cdeeb16a0a23a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049617

```text
(config)# default do-exec show ip pim interface <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 12 `；EOL ` RVA 0x347558F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055639

```text
(config)# default do-exec show ip pim interface bfd <cr>
```

Handler ` RVA 0xC4A31B0 `；selector ` 1 `；EOL ` RVA 0x33A9C488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d8f0ef3346d04137](../../evidence/conditions-sets-084.md#c-d8f0ef3346d04137) · [状态效果 S-ffb1e11332c518b4](../../evidence/state_effects-sets-054.md#s-ffb1e11332c518b4)

### path-055443

```text
(config)# default do-exec show ip pim interface detail <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 39 `；EOL ` RVA 0x34755648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055410

```text
(config)# default do-exec show ip pim interface traffic <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 96 `；EOL ` RVA 0x347553A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-07a68833af1a33e6](../../evidence/conditions-sets-003.md#c-07a68833af1a33e6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049818

```text
(config)# default do-exec show ip pim mdt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 0 `；EOL ` RVA 0x3478DCC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-055714

```text
(config)# default do-exec show ip pim mdt bgp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 1 `；EOL ` RVA 0x3478BB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058513

```text
(config)# default do-exec show ip pim mdt bgp c-mroutes <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 6 `；EOL ` RVA 0x3478B838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf077db1e2ed5988](../../evidence/conditions-sets-080.md#c-cf077db1e2ed5988) · [状态效果 S-eec0ba11e4c4cc6a](../../evidence/state_effects-sets-050.md#s-eec0ba11e4c4cc6a)

### path-059507

```text
(config)# default do-exec show ip pim mdt history interval <number:1..71582> <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 2 `；EOL ` RVA 0x3478B440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` in minutes, maximum is 71582 minutes (7 weeks)。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [参数 P-e84d14ee7ea2ba12](../../evidence/parameters-sets-017.md#p-e84d14ee7ea2ba12) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058518

```text
(config)# default do-exec show ip pim mdt internal bier <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 10 `；EOL ` RVA 0x3478C440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6db24216c4fdc7ec](../../evidence/conditions-sets-042.md#c-6db24216c4fdc7ec) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058546

```text
(config)# default do-exec show ip pim mdt internal crt <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 11 `；EOL ` RVA 0x3478CEE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7bbaed72ce0a43ad](../../evidence/conditions-sets-048.md#c-7bbaed72ce0a43ad) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058511

```text
(config)# default do-exec show ip pim mdt internal gre <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 7 `；EOL ` RVA 0x3478C198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f2b4ac5100bf9f7f](../../evidence/conditions-sets-094.md#c-f2b4ac5100bf9f7f) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058523

```text
(config)# default do-exec show ip pim mdt internal ir <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 9 `；EOL ` RVA 0x3478C6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c16359b8e05cadd8](../../evidence/conditions-sets-075.md#c-c16359b8e05cadd8) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058529

```text
(config)# default do-exec show ip pim mdt internal leaf-ad <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 15 `；EOL ` RVA 0x3478C990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5c211cb049c339b](../../evidence/conditions-sets-095.md#c-f5c211cb049c339b) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058536

```text
(config)# default do-exec show ip pim mdt internal mldp <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 8 `；EOL ` RVA 0x3478CC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ddc67b17a015de2e](../../evidence/conditions-sets-085.md#c-ddc67b17a015de2e) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058583

```text
(config)# default do-exec show ip pim mdt internal pe <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 12 `；EOL ` RVA 0x3478D498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-76cae2930b2d3c49](../../evidence/conditions-sets-046.md#c-76cae2930b2d3c49) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-059526

```text
(config)# default do-exec show ip pim mdt internal pe all <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 14 `；EOL ` RVA 0x3478D740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-96f6f37effc35394](../../evidence/conditions-sets-058.md#c-96f6f37effc35394) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058556

```text
(config)# default do-exec show ip pim mdt internal replication <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 16 `；EOL ` RVA 0x3478D188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-742fb4ffa38ff317](../../evidence/conditions-sets-045.md#c-742fb4ffa38ff317) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058580

```text
(config)# default do-exec show ip pim mdt internal tdb <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 13 `；EOL ` RVA 0x3478D9D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-16dedd191bd5cbdd](../../evidence/conditions-sets-009.md#c-16dedd191bd5cbdd) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058499

```text
(config)# default do-exec show ip pim mdt internal vxlan <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 24 `；EOL ` RVA 0x3478BEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-acd2dbb27d204214](../../evidence/conditions-sets-067.md#c-acd2dbb27d204214) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-055615

```text
(config)# default do-exec show ip pim mdt receive <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 3 `；EOL ` RVA 0x3478AEC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-058475

```text
(config)# default do-exec show ip pim mdt receive detail <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 4 `；EOL ` RVA 0x3478AEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-055569

```text
(config)# default do-exec show ip pim mdt send <cr>
```

Handler ` RVA 0xF963AF0 `；selector ` 5 `；EOL ` RVA 0x3478AB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef425f477cec0d28](../../evidence/conditions-sets-092.md#c-ef425f477cec0d28) · [状态效果 S-fb3e119c49cdfb74](../../evidence/state_effects-sets-053.md#s-fb3e119c49cdfb74)

### path-049321

```text
(config)# default do-exec show ip pim mvpn <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 52 `；EOL ` RVA 0x34752B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055344

```text
(config)# default do-exec show ip pim mvpn bier <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 89 `；EOL ` RVA 0x34752840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055115

```text
(config)# default do-exec show ip pim mvpn crt <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 70 `；EOL ` RVA 0x34751850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055306

```text
(config)# default do-exec show ip pim mvpn gre <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 90 `；EOL ` RVA 0x34752598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055273

```text
(config)# default do-exec show ip pim mvpn ir <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 91 `；EOL ` RVA 0x347522F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055202

```text
(config)# default do-exec show ip pim mvpn leaf-ad <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 92 `；EOL ` RVA 0x34751DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055035

```text
(config)# default do-exec show ip pim mvpn mldp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 68 `；EOL ` RVA 0x34751300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055075

```text
(config)# default do-exec show ip pim mvpn pe <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 69 `；EOL ` RVA 0x347515A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055158

```text
(config)# default do-exec show ip pim mvpn replication <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 93 `；EOL ` RVA 0x34751AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055236

```text
(config)# default do-exec show ip pim mvpn srv6 <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 97 `；EOL ` RVA 0x34752048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055383

```text
(config)# default do-exec show ip pim mvpn tdb <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 94 `；EOL ` RVA 0x34752AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054993

```text
(config)# default do-exec show ip pim mvpn vxlan <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 95 `；EOL ` RVA 0x34751058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048952

```text
(config)# default do-exec show ip pim neighbor <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 10 `；EOL ` RVA 0x347710F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-51b0d38796dd21f0](../../evidence/conditions-sets-032.md#c-51b0d38796dd21f0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055188

```text
(config)# default do-exec show ip pim pfp-sa announcements <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 83 `；EOL ` RVA 0x34753790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055269

```text
(config)# default do-exec show ip pim pfp-sa cache <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 86 `；EOL ` RVA 0x34753CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055230

```text
(config)# default do-exec show ip pim pfp-sa originator <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 84 `；EOL ` RVA 0x34753A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a757d600e7b7aab8](../../evidence/conditions-sets-065.md#c-a757d600e7b7aab8) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049317

```text
(config)# default do-exec show ip pim rp <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 11 `；EOL ` RVA 0x34754BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa560e3937bdf339](../../evidence/conditions-sets-097.md#c-fa560e3937bdf339) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055293

```text
(config)# default do-exec show ip pim rp-hash <address> <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 22 `；EOL ` RVA 0x34754FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` group address。

[条件 C-6dbd6590a9eb7383](../../evidence/conditions-sets-042.md#c-6dbd6590a9eb7383) · [参数 P-c66d3e1e0ed7b695](../../evidence/parameters-sets-015.md#p-c66d3e1e0ed7b695) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049314

```text
(config)# default do-exec show ip pim tunnel <cr>
```

Handler ` RVA 0xF81E530 `；selector ` 55 `；EOL ` RVA 0x347547A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9bb185ecd494e32d](../../evidence/conditions-sets-060.md#c-9bb185ecd494e32d) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040149

```text
(config)# default do-exec show ip policy <cr>
```

Handler ` RVA 0xFAD9620 `；selector ` 0 `；EOL ` RVA 0x34804A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049117

```text
(config)# default do-exec show ip policy adj-subblock <cr>
```

Handler ` RVA 0xFAD9440 `；selector ` 0 `；EOL ` RVA 0x34804A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-039239

```text
(config)# default do-exec show ip policy-list <cr>
```

Handler ` RVA 0xE218540 `；selector ` 0 `；EOL ` RVA 0x344BABE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059417

```text
(config)# default do-exec show ip portbundle ip <address> bundle <number:1..65535> <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 0 `；EOL ` RVA 0x356A5148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Portbundle IP address；` unsigned_number ` Portbundle bundle number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-81af61e5ba4224a6](../../evidence/parameters-sets-010.md#p-81af61e5ba4224a6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047983

```text
(config)# default do-exec show ip portbundle status <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 1 `；EOL ` RVA 0x356A4DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054610

```text
(config)# default do-exec show ip portbundle status free <cr>
```

Handler ` RVA 0x11C31540 `；selector ` 2 `；EOL ` RVA 0x356A4B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e96378ec1c59be63](../../evidence/state_effects-sets-049.md#s-e96378ec1c59be63)

### path-048090

```text
(config)# default do-exec show ip ports all <cr>
```

Handler ` RVA 0xCE51730 `；selector ` 0 `；EOL ` RVA 0x33CF6FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048041

```text
(config)# default do-exec show ip ports ephemeral-max <cr>
```

Handler ` RVA 0xCDEFA80 `；selector ` 0 `；EOL ` RVA 0x33CF6D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048135

```text
(config)# default do-exec show ip ports reservation <cr>
```

Handler ` RVA 0xCE518D0 `；selector ` 0 `；EOL ` RVA 0x33CF7250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c6a825157ac462ea](../../evidence/conditions-sets-077.md#c-c6a825157ac462ea) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040630

```text
(config)# default do-exec show ip prefix-list <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 0 `；EOL ` RVA 0x342832B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ddcaf979b496d8fc](../../evidence/conditions-sets-085.md#c-ddcaf979b496d8fc) · [状态效果 S-1b3ddb4c6a81dd7b](../../evidence/state_effects-sets-006.md#s-1b3ddb4c6a81dd7b)

### path-058509

```text
(config)# default do-exec show ip prefix-list <string> seq <number:1..4294967295> <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 3 `；EOL ` RVA 0x34283358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of a prefix list；` unsigned_number ` Sequence number。

[条件 C-ddcaf979b496d8fc](../../evidence/conditions-sets-085.md#c-ddcaf979b496d8fc) · [参数 P-0d71bd8044f6fc2b](../../evidence/parameters-sets-001.md#p-0d71bd8044f6fc2b) · [状态效果 S-1b3ddb4c6a81dd7b](../../evidence/state_effects-sets-006.md#s-1b3ddb4c6a81dd7b)

### path-049754

```text
(config)# default do-exec show ip prefix-list detail <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 2 `；EOL ` RVA 0x34282FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1b3ddb4c6a81dd7b](../../evidence/state_effects-sets-006.md#s-1b3ddb4c6a81dd7b)

### path-049721

```text
(config)# default do-exec show ip prefix-list summary <cr>
```

Handler ` RVA 0xE2203B0 `；selector ` 1 `；EOL ` RVA 0x34282CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1b3ddb4c6a81dd7b](../../evidence/state_effects-sets-006.md#s-1b3ddb4c6a81dd7b)

### path-039285

```text
(config)# default do-exec show ip protocols <cr>
```

Handler ` RVA 0xE1F60E0 `；selector ` 0 `；EOL ` RVA 0x3422FAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-662dab67c3ad9644](../../evidence/conditions-sets-039.md#c-662dab67c3ad9644) · [状态效果 S-b9239cadeab40961](../../evidence/state_effects-sets-039.md#s-b9239cadeab40961)

### path-048224

```text
(config)# default do-exec show ip protocols summary <cr>
```

Handler ` RVA 0xE1F5DF0 `；selector ` 0 `；EOL ` RVA 0x3422FA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-662dab67c3ad9644](../../evidence/conditions-sets-039.md#c-662dab67c3ad9644) · [状态效果 S-b9239cadeab40961](../../evidence/state_effects-sets-039.md#s-b9239cadeab40961)

### path-038105

```text
(config)# default do-exec show ip redirects <cr>
```

Handler ` RVA 0xCF509C0 `；selector ` 0 `；EOL ` RVA 0x33D31570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048276

```text
(config)# default do-exec show ip rib database <cr>
```

Handler ` RVA 0xDC0B310 `；selector ` 1 `；EOL ` RVA 0x3422F578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-aa3e36e3194bcd23](../../evidence/conditions-sets-066.md#c-aa3e36e3194bcd23) · [状态效果 S-0287c8f4942b769a](../../evidence/state_effects-sets-001.md#s-0287c8f4942b769a)

### path-049365

```text
(config)# default do-exec show ip rip database <cr>
```

Handler ` RVA 0xFB73AB0 `；selector ` 0 `；EOL ` RVA 0x34822820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c00b49cbd29f681](../../evidence/conditions-sets-048.md#c-7c00b49cbd29f681) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049341

```text
(config)# default do-exec show ip rip neighbors <cr>
```

Handler ` RVA 0xFB52AC0 `；selector ` 0 `；EOL ` RVA 0x34822B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-662365bd75b0a5eb](../../evidence/conditions-sets-039.md#c-662365bd75b0a5eb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049168

```text
(config)# default do-exec show ip rip timers <cr>
```

Handler ` RVA 0xFB56CB0 `；selector ` 0 `；EOL ` RVA 0x34822428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054823

```text
(config)# default do-exec show ip route list <number:1..199> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 12 `；EOL ` RVA 0x34230C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IP access list number。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [参数 P-6f46a0106e78d96b](../../evidence/parameters-sets-009.md#p-6f46a0106e78d96b) · [状态效果 S-e1dd26f7fb4ac43e](../../evidence/state_effects-sets-048.md#s-e1dd26f7fb4ac43e)

### path-054886

```text
(config)# default do-exec show ip route omp-tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 15 `；EOL ` RVA 0x34231420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Management Protocol (OMP) Tag value。

[条件 C-bfe07068749ae3df](../../evidence/conditions-sets-074.md#c-bfe07068749ae3df) · [参数 P-1586b2be9da07e52](../../evidence/parameters-sets-002.md#p-1586b2be9da07e52) · [状态效果 S-e1dd26f7fb4ac43e](../../evidence/state_effects-sets-048.md#s-e1dd26f7fb4ac43e)

### path-054885

```text
(config)# default do-exec show ip route tag <number:0..4294967295> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 14 `；EOL ` RVA 0x34231000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tag value。

[条件 C-247403f934361232](../../evidence/conditions-sets-014.md#c-247403f934361232) · [参数 P-e0210763947c7838](../../evidence/parameters-sets-017.md#p-e0210763947c7838) · [状态效果 S-e1dd26f7fb4ac43e](../../evidence/state_effects-sets-048.md#s-e1dd26f7fb4ac43e)

### path-058184

```text
(config)# default do-exec show ip route tree <address> <address> <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 3 `；EOL ` RVA 0x34230700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Network to display information about；` address ` Network mask。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [参数 P-3c5f288fee4ae5f4](../../evidence/parameters-sets-005.md#p-3c5f288fee4ae5f4) · [状态效果 S-e1dd26f7fb4ac43e](../../evidence/state_effects-sets-048.md#s-e1dd26f7fb4ac43e)

### path-048418

```text
(config)# default do-exec show ip route tree <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 1 `；EOL ` RVA 0x342306C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [状态效果 S-e1dd26f7fb4ac43e](../../evidence/state_effects-sets-048.md#s-e1dd26f7fb4ac43e)

### path-054797

```text
(config)# default do-exec show ip route tree summary <cr>
```

Handler ` RVA 0xE1CEA80 `；selector ` 2 `；EOL ` RVA 0x342303F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ccae3c6fa6a19008](../../evidence/conditions-sets-079.md#c-ccae3c6fa6a19008) · [状态效果 S-e1dd26f7fb4ac43e](../../evidence/state_effects-sets-048.md#s-e1dd26f7fb4ac43e)

### path-048566

```text
(config)# default do-exec show ip rpf queued <cr>
```

Handler ` RVA 0xF740240 `；selector ` 0 `；EOL ` RVA 0x34750190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7f172e32cfc78a0](../../evidence/conditions-sets-096.md#c-f7f172e32cfc78a0) · [状态效果 S-6f7bfdf7fe56e532](../../evidence/state_effects-sets-024.md#s-6f7bfdf7fe56e532)

### path-040973

```text
(config)# default do-exec show ip rsvp <cr>
```

Handler ` RVA 0x10073190 `；selector ` 0 `；EOL ` RVA 0x34A3A428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5e6a7f2c6539d6b3](../../evidence/conditions-sets-037.md#c-5e6a7f2c6539d6b3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055574

```text
(config)# default do-exec show ip rsvp aggregation ip <cr>
```

Handler ` RVA 0x101C49F0 `；selector ` 0 `；EOL ` RVA 0x34A69C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058507

```text
(config)# default do-exec show ip rsvp aggregation ip endpoints <cr>
```

Handler ` RVA 0x101C42E0 `；selector ` 0 `；EOL ` RVA 0x34A69F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058479

```text
(config)# default do-exec show ip rsvp aggregation ip interface <cr>
```

Handler ` RVA 0x101C4050 `；selector ` 0 `；EOL ` RVA 0x34A69970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-77f9e62a2b300c22](../../evidence/conditions-sets-047.md#c-77f9e62a2b300c22) · [状态效果 S-ac73483175b373cc](../../evidence/state_effects-sets-036.md#s-ac73483175b373cc)

### path-058449

```text
(config)# default do-exec show ip rsvp aggregation ip map <cr>
```

Handler ` RVA 0x101C3C20 `；selector ` 0 `；EOL ` RVA 0x34A691B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058457

```text
(config)# default do-exec show ip rsvp aggregation ip reservation <cr>
```

Handler ` RVA 0x101C3DE0 `；selector ` 0 `；EOL ` RVA 0x34A694F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049985

```text
(config)# default do-exec show ip rsvp atm-peak-rate-limit <cr>
```

Handler ` RVA 0x100542A0 `；selector ` 0 `；EOL ` RVA 0x34A34388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b6c5c4cc381f4a1f](../../evidence/conditions-sets-071.md#c-b6c5c4cc381f4a1f) · [状态效果 S-a273524ac9e014a8](../../evidence/state_effects-sets-034.md#s-a273524ac9e014a8)

### path-049559

```text
(config)# default do-exec show ip rsvp authentication <cr>
```

Handler ` RVA 0x10073FB0 `；selector ` 0 `；EOL ` RVA 0x34A2FFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050124

```text
(config)# default do-exec show ip rsvp counters <cr>
```

Handler ` RVA 0x100B61F0 `；selector ` 0 `；EOL ` RVA 0x34A35FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-b325d4e7f880db7b](../../evidence/state_effects-sets-038.md#s-b325d4e7f880db7b)

### path-049917

```text
(config)# default do-exec show ip rsvp handles <cr>
```

Handler ` RVA 0x10070450 `；selector ` 0 `；EOL ` RVA 0x34A34000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f6ac0974c487853d](../../evidence/conditions-sets-095.md#c-f6ac0974c487853d) · [状态效果 S-5fbaaa1e6b6804e6](../../evidence/state_effects-sets-021.md#s-5fbaaa1e6b6804e6)

### path-050178

```text
(config)# default do-exec show ip rsvp hello <cr>
```

Handler ` RVA 0x10072260 `；selector ` 0 `；EOL ` RVA 0x34A38728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-73e1ff93bbad3fdc](../../evidence/conditions-sets-045.md#c-73e1ff93bbad3fdc) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058655

```text
(config)# default do-exec show ip rsvp hello bfd nbr <cr>
```

Handler ` RVA 0x10076740 `；selector ` 0 `；EOL ` RVA 0x34A37650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec7faa639c22b742](../../evidence/conditions-sets-091.md#c-ec7faa639c22b742) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059551

```text
(config)# default do-exec show ip rsvp hello bfd nbr detail <cr>
```

Handler ` RVA 0x10076940 `；selector ` 0 `；EOL ` RVA 0x34A37348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec7faa639c22b742](../../evidence/conditions-sets-091.md#c-ec7faa639c22b742) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059557

```text
(config)# default do-exec show ip rsvp hello client lsp detail <cr>
```

Handler ` RVA 0x10076EA0 `；selector ` 0 `；EOL ` RVA 0x34A38108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059556

```text
(config)# default do-exec show ip rsvp hello client lsp summary <cr>
```

Handler ` RVA 0x10076D20 `；selector ` 0 `；EOL ` RVA 0x34A38410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058662

```text
(config)# default do-exec show ip rsvp hello client nbr <cr>
```

Handler ` RVA 0x10076A40 `；selector ` 0 `；EOL ` RVA 0x34A37DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059554

```text
(config)# default do-exec show ip rsvp hello client nbr detail <cr>
```

Handler ` RVA 0x10076C10 `；selector ` 0 `；EOL ` RVA 0x34A37A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cf0f65375dcb14e](../../evidence/conditions-sets-018.md#c-2cf0f65375dcb14e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055929

```text
(config)# default do-exec show ip rsvp hello graceful-restart <cr>
```

Handler ` RVA 0x10073050 `；selector ` 0 `；EOL ` RVA 0x34A38700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e789b95db429da7](../../evidence/conditions-sets-061.md#c-9e789b95db429da7) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058626

```text
(config)# default do-exec show ip rsvp hello instance internal <cr>
```

Handler ` RVA 0x10076620 `；selector ` 0 `；EOL ` RVA 0x34A368E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eb6da402bd619e6](../../evidence/conditions-sets-018.md#c-2eb6da402bd619e6) · [状态效果 S-7445fae6add33ee0](../../evidence/state_effects-sets-025.md#s-7445fae6add33ee0)

### path-058636

```text
(config)# default do-exec show ip rsvp hello instance summary <cr>
```

Handler ` RVA 0x10076290 `；selector ` 0 `；EOL ` RVA 0x34A36C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eb6da402bd619e6](../../evidence/conditions-sets-018.md#c-2eb6da402bd619e6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055874

```text
(config)# default do-exec show ip rsvp hello statistics <cr>
```

Handler ` RVA 0x100761D0 `；selector ` 0 `；EOL ` RVA 0x34A36F28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7dad2cd3040acf55](../../evidence/conditions-sets-049.md#c-7dad2cd3040acf55) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055882

```text
(config)# default do-exec show ip rsvp host receivers <cr>
```

Handler ` RVA 0x1006D010 `；selector ` 0 `；EOL ` RVA 0x34A35B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-39d6a432d7818418](../../evidence/state_effects-sets-013.md#s-39d6a432d7818418)

### path-055860

```text
(config)# default do-exec show ip rsvp host senders <cr>
```

Handler ` RVA 0x1006D750 `；selector ` 0 `；EOL ` RVA 0x34A358A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-7b09cff0ea041db2](../../evidence/state_effects-sets-026.md#s-7b09cff0ea041db2)

### path-049963

```text
(config)# default do-exec show ip rsvp installed <cr>
```

Handler ` RVA 0x1006B120 `；selector ` 0 `；EOL ` RVA 0x34A33858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be548ffe4fb04560](../../evidence/conditions-sets-073.md#c-be548ffe4fb04560) · [状态效果 S-f48ac21d42e71411](../../evidence/state_effects-sets-052.md#s-f48ac21d42e71411)

### path-049921

```text
(config)# default do-exec show ip rsvp interface <cr>
```

Handler ` RVA 0x1006B3E0 `；selector ` 0 `；EOL ` RVA 0x34A33020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7276fe3cb0565025](../../evidence/conditions-sets-044.md#c-7276fe3cb0565025) · [状态效果 S-c60f2fe15d545c2f](../../evidence/state_effects-sets-042.md#s-c60f2fe15d545c2f)

### path-055884

```text
(config)# default do-exec show ip rsvp listeners <address> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 6 `；EOL ` RVA 0x34A35008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-559a5e35800d3230](../../evidence/parameters-sets-007.md#p-559a5e35800d3230) · [状态效果 S-5d6ea453853bfe57](../../evidence/state_effects-sets-020.md#s-5d6ea453853bfe57)

### path-058615

```text
(config)# default do-exec show ip rsvp listeners <address> <number:0..255> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 4 `；EOL ` RVA 0x34A34CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-c1d702e7762de23b](../../evidence/parameters-sets-015.md#p-c1d702e7762de23b) · [状态效果 S-5d6ea453853bfe57](../../evidence/state_effects-sets-020.md#s-5d6ea453853bfe57)

### path-059527

```text
(config)# default do-exec show ip rsvp listeners <address> <number:0..255> <number:0..65535> <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 0 `；EOL ` RVA 0x34A34A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [参数 P-eeed49378aa0252c](../../evidence/parameters-sets-018.md#p-eeed49378aa0252c) · [状态效果 S-5d6ea453853bfe57](../../evidence/state_effects-sets-020.md#s-5d6ea453853bfe57)

### path-050034

```text
(config)# default do-exec show ip rsvp listeners <cr>
```

Handler ` RVA 0x1006F480 `；selector ` 7 `；EOL ` RVA 0x34A352C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4759a80b867df040](../../evidence/conditions-sets-028.md#c-4759a80b867df040) · [状态效果 S-5d6ea453853bfe57](../../evidence/state_effects-sets-020.md#s-5d6ea453853bfe57)

### path-049792

```text
(config)# default do-exec show ip rsvp metadata <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A32250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-b1f6a1bc90a63ade](../../evidence/state_effects-sets-038.md#s-b1f6a1bc90a63ade)

### path-049736

```text
(config)# default do-exec show ip rsvp neighbor <cr>
```

Handler ` RVA 0x1006DCE0 `；selector ` 0 `；EOL ` RVA 0x34A309B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-1604abf1c0707041](../../evidence/state_effects-sets-005.md#s-1604abf1c0707041)

### path-055612

```text
(config)# default do-exec show ip rsvp neighbor queues <cr>
```

Handler ` RVA 0x1006DB00 `；selector ` 0 `；EOL ` RVA 0x34A30C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c1ac38b85e1fb7bb](../../evidence/conditions-sets-075.md#c-c1ac38b85e1fb7bb) · [状态效果 S-1604abf1c0707041](../../evidence/state_effects-sets-005.md#s-1604abf1c0707041)

### path-055463

```text
(config)# default do-exec show ip rsvp nsr counters <cr>
```

Handler ` RVA 0x100723C0 `；selector ` 0 `；EOL ` RVA 0x34A2FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9514e4dc259ba20d](../../evidence/conditions-sets-058.md#c-9514e4dc259ba20d) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055869

```text
(config)# default do-exec show ip rsvp p2mp counters <cr>
```

Handler ` RVA 0x101A72E0 `；selector ` 0 `；EOL ` RVA 0x34A3A468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-961c18143c16ea2a](../../evidence/conditions-sets-058.md#c-961c18143c16ea2a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049520

```text
(config)# default do-exec show ip rsvp policy <cr>
```

Handler ` RVA 0x10113110 `；selector ` 0 `；EOL ` RVA 0x34A40A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9c3376d0c22839b3](../../evidence/conditions-sets-060.md#c-9c3376d0c22839b3) · [状态效果 S-512b4b990e50e162](../../evidence/state_effects-sets-018.md#s-512b4b990e50e162)

### path-055547

```text
(config)# default do-exec show ip rsvp policy cops <cr>
```

Handler ` RVA 0x10113110 `；selector ` 8 `；EOL ` RVA 0x34A40AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e3c951b0abf3e01c](../../evidence/conditions-sets-088.md#c-e3c951b0abf3e01c) · [状态效果 S-512b4b990e50e162](../../evidence/state_effects-sets-018.md#s-512b4b990e50e162)

### path-055480

```text
(config)# default do-exec show ip rsvp policy identity <cr>
```

Handler ` RVA 0x10112D90 `；selector ` 0 `；EOL ` RVA 0x34A40020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-512b4b990e50e162](../../evidence/state_effects-sets-018.md#s-512b4b990e50e162)

### path-055703

```text
(config)# default do-exec show ip rsvp policy local <cr>
```

Handler ` RVA 0x10113110 `；selector ` 1 `；EOL ` RVA 0x34A40490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-af443612a5524707](../../evidence/conditions-sets-068.md#c-af443612a5524707) · [状态效果 S-3e8fab8337a5bb89](../../evidence/state_effects-sets-014.md#s-3e8fab8337a5bb89)

### path-049919

```text
(config)# default do-exec show ip rsvp precedence <cr>
```

Handler ` RVA 0x10054510 `；selector ` 0 `；EOL ` RVA 0x34A33C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-554816663dbba392](../../evidence/conditions-sets-033.md#c-554816663dbba392) · [状态效果 S-999cdd1815c88c4e](../../evidence/state_effects-sets-033.md#s-999cdd1815c88c4e)

### path-049648

```text
(config)# default do-exec show ip rsvp sbm <cr>
```

Handler ` RVA 0x1006E490 `；selector ` 0 `；EOL ` RVA 0x34A303A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e394e7d7feb6c7ab](../../evidence/conditions-sets-088.md#c-e394e7d7feb6c7ab) · [状态效果 S-8ef177958ac67d94](../../evidence/state_effects-sets-030.md#s-8ef177958ac67d94)

### path-049796

```text
(config)# default do-exec show ip rsvp sender <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A315A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-1846bf864f061710](../../evidence/state_effects-sets-006.md#s-1846bf864f061710)

### path-055967

```text
(config)# default do-exec show ip rsvp signalling blockade <cr>
```

Handler ` RVA 0x10067C20 `；selector ` 0 `；EOL ` RVA 0x34A3A0B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1de7acaebb82474a](../../evidence/conditions-sets-012.md#c-1de7acaebb82474a) · [状态效果 S-203a357cd38639d1](../../evidence/state_effects-sets-007.md#s-203a357cd38639d1)

### path-055857

```text
(config)# default do-exec show ip rsvp signalling fast-local-repair <cr>
```

Handler ` RVA 0x100713E0 `；selector ` 0 `；EOL ` RVA 0x34A38D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055846

```text
(config)# default do-exec show ip rsvp signalling rate-limit <cr>
```

Handler ` RVA 0x100712D0 `；selector ` 0 `；EOL ` RVA 0x34A38FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058644

```text
(config)# default do-exec show ip rsvp signalling refresh interval <cr>
```

Handler ` RVA 0x10071130 `；selector ` 0 `；EOL ` RVA 0x34A39858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058651

```text
(config)# default do-exec show ip rsvp signalling refresh misses <cr>
```

Handler ` RVA 0x100711A0 `；selector ` 0 `；EOL ` RVA 0x34A39B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058633

```text
(config)# default do-exec show ip rsvp signalling refresh reduction <cr>
```

Handler ` RVA 0x10071210 `；selector ` 0 `；EOL ` RVA 0x34A395B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055875

```text
(config)# default do-exec show ip rsvp signalling session-timers <cr>
```

Handler ` RVA 0x10072130 `；selector ` 0 `；EOL ` RVA 0x34A392A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbe8e5f206948a04](../../evidence/conditions-sets-073.md#c-bbe8e5f206948a04) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055584

```text
(config)# default do-exec show ip rsvp transport clients <cr>
```

Handler ` RVA 0x10069BC0 `；selector ` 0 `；EOL ` RVA 0x34A31E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7fe18cb68439d029](../../evidence/conditions-sets-050.md#c-7fe18cb68439d029) · [状态效果 S-f00c4900096aa6d0](../../evidence/state_effects-sets-051.md#s-f00c4900096aa6d0)

### path-047771

```text
(config)# default do-exec show ip rtp header-compression <cr>
```

Handler ` RVA 0xD194110 `；selector ` 0 `；EOL ` RVA 0x33DAABA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6a83c6ecb85845ec](../../evidence/conditions-sets-041.md#c-6a83c6ecb85845ec) · [状态效果 S-51fc0799e5be5c83](../../evidence/state_effects-sets-018.md#s-51fc0799e5be5c83)

### path-055076

```text
(config)# default do-exec show ip sctp association list <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 2 `；EOL ` RVA 0x33D0DFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058270

```text
(config)# default do-exec show ip sctp association parameters <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 3 `；EOL ` RVA 0x33D0DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d2fce9ec1de3fa16](../../evidence/parameters-sets-016.md#p-d2fce9ec1de3fa16) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058252

```text
(config)# default do-exec show ip sctp association statistics <number:0..4294967295> <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 4 `；EOL ` RVA 0x33D0DA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Association ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-39686869c9f42ad0](../../evidence/parameters-sets-005.md#p-39686869c9f42ad0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048602

```text
(config)# default do-exec show ip sctp errors <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 6 `；EOL ` RVA 0x33D0D6F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048714

```text
(config)# default do-exec show ip sctp instances <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 1 `；EOL ` RVA 0x33D0E288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048535

```text
(config)# default do-exec show ip sctp statistics <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 5 `；EOL ` RVA 0x33D0D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-039545

```text
(config)# default do-exec show ip sdr <cr>
```

Handler ` RVA 0xF87E5A0 `；selector ` 0 `；EOL ` RVA 0x3474E828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a322bbb3e692625](../../evidence/conditions-sets-004.md#c-0a322bbb3e692625) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050139

```text
(config)# default do-exec show ip sla application <cr>
```

Handler ` RVA 0x102DD0E0 `；selector ` 0 `；EOL ` RVA 0x34A99F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049827

```text
(config)# default do-exec show ip sla authentication <cr>
```

Handler ` RVA 0x101DA830 `；selector ` 0 `；EOL ` RVA 0x34A6E750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055833

```text
(config)# default do-exec show ip sla auto discovery <cr>
```

Handler ` RVA 0x10241B90 `；selector ` 0 `；EOL ` RVA 0x34A7ADC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055824

```text
(config)# default do-exec show ip sla auto group <cr>
```

Handler ` RVA 0x10240F70 `；selector ` 0 `；EOL ` RVA 0x34A7A360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-757c8fe8ca5c3a36](../../evidence/state_effects-sets-025.md#s-757c8fe8ca5c3a36)

### path-055821

```text
(config)# default do-exec show ip sla auto schedule <cr>
```

Handler ` RVA 0x10241510 `；selector ` 0 `；EOL ` RVA 0x34A7A6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-060106

```text
(config)# default do-exec show ip sla auto summary-statistics group type ip <string> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 2 `；EOL ` RVA 0x34A7B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Group name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-c18745a50f6313c9](../../evidence/state_effects-sets-041.md#s-c18745a50f6313c9)

### path-060239

```text
(config)# default do-exec show ip sla auto summary-statistics group type ip <string> ip-address <address> port <number:0..64000> <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 3 `；EOL ` RVA 0x34A7B2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Group name；` address ` destination ip address；` unsigned_number ` destination port。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-8528621cf3b47973](../../evidence/parameters-sets-010.md#p-8528621cf3b47973) · [状态效果 S-c18745a50f6313c9](../../evidence/state_effects-sets-041.md#s-c18745a50f6313c9)

### path-060181

```text
(config)# default do-exec show ip sla auto summary-statistics group type ip <string> ip-address <cr>
```

Handler ` RVA 0x10241ED0 `；selector ` 1 `；EOL ` RVA 0x34A7B248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Group name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-f84b4562b23f6845](../../evidence/parameters-sets-019.md#p-f84b4562b23f6845) · [状态效果 S-c18745a50f6313c9](../../evidence/state_effects-sets-041.md#s-c18745a50f6313c9)

### path-055859

```text
(config)# default do-exec show ip sla auto template <cr>
```

Handler ` RVA 0x102415E0 `；selector ` 0 `；EOL ` RVA 0x34A7AAC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-418d8f014ee47204](../../evidence/state_effects-sets-014.md#s-418d8f014ee47204)

### path-050030

```text
(config)# default do-exec show ip sla collection-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 0 `；EOL ` RVA 0x34A97478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049872

```text
(config)# default do-exec show ip sla configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 14 `；EOL ` RVA 0x34A95AC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050146

```text
(config)# default do-exec show ip sla distribution-statistics <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055873

```text
(config)# default do-exec show ip sla distribution-statistics full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 1 `；EOL ` RVA 0x34A97A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055845

```text
(config)# default do-exec show ip sla distribution-statistics raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 3 `；EOL ` RVA 0x34A977B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055896

```text
(config)# default do-exec show ip sla distribution-statistics tabular <cr>
```

Handler ` RVA 0x102DD820 `；selector ` 0 `；EOL ` RVA 0x34A97D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050259

```text
(config)# default do-exec show ip sla endpoint-list <cr>
```

Handler ` RVA 0x10241300 `；selector ` 0 `；EOL ` RVA 0x34A9A980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2fcb8b13c6aa2992](../../evidence/state_effects-sets-011.md#s-2fcb8b13c6aa2992)

### path-055879

```text
(config)# default do-exec show ip sla enhanced-history distribution-statistics <cr>
```

Handler ` RVA 0x102DD570 `；selector ` 0 `；EOL ` RVA 0x34A98318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1ab8febc33f23bce](../../evidence/state_effects-sets-006.md#s-1ab8febc33f23bce)

### path-055837

```text
(config)# default do-exec show ip sla ethernet-monitor configuration <cr>
```

Handler ` RVA 0x103C1120 `；selector ` 0 `；EOL ` RVA 0x34B09AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055794

```text
(config)# default do-exec show ip sla ethernet-monitor responder <cr>
```

Handler ` RVA 0x103C1230 `；selector ` 0 `；EOL ` RVA 0x34B09800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049892

```text
(config)# default do-exec show ip sla event-publisher <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 1 `；EOL ` RVA 0x34A890E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055728

```text
(config)# default do-exec show ip sla event-publisher detail <cr>
```

Handler ` RVA 0x102759D0 `；selector ` 2 `；EOL ` RVA 0x34A890C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055808

```text
(config)# default do-exec show ip sla group schedule <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 0 `；EOL ` RVA 0x34A96958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058575

```text
(config)# default do-exec show ip sla group schedule details <cr>
```

Handler ` RVA 0x102DD930 `；selector ` 28 `；EOL ` RVA 0x34A96930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050218

```text
(config)# default do-exec show ip sla history <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055911

```text
(config)# default do-exec show ip sla history full <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 5 `；EOL ` RVA 0x34A989A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055939

```text
(config)# default do-exec show ip sla history interval-statistics <cr>
```

Handler ` RVA 0x102DDA40 `；selector ` 45 `；EOL ` RVA 0x34A98EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055892

```text
(config)# default do-exec show ip sla history raw <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 7 `；EOL ` RVA 0x34A98700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055926

```text
(config)# default do-exec show ip sla history tabular <cr>
```

Handler ` RVA 0x102DD460 `；selector ` 0 `；EOL ` RVA 0x34A98C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049978

```text
(config)# default do-exec show ip sla operational-state <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 16 `；EOL ` RVA 0x34A96E98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050215

```text
(config)# default do-exec show ip sla reaction-configuration <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 17 `；EOL ` RVA 0x34A9A568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050194

```text
(config)# default do-exec show ip sla reaction-trigger <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 12 `；EOL ` RVA 0x34A9A278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049887

```text
(config)# default do-exec show ip sla responder <cr>
```

Handler ` RVA 0x101FD080 `；selector ` 0 `；EOL ` RVA 0x34A719E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050199

```text
(config)# default do-exec show ip sla statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 18 `；EOL ` RVA 0x34A99A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055933

```text
(config)# default do-exec show ip sla statistics aggregated <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 25 `；EOL ` RVA 0x34A99550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058643

```text
(config)# default do-exec show ip sla statistics aggregated details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 26 `；EOL ` RVA 0x34A99528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055925

```text
(config)# default do-exec show ip sla statistics details <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 22 `；EOL ` RVA 0x34A99A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049891

```text
(config)# default do-exec show ip sla summary <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 46 `；EOL ` RVA 0x34A95DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050005

```text
(config)# default do-exec show ip sla totals-statistics <cr>
```

Handler ` RVA 0x102DCF60 `；selector ` 4 `；EOL ` RVA 0x34A97188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058597

```text
(config)# default do-exec show ip sla twamp connection requests <cr>
```

Handler ` RVA 0x1021EB60 `；selector ` 0 `；EOL ` RVA 0x34A73EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8da2c29d212cdc51](../../evidence/state_effects-sets-030.md#s-8da2c29d212cdc51)

### path-055788

```text
(config)# default do-exec show ip sla twamp session <cr>
```

Handler ` RVA 0x10238810 `；selector ` 0 `；EOL ` RVA 0x34A76DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-96807f22a73f43c3](../../evidence/state_effects-sets-032.md#s-96807f22a73f43c3)

### path-055760

```text
(config)# default do-exec show ip sla twamp standards <cr>
```

Handler ` RVA 0x10238750 `；selector ` 0 `；EOL ` RVA 0x34A770A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055809

```text
(config)# default do-exec show ip sla twamp-light session <cr>
```

Handler ` RVA 0x1023AE80 `；selector ` 0 `；EOL ` RVA 0x34A79728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f3668fdcf21cf0d6](../../evidence/state_effects-sets-051.md#s-f3668fdcf21cf0d6)

### path-038149

```text
(config)# default do-exec show ip sockets <cr>
```

Handler ` RVA 0xCE441C0 `；selector ` 0 `；EOL ` RVA 0x33D31858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050015

```text
(config)# default do-exec show ip source binding <cr>
```

Handler ` RVA 0x15FA8BF0 `；selector ` 0 `；EOL ` RVA 0x35E7DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b8dbd9ab5c91f915](../../evidence/conditions-sets-071.md#c-b8dbd9ab5c91f915) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-038136

```text
(config)# default do-exec show ip spd <cr>
```

Handler ` RVA 0xCF78E90 `；selector ` 0 `；EOL ` RVA 0x33D31AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040452

```text
(config)# default do-exec show ip ssh <cr>
```

Handler ` RVA 0x12360610 `；selector ` 0 `；EOL ` RVA 0x35828848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055390

```text
(config)# default do-exec show ip static route bfd <cr>
```

Handler ` RVA 0xE2A6F50 `；selector ` 0 `；EOL ` RVA 0x3428F298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47dd4a8f8df142f4](../../evidence/conditions-sets-028.md#c-47dd4a8f8df142f4) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055235

```text
(config)# default do-exec show ip static route rwatch-rib <cr>
```

Handler ` RVA 0xE2A7940 `；selector ` 0 `；EOL ` RVA 0x3428F850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d082036f9d027b1b](../../evidence/conditions-sets-080.md#c-d082036f9d027b1b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055305

```text
(config)# default do-exec show ip static route sr-polices <cr>
```

Handler ` RVA 0xE2A79D0 `；selector ` 0 `；EOL ` RVA 0x3428FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-65d1b2164bbdba22](../../evidence/conditions-sets-039.md#c-65d1b2164bbdba22) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055151

```text
(config)# default do-exec show ip static route summary <cr>
```

Handler ` RVA 0xE2A7770 `；selector ` 0 `；EOL ` RVA 0x3428EE60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040730

```text
(config)# default do-exec show ip subscriber <cr>
```

Handler ` RVA 0x11A37870 `；selector ` 0 `；EOL ` RVA 0x355CDAE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8d6b94dc181ba373](../../evidence/state_effects-sets-030.md#s-8d6b94dc181ba373)

### path-047818

```text
(config)# default do-exec show ip tcp header-compression <cr>
```

Handler ` RVA 0xD194400 `；selector ` 0 `；EOL ` RVA 0x33DAB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f8c1239e9b64ddef](../../evidence/conditions-sets-096.md#c-f8c1239e9b64ddef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048123

```text
(config)# default do-exec show ip telnet status <cr>
```

Handler ` RVA 0xCDEFBC0 `；selector ` 0 `；EOL ` RVA 0x33D02090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-038282

```text
(config)# default do-exec show ip traffic <cr>
```

Handler ` RVA 0xCECF560 `；selector ` 0 `；EOL ` RVA 0x33D32270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054441

```text
(config)# default do-exec show ip traffic topology base <cr>
```

Handler ` RVA 0xCF0ED10 `；selector ` 0 `；EOL ` RVA 0x33D31E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-5d40e42a18e70dbb](../../evidence/state_effects-sets-020.md#s-5d40e42a18e70dbb)

### path-040229

```text
(config)# default do-exec show ip trigger-authentication <cr>
```

Handler ` RVA 0x10571410 `；selector ` 2 `；EOL ` RVA 0x34B5A698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040655

```text
(config)# default do-exec show ip virtual-reassembly <cr>
```

Handler ` RVA 0xC78EA70 `；selector ` 0 `；EOL ` RVA 0x33AECED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed87af899d4f2fe6](../../evidence/conditions-sets-092.md#c-ed87af899d4f2fe6) · [状态效果 S-4522125021675210](../../evidence/state_effects-sets-015.md#s-4522125021675210)

### path-037929

```text
(config)# default do-exec show ipam counts <cr>
```

Handler ` RVA 0xCEA9220 `；selector ` 0 `；EOL ` RVA 0x33D1B0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037910

```text
(config)# default do-exec show ipam pool <cr>
```

Handler ` RVA 0xCEA02D0 `；selector ` 0 `；EOL ` RVA 0x33D1B340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037949

```text
(config)# default do-exec show ipam queues <cr>
```

Handler ` RVA 0xCEA9160 `；selector ` 0 `；EOL ` RVA 0x33D1B5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037996

```text
(config)# default do-exec show ipam status <cr>
```

Handler ` RVA 0xCE9D6D0 `；selector ` 0 `；EOL ` RVA 0x33D1B890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035613

```text
(config)# default do-exec show ipc all <cr>
```

Handler ` RVA 0xD3B9630 `；selector ` 0 `；EOL ` RVA 0x33E2A320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3752e6d444c14e50](../../evidence/state_effects-sets-012.md#s-3752e6d444c14e50)

### path-036186

```text
(config)# default do-exec show ipc app <cr>
```

Handler ` RVA 0xD3BE590 `；selector ` 0 `；EOL ` RVA 0x33E2D5B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036247

```text
(config)# default do-exec show ipc buffer <cr>
```

Handler ` RVA 0xD39FCA0 `；selector ` 0 `；EOL ` RVA 0x33E2D858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052837

```text
(config)# default do-exec show ipc cli <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xD38B220 `；selector ` 0 `；EOL ` RVA 0x33E2AAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IPC Seatid (in hex)；` string ` Remote command string。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d04ece3d584907a5](../../evidence/parameters-sets-016.md#p-d04ece3d584907a5) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036034

```text
(config)# default do-exec show ipc delayed <cr>
```

Handler ` RVA 0xD3A24C0 `；selector ` 0 `；EOL ` RVA 0x33E2D018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035425

```text
(config)# default do-exec show ipc fc <cr>
```

Handler ` RVA 0xD3B96E0 `；selector ` 0 `；EOL ` RVA 0x33E29FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036212

```text
(config)# default do-exec show ipc fragment <cr>
```

Handler ` RVA 0xD3BE5F0 `；selector ` 0 `；EOL ` RVA 0x33E2CD28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6933166bdbdee99a](../../evidence/state_effects-sets-022.md#s-6933166bdbdee99a)

### path-035887

```text
(config)# default do-exec show ipc hog-info <cr>
```

Handler ` RVA 0xD3B8FB0 `；selector ` 0 `；EOL ` RVA 0x33E2C938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045892

```text
(config)# default do-exec show ipc keepalive tx <cr>
```

Handler ` RVA 0xD3B8EC0 `；selector ` 0 `；EOL ` RVA 0x33E2E360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-32ac32e1517adb56](../../evidence/state_effects-sets-011.md#s-32ac32e1517adb56)

### path-045214

```text
(config)# default do-exec show ipc mcast appclass <cr>
```

Handler ` RVA 0xD408040 `；selector ` 0 `；EOL ` RVA 0x33E42858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6e43ef7626be75a3](../../evidence/state_effects-sets-023.md#s-6e43ef7626be75a3)

### path-045329

```text
(config)# default do-exec show ipc mcast groups <cr>
```

Handler ` RVA 0xD407F80 `；selector ` 0 `；EOL ` RVA 0x33E42C30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fb521592ab3730f1](../../evidence/state_effects-sets-053.md#s-fb521592ab3730f1)

### path-052878

```text
(config)# default do-exec show ipc mcast groups <number:1..4294967295> <cr>
```

Handler ` RVA 0xD407F10 `；selector ` 0 `；EOL ` RVA 0x33E42F18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` group id。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6d276200dc0ed569](../../evidence/parameters-sets-009.md#p-6d276200dc0ed569) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045486

```text
(config)# default do-exec show ipc mcast sessions <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 0 `；EOL ` RVA 0x33E43368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e2587bba30e1a3e7](../../evidence/state_effects-sets-048.md#s-e2587bba30e1a3e7)

### path-053016

```text
(config)# default do-exec show ipc mcast sessions verbose <cr>
```

Handler ` RVA 0xD407DA0 `；selector ` 1 `；EOL ` RVA 0x33E43340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e2587bba30e1a3e7](../../evidence/state_effects-sets-048.md#s-e2587bba30e1a3e7)

### path-045162

```text
(config)# default do-exec show ipc mcast status <cr>
```

Handler ` RVA 0xD408100 `；selector ` 0 `；EOL ` RVA 0x33E42480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-140bee7426443b15](../../evidence/state_effects-sets-005.md#s-140bee7426443b15)

### path-035726

```text
(config)# default do-exec show ipc nodes <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 0 `；EOL ` RVA 0x33E2A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fa3b566300f5aaa0](../../evidence/state_effects-sets-053.md#s-fa3b566300f5aaa0)

### path-045369

```text
(config)# default do-exec show ipc nodes capabilities <cr>
```

Handler ` RVA 0xD45A9C0 `；selector ` 0 `；EOL ` RVA 0x33E489F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fa3b566300f5aaa0](../../evidence/state_effects-sets-053.md#s-fa3b566300f5aaa0)

### path-045310

```text
(config)# default do-exec show ipc nodes issu <cr>
```

Handler ` RVA 0xD45ADB0 `；selector ` 0 `；EOL ` RVA 0x33E48750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fa3b566300f5aaa0](../../evidence/state_effects-sets-053.md#s-fa3b566300f5aaa0)

### path-045370

```text
(config)# default do-exec show ipc nodes verbose <cr>
```

Handler ` RVA 0xD3B9570 `；selector ` 1 `；EOL ` RVA 0x33E27958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fa3b566300f5aaa0](../../evidence/state_effects-sets-053.md#s-fa3b566300f5aaa0)

### path-035991

```text
(config)# default do-exec show ipc ports <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 0 `；EOL ` RVA 0x33E2B120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1bb652df7c6749d3](../../evidence/state_effects-sets-006.md#s-1bb652df7c6749d3)

### path-045421

```text
(config)# default do-exec show ipc ports verbose <cr>
```

Handler ` RVA 0xD3B9210 `；selector ` 1 `；EOL ` RVA 0x33E2B3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1bb652df7c6749d3](../../evidence/state_effects-sets-006.md#s-1bb652df7c6749d3)

### path-035361

```text
(config)# default do-exec show ipc queue <cr>
```

Handler ` RVA 0xD3B91C0 `；selector ` 0 `；EOL ` RVA 0x33E29D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045164

```text
(config)# default do-exec show ipc rmi all <cr>
```

Handler ` RVA 0xD3FE890 `；selector ` 0 `；EOL ` RVA 0x33E3F8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0182e067a9c083b0](../../evidence/state_effects-sets-001.md#s-0182e067a9c083b0)

### path-057124

```text
(config)# default do-exec show ipc rmi thresholds ru <string> <cr>
```

Handler ` RVA 0xD3FE9F0 `；selector ` 0 `；EOL ` RVA 0x33E401F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` IPC RU id(in hex)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-1f71f90238213b0b](../../evidence/parameters-sets-003.md#p-1f71f90238213b0b) · [状态效果 S-1bc8caecbd6cbf55](../../evidence/state_effects-sets-006.md#s-1bc8caecbd6cbf55)

### path-036714

```text
(config)# default do-exec show ipc rpc <cr>
```

Handler ` RVA 0xD3B90F0 `；selector ` 0 `；EOL ` RVA 0x33E2E7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f9ee33fc0a8d5504](../../evidence/state_effects-sets-053.md#s-f9ee33fc0a8d5504)

### path-036380

```text
(config)# default do-exec show ipc sess-ack <cr>
```

Handler ` RVA 0xD3B92E0 `；selector ` 0 `；EOL ` RVA 0x33E2DDA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045481

```text
(config)# default do-exec show ipc session all <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 0 `；EOL ` RVA 0x33E2B898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b16953aa222830af](../../evidence/state_effects-sets-038.md#s-b16953aa222830af)

### path-053009

```text
(config)# default do-exec show ipc session all verbose <cr>
```

Handler ` RVA 0xD3B9330 `；selector ` 1 `；EOL ` RVA 0x33E2B870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b16953aa222830af](../../evidence/state_effects-sets-038.md#s-b16953aa222830af)

### path-045540

```text
(config)# default do-exec show ipc session tx <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 0 `；EOL ` RVA 0x33E2BF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e993dc58338fb590](../../evidence/state_effects-sets-049.md#s-e993dc58338fb590)

### path-053049

```text
(config)# default do-exec show ipc session tx verbose <cr>
```

Handler ` RVA 0xD3B9450 `；selector ` 1 `；EOL ` RVA 0x33E2BF10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e993dc58338fb590](../../evidence/state_effects-sets-049.md#s-e993dc58338fb590)

### path-036138

```text
(config)# default do-exec show ipc status <cr>
```

Handler ` RVA 0xD3B8DA0 `；selector ` 0 `；EOL ` RVA 0x33E2C640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-17f2b6cd95717042](../../evidence/state_effects-sets-005.md#s-17f2b6cd95717042)

### path-036317

```text
(config)# default do-exec show ipc thread-stats <cr>
```

Handler ` RVA 0xD3985A0 `；selector ` 0 `；EOL ` RVA 0x33E2DB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045554

```text
(config)# default do-exec show ipc trace <number:1..3> <cr>
```

Handler ` RVA 0xD3B9000 `；selector ` 0 `；EOL ` RVA 0x33E2D328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Type of buffer(1. event 2. debug 3. error)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-8efb61522b8c3136](../../evidence/parameters-sets-011.md#p-8efb61522b8c3136) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036607

```text
(config)# default do-exec show ipc util <cr>
```

Handler ` RVA 0xD3BC620 `；selector ` 0 `；EOL ` RVA 0x33E2EA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036438

```text
(config)# default do-exec show ipc watermark <cr>
```

Handler ` RVA 0xD3B8F20 `；selector ` 0 `；EOL ` RVA 0x33E2E050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035644

```text
(config)# default do-exec show ipc zones <cr>
```

Handler ` RVA 0xD3BC120 `；selector ` 0 `；EOL ` RVA 0x33E2AD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040571

```text
(config)# default do-exec show ipv6 access-list <cr>
```

Handler ` RVA 0x1217F2C0 `；selector ` 0 `；EOL ` RVA 0x357B0418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c0366a2229b2aaf5](../../evidence/conditions-sets-074.md#c-c0366a2229b2aaf5) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055653

```text
(config)# default do-exec show ipv6 access-list <string> dump-og-database <cr>
```

Handler ` RVA 0x1217F470 `；selector ` 0 `；EOL ` RVA 0x357B04A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` User selected string identifying this access list。

[条件 C-f9be45a27f3252dd](../../evidence/conditions-sets-096.md#c-f9be45a27f3252dd) · [参数 P-4019a6f8b247af69](../../evidence/parameters-sets-005.md#p-4019a6f8b247af69) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040689

```text
(config)# default do-exec show ipv6 alias <cr>
```

Handler ` RVA 0x12303F00 `；selector ` 0 `；EOL ` RVA 0x357DF538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041547

```text
(config)# default do-exec show ipv6 cef <cr>
```

Handler ` RVA 0xB662E40 `；selector ` 0 `；EOL ` RVA 0x337CDBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dce39c0405d8719d](../../evidence/conditions-sets-085.md#c-dce39c0405d8719d) · [状态效果 S-6b26ebaa4a879f7b](../../evidence/state_effects-sets-023.md#s-6b26ebaa4a879f7b)

### path-050263

```text
(config)# default do-exec show ipv6 cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337CE290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a7a0a4a69ad47303](../../evidence/conditions-sets-065.md#c-a7a0a4a69ad47303) · [状态效果 S-bfbf3d47dbeb1a5c](../../evidence/state_effects-sets-041.md#s-bfbf3d47dbeb1a5c)

### path-058593

```text
(config)# default do-exec show ipv6 cef neighbor discovery throttling <cr>
```

Handler ` RVA 0xB671710 `；selector ` 0 `；EOL ` RVA 0x337CD4C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-208fd76d36a9470d](../../evidence/conditions-sets-013.md#c-208fd76d36a9470d) · [状态效果 S-6b26ebaa4a879f7b](../../evidence/state_effects-sets-023.md#s-6b26ebaa4a879f7b)

### path-049885

```text
(config)# default do-exec show ipv6 cef protocol-discard <cr>
```

Handler ` RVA 0xB5C2EB0 `；selector ` 73 `；EOL ` RVA 0x337D89C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049935

```text
(config)# default do-exec show ipv6 cef summary <cr>
```

Handler ` RVA 0xB670E30 `；selector ` 1 `；EOL ` RVA 0x337CD130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-208fd76d36a9470d](../../evidence/conditions-sets-013.md#c-208fd76d36a9470d) · [状态效果 S-6b26ebaa4a879f7b](../../evidence/state_effects-sets-023.md#s-6b26ebaa4a879f7b)

### path-055878

```text
(config)# default do-exec show ipv6 cef switching statistics <cr>
```

Handler ` RVA 0xB66E5F0 `；selector ` 0 `；EOL ` RVA 0x337CDF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a7a0a4a69ad47303](../../evidence/conditions-sets-065.md#c-a7a0a4a69ad47303) · [状态效果 S-6b26ebaa4a879f7b](../../evidence/state_effects-sets-023.md#s-6b26ebaa4a879f7b)

### path-055889

```text
(config)# default do-exec show ipv6 cef traffic prefix-length <cr>
```

Handler ` RVA 0xB671680 `；selector ` 0 `；EOL ` RVA 0x337CE7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a7a0a4a69ad47303](../../evidence/conditions-sets-065.md#c-a7a0a4a69ad47303) · [状态效果 S-8962d9be7223ed16](../../evidence/state_effects-sets-029.md#s-8962d9be7223ed16)

### path-050031

```text
(config)# default do-exec show ipv6 cef tree <cr>
```

Handler ` RVA 0xB670D30 `；selector ` 0 `；EOL ` RVA 0x337CD7E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-208fd76d36a9470d](../../evidence/conditions-sets-013.md#c-208fd76d36a9470d) · [状态效果 S-6b26ebaa4a879f7b](../../evidence/state_effects-sets-023.md#s-6b26ebaa4a879f7b)

### path-049547

```text
(config)# default do-exec show ipv6 destination-guard policy <cr>
```

Handler ` RVA 0x136B13F0 `；selector ` 0 `；EOL ` RVA 0x35C02EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-040429

```text
(config)# default do-exec show ipv6 dhcp <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 0 `；EOL ` RVA 0x357C0EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049789

```text
(config)# default do-exec show ipv6 dhcp binding <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 0 `；EOL ` RVA 0x357C6450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049832

```text
(config)# default do-exec show ipv6 dhcp conflict <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 3 `；EOL ` RVA 0x357C6D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049682

```text
(config)# default do-exec show ipv6 dhcp database <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 2 `；EOL ` RVA 0x357C5C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049516

```text
(config)# default do-exec show ipv6 dhcp interface <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 1 `；EOL ` RVA 0x357C0868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3e89b51bedb64f0f](../../evidence/conditions-sets-024.md#c-3e89b51bedb64f0f) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059519

```text
(config)# default do-exec show ipv6 dhcp mac-hash-table dump pool <string> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 8 `；EOL ` RVA 0x357C7158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` pool name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c08b972a2d83bb8c](../../evidence/parameters-sets-015.md#p-c08b972a2d83bb8c) · [状态效果 S-2ecc401cd548569b](../../evidence/state_effects-sets-010.md#s-2ecc401cd548569b)

### path-060099

```text
(config)# default do-exec show ipv6 dhcp mac-hash-table dump pool <string> <number:0..255> <number:0..255> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 7 `；EOL ` RVA 0x357C71A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` pool name；` unsigned_number ` Lower bound of index range；` unsigned_number ` Upper bound of index range。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6b881825297e6ab3](../../evidence/parameters-sets-008.md#p-6b881825297e6ab3) · [状态效果 S-2ecc401cd548569b](../../evidence/state_effects-sets-010.md#s-2ecc401cd548569b)

### path-055675

```text
(config)# default do-exec show ipv6 dhcp packet statistics <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 6 `；EOL ` RVA 0x357C6A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049788

```text
(config)# default do-exec show ipv6 dhcp pool <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 1 `；EOL ` RVA 0x357C6748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055590

```text
(config)# default do-exec show ipv6 dhcp relay binding <cr>
```

Handler ` RVA 0x121B3460 `；selector ` 1 `；EOL ` RVA 0x357C33B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-055658

```text
(config)# default do-exec show ipv6 dhcp route <address> <cr>
```

Handler ` RVA 0x121CD760 `；selector ` 5 `；EOL ` RVA 0x357C6040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 Address。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-bed6f5b93ba7ce08](../../evidence/parameters-sets-014.md#p-bed6f5b93ba7ce08) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049440

```text
(config)# default do-exec show ipv6 dhcp statistics <cr>
```

Handler ` RVA 0x121A4390 `；selector ` 2 `；EOL ` RVA 0x357C0B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-049452

```text
(config)# default do-exec show ipv6 eigrp accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x35467758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f2dac0315bc903c1](../../evidence/state_effects-sets-051.md#s-f2dac0315bc903c1)

### path-049420

```text
(config)# default do-exec show ipv6 eigrp interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x35466788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-02072856c732d360](../../evidence/conditions-sets-001.md#c-02072856c732d360) · [状态效果 S-f2dac0315bc903c1](../../evidence/state_effects-sets-051.md#s-f2dac0315bc903c1)

### path-049480

```text
(config)# default do-exec show ipv6 eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x35466290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cc2ca51f771d257b](../../evidence/conditions-sets-079.md#c-cc2ca51f771d257b) · [状态效果 S-f2dac0315bc903c1](../../evidence/state_effects-sets-051.md#s-f2dac0315bc903c1)

### path-049553

```text
(config)# default do-exec show ipv6 eigrp sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1a11f65b1a336eac](../../evidence/state_effects-sets-006.md#s-1a11f65b1a336eac)

### path-049645

```text
(config)# default do-exec show ipv6 eigrp sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x35467E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0cb5828375c6d1ab](../../evidence/state_effects-sets-003.md#s-0cb5828375c6d1ab)

