# policymap-service-classmap · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008698

```text
(config-service-policymap-class-traffic)# accounting aaa list <string> <cr>
```

Handler ` RVA 0x11563B20 `；selector ` 0 `；EOL ` RVA 0x3551C2E8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AAA method-list name。

[条件 C-11c49b6c0f69b96a](../../evidence/conditions-sets-007.md#c-11c49b6c0f69b96a) · [参数 P-0b3807063198046a](../../evidence/parameters-sets-001.md#p-0b3807063198046a)

### observed_connections-008681

```text
(config-service-policymap-class-traffic)# default accounting <cr>
```

Handler ` RVA 0x11563B20 `；selector ` 0 `；EOL ` RVA 0x3551C2E8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7b2a124649aab9aa](../../evidence/conditions-sets-048.md#c-7b2a124649aab9aa) · [状态效果 S-1d131eae360c8565](../../evidence/state_effects-sets-007.md#s-1d131eae360c8565)

### observed_connections-008690

```text
(config-service-policymap-class-traffic)# default dscp output <cr>
```

Handler ` RVA 0x1159AB30 `；selector ` 0 `；EOL ` RVA 0x3551CA58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b686805accd1d75](../../evidence/conditions-sets-042.md#c-6b686805accd1d75) · [状态效果 S-6b8a2deaa550e2ee](../../evidence/state_effects-sets-023.md#s-6b8a2deaa550e2ee)

### observed_connections-008693

```text
(config-service-policymap-class-traffic)# default gx-monitoring-key <string> <cr>
```

Handler ` RVA 0x1349DFE0 `；selector ` 0 `；EOL ` RVA 0x35A9EC78 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` specify the gx monitoring key。

[参数 P-d41d301d86372f74](../../evidence/parameters-sets-016.md#p-d41d301d86372f74) · [状态效果 S-1d131eae360c8565](../../evidence/state_effects-sets-007.md#s-1d131eae360c8565)

### observed_connections-008695

```text
(config-service-policymap-class-traffic)# default police output <cr>
```

Handler ` RVA 0x10A64C80 `；selector ` 9 `；EOL ` RVA 0x34C27588 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9f1edce53433838](../../evidence/conditions-sets-090.md#c-e9f1edce53433838) · [状态效果 S-ad834ddcaf5cf94b](../../evidence/state_effects-sets-037.md#s-ad834ddcaf5cf94b)

### observed_connections-008699

```text
(config-service-policymap-class-traffic)# default prepaid config default <cr>
```

Handler ` RVA 0x10A8E170 `；selector ` 0 `；EOL ` RVA 0x34C92578 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dbe251f78927d81f](../../evidence/conditions-sets-085.md#c-dbe251f78927d81f) · [状态效果 S-a7b0bc2a195b3751](../../evidence/state_effects-sets-035.md#s-a7b0bc2a195b3751)

### observed_connections-008703

```text
(config-service-policymap-class-traffic)# default redirect to group <string> <cr>
```

Handler ` RVA 0x11AA2550 `；selector ` 1 `；EOL ` RVA 0x355E3C58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Server group name。

[条件 C-bf89491d372261e3](../../evidence/conditions-sets-074.md#c-bf89491d372261e3) · [参数 P-ebd1e13bbfb3dd7e](../../evidence/parameters-sets-018.md#p-ebd1e13bbfb3dd7e) · [状态效果 S-f649b7f707b3a925](../../evidence/state_effects-sets-052.md#s-f649b7f707b3a925)

### observed_connections-008705

```text
(config-service-policymap-class-traffic)# default reroute to next-hop ip <address> <cr>
```

Handler ` RVA 0x1349B560 `；selector ` 0 `；EOL ` RVA 0x35A9DBD8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of the server。

[条件 C-c13d1f21d0346da7](../../evidence/conditions-sets-075.md#c-c13d1f21d0346da7) · [参数 P-2499bb58c13d2cfd](../../evidence/parameters-sets-003.md#p-2499bb58c13d2cfd) · [状态效果 S-1d131eae360c8565](../../evidence/state_effects-sets-007.md#s-1d131eae360c8565)

### observed_connections-008687

```text
(config-service-policymap-class-traffic)# default timeout absolute <cr>
```

Handler ` RVA 0x10912880 `；selector ` 0 `；EOL ` RVA 0x34BDB3B8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-51aa7b60573126f6](../../evidence/conditions-sets-032.md#c-51aa7b60573126f6) · [状态效果 S-1d131eae360c8565](../../evidence/state_effects-sets-007.md#s-1d131eae360c8565)

### observed_connections-008684

```text
(config-service-policymap-class-traffic)# default timeout idle <cr>
```

Handler ` RVA 0x10658E50 `；selector ` 0 `；EOL ` RVA 0x34BDAE98 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a9c98c0aabbdc3c](../../evidence/conditions-sets-010.md#c-1a9c98c0aabbdc3c) · [状态效果 S-1d131eae360c8565](../../evidence/state_effects-sets-007.md#s-1d131eae360c8565)

### observed_connections-008707

```text
(config-service-policymap-class-traffic)# dscp <cr>
```

Handler ` RVA 0x1159AB30 `；selector ` 0 `；EOL ` RVA 0x3551CA58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d5af33e500405307](../../evidence/conditions-sets-082.md#c-d5af33e500405307) · [缺口 G-0d93e01dfef324a2](../../evidence/gaps-sets-001.md#g-0d93e01dfef324a2)

### observed_connections-008692

```text
(config-service-policymap-class-traffic)# dscp output <number:0..63> <cr>
```

Handler ` RVA 0x1159AB30 `；selector ` 0 `；EOL ` RVA 0x3551CA58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` marking value。

[条件 C-d4c40ae96471a971](../../evidence/conditions-sets-082.md#c-d4c40ae96471a971) · [参数 P-93943add3a5f7429](../../evidence/parameters-sets-011.md#p-93943add3a5f7429) · [状态效果 S-6174b529a4c2c99c](../../evidence/state_effects-sets-021.md#s-6174b529a4c2c99c)

### observed_connections-008679

```text
(config-service-policymap-class-traffic)# exit <cr>
```

Handler ` RVA 0x10A64810 `；selector ` 0 `；EOL ` RVA 0x34C83278 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f914b98fd4d72648](../../evidence/conditions-sets-096.md#c-f914b98fd4d72648)

### observed_connections-008682

```text
(config-service-policymap-class-traffic)# gx-monitoring-key <string> <cr>
```

Handler ` RVA 0x1349DFE0 `；selector ` 0 `；EOL ` RVA 0x35A9EC78 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` specify the gx monitoring key。

[参数 P-d41d301d86372f74](../../evidence/parameters-sets-016.md#p-d41d301d86372f74)

### observed_connections-008680

```text
(config-service-policymap-class-traffic)# no accounting <cr>
```

Handler ` RVA 0x11563B20 `；selector ` 0 `；EOL ` RVA 0x3551C2E8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c833302c3590899](../../evidence/conditions-sets-005.md#c-0c833302c3590899) · [状态效果 S-7fee9f251355bde8](../../evidence/state_effects-sets-027.md#s-7fee9f251355bde8)

### observed_connections-008689

```text
(config-service-policymap-class-traffic)# no dscp output <cr>
```

Handler ` RVA 0x1159AB30 `；selector ` 0 `；EOL ` RVA 0x3551CA58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d1db7a3e173f3dd3](../../evidence/conditions-sets-081.md#c-d1db7a3e173f3dd3) · [状态效果 S-ac8fb37df04d6617](../../evidence/state_effects-sets-036.md#s-ac8fb37df04d6617)

### observed_connections-008691

```text
(config-service-policymap-class-traffic)# no gx-monitoring-key <string> <cr>
```

Handler ` RVA 0x1349DFE0 `；selector ` 0 `；EOL ` RVA 0x35A9EC78 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` specify the gx monitoring key。

[参数 P-d41d301d86372f74](../../evidence/parameters-sets-016.md#p-d41d301d86372f74) · [状态效果 S-7fee9f251355bde8](../../evidence/state_effects-sets-027.md#s-7fee9f251355bde8)

### observed_connections-008694

```text
(config-service-policymap-class-traffic)# no police output <cr>
```

Handler ` RVA 0x10A64C80 `；selector ` 9 `；EOL ` RVA 0x34C27588 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d6912e71ce8f7a92](../../evidence/conditions-sets-083.md#c-d6912e71ce8f7a92) · [状态效果 S-67fad17eeb9650b2](../../evidence/state_effects-sets-022.md#s-67fad17eeb9650b2)

### observed_connections-008697

```text
(config-service-policymap-class-traffic)# no prepaid config default <cr>
```

Handler ` RVA 0x10A8E170 `；selector ` 0 `；EOL ` RVA 0x34C92578 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dbe251f78927d81f](../../evidence/conditions-sets-085.md#c-dbe251f78927d81f) · [状态效果 S-7c955466ed4e7852](../../evidence/state_effects-sets-026.md#s-7c955466ed4e7852)

### observed_connections-008702

```text
(config-service-policymap-class-traffic)# no redirect to group <string> <cr>
```

Handler ` RVA 0x11AA2550 `；selector ` 1 `；EOL ` RVA 0x355E3C58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Server group name。

[条件 C-bf89491d372261e3](../../evidence/conditions-sets-074.md#c-bf89491d372261e3) · [参数 P-ebd1e13bbfb3dd7e](../../evidence/parameters-sets-018.md#p-ebd1e13bbfb3dd7e) · [状态效果 S-4c152afabdbf7b66](../../evidence/state_effects-sets-017.md#s-4c152afabdbf7b66)

### observed_connections-008704

```text
(config-service-policymap-class-traffic)# no reroute to next-hop ip <address> <cr>
```

Handler ` RVA 0x1349B560 `；selector ` 0 `；EOL ` RVA 0x35A9DBD8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IP address of the server。

[条件 C-c13d1f21d0346da7](../../evidence/conditions-sets-075.md#c-c13d1f21d0346da7) · [参数 P-2499bb58c13d2cfd](../../evidence/parameters-sets-003.md#p-2499bb58c13d2cfd) · [状态效果 S-7fee9f251355bde8](../../evidence/state_effects-sets-027.md#s-7fee9f251355bde8)

### observed_connections-008685

```text
(config-service-policymap-class-traffic)# no timeout absolute <cr>
```

Handler ` RVA 0x10912880 `；selector ` 0 `；EOL ` RVA 0x34BDB3B8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-55caeda5a95505cd](../../evidence/conditions-sets-034.md#c-55caeda5a95505cd) · [状态效果 S-7fee9f251355bde8](../../evidence/state_effects-sets-027.md#s-7fee9f251355bde8)

### observed_connections-008683

```text
(config-service-policymap-class-traffic)# no timeout idle <cr>
```

Handler ` RVA 0x10658E50 `；selector ` 0 `；EOL ` RVA 0x34BDAE98 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3161f2b2a766882e](../../evidence/conditions-sets-019.md#c-3161f2b2a766882e) · [状态效果 S-7fee9f251355bde8](../../evidence/state_effects-sets-027.md#s-7fee9f251355bde8)

### observed_connections-008708

```text
(config-service-policymap-class-traffic)# police <cr>
```

Handler ` RVA 0x10A64C80 `；selector ` 9 `；EOL ` RVA 0x34C27588 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-adb606ba412e164b](../../evidence/conditions-sets-067.md#c-adb606ba412e164b) · [缺口 G-b6ec94e293fd103e](../../evidence/gaps-sets-006.md#g-b6ec94e293fd103e)

### observed_connections-008696

```text
(config-service-policymap-class-traffic)# police output <number:8000..1000000000> <cr>
```

Handler ` RVA 0x10A64C80 `；selector ` 9 `；EOL ` RVA 0x34C27588 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rate in Bits per second。

[条件 C-100f99e2c9b35ae3](../../evidence/conditions-sets-006.md#c-100f99e2c9b35ae3) · [参数 P-95f7def6ee6c724d](../../evidence/parameters-sets-012.md#p-95f7def6ee6c724d) · [状态效果 S-e672ac3aaef5fcb4](../../evidence/state_effects-sets-049.md#s-e672ac3aaef5fcb4)

### observed_connections-008706

```text
(config-service-policymap-class-traffic)# prepaid <cr>
```

Handler ` RVA 0x10A8ABB0 `；selector ` 0 `；EOL ` RVA 0x34C92918 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ed8a5fce9d8bbb82](../../evidence/conditions-sets-092.md#c-ed8a5fce9d8bbb82) · [缺口 G-884ad300cc28400e](../../evidence/gaps-sets-005.md#g-884ad300cc28400e)

### observed_connections-008688

```text
(config-service-policymap-class-traffic)# prepaid config default <cr>
```

Handler ` RVA 0x10A8E170 `；selector ` 0 `；EOL ` RVA 0x34C92578 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dbe251f78927d81f](../../evidence/conditions-sets-085.md#c-dbe251f78927d81f) · [状态效果 S-f4a58c1c74fd9e4b](../../evidence/state_effects-sets-052.md#s-f4a58c1c74fd9e4b)

### observed_connections-008700

```text
(config-service-policymap-class-traffic)# redirect to group <string> <cr>
```

Handler ` RVA 0x11AA2550 `；selector ` 1 `；EOL ` RVA 0x355E3C58 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Server group name。

[条件 C-bf89491d372261e3](../../evidence/conditions-sets-074.md#c-bf89491d372261e3) · [参数 P-ebd1e13bbfb3dd7e](../../evidence/parameters-sets-018.md#p-ebd1e13bbfb3dd7e) · [状态效果 S-f1ba9ff255abd78f](../../evidence/state_effects-sets-051.md#s-f1ba9ff255abd78f)

### observed_connections-008701

```text
(config-service-policymap-class-traffic)# reroute to next-hop ip <address> <cr>
```

Handler ` RVA 0x1349B560 `；selector ` 0 `；EOL ` RVA 0x35A9DBD8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of the server。

[条件 C-c13d1f21d0346da7](../../evidence/conditions-sets-075.md#c-c13d1f21d0346da7) · [参数 P-2499bb58c13d2cfd](../../evidence/parameters-sets-003.md#p-2499bb58c13d2cfd)

### observed_connections-008686

```text
(config-service-policymap-class-traffic)# timeout absolute <number:0..31104000> <cr>
```

Handler ` RVA 0x10912880 `；selector ` 0 `；EOL ` RVA 0x34BDB3B8 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Absolute timeout value in seconds。

[条件 C-28430c98f9c0431a](../../evidence/conditions-sets-016.md#c-28430c98f9c0431a) · [参数 P-5ba20c96aed9d956](../../evidence/parameters-sets-007.md#p-5ba20c96aed9d956)

### observed_connections-008709

```text
(config-service-policymap-class-traffic)# timeout idle <number:dynamic> <cr>
```

Handler ` RVA 0x10658E50 `；selector ` 0 `；EOL ` RVA 0x34BDAE98 `。

模式根 ` RVA 0x34C82F78 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Idle timeout value in MINUITS。

[条件 C-b50074b257444839](../../evidence/conditions-sets-070.md#c-b50074b257444839) · [缺口 G-001dc494140e4008](../../evidence/gaps-sets-001.md#g-001dc494140e4008) · [参数 P-faf85b9591cf4056](../../evidence/parameters-sets-019.md#p-faf85b9591cf4056)
