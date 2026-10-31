# application-redundancy-group · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009555

```text
(config-red-app)# dampening <number:dynamic> <cr>
```

Handler ` RVA 0xCBD7260 `；selector ` 0 `；EOL ` RVA 0x33C0D550 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` dampening value in miliseconds。

[条件 C-97969c912a0b5e95](../../evidence/conditions-sets-059.md#c-97969c912a0b5e95) · [缺口 G-497c529c5d328d11](../../evidence/gaps-sets-003.md#g-497c529c5d328d11) · [参数 P-c6ab56968bf553de](../../evidence/parameters-sets-015.md#p-c6ab56968bf553de)

### observed_connections-009548

```text
(config-red-app)# default dampening <cr>
```

Handler ` RVA 0xCBD7260 `；selector ` 0 `；EOL ` RVA 0x33C0D550 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-252c064edc20294e](../../evidence/conditions-sets-014.md#c-252c064edc20294e) · [状态效果 S-2bd6480d450783b9](../../evidence/state_effects-sets-010.md#s-2bd6480d450783b9)

### observed_connections-009552

```text
(config-red-app)# default group <number:1..2> <cr>
```

Handler ` RVA 0xCBDFD40 `；selector ` 0 `；EOL ` RVA 0x33C13448 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` RG Group Id。

[条件 C-f002ff50467b7e65](../../evidence/conditions-sets-093.md#c-f002ff50467b7e65) · [参数 P-fe50d191d2f14f50](../../evidence/parameters-sets-019.md#p-fe50d191d2f14f50) · [状态效果 S-2bd6480d450783b9](../../evidence/state_effects-sets-010.md#s-2bd6480d450783b9)

### observed_connections-009554

```text
(config-red-app)# default protocol <number:1..8> <cr>
```

Handler ` RVA 0xCBD6D90 `；selector ` 0 `；EOL ` RVA 0x33C137A8 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` RG Protocol Id。

[条件 C-158fb5f25731f249](../../evidence/conditions-sets-009.md#c-158fb5f25731f249) · [参数 P-05f422a9388f033b](../../evidence/parameters-sets-001.md#p-05f422a9388f033b) · [状态效果 S-2bd6480d450783b9](../../evidence/state_effects-sets-010.md#s-2bd6480d450783b9)

### observed_connections-009549

```text
(config-red-app)# group <number:1..2> <cr>
```

Handler ` RVA 0xCBDFD40 `；selector ` 0 `；EOL ` RVA 0x33C13448 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RG Group Id。

[条件 C-a70a0a7552cd0d93](../../evidence/conditions-sets-064.md#c-a70a0a7552cd0d93) · [参数 P-fe50d191d2f14f50](../../evidence/parameters-sets-019.md#p-fe50d191d2f14f50)

### observed_connections-009547

```text
(config-red-app)# no dampening <cr>
```

Handler ` RVA 0xCBD7260 `；selector ` 0 `；EOL ` RVA 0x33C0D550 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-edbc61dc11fc80eb](../../evidence/conditions-sets-092.md#c-edbc61dc11fc80eb) · [状态效果 S-bd19463a04d50487](../../evidence/state_effects-sets-040.md#s-bd19463a04d50487)

### observed_connections-009551

```text
(config-red-app)# no group <number:1..2> <cr>
```

Handler ` RVA 0xCBDFD40 `；selector ` 0 `；EOL ` RVA 0x33C13448 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` RG Group Id。

[条件 C-e36ff303d6c2bda4](../../evidence/conditions-sets-088.md#c-e36ff303d6c2bda4) · [参数 P-fe50d191d2f14f50](../../evidence/parameters-sets-019.md#p-fe50d191d2f14f50) · [状态效果 S-bd19463a04d50487](../../evidence/state_effects-sets-040.md#s-bd19463a04d50487)

### observed_connections-009553

```text
(config-red-app)# no protocol <number:1..8> <cr>
```

Handler ` RVA 0xCBD6D90 `；selector ` 0 `；EOL ` RVA 0x33C137A8 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` RG Protocol Id。

[条件 C-403acede2618896a](../../evidence/conditions-sets-025.md#c-403acede2618896a) · [参数 P-05f422a9388f033b](../../evidence/parameters-sets-001.md#p-05f422a9388f033b) · [状态效果 S-bd19463a04d50487](../../evidence/state_effects-sets-040.md#s-bd19463a04d50487)

### observed_connections-009550

```text
(config-red-app)# protocol <number:1..8> <cr>
```

Handler ` RVA 0xCBD6D90 `；selector ` 0 `；EOL ` RVA 0x33C137A8 `。

模式根 ` RVA 0x33C0D3F0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RG Protocol Id。

[条件 C-01051b17b3d84b74](../../evidence/conditions-sets-001.md#c-01051b17b3d84b74) · [参数 P-05f422a9388f033b](../../evidence/parameters-sets-001.md#p-05f422a9388f033b)

