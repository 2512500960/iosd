# router_eigrp_named · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009417

```text
(config-router)# address-family ipv4 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x346BA558 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-52ea070ddc453732](../../evidence/conditions-sets-032.md#c-52ea070ddc453732) · [参数 P-8de07dd7d8f2021f](../../evidence/parameters-sets-011.md#p-8de07dd7d8f2021f) · [状态效果 S-55471b0ae053686a](../../evidence/state_effects-sets-019.md#s-55471b0ae053686a)

### observed_connections-009415

```text
(config-router)# address-family ipv6 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x35458B00 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-bae8a1593efd49bd](../../evidence/conditions-sets-072.md#c-bae8a1593efd49bd) · [参数 P-332b06c2ff9d3d60](../../evidence/parameters-sets-004.md#p-332b06c2ff9d3d60) · [状态效果 S-09c9b37781ce4664](../../evidence/state_effects-sets-002.md#s-09c9b37781ce4664)

### observed_connections-009425

```text
(config-router)# default address-family ipv4 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x346BA558 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-52ea070ddc453732](../../evidence/conditions-sets-032.md#c-52ea070ddc453732) · [参数 P-8de07dd7d8f2021f](../../evidence/parameters-sets-011.md#p-8de07dd7d8f2021f) · [状态效果 S-e4a77a04696b7102](../../evidence/state_effects-sets-048.md#s-e4a77a04696b7102)

### observed_connections-009422

```text
(config-router)# default address-family ipv6 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x35458B00 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-bae8a1593efd49bd](../../evidence/conditions-sets-072.md#c-bae8a1593efd49bd) · [参数 P-332b06c2ff9d3d60](../../evidence/parameters-sets-004.md#p-332b06c2ff9d3d60) · [状态效果 S-ef450dad57335c85](../../evidence/state_effects-sets-051.md#s-ef450dad57335c85)

### observed_connections-009420

```text
(config-router)# default service-family ipv4 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x346F6368 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Autonomous System。

[参数 P-e24ae05c2a6de0e5](../../evidence/parameters-sets-017.md#p-e24ae05c2a6de0e5) · [状态效果 S-e983664961b2e2c4](../../evidence/state_effects-sets-049.md#s-e983664961b2e2c4)

### observed_connections-009423

```text
(config-router)# default service-family ipv6 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x3547CBE8 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-025a4540662a0f9e](../../evidence/conditions-sets-001.md#c-025a4540662a0f9e) · [参数 P-2894af4a08a0dbb5](../../evidence/parameters-sets-003.md#p-2894af4a08a0dbb5) · [状态效果 S-259ce03f35942405](../../evidence/state_effects-sets-008.md#s-259ce03f35942405)

### observed_connections-009424

```text
(config-router)# no address-family ipv4 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x346BA558 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-52ea070ddc453732](../../evidence/conditions-sets-032.md#c-52ea070ddc453732) · [参数 P-8de07dd7d8f2021f](../../evidence/parameters-sets-011.md#p-8de07dd7d8f2021f) · [状态效果 S-db2d5c54eeedc6c8](../../evidence/state_effects-sets-046.md#s-db2d5c54eeedc6c8)

### observed_connections-009419

```text
(config-router)# no address-family ipv6 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x35458B00 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-bae8a1593efd49bd](../../evidence/conditions-sets-072.md#c-bae8a1593efd49bd) · [参数 P-332b06c2ff9d3d60](../../evidence/parameters-sets-004.md#p-332b06c2ff9d3d60) · [状态效果 S-e70d3c0127f49d11](../../evidence/state_effects-sets-049.md#s-e70d3c0127f49d11)

### observed_connections-009418

```text
(config-router)# no service-family ipv4 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x346F6368 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[参数 P-e24ae05c2a6de0e5](../../evidence/parameters-sets-017.md#p-e24ae05c2a6de0e5) · [状态效果 S-8dfc1b882ae685d2](../../evidence/state_effects-sets-030.md#s-8dfc1b882ae685d2)

### observed_connections-009421

```text
(config-router)# no service-family ipv6 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x3547CBE8 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-025a4540662a0f9e](../../evidence/conditions-sets-001.md#c-025a4540662a0f9e) · [参数 P-2894af4a08a0dbb5](../../evidence/parameters-sets-003.md#p-2894af4a08a0dbb5) · [状态效果 S-db2f192266724017](../../evidence/state_effects-sets-046.md#s-db2f192266724017)

### observed_connections-009414

```text
(config-router)# service-family ipv4 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x346F6368 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[参数 P-e24ae05c2a6de0e5](../../evidence/parameters-sets-017.md#p-e24ae05c2a6de0e5) · [状态效果 S-9fd5056b34bf6993](../../evidence/state_effects-sets-034.md#s-9fd5056b34bf6993)

### observed_connections-009416

```text
(config-router)# service-family ipv6 autonomous-system <number:1..65535> <cr>
```

Handler ` RVA 0xF578A40 `；selector ` 3 `；EOL ` RVA 0x3547CBE8 `。

模式根 ` RVA 0x34697F00 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Autonomous System。

[条件 C-025a4540662a0f9e](../../evidence/conditions-sets-001.md#c-025a4540662a0f9e) · [参数 P-2894af4a08a0dbb5](../../evidence/parameters-sets-003.md#p-2894af4a08a0dbb5) · [状态效果 S-99b29e816ae66955](../../evidence/state_effects-sets-033.md#s-99b29e816ae66955)
