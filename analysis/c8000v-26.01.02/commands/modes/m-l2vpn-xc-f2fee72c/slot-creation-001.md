# l2vpn-xc · 依赖静态建槽的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### static_slot_creation_candidates-004178

```text
(config-xconnect)# default description <cr>
```

Handler ` RVA 0x1A9E9C60 `；selector ` 0 `；EOL ` RVA 0x36D37E08 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-974457eadabbbf81](../../evidence/conditions-sets-058.md#c-974457eadabbbf81) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004181

```text
(config-xconnect)# default interworking <cr>
```

Handler ` RVA 0x1A9E99E0 `；selector ` 0 `；EOL ` RVA 0x36D38120 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-de4def35a1d91f83](../../evidence/conditions-sets-086.md#c-de4def35a1d91f83) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004193

```text
(config-xconnect)# default match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9E93B0 `；selector ` 0 `；EOL ` RVA 0x36D373E0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-a39e7e9713443941](../../evidence/conditions-sets-063.md#c-a39e7e9713443941) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004198

```text
(config-xconnect)# default member pseudowire <number:1..100000> <cr>
```

Handler ` RVA 0x1A9EB8A0 `；selector ` 0 `；EOL ` RVA 0x36D34618 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pseudowire interface number。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2c80b27fc6aee5f7](../../evidence/parameters-sets-004.md#p-2c80b27fc6aee5f7) · [状态效果 S-3232be74fadd5b6f](../../evidence/state_effects-sets-011.md#s-3232be74fadd5b6f)

### static_slot_creation_candidates-004190

```text
(config-xconnect)# default redundancy all-active <cr>
```

Handler ` RVA 0x1A9EA250 `；selector ` 0 `；EOL ` RVA 0x36D39028 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-f7b6df2ca661209b](../../evidence/conditions-sets-096.md#c-f7b6df2ca661209b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004203

```text
(config-xconnect)# default redundancy delay <number:0..180> <number:0..180> group <string> <cr>
```

Handler ` RVA 0x1A9E9F30 `；selector ` 0 `；EOL ` RVA 0x36D38970 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enable delay；` unsigned_number ` Disable delay；` string ` Enter name。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5aafa79dc25e28a8](../../evidence/parameters-sets-007.md#p-5aafa79dc25e28a8) · [状态效果 S-0533242165dbf761](../../evidence/state_effects-sets-002.md#s-0533242165dbf761)

### static_slot_creation_candidates-004187

```text
(config-xconnect)# default redundancy predictive <cr>
```

Handler ` RVA 0x1A9EA100 `；selector ` 0 `；EOL ` RVA 0x36D38CC8 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-ff9f74c95f6179b8](../../evidence/conditions-sets-099.md#c-ff9f74c95f6179b8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004196

```text
(config-xconnect)# default remote circuit id <cr>
```

Handler ` RVA 0x1A9E9530 `；selector ` 0 `；EOL ` RVA 0x36D377B0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-f91560602b8ee2f2](../../evidence/conditions-sets-096.md#c-f91560602b8ee2f2) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004200

```text
(config-xconnect)# default remote link failure notification <cr>
```

Handler ` RVA 0x1A9E96A0 `；selector ` 0 `；EOL ` RVA 0x36D37AC8 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004183

```text
(config-xconnect)# default shutdown <cr>
```

Handler ` RVA 0x1A9E9E10 `；selector ` 0 `；EOL ` RVA 0x36D392E0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,1,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-6a9f0670482626ce](../../evidence/state_effects-sets-023.md#s-6a9f0670482626ce)

### static_slot_creation_candidates-004177

```text
(config-xconnect)# description <string> <cr>
```

Handler ` RVA 0x1A9E9C60 `；selector ` 0 `；EOL ` RVA 0x36D37E08 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Description string。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-b26afa1c0d404a67](../../evidence/conditions-sets-069.md#c-b26afa1c0d404a67) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-96f13b1de29a64b6](../../evidence/parameters-sets-012.md#p-96f13b1de29a64b6)

### static_slot_creation_candidates-004180

```text
(config-xconnect)# interworking ethernet <cr>
```

Handler ` RVA 0x1A9E99E0 `；selector ` 0 `；EOL ` RVA 0x36D38120 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-44ca486791ddfff5](../../evidence/conditions-sets-027.md#c-44ca486791ddfff5) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-a2f747585c5ab4c3](../../evidence/state_effects-sets-035.md#s-a2f747585c5ab4c3)

### static_slot_creation_candidates-004184

```text
(config-xconnect)# match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9E93B0 `；selector ` 0 `；EOL ` RVA 0x36D373E0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-a39e7e9713443941](../../evidence/conditions-sets-063.md#c-a39e7e9713443941) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004191

```text
(config-xconnect)# member pseudowire <number:1..100000> <cr>
```

Handler ` RVA 0x1A9EB8A0 `；selector ` 0 `；EOL ` RVA 0x36D34618 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pseudowire interface number。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2c80b27fc6aee5f7](../../evidence/parameters-sets-004.md#p-2c80b27fc6aee5f7) · [状态效果 S-42eca7aae817cdf3](../../evidence/state_effects-sets-015.md#s-42eca7aae817cdf3)

### static_slot_creation_candidates-004176

```text
(config-xconnect)# no description <cr>
```

Handler ` RVA 0x1A9E9C60 `；selector ` 0 `；EOL ` RVA 0x36D37E08 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-905f794c2c44a8c8](../../evidence/conditions-sets-056.md#c-905f794c2c44a8c8) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004179

```text
(config-xconnect)# no interworking <cr>
```

Handler ` RVA 0x1A9E99E0 `；selector ` 0 `；EOL ` RVA 0x36D38120 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-1dbb2be78d50cacb](../../evidence/conditions-sets-012.md#c-1dbb2be78d50cacb) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004192

```text
(config-xconnect)# no match protocol ipv6 <cr>
```

Handler ` RVA 0x1A9E93B0 `；selector ` 0 `；EOL ` RVA 0x36D373E0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-a39e7e9713443941](../../evidence/conditions-sets-063.md#c-a39e7e9713443941) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004197

```text
(config-xconnect)# no member pseudowire <number:1..100000> <cr>
```

Handler ` RVA 0x1A9EB8A0 `；selector ` 0 `；EOL ` RVA 0x36D34618 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Pseudowire interface number。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-2c80b27fc6aee5f7](../../evidence/parameters-sets-004.md#p-2c80b27fc6aee5f7) · [状态效果 S-c1d14b5d92eb64b1](../../evidence/state_effects-sets-041.md#s-c1d14b5d92eb64b1)

### static_slot_creation_candidates-004188

```text
(config-xconnect)# no redundancy all-active <cr>
```

Handler ` RVA 0x1A9EA250 `；selector ` 0 `；EOL ` RVA 0x36D39028 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-50f53ab7731f3f5a](../../evidence/conditions-sets-032.md#c-50f53ab7731f3f5a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004202

```text
(config-xconnect)# no redundancy delay <number:0..180> <number:0..180> group <string> <cr>
```

Handler ` RVA 0x1A9E9F30 `；selector ` 0 `；EOL ` RVA 0x36D38970 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Enable delay；` unsigned_number ` Disable delay；` string ` Enter name。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5aafa79dc25e28a8](../../evidence/parameters-sets-007.md#p-5aafa79dc25e28a8) · [状态效果 S-9668a36aed228365](../../evidence/state_effects-sets-032.md#s-9668a36aed228365)

### static_slot_creation_candidates-004185

```text
(config-xconnect)# no redundancy predictive <cr>
```

Handler ` RVA 0x1A9EA100 `；selector ` 0 `；EOL ` RVA 0x36D38CC8 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-bf4ced388ddbd95a](../../evidence/conditions-sets-074.md#c-bf4ced388ddbd95a) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004194

```text
(config-xconnect)# no remote circuit id <cr>
```

Handler ` RVA 0x1A9E9530 `；selector ` 0 `；EOL ` RVA 0x36D377B0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-d56cf3a206f439b1](../../evidence/conditions-sets-082.md#c-d56cf3a206f439b1) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004199

```text
(config-xconnect)# no remote link failure notification <cr>
```

Handler ` RVA 0x1A9E96A0 `；selector ` 0 `；EOL ` RVA 0x36D37AC8 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004182

```text
(config-xconnect)# no shutdown <cr>
```

Handler ` RVA 0x1A9E9E10 `；selector ` 0 `；EOL ` RVA 0x36D392E0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [0,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-c52832435612b6cf](../../evidence/state_effects-sets-042.md#s-c52832435612b6cf)

### static_slot_creation_candidates-004189

```text
(config-xconnect)# redundancy all-active replicate <cr>
```

Handler ` RVA 0x1A9EA250 `；selector ` 0 `；EOL ` RVA 0x36D39028 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-b1d30f402ec45368](../../evidence/conditions-sets-069.md#c-b1d30f402ec45368) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004201

```text
(config-xconnect)# redundancy delay <number:0..180> <number:0..180> group <string> <cr>
```

Handler ` RVA 0x1A9E9F30 `；selector ` 0 `；EOL ` RVA 0x36D38970 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable delay；` unsigned_number ` Disable delay；` string ` Enter name。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [参数 P-5aafa79dc25e28a8](../../evidence/parameters-sets-007.md#p-5aafa79dc25e28a8) · [状态效果 S-71bc2269bdcb61d2](../../evidence/state_effects-sets-024.md#s-71bc2269bdcb61d2)

### static_slot_creation_candidates-004186

```text
(config-xconnect)# redundancy predictive disabled <cr>
```

Handler ` RVA 0x1A9EA100 `；selector ` 0 `；EOL ` RVA 0x36D38CC8 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-e936d61e96a1ee8b](../../evidence/conditions-sets-090.md#c-e936d61e96a1ee8b) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f) · [状态效果 S-717e2bba83445b61](../../evidence/state_effects-sets-024.md#s-717e2bba83445b61)

### static_slot_creation_candidates-004204

```text
(config-xconnect)# remote circuit id <number:dynamic> <cr>
```

Handler ` RVA 0x1A9E9530 `；selector ` 0 `；EOL ` RVA 0x36D377B0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Remote circuit ID。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-7133eca2532a99bd](../../evidence/conditions-sets-044.md#c-7133eca2532a99bd) · [缺口 G-2c51002c55f9d576](../../evidence/gaps-sets-002.md#g-2c51002c55f9d576) · [参数 P-94e2dbecd2c28b7d](../../evidence/parameters-sets-011.md#p-94e2dbecd2c28b7d)

### static_slot_creation_candidates-004195

```text
(config-xconnect)# remote link failure notification <cr>
```

Handler ` RVA 0x1A9E96A0 `；selector ` 0 `；EOL ` RVA 0x36D37AC8 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)

### static_slot_creation_candidates-004175

```text
(config-xconnect)# shutdown <cr>
```

Handler ` RVA 0x1A9E9E10 `；selector ` 0 `；EOL ` RVA 0x36D392E0 `。

模式根 ` RVA 0x36D339E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,0,0] `。

[候选注册 R-5c68e61c35f2e1e0](../../evidence/conditional_registrations-sets-001.md#r-5c68e61c35f2e1e0) · [条件 C-2b053ebf953311a6](../../evidence/conditions-sets-017.md#c-2b053ebf953311a6) · [缺口 G-b44198d32133d73f](../../evidence/gaps-sets-006.md#g-b44198d32133d73f)
