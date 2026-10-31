# bba-group · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-006435

```text
(config-bba-group)# ac name <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 3 `；EOL ` RVA 0x35438FB8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AC Name。

[条件 C-d1f283e3c305dc46](../../evidence/conditions-sets-081.md#c-d1f283e3c305dc46) · [参数 P-720bdeaa68b9d3e4](../../evidence/parameters-sets-009.md#p-720bdeaa68b9d3e4)

### observed_connections-006458

```text
(config-bba-group)# control-packets vlan cos <number:0..7> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 23 `；EOL ` RVA 0x354378A0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pirority value for PPP/PPPoE control packets in VLAN header。

[条件 C-f466682478699410](../../evidence/conditions-sets-094.md#c-f466682478699410) · [参数 P-660f2c8b2cc44283](../../evidence/parameters-sets-008.md#p-660f2c8b2cc44283)

### observed_connections-006436

```text
(config-bba-group)# default ac name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 3 `；EOL ` RVA 0x35438FB8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c7082f80ecfbd00b](../../evidence/conditions-sets-077.md#c-c7082f80ecfbd00b) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006459

```text
(config-bba-group)# default control-packets vlan cos <cr>
```

Handler ` RVA 0x11255790 `；selector ` 23 `；EOL ` RVA 0x354378A0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6906df683401c15b](../../evidence/conditions-sets-041.md#c-6906df683401c15b) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006444

```text
(config-bba-group)# default limit pado service-name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 37 `；EOL ` RVA 0x35435098 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006417

```text
(config-bba-group)# default mac-address <cr>
```

Handler ` RVA 0x11255790 `；selector ` 4 `；EOL ` RVA 0x354392F0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-531b38a69c13a903](../../evidence/conditions-sets-032.md#c-531b38a69c13a903) · [状态效果 S-270fbc688cde999d](../../evidence/state_effects-sets-009.md#s-270fbc688cde999d)

### observed_connections-006461

```text
(config-bba-group)# default nas-port-id format c <cr>
```

Handler ` RVA 0x11255790 `；selector ` 21 `；EOL ` RVA 0x35438120 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5582e634c4f0dba0](../../evidence/conditions-sets-034.md#c-5582e634c4f0dba0) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006464

```text
(config-bba-group)# default pado delay <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 28 `；EOL ` RVA 0x3543C2B0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-2e90ee863e7fc085](../../evidence/parameters-sets-004.md#p-2e90ee863e7fc085) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006499

```text
(config-bba-group)# default pado delay circuit-id <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 29 `；EOL ` RVA 0x3543C5C8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-ad770cfcf6e7fd15](../../evidence/parameters-sets-013.md#p-ad770cfcf6e7fd15) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006501

```text
(config-bba-group)# default pado delay remote-id <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 30 `；EOL ` RVA 0x3543C890 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-6387bcdc8298aa36](../../evidence/parameters-sets-008.md#p-6387bcdc8298aa36) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006441

```text
(config-bba-group)# default pppoe disable-credit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 39 `；EOL ` RVA 0x3543D4F8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-36864fa8f91bb994](../../evidence/conditions-sets-021.md#c-36864fa8f91bb994) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006510

```text
(config-bba-group)# default pppoe server circuit-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 31 `；EOL ` RVA 0x3543CDA0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Circuit-Id String。

[条件 C-917e4426ba8425c2](../../evidence/conditions-sets-056.md#c-917e4426ba8425c2) · [参数 P-a4cf5efa51a83e38](../../evidence/parameters-sets-013.md#p-a4cf5efa51a83e38) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006512

```text
(config-bba-group)# default pppoe server remote-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 32 `；EOL ` RVA 0x3543D208 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Remote-Id String。

[条件 C-8ad60ed169313a17](../../evidence/conditions-sets-054.md#c-8ad60ed169313a17) · [参数 P-8d3127976585171b](../../evidence/parameters-sets-011.md#p-8d3127976585171b) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006433

```text
(config-bba-group)# default service name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 36 `；EOL ` RVA 0x35438850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bf6b3315a787579](../../evidence/conditions-sets-054.md#c-8bf6b3315a787579) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006434

```text
(config-bba-group)# default service profile <cr>
```

Handler ` RVA 0x11255790 `；selector ` 11 `；EOL ` RVA 0x354384D0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-46a9c3b2a231716e](../../evidence/conditions-sets-028.md#c-46a9c3b2a231716e) · [状态效果 S-29b6acc3c54901ee](../../evidence/state_effects-sets-009.md#s-29b6acc3c54901ee)

### observed_connections-006483

```text
(config-bba-group)# default sessions auto cleanup <cr>
```

Handler ` RVA 0x11255790 `；selector ` 24 `；EOL ` RVA 0x3543BC20 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006484

```text
(config-bba-group)# default sessions max limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 0 `；EOL ` RVA 0x3543B148 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-38ad72db9a8b08f5](../../evidence/conditions-sets-022.md#c-38ad72db9a8b08f5) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006470

```text
(config-bba-group)# default sessions per-mac iwf <cr>
```

Handler ` RVA 0x11255790 `；selector ` 6 `；EOL ` RVA 0x35439EF0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef8b4121caab3869](../../evidence/conditions-sets-093.md#c-ef8b4121caab3869) · [状态效果 S-2f35811b7589c767](../../evidence/state_effects-sets-010.md#s-2f35811b7589c767)

### observed_connections-006476

```text
(config-bba-group)# default sessions per-mac limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 6 `；EOL ` RVA 0x3543A258 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4799a16bae0a81bc](../../evidence/conditions-sets-028.md#c-4799a16bae0a81bc) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006482

```text
(config-bba-group)# default sessions per-mac throttle <cr>
```

Handler ` RVA 0x11255790 `；selector ` 9 `；EOL ` RVA 0x3543A548 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e273ee4e569c18dc](../../evidence/conditions-sets-087.md#c-e273ee4e569c18dc) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006465

```text
(config-bba-group)# default sessions per-vc limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 7 `；EOL ` RVA 0x35439730 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3715cb6d9f9d93d1](../../evidence/conditions-sets-021.md#c-3715cb6d9f9d93d1) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006472

```text
(config-bba-group)# default sessions per-vc throttle <cr>
```

Handler ` RVA 0x11255790 `；selector ` 10 `；EOL ` RVA 0x35439AB8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0647d21cfe7df0e5](../../evidence/conditions-sets-003.md#c-0647d21cfe7df0e5) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006475

```text
(config-bba-group)# default sessions per-vlan limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 5 `；EOL ` RVA 0x3543A980 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f1c9ec434a0dea71](../../evidence/conditions-sets-093.md#c-f1c9ec434a0dea71) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006481

```text
(config-bba-group)# default sessions per-vlan throttle <cr>
```

Handler ` RVA 0x11255790 `；selector ` 38 `；EOL ` RVA 0x3543AD08 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-185546ed935f121b](../../evidence/conditions-sets-009.md#c-185546ed935f121b) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006504

```text
(config-bba-group)# default sessions pre-auth limit ignore <cr>
```

Handler ` RVA 0x11255790 `；selector ` 33 `；EOL ` RVA 0x3543BF30 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006487

```text
(config-bba-group)# default sessions threshold percent <cr>
```

Handler ` RVA 0x11255790 `；selector ` 2 `；EOL ` RVA 0x3543B880 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4968bf42398936f5](../../evidence/conditions-sets-029.md#c-4968bf42398936f5) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006446

```text
(config-bba-group)# default tag ppp-max-payload deny <cr>
```

Handler ` RVA 0x11255790 `；selector ` 26 `；EOL ` RVA 0x354353D8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006452

```text
(config-bba-group)# default tag ppp-max-payload minimum <cr>
```

Handler ` RVA 0x11255790 `；selector ` 27 `；EOL ` RVA 0x354356E8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a6f6fd5f5c8a391](../../evidence/conditions-sets-035.md#c-5a6f6fd5f5c8a391) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006454

```text
(config-bba-group)# default test tag <number:0..65535> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 25 `；EOL ` RVA 0x35436850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tag type in hex or decimal。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [参数 P-a122e17606fa85d1](../../evidence/parameters-sets-012.md#p-a122e17606fa85d1) · [状态效果 S-71e565765fd9d098](../../evidence/state_effects-sets-024.md#s-71e565765fd9d098)

### observed_connections-006489

```text
(config-bba-group)# default test vendor-tag circuit-id client <cr>
```

Handler ` RVA 0x11255790 `；selector ` 13 `；EOL ` RVA 0x35436B88 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [状态效果 S-5e1c0961c7372b51](../../evidence/state_effects-sets-020.md#s-5e1c0961c7372b51)

### observed_connections-006494

```text
(config-bba-group)# default test vendor-tag circuit-id string <cr>
```

Handler ` RVA 0x11255790 `；selector ` 15 `；EOL ` RVA 0x35436E98 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c36747ede4637ff2](../../evidence/conditions-sets-075.md#c-c36747ede4637ff2) · [状态效果 S-5e1c0961c7372b51](../../evidence/state_effects-sets-020.md#s-5e1c0961c7372b51)

### observed_connections-006491

```text
(config-bba-group)# default test vendor-tag remote-id client <cr>
```

Handler ` RVA 0x11255790 `；selector ` 17 `；EOL ` RVA 0x35437198 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [状态效果 S-5e1c0961c7372b51](../../evidence/state_effects-sets-020.md#s-5e1c0961c7372b51)

### observed_connections-006497

```text
(config-bba-group)# default test vendor-tag remote-id string <cr>
```

Handler ` RVA 0x11255790 `；selector ` 18 `；EOL ` RVA 0x354374A8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a664525bb907e4d0](../../evidence/conditions-sets-064.md#c-a664525bb907e4d0) · [状态效果 S-5e1c0961c7372b51](../../evidence/state_effects-sets-020.md#s-5e1c0961c7372b51)

### observed_connections-006449

```text
(config-bba-group)# default vendor-tag circuit-id service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 12 `；EOL ` RVA 0x35435B40 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b958c086e913337](../../evidence/conditions-sets-042.md#c-6b958c086e913337) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006425

```text
(config-bba-group)# default vendor-tag dsl-sync-rate <cr>
```

Handler ` RVA 0x11255790 `；selector ` 19 `；EOL ` RVA 0x35436168 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4f3adb979dd5747f](../../evidence/conditions-sets-031.md#c-4f3adb979dd5747f) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006456

```text
(config-bba-group)# default vendor-tag remote-id service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 16 `；EOL ` RVA 0x35435E60 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-da72426a6de1c3e4](../../evidence/conditions-sets-084.md#c-da72426a6de1c3e4) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006428

```text
(config-bba-group)# default vendor-tag strip <cr>
```

Handler ` RVA 0x11255790 `；selector ` 14 `；EOL ` RVA 0x35436490 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2eaa80288031f49e](../../evidence/conditions-sets-018.md#c-2eaa80288031f49e) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006413

```text
(config-bba-group)# default virtual-template <cr>
```

Handler ` RVA 0x11255790 `；selector ` 8 `；EOL ` RVA 0x35434D68 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-52f828a313e691e2](../../evidence/conditions-sets-032.md#c-52f828a313e691e2) · [状态效果 S-3ec50ad81b9f5a04](../../evidence/state_effects-sets-014.md#s-3ec50ad81b9f5a04)

### observed_connections-006411

```text
(config-bba-group)# exit <cr>
```

Handler ` RVA 0x112556F0 `；selector ` 0 `；EOL ` RVA 0x3543D9F0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0502b6876be7d81d](../../evidence/conditions-sets-002.md#c-0502b6876be7d81d)

### observed_connections-006419

```text
(config-bba-group)# limit pado service-name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 37 `；EOL ` RVA 0x35435098 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-006416

```text
(config-bba-group)# mac-address autoselect <cr>
```

Handler ` RVA 0x11255790 `；selector ` 4 `；EOL ` RVA 0x354392F0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-65fee91de3f54025](../../evidence/conditions-sets-039.md#c-65fee91de3f54025) · [状态效果 S-abb2eec067c76d45](../../evidence/state_effects-sets-036.md#s-abb2eec067c76d45)

### observed_connections-006523

```text
(config-bba-group)# nas-port format d <number:0..8> / <?number_func_nows_action@55558a98bc70> / <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 22 `；EOL ` RVA 0x35437D78 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of bits to store slot number；` unsigned_number_dynamic ` Number of bits to store port number。

[条件 C-e1f3f540ada0a361](../../evidence/conditions-sets-087.md#c-e1f3f540ada0a361) · [缺口 G-0a86a8633589d70c](../../evidence/gaps-sets-001.md#g-0a86a8633589d70c) · [参数 P-033f907c0de15125](../../evidence/parameters-sets-001.md#p-033f907c0de15125)

### observed_connections-006429

```text
(config-bba-group)# nas-port-id format c <cr>
```

Handler ` RVA 0x11255790 `；selector ` 21 `；EOL ` RVA 0x35438120 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ad640bde0c4124f](../../evidence/conditions-sets-054.md#c-8ad640bde0c4124f)

### observed_connections-006432

```text
(config-bba-group)# no ac name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 3 `；EOL ` RVA 0x35438FB8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-16d548a9e29583c3](../../evidence/conditions-sets-009.md#c-16d548a9e29583c3) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006455

```text
(config-bba-group)# no control-packets vlan cos <cr>
```

Handler ` RVA 0x11255790 `；selector ` 23 `；EOL ` RVA 0x354378A0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-206d1efe63f679a7](../../evidence/conditions-sets-013.md#c-206d1efe63f679a7) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006443

```text
(config-bba-group)# no limit pado service-name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 37 `；EOL ` RVA 0x35435098 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006415

```text
(config-bba-group)# no mac-address <cr>
```

Handler ` RVA 0x11255790 `；selector ` 4 `；EOL ` RVA 0x354392F0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-581239e7547666e2](../../evidence/conditions-sets-035.md#c-581239e7547666e2) · [状态效果 S-e97cad3f6a14e05d](../../evidence/state_effects-sets-049.md#s-e97cad3f6a14e05d)

### observed_connections-006460

```text
(config-bba-group)# no nas-port-id format c <cr>
```

Handler ` RVA 0x11255790 `；selector ` 21 `；EOL ` RVA 0x35438120 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-32a064f39043cb5b](../../evidence/conditions-sets-020.md#c-32a064f39043cb5b) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006462

```text
(config-bba-group)# no pado delay <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 28 `；EOL ` RVA 0x3543C2B0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-2e90ee863e7fc085](../../evidence/parameters-sets-004.md#p-2e90ee863e7fc085) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006498

```text
(config-bba-group)# no pado delay circuit-id <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 29 `；EOL ` RVA 0x3543C5C8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-ad770cfcf6e7fd15](../../evidence/parameters-sets-013.md#p-ad770cfcf6e7fd15) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006500

```text
(config-bba-group)# no pado delay remote-id <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 30 `；EOL ` RVA 0x3543C890 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-6387bcdc8298aa36](../../evidence/parameters-sets-008.md#p-6387bcdc8298aa36) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006440

```text
(config-bba-group)# no pppoe disable-credit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 39 `；EOL ` RVA 0x3543D4F8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-36864fa8f91bb994](../../evidence/conditions-sets-021.md#c-36864fa8f91bb994) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006509

```text
(config-bba-group)# no pppoe server circuit-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 31 `；EOL ` RVA 0x3543CDA0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Circuit-Id String。

[条件 C-917e4426ba8425c2](../../evidence/conditions-sets-056.md#c-917e4426ba8425c2) · [参数 P-a4cf5efa51a83e38](../../evidence/parameters-sets-013.md#p-a4cf5efa51a83e38) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006511

```text
(config-bba-group)# no pppoe server remote-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 32 `；EOL ` RVA 0x3543D208 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Remote-Id String。

[条件 C-8ad60ed169313a17](../../evidence/conditions-sets-054.md#c-8ad60ed169313a17) · [参数 P-8d3127976585171b](../../evidence/parameters-sets-011.md#p-8d3127976585171b) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006430

```text
(config-bba-group)# no service name <cr>
```

Handler ` RVA 0x11255790 `；selector ` 36 `；EOL ` RVA 0x35438850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bf9c831474f08adf](../../evidence/conditions-sets-074.md#c-bf9c831474f08adf) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006431

```text
(config-bba-group)# no service profile <cr>
```

Handler ` RVA 0x11255790 `；selector ` 11 `；EOL ` RVA 0x354384D0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-21f5f117587e0d47](../../evidence/conditions-sets-013.md#c-21f5f117587e0d47) · [状态效果 S-45b4c07d1f9ef17b](../../evidence/state_effects-sets-015.md#s-45b4c07d1f9ef17b)

### observed_connections-006479

```text
(config-bba-group)# no sessions auto cleanup <cr>
```

Handler ` RVA 0x11255790 `；selector ` 24 `；EOL ` RVA 0x3543BC20 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006480

```text
(config-bba-group)# no sessions max limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 0 `；EOL ` RVA 0x3543B148 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8414b8fc3190b8ca](../../evidence/conditions-sets-051.md#c-8414b8fc3190b8ca) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006466

```text
(config-bba-group)# no sessions per-mac iwf <cr>
```

Handler ` RVA 0x11255790 `；selector ` 6 `；EOL ` RVA 0x35439EF0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dcf9a2dd15219a49](../../evidence/conditions-sets-085.md#c-dcf9a2dd15219a49) · [状态效果 S-c204bee6382c97ca](../../evidence/state_effects-sets-041.md#s-c204bee6382c97ca)

### observed_connections-006473

```text
(config-bba-group)# no sessions per-mac limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 6 `；EOL ` RVA 0x3543A258 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-aaca771b4cefa6f6](../../evidence/conditions-sets-066.md#c-aaca771b4cefa6f6) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006478

```text
(config-bba-group)# no sessions per-mac throttle <cr>
```

Handler ` RVA 0x11255790 `；selector ` 9 `；EOL ` RVA 0x3543A548 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b6ac9a59c5286da6](../../evidence/conditions-sets-071.md#c-b6ac9a59c5286da6) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006463

```text
(config-bba-group)# no sessions per-vc limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 7 `；EOL ` RVA 0x35439730 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-35e71474a69c4f8b](../../evidence/conditions-sets-021.md#c-35e71474a69c4f8b) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006468

```text
(config-bba-group)# no sessions per-vc throttle <cr>
```

Handler ` RVA 0x11255790 `；selector ` 10 `；EOL ` RVA 0x35439AB8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-76cbf7d67c44e6d2](../../evidence/conditions-sets-046.md#c-76cbf7d67c44e6d2) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006471

```text
(config-bba-group)# no sessions per-vlan limit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 5 `；EOL ` RVA 0x3543A980 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e220d770aab5b6fd](../../evidence/conditions-sets-087.md#c-e220d770aab5b6fd) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006477

```text
(config-bba-group)# no sessions per-vlan throttle <cr>
```

Handler ` RVA 0x11255790 `；selector ` 38 `；EOL ` RVA 0x3543AD08 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-17057579d4e79213](../../evidence/conditions-sets-009.md#c-17057579d4e79213) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006502

```text
(config-bba-group)# no sessions pre-auth limit ignore <cr>
```

Handler ` RVA 0x11255790 `；selector ` 33 `；EOL ` RVA 0x3543BF30 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006486

```text
(config-bba-group)# no sessions threshold percent <cr>
```

Handler ` RVA 0x11255790 `；selector ` 2 `；EOL ` RVA 0x3543B880 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0920cee76fca2a58](../../evidence/conditions-sets-004.md#c-0920cee76fca2a58) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006445

```text
(config-bba-group)# no tag ppp-max-payload deny <cr>
```

Handler ` RVA 0x11255790 `；selector ` 26 `；EOL ` RVA 0x354353D8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006448

```text
(config-bba-group)# no tag ppp-max-payload minimum <cr>
```

Handler ` RVA 0x11255790 `；selector ` 27 `；EOL ` RVA 0x354356E8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2bfd4440375c897d](../../evidence/conditions-sets-017.md#c-2bfd4440375c897d) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006450

```text
(config-bba-group)# no test tag <number:0..65535> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 25 `；EOL ` RVA 0x35436850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Tag type in hex or decimal。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [参数 P-a122e17606fa85d1](../../evidence/parameters-sets-012.md#p-a122e17606fa85d1) · [状态效果 S-b4fa97e2ef708620](../../evidence/state_effects-sets-038.md#s-b4fa97e2ef708620)

### observed_connections-006488

```text
(config-bba-group)# no test vendor-tag circuit-id client <cr>
```

Handler ` RVA 0x11255790 `；selector ` 13 `；EOL ` RVA 0x35436B88 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [状态效果 S-92d2bed352ec25b4](../../evidence/state_effects-sets-031.md#s-92d2bed352ec25b4)

### observed_connections-006492

```text
(config-bba-group)# no test vendor-tag circuit-id string <cr>
```

Handler ` RVA 0x11255790 `；selector ` 15 `；EOL ` RVA 0x35436E98 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-59c5fb4abd4634bb](../../evidence/conditions-sets-035.md#c-59c5fb4abd4634bb) · [状态效果 S-92d2bed352ec25b4](../../evidence/state_effects-sets-031.md#s-92d2bed352ec25b4)

### observed_connections-006490

```text
(config-bba-group)# no test vendor-tag remote-id client <cr>
```

Handler ` RVA 0x11255790 `；selector ` 17 `；EOL ` RVA 0x35437198 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [状态效果 S-92d2bed352ec25b4](../../evidence/state_effects-sets-031.md#s-92d2bed352ec25b4)

### observed_connections-006495

```text
(config-bba-group)# no test vendor-tag remote-id string <cr>
```

Handler ` RVA 0x11255790 `；selector ` 18 `；EOL ` RVA 0x354374A8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fcaad8a4903acb96](../../evidence/conditions-sets-097.md#c-fcaad8a4903acb96) · [状态效果 S-92d2bed352ec25b4](../../evidence/state_effects-sets-031.md#s-92d2bed352ec25b4)

### observed_connections-006447

```text
(config-bba-group)# no vendor-tag circuit-id service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 12 `；EOL ` RVA 0x35435B40 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-950f9a00dcf84593](../../evidence/conditions-sets-058.md#c-950f9a00dcf84593) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006424

```text
(config-bba-group)# no vendor-tag dsl-sync-rate <cr>
```

Handler ` RVA 0x11255790 `；selector ` 19 `；EOL ` RVA 0x35436168 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-472538be0912d3b9](../../evidence/conditions-sets-028.md#c-472538be0912d3b9) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006451

```text
(config-bba-group)# no vendor-tag remote-id service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 16 `；EOL ` RVA 0x35435E60 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c3d1d4a70315a510](../../evidence/conditions-sets-076.md#c-c3d1d4a70315a510) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006426

```text
(config-bba-group)# no vendor-tag strip <cr>
```

Handler ` RVA 0x11255790 `；selector ` 14 `；EOL ` RVA 0x35436490 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-850c858d7ba2519e](../../evidence/conditions-sets-051.md#c-850c858d7ba2519e) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006412

```text
(config-bba-group)# no virtual-template <cr>
```

Handler ` RVA 0x11255790 `；selector ` 8 `；EOL ` RVA 0x35434D68 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c7ce8a8dfc6c5e06](../../evidence/conditions-sets-077.md#c-c7ce8a8dfc6c5e06) · [状态效果 S-32b2fbe57a37c1c2](../../evidence/state_effects-sets-011.md#s-32b2fbe57a37c1c2)

### observed_connections-006439

```text
(config-bba-group)# pado delay <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 28 `；EOL ` RVA 0x3543C2B0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-2e90ee863e7fc085](../../evidence/parameters-sets-004.md#p-2e90ee863e7fc085)

### observed_connections-006469

```text
(config-bba-group)# pado delay circuit-id <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 29 `；EOL ` RVA 0x3543C5C8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-ad770cfcf6e7fd15](../../evidence/parameters-sets-013.md#p-ad770cfcf6e7fd15)

### observed_connections-006474

```text
(config-bba-group)# pado delay remote-id <number:0..9999> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 30 `；EOL ` RVA 0x3543C890 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time in milliseconds for PADO delay。

[参数 P-6387bcdc8298aa36](../../evidence/parameters-sets-008.md#p-6387bcdc8298aa36)

### observed_connections-006418

```text
(config-bba-group)# pppoe disable-credit <cr>
```

Handler ` RVA 0x11255790 `；selector ` 39 `；EOL ` RVA 0x3543D4F8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-36864fa8f91bb994](../../evidence/conditions-sets-021.md#c-36864fa8f91bb994)

### observed_connections-006503

```text
(config-bba-group)# pppoe server circuit-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 31 `；EOL ` RVA 0x3543CDA0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Circuit-Id String。

[条件 C-917e4426ba8425c2](../../evidence/conditions-sets-056.md#c-917e4426ba8425c2) · [参数 P-a4cf5efa51a83e38](../../evidence/parameters-sets-013.md#p-a4cf5efa51a83e38)

### observed_connections-006505

```text
(config-bba-group)# pppoe server remote-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 32 `；EOL ` RVA 0x3543D208 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Remote-Id String。

[条件 C-8ad60ed169313a17](../../evidence/conditions-sets-054.md#c-8ad60ed169313a17) · [参数 P-8d3127976585171b](../../evidence/parameters-sets-011.md#p-8d3127976585171b)

### observed_connections-006467

```text
(config-bba-group)# service name contains <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 36 `；EOL ` RVA 0x35438850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Partial service name to be matched。

[条件 C-b1c1ddfac78aecc4](../../evidence/conditions-sets-069.md#c-b1c1ddfac78aecc4) · [参数 P-8fe9e54765e849ee](../../evidence/parameters-sets-011.md#p-8fe9e54765e849ee)

### observed_connections-006437

```text
(config-bba-group)# service name match <cr>
```

Handler ` RVA 0x11255790 `；selector ` 34 `；EOL ` RVA 0x354388E0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1c1ddfac78aecc4](../../evidence/conditions-sets-069.md#c-b1c1ddfac78aecc4)

### observed_connections-006438

```text
(config-bba-group)# service profile <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 11 `；EOL ` RVA 0x354384D0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of service policy-map。

[条件 C-16c825c4547b9d58](../../evidence/conditions-sets-009.md#c-16c825c4547b9d58) · [参数 P-91d3482d326e078f](../../evidence/parameters-sets-011.md#p-91d3482d326e078f) · [状态效果 S-f227675998a3c5af](../../evidence/state_effects-sets-051.md#s-f227675998a3c5af)

### observed_connections-006442

```text
(config-bba-group)# sessions auto cleanup <cr>
```

Handler ` RVA 0x11255790 `；selector ` 24 `；EOL ` RVA 0x3543BC20 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-006520

```text
(config-bba-group)# sessions max limit <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 0 `；EOL ` RVA 0x3543B148 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Global pppoe session limit。

[条件 C-9d3cf564ae7b18ed](../../evidence/conditions-sets-061.md#c-9d3cf564ae7b18ed) · [缺口 G-59cfa2ffa6c2ec32](../../evidence/gaps-sets-004.md#g-59cfa2ffa6c2ec32) · [参数 P-c0df5e19f49feddf](../../evidence/parameters-sets-015.md#p-c0df5e19f49feddf)

### observed_connections-006521

```text
(config-bba-group)# sessions per-mac iwf limit <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 6 `；EOL ` RVA 0x35439EF0 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Per-MAC session limit to be applied for IWF sessions。

[条件 C-19352bf8a6a20d14](../../evidence/conditions-sets-010.md#c-19352bf8a6a20d14) · [缺口 G-e87dee41d3b89925](../../evidence/gaps-sets-008.md#g-e87dee41d3b89925) · [参数 P-76f47449d688dc7e](../../evidence/parameters-sets-009.md#p-76f47449d688dc7e) · [状态效果 S-2937ab7ee7febbbb](../../evidence/state_effects-sets-009.md#s-2937ab7ee7febbbb)

### observed_connections-006518

```text
(config-bba-group)# sessions per-mac limit <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 6 `；EOL ` RVA 0x3543A258 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Per-MAC session limit。

[条件 C-43d03bbd679969f6](../../evidence/conditions-sets-027.md#c-43d03bbd679969f6) · [缺口 G-37e15a20c5ab3ecc](../../evidence/gaps-sets-002.md#g-37e15a20c5ab3ecc) · [参数 P-4cf4884ea5b65ff6](../../evidence/parameters-sets-006.md#p-4cf4884ea5b65ff6)

### observed_connections-006508

```text
(config-bba-group)# sessions per-mac throttle <number:1..100000> <number:1..3600> <number:0..3600> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 9 `；EOL ` RVA 0x3543A548 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of calls allowed per MAC per specific time duration；` unsigned_number ` Time in seconds for allowing N calls per MAC；` unsigned_number ` Time in seconds for blocking calls per MAC。

[条件 C-2ceb047a592b1ab0](../../evidence/conditions-sets-018.md#c-2ceb047a592b1ab0) · [参数 P-aa12a91a9fa7a5fc](../../evidence/parameters-sets-013.md#p-aa12a91a9fa7a5fc)

### observed_connections-006517

```text
(config-bba-group)# sessions per-vc limit <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 7 `；EOL ` RVA 0x35439730 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Per-VC session limit。

[条件 C-28c8917b43c5fa9d](../../evidence/conditions-sets-016.md#c-28c8917b43c5fa9d) · [缺口 G-8bf3ca0d2c94d59b](../../evidence/gaps-sets-005.md#g-8bf3ca0d2c94d59b) · [参数 P-da3227d4c2554c3d](../../evidence/parameters-sets-016.md#p-da3227d4c2554c3d)

### observed_connections-006506

```text
(config-bba-group)# sessions per-vc throttle <number:1..100000> <number:1..3600> <number:0..3600> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 10 `；EOL ` RVA 0x35439AB8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of calls N allowed per VC per specific time duration；` unsigned_number ` Time in seconds for allowing N calls per VC；` unsigned_number ` Time in seconds for blocking calls per VC。

[条件 C-ea51f64eb6bf815b](../../evidence/conditions-sets-090.md#c-ea51f64eb6bf815b) · [参数 P-1636a2f11fa3afa6](../../evidence/parameters-sets-002.md#p-1636a2f11fa3afa6)

### observed_connections-006519

```text
(config-bba-group)# sessions per-vlan limit <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 5 `；EOL ` RVA 0x3543A980 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Per-VLAN session limit。

[条件 C-f1aa2893f42abdcd](../../evidence/conditions-sets-093.md#c-f1aa2893f42abdcd) · [缺口 G-d5d9fca1a7c72739](../../evidence/gaps-sets-007.md#g-d5d9fca1a7c72739) · [参数 P-50fab3f32cd28b92](../../evidence/parameters-sets-007.md#p-50fab3f32cd28b92)

### observed_connections-006507

```text
(config-bba-group)# sessions per-vlan throttle <number:1..100000> <number:1..3600> <number:0..3600> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 38 `；EOL ` RVA 0x3543AD08 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of calls N allowed per VLAN per specific time duration；` unsigned_number ` Time in seconds for allowing N calls per VLAN；` unsigned_number ` Time in seconds for blocking calls per VLAN。

[条件 C-6d5cf40f71145888](../../evidence/conditions-sets-042.md#c-6d5cf40f71145888) · [参数 P-7532b015ccdfd0a6](../../evidence/parameters-sets-009.md#p-7532b015ccdfd0a6)

### observed_connections-006485

```text
(config-bba-group)# sessions pre-auth limit ignore <cr>
```

Handler ` RVA 0x11255790 `；selector ` 33 `；EOL ` RVA 0x3543BF30 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-006515

```text
(config-bba-group)# sessions threshold <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 1 `；EOL ` RVA 0x3543B568 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` session loss threshold watermark value。

[条件 C-02b3a076e69d0f90](../../evidence/conditions-sets-002.md#c-02b3a076e69d0f90) · [缺口 G-d830fd3ab4880980](../../evidence/gaps-sets-008.md#g-d830fd3ab4880980) · [参数 P-9c6956ab87ae1cb0](../../evidence/parameters-sets-012.md#p-9c6956ab87ae1cb0)

### observed_connections-006513

```text
(config-bba-group)# sessions threshold percent <number:0..100> interval <number:1..3600> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 2 `；EOL ` RVA 0x3543B880 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` percentage of sessions to be loss for sending trap；` unsigned_number ` pppoe session loss interval。

[条件 C-ffe557c670e46d3b](../../evidence/conditions-sets-099.md#c-ffe557c670e46d3b) · [参数 P-6e3bcfcee92c6624](../../evidence/parameters-sets-009.md#p-6e3bcfcee92c6624)

### observed_connections-006420

```text
(config-bba-group)# tag ppp-max-payload deny <cr>
```

Handler ` RVA 0x11255790 `；selector ` 26 `；EOL ` RVA 0x354353D8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-006522

```text
(config-bba-group)# tag ppp-max-payload minimum <number:dynamic> maximum <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 27 `；EOL ` RVA 0x354356E8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Minimum accepted tag value in decimal. Default 1492；` unsigned_number_dynamic ` Maximum accepted tag value in decimal. Default 1500。

[条件 C-4776bb0c9c87e9fe](../../evidence/conditions-sets-028.md#c-4776bb0c9c87e9fe) · [缺口 G-93051544a2441df6](../../evidence/gaps-sets-005.md#g-93051544a2441df6) · [参数 P-e865abe81e53e5b8](../../evidence/parameters-sets-017.md#p-e865abe81e53e5b8)

### observed_connections-006422

```text
(config-bba-group)# test tag <number:0..65535> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 25 `；EOL ` RVA 0x35436850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tag type in hex or decimal。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [参数 P-a122e17606fa85d1](../../evidence/parameters-sets-012.md#p-a122e17606fa85d1) · [状态效果 S-4155044f7d7d388a](../../evidence/state_effects-sets-014.md#s-4155044f7d7d388a)

### observed_connections-006516

```text
(config-bba-group)# test tag <number:0..65535> <hex-string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 25 `；EOL ` RVA 0x35436850 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tag type in hex or decimal；` hexstring ` Exact Tag value to be sent on wire, in hex。

[条件 C-f3004809fedf6569](../../evidence/conditions-sets-094.md#c-f3004809fedf6569) · [缺口 G-749b0c6c1ae22331](../../evidence/gaps-sets-004.md#g-749b0c6c1ae22331) · [参数 P-ae27585f213211af](../../evidence/parameters-sets-013.md#p-ae27585f213211af) · [状态效果 S-4155044f7d7d388a](../../evidence/state_effects-sets-014.md#s-4155044f7d7d388a)

### observed_connections-006453

```text
(config-bba-group)# test vendor-tag circuit-id client <cr>
```

Handler ` RVA 0x11255790 `；selector ` 13 `；EOL ` RVA 0x35436B88 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [状态效果 S-df26a7341ce9f7f5](../../evidence/state_effects-sets-047.md#s-df26a7341ce9f7f5)

### observed_connections-006493

```text
(config-bba-group)# test vendor-tag circuit-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 15 `；EOL ` RVA 0x35436E98 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Circuit-ID tag string for PPPoE client。

[条件 C-a0baf6e0277025bd](../../evidence/conditions-sets-062.md#c-a0baf6e0277025bd) · [参数 P-86627b1de97858a9](../../evidence/parameters-sets-010.md#p-86627b1de97858a9) · [状态效果 S-df26a7341ce9f7f5](../../evidence/state_effects-sets-047.md#s-df26a7341ce9f7f5)

### observed_connections-006457

```text
(config-bba-group)# test vendor-tag remote-id client <cr>
```

Handler ` RVA 0x11255790 `；selector ` 17 `；EOL ` RVA 0x35437198 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b979fca68cda31b0](../../evidence/conditions-sets-072.md#c-b979fca68cda31b0) · [状态效果 S-df26a7341ce9f7f5](../../evidence/state_effects-sets-047.md#s-df26a7341ce9f7f5)

### observed_connections-006496

```text
(config-bba-group)# test vendor-tag remote-id string <string> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 18 `；EOL ` RVA 0x354374A8 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Remote-ID tag string for PPPoE client。

[条件 C-3d6759c545eedd10](../../evidence/conditions-sets-024.md#c-3d6759c545eedd10) · [参数 P-57494cf7dbc9358b](../../evidence/parameters-sets-007.md#p-57494cf7dbc9358b) · [状态效果 S-df26a7341ce9f7f5](../../evidence/state_effects-sets-047.md#s-df26a7341ce9f7f5)

### observed_connections-006421

```text
(config-bba-group)# vendor-tag circuit-id service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 12 `；EOL ` RVA 0x35435B40 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7484697cbaf95c04](../../evidence/conditions-sets-045.md#c-7484697cbaf95c04)

### observed_connections-006427

```text
(config-bba-group)# vendor-tag dsl-sync-rate service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 19 `；EOL ` RVA 0x35436168 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da92261ef3f23540](../../evidence/conditions-sets-084.md#c-da92261ef3f23540)

### observed_connections-006423

```text
(config-bba-group)# vendor-tag remote-id service <cr>
```

Handler ` RVA 0x11255790 `；selector ` 16 `；EOL ` RVA 0x35435E60 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eaf75bb424bceb6d](../../evidence/conditions-sets-091.md#c-eaf75bb424bceb6d)

### observed_connections-006414

```text
(config-bba-group)# vendor-tag strip <cr>
```

Handler ` RVA 0x11255790 `；selector ` 14 `；EOL ` RVA 0x35436490 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6f9ad7f5a7602095](../../evidence/conditions-sets-043.md#c-6f9ad7f5a7602095)

### observed_connections-006514

```text
(config-bba-group)# virtual-template <number:dynamic> <cr>
```

Handler ` RVA 0x11255790 `；selector ` 8 `；EOL ` RVA 0x35434D68 `。

模式根 ` RVA 0x354347E0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Virtual Template interface number。

[条件 C-b0881e34e30a82c4](../../evidence/conditions-sets-068.md#c-b0881e34e30a82c4) · [缺口 G-2644da7e1618875e](../../evidence/gaps-sets-002.md#g-2644da7e1618875e) · [参数 P-37d2ec1b5b6fb4d5](../../evidence/parameters-sets-005.md#p-37d2ec1b5b6fb4d5)
