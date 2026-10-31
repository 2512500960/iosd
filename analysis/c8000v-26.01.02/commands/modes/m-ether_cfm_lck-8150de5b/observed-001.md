# ether_cfm_lck · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009379

```text
(config-lck-link-cfm)# default disable <cr>
```

Handler ` RVA 0xBDC3F60 `；selector ` 0 `；EOL ` RVA 0x338F3CC0 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-a5a0f435ddb84218](../../evidence/state_effects-sets-035.md#s-a5a0f435ddb84218)

### observed_connections-009382

```text
(config-lck-link-cfm)# default level <cr>
```

Handler ` RVA 0xBDC3FB0 `；selector ` 0 `；EOL ` RVA 0x338F3FF8 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d7101b8d1c21539b](../../evidence/conditions-sets-083.md#c-d7101b8d1c21539b) · [状态效果 S-a5a0f435ddb84218](../../evidence/state_effects-sets-035.md#s-a5a0f435ddb84218)

### observed_connections-009385

```text
(config-lck-link-cfm)# default period <cr>
```

Handler ` RVA 0xBDC4070 `；selector ` 0 `；EOL ` RVA 0x338F42E8 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b1d34694071015ef](../../evidence/conditions-sets-069.md#c-b1d34694071015ef) · [状态效果 S-a5a0f435ddb84218](../../evidence/state_effects-sets-035.md#s-a5a0f435ddb84218)

### observed_connections-009377

```text
(config-lck-link-cfm)# disable <cr>
```

Handler ` RVA 0xBDC3F60 `；selector ` 0 `；EOL ` RVA 0x338F3CC0 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009376

```text
(config-lck-link-cfm)# exit <cr>
```

Handler ` RVA 0xBDBEEE0 `；selector ` 0 `；EOL ` RVA 0x338CAC08 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-222190beb7c4dd3d](../../evidence/conditions-sets-013.md#c-222190beb7c4dd3d)

### observed_connections-009381

```text
(config-lck-link-cfm)# level <number:0..7> <cr>
```

Handler ` RVA 0xBDC3FB0 `；selector ` 0 `；EOL ` RVA 0x338F3FF8 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maintenance Level。

[条件 C-9f9b59c1b3e775b9](../../evidence/conditions-sets-062.md#c-9f9b59c1b3e775b9) · [参数 P-0382f6142e3189f9](../../evidence/parameters-sets-001.md#p-0382f6142e3189f9)

### observed_connections-009378

```text
(config-lck-link-cfm)# no disable <cr>
```

Handler ` RVA 0xBDC3F60 `；selector ` 0 `；EOL ` RVA 0x338F3CC0 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-c00a55105a8ed2a8](../../evidence/state_effects-sets-041.md#s-c00a55105a8ed2a8)

### observed_connections-009380

```text
(config-lck-link-cfm)# no level <cr>
```

Handler ` RVA 0xBDC3FB0 `；selector ` 0 `；EOL ` RVA 0x338F3FF8 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-017c571a336ce7f5](../../evidence/conditions-sets-001.md#c-017c571a336ce7f5) · [状态效果 S-c00a55105a8ed2a8](../../evidence/state_effects-sets-041.md#s-c00a55105a8ed2a8)

### observed_connections-009383

```text
(config-lck-link-cfm)# no period <cr>
```

Handler ` RVA 0xBDC4070 `；selector ` 0 `；EOL ` RVA 0x338F42E8 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c913582a74823c9e](../../evidence/conditions-sets-077.md#c-c913582a74823c9e) · [状态效果 S-c00a55105a8ed2a8](../../evidence/state_effects-sets-041.md#s-c00a55105a8ed2a8)

### observed_connections-009384

```text
(config-lck-link-cfm)# period 1 <cr>
```

Handler ` RVA 0xBDC4070 `；selector ` 0 `；EOL ` RVA 0x338F42E8 `。

模式根 ` RVA 0x338CA0F8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2c04623fe975d276](../../evidence/conditions-sets-017.md#c-2c04623fe975d276) · [状态效果 S-2b0520f1da2d2ab2](../../evidence/state_effects-sets-010.md#s-2b0520f1da2d2ab2)
