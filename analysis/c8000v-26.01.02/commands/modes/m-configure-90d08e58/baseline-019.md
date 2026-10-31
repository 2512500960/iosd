# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-043349

```text
(config)# default do-exec show object-group parent-list <cr>
```

Handler ` RVA 0xF9FAA80 `；selector ` 0 `；EOL ` RVA 0x347A88F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-042349

```text
(config)# default do-exec show odb client <cr>
```

Handler ` RVA 0x12414120 `；selector ` 0 `；EOL ` RVA 0x35855BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056384

```text
(config)# default do-exec show odb record <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x12414650 `；selector ` 0 `；EOL ` RVA 0x358561E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Higher 32 bits of record handle；` unsigned_number ` Lower 32 bits of record handle。

[条件 C-889ad35d3bb9ccae](../../evidence/conditions-sets-053.md#c-889ad35d3bb9ccae) · [参数 P-88ac05a25c551cf3](../../evidence/parameters-sets-011.md#p-88ac05a25c551cf3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-042362

```text
(config)# default do-exec show odb table <cr>
```

Handler ` RVA 0x124143E0 `；selector ` 0 `；EOL ` RVA 0x35855ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3d2280756fca9c3](../../evidence/conditions-sets-076.md#c-c3d2280756fca9c3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-033641

```text
(config)# default do-exec show odm-format <cr>
```

Handler ` RVA 0xF4149D0 `；selector ` 0 `；EOL ` RVA 0x34642680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bb535702d0316d4b](../../evidence/conditions-sets-072.md#c-bb535702d0316d4b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-042399

```text
(config)# default do-exec show onep status <cr>
```

Handler ` RVA 0x13A7D280 `；selector ` 0 `；EOL ` RVA 0x35CAFB18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8dd154a4a55367f0](../../evidence/conditions-sets-055.md#c-8dd154a4a55367f0) · [状态效果 S-8a76e16ec7041794](../../evidence/state_effects-sets-029.md#s-8a76e16ec7041794)

### path-058737

```text
(config)# default do-exec show opflex agent service vxlan-evpn all <cr>
```

Handler ` RVA 0xC496270 `；selector ` 0 `；EOL ` RVA 0x33A963C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059586

```text
(config)# default do-exec show opflex agent service vxlan-evpn concrete-config all <cr>
```

Handler ` RVA 0xC4963B0 `；selector ` 0 `；EOL ` RVA 0x33A96998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059582

```text
(config)# default do-exec show opflex agent service vxlan-evpn tenant <string> <cr>
```

Handler ` RVA 0xC4962D0 `；selector ` 0 `；EOL ` RVA 0x33A966D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tenant name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-89ba2ccdc27ae0f8](../../evidence/parameters-sets-011.md#p-89ba2ccdc27ae0f8) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050739

```text
(config)# default do-exec show opflex agent session <cr>
```

Handler ` RVA 0xC483680 `；selector ` 0 `；EOL ` RVA 0x33A93118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-033034

```text
(config)# default do-exec show ospfv3 <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 11 `；EOL ` RVA 0x3568C460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2754c109ed50a781](../../evidence/conditions-sets-015.md#c-2754c109ed50a781) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041709

```text
(config)# default do-exec show ospfv3 bad-checksum <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 1 `；EOL ` RVA 0x35670DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-35c4ab5fad939222](../../evidence/conditions-sets-021.md#c-35c4ab5fad939222) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041923

```text
(config)# default do-exec show ospfv3 border-routers <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 10 `；EOL ` RVA 0x35672D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042380

```text
(config)# default do-exec show ospfv3 database <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 29 `；EOL ` RVA 0x35689FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7c78501fb4dedad7](../../evidence/conditions-sets-048.md#c-7c78501fb4dedad7) · [状态效果 S-59e61f7121525c87](../../evidence/state_effects-sets-019.md#s-59e61f7121525c87)

### path-051023

```text
(config)# default do-exec show ospfv3 database database-summary <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 30 `；EOL ` RVA 0x3568C750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-62b37738b01d0361](../../evidence/conditions-sets-038.md#c-62b37738b01d0361) · [状态效果 S-59e61f7121525c87](../../evidence/state_effects-sets-019.md#s-59e61f7121525c87)

### path-056381

```text
(config)# default do-exec show ospfv3 database database-summary detail <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 26 `；EOL ` RVA 0x3568CA70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c81d5891201083e2](../../evidence/conditions-sets-077.md#c-c81d5891201083e2) · [状态效果 S-831777bbc24329aa](../../evidence/state_effects-sets-028.md#s-831777bbc24329aa)

### path-041770

```text
(config)# default do-exec show ospfv3 events <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 7 `；EOL ` RVA 0x356713A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc0cbe3da86d9245](../../evidence/conditions-sets-073.md#c-bc0cbe3da86d9245) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042200

```text
(config)# default do-exec show ospfv3 flood-list <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 37 `；EOL ` RVA 0x3568B660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c007bfc4b362af71](../../evidence/conditions-sets-074.md#c-c007bfc4b362af71) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041840

```text
(config)# default do-exec show ospfv3 graceful-restart <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 20 `；EOL ` RVA 0x35672218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042185

```text
(config)# default do-exec show ospfv3 interface <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 36 `；EOL ` RVA 0x3568AC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0cd16a97b0bac1c9](../../evidence/conditions-sets-005.md#c-0cd16a97b0bac1c9) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-050929

```text
(config)# default do-exec show ospfv3 internal work-queue <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 2 `；EOL ` RVA 0x3568C1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041710

```text
(config)# default do-exec show ospfv3 lsdb-radix <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 6 `；EOL ` RVA 0x35671090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-42a80b284feb87f3](../../evidence/conditions-sets-026.md#c-42a80b284feb87f3) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041970

```text
(config)# default do-exec show ospfv3 max-metric <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 14 `；EOL ` RVA 0x356732C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041993

```text
(config)# default do-exec show ospfv3 maxage-list <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 13 `；EOL ` RVA 0x35673568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-058783

```text
(config)# default do-exec show ospfv3 mpls traffic-eng tunnel interface <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 32 `；EOL ` RVA 0x35CD82E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-058774

```text
(config)# default do-exec show ospfv3 mpls traffic-eng tunnel tail <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 31 `；EOL ` RVA 0x35CD8040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041874

```text
(config)# default do-exec show ospfv3 multi-area <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 39 `；EOL ` RVA 0x35671D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7f31822ef0b6e69](../../evidence/conditions-sets-090.md#c-e7f31822ef0b6e69) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-050609

```text
(config)# default do-exec show ospfv3 multi-area internal <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 3 `；EOL ` RVA 0x35671D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e7f31822ef0b6e69](../../evidence/conditions-sets-090.md#c-e7f31822ef0b6e69) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042335

```text
(config)# default do-exec show ospfv3 neighbor <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 42 `；EOL ` RVA 0x35689818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c9765600e1e7ac95](../../evidence/conditions-sets-078.md#c-c9765600e1e7ac95) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042273

```text
(config)# default do-exec show ospfv3 request-list <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 44 `；EOL ` RVA 0x3568BE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d424ee4acabd708e](../../evidence/conditions-sets-082.md#c-d424ee4acabd708e) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042250

```text
(config)# default do-exec show ospfv3 retransmission-list <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 43 `；EOL ` RVA 0x3568BA88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7578fcf61420f6db](../../evidence/conditions-sets-046.md#c-7578fcf61420f6db) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042107

```text
(config)# default do-exec show ospfv3 rib <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 18 `；EOL ` RVA 0x356738C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2b07e602eed824fd](../../evidence/conditions-sets-017.md#c-2b07e602eed824fd) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042033

```text
(config)# default do-exec show ospfv3 route-lists <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 19 `；EOL ` RVA 0x35673CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041817

```text
(config)# default do-exec show ospfv3 sham-links <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 9 `；EOL ` RVA 0x356719D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d3f3210d3949c416](../../evidence/conditions-sets-082.md#c-d3f3210d3949c416) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041979

```text
(config)# default do-exec show ospfv3 statistic <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 15 `；EOL ` RVA 0x35673020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041897

```text
(config)# default do-exec show ospfv3 summary-prefix <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 12 `；EOL ` RVA 0x35672A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-050631

```text
(config)# default do-exec show ospfv3 timers lsa-group <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 17 `；EOL ` RVA 0x35672528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-050656

```text
(config)# default do-exec show ospfv3 timers rate-limit <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 16 `；EOL ` RVA 0x356727D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f3eb511ea4549278](../../evidence/conditions-sets-094.md#c-f3eb511ea4549278) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-042201

```text
(config)# default do-exec show ospfv3 traffic <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 38 `；EOL ` RVA 0x3568B1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2a3c7d2a7d651f8b](../../evidence/conditions-sets-017.md#c-2a3c7d2a7d651f8b) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-041789

```text
(config)# default do-exec show ospfv3 virtual-links <cr>
```

Handler ` RVA 0x11BF3C40 `；selector ` 8 `；EOL ` RVA 0x356716C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6274e8c9efd4abac](../../evidence/conditions-sets-038.md#c-6274e8c9efd4abac) · [状态效果 S-5dd95ede8d509488](../../evidence/state_effects-sets-020.md#s-5dd95ede8d509488)

### path-038474

```text
(config)# default do-exec show packet-debug pak_debug_tracebuf <cr>
```

Handler ` RVA 0xEB833B0 `；selector ` 0 `；EOL ` RVA 0x343CEB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-044776

```text
(config)# default do-exec show parser atomic-config statistics <cr>
```

Handler ` RVA 0xDF73890 `；selector ` 0 `；EOL ` RVA 0x340AB700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd966ff6641a4178](../../evidence/state_effects-sets-044.md#s-cd966ff6641a4178)

### path-034917

```text
(config)# default do-exec show parser cache <cr>
```

Handler ` RVA 0xE101670 `；selector ` 0 `；EOL ` RVA 0x340AA388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f7627e2a7581b0a](../../evidence/conditions-sets-019.md#c-2f7627e2a7581b0a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-044561

```text
(config)# default do-exec show parser cache <number:0..29> <cr>
```

Handler ` RVA 0xE101670 `；selector ` 1 `；EOL ` RVA 0x340AA360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Display a specific element of the parser cache。

[条件 C-2f7627e2a7581b0a](../../evidence/conditions-sets-019.md#c-2f7627e2a7581b0a) · [参数 P-f4ffc6113b4a8d77](../../evidence/parameters-sets-018.md#p-f4ffc6113b4a8d77) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-044858

```text
(config)# default do-exec show parser csb flags <cr>
```

Handler ` RVA 0xDEE4DB0 `；selector ` 0 `；EOL ` RVA 0x340ABCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052560

```text
(config)# default do-exec show parser encrypt file status <cr>
```

Handler ` RVA 0xDF33A40 `；selector ` 0 `；EOL ` RVA 0x340AABA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034775

```text
(config)# default do-exec show parser links <cr>
```

Handler ` RVA 0xDEF81C0 `；selector ` 0 `；EOL ` RVA 0x340A9B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035003

```text
(config)# default do-exec show parser memory <cr>
```

Handler ` RVA 0xDF00A10 `；selector ` 0 `；EOL ` RVA 0x340AAE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034806

```text
(config)# default do-exec show parser modes <cr>
```

Handler ` RVA 0xDF3C0D0 `；selector ` 0 `；EOL ` RVA 0x340AA050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034903

```text
(config)# default do-exec show parser statistics <cr>
```

Handler ` RVA 0xDF339D0 `；selector ` 0 `；EOL ` RVA 0x340AA850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034763

```text
(config)# default do-exec show parser unresolved <cr>
```

Handler ` RVA 0xDEF8640 `；selector ` 0 `；EOL ` RVA 0x340A9DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035181

```text
(config)# default do-exec show parser view <cr>
```

Handler ` RVA 0xDF73920 `；selector ` 0 `；EOL ` RVA 0x340ABA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048471

```text
(config)# default do-exec show passwd encryption status <cr>
```

Handler ` RVA 0x127F5E10 `；selector ` 4 `；EOL ` RVA 0x358D8300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035409

```text
(config)# default do-exec show persistent variable <cr>
```

Handler ` RVA 0xD7C8060 `；selector ` 0 `；EOL ` RVA 0x33EF5420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-028409

```text
(config)# default do-exec show platform <cr>
```

Handler ` RVA 0x1581F960 `；selector ` 0 `；EOL ` RVA 0x3435D198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-26bb52874214d99f](../../evidence/conditions-sets-015.md#c-26bb52874214d99f) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034450

```text
(config)# default do-exec show platform atm-cdvt <cr>
```

Handler ` RVA 0xE982130 `；selector ` 0 `；EOL ` RVA 0x343626D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052144

```text
(config)# default do-exec show platform authentication session all <cr>
```

Handler ` RVA 0x15E9CA40 `；selector ` 0 `；EOL ` RVA 0x35E58FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056804

```text
(config)# default do-exec show platform authentication session handle <number:1..4294967295> <cr>
```

Handler ` RVA 0x15E9CA40 `；selector ` 1 `；EOL ` RVA 0x35E592F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [参数 P-8027e4d27e013afc](../../evidence/parameters-sets-010.md#p-8027e4d27e013afc) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056838

```text
(config)# default do-exec show platform authentication session mac <address> <cr>
```

Handler ` RVA 0x15E9CA40 `；selector ` 2 `；EOL ` RVA 0x35E598E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` sessions for mac。

[条件 C-5ac077b163d8a150](../../evidence/conditions-sets-036.md#c-5ac077b163d8a150) · [参数 P-a613d424f0be2719](../../evidence/parameters-sets-013.md#p-a613d424f0be2719) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052211

```text
(config)# default do-exec show platform chassis <number:1..2> R0 <cr>
```

Handler ` RVA 0xE9C7FE0 `；selector ` 0 `；EOL ` RVA 0x3437D1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Chassis num。

[条件 C-8bf81c8d2c08a785](../../evidence/conditions-sets-054.md#c-8bf81c8d2c08a785) · [参数 P-ff9315ccbcc69a28](../../evidence/parameters-sets-019.md#p-ff9315ccbcc69a28) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052238

```text
(config)# default do-exec show platform chassis active R0 <cr>
```

Handler ` RVA 0xE9C7C10 `；selector ` 0 `；EOL ` RVA 0x3437D4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bf81c8d2c08a785](../../evidence/conditions-sets-054.md#c-8bf81c8d2c08a785) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052267

```text
(config)# default do-exec show platform chassis standby R0 <cr>
```

Handler ` RVA 0xE9C7E70 `；selector ` 0 `；EOL ` RVA 0x3437D7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bf81c8d2c08a785](../../evidence/conditions-sets-054.md#c-8bf81c8d2c08a785) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034320

```text
(config)# default do-exec show platform conditions <cr>
```

Handler ` RVA 0x158D5C30 `；selector ` 143165576 `；EOL ` RVA 0x35DAF7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-044090

```text
(config)# default do-exec show platform conditions internal <cr>
```

Handler ` RVA 0x158D4B40 `；selector ` 0 `；EOL ` RVA 0x35DAF7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034449

```text
(config)# default do-exec show platform diag <cr>
```

Handler ` RVA 0x1581A830 `；selector ` 0 `；EOL ` RVA 0x3435CE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8c24ac31d2678e56](../../evidence/conditions-sets-054.md#c-8c24ac31d2678e56) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059622

```text
(config)# default do-exec show platform fabric border dhcp snooping ipv4 statistics <cr>
```

Handler ` RVA 0xEACACF0 `；selector ` 0 `；EOL ` RVA 0x343A0480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-899d094b0310a680](../../evidence/state_effects-sets-029.md#s-899d094b0310a680)

### path-044185

```text
(config)# default do-exec show platform packet-trace configuration <cr>
```

Handler ` RVA 0x158D2D80 `；selector ` 0 `；EOL ` RVA 0x35DAFDC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-adb8874585e46cd9](../../evidence/conditions-sets-067.md#c-adb8874585e46cd9) · [状态效果 S-f7a0a96bcaa0b975](../../evidence/state_effects-sets-052.md#s-f7a0a96bcaa0b975)

### path-034537

```text
(config)# default do-exec show platform power <cr>
```

Handler ` RVA 0x1581D830 `；selector ` 0 `；EOL ` RVA 0x3435D170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-847609a8287bdc53](../../evidence/conditions-sets-051.md#c-847609a8287bdc53) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-034324

```text
(config)# default do-exec show platform resources <cr>
```

Handler ` RVA 0x15905880 `；selector ` 0 `；EOL ` RVA 0x35DB6258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-223644ac6fd7aa06](../../evidence/conditions-sets-013.md#c-223644ac6fd7aa06) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-044177

```text
(config)# default do-exec show platform sd status <cr>
```

Handler ` RVA 0xE9C7360 `；selector ` 0 `；EOL ` RVA 0x3437B9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea8ca9b646b85407](../../evidence/conditions-sets-091.md#c-ea8ca9b646b85407) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036400

```text
(config)# default do-exec show platform software <cr>
```

Handler ` RVA 0xC6B1CD0 `；selector ` 0 `；EOL ` RVA 0x33AD2570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057032

```text
(config)# default do-exec show platform software access-list template <string> <cr>
```

Handler ` RVA 0xE5271E0 `；selector ` 0 `；EOL ` RVA 0x342EF918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Access list name。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-050d77a249db07fa](../../evidence/parameters-sets-001.md#p-050d77a249db07fa) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052461

```text
(config)# default do-exec show platform software adjacency counters <cr>
```

Handler ` RVA 0xE567250 `；selector ` 1 `；EOL ` RVA 0x342F3228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056923

```text
(config)# default do-exec show platform software adjacency counters tun-qos-ha <cr>
```

Handler ` RVA 0xE567250 `；selector ` 7 `；EOL ` RVA 0x342F3200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052447

```text
(config)# default do-exec show platform software adjacency nexthop-ipfrr <cr>
```

Handler ` RVA 0xE567250 `；selector ` 2 `；EOL ` RVA 0x342F36F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056974

```text
(config)# default do-exec show platform software adjacency oce <number:1..4294967295> <cr>
```

Handler ` RVA 0xE567250 `；selector ` 3 `；EOL ` RVA 0x342F3C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter OCE Object ID。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-2fe33afd0da0c956](../../evidence/parameters-sets-004.md#p-2fe33afd0da0c956) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-058988

```text
(config)# default do-exec show platform software adjacency oce inlabel <number:1..2147483647> <cr>
```

Handler ` RVA 0xE567250 `；selector ` 5 `；EOL ` RVA 0x342F3FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter MPLS Label Value。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-7bf93034ee420db6](../../evidence/parameters-sets-010.md#p-7bf93034ee420db6) · [状态效果 S-b30a5a8a24d237d2](../../evidence/state_effects-sets-038.md#s-b30a5a8a24d237d2)

### path-052479

```text
(config)# default do-exec show platform software adjacency tunadj <cr>
```

Handler ` RVA 0xE567250 `；selector ` 8 `；EOL ` RVA 0x342F39A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052389

```text
(config)# default do-exec show platform software bfd counters <cr>
```

Handler ` RVA 0x158C95B0 `；selector ` 1 `；EOL ` RVA 0x35DA7EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052423

```text
(config)# default do-exec show platform software bfd pending <cr>
```

Handler ` RVA 0x158C95B0 `；selector ` 3 `；EOL ` RVA 0x35DA81A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052354

```text
(config)# default do-exec show platform software bfd session <cr>
```

Handler ` RVA 0x158C95B0 `；selector ` 2 `；EOL ` RVA 0x35DA7C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052940

```text
(config)# default do-exec show platform software cce statistics <cr>
```

Handler ` RVA 0xE597F40 `；selector ` 1 `；EOL ` RVA 0x342F7D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052131

```text
(config)# default do-exec show platform software cdna all <cr>
```

Handler ` RVA 0xB7C73C0 `；selector ` 0 `；EOL ` RVA 0x3380D088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-c6e296efd3a30c09](../../evidence/state_effects-sets-042.md#s-c6e296efd3a30c09)

### path-052442

```text
(config)# default do-exec show platform software cef counters <cr>
```

Handler ` RVA 0xE5CE560 `；selector ` 1 `；EOL ` RVA 0x342FB450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059691

```text
(config)# default do-exec show platform software cef ipv4 <address> <address> feature-all <cr>
```

Handler ` RVA 0xE5CE560 `；selector ` 2 `；EOL ` RVA 0x342FB9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` prefix of entries to show；` address ` prefix mask。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-27cdb7db3651d282](../../evidence/parameters-sets-003.md#p-27cdb7db3651d282) · [状态效果 S-b9bad22a6e044565](../../evidence/state_effects-sets-039.md#s-b9bad22a6e044565)

### path-053401

```text
(config)# default do-exec show platform software cli-agent counters <cr>
```

Handler ` RVA 0x143F2990 `；selector ` 0 `；EOL ` RVA 0x35D5D3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052148

```text
(config)# default do-exec show platform software cman statistics <cr>
```

Handler ` RVA 0xE3887B0 `；selector ` 1 `；EOL ` RVA 0x342AD3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045707

```text
(config)# default do-exec show platform software consent-token <cr>
```

Handler ` RVA 0x1569AFA0 `；selector ` 0 `；EOL ` RVA 0x35D7B658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053081

```text
(config)# default do-exec show platform software consent-token shell-access <cr>
```

Handler ` RVA 0x1569B220 `；selector ` 0 `；EOL ` RVA 0x35D7B340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-11b25e4eb6c23c61](../../evidence/state_effects-sets-004.md#s-11b25e4eb6c23c61)

### path-057284

```text
(config)# default do-exec show platform software crimson lock request-wait-histogram <cr>
```

Handler ` RVA 0x1444AA50 `；selector ` 6 `；EOL ` RVA 0x35D66460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057253

```text
(config)# default do-exec show platform software crimson lock statistics <cr>
```

Handler ` RVA 0x1444AA50 `；selector ` 4 `；EOL ` RVA 0x35D661B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057277

```text
(config)# default do-exec show platform software crimson notification statistics <cr>
```

Handler ` RVA 0x1444A9E0 `；selector ` 5 `；EOL ` RVA 0x35D66738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057335

```text
(config)# default do-exec show platform software crimson operational audit <cr>
```

Handler ` RVA 0x1444A6F0 `；selector ` 7 `；EOL ` RVA 0x35D6B9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059123

```text
(config)# default do-exec show platform software crimson operational audit baseline <cr>
```

Handler ` RVA 0x1444A6F0 `；selector ` 8 `；EOL ` RVA 0x35D6B9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057288

```text
(config)# default do-exec show platform software crimson operational database <cr>
```

Handler ` RVA 0x1444A6F0 `；selector ` 2 `；EOL ` RVA 0x35D6B6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057316

```text
(config)# default do-exec show platform software crimson operational offload <cr>
```

Handler ` RVA 0x15711870 `；selector ` 0 `；EOL ` RVA 0x35D7F218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059116

```text
(config)# default do-exec show platform software crimson operational offload details <cr>
```

Handler ` RVA 0x15711820 `；selector ` 0 `；EOL ` RVA 0x35D7F1F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d4e0c335d570b14](../../evidence/conditions-sets-042.md#c-6d4e0c335d570b14) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057318

```text
(config)# default do-exec show platform software crimson operational statistics <cr>
```

Handler ` RVA 0x1444A6F0 `；selector ` 0 `；EOL ` RVA 0x35D6B208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059118

```text
(config)# default do-exec show platform software crimson operational statistics idb <cr>
```

Handler ` RVA 0x1444A6F0 `；selector ` 3 `；EOL ` RVA 0x35D6B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059110

```text
(config)# default do-exec show platform software crimson operational statistics table <cr>
```

Handler ` RVA 0x1444A6F0 `；selector ` 1 `；EOL ` RVA 0x35D6AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056802

```text
(config)# default do-exec show platform software dbal ios mqipc-list <cr>
```

Handler ` RVA 0x1571DDC0 `；selector ` 0 `；EOL ` RVA 0x35D82E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056984

```text
(config)# default do-exec show platform software dpidb atm pvc <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 13 `；EOL ` RVA 0x3438E7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c83013e3a7002d0b](../../evidence/conditions-sets-077.md#c-c83013e3a7002d0b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056999

```text
(config)# default do-exec show platform software dpidb atm pvp <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 14 `；EOL ` RVA 0x3438EB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ecfd4a9043a8ccc5](../../evidence/conditions-sets-092.md#c-ecfd4a9043a8ccc5) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052380

```text
(config)# default do-exec show platform software dpidb database <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 4 `；EOL ` RVA 0x3438CA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056842

```text
(config)# default do-exec show platform software dpidb database controller <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 6 `；EOL ` RVA 0x3438BF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056883

```text
(config)# default do-exec show platform software dpidb database l2-vlan <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 16 `；EOL ` RVA 0x3438C750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056825

```text
(config)# default do-exec show platform software dpidb database legacy <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 5 `；EOL ` RVA 0x3438BCB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056898

```text
(config)# default do-exec show platform software dpidb database qos-template <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 17 `；EOL ` RVA 0x3438C9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056858

```text
(config)# default do-exec show platform software dpidb database session <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 7 `；EOL ` RVA 0x3438C200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056871

```text
(config)# default do-exec show platform software dpidb database vfiseg <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 15 `；EOL ` RVA 0x3438C4A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056947

```text
(config)# default do-exec show platform software dpidb ethernet efp <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 12 `；EOL ` RVA 0x3438E368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6896b05021adb6fa](../../evidence/conditions-sets-040.md#c-6896b05021adb6fa) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056949

```text
(config)# default do-exec show platform software dpidb frame-relay pvc <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 8 `；EOL ` RVA 0x3438DF68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84e758a734b90bbc](../../evidence/conditions-sets-051.md#c-84e758a734b90bbc) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052227

```text
(config)# default do-exec show platform software dpidb index <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 2 `；EOL ` RVA 0x3438B9C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056940

```text
(config)# default do-exec show platform software dpidb l2lisp <number:1..16777214> <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 18 `；EOL ` RVA 0x3438EEB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Instance-ID。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-50e249bb6c884128](../../evidence/parameters-sets-007.md#p-50e249bb6c884128) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052378

```text
(config)# default do-exec show platform software dpidb session <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 10 `；EOL ` RVA 0x3438DB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052276

```text
(config)# default do-exec show platform software dpidb spa <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 3 `；EOL ` RVA 0x3438D1D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052250

```text
(config)# default do-exec show platform software dpidb stats <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 1 `；EOL ` RVA 0x3438CF28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052348

```text
(config)# default do-exec show platform software dpidb swidb <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 9 `；EOL ` RVA 0x3438D560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6c9c0be0e6eb7de8](../../evidence/conditions-sets-042.md#c-6c9c0be0e6eb7de8) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052346

```text
(config)# default do-exec show platform software dpidb vlans <cr>
```

Handler ` RVA 0xEA18AD0 `；selector ` 11 `；EOL ` RVA 0x3438D888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052613

```text
(config)# default do-exec show platform software epbr statistics <cr>
```

Handler ` RVA 0x15775BB0 `；selector ` 1 `；EOL ` RVA 0x35D8A168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057009

```text
(config)# default do-exec show platform software epbr statistics flowspec <cr>
```

Handler ` RVA 0x15775BB0 `；selector ` 2 `；EOL ` RVA 0x35D8A140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052545

```text
(config)# default do-exec show platform software epbr track <cr>
```

Handler ` RVA 0x15775BB0 `；selector ` 3 `；EOL ` RVA 0x35D89E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056850

```text
(config)# default do-exec show platform software ethernet efp statistics <cr>
```

Handler ` RVA 0xC0843F0 `；selector ` 1 `；EOL ` RVA 0x3398ECC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052495

```text
(config)# default do-exec show platform software fhs statistics <cr>
```

Handler ` RVA 0x1579CD20 `；selector ` 1 `；EOL ` RVA 0x35D8DD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059040

```text
(config)# default do-exec show platform software flow monitor name <string> <cr>
```

Handler ` RVA 0xE6B1370 `；selector ` 2 `；EOL ` RVA 0x34303D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the monitor to display details。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-d9a984b91271646e](../../evidence/parameters-sets-016.md#p-d9a984b91271646e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052683

```text
(config)# default do-exec show platform software flow statistics <cr>
```

Handler ` RVA 0xE6B1370 `；selector ` 1 `；EOL ` RVA 0x34303A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056870

```text
(config)# default do-exec show platform software flow-control identifiers detail <cr>
```

Handler ` RVA 0xEAFA5D0 `；selector ` 0 `；EOL ` RVA 0x343AA4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056855

```text
(config)# default do-exec show platform software flow-control identifiers pools <cr>
```

Handler ` RVA 0xEAFA800 `；selector ` 0 `；EOL ` RVA 0x343AA228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052698

```text
(config)# default do-exec show platform software icmp statistics <cr>
```

Handler ` RVA 0xE6CEF90 `；selector ` 1 `；EOL ` RVA 0x34306A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052385

```text
(config)# default do-exec show platform software iid all <cr>
```

Handler ` RVA 0x159BB9F0 `；selector ` 1 `；EOL ` RVA 0x35DD1600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053630

```text
(config)# default do-exec show platform software infrastructure bipc <cr>
```

Handler ` RVA 0xE9C18A0 `；selector ` 1 `；EOL ` RVA 0x34376180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053259

```text
(config)# default do-exec show platform software infrastructure chasfs <cr>
```

Handler ` RVA 0xE9C18A0 `；selector ` 4 `；EOL ` RVA 0x34377170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-08396349c2ef3cfb](../../evidence/state_effects-sets-002.md#s-08396349c2ef3cfb)

### path-053300

```text
(config)# default do-exec show platform software infrastructure debug <cr>
```

Handler ` RVA 0xE9C18A0 `；selector ` 5 `；EOL ` RVA 0x34377428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-ca334bbbb50c658f](../../evidence/state_effects-sets-043.md#s-ca334bbbb50c658f)

### path-053213

```text
(config)# default do-exec show platform software infrastructure flowctl <cr>
```

Handler ` RVA 0x15A48580 `；selector ` 0 `；EOL ` RVA 0x35DD9F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053340

```text
(config)# default do-exec show platform software infrastructure inject <cr>
```

Handler ` RVA 0xEA60370 `；selector ` 1 `；EOL ` RVA 0x34395160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057254

```text
(config)# default do-exec show platform software infrastructure integrated-service l2-switch <cr>
```

Handler ` RVA 0x15927830 `；selector ` 0 `；EOL ` RVA 0x35DC32F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059138

```text
(config)# default do-exec show platform software infrastructure lfts sar all <cr>
```

Handler ` RVA 0xE307150 `；selector ` 3 `；EOL ` RVA 0x342A9D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059760

```text
(config)# default do-exec show platform software infrastructure lfts sar ipv4-addr <address> <cr>
```

Handler ` RVA 0xE307150 `；selector ` 1 `；EOL ` RVA 0x342AA0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 destination address。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-c6985a7a41b42699](../../evidence/parameters-sets-015.md#p-c6985a7a41b42699) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059765

```text
(config)# default do-exec show platform software infrastructure lfts sar ipv6-addr <address> <cr>
```

Handler ` RVA 0xE307150 `；selector ` 2 `；EOL ` RVA 0x342AA3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv6 destination address。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-0ee2b849028ae0fe](../../evidence/parameters-sets-002.md#p-0ee2b849028ae0fe) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059128

```text
(config)# default do-exec show platform software infrastructure lfts sar stat <cr>
```

Handler ` RVA 0xE307150 `；selector ` 0 `；EOL ` RVA 0x342A9AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057377

```text
(config)# default do-exec show platform software infrastructure lfts stat <cr>
```

Handler ` RVA 0xE307150 `；selector ` 5 `；EOL ` RVA 0x342AA6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059753

```text
(config)# default do-exec show platform software infrastructure lfts stat vrf <string> <cr>
```

Handler ` RVA 0xE307150 `；selector ` 4 `；EOL ` RVA 0x342AA708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-8f4d310c9ecf359a](../../evidence/parameters-sets-011.md#p-8f4d310c9ecf359a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053260

```text
(config)# default do-exec show platform software infrastructure liin <cr>
```

Handler ` RVA 0xEE94BA0 `；selector ` 0 `；EOL ` RVA 0x34453978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053514

```text
(config)# default do-exec show platform software infrastructure lsmpi <cr>
```

Handler ` RVA 0xED2E720 `；selector ` 0 `；EOL ` RVA 0x3440AE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-b3b53ecdfeb4636e](../../evidence/state_effects-sets-038.md#s-b3b53ecdfeb4636e)

### path-053165

```text
(config)# default do-exec show platform software infrastructure packet <cr>
```

Handler ` RVA 0xE9C18A0 `；selector ` 2 `；EOL ` RVA 0x34376B10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053475

```text
(config)# default do-exec show platform software infrastructure punt-keepalive <cr>
```

Handler ` RVA 0xEA5FC90 `；selector ` 1 `；EOL ` RVA 0x34395A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059170

```text
(config)# default do-exec show platform software infrastructure punt-keepalive statistics esp <cr>
```

Handler ` RVA 0xEA5FC30 `；selector ` 1 `；EOL ` RVA 0x34395A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053224

```text
(config)# default do-exec show platform software infrastructure query <cr>
```

Handler ` RVA 0xE306F30 `；selector ` 0 `；EOL ` RVA 0x342A9530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057306

```text
(config)# default do-exec show platform software infrastructure query rwatch <cr>
```

Handler ` RVA 0xE3070F0 `；selector ` 0 `；EOL ` RVA 0x342A9508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-133830bac9146812](../../evidence/conditions-sets-008.md#c-133830bac9146812) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053174

```text
(config)# default do-exec show platform software infrastructure scheduler <cr>
```

Handler ` RVA 0xE8E7C60 `；selector ` 1 `；EOL ` RVA 0x3433D758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057278

```text
(config)# default do-exec show platform software infrastructure scheduler detail <cr>
```

Handler ` RVA 0xE8E7C60 `；selector ` 2 `；EOL ` RVA 0x3433D730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053308

```text
(config)# default do-exec show platform software infrastructure session <cr>
```

Handler ` RVA 0xE9C18A0 `；selector ` 3 `；EOL ` RVA 0x34376EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-ddd9ea0f56cec23e](../../evidence/state_effects-sets-047.md#s-ddd9ea0f56cec23e)

### path-053349

```text
(config)# default do-exec show platform software infrastructure thread <cr>
```

Handler ` RVA 0xE9C18A0 `；selector ` 0 `；EOL ` RVA 0x34375BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059642

```text
(config)# default do-exec show platform software l2fib-iosd bdomain <number:1..65535> v4 stats <cr>
```

Handler ` RVA 0xC85A640 `；selector ` 0 `；EOL ` RVA 0x33B02050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` bridge-domain ID。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-48a0c231125f9ec8](../../evidence/parameters-sets-006.md#p-48a0c231125f9ec8) · [状态效果 S-e0e8c5443920e136](../../evidence/state_effects-sets-048.md#s-e0e8c5443920e136)

### path-052316

```text
(config)# default do-exec show platform software l2fib-iosd mac-statistics <cr>
```

Handler ` RVA 0xC85AB10 `；selector ` 0 `；EOL ` RVA 0x33B02330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052590

```text
(config)# default do-exec show platform software l2pt statistics <cr>
```

Handler ` RVA 0x15FE9620 `；selector ` 1 `；EOL ` RVA 0x35E92368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057274

```text
(config)# default do-exec show platform software macsec classify-pattern all <cr>
```

Handler ` RVA 0x160DB170 `；selector ` 84 `；EOL ` RVA 0x35EC2D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059122

```text
(config)# default do-exec show platform software macsec classify-pattern name <string> <cr>
```

Handler ` RVA 0x160DB170 `；selector ` 39 `；EOL ` RVA 0x35EC3018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` pattern name。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-a71e81cb52fee682](../../evidence/parameters-sets-013.md#p-a71e81cb52fee682) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057325

```text
(config)# default do-exec show platform software macsec secy config-all <cr>
```

Handler ` RVA 0x160DB170 `；selector ` 85 `；EOL ` RVA 0x35EC36C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052309

```text
(config)# default do-exec show platform software mlppp counters <cr>
```

Handler ` RVA 0xE70B070 `；selector ` 1 `；EOL ` RVA 0x34315650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059019

```text
(config)# default do-exec show platform software multicast ipv4 mfib-summary <address> <cr>
```

Handler ` RVA 0xE6F5380 `；selector ` 2 `；EOL ` RVA 0x3430B158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Group IPv4 address。

[条件 C-a297d8b2cbaaa31a](../../evidence/conditions-sets-063.md#c-a297d8b2cbaaa31a) · [参数 P-8bc9aeb53ea441cf](../../evidence/parameters-sets-011.md#p-8bc9aeb53ea441cf) · [状态效果 S-26b4def54e3e198d](../../evidence/state_effects-sets-009.md#s-26b4def54e3e198d)

### path-057030

```text
(config)# default do-exec show platform software multicast mfib-summary <address> <cr>
```

Handler ` RVA 0xE6F5380 `；selector ` 2 `；EOL ` RVA 0x3430B670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Group IPv6 address。

[条件 C-a297d8b2cbaaa31a](../../evidence/conditions-sets-063.md#c-a297d8b2cbaaa31a) · [参数 P-5d168b273192b2d1](../../evidence/parameters-sets-007.md#p-5d168b273192b2d1) · [状态效果 S-cb8e900a6226e8ea](../../evidence/state_effects-sets-043.md#s-cb8e900a6226e8ea)

### path-058975

```text
(config)# default do-exec show platform software multicast retry mroute ipv4 <cr>
```

Handler ` RVA 0xE6F5380 `；selector ` 3 `；EOL ` RVA 0x3430A700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db9bb5314288ad25](../../evidence/conditions-sets-085.md#c-db9bb5314288ad25) · [状态效果 S-7504a456b996b452](../../evidence/state_effects-sets-025.md#s-7504a456b996b452)

### path-058989

```text
(config)# default do-exec show platform software multicast retry mroute ipv6 <cr>
```

Handler ` RVA 0xE6F5380 `；selector ` 3 `；EOL ` RVA 0x3430A9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db9bb5314288ad25](../../evidence/conditions-sets-085.md#c-db9bb5314288ad25) · [状态效果 S-365f23519618a64d](../../evidence/state_effects-sets-012.md#s-365f23519618a64d)

### path-052500

```text
(config)# default do-exec show platform software multicast stats <cr>
```

Handler ` RVA 0xE6F5380 `；selector ` 1 `；EOL ` RVA 0x3430AC70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a297d8b2cbaaa31a](../../evidence/conditions-sets-063.md#c-a297d8b2cbaaa31a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052844

```text
(config)# default do-exec show platform software nat counters <cr>
```

Handler ` RVA 0x10D452B0 `；selector ` 1 `；EOL ` RVA 0x34D16008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052884

```text
(config)# default do-exec show platform software nat ipalias <cr>
```

Handler ` RVA 0x10D452B0 `；selector ` 2 `；EOL ` RVA 0x34D162B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052926

```text
(config)# default do-exec show platform software nat static-route <cr>
```

Handler ` RVA 0x10D452B0 `；selector ` 3 `；EOL ` RVA 0x34D16558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057168

```text
(config)# default do-exec show platform software nat wlan session <cr>
```

Handler ` RVA 0x10D452B0 `；selector ` 4 `；EOL ` RVA 0x34D16840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052718

```text
(config)# default do-exec show platform software nat64 statistics <cr>
```

Handler ` RVA 0xE72D4A0 `；selector ` 0 `；EOL ` RVA 0x3431D4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052732

```text
(config)# default do-exec show platform software nat66 statistics <cr>
```

Handler ` RVA 0xE733B20 `；selector ` 0 `；EOL ` RVA 0x34321860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052620

```text
(config)# default do-exec show platform software nbar statistics <cr>
```

Handler ` RVA 0xE77FD40 `；selector ` 1 `；EOL ` RVA 0x34330F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052757

```text
(config)# default do-exec show platform software netflow statistics <cr>
```

Handler ` RVA 0xE73C4A0 `；selector ` 1 `；EOL ` RVA 0x34324878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052646

```text
(config)# default do-exec show platform software nwpi counters <cr>
```

Handler ` RVA 0xC6A00F0 `；selector ` 0 `；EOL ` RVA 0x33AD0950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052777

```text
(config)# default do-exec show platform software pfr statistics <cr>
```

Handler ` RVA 0xE74FAD0 `；selector ` 1 `；EOL ` RVA 0x34325D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053280

```text
(config)# default do-exec show platform software pkt-reorder cfg <cr>
```

Handler ` RVA 0xC731260 `；selector ` 12 `；EOL ` RVA 0x33AD68C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057460

```text
(config)# default do-exec show platform software pkt-reorder ctx sdwan <cr>
```

Handler ` RVA 0xC7313C0 `；selector ` 14 `；EOL ` RVA 0x33AD6ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-42aadb35e9b0d8c3](../../evidence/state_effects-sets-015.md#s-42aadb35e9b0d8c3)

### path-059158

```text
(config)# default do-exec show platform software pkt-reorder ctx sdwan <number:1..512> <cr>
```

Handler ` RVA 0xC731840 `；selector ` 15 `；EOL ` RVA 0x33AD6EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Context ID。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-65b53651b66a09df](../../evidence/parameters-sets-008.md#p-65b53651b66a09df) · [状态效果 S-42aadb35e9b0d8c3](../../evidence/state_effects-sets-015.md#s-42aadb35e9b0d8c3)

### path-053328

```text
(config)# default do-exec show platform software pkt-reorder stats <cr>
```

Handler ` RVA 0xC731360 `；selector ` 13 `；EOL ` RVA 0x33AD6B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059174

```text
(config)# default do-exec show platform software plim qos class-map all <cr>
```

Handler ` RVA 0xE948E00 `；selector ` 0 `；EOL ` RVA 0x3434DA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-8d91753b149c2653](../../evidence/state_effects-sets-030.md#s-8d91753b149c2653)

### path-060145

```text
(config)# default do-exec show platform software qos class statistics class-group <number:0..4294967294> class <number:0..4294967294> <cr>
```

Handler ` RVA 0x10D7A290 `；selector ` 2 `；EOL ` RVA 0x34D1A808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` ID；` unsigned_number ` ID。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-4184fa7506499208](../../evidence/parameters-sets-006.md#p-4184fa7506499208) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053059

```text
(config)# default do-exec show platform software qos database <cr>
```

Handler ` RVA 0x10D7A290 `；selector ` 3 `；EOL ` RVA 0x34D1ADF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052985

```text
(config)# default do-exec show platform software qos statistics <cr>
```

Handler ` RVA 0x10D7A290 `；selector ` 1 `；EOL ` RVA 0x34D1AAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053132

```text
(config)# default do-exec show platform software qos template <cr>
```

Handler ` RVA 0x10D7A290 `；selector ` 4 `；EOL ` RVA 0x34D1B178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-734ee218014e8605](../../evidence/conditions-sets-045.md#c-734ee218014e8605) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057116

```text
(config)# default do-exec show platform software route-map client all <cr>
```

Handler ` RVA 0xE773610 `；selector ` 3 `；EOL ` RVA 0x3432EDF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059073

```text
(config)# default do-exec show platform software route-map client route-map <string> <cr>
```

Handler ` RVA 0xE773610 `；selector ` 2 `；EOL ` RVA 0x3432F0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` route-map name。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [参数 P-6b807fe7109b3e27](../../evidence/parameters-sets-008.md#p-6b807fe7109b3e27) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052792

```text
(config)# default do-exec show platform software route-map counters <cr>
```

Handler ` RVA 0xE773610 `；selector ` 1 `；EOL ` RVA 0x3432EB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057238

```text
(config)# default do-exec show platform software shell command connection <cr>
```

Handler ` RVA 0xEB0CE20 `；selector ` 0 `；EOL ` RVA 0x343B2B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057296

```text
(config)# default do-exec show platform software shell command package <cr>
```

Handler ` RVA 0xEB0DC00 `；selector ` 0 `；EOL ` RVA 0x343B27B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-33efdc8e793b5361](../../evidence/state_effects-sets-011.md#s-33efdc8e793b5361)

### path-057216

```text
(config)# default do-exec show platform software shell command set <cr>
```

Handler ` RVA 0xEB0D3D0 `；selector ` 0 `；EOL ` RVA 0x343B2268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059099

```text
(config)# default do-exec show platform software shell command set detail <cr>
```

Handler ` RVA 0xEB0D5C0 `；selector ` 0 `；EOL ` RVA 0x343B2240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-057204

```text
(config)# default do-exec show platform software shell manager statistics <cr>
```

Handler ` RVA 0xEB0D2C0 `；selector ` 0 `；EOL ` RVA 0x343B2DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052201

```text
(config)# default do-exec show platform software sl-infra all <cr>
```

Handler ` RVA 0x15880740 `；selector ` 0 `；EOL ` RVA 0x35D9DC60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052176

```text
(config)# default do-exec show platform software sl-infra current <cr>
```

Handler ` RVA 0x158805C0 `；selector ` 0 `；EOL ` RVA 0x35D9D9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052137

```text
(config)# default do-exec show platform software sl-infra debug <cr>
```

Handler ` RVA 0x158808B0 `；selector ` 0 `；EOL ` RVA 0x35D9D468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052117

```text
(config)# default do-exec show platform software sl-infra pak-info <cr>
```

Handler ` RVA 0x15880840 `；selector ` 0 `；EOL ` RVA 0x35D9D1C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-052154

```text
(config)# default do-exec show platform software sl-infra stored <cr>
```

Handler ` RVA 0x15880680 `；selector ` 0 `；EOL ` RVA 0x35D9D710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-056840

```text
(config)# default do-exec show platform software spi4 headers pools <cr>
```

Handler ` RVA 0xEAEE3B0 `；selector ` 0 `；EOL ` RVA 0x343A9138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053448

```text
(config)# default do-exec show platform software system all <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 1 `；EOL ` RVA 0x35D92038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053655

```text
(config)# default do-exec show platform software system boot <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 7 `；EOL ` RVA 0x35D92D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053624

```text
(config)# default do-exec show platform software system hypervisor <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 5 `；EOL ` RVA 0x35D92AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053721

```text
(config)# default do-exec show platform software system license <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 6 `；EOL ` RVA 0x35D93090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059219

```text
(config)# default do-exec show platform software system license metering detail <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 9 `；EOL ` RVA 0x35D93378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059227

```text
(config)# default do-exec show platform software system license metering report <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 10 `；EOL ` RVA 0x35D93620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-059212

```text
(config)# default do-exec show platform software system license metering status <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 8 `；EOL ` RVA 0x35D930D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053544

```text
(config)# default do-exec show platform software system memory <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 3 `；EOL ` RVA 0x35D92588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053498

```text
(config)# default do-exec show platform software system processor <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 2 `；EOL ` RVA 0x35D922E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053587

```text
(config)# default do-exec show platform software system vnic <cr>
```

Handler ` RVA 0x1583EB20 `；selector ` 4 `；EOL ` RVA 0x35D92830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-044659

```text
(config)# default do-exec show platform software timestamp-engine <cr>
```

Handler ` RVA 0x15AA0B40 `；selector ` 1 `；EOL ` RVA 0x35DE6630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053193

```text
(config)# default do-exec show platform software vmemory info <cr>
```

Handler ` RVA 0xBB65A40 `；selector ` 0 `；EOL ` RVA 0x33869BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053385

```text
(config)# default do-exec show platform software vnic-if interface-mapping <cr>
```

Handler ` RVA 0x15A6DD00 `；selector ` 0 `；EOL ` RVA 0x35DE4190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-9e87777ecf326312](../../evidence/state_effects-sets-034.md#s-9e87777ecf326312)

### path-052516

```text
(config)# default do-exec show platform software vrf statistics <cr>
```

Handler ` RVA 0xE786770 `；selector ` 0 `；EOL ` RVA 0x343346B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045320

```text
(config)# default do-exec show platform software vty <cr>
```

Handler ` RVA 0xEB36890 `；selector ` 0 `；EOL ` RVA 0x343B5990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-2b224c1c6963bb68](../../evidence/state_effects-sets-010.md#s-2b224c1c6963bb68)

### path-045489

```text
(config)# default do-exec show platform software wccp <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 1 `；EOL ` RVA 0x34336B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88a272da3431187e](../../evidence/conditions-sets-053.md#c-88a272da3431187e) · [状态效果 S-4f8ccaf2813a8fa2](../../evidence/state_effects-sets-017.md#s-4f8ccaf2813a8fa2)

### path-057207

```text
(config)# default do-exec show platform software wccp interface counters <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 4 `；EOL ` RVA 0x34336BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88a272da3431187e](../../evidence/conditions-sets-053.md#c-88a272da3431187e) · [状态效果 S-4f8ccaf2813a8fa2](../../evidence/state_effects-sets-017.md#s-4f8ccaf2813a8fa2)

### path-057237

```text
(config)# default do-exec show platform software wccp interface list <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 5 `；EOL ` RVA 0x34336E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88a272da3431187e](../../evidence/conditions-sets-053.md#c-88a272da3431187e) · [状态效果 S-4f8ccaf2813a8fa2](../../evidence/state_effects-sets-017.md#s-4f8ccaf2813a8fa2)

### path-052988

```text
(config)# default do-exec show platform software wccp statistics <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 3 `；EOL ` RVA 0x343368A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88a272da3431187e](../../evidence/conditions-sets-053.md#c-88a272da3431187e) · [状态效果 S-4f8ccaf2813a8fa2](../../evidence/state_effects-sets-017.md#s-4f8ccaf2813a8fa2)

### path-057191

```text
(config)# default do-exec show platform software wccp web-cache counters <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 6 `；EOL ` RVA 0x34335FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-49ebfffae1dfe833](../../evidence/state_effects-sets-016.md#s-49ebfffae1dfe833)

### path-057240

```text
(config)# default do-exec show platform software wccp web-cache info <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 7 `；EOL ` RVA 0x34336520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-49ebfffae1dfe833](../../evidence/state_effects-sets-016.md#s-49ebfffae1dfe833)

### path-057212

```text
(config)# default do-exec show platform software wccp web-cache merged-acl <cr>
```

Handler ` RVA 0xE7AD2E0 `；selector ` 2 `；EOL ` RVA 0x34336278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db3852e630d6dcf0](../../evidence/conditions-sets-084.md#c-db3852e630d6dcf0) · [状态效果 S-49ebfffae1dfe833](../../evidence/state_effects-sets-016.md#s-49ebfffae1dfe833)

### path-044205

```text
(config)# default do-exec show platform usb status <cr>
```

Handler ` RVA 0xE9C7220 `；selector ` 0 `；EOL ` RVA 0x3437BC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea8ca9b646b85407](../../evidence/conditions-sets-091.md#c-ea8ca9b646b85407) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-051978

```text
(config)# default do-exec show pm vlan <number:1..4095> <cr>
```

Handler ` RVA 0x15D58330 `；selector ` 0 `；EOL ` RVA 0x35E21878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan id。

[条件 C-fd9fffdebe7fff43](../../evidence/conditions-sets-098.md#c-fd9fffdebe7fff43) · [参数 P-1a1947a9dde9ee2e](../../evidence/parameters-sets-002.md#p-1a1947a9dde9ee2e) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043782

```text
(config)# default do-exec show pnp all-summary <cr>
```

Handler ` RVA 0xC9F9D40 `；selector ` 0 `；EOL ` RVA 0x33B47128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043888

```text
(config)# default do-exec show pnp auto-install-tech-support <cr>
```

Handler ` RVA 0xCA433E0 `；selector ` 0 `；EOL ` RVA 0x33B4C910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043861

```text
(config)# default do-exec show pnp beacon-info <cr>
```

Handler ` RVA 0xCA43A50 `；selector ` 0 `；EOL ` RVA 0x33B4A3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fbb88f0ddbef759d](../../evidence/conditions-sets-097.md#c-fbb88f0ddbef759d) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043868

```text
(config)# default do-exec show pnp bootstrap <cr>
```

Handler ` RVA 0xCA6F7F0 `；selector ` 0 `；EOL ` RVA 0x33B4AE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043848

```text
(config)# default do-exec show pnp capabilities <cr>
```

Handler ` RVA 0xCA42460 `；selector ` 0 `；EOL ` RVA 0x33B493B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043886

```text
(config)# default do-exec show pnp cco <cr>
```

Handler ` RVA 0xCA42E60 `；selector ` 0 `；EOL ` RVA 0x33B4C668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043840

```text
(config)# default do-exec show pnp cert-info <cr>
```

Handler ` RVA 0xCA428C0 `；selector ` 0 `；EOL ` RVA 0x33B48910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043838

```text
(config)# default do-exec show pnp cmd-info <cr>
```

Handler ` RVA 0xCA41FB0 `；selector ` 0 `；EOL ` RVA 0x33B48668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043836

```text
(config)# default do-exec show pnp config-info <cr>
```

Handler ` RVA 0xCA41F30 `；selector ` 0 `；EOL ` RVA 0x33B483C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043846

```text
(config)# default do-exec show pnp device-info <cr>
```

Handler ` RVA 0xCA424D0 `；selector ` 0 `；EOL ` RVA 0x33B49108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043752

```text
(config)# default do-exec show pnp diagnostic <cr>
```

Handler ` RVA 0xC9A4810 `；selector ` 0 `；EOL ` RVA 0x33B46138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043844

```text
(config)# default do-exec show pnp dir-info <cr>
```

Handler ` RVA 0xCA42540 `；selector ` 0 `；EOL ` RVA 0x33B48E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043866

```text
(config)# default do-exec show pnp discovery-info <cr>
```

Handler ` RVA 0xCA420C0 `；selector ` 0 `；EOL ` RVA 0x33B4ABD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043777

```text
(config)# default do-exec show pnp discovery-summary <cr>
```

Handler ` RVA 0xC9F9A90 `；selector ` 0 `；EOL ` RVA 0x33B46E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043884

```text
(config)# default do-exec show pnp dns <cr>
```

Handler ` RVA 0xCA42ED0 `；selector ` 0 `；EOL ` RVA 0x33B4C3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043771

```text
(config)# default do-exec show pnp error-summary <cr>
```

Handler ` RVA 0xC9F9C10 `；selector ` 0 `；EOL ` RVA 0x33B46BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043874

```text
(config)# default do-exec show pnp errors <cr>
```

Handler ` RVA 0xCA43090 `；selector ` 0 `；EOL ` RVA 0x33B4B678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043842

```text
(config)# default do-exec show pnp fs-info <cr>
```

Handler ` RVA 0xCA425B0 `；selector ` 0 `；EOL ` RVA 0x33B48BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043764

```text
(config)# default do-exec show pnp history <cr>
```

Handler ` RVA 0xC9A46B0 `；selector ` 0 `；EOL ` RVA 0x33B46688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043872

```text
(config)# default do-exec show pnp idb <cr>
```

Handler ` RVA 0xCA427E0 `；selector ` 0 `；EOL ` RVA 0x33B4B3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043870

```text
(config)# default do-exec show pnp image <cr>
```

Handler ` RVA 0xCA42850 `；selector ` 0 `；EOL ` RVA 0x33B4B128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043738

```text
(config)# default do-exec show pnp listener <cr>
```

Handler ` RVA 0xCA43910 `；selector ` 0 `；EOL ` RVA 0x33B45828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043830

```text
(config)# default do-exec show pnp locks <cr>
```

Handler ` RVA 0xCA42020 `；selector ` 0 `；EOL ` RVA 0x33B48118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043825

```text
(config)# default do-exec show pnp monitor-info <cr>
```

Handler ` RVA 0xCA42070 `；selector ` 0 `；EOL ` RVA 0x33B47E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043816

```text
(config)# default do-exec show pnp monitor-logging <cr>
```

Handler ` RVA 0xC9A48C0 `；selector ` 0 `；EOL ` RVA 0x33B47BC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043729

```text
(config)# default do-exec show pnp profile <cr>
```

Handler ` RVA 0xCA437B0 `；selector ` 0 `；EOL ` RVA 0x33B453D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043878

```text
(config)# default do-exec show pnp reconfig <cr>
```

Handler ` RVA 0xCA42DF0 `；selector ` 0 `；EOL ` RVA 0x33B4BBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043806

```text
(config)# default do-exec show pnp reload-info <cr>
```

Handler ` RVA 0xCA42B40 `；selector ` 0 `；EOL ` RVA 0x33B47920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043767

```text
(config)# default do-exec show pnp reload-summary <cr>
```

Handler ` RVA 0xC9F9B50 `；selector ` 0 `；EOL ` RVA 0x33B46930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043854

```text
(config)# default do-exec show pnp request <cr>
```

Handler ` RVA 0xCA42310 `；selector ` 0 `；EOL ` RVA 0x33B49BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043858

```text
(config)# default do-exec show pnp schema <cr>
```

Handler ` RVA 0xCA43260 `；selector ` 0 `；EOL ` RVA 0x33B4A0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043882

```text
(config)# default do-exec show pnp script <cr>
```

Handler ` RVA 0xCA42FB0 `；selector ` 0 `；EOL ` RVA 0x33B4C118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043744

```text
(config)# default do-exec show pnp sdwan-onboarding <cr>
```

Handler ` RVA 0xCA42190 `；selector ` 0 `；EOL ` RVA 0x33B45E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043856

```text
(config)# default do-exec show pnp services <cr>
```

Handler ` RVA 0xCA42290 `；selector ` 0 `；EOL ` RVA 0x33B49E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043880

```text
(config)# default do-exec show pnp smu <cr>
```

Handler ` RVA 0xCA42F40 `；selector ` 0 `；EOL ` RVA 0x33B4BE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043862

```text
(config)# default do-exec show pnp stack-info <cr>
```

Handler ` RVA 0xCA439A0 `；selector ` 0 `；EOL ` RVA 0x33B4A688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043864

```text
(config)# default do-exec show pnp stats <cr>
```

Handler ` RVA 0xCA42210 `；selector ` 0 `；EOL ` RVA 0x33B4A930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043852

```text
(config)# default do-exec show pnp task <cr>
```

Handler ` RVA 0xCA42390 `；selector ` 0 `；EOL ` RVA 0x33B49900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043890

```text
(config)# default do-exec show pnp tech-support <cr>
```

Handler ` RVA 0xCA43610 `；selector ` 0 `；EOL ` RVA 0x33B4CBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043876

```text
(config)# default do-exec show pnp time <cr>
```

Handler ` RVA 0xCA43040 `；selector ` 0 `；EOL ` RVA 0x33B4B920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9fcc7a71c40e22ef](../../evidence/conditions-sets-062.md#c-9fcc7a71c40e22ef) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043850

```text
(config)# default do-exec show pnp topology <cr>
```

Handler ` RVA 0xCA42B90 `；selector ` 0 `；EOL ` RVA 0x33B49658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043734

```text
(config)# default do-exec show pnp trace <cr>
```

Handler ` RVA 0xC9A4760 `；selector ` 0 `；EOL ` RVA 0x33B45BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043787

```text
(config)# default do-exec show pnp udi <cr>
```

Handler ` RVA 0xCA42410 `；selector ` 0 `；EOL ` RVA 0x33B473D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043796

```text
(config)# default do-exec show pnp version <cr>
```

Handler ` RVA 0xCA42950 `；selector ` 0 `；EOL ` RVA 0x33B47678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043758

```text
(config)# default do-exec show pnp webui <cr>
```

Handler ` RVA 0xC9E5CD0 `；selector ` 0 `；EOL ` RVA 0x33B463E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043114

```text
(config)# default do-exec show policy-manager events <cr>
```

Handler ` RVA 0xE10BE00 `；selector ` 0 `；EOL ` RVA 0x34205478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043204

```text
(config)# default do-exec show policy-manager policy <cr>
```

Handler ` RVA 0xE10F310 `；selector ` 0 `；EOL ` RVA 0x34204ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-07710d8249739e72](../../evidence/state_effects-sets-002.md#s-07710d8249739e72)

### path-043186

```text
(config)# default do-exec show policy-manager subsystem <cr>
```

Handler ` RVA 0xE109AC0 `；selector ` 0 `；EOL ` RVA 0x34205820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-98fab00510544ae6](../../evidence/conditions-sets-059.md#c-98fab00510544ae6) · [状态效果 S-21514a46b5728012](../../evidence/state_effects-sets-008.md#s-21514a46b5728012)

### path-032622

```text
(config)# default do-exec show policy-map <cr>
```

Handler ` RVA 0xD888CF0 `；selector ` 0 `；EOL ` RVA 0x33F247E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4a1cb70dec61c348](../../evidence/conditions-sets-029.md#c-4a1cb70dec61c348) · [状态效果 S-290359279e849192](../../evidence/state_effects-sets-009.md#s-290359279e849192)

### path-041539

```text
(config)# default do-exec show policy-map <string> <cr>
```

Handler ` RVA 0xD8889B0 `；selector ` 0 `；EOL ` RVA 0x33F24850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy-map name。

[条件 C-4a1cb70dec61c348](../../evidence/conditions-sets-029.md#c-4a1cb70dec61c348) · [参数 P-8e5848c82238ee3a](../../evidence/parameters-sets-011.md#p-8e5848c82238ee3a) · [状态效果 S-290359279e849192](../../evidence/state_effects-sets-009.md#s-290359279e849192)

### path-056009

```text
(config)# default do-exec show policy-map <string> class <string> <cr>
```

Handler ` RVA 0xD88ACA0 `；selector ` 0 `；EOL ` RVA 0x33F24890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy-map name；` string ` class-map name。

[条件 C-4a1cb70dec61c348](../../evidence/conditions-sets-029.md#c-4a1cb70dec61c348) · [参数 P-804c6938b073fff8](../../evidence/parameters-sets-010.md#p-804c6938b073fff8) · [状态效果 S-290359279e849192](../../evidence/state_effects-sets-009.md#s-290359279e849192)

### path-050196

```text
(config)# default do-exec show policy-map application handles <cr>
```

Handler ` RVA 0x12844890 `；selector ` 0 `；EOL ` RVA 0x358F2B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f893f7d9e7163cf](../../evidence/conditions-sets-031.md#c-4f893f7d9e7163cf) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041062

```text
(config)# default do-exec show policy-map control <cr>
```

Handler ` RVA 0x10A70140 `；selector ` 0 `；EOL ` RVA 0x34C740B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f893f7d9e7163cf](../../evidence/conditions-sets-031.md#c-4f893f7d9e7163cf) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041429

```text
(config)# default do-exec show policy-map multipoint <cr>
```

Handler ` RVA 0xD88A100 `；selector ` 0 `；EOL ` RVA 0x33F1FA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e01a7138d8af604](../../evidence/conditions-sets-055.md#c-8e01a7138d8af604) · [状态效果 S-253e828acb5c469e](../../evidence/state_effects-sets-008.md#s-253e828acb5c469e)

### path-058674

```text
(config)# default do-exec show policy-map multipoint input class <string> <cr>
```

Handler ` RVA 0xD88A100 `；selector ` 0 `；EOL ` RVA 0x33F1FDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` class-map name。

[条件 C-1c535b1be3eece7e](../../evidence/conditions-sets-011.md#c-1c535b1be3eece7e) · [参数 P-2e89626147cf96e5](../../evidence/parameters-sets-004.md#p-2e89626147cf96e5) · [状态效果 S-45c5ea871b606d38](../../evidence/state_effects-sets-015.md#s-45c5ea871b606d38)

### path-050192

```text
(config)# default do-exec show policy-map policy-handle <string> <cr>
```

Handler ` RVA 0x12844C60 `；selector ` 0 `；EOL ` RVA 0x358F2EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map handle。

[条件 C-4f893f7d9e7163cf](../../evidence/conditions-sets-031.md#c-4f893f7d9e7163cf) · [参数 P-d35bfc7ac1ab86fa](../../evidence/parameters-sets-016.md#p-d35bfc7ac1ab86fa) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041099

```text
(config)# default do-exec show policy-map service <cr>
```

Handler ` RVA 0x10A47290 `；selector ` 0 `；EOL ` RVA 0x34C27F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f893f7d9e7163cf](../../evidence/conditions-sets-031.md#c-4f893f7d9e7163cf) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041501

```text
(config)# default do-exec show policy-map session <cr>
```

Handler ` RVA 0xD88A410 `；selector ` 0 `；EOL ` RVA 0x33F23808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0d39afcb72a03be3](../../evidence/conditions-sets-005.md#c-0d39afcb72a03be3) · [状态效果 S-aa8d631f7949f054](../../evidence/state_effects-sets-036.md#s-aa8d631f7949f054)

### path-050492

```text
(config)# default do-exec show policy-map session brief <cr>
```

Handler ` RVA 0xD889230 `；selector ` 0 `；EOL ` RVA 0x33F211B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [状态效果 S-aa8d631f7949f054](../../evidence/state_effects-sets-036.md#s-aa8d631f7949f054)

### path-056085

```text
(config)# default do-exec show policy-map session brief <string> <cr>
```

Handler ` RVA 0xD889230 `；selector ` 0 `；EOL ` RVA 0x33F22138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-99dba195064e9170](../../evidence/state_effects-sets-033.md#s-99dba195064e9170)

### path-058694

```text
(config)# default do-exec show policy-map session brief <string> timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 2 `；EOL ` RVA 0x33F21EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-26949db233ed4ffe](../../evidence/state_effects-sets-009.md#s-26949db233ed4ffe)

### path-058700

```text
(config)# default do-exec show policy-map session brief <string> vrf <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F21BD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[条件 C-40770bc8a4c52717](../../evidence/conditions-sets-025.md#c-40770bc8a4c52717) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-4dde417346301bec](../../evidence/state_effects-sets-017.md#s-4dde417346301bec)

### path-059569

```text
(config)# default do-exec show policy-map session brief <string> vrf <string> <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F21948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name；` string ` VRF name。

[条件 C-40770bc8a4c52717](../../evidence/conditions-sets-025.md#c-40770bc8a4c52717) · [参数 P-3dbd6dbc914eb89a](../../evidence/parameters-sets-005.md#p-3dbd6dbc914eb89a) · [状态效果 S-86a35598d8f78ce9](../../evidence/state_effects-sets-029.md#s-86a35598d8f78ce9)

### path-059925

```text
(config)# default do-exec show policy-map session brief <string> vrf <string> timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F216D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name；` string ` VRF name。

[条件 C-40770bc8a4c52717](../../evidence/conditions-sets-025.md#c-40770bc8a4c52717) · [参数 P-3dbd6dbc914eb89a](../../evidence/parameters-sets-005.md#p-3dbd6dbc914eb89a) · [状态效果 S-d065152d8ed46233](../../evidence/state_effects-sets-044.md#s-d065152d8ed46233)

### path-059566

```text
(config)# default do-exec show policy-map session brief <string> vrf timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F212F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy-map name。

[条件 C-ab4f5be6333a9aaf](../../evidence/conditions-sets-066.md#c-ab4f5be6333a9aaf) · [参数 P-618e44db93e27b61](../../evidence/parameters-sets-008.md#p-618e44db93e27b61) · [状态效果 S-e6ce0625c7a84e8b](../../evidence/state_effects-sets-049.md#s-e6ce0625c7a84e8b)

### path-056028

```text
(config)# default do-exec show policy-map session brief timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 2 `；EOL ` RVA 0x33F20E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0225f4279e87a276](../../evidence/conditions-sets-001.md#c-0225f4279e87a276) · [状态效果 S-aa8d631f7949f054](../../evidence/state_effects-sets-036.md#s-aa8d631f7949f054)

### path-056046

```text
(config)# default do-exec show policy-map session brief vrfs <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F206C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9989e47c1ebeff96](../../evidence/conditions-sets-059.md#c-9989e47c1ebeff96) · [状态效果 S-aa8d631f7949f054](../../evidence/state_effects-sets-036.md#s-aa8d631f7949f054)

### path-058692

```text
(config)# default do-exec show policy-map session brief vrfs <string> <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F20730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF name。

[条件 C-9989e47c1ebeff96](../../evidence/conditions-sets-059.md#c-9989e47c1ebeff96) · [参数 P-e418100594147980](../../evidence/parameters-sets-017.md#p-e418100594147980) · [状态效果 S-aa8d631f7949f054](../../evidence/state_effects-sets-036.md#s-aa8d631f7949f054)

### path-059564

```text
(config)# default do-exec show policy-map session brief vrfs <string> timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F20770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF name。

[条件 C-9989e47c1ebeff96](../../evidence/conditions-sets-059.md#c-9989e47c1ebeff96) · [参数 P-e418100594147980](../../evidence/parameters-sets-017.md#p-e418100594147980) · [状态效果 S-06b24ded814395e7](../../evidence/state_effects-sets-002.md#s-06b24ded814395e7)

### path-058688

```text
(config)# default do-exec show policy-map session brief vrfs timestamp <cr>
```

Handler ` RVA 0xD889230 `；selector ` 1 `；EOL ` RVA 0x33F203D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0225f4279e87a276](../../evidence/conditions-sets-001.md#c-0225f4279e87a276) · [状态效果 S-729a2461af5aea7c](../../evidence/state_effects-sets-024.md#s-729a2461af5aea7c)

### path-056027

```text
(config)# default do-exec show policy-map session class <string> <cr>
```

Handler ` RVA 0xD88A410 `；selector ` 0 `；EOL ` RVA 0x33F22688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` class-map name。

[条件 C-0225f4279e87a276](../../evidence/conditions-sets-001.md#c-0225f4279e87a276) · [参数 P-a4b7ae5f6035cab1](../../evidence/parameters-sets-013.md#p-a4b7ae5f6035cab1) · [状态效果 S-aa8d631f7949f054](../../evidence/state_effects-sets-036.md#s-aa8d631f7949f054)

### path-041191

```text
(config)# default do-exec show policy-map summary <cr>
```

Handler ` RVA 0xD888ED0 `；selector ` 0 `；EOL ` RVA 0x33F23D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f893f7d9e7163cf](../../evidence/conditions-sets-031.md#c-4f893f7d9e7163cf) · [状态效果 S-b8dc4bf1d290b81f](../../evidence/state_effects-sets-039.md#s-b8dc4bf1d290b81f)

### path-041611

```text
(config)# default do-exec show policy-map target <cr>
```

Handler ` RVA 0xD894B50 `；selector ` 1 `；EOL ` RVA 0x33F27068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [状态效果 S-290359279e849192](../../evidence/state_effects-sets-009.md#s-290359279e849192)

### path-050365

```text
(config)# default do-exec show policy-map target sub-interface <cr>
```

Handler ` RVA 0xD894B50 `；selector ` 0 `；EOL ` RVA 0x33F26BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [状态效果 S-db27b2b237e97c90](../../evidence/state_effects-sets-046.md#s-db27b2b237e97c90)

### path-059563

```text
(config)# default do-exec show policy-map target vrf <string> ipv4 input <cr>
```

Handler ` RVA 0xD8A0B50 `；selector ` 0 `；EOL ` RVA 0x33F28DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF Name.。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [参数 P-977bbc179da5941a](../../evidence/parameters-sets-012.md#p-977bbc179da5941a) · [状态效果 S-1b493e92a38e164a](../../evidence/state_effects-sets-006.md#s-1b493e92a38e164a)

### path-059572

```text
(config)# default do-exec show policy-map target vrf <string> type nwpi <cr>
```

Handler ` RVA 0xD8A1240 `；selector ` 0 `；EOL ` RVA 0x33F292B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF Name.。

[条件 C-b66491d1ee3eb93c](../../evidence/conditions-sets-071.md#c-b66491d1ee3eb93c) · [参数 P-977bbc179da5941a](../../evidence/parameters-sets-012.md#p-977bbc179da5941a) · [状态效果 S-7811f9220f29eb88](../../evidence/state_effects-sets-025.md#s-7811f9220f29eb88)

### path-033859

```text
(config)# default do-exec show port-security <cr>
```

Handler ` RVA 0x15F55EA0 `；selector ` 0 `；EOL ` RVA 0x35E724E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8c64bffcd117770c](../../evidence/state_effects-sets-030.md#s-8c64bffcd117770c)

### path-030664

```text
(config)# default do-exec show power <cr>
```

Handler ` RVA 0x1606BEB0 `；selector ` 0 `；EOL ` RVA 0x35EABE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-114e00f417e641ac](../../evidence/conditions-sets-007.md#c-114e00f417e641ac) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037454

```text
(config)# default do-exec show power detail <cr>
```

Handler ` RVA 0x1606BFA0 `；selector ` 0 `；EOL ` RVA 0x35EABB40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d66e06e55a6f6b34](../../evidence/conditions-sets-083.md#c-d66e06e55a6f6b34) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037535

```text
(config)# default do-exec show power history <cr>
```

Handler ` RVA 0x1606BF00 `；selector ` 0 `；EOL ` RVA 0x35EABE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef51306a05334dd5](../../evidence/conditions-sets-092.md#c-ef51306a05334dd5) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037651

```text
(config)# default do-exec show power inline <cr>
```

Handler ` RVA 0x16028620 `；selector ` 0 `；EOL ` RVA 0x35EA27D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-365e7e9b55f0a771](../../evidence/conditions-sets-021.md#c-365e7e9b55f0a771) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046919

```text
(config)# default do-exec show power inline dynamic-priority <cr>
```

Handler ` RVA 0x16013BA0 `；selector ` 0 `；EOL ` RVA 0x35EA1400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1d558c2c7f55b6a7](../../evidence/conditions-sets-011.md#c-1d558c2c7f55b6a7) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046933

```text
(config)# default do-exec show power inline meter <cr>
```

Handler ` RVA 0x16028620 `；selector ` 18 `；EOL ` RVA 0x35E9F800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec90d2f1179777b1](../../evidence/conditions-sets-091.md#c-ec90d2f1179777b1) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046978

```text
(config)# default do-exec show power inline police <cr>
```

Handler ` RVA 0x16028620 `；selector ` 8 `；EOL ` RVA 0x35EA0D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cec7f9a8277ff60b](../../evidence/conditions-sets-080.md#c-cec7f9a8277ff60b) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047003

```text
(config)# default do-exec show power inline priority <cr>
```

Handler ` RVA 0x16028620 `；selector ` 12 `；EOL ` RVA 0x35EA1AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f59b921c71fcfeb](../../evidence/conditions-sets-037.md#c-5f59b921c71fcfeb) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046957

```text
(config)# default do-exec show power inline upoe-plus <cr>
```

Handler ` RVA 0x16028620 `；selector ` 15 `；EOL ` RVA 0x35EA02A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-041254ca3cd26ab4](../../evidence/conditions-sets-002.md#c-041254ca3cd26ab4) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037395

```text
(config)# default do-exec show power usage <cr>
```

Handler ` RVA 0x1606BF50 `；selector ` 0 `；EOL ` RVA 0x35EAB858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bf58bb22cacad229](../../evidence/conditions-sets-074.md#c-bf58bb22cacad229) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036006

```text
(config)# default do-exec show ppp all <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 1 `；EOL ` RVA 0x3490D890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046412

```text
(config)# default do-exec show ppp bap counters <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 18 `；EOL ` RVA 0x34487EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046571

```text
(config)# default do-exec show ppp bap group <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 16 `；EOL ` RVA 0x34487558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-10a510f4b69a46c3](../../evidence/conditions-sets-007.md#c-10a510f4b69a46c3) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053862

```text
(config)# default do-exec show ppp bap group <string> <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 15 `；EOL ` RVA 0x34487530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Group name。

[条件 C-10a510f4b69a46c3](../../evidence/conditions-sets-007.md#c-10a510f4b69a46c3) · [参数 P-f42785924a741e53](../../evidence/parameters-sets-018.md#p-f42785924a741e53) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046287

```text
(config)# default do-exec show ppp bap queues <cr>
```

Handler ` RVA 0xEF4B400 `；selector ` 17 `；EOL ` RVA 0x34487BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045695

```text
(config)# default do-exec show ppp disconnect history <cr>
```

Handler ` RVA 0xFEDDCC0 `；selector ` 0 `；EOL ` RVA 0x3490DE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045546

```text
(config)# default do-exec show ppp disconnect stats <cr>
```

Handler ` RVA 0xFEDDD20 `；selector ` 0 `；EOL ` RVA 0x3490DBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045660

```text
(config)# default do-exec show ppp id <number:1..4294967295> <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 2 `；EOL ` RVA 0x3490E538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPP Unique ID。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d4e284cec2e04a4a](../../evidence/parameters-sets-016.md#p-d4e284cec2e04a4a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036703

```text
(config)# default do-exec show ppp memory <cr>
```

Handler ` RVA 0xFEC1750 `；selector ` 10 `；EOL ` RVA 0x3490FB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037178

```text
(config)# default do-exec show ppp multilink <cr>
```

Handler ` RVA 0xFF79560 `；selector ` 14 `；EOL ` RVA 0x3493E320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036605

```text
(config)# default do-exec show ppp protocols <cr>
```

Handler ` RVA 0xFEC1700 `；selector ` 7 `；EOL ` RVA 0x3490F868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036488

```text
(config)# default do-exec show ppp queues <cr>
```

Handler ` RVA 0xFEDEC00 `；selector ` 8 `；EOL ` RVA 0x3490F318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036507

```text
(config)# default do-exec show ppp statistics <cr>
```

Handler ` RVA 0xFEDD2E0 `；selector ` 6 `；EOL ` RVA 0x3490ED78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045786

```text
(config)# default do-exec show ppp statistics fsm <cr>
```

Handler ` RVA 0xFEC76B0 `；selector ` 13 `；EOL ` RVA 0x3490EAD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046078

```text
(config)# default do-exec show ppp subscriber statistics <cr>
```

Handler ` RVA 0xFF12CE0 `；selector ` 11 `；EOL ` RVA 0x3490FE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036307

```text
(config)# default do-exec show ppp summary <cr>
```

Handler ` RVA 0xFEDE3A0 `；selector ` 5 `；EOL ` RVA 0x3490E7C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045844

```text
(config)# default do-exec show ppp syslog statistics <cr>
```

Handler ` RVA 0xFEDECC0 `；selector ` 12 `；EOL ` RVA 0x3490F088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036553

```text
(config)# default do-exec show ppp throttled <cr>
```

Handler ` RVA 0xFEDDD70 `；selector ` 4 `；EOL ` RVA 0x3490F5C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041558

```text
(config)# default do-exec show pppatm redundancy <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 3 `；EOL ` RVA 0x35404A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041650

```text
(config)# default do-exec show pppatm session <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 2 `；EOL ` RVA 0x35404FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041592

```text
(config)# default do-exec show pppatm statistics <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 4 `；EOL ` RVA 0x35404CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041514

```text
(config)# default do-exec show pppatm summary <cr>
```

Handler ` RVA 0x1111C970 `；selector ` 1 `；EOL ` RVA 0x35404788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054848

```text
(config)# default do-exec show pppoe derived group <string> <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 7 `；EOL ` RVA 0x356ADAD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the PPPoE group。

[条件 C-8b73de39b2bfa08a](../../evidence/conditions-sets-054.md#c-8b73de39b2bfa08a) · [参数 P-4b93aedf3e835547](../../evidence/parameters-sets-006.md#p-4b93aedf3e835547) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-039473

```text
(config)# default do-exec show pppoe statistics <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 9 `；EOL ` RVA 0x356ADD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b73de39b2bfa08a](../../evidence/conditions-sets-054.md#c-8b73de39b2bfa08a) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-039275

```text
(config)# default do-exec show pppoe summary <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 8 `；EOL ` RVA 0x356ACF98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-a80fad27a9c173e6](../../evidence/state_effects-sets-035.md#s-a80fad27a9c173e6)

### path-048531

```text
(config)# default do-exec show pppoe vrrs summary <cr>
```

Handler ` RVA 0x11C519F0 `；selector ` 10 `；EOL ` RVA 0x356AE0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-035738617d0a2b60](../../evidence/conditions-sets-002.md#c-035738617d0a2b60) · [状态效果 S-bf0d2f2adafc9e72](../../evidence/state_effects-sets-040.md#s-bf0d2f2adafc9e72)

### path-028262

```text
(config)# default do-exec show privilege <cr>
```

Handler ` RVA 0xDF438A0 `；selector ` 0 `；EOL ` RVA 0x34126C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-030395

```text
(config)# default do-exec show processes <cr>
```

Handler ` RVA 0xE083200 `；selector ` 0 `；EOL ` RVA 0x341E2588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036863

```text
(config)# default do-exec show processes <number:1..2147483647> <cr>
```

Handler ` RVA 0xE0475E0 `；selector ` 0 `；EOL ` RVA 0x341E22D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` IOS(d) Process Number。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-56677249233b99d8](../../evidence/parameters-sets-007.md#p-56677249233b99d8) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036541

```text
(config)# default do-exec show processes all-events <cr>
```

Handler ` RVA 0xE0863A0 `；selector ` 0 `；EOL ` RVA 0x341DF120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bd969664c9724878](../../evidence/conditions-sets-073.md#c-bd969664c9724878) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036741

```text
(config)# default do-exec show processes bootup-init <cr>
```

Handler ` RVA 0xE047460 `；selector ` 0 `；EOL ` RVA 0x341E0338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c2248ce3c0bc6834](../../evidence/conditions-sets-075.md#c-c2248ce3c0bc6834) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036690

```text
(config)# default do-exec show processes bootup-time <cr>
```

Handler ` RVA 0xE0472D0 `；selector ` 0 `；EOL ` RVA 0x341E0090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef446159c9cea4be](../../evidence/conditions-sets-092.md#c-ef446159c9cea4be) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036997

```text
(config)# default do-exec show processes cpu <cr>
```

Handler ` RVA 0xE083260 `；selector ` 0 `；EOL ` RVA 0x341E1820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053700

```text
(config)# default do-exec show processes cpu autoprofile hog <cr>
```

Handler ` RVA 0xE087310 `；selector ` 0 `；EOL ` RVA 0x341E12B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053742

```text
(config)# default do-exec show processes cpu autoprofile process <cr>
```

Handler ` RVA 0xE087380 `；selector ` 0 `；EOL ` RVA 0x341E1560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046466

```text
(config)# default do-exec show processes cpu extended <cr>
```

Handler ` RVA 0xE0873F0 `；selector ` 0 `；EOL ` RVA 0x341E1860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053777

```text
(config)# default do-exec show processes cpu extended accounting <cr>
```

Handler ` RVA 0xE088780 `；selector ` 0 `；EOL ` RVA 0x341E1B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a1214c0b787e7dd1](../../evidence/conditions-sets-062.md#c-a1214c0b787e7dd1) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046235

```text
(config)# default do-exec show processes cpu history <cr>
```

Handler ` RVA 0xE048EC0 `；selector ` 0 `；EOL ` RVA 0x341E06D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-053604

```text
(config)# default do-exec show processes cpu history table <cr>
```

Handler ` RVA 0xE0869D0 `；selector ` 0 `；EOL ` RVA 0x341E06B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046264

```text
(config)# default do-exec show processes cpu monitor <cr>
```

Handler ` RVA 0xE083C90 `；selector ` 0 `；EOL ` RVA 0x341E0C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046302

```text
(config)# default do-exec show processes cpu sorted <cr>
```

Handler ` RVA 0xE083640 `；selector ` 0 `；EOL ` RVA 0x341E0F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036653

```text
(config)# default do-exec show processes events <cr>
```

Handler ` RVA 0xE0862A0 `；selector ` 0 `；EOL ` RVA 0x341DF430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a5b0ed31ac872242](../../evidence/conditions-sets-064.md#c-a5b0ed31ac872242) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036417

```text
(config)# default do-exec show processes heapcheck <cr>
```

Handler ` RVA 0xE04C3C0 `；selector ` 0 `；EOL ` RVA 0x341DEBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036827

```text
(config)# default do-exec show processes history <cr>
```

Handler ` RVA 0xE047B20 `；selector ` 0 `；EOL ` RVA 0x341E2030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036844

```text
(config)# default do-exec show processes memory <cr>
```

Handler ` RVA 0xE084D90 `；selector ` 0 `；EOL ` RVA 0x341DF720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046187

```text
(config)# default do-exec show processes memory old-header <cr>
```

Handler ` RVA 0xE084D00 `；selector ` 0 `；EOL ` RVA 0x341DFD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046201

```text
(config)# default do-exec show processes memory sorted <cr>
```

Handler ` RVA 0xE085350 `；selector ` 0 `；EOL ` RVA 0x341DFA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036479

```text
(config)# default do-exec show processes timercheck <cr>
```

Handler ` RVA 0xE0489C0 `；selector ` 0 `；EOL ` RVA 0x341DEE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-033462

```text
(config)# default do-exec show profile <cr>
```

Handler ` RVA 0xD7AEFD0 `；selector ` 0 `；EOL ` RVA 0x34178530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-031993

```text
(config)# default do-exec show protocols <cr>
```

Handler ` RVA 0xDFEAD70 `；selector ` 0 `；EOL ` RVA 0x3423C118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1cd75225e0ca61d](../../evidence/conditions-sets-081.md#c-d1cd75225e0ca61d) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037056

```text
(config)# default do-exec show qbm client <cr>
```

Handler ` RVA 0xFF96040 `；selector ` 0 `；EOL ` RVA 0x34942438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-037163

```text
(config)# default do-exec show qbm pool <cr>
```

Handler ` RVA 0xFF96600 `；selector ` 0 `；EOL ` RVA 0x34942748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046032

```text
(config)# default do-exec show qfp drops thresholds <cr>
```

Handler ` RVA 0x1595C690 `；selector ` 0 `；EOL ` RVA 0x35DC95C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045985

```text
(config)# default do-exec show qfp utilization monitor <cr>
```

Handler ` RVA 0x1595C620 `；selector ` 0 `；EOL ` RVA 0x35DC92F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-033828

```text
(config)# default do-exec show qllc <cr>
```

Handler ` RVA 0x11CBDCB0 `；selector ` 0 `；EOL ` RVA 0x356C1070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64c425b4cea208ea](../../evidence/conditions-sets-039.md#c-64c425b4cea208ea) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047568

```text
(config)# default do-exec show qos adaptive db <cr>
```

Handler ` RVA 0x127CCFD0 `；selector ` 0 `；EOL ` RVA 0x358D01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047615

```text
(config)# default do-exec show qos adaptive multipoint <cr>
```

Handler ` RVA 0x127CCF40 `；selector ` 0 `；EOL ` RVA 0x358CFF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66766805ceb0420c](../../evidence/conditions-sets-040.md#c-66766805ceb0420c) · [状态效果 S-e2b97e0ca6f221cb](../../evidence/state_effects-sets-048.md#s-e2b97e0ca6f221cb)

### path-038460

```text
(config)# default do-exec show qos event <cr>
```

Handler ` RVA 0x13FB7E50 `；selector ` 0 `；EOL ` RVA 0x35CE0FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-038649

```text
(config)# default do-exec show qos trace <cr>
```

Handler ` RVA 0x13FB8240 `；selector ` 0 `；EOL ` RVA 0x35CE1FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047656

```text
(config)# default do-exec show qos trace error <cr>
```

Handler ` RVA 0x13FB81C0 `；selector ` 0 `；EOL ` RVA 0x35CE1D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047589

```text
(config)# default do-exec show qos trace event <cr>
```

Handler ` RVA 0x13FB80D0 `；selector ` 0 `；EOL ` RVA 0x35CE17E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-047628

```text
(config)# default do-exec show qos trace warning <cr>
```

Handler ` RVA 0x13FB8140 `；selector ` 0 `；EOL ` RVA 0x35CE1A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050927

```text
(config)# default do-exec show radius server-group all <cr>
```

Handler ` RVA 0xFFDBDE0 `；selector ` 0 `；EOL ` RVA 0x3494E698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-71da3cddeecaf677](../../evidence/state_effects-sets-024.md#s-71da3cddeecaf677)

### path-042209

```text
(config)# default do-exec show radius statistics <cr>
```

Handler ` RVA 0xFFDA670 `；selector ` 0 `；EOL ` RVA 0x3494E3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-050928

```text
(config)# default do-exec show radius table attributes <cr>
```

Handler ` RVA 0x10038220 `；selector ` 1 `；EOL ` RVA 0x34A263E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-048234

```text
(config)# default do-exec show radius-proxy client <address> <cr>
```

Handler ` RVA 0x11CE8890 `；selector ` 0 `；EOL ` RVA 0x356C6F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of client。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-06758b1faa69743d](../../evidence/parameters-sets-001.md#p-06758b1faa69743d) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-054766

```text
(config)# default do-exec show radius-proxy session id <number:1..4294967295> <cr>
```

Handler ` RVA 0x11CE8EA0 `；selector ` 0 `；EOL ` RVA 0x356C7368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` RP ID of session。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-dabd2c907aaaeecf](../../evidence/parameters-sets-016.md#p-dabd2c907aaaeecf) · [状态效果 S-b3d7bbc853a340e5](../../evidence/state_effects-sets-038.md#s-b3d7bbc853a340e5)

### path-039256

```text
(config)# default do-exec show radius-proxy statistics <cr>
```

Handler ` RVA 0x11CE92C0 `；selector ` 0 `；EOL ` RVA 0x356C7738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-041293

```text
(config)# default do-exec show rbscp state <cr>
```

Handler ` RVA 0xFBC94F0 `；selector ` 0 `；EOL ` RVA 0x34840320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bf98c086abec49cc](../../evidence/conditions-sets-074.md#c-bf98c086abec49cc) · [状态效果 S-4d6eb8fbf4b49c24](../../evidence/state_effects-sets-017.md#s-4d6eb8fbf4b49c24)

### path-039132

```text
(config)# default do-exec show redirect group <cr>
```

Handler ` RVA 0x11AA26F0 `；selector ` 3 `；EOL ` RVA 0x355E14B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-039333

```text
(config)# default do-exec show redirect translations <cr>
```

Handler ` RVA 0x11AA26F0 `；selector ` 7 `；EOL ` RVA 0x355E1868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fa8e750fd86d79ba](../../evidence/conditions-sets-097.md#c-fa8e750fd86d79ba) · [状态效果 S-3bbf0f3181471575](../../evidence/state_effects-sets-013.md#s-3bbf0f3181471575)

### path-030550

```text
(config)# default do-exec show redundancy <cr>
```

Handler ` RVA 0xDB583B0 `；selector ` 0 `；EOL ` RVA 0x33FD6160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-edcfd5914f2fe30b](../../evidence/conditions-sets-092.md#c-edcfd5914f2fe30b) · [状态效果 S-0f3ee076e59e17bd](../../evidence/state_effects-sets-004.md#s-0f3ee076e59e17bd)

### path-046818

```text
(config)# default do-exec show redundancy application group <cr>
```

Handler ` RVA 0xCC193A0 `；selector ` 0 `；EOL ` RVA 0x33C1F348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-25f537ead69fbc33](../../evidence/state_effects-sets-009.md#s-25f537ead69fbc33)

### path-036878

```text
(config)# default do-exec show redundancy clients <cr>
```

Handler ` RVA 0xDB584B0 `；selector ` 0 `；EOL ` RVA 0x33FD6630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-1a708ba862fe9104](../../evidence/state_effects-sets-006.md#s-1a708ba862fe9104)

### path-046788

```text
(config)# default do-exec show redundancy cloud provider <cr>
```

Handler ` RVA 0x1441BDA0 `；selector ` 0 `；EOL ` RVA 0x35D61218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-ce33799eb8281c64](../../evidence/state_effects-sets-044.md#s-ce33799eb8281c64)

### path-046507

```text
(config)# default do-exec show redundancy history monitor <cr>
```

Handler ` RVA 0x127EBDA0 `；selector ` 0 `；EOL ` RVA 0x358D4828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-036942

```text
(config)# default do-exec show redundancy idb-sync-history <cr>
```

Handler ` RVA 0xDB584B0 `；selector ` 0 `；EOL ` RVA 0x33FD9DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-81102599fa2476d0](../../evidence/state_effects-sets-027.md#s-81102599fa2476d0)

### path-037289

```text
(config)# default do-exec show redundancy interchassis <cr>
```

Handler ` RVA 0xC936BE0 `；selector ` 0 `；EOL ` RVA 0x33B309D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-d5e508851b953d7a](../../evidence/state_effects-sets-045.md#s-d5e508851b953d7a)

### path-037210

```text
(config)# default do-exec show redundancy rii <cr>
```

Handler ` RVA 0xCC18EE0 `；selector ` 0 `；EOL ` RVA 0x33C1EB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046586

```text
(config)# default do-exec show redundancy rii <number:1..65535> <cr>
```

Handler ` RVA 0xCC18F30 `；selector ` 0 `；EOL ` RVA 0x33C1EB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` RII id。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [参数 P-2d0fad45d62d9dbd](../../evidence/parameters-sets-004.md#p-2d0fad45d62d9dbd) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-046562

```text
(config)# default do-exec show redundancy switchover history <cr>
```

Handler ` RVA 0xDB3B5C0 `；selector ` 0 `；EOL ` RVA 0x33FCFB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-08fd41bd0aded097](../../evidence/state_effects-sets-002.md#s-08fd41bd0aded097)

### path-046665

```text
(config)# default do-exec show redundancy trace main <cr>
```

Handler ` RVA 0xDB56250 `；selector ` 0 `；EOL ` RVA 0x33FDC188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f989d1289409e0](../../evidence/conditions-sets-032.md#c-52f989d1289409e0) · [状态效果 S-5614d2d40a7ab8f2](../../evidence/state_effects-sets-019.md#s-5614d2d40a7ab8f2)

### path-031991

```text
(config)# default do-exec show refuse-message <cr>
```

Handler ` RVA 0xCE36CF0 `；selector ` 0 `；EOL ` RVA 0x33CF5EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-033431

```text
(config)# default do-exec show region <cr>
```

Handler ` RVA 0xE046370 `；selector ` 0 `；EOL ` RVA 0x34175668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-033530

```text
(config)# default do-exec show registry <cr>
```

Handler ` RVA 0xE053860 `；selector ` 0 `；EOL ` RVA 0x3417BC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4525ec4e185f3f19](../../evidence/conditions-sets-027.md#c-4525ec4e185f3f19) · [状态效果 S-e5a42fa54b156ca2](../../evidence/state_effects-sets-049.md#s-e5a42fa54b156ca2)

### path-043043

```text
(config)# default do-exec show registry calls <cr>
```

Handler ` RVA 0xE053C40 `；selector ` 0 `；EOL ` RVA 0x3417C340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-029124

```text
(config)# default do-exec show reload <cr>
```

Handler ` RVA 0xE003920 `；selector ` 0 `；EOL ` RVA 0x341630A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035147

```text
(config)# default do-exec show reload history <cr>
```

Handler ` RVA 0xE003A10 `；selector ` 0 `；EOL ` RVA 0x34163078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-043769

```text
(config)# default do-exec show remote-management status <cr>
```

Handler ` RVA 0x15696D40 `；selector ` 1 `；EOL ` RVA 0x35D77D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-035549

```text
(config)# default do-exec show resource database <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 2 `；EOL ` RVA 0x33ECAC50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-1967cc1f85524ce6](../../evidence/state_effects-sets-006.md#s-1967cc1f85524ce6)

### path-045317

```text
(config)# default do-exec show resource monitor all <cr>
```

Handler ` RVA 0xD695D90 `；selector ` 6 `；EOL ` RVA 0x33ECAEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-3d7cd2103746f8ef](../../evidence/state_effects-sets-013.md#s-3d7cd2103746f8ef)
