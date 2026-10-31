# ecfm_srv · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007362

```text
(config-ecfm-srv)# ais <cr>
```

Handler ` RVA 0xBDCA680 `；selector ` 0 `；EOL ` RVA 0x338E7B38 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-061d6104b1343085](../../evidence/conditions-sets-003.md#c-061d6104b1343085)

### observed_connections-007404

```text
(config-ecfm-srv)# ais expiry-threshold <number:2..255> <cr>
```

Handler ` RVA 0xBDCABA0 `；selector ` 0 `；EOL ` RVA 0x338E7888 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Expiry Threshold。

[条件 C-1c395088925fd028](../../evidence/conditions-sets-011.md#c-1c395088925fd028) · [参数 P-2020ba664c32b004](../../evidence/parameters-sets-003.md#p-2020ba664c32b004)

### observed_connections-007396

```text
(config-ecfm-srv)# ais level <number:0..7> <cr>
```

Handler ` RVA 0xBDCA9F0 `；selector ` 0 `；EOL ` RVA 0x338E7570 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maintenance Level。

[条件 C-1733db7d4fd5fe43](../../evidence/conditions-sets-009.md#c-1733db7d4fd5fe43) · [参数 P-75dba30b96f1fdf5](../../evidence/parameters-sets-009.md#p-75dba30b96f1fdf5)

### observed_connections-007392

```text
(config-ecfm-srv)# ais period 1 <cr>
```

Handler ` RVA 0xBDCA840 `；selector ` 0 `；EOL ` RVA 0x338E71E8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-21b271e785d887f6](../../evidence/conditions-sets-013.md#c-21b271e785d887f6) · [状态效果 S-f4ad8cea83e37a37](../../evidence/state_effects-sets-052.md#s-f4ad8cea83e37a37)

### observed_connections-007371

```text
(config-ecfm-srv)# ais suppress-alarms <cr>
```

Handler ` RVA 0xBDCAD50 `；selector ` 0 `；EOL ` RVA 0x338E7B10 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-061d6104b1343085](../../evidence/conditions-sets-003.md#c-061d6104b1343085)

### observed_connections-007378

```text
(config-ecfm-srv)# alias <string> <cr>
```

Handler ` RVA 0xBDCBD60 `；selector ` 0 `；EOL ` RVA 0x338E9908 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` alias short MA name。

[条件 C-d7b075c5ff425eb4](../../evidence/conditions-sets-083.md#c-d7b075c5ff425eb4) · [参数 P-814995d013098f51](../../evidence/parameters-sets-010.md#p-814995d013098f51) · [状态效果 S-03bfd7574962cd08](../../evidence/state_effects-sets-001.md#s-03bfd7574962cd08)

### observed_connections-007361

```text
(config-ecfm-srv)# continuity-check <cr>
```

Handler ` RVA 0xBDC94B0 `；selector ` 0 `；EOL ` RVA 0x338E5CA0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-351aa7887d4d6f7d](../../evidence/conditions-sets-021.md#c-351aa7887d4d6f7d)

### observed_connections-007384

```text
(config-ecfm-srv)# continuity-check interval 3.3ms <cr>
```

Handler ` RVA 0xBDC9660 `；selector ` 0 `；EOL ` RVA 0x338E5280 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dcffacda43224e96](../../evidence/conditions-sets-085.md#c-dcffacda43224e96) · [状态效果 S-74fce6091dae792e](../../evidence/state_effects-sets-025.md#s-74fce6091dae792e)

### observed_connections-007383

```text
(config-ecfm-srv)# continuity-check loss-threshold <number:2..255> <cr>
```

Handler ` RVA 0xBDC99D0 `；selector ` 0 `；EOL ` RVA 0x338E59B0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Continuity Check messages missed before MEP down (default 3)。

[条件 C-022743a9c0294b7c](../../evidence/conditions-sets-001.md#c-022743a9c0294b7c) · [参数 P-3c51bd2d17526854](../../evidence/parameters-sets-005.md#p-3c51bd2d17526854)

### observed_connections-007386

```text
(config-ecfm-srv)# continuity-check static rmep <cr>
```

Handler ` RVA 0xBDC9BA0 `；selector ` 0 `；EOL ` RVA 0x338E5CE0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58ebf06be28ae7c4](../../evidence/conditions-sets-035.md#c-58ebf06be28ae7c4)

### observed_connections-007375

```text
(config-ecfm-srv)# default ais <cr>
```

Handler ` RVA 0xBDCA680 `；selector ` 0 `；EOL ` RVA 0x338E7B38 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-061d6104b1343085](../../evidence/conditions-sets-003.md#c-061d6104b1343085) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007411

```text
(config-ecfm-srv)# default ais expiry-threshold <cr>
```

Handler ` RVA 0xBDCABA0 `；selector ` 0 `；EOL ` RVA 0x338E7888 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1bf0c0fb19cfad41](../../evidence/conditions-sets-011.md#c-1bf0c0fb19cfad41) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007400

```text
(config-ecfm-srv)# default ais level <cr>
```

Handler ` RVA 0xBDCA9F0 `；selector ` 0 `；EOL ` RVA 0x338E7570 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-20d899e87a2bbd4f](../../evidence/conditions-sets-013.md#c-20d899e87a2bbd4f) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007393

```text
(config-ecfm-srv)# default ais period <cr>
```

Handler ` RVA 0xBDCA840 `；selector ` 0 `；EOL ` RVA 0x338E71E8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2673a2b61be15603](../../evidence/conditions-sets-015.md#c-2673a2b61be15603) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007406

```text
(config-ecfm-srv)# default ais suppress-alarms <cr>
```

Handler ` RVA 0xBDCAD50 `；selector ` 0 `；EOL ` RVA 0x338E7B10 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-061d6104b1343085](../../evidence/conditions-sets-003.md#c-061d6104b1343085) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007376

```text
(config-ecfm-srv)# default alias <cr>
```

Handler ` RVA 0xBDCBD60 `；selector ` 0 `；EOL ` RVA 0x338E9908 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d901d2291fdf0514](../../evidence/conditions-sets-084.md#c-d901d2291fdf0514) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007368

```text
(config-ecfm-srv)# default continuity-check <cr>
```

Handler ` RVA 0xBDC94B0 `；selector ` 0 `；EOL ` RVA 0x338E5CA0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-351aa7887d4d6f7d](../../evidence/conditions-sets-021.md#c-351aa7887d4d6f7d) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007380

```text
(config-ecfm-srv)# default continuity-check interval <cr>
```

Handler ` RVA 0xBDC9660 `；selector ` 0 `；EOL ` RVA 0x338E5280 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1382ef323237833e](../../evidence/conditions-sets-008.md#c-1382ef323237833e) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007385

```text
(config-ecfm-srv)# default continuity-check loss-threshold <cr>
```

Handler ` RVA 0xBDC99D0 `；selector ` 0 `；EOL ` RVA 0x338E59B0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d9f108119ece7f3](../../evidence/conditions-sets-006.md#c-0d9f108119ece7f3) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007422

```text
(config-ecfm-srv)# default continuity-check static rmep <cr>
```

Handler ` RVA 0xBDC9BA0 `；selector ` 0 `；EOL ` RVA 0x338E5CE0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-58ebf06be28ae7c4](../../evidence/conditions-sets-035.md#c-58ebf06be28ae7c4) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007405

```text
(config-ecfm-srv)# default efd line-protocol <cr>
```

Handler ` RVA 0xBDCB280 `；selector ` 0 `；EOL ` RVA 0x338E8558 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d97d029eb3faf1c6](../../evidence/conditions-sets-084.md#c-d97d029eb3faf1c6) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007409

```text
(config-ecfm-srv)# default efd notify <cr>
```

Handler ` RVA 0xBDCAF10 `；selector ` 0 `；EOL ` RVA 0x338E81A0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b8c76740bcacc2e9](../../evidence/conditions-sets-071.md#c-b8c76740bcacc2e9) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007377

```text
(config-ecfm-srv)# default lck <cr>
```

Handler ` RVA 0xBDCB430 `；selector ` 0 `；EOL ` RVA 0x338E8F60 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a528205a001f5b62](../../evidence/conditions-sets-064.md#c-a528205a001f5b62) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007418

```text
(config-ecfm-srv)# default lck expiry-threshold <cr>
```

Handler ` RVA 0xBDCB950 `；selector ` 0 `；EOL ` RVA 0x338E8FC8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d730f070db66dd8c](../../evidence/conditions-sets-083.md#c-d730f070db66dd8c) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007415

```text
(config-ecfm-srv)# default lck level <cr>
```

Handler ` RVA 0xBDCB7A0 `；selector ` 0 `；EOL ` RVA 0x338E8CB0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a48745eae88f4af](../../evidence/conditions-sets-035.md#c-5a48745eae88f4af) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007407

```text
(config-ecfm-srv)# default lck period <cr>
```

Handler ` RVA 0xBDCB5F0 `；selector ` 0 `；EOL ` RVA 0x338E8928 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f62c64599f5af97](../../evidence/conditions-sets-019.md#c-2f62c64599f5af97) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007389

```text
(config-ecfm-srv)# default maximum meps <cr>
```

Handler ` RVA 0xBDCA3E0 `；selector ` 0 `；EOL ` RVA 0x338E6E18 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-70f64efbb2e35b3d](../../evidence/conditions-sets-044.md#c-70f64efbb2e35b3d) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007420

```text
(config-ecfm-srv)# default mep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDC9D70 `；selector ` 0 `；EOL ` RVA 0x338E62C0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-664e99507f0fc8cf](../../evidence/conditions-sets-040.md#c-664e99507f0fc8cf) · [参数 P-4864123b7bfc62a2](../../evidence/parameters-sets-006.md#p-4864123b7bfc62a2) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007395

```text
(config-ecfm-srv)# default mip auto-create <cr>
```

Handler ` RVA 0xBDCA230 `；selector ` 0 `；EOL ` RVA 0x338E6A00 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84e2a867afff806c](../../evidence/conditions-sets-051.md#c-84e2a867afff806c) · [状态效果 S-33eab6b99e508110](../../evidence/state_effects-sets-011.md#s-33eab6b99e508110)

### observed_connections-007414

```text
(config-ecfm-srv)# default offload sampling <cr>
```

Handler ` RVA 0xBDCBB00 `；selector ` 0 `；EOL ` RVA 0x338E95C8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dec66f447960c7b0](../../evidence/conditions-sets-086.md#c-dec66f447960c7b0) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007367

```text
(config-ecfm-srv)# default sender-id <cr>
```

Handler ` RVA 0xBDCA080 `；selector ` 0 `；EOL ` RVA 0x338E65E8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d9731db0827a2db9](../../evidence/conditions-sets-084.md#c-d9731db0827a2db9) · [状态效果 S-96a0bd91c26e3398](../../evidence/state_effects-sets-032.md#s-96a0bd91c26e3398)

### observed_connections-007370

```text
(config-ecfm-srv)# efd line-protocol <cr>
```

Handler ` RVA 0xBDCB280 `；selector ` 0 `；EOL ` RVA 0x338E8558 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d97d029eb3faf1c6](../../evidence/conditions-sets-084.md#c-d97d029eb3faf1c6)

### observed_connections-007413

```text
(config-ecfm-srv)# efd notify g8032 <cr>
```

Handler ` RVA 0xBDCAF10 `；selector ` 0 `；EOL ` RVA 0x338E81A0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9b75a207cb9dd792](../../evidence/conditions-sets-060.md#c-9b75a207cb9dd792) · [状态效果 S-34840addc684f58b](../../evidence/state_effects-sets-012.md#s-34840addc684f58b)

### observed_connections-007360

```text
(config-ecfm-srv)# exit <cr>
```

Handler ` RVA 0xBDBE780 `；selector ` 0 `；EOL ` RVA 0x338CA568 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-059b332f47bfefd0](../../evidence/conditions-sets-003.md#c-059b332f47bfefd0)

### observed_connections-007363

```text
(config-ecfm-srv)# lck <cr>
```

Handler ` RVA 0xBDCB430 `；selector ` 0 `；EOL ` RVA 0x338E8F60 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a528205a001f5b62](../../evidence/conditions-sets-064.md#c-a528205a001f5b62)

### observed_connections-007417

```text
(config-ecfm-srv)# lck expiry-threshold <number:2..255> <cr>
```

Handler ` RVA 0xBDCB950 `；selector ` 0 `；EOL ` RVA 0x338E8FC8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Expiry Threshold。

[条件 C-374c16df67f6c0a7](../../evidence/conditions-sets-021.md#c-374c16df67f6c0a7) · [参数 P-6a7e64cc5ec81601](../../evidence/parameters-sets-008.md#p-6a7e64cc5ec81601)

### observed_connections-007412

```text
(config-ecfm-srv)# lck level <number:0..7> <cr>
```

Handler ` RVA 0xBDCB7A0 `；selector ` 0 `；EOL ` RVA 0x338E8CB0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maintenance Level。

[条件 C-69d20eaf7026b1df](../../evidence/conditions-sets-041.md#c-69d20eaf7026b1df) · [参数 P-24fa3ce58b3ed9a1](../../evidence/parameters-sets-003.md#p-24fa3ce58b3ed9a1)

### observed_connections-007403

```text
(config-ecfm-srv)# lck period 1 <cr>
```

Handler ` RVA 0xBDCB5F0 `；selector ` 0 `；EOL ` RVA 0x338E8928 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00fc855c5b4b338e](../../evidence/conditions-sets-001.md#c-00fc855c5b4b338e) · [状态效果 S-de5eb952ebee3a76](../../evidence/state_effects-sets-047.md#s-de5eb952ebee3a76)

### observed_connections-007388

```text
(config-ecfm-srv)# maximum meps <number:1..65535> <cr>
```

Handler ` RVA 0xBDCA3E0 `；selector ` 0 `；EOL ` RVA 0x338E6E18 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max meps (default 100)。

[条件 C-66c4042655f046d5](../../evidence/conditions-sets-040.md#c-66c4042655f046d5) · [参数 P-feefa4c80bdc6944](../../evidence/parameters-sets-019.md#p-feefa4c80bdc6944)

### observed_connections-007382

```text
(config-ecfm-srv)# mep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDC9D70 `；selector ` 0 `；EOL ` RVA 0x338E62C0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-664e99507f0fc8cf](../../evidence/conditions-sets-040.md#c-664e99507f0fc8cf) · [参数 P-4864123b7bfc62a2](../../evidence/parameters-sets-006.md#p-4864123b7bfc62a2)

### observed_connections-007369

```text
(config-ecfm-srv)# mip auto-create <cr>
```

Handler ` RVA 0xBDCA230 `；selector ` 0 `；EOL ` RVA 0x338E6A00 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84e2a867afff806c](../../evidence/conditions-sets-051.md#c-84e2a867afff806c) · [状态效果 S-66bdb5ccbe07b547](../../evidence/state_effects-sets-022.md#s-66bdb5ccbe07b547)

### observed_connections-007372

```text
(config-ecfm-srv)# no ais <cr>
```

Handler ` RVA 0xBDCA680 `；selector ` 0 `；EOL ` RVA 0x338E7B38 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-061d6104b1343085](../../evidence/conditions-sets-003.md#c-061d6104b1343085) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007402

```text
(config-ecfm-srv)# no ais expiry-threshold <cr>
```

Handler ` RVA 0xBDCABA0 `；selector ` 0 `；EOL ` RVA 0x338E7888 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4710a6abf368c6a4](../../evidence/conditions-sets-028.md#c-4710a6abf368c6a4) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007394

```text
(config-ecfm-srv)# no ais level <cr>
```

Handler ` RVA 0xBDCA9F0 `；selector ` 0 `；EOL ` RVA 0x338E7570 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d9f7852e184aa12f](../../evidence/conditions-sets-084.md#c-d9f7852e184aa12f) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007390

```text
(config-ecfm-srv)# no ais period <cr>
```

Handler ` RVA 0xBDCA840 `；selector ` 0 `；EOL ` RVA 0x338E71E8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4b113e4c5d97ef97](../../evidence/conditions-sets-029.md#c-4b113e4c5d97ef97) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007398

```text
(config-ecfm-srv)# no ais suppress-alarms <cr>
```

Handler ` RVA 0xBDCAD50 `；selector ` 0 `；EOL ` RVA 0x338E7B10 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-061d6104b1343085](../../evidence/conditions-sets-003.md#c-061d6104b1343085) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007373

```text
(config-ecfm-srv)# no alias <cr>
```

Handler ` RVA 0xBDCBD60 `；selector ` 0 `；EOL ` RVA 0x338E9908 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-231ae00dcce632b1](../../evidence/conditions-sets-014.md#c-231ae00dcce632b1) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007365

```text
(config-ecfm-srv)# no continuity-check <cr>
```

Handler ` RVA 0xBDC94B0 `；selector ` 0 `；EOL ` RVA 0x338E5CA0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-351aa7887d4d6f7d](../../evidence/conditions-sets-021.md#c-351aa7887d4d6f7d) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007379

```text
(config-ecfm-srv)# no continuity-check interval <cr>
```

Handler ` RVA 0xBDC9660 `；selector ` 0 `；EOL ` RVA 0x338E5280 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a9cd0e4cd40c28a4](../../evidence/conditions-sets-066.md#c-a9cd0e4cd40c28a4) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007381

```text
(config-ecfm-srv)# no continuity-check loss-threshold <cr>
```

Handler ` RVA 0xBDC99D0 `；selector ` 0 `；EOL ` RVA 0x338E59B0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-463c456d7489a021](../../evidence/conditions-sets-027.md#c-463c456d7489a021) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007421

```text
(config-ecfm-srv)# no continuity-check static rmep <cr>
```

Handler ` RVA 0xBDC9BA0 `；selector ` 0 `；EOL ` RVA 0x338E5CE0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-58ebf06be28ae7c4](../../evidence/conditions-sets-035.md#c-58ebf06be28ae7c4) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007397

```text
(config-ecfm-srv)# no efd line-protocol <cr>
```

Handler ` RVA 0xBDCB280 `；selector ` 0 `；EOL ` RVA 0x338E8558 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d97d029eb3faf1c6](../../evidence/conditions-sets-084.md#c-d97d029eb3faf1c6) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007401

```text
(config-ecfm-srv)# no efd notify <cr>
```

Handler ` RVA 0xBDCAF10 `；selector ` 0 `；EOL ` RVA 0x338E81A0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9e7e0858fba15cdb](../../evidence/conditions-sets-061.md#c-9e7e0858fba15cdb) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007374

```text
(config-ecfm-srv)# no lck <cr>
```

Handler ` RVA 0xBDCB430 `；selector ` 0 `；EOL ` RVA 0x338E8F60 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a528205a001f5b62](../../evidence/conditions-sets-064.md#c-a528205a001f5b62) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007416

```text
(config-ecfm-srv)# no lck expiry-threshold <cr>
```

Handler ` RVA 0xBDCB950 `；selector ` 0 `；EOL ` RVA 0x338E8FC8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-97f995338a01165d](../../evidence/conditions-sets-059.md#c-97f995338a01165d) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007410

```text
(config-ecfm-srv)# no lck level <cr>
```

Handler ` RVA 0xBDCB7A0 `；selector ` 0 `；EOL ` RVA 0x338E8CB0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4faebb4f19fda8a4](../../evidence/conditions-sets-031.md#c-4faebb4f19fda8a4) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007399

```text
(config-ecfm-srv)# no lck period <cr>
```

Handler ` RVA 0xBDCB5F0 `；selector ` 0 `；EOL ` RVA 0x338E8928 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b5e8b81dc35dd78b](../../evidence/conditions-sets-070.md#c-b5e8b81dc35dd78b) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007387

```text
(config-ecfm-srv)# no maximum meps <cr>
```

Handler ` RVA 0xBDCA3E0 `；selector ` 0 `；EOL ` RVA 0x338E6E18 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fbee03f53a1e4a01](../../evidence/conditions-sets-097.md#c-fbee03f53a1e4a01) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007419

```text
(config-ecfm-srv)# no mep mpid <number:1..8191> <cr>
```

Handler ` RVA 0xBDC9D70 `；selector ` 0 `；EOL ` RVA 0x338E62C0 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Identifier value。

[条件 C-664e99507f0fc8cf](../../evidence/conditions-sets-040.md#c-664e99507f0fc8cf) · [参数 P-4864123b7bfc62a2](../../evidence/parameters-sets-006.md#p-4864123b7bfc62a2) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007391

```text
(config-ecfm-srv)# no mip auto-create <cr>
```

Handler ` RVA 0xBDCA230 `；selector ` 0 `；EOL ` RVA 0x338E6A00 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-84e2a867afff806c](../../evidence/conditions-sets-051.md#c-84e2a867afff806c) · [状态效果 S-cff0048a4aa28106](../../evidence/state_effects-sets-044.md#s-cff0048a4aa28106)

### observed_connections-007408

```text
(config-ecfm-srv)# no offload sampling <cr>
```

Handler ` RVA 0xBDCBB00 `；selector ` 0 `；EOL ` RVA 0x338E95C8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef970513da2ea711](../../evidence/conditions-sets-093.md#c-ef970513da2ea711) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007364

```text
(config-ecfm-srv)# no sender-id <cr>
```

Handler ` RVA 0xBDCA080 `；selector ` 0 `；EOL ` RVA 0x338E65E8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f651af37b646bb10](../../evidence/conditions-sets-095.md#c-f651af37b646bb10) · [状态效果 S-1dc35fbcc1442f82](../../evidence/state_effects-sets-007.md#s-1dc35fbcc1442f82)

### observed_connections-007423

```text
(config-ecfm-srv)# offload sampling <number:dynamic> <cr>
```

Handler ` RVA 0xBDCBB00 `；selector ` 0 `；EOL ` RVA 0x338E95C8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Sampling rate。

[条件 C-4b9c56c2aed55b8e](../../evidence/conditions-sets-030.md#c-4b9c56c2aed55b8e) · [缺口 G-2a117923b6b345a2](../../evidence/gaps-sets-002.md#g-2a117923b6b345a2) · [参数 P-486e4bcf60a2b5f8](../../evidence/parameters-sets-006.md#p-486e4bcf60a2b5f8)

### observed_connections-007366

```text
(config-ecfm-srv)# sender-id chassis <cr>
```

Handler ` RVA 0xBDCA080 `；selector ` 0 `；EOL ` RVA 0x338E65E8 `。

模式根 ` RVA 0x338CA0A8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fef25d26b7f4448e](../../evidence/conditions-sets-098.md#c-fef25d26b7f4448e) · [状态效果 S-9309bf6809d96479](../../evidence/state_effects-sets-031.md#s-9309bf6809d96479)

