# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-057039

```text
(config)# default do-exec test platform software infrastructure drop-debug on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 4 `；EOL ` RVA 0x34378CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057047

```text
(config)# default do-exec test platform software infrastructure pae-cssm send_packet <cr>
```

Handler ` RVA 0x1658B2C0 `；selector ` 0 `；EOL ` RVA 0x35FA4C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-779c6201aeeb38b5](../../evidence/conditions-sets-047.md#c-779c6201aeeb38b5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059048

```text
(config)# default do-exec test platform software infrastructure session open <number:1..4294967295> <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 1 `；EOL ` RVA 0x34379680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Session handle。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-4f1e17e220686aee](../../evidence/parameters-sets-007.md#p-4f1e17e220686aee) · [状态效果 S-3df527bf7e2357ac](../../evidence/state_effects-sets-014.md#s-3df527bf7e2357ac)

### path-057035

```text
(config)# default do-exec test platform software infrastructure watchdog off <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 3 `；EOL ` RVA 0x34378FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057051

```text
(config)# default do-exec test platform software infrastructure watchdog on <cr>
```

Handler ` RVA 0xE9C5930 `；selector ` 2 `；EOL ` RVA 0x34379268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059961

```text
(config)# default do-exec test platform software inject bd <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 1 `；EOL ` RVA 0x343994F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-a9c8be145fb1b3cc](../../evidence/conditions-sets-065.md#c-a9c8be145fb1b3cc) · [参数 P-1b2ddfe043e3c48c](../../evidence/parameters-sets-003.md#p-1b2ddfe043e3c48c) · [状态效果 S-21e8ba3977c94a7a](../../evidence/state_effects-sets-008.md#s-21e8ba3977c94a7a)

### path-059964

```text
(config)# default do-exec test platform software inject bd-local <number:1..4096> <address> <address> ipv4 <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 2 `；EOL ` RVA 0x34399B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` BD number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-d7ef56c55d1404c7](../../evidence/conditions-sets-083.md#c-d7ef56c55d1404c7) · [参数 P-6e5d53caf4ab1776](../../evidence/parameters-sets-009.md#p-6e5d53caf4ab1776) · [状态效果 S-2a7fa5ff851c5c58](../../evidence/state_effects-sets-010.md#s-2a7fa5ff851c5c58)

### path-059669

```text
(config)# default do-exec test platform software inject bridge_vlan <number:1..4096> <address> <address> <cr>
```

Handler ` RVA 0xEA9C880 `；selector ` 4 `；EOL ` RVA 0x3439A9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Bridge VLAN number；` address ` Dst MAC address；` address ` Src MAC address。

[条件 C-ed4e88d6636d168b](../../evidence/conditions-sets-092.md#c-ed4e88d6636d168b) · [参数 P-f32d96ee52c39e1c](../../evidence/parameters-sets-018.md#p-f32d96ee52c39e1c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052194

```text
(config)# default do-exec test platform software inject bypass <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 0 `；EOL ` RVA 0x34398A80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056904

```text
(config)# default do-exec test platform software inject inject-rate <number:1..10000> <cr>
```

Handler ` RVA 0xEA9BB10 `；selector ` 0 `；EOL ` RVA 0x3439A070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` packets/sec supported by platfform。

[条件 C-ed4e88d6636d168b](../../evidence/conditions-sets-092.md#c-ed4e88d6636d168b) · [参数 P-d70ce1762a244fde](../../evidence/parameters-sets-016.md#p-d70ce1762a244fde) · [状态效果 S-fb96d5d4157b022e](../../evidence/state_effects-sets-053.md#s-fb96d5d4157b022e)

### path-056997

```text
(config)# default do-exec test platform software inject ipv4 arp-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 3 `；EOL ` RVA 0x3439BAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b256c3b71822bbf8](../../evidence/conditions-sets-069.md#c-b256c3b71822bbf8) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058977

```text
(config)# default do-exec test platform software inject ipv4 nexthop <address> <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 2 `；EOL ` RVA 0x3439B830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Nexthop Address。

[条件 C-b256c3b71822bbf8](../../evidence/conditions-sets-069.md#c-b256c3b71822bbf8) · [参数 P-c9f339e88974e4e5](../../evidence/parameters-sets-015.md#p-c9f339e88974e4e5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056992

```text
(config)# default do-exec test platform software inject ipv6 nd-trigger <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 4 `；EOL ` RVA 0x3439BD88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b256c3b71822bbf8](../../evidence/conditions-sets-069.md#c-b256c3b71822bbf8) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052202

```text
(config)# default do-exec test platform software inject keepalive <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 6 `；EOL ` RVA 0x343987D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052221

```text
(config)# default do-exec test platform software inject off <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 1 `；EOL ` RVA 0x34398D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052252

```text
(config)# default do-exec test platform software inject pak-priority <cr>
```

Handler ` RVA 0xEA60A60 `；selector ` 5 `；EOL ` RVA 0x34398FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059050

```text
(config)# default do-exec test platform software license expire eval <number:1..259200> <cr>
```

Handler ` RVA 0x12437380 `；selector ` 0 `；EOL ` RVA 0x35867168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` minutes。

[条件 C-2c0106cbc1898a7c](../../evidence/conditions-sets-017.md#c-2c0106cbc1898a7c) · [参数 P-1e0ad3d9a0d06b72](../../evidence/parameters-sets-003.md#p-1e0ad3d9a0d06b72) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057068

```text
(config)# default do-exec test platform software license metering reachability <cr>
```

Handler ` RVA 0x124373D0 `；selector ` 0 `；EOL ` RVA 0x35866E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f5c426468dd25130](../../evidence/conditions-sets-095.md#c-f5c426468dd25130) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056865

```text
(config)# default do-exec test platform software lsmpi tx-fail-retry enable <cr>
```

Handler ` RVA 0xED2D730 `；selector ` 0 `；EOL ` RVA 0x3440C730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-d2a53248814435cb](../../evidence/state_effects-sets-045.md#s-d2a53248814435cb)

### path-059051

```text
(config)# default do-exec test platform software macsec pattern-delete name <string> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 54 `；EOL ` RVA 0x35ECA218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` pattern name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-2b96e7d041d5508f](../../evidence/parameters-sets-004.md#p-2b96e7d041d5508f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060275

```text
(config)# default do-exec test platform software macsec pattern-name name <string> is-control yes has-vlan-tag yes has-vlan-inner-tag yes vlan-id <number:0..65535> inner-vlan-id <number:0..65535> priority <number:0..15> header <string> header-length <number:0..65535> control-frame dmac dest-mac <address> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 55 `；EOL ` RVA 0x35EC94B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` pattern name；` unsigned_number ` outer vlan id；` unsigned_number ` inner vlan id；` unsigned_number ` priority level；` string ` header pattern；` unsigned_number ` header pattern length；` address ` MAC address。

[条件 C-46f9c82671e8712f](../../evidence/conditions-sets-028.md#c-46f9c82671e8712f) · [参数 P-8671486ebe6bccdf](../../evidence/parameters-sets-010.md#p-8671486ebe6bccdf) · [状态效果 S-6e903f67d6253308](../../evidence/state_effects-sets-023.md#s-6e903f67d6253308)

### path-052456

```text
(config)# default do-exec test platform software multicast join <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 1 `；EOL ` RVA 0x3430E098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052484

```text
(config)# default do-exec test platform software multicast leave <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 2 `；EOL ` RVA 0x3430E340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056930

```text
(config)# default do-exec test platform software multicast shim dynamic <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 9 `；EOL ` RVA 0x3430C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056944

```text
(config)# default do-exec test platform software multicast shim notdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 10 `；EOL ` RVA 0x3430CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056906

```text
(config)# default do-exec test platform software multicast shim off <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 6 `；EOL ` RVA 0x3430C2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056890

```text
(config)# default do-exec test platform software multicast shim on <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 7 `；EOL ` RVA 0x3430C018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056919

```text
(config)# default do-exec test platform software multicast shim sticky <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 8 `；EOL ` RVA 0x3430C568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-056963

```text
(config)# default do-exec test platform software multicast shim tdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 11 `；EOL ` RVA 0x3430CD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052427

```text
(config)# default do-exec test platform software multicast start <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 0 `；EOL ` RVA 0x3430DDF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052366

```text
(config)# default do-exec test platform software multicast status <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 4 `；EOL ` RVA 0x3430D028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052508

```text
(config)# default do-exec test platform software multicast stop <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 3 `；EOL ` RVA 0x3430E5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052205

```text
(config)# default do-exec test platform software peer timeout <cr>
```

Handler ` RVA 0xE9492B0 `；selector ` 0 `；EOL ` RVA 0x34350DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-513be3046f6b3107](../../evidence/conditions-sets-032.md#c-513be3046f6b3107) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057123

```text
(config)# default do-exec test platform software plim qos class-map <cr>
```

Handler ` RVA 0xE93D510 `；selector ` 0 `；EOL ` RVA 0x3434D0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-8ae02d0376cb6095](../../evidence/state_effects-sets-030.md#s-8ae02d0376cb6095)

### path-052601

```text
(config)# default do-exec test platform software product-analytics fast-grace-period <cr>
```

Handler ` RVA 0x1658B060 `；selector ` 0 `；EOL ` RVA 0x35FA4068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34ff8707fac2e0b3](../../evidence/conditions-sets-021.md#c-34ff8707fac2e0b3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052544

```text
(config)# default do-exec test platform software product-analytics sa-notify-false <cr>
```

Handler ` RVA 0x1658ADB0 `；selector ` 0 `；EOL ` RVA 0x35FA3B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c42e7c95b62b9b3e](../../evidence/conditions-sets-076.md#c-c42e7c95b62b9b3e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052568

```text
(config)# default do-exec test platform software product-analytics sa-notify-true <cr>
```

Handler ` RVA 0x1658AFD0 `；selector ` 0 `；EOL ` RVA 0x35FA3DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f9c9154b2f7bc0c0](../../evidence/conditions-sets-096.md#c-f9c9154b2f7bc0c0) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052630

```text
(config)# default do-exec test platform software product-analytics timer <cr>
```

Handler ` RVA 0x1658B100 `；selector ` 0 `；EOL ` RVA 0x35FA4310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ecda1560dcb00e7d](../../evidence/conditions-sets-091.md#c-ecda1560dcb00e7d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052188

```text
(config)# default do-exec test platform software punt-keepalive ignore-fault <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 1 `；EOL ` RVA 0x3439C158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052219

```text
(config)# default do-exec test platform software punt-keepalive trigger-failure <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 0 `；EOL ` RVA 0x3439C400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059674

```text
(config)# default do-exec test platform software qos statistics <number:1..50000> <number:1..100000> <number:1..100> <cr>
```

Handler ` RVA 0x10DA0020 `；selector ` 1 `；EOL ` RVA 0x34D1B8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` dpidx from sh pl so dbidx swidb；` unsigned_number ` num queries；` unsigned_number ` num of query in parallel。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-65b36f41d2d9da61](../../evidence/parameters-sets-008.md#p-65b36f41d2d9da61) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052384

```text
(config)# default do-exec test platform software redundancy use-vmac <cr>
```

Handler ` RVA 0x15A6EA80 `；selector ` 0 `；EOL ` RVA 0x35DE5530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058986

```text
(config)# default do-exec test platform software rg ar_alwys_dvrt <number:0..4> <number:0..12> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 7 `；EOL ` RVA 0x3432BC80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-4ffd42aa3d1d5e77](../../evidence/parameters-sets-007.md#p-4ffd42aa3d1d5e77) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059684

```text
(config)# default do-exec test platform software rg notify bulksync <number:0..10> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 2 `；EOL ` RVA 0x3432C378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` result。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-5e3b6cf8076791cc](../../evidence/parameters-sets-008.md#p-5e3b6cf8076791cc) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059977

```text
(config)# default do-exec test platform software rg notify transport <number:0..10> <number:1..100000> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 1 `；EOL ` RVA 0x3432C068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` handler；` unsigned_number ` state。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-769bf5d82d2ae140](../../evidence/parameters-sets-009.md#p-769bf5d82d2ae140) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060197

```text
(config)# default do-exec test platform software rg services parameters <number:0..10> <number:0..10> <number:0..10> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 0 `；EOL ` RVA 0x3432B938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id；` unsigned_number ` rg state；` unsigned_number ` transport request；` unsigned_number ` bulk sync request。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-7c5e56bce406174a](../../evidence/parameters-sets-010.md#p-7c5e56bce406174a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052632

```text
(config)# default do-exec test platform software rg tc-req <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 5 `；EOL ` RVA 0x3432D980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060229

```text
(config)# default do-exec test platform software rg transport parameters <number:1..100000> <number:0..10> <address> <address> <number:0..10> <number:0..2048> <number:0..2048> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 3 `；EOL ` RVA 0x3432C860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` handler；` unsigned_number ` application；` address ` IPv4 src address；` address ` IPv4 dst address；` unsigned_number ` l4 protocol；` unsigned_number ` src port；` unsigned_number ` dst port。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-82c662ee053c7586](../../evidence/parameters-sets-010.md#p-82c662ee053c7586) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059700

```text
(config)# default do-exec test platform software shell command handler automore disable <cr>
```

Handler ` RVA 0xEB0C800 `；selector ` 0 `；EOL ` RVA 0x343B1310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059696

```text
(config)# default do-exec test platform software shell command handler automore manual <cr>
```

Handler ` RVA 0xEB0C900 `；selector ` 0 `；EOL ` RVA 0x343B1068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059032

```text
(config)# default do-exec test platform software shell command handler basic <cr>
```

Handler ` RVA 0xEB0C720 `；selector ` 0 `；EOL ` RVA 0x343B15A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059037

```text
(config)# default do-exec test platform software shell command handler null <cr>
```

Handler ` RVA 0xEB0C640 `；selector ` 0 `；EOL ` RVA 0x343B1850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059692

```text
(config)# default do-exec test platform software shell command handler output redirect <cr>
```

Handler ` RVA 0xEB0CA90 `；selector ` 0 `；EOL ` RVA 0x343B0D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059043

```text
(config)# default do-exec test platform software shell command handler space <cr>
```

Handler ` RVA 0xEB0C560 `；selector ` 0 `；EOL ` RVA 0x343B1AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059018

```text
(config)# default do-exec test platform software shell command set delete <cr>
```

Handler ` RVA 0xEB0CD30 `；selector ` 0 `；EOL ` RVA 0x343B0A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059010

```text
(config)# default do-exec test platform software shell command set load <cr>
```

Handler ` RVA 0xEB0CCE0 `；selector ` 0 `；EOL ` RVA 0x343B0760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058901

```text
(config)# default do-exec test platform software stdout log running-config enable <cr>
```

Handler ` RVA 0xE950340 `；selector ` 0 `；EOL ` RVA 0x34351DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd45860aeb890184](../../evidence/conditions-sets-079.md#c-cd45860aeb890184) · [状态效果 S-9f1f1d7c121e7c54](../../evidence/state_effects-sets-034.md#s-9f1f1d7c121e7c54)

### path-056901

```text
(config)# default do-exec test platform software tdl ping rp <cr>
```

Handler ` RVA 0xE90CE60 `；selector ` 0 `；EOL ` RVA 0x343432E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-805256a98e774e10](../../evidence/conditions-sets-050.md#c-805256a98e774e10) · [状态效果 S-babd7a3db9d0b021](../../evidence/state_effects-sets-039.md#s-babd7a3db9d0b021)

### path-058929

```text
(config)# default do-exec test platform software tdl ping rp stats <cr>
```

Handler ` RVA 0xE90F1B0 `；selector ` 0 `；EOL ` RVA 0x34343800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-805256a98e774e10](../../evidence/conditions-sets-050.md#c-805256a98e774e10) · [状态效果 S-babd7a3db9d0b021](../../evidence/state_effects-sets-039.md#s-babd7a3db9d0b021)

### path-059638

```text
(config)# default do-exec test platform software tdl ping rp stats clear <cr>
```

Handler ` RVA 0xE90F090 `；selector ` 0 `；EOL ` RVA 0x343437D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-805256a98e774e10](../../evidence/conditions-sets-050.md#c-805256a98e774e10) · [状态效果 S-babd7a3db9d0b021](../../evidence/state_effects-sets-039.md#s-babd7a3db9d0b021)

### path-059979

```text
(config)# default do-exec test platform software timestamp-engine oam y1731 default disable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 4 `；EOL ` RVA 0x35DE78A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff0158eefc867b95](../../evidence/conditions-sets-098.md#c-ff0158eefc867b95) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059974

```text
(config)# default do-exec test platform software timestamp-engine oam y1731 default enable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 2 `；EOL ` RVA 0x35DE7268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3a063ed786e14f24](../../evidence/conditions-sets-022.md#c-3a063ed786e14f24) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057069

```text
(config)# default do-exec test platform software uidp batch-count <number:0..1000> <cr>
```

Handler ` RVA 0x1599CE30 `；selector ` 0 `；EOL ` RVA 0x35DCF728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of user sessions per batch。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-7c336c4b98660031](../../evidence/parameters-sets-010.md#p-7c336c4b98660031) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057063

```text
(config)# default do-exec test platform software uidp binding clear <cr>
```

Handler ` RVA 0x1599C3F0 `；selector ` 0 `；EOL ` RVA 0x35DCEE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060141

```text
(config)# default do-exec test platform software uidp binding ip-user add <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 0 `；EOL ` RVA 0x35DCE1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-168aba61599d0180](../../evidence/parameters-sets-002.md#p-168aba61599d0180) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060143

```text
(config)# default do-exec test platform software uidp binding ip-user delete <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 1 `；EOL ` RVA 0x35DCE4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-82cd5055a6ddb96f](../../evidence/parameters-sets-010.md#p-82cd5055a6ddb96f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059705

```text
(config)# default do-exec test platform software uidp binding user-usergroup add <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 2 `；EOL ` RVA 0x35DCE8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-12f4f3bbd76a04fe](../../evidence/parameters-sets-002.md#p-12f4f3bbd76a04fe) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059708

```text
(config)# default do-exec test platform software uidp binding user-usergroup delete <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 3 `；EOL ` RVA 0x35DCEBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-1defe1bf1a446589](../../evidence/parameters-sets-003.md#p-1defe1bf1a446589) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057078

```text
(config)# default do-exec test platform software uidp dwnld-timer <number:100..2000> <cr>
```

Handler ` RVA 0x1599CEA0 `；selector ` 0 `；EOL ` RVA 0x35DCF9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pause time for downloading batch of sessions。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-72b2461fd4b2a57e](../../evidence/parameters-sets-009.md#p-72b2461fd4b2a57e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057046

```text
(config)# default do-exec test platform software uidp user <string> <cr>
```

Handler ` RVA 0x1599CCD0 `；selector ` 4 `；EOL ` RVA 0x35DCF150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` User name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-0fa27b7ec79838bd](../../evidence/parameters-sets-002.md#p-0fa27b7ec79838bd) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057059

```text
(config)# default do-exec test platform software uidp user-group <string> <cr>
```

Handler ` RVA 0x1599CD80 `；selector ` 5 `；EOL ` RVA 0x35DCF440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` User group name。

[条件 C-ff9c946997ed0ce2](../../evidence/conditions-sets-099.md#c-ff9c946997ed0ce2) · [参数 P-a9f2b7b5d4e2e4fa](../../evidence/parameters-sets-013.md#p-a9f2b7b5d4e2e4fa) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059716

```text
(config)# default do-exec test platform software usb slot <number:1..4294967295> usbflash0 fake-remove <cr>
```

Handler ` RVA 0xE9C72A0 `；selector ` 0 `；EOL ` RVA 0x3437C7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` slot/switch Number。

[条件 C-a37c5dd4ddfec3d9](../../evidence/conditions-sets-063.md#c-a37c5dd4ddfec3d9) · [参数 P-8880f5ca265b7b86](../../evidence/parameters-sets-011.md#p-8880f5ca265b7b86) · [状态效果 S-26cfa3fc725d3e04](../../evidence/state_effects-sets-009.md#s-26cfa3fc725d3e04)

### path-039896

```text
(config)# default do-exec test pm <string> <cr>
```

Handler ` RVA 0x15DD1600 `；selector ` 0 `；EOL ` RVA 0x35E22898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ...。

[条件 C-8cbb5653d1027960](../../evidence/conditions-sets-054.md#c-8cbb5653d1027960) · [参数 P-bc02e5e87b3d0fdc](../../evidence/parameters-sets-014.md#p-bc02e5e87b3d0fdc) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048116

```text
(config)# default do-exec test policy-manager appl-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f1913a29079355a](../../evidence/conditions-sets-018.md#c-2f1913a29079355a) · [状态效果 S-00446f1feddee874](../../evidence/state_effects-sets-001.md#s-00446f1feddee874)

### path-048162

```text
(config)# default do-exec test policy-manager wd-timer-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-202d71370fb84be8](../../evidence/conditions-sets-013.md#c-202d71370fb84be8) · [状态效果 S-ae4ff24c97002041](../../evidence/state_effects-sets-037.md#s-ae4ff24c97002041)

### path-060175

```text
(config)# default do-exec test pppatm subscriber delay <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <cr>
```

Handler ` RVA 0x1111E220 `；selector ` 0 `；EOL ` RVA 0x35401D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` msecs. for subscriber msgs；` unsigned_number ` msecs. for ppp msgs；` unsigned_number ` msecs. for peer msgs；` unsigned_number ` msecs. for feature msgs；` unsigned_number ` msecs. for incoming calls；` unsigned_number ` msecs. for vaccess。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9a76ee1c5bfa38c4](../../evidence/parameters-sets-012.md#p-9a76ee1c5bfa38c4) · [状态效果 S-625d48e88f72eb09](../../evidence/state_effects-sets-021.md#s-625d48e88f72eb09)

### path-031063

```text
(config)# default do-exec test pppoe <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 0 `；EOL ` RVA 0x356B32E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-273139fdb81197ba](../../evidence/state_effects-sets-009.md#s-273139fdb81197ba)

### path-047101

```text
(config)# default do-exec test pppoe init-session-num <number:1..65535> <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 12 `；EOL ` RVA 0x356B3650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Starting PPPoE Session Number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-465592a267d1213c](../../evidence/parameters-sets-006.md#p-465592a267d1213c) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-054374

```text
(config)# default do-exec test pppoe session <number:1..20000> autogrant <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 2 `；EOL ` RVA 0x356B48A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057964

```text
(config)# default do-exec test pppoe session <number:1..20000> autogrant on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 1 `；EOL ` RVA 0x356B45F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057985

```text
(config)# default do-exec test pppoe session <number:1..20000> grant-threshold <number:0..65534> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 6 `；EOL ` RVA 0x356B56E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set grant credit unit threshold 。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c52715e3f07536be](../../evidence/parameters-sets-015.md#p-c52715e3f07536be) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-054341

```text
(config)# default do-exec test pppoe session <number:1..20000> headDropping <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 16 `；EOL ` RVA 0x356B3D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057950

```text
(config)# default do-exec test pppoe session <number:1..20000> headDropping on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 15 `；EOL ` RVA 0x356B3AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-054354

```text
(config)# default do-exec test pppoe session <number:1..20000> inband-credits <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 14 `；EOL ` RVA 0x356B42F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057957

```text
(config)# default do-exec test pppoe session <number:1..20000> inband-credits on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 13 `；EOL ` RVA 0x356B4050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-058002

```text
(config)# default do-exec test pppoe session <number:1..20000> local-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 10 `；EOL ` RVA 0x356B5CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credits。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-1eb21824c744cc30](../../evidence/parameters-sets-003.md#p-1eb21824c744cc30) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057976

```text
(config)# default do-exec test pppoe session <number:1..20000> max-grant <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 5 `；EOL ` RVA 0x356B53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set maximum number of credit units per grant。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-513dc72ce2a78132](../../evidence/parameters-sets-007.md#p-513dc72ce2a78132) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057989

```text
(config)# default do-exec test pppoe session <number:1..20000> padg <number:1..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 7 `；EOL ` RVA 0x356B50F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Number of PPPoE credit units to grant。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-18fe21eb467de39c](../../evidence/parameters-sets-002.md#p-18fe21eb467de39c) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057979

```text
(config)# default do-exec test pppoe session <number:1..20000> padg off <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 3 `；EOL ` RVA 0x356B4E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-057968

```text
(config)# default do-exec test pppoe session <number:1..20000> padg on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 4 `；EOL ` RVA 0x356B4BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-058074

```text
(config)# default do-exec test pppoe session <number:1..20000> padq receive-only <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 8 `；EOL ` RVA 0x356B6218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-198e6be8adbeecd8](../../evidence/state_effects-sets-006.md#s-198e6be8adbeecd8)

### path-057993

```text
(config)# default do-exec test pppoe session <number:1..20000> peer-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 9 `；EOL ` RVA 0x356B59D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credit units。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-cec15d709fc4fb0a](../../evidence/parameters-sets-016.md#p-cec15d709fc4fb0a) · [状态效果 S-0cb2f66981946a2e](../../evidence/state_effects-sets-003.md#s-0cb2f66981946a2e)

### path-056787

```text
(config)# default do-exec test process create <number:1..5000> <number:1..10000> <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2550 `；selector ` 0 `；EOL ` RVA 0x33ECDDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter time to run for (ms)；` unsigned_number ` Enter time to sleep for (ms)；` unsigned_number ` Enter time to susp after (ms)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f57e4b11ecf3ba88](../../evidence/parameters-sets-018.md#p-f57e4b11ecf3ba88) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-044112

```text
(config)# default do-exec test process kill <number:1..4294967295> <cr>
```

Handler ` RVA 0xD6D2A10 `；selector ` 0 `；EOL ` RVA 0x33ECE140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pid to kill。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-cca3915cfbc7547d](../../evidence/parameters-sets-016.md#p-cca3915cfbc7547d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-031524

```text
(config)# default do-exec test rfd <cr>
```

Handler ` RVA 0xD7C53C0 `；selector ` 0 `；EOL ` RVA 0x33EF4C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be2db87780940846](../../evidence/conditions-sets-073.md#c-be2db87780940846) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054107

```text
(config)# default do-exec test rib application create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 5 `；EOL ` RVA 0x3400B460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Application instance name。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [参数 P-44a7689de98431a1](../../evidence/parameters-sets-006.md#p-44a7689de98431a1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054085

```text
(config)# default do-exec test rib application delete <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 6 `；EOL ` RVA 0x3400B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [参数 P-84485f3ce4166b87](../../evidence/parameters-sets-010.md#p-84485f3ce4166b87) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054014

```text
(config)# default do-exec test rib client create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 0 `；EOL ` RVA 0x34009A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Client name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6fbb31bff7eebb42](../../evidence/parameters-sets-009.md#p-6fbb31bff7eebb42) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053877

```text
(config)# default do-exec test rib client delete <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 1 `；EOL ` RVA 0x34009758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-61bebf93f1ef1e6e](../../evidence/parameters-sets-008.md#p-61bebf93f1ef1e6e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054146

```text
(config)# default do-exec test rib firsthop <address> <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 7 `；EOL ` RVA 0x3400AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` destination address；` unsigned_number ` Multipath path select index。

[条件 C-c2292911a7e8bfe1](../../evidence/conditions-sets-075.md#c-c2292911a7e8bfe1) · [参数 P-adbd895aad18df4d](../../evidence/parameters-sets-013.md#p-adbd895aad18df4d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054023

```text
(config)# default do-exec test rib route show <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 3 `；EOL ` RVA 0x3400A550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [参数 P-8d99215107ac3986](../../evidence/parameters-sets-011.md#p-8d99215107ac3986) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054062

```text
(config)# default do-exec test rib table set forwarding-base <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 4 `；EOL ` RVA 0x3400A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-04b8fa829f79145d](../../evidence/conditions-sets-002.md#c-04b8fa829f79145d) · [状态效果 S-3629f4634ee4b813](../../evidence/state_effects-sets-012.md#s-3629f4634ee4b813)

### path-037249

```text
(config)# default do-exec test rib ut <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 8 `；EOL ` RVA 0x34009DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea981e0e12eb7a51](../../evidence/conditions-sets-091.md#c-ea981e0e12eb7a51) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054721

```text
(config)# default do-exec test rmi create user-type <string> <cr>
```

Handler ` RVA 0xE081680 `；selector ` 0 `；EOL ` RVA 0x341D60C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Resource User-Type Name。

[条件 C-0b0b6e41a17a8c06](../../evidence/conditions-sets-005.md#c-0b0b6e41a17a8c06) · [参数 P-71c7f62eb30da67d](../../evidence/parameters-sets-009.md#p-71c7f62eb30da67d) · [状态效果 S-e95013cfd59378d8](../../evidence/state_effects-sets-049.md#s-e95013cfd59378d8)

### path-039478

```text
(config)# default do-exec test rmi entphyind <cr>
```

Handler ` RVA 0xD695F20 `；selector ` 0 `；EOL ` RVA 0x341D7518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059868

```text
(config)# default do-exec test rmon hc-alarms <number:1..65535> Low32bitvalue <number:0..4294967295> High32bitvalue <number:0..4294967295> <cr>
```

Handler ` RVA 0xC4F9D90 `；selector ` 0 `；EOL ` RVA 0x33AADCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Hc alarm index；` unsigned_number ` Low32bitvalue；` unsigned_number ` High32bitvalue。

[条件 C-716d9d144a297e82](../../evidence/conditions-sets-044.md#c-716d9d144a297e82) · [参数 P-88ec7857607f280e](../../evidence/parameters-sets-011.md#p-88ec7857607f280e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060066

```text
(config)# default do-exec test rsvp metadata forward <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x100784A0 `；selector ` 0 `；EOL ` RVA 0x34A3F398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-44e300ba87708e67](../../evidence/conditions-sets-027.md#c-44e300ba87708e67) · [参数 P-164d4baefc6af40a](../../evidence/parameters-sets-002.md#p-164d4baefc6af40a) · [状态效果 S-f02e91be543b0994](../../evidence/state_effects-sets-051.md#s-f02e91be543b0994)

### path-046916

```text
(config)# default do-exec test rsvp nsr disable <cr>
```

Handler ` RVA 0x10078B00 `；selector ` 0 `；EOL ` RVA 0x34A3ED00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046883

```text
(config)# default do-exec test rsvp nsr enable <cr>
```

Handler ` RVA 0x100789F0 `；selector ` 0 `；EOL ` RVA 0x34A3EA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046853

```text
(config)# default do-exec test rsvp nsr incr <cr>
```

Handler ` RVA 0x100788E0 `；selector ` 0 `；EOL ` RVA 0x34A3E7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046821

```text
(config)# default do-exec test rsvp nsr start <cr>
```

Handler ` RVA 0x100787C0 `；selector ` 0 `；EOL ` RVA 0x34A3E508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060250

```text
(config)# default do-exec test rsvp transport send path <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..65535> <address> <number:1..65535> data <string> <cr>
```

Handler ` RVA 0x1005D100 `；selector ` 0 `；EOL ` RVA 0x34A3DFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Client Identifier；` address ` Initiator Id；` unsigned_number ` Instance Id；` string ` RSVP Transport message。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-c024f648c9188b95](../../evidence/parameters-sets-015.md#p-c024f648c9188b95) · [状态效果 S-461d31e80e83e5e7](../../evidence/state_effects-sets-015.md#s-461d31e80e83e5e7)

### path-048890

```text
(config)# default do-exec test rtty <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xCC38580 `；selector ` 0 `；EOL ` RVA 0x33C237D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Remote Seat ID(in hexadecimal)；` string ` Command String。

[条件 C-9ee8389756ff7b14](../../evidence/conditions-sets-061.md#c-9ee8389756ff7b14) · [参数 P-87096cdef34360d5](../../evidence/parameters-sets-010.md#p-87096cdef34360d5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-049033

```text
(config)# default do-exec test rtty statistics disable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 0 `；EOL ` RVA 0x33C23D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7b263b83285ee6b6](../../evidence/conditions-sets-048.md#c-7b263b83285ee6b6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048962

```text
(config)# default do-exec test rtty statistics enable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 1 `；EOL ` RVA 0x33C23A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c937aa2f37c5639d](../../evidence/conditions-sets-078.md#c-c937aa2f37c5639d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-049085

```text
(config)# default do-exec test rtty statistics print <cr>
```

Handler ` RVA 0xCC38340 `；selector ` 0 `；EOL ` RVA 0x33C23FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2f67e2e03fdf8f75](../../evidence/conditions-sets-019.md#c-2f67e2e03fdf8f75) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059491

```text
(config)# default do-exec test sasl client ip <address> port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 1 `；EOL ` RVA 0x34B14C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0a6a0a313046b956](../../evidence/parameters-sets-001.md#p-0a6a0a313046b956) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060095

```text
(config)# default do-exec test sasl client ip <address> port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 2 `；EOL ` RVA 0x34B14F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection；` string ` SASL profile name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f6b83400a54cfc55](../../evidence/parameters-sets-018.md#p-f6b83400a54cfc55) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-055386

```text
(config)# default do-exec test sasl server port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 3 `；EOL ` RVA 0x34B153F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port value for SASL listening。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f5808002237e59f6](../../evidence/parameters-sets-018.md#p-f5808002237e59f6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059488

```text
(config)# default do-exec test sasl server port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 4 `；EOL ` RVA 0x34B156E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Port value for SASL listening；` string ` SASL profile name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7fbae1e202e71069](../../evidence/parameters-sets-010.md#p-7fbae1e202e71069) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-049171

```text
(config)# default do-exec test sasl server stop <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 5 `；EOL ` RVA 0x34B15978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-034270

```text
(config)# default do-exec test save snapshot <cr>
```

Handler ` RVA 0xD6D2B10 `；selector ` 0 `；EOL ` RVA 0x33ECE430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046521

```text
(config)# default do-exec test scheduler trash edisms <cr>
```

Handler ` RVA 0xD7A41D0 `；selector ` 0 `；EOL ` RVA 0x33EEE678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f463be9d971647c6](../../evidence/conditions-sets-094.md#c-f463be9d971647c6) · [状态效果 S-cc3c72e62a88365d](../../evidence/state_effects-sets-043.md#s-cc3c72e62a88365d)

### path-035584

```text
(config)# default do-exec test scheduler watched-message <cr>
```

Handler ` RVA 0xD79FA20 `；selector ` 0 `；EOL ` RVA 0x33EED500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c2445050f638f023](../../evidence/conditions-sets-075.md#c-c2445050f638f023) · [状态效果 S-edd0a690950a2e02](../../evidence/state_effects-sets-050.md#s-edd0a690950a2e02)

### path-046459

```text
(config)# default do-exec test sctp association create <cr>
```

Handler ` RVA 0xCE848E0 `；selector ` 0 `；EOL ` RVA 0x33D12C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037070

```text
(config)# default do-exec test sctp delete <cr>
```

Handler ` RVA 0xCE84E80 `；selector ` 0 `；EOL ` RVA 0x33D12690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046410

```text
(config)# default do-exec test sctp instance create <cr>
```

Handler ` RVA 0xCE828C0 `；selector ` 0 `；EOL ` RVA 0x33D12308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053766

```text
(config)# default do-exec test sctp instance delete <number:1..65535> <cr>
```

Handler ` RVA 0xCE847D0 `；selector ` 0 `；EOL ` RVA 0x33D12668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Local port of instance to delete。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-b7f8a9d96e4fa6a8](../../evidence/parameters-sets-014.md#p-b7f8a9d96e4fa6a8) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054029

```text
(config)# default do-exec test sctp parameters burstsize <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 8 `；EOL ` RVA 0x33D0FE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of packets to burst。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5f332658bcc3b1ba](../../evidence/parameters-sets-008.md#p-5f332658bcc3b1ba) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057923

```text
(config)# default do-exec test sctp parameters congabate <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 17 `；EOL ` RVA 0x33D11C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Congestion level to define abate value；` unsigned_number ` Value for congestion abate。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6e3b56e35279f34e](../../evidence/parameters-sets-009.md#p-6e3b56e35279f34e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054214

```text
(config)# default do-exec test sctp parameters conglevels <number:0..3> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 15 `；EOL ` RVA 0x33D115A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of congestion levels to define。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-90dac4eb92412f64](../../evidence/parameters-sets-011.md#p-90dac4eb92412f64) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057915

```text
(config)# default do-exec test sctp parameters congonset <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 16 `；EOL ` RVA 0x33D118E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Congestion level to define onset value；` unsigned_number ` Value for congestion onset。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-07fdbf832d65708c](../../evidence/parameters-sets-001.md#p-07fdbf832d65708c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054064

```text
(config)# default do-exec test sctp parameters delay <number:0..60000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 9 `；EOL ` RVA 0x33D10118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Delay (msecs) between bursts。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-a85ef6772e443ce4](../../evidence/parameters-sets-013.md#p-a85ef6772e443ce4) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047030

```text
(config)# default do-exec test sctp parameters display <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 0 `；EOL ` RVA 0x33D11EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053842

```text
(config)# default do-exec test sctp parameters fixedparams <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 4 `；EOL ` RVA 0x33D0F268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Use fixed params (FALSE=0/TRUE=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-148bb4a30eac7147](../../evidence/parameters-sets-002.md#p-148bb4a30eac7147) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054089

```text
(config)# default do-exec test sctp parameters hbenabled <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 10 `；EOL ` RVA 0x33D10408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Heartbeat dest addrs (FALSE=0/TRUE=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-acd27b8447a1b688](../../evidence/parameters-sets-013.md#p-acd27b8447a1b688) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054110

```text
(config)# default do-exec test sctp parameters hbtimeout <number:0..600000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 11 `；EOL ` RVA 0x33D106F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Heartbeat timer value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-001bdbe6024b7fc0](../../evidence/parameters-sets-001.md#p-001bdbe6024b7fc0) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053730

```text
(config)# default do-exec test sctp parameters instreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 1 `；EOL ` RVA 0x33D0E998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of inbound streams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f60c7b1ad05500ca](../../evidence/parameters-sets-018.md#p-f60c7b1ad05500ca) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054179

```text
(config)# default do-exec test sctp parameters maxRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 13 `；EOL ` RVA 0x33D10FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Max retrans timer value (ms)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-656c5afea3fc72ab](../../evidence/parameters-sets-008.md#p-656c5afea3fc72ab) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053987

```text
(config)# default do-exec test sctp parameters maxoutstand <number:0..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 7 `；EOL ` RVA 0x33D0FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Max number of packets outstanding。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-565a162e37a45ac2](../../evidence/parameters-sets-007.md#p-565a162e37a45ac2) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053938

```text
(config)# default do-exec test sctp parameters maxpackets <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 6 `；EOL ` RVA 0x33D0F848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Max number of packets to send (9999=inf)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-7b10493dc6084a57](../../evidence/parameters-sets-010.md#p-7b10493dc6084a57) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053803

```text
(config)# default do-exec test sctp parameters maxpdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 3 `；EOL ` RVA 0x33D0EF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-0cff93470ff98b66](../../evidence/parameters-sets-001.md#p-0cff93470ff98b66) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054153

```text
(config)# default do-exec test sctp parameters minRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 12 `；EOL ` RVA 0x33D10CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Min retrans timer value (ms)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f7c8c4e77b4b985e](../../evidence/parameters-sets-018.md#p-f7c8c4e77b4b985e) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053694

```text
(config)# default do-exec test sctp parameters outstreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 0 `；EOL ` RVA 0x33D0E6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of outbound streams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-71ac10a0fbb6fc04](../../evidence/parameters-sets-009.md#p-71ac10a0fbb6fc04) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053767

```text
(config)# default do-exec test sctp parameters pdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 2 `；EOL ` RVA 0x33D0EC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-6fa3fc9c170f9a06](../../evidence/parameters-sets-009.md#p-6fa3fc9c170f9a06) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054198

```text
(config)# default do-exec test sctp parameters rcvwin <number:1500..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 14 `；EOL ` RVA 0x33D112B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Local receive window value (bytes)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ac176c644c368388](../../evidence/parameters-sets-013.md#p-ac176c644c368388) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054132

```text
(config)# default do-exec test sctp parameters testtype <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 18 `；EOL ` RVA 0x33D109E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Test type (SIMPLE=0/LOOPREQ=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-ed32cc90492c4587](../../evidence/parameters-sets-018.md#p-ed32cc90492c4587) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053889

```text
(config)# default do-exec test sctp parameters usealladdrs <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 5 `；EOL ` RVA 0x33D0F558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Use all dest addrs (FALSE=0/TRUE=1)?。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-64b63411945a3011](../../evidence/parameters-sets-008.md#p-64b63411945a3011) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-047988

```text
(config)# default do-exec test sdb add <string> <cr>
```

Handler ` RVA 0xDEC82E0 `；selector ` 0 `；EOL ` RVA 0x34093138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5c1d0be0e07d0031](../../evidence/parameters-sets-007.md#p-5c1d0be0e07d0031) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048031

```text
(config)# default do-exec test sdb remove <string> <cr>
```

Handler ` RVA 0xDEC8430 `；selector ` 0 `；EOL ` RVA 0x34093420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-5c6127879750809b](../../evidence/parameters-sets-007.md#p-5c6127879750809b) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048074

```text
(config)# default do-exec test sdb search <string> <cr>
```

Handler ` RVA 0xDEC8550 `；selector ` 0 `；EOL ` RVA 0x340936E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-427368a9e0878d44](../../evidence/parameters-sets-006.md#p-427368a9e0878d44) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046626

```text
(config)# default do-exec test service-overlay application register <cr>
```

Handler ` RVA 0x108F5810 `；selector ` 1 `；EOL ` RVA 0x34BF7E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-16bff770590b3413](../../evidence/conditions-sets-009.md#c-16bff770590b3413) · [状态效果 S-0083adb90c9fd1d5](../../evidence/state_effects-sets-001.md#s-0083adb90c9fd1d5)

### path-057951

```text
(config)# default do-exec test service-routing api debug <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 17 `；EOL ` RVA 0x34B2F8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Debug flags。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-fc2096c688c2da52](../../evidence/parameters-sets-019.md#p-fc2096c688c2da52) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060270

```text
(config)# default do-exec test service-routing api publish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:1..4294967295> <number:0..32768> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 21 `；EOL ` RVA 0x34B2E0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Service-sequence；` unsigned_number ` Service-size。

[条件 C-3852d83c46d8182b](../../evidence/conditions-sets-022.md#c-3852d83c46d8182b) · [参数 P-bbe7af018acbc6ac](../../evidence/parameters-sets-014.md#p-bbe7af018acbc6ac) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054263

```text
(config)# default do-exec test service-routing api register-client <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 24 `；EOL ` RVA 0x34B2D520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Client context。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-c58be6cbdbca42b7](../../evidence/parameters-sets-015.md#p-c58be6cbdbca42b7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057922

```text
(config)# default do-exec test service-routing api register-client <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 23 `；EOL ` RVA 0x34B2D4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Client context；` string ` Client name。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-28a8a8d90e5fc0a1](../../evidence/parameters-sets-004.md#p-28a8a8d90e5fc0a1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060267

```text
(config)# default do-exec test service-routing api subscribe-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:0..255> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 19 `；EOL ` RVA 0x34B2F088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Maximum-paths。

[条件 C-f83ee40f41020790](../../evidence/conditions-sets-096.md#c-f83ee40f41020790) · [参数 P-7447444ab7796741](../../evidence/parameters-sets-009.md#p-7447444ab7796741) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060259

```text
(config)# default do-exec test service-routing api unpublish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 20 `；EOL ` RVA 0x34B2E898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-ab217c6e4930bfe1](../../evidence/conditions-sets-066.md#c-ab217c6e4930bfe1) · [参数 P-6205f9bccb319166](../../evidence/parameters-sets-008.md#p-6205f9bccb319166) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054256

```text
(config)# default do-exec test service-routing api unregister-client <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 22 `；EOL ` RVA 0x34B2DA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-fd4fdd18c511da0a](../../evidence/parameters-sets-019.md#p-fd4fdd18c511da0a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057944

```text
(config)# default do-exec test service-routing api unsubscribe-service <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 18 `；EOL ` RVA 0x34B2F598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Subscription handle。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-ea16afa033846cd9](../../evidence/parameters-sets-018.md#p-ea16afa033846cd9) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046965

```text
(config)# default do-exec test service-routing api version <cr>
```

Handler ` RVA 0x10452690 `；selector ` 25 `；EOL ` RVA 0x34B2D1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059845

```text
(config)# default do-exec test service-routing capabilities-manager api register <string> <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Component；` string ` Capability；` string ` Capability Data。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-2cd42d186cef97f3](../../evidence/parameters-sets-004.md#p-2cd42d186cef97f3) · [状态效果 S-8f006ce31ad77646](../../evidence/state_effects-sets-030.md#s-8f006ce31ad77646)

### path-059322

```text
(config)# default do-exec test service-routing capabilities-manager api unregister <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Component；` string ` Capability。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-ca371a52bc56aa69](../../evidence/parameters-sets-015.md#p-ca371a52bc56aa69) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-054235

```text
(config)# default do-exec test service-routing capabilities-manager api version <cr>
```

Handler ` RVA 0x1045B660 `；selector ` 79 `；EOL ` RVA 0x34B34CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059320

```text
(config)# default do-exec test service-routing xmcp client <number:0..4294967295> error-response <number:100..699> <cr>
```

Handler ` RVA 0x10472C70 `；selector ` 56 `；EOL ` RVA 0x34B37C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Error code。

[条件 C-e701e52bacd9039a](../../evidence/conditions-sets-089.md#c-e701e52bacd9039a) · [参数 P-82ab05eb296bdede](../../evidence/parameters-sets-010.md#p-82ab05eb296bdede) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046529

```text
(config)# default do-exec test session-mgr acct-stats start <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-ea8aa4bd91f32bad](../../evidence/state_effects-sets-050.md#s-ea8aa4bd91f32bad)

### path-053929

```text
(config)# default do-exec test session-mgr cga-remote-auth authc <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-da2f08bdc200c03c](../../evidence/parameters-sets-016.md#p-da2f08bdc200c03c) · [状态效果 S-27c55bb28079ac90](../../evidence/state_effects-sets-009.md#s-27c55bb28079ac90)

### path-057818

```text
(config)# default do-exec test session-mgr crimson table mab create <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-08542384c729ce77](../../evidence/state_effects-sets-002.md#s-08542384c729ce77)

### path-059796

```text
(config)# default do-exec test session-mgr event send async start handle <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B96910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-dbf47fc2f6ef65b4](../../evidence/conditions-sets-085.md#c-dbf47fc2f6ef65b4) · [参数 P-96568601ab7c7b37](../../evidence/parameters-sets-012.md#p-96568601ab7c7b37) · [状态效果 S-b9d6055466f20697](../../evidence/state_effects-sets-039.md#s-b9d6055466f20697)

### path-054021

```text
(config)# default do-exec test session-mgr fqdn-epm-notify <number:1..4294967295> <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Handle value；` address ` IP address to notify。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-d0e66e8ab24af0c2](../../evidence/parameters-sets-016.md#p-d0e66e8ab24af0c2) · [状态效果 S-c8f59bc1d43c2f0e](../../evidence/state_effects-sets-043.md#s-c8f59bc1d43c2f0e)

### path-046815

```text
(config)# default do-exec test session-mgr green create <cr>
```

Handler ` RVA 0xCAD3E50 `；selector ` 0 `；EOL ` RVA 0x33B99460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-d700d930b0dbeb1c](../../evidence/state_effects-sets-046.md#s-d700d930b0dbeb1c)

### path-059837

```text
(config)# default do-exec test session-mgr identity mac <address> add ip <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B9A048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MAC address；` address ` IP address。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-bb158b26fcbfa514](../../evidence/parameters-sets-014.md#p-bb158b26fcbfa514) · [状态效果 S-2e4301c9c8ffb16b](../../evidence/state_effects-sets-010.md#s-2e4301c9c8ffb16b)

### path-046481

```text
(config)# default do-exec test session-mgr sm-client register <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [状态效果 S-48cc9575ee1d1550](../../evidence/state_effects-sets-016.md#s-48cc9575ee1d1550)

### path-059273

```text
(config)# default do-exec test session-mgr test-vlan <string> <number:1..4095> <number:1..4> <number:1..1000> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the vlan group；` unsigned_number ` Value of the vlan；` unsigned_number ` 1 to add any other value to remove；` unsigned_number ` Number of users。

[条件 C-34930c8cd32478c6](../../evidence/conditions-sets-020.md#c-34930c8cd32478c6) · [参数 P-8f6fc02bc311139a](../../evidence/parameters-sets-011.md#p-8f6fc02bc311139a) · [状态效果 S-868e73af3699bfd2](../../evidence/state_effects-sets-029.md#s-868e73af3699bfd2)

### path-046212

```text
(config)# default do-exec test snmp cpu-stats start <cr>
```

Handler ` RVA 0xCC7C220 `；selector ` 0 `；EOL ` RVA 0x33C3C500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-44e127c949423ac8](../../evidence/conditions-sets-027.md#c-44e127c949423ac8) · [状态效果 S-e43903158ab8081f](../../evidence/state_effects-sets-048.md#s-e43903158ab8081f)

### path-046564

```text
(config)# default do-exec test snmp trap config-copy <cr>
```

Handler ` RVA 0x104C05D0 `；selector ` 41 `；EOL ` RVA 0x33C3C888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-f5fd4fcb048a5166](../../evidence/state_effects-sets-052.md#s-f5fd4fcb048a5166)

### path-053197

```text
(config)# default do-exec test ssm asynchronous throttling print <cr>
```

Handler ` RVA 0x10433590 `；selector ` 0 `；EOL ` RVA 0x34B25118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-a3b5c91e7d65069e](../../evidence/state_effects-sets-035.md#s-a3b5c91e7d65069e)

### path-045391

```text
(config)# default do-exec test ssm counters enable <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B23798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-27ad99a4f9d3f7f7](../../evidence/state_effects-sets-009.md#s-27ad99a4f9d3f7f7)

### path-057223

```text
(config)# default do-exec test ssm fcdb nosupport <number:1..25> <number:0..2> <cr>
```

Handler ` RVA 0x104365F0 `；selector ` 0 `；EOL ` RVA 0x34B23BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` feature type；` unsigned_number ` nosupport action (0=ignore, 1=punt, 2=teardown seg)。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-23be321c29567b35](../../evidence/parameters-sets-003.md#p-23be321c29567b35) · [状态效果 S-274a98b6df264b2d](../../evidence/state_effects-sets-009.md#s-274a98b6df264b2d)

### path-045745

```text
(config)# default do-exec test ssm feature status <cr>
```

Handler ` RVA 0x10435390 `；selector ` 0 `；EOL ` RVA 0x34B24850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-0e30be63b43baf87](../../evidence/state_effects-sets-003.md#s-0e30be63b43baf87)

### path-052963

```text
(config)# default do-exec test ssm repop <number:1..14> <number:0..2> <cr>
```

Handler ` RVA 0x104331B0 `；selector ` 0 `；EOL ` RVA 0x34B234A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` switch type : 1-AC/AC, 2-AC/ATOM, 3-AC/L2TP, 4-AC/VFI, 5-VFI/AToM, 6-VFI/L2TP, 7-All；` unsigned_number ` segment class type : 1-SSS, 2-HW, 3-ALL。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-53f05257c23695ba](../../evidence/parameters-sets-007.md#p-53f05257c23695ba) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-053099

```text
(config)# default do-exec test ssm segment lock <number:1..4294967295> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` segment id。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-921027c1fa5afe65](../../evidence/parameters-sets-011.md#p-921027c1fa5afe65) · [状态效果 S-664bda3f875e0e13](../../evidence/state_effects-sets-022.md#s-664bda3f875e0e13)

### path-057244

```text
(config)# default do-exec test ssm segment support enable <number:1..41> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` segment type value。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-35adb604690ed821](../../evidence/parameters-sets-005.md#p-35adb604690ed821) · [状态效果 S-6f0e988fcdd9147d](../../evidence/state_effects-sets-024.md#s-6f0e988fcdd9147d)

### path-059137

```text
(config)# default do-exec test subscriber feature accounting accuracy throttling print <cr>
```

Handler ` RVA 0x1093B5A0 `；selector ` 0 `；EOL ` RVA 0x34C06558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-283bf674c2bb85f0](../../evidence/conditions-sets-016.md#c-283bf674c2bb85f0) · [状态效果 S-546414e8041bc4e6](../../evidence/state_effects-sets-018.md#s-546414e8041bc4e6)

### path-057334

```text
(config)# default do-exec test subscriber feature timer acceleration enable <cr>
```

Handler ` RVA 0x1093F020 `；selector ` 0 `；EOL ` RVA 0x34C06130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4655ff8d3efa5834](../../evidence/conditions-sets-027.md#c-4655ff8d3efa5834) · [状态效果 S-7e6d238d6591cb8d](../../evidence/state_effects-sets-027.md#s-7e6d238d6591cb8d)

### path-057525

```text
(config)# default do-exec test subscriber policy account-logon session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-65fb485e87c94d63](../../evidence/conditions-sets-039.md#c-65fb485e87c94d63) · [参数 P-a89542a0c784be09](../../evidence/parameters-sets-013.md#p-a89542a0c784be09) · [状态效果 S-edcc73cc74bd9056](../../evidence/state_effects-sets-050.md#s-edcc73cc74bd9056)

### path-057383

```text
(config)# default do-exec test subscriber policy condition-map <string> <string> <cr>
```

Handler ` RVA 0x10A59C40 `；selector ` 0 `；EOL ` RVA 0x34C749F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` The condition map to be tested for equality；` string ` The condition map to be used as the identifier source。

[条件 C-a5f24b6bf4def107](../../evidence/conditions-sets-064.md#c-a5f24b6bf4def107) · [参数 P-10987eb1655aac27](../../evidence/parameters-sets-002.md#p-10987eb1655aac27) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045924

```text
(config)# default do-exec test subscriber policy dummy <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-234568e1f8b26a9a](../../evidence/conditions-sets-014.md#c-234568e1f8b26a9a) · [状态效果 S-00a2ba530681b508](../../evidence/state_effects-sets-001.md#s-00a2ba530681b508)

### path-060217

```text
(config)# default do-exec test subscriber policy epd accounting-req start session-guid <string> epd-flow-id <number:0..32> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE8A740 `；selector ` 0 `；EOL ` RVA 0x34C53288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Enter ISG Session GUID；` unsigned_number ` Enter EPD Flow Id；` address ` Enter EPD Device IP Address。

[条件 C-19aa69e77a2dedba](../../evidence/conditions-sets-010.md#c-19aa69e77a2dedba) · [参数 P-c12bb31bafc45042](../../evidence/parameters-sets-015.md#p-c12bb31bafc45042) · [状态效果 S-493606f4c69e7fdb](../../evidence/state_effects-sets-016.md#s-493606f4c69e7fdb)

### path-060232

```text
(config)# default do-exec test subscriber policy epd conn_mgmt-query version <string> command <string> peer-ip <address> keepalive <number:0..3600> <cr>
```

Handler ` RVA 0xFE89ED0 `；selector ` 0 `；EOL ` RVA 0x34C54440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Version string, only "1.0" is valid；` string ` Command string (establish, disestablish, keepalive)；` address ` IP address of the peer；` unsigned_number ` keepalive value(0 not to send)。

[条件 C-e6c55dbbd090fba6](../../evidence/conditions-sets-089.md#c-e6c55dbbd090fba6) · [参数 P-528cd97ddb37152d](../../evidence/parameters-sets-007.md#p-528cd97ddb37152d) · [状态效果 S-5a694c8cce9b40a1](../../evidence/state_effects-sets-019.md#s-5a694c8cce9b40a1)

### path-059783

```text
(config)# default do-exec test subscriber policy epd conn_mgmt-ses-test <number:1..2> <number:0..30> <string> <cr>
```

Handler ` RVA 0xFE89E20 `；selector ` 0 `；EOL ` RVA 0x34C547F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` 1 - to add, 2 to remove；` unsigned_number ` conn id ；` string ` session guid string  。

[条件 C-5626498617550105](../../evidence/conditions-sets-034.md#c-5626498617550105) · [参数 P-2f90b406a6098bc7](../../evidence/parameters-sets-004.md#p-2f90b406a6098bc7) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060162

```text
(config)# default do-exec test subscriber policy epd handler coa-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F1A0 `；selector ` 0 `；EOL ` RVA 0x34C537B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-74b1d4d21e4c1926](../../evidence/conditions-sets-045.md#c-74b1d4d21e4c1926) · [参数 P-69204721b34e1501](../../evidence/parameters-sets-008.md#p-69204721b34e1501) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060164

```text
(config)# default do-exec test subscriber policy epd handler disconnect-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F290 `；selector ` 0 `；EOL ` RVA 0x34C53B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-a51bb04b9f29e63a](../../evidence/conditions-sets-064.md#c-a51bb04b9f29e63a) · [参数 P-c47ed38e510f496d](../../evidence/parameters-sets-015.md#p-c47ed38e510f496d) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057517

```text
(config)# default do-exec test subscriber policy epd handler stop <cr>
```

Handler ` RVA 0xFE7ECD0 `；selector ` 0 `；EOL ` RVA 0x34C53E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c420e74db5cd33f9](../../evidence/conditions-sets-076.md#c-c420e74db5cd33f9) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059770

```text
(config)# default do-exec test subscriber policy epd session-mgmt-req activate-policy-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A1B0 `；selector ` 0 `；EOL ` RVA 0x34C52850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-19b0749adcf714d2](../../evidence/conditions-sets-010.md#c-19b0749adcf714d2) · [参数 P-ef7400e9df8d5866](../../evidence/parameters-sets-018.md#p-ef7400e9df8d5866) · [状态效果 S-603d6dfd330649a0](../../evidence/state_effects-sets-021.md#s-603d6dfd330649a0)

### path-060026

```text
(config)# default do-exec test subscriber policy epd session-query-req session-ipaddress <address> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE89C40 `；selector ` 0 `；EOL ` RVA 0x34C52328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Enter ISG Session IP Address；` address ` Enter EPD Device IP Address。

[条件 C-f1b1a69095e7b731](../../evidence/conditions-sets-093.md#c-f1b1a69095e7b731) · [参数 P-995339be86ea8070](../../evidence/parameters-sets-012.md#p-995339be86ea8070) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059157

```text
(config)# default do-exec test subscriber policy epd session-terminate-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A610 `；selector ` 0 `；EOL ` RVA 0x34C52DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-e42c8ad1a3bf92cd](../../evidence/conditions-sets-088.md#c-e42c8ad1a3bf92cd) · [参数 P-bfaf933945c5acf1](../../evidence/parameters-sets-015.md#p-bfaf933945c5acf1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057611

```text
(config)# default do-exec test subscriber policy insert circuit-id <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C575A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Circuit Id to be inserted for testing, enter "none" to disable。

[条件 C-fb772603616821d0](../../evidence/conditions-sets-097.md#c-fb772603616821d0) · [参数 P-01f789955e639dbf](../../evidence/parameters-sets-001.md#p-01f789955e639dbf) · [状态效果 S-50a2a73bef7a14e2](../../evidence/state_effects-sets-018.md#s-50a2a73bef7a14e2)

### path-057465

```text
(config)# default do-exec test subscriber policy mlplink-added session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` MLP link Subscriber Service Switch session id value。

[条件 C-9dea6c906dca9065](../../evidence/conditions-sets-061.md#c-9dea6c906dca9065) · [参数 P-eca3557bd67d1f82](../../evidence/parameters-sets-018.md#p-eca3557bd67d1f82) · [状态效果 S-73348f9c1670c587](../../evidence/state_effects-sets-024.md#s-73348f9c1670c587)

### path-060160

```text
(config)# default do-exec test subscriber policy policy-client session <number:0..4294967295> client Radius-Proxy event start <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C550E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-7b65c8e91fa58e16](../../evidence/conditions-sets-048.md#c-7b65c8e91fa58e16) · [参数 P-43db9ec51cad8b99](../../evidence/parameters-sets-006.md#p-43db9ec51cad8b99) · [状态效果 S-74886a9de1579ad1](../../evidence/state_effects-sets-025.md#s-74886a9de1579ad1)

### path-057588

```text
(config)# default do-exec test subscriber policy send-session-log session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-135a150050e616ea](../../evidence/conditions-sets-008.md#c-135a150050e616ea) · [参数 P-2db34b641405b555](../../evidence/parameters-sets-004.md#p-2db34b641405b555) · [状态效果 S-a67260e39f61b7d1](../../evidence/state_effects-sets-035.md#s-a67260e39f61b7d1)

### path-053287

```text
(config)# default do-exec test subscriber policy service-profile-download <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C54BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` service profile key name。

[条件 C-c2801c7c26902304](../../evidence/conditions-sets-075.md#c-c2801c7c26902304) · [参数 P-6e2772433acac708](../../evidence/parameters-sets-009.md#p-6e2772433acac708) · [状态效果 S-5d844dc23bcf05c4](../../evidence/state_effects-sets-020.md#s-5d844dc23bcf05c4)

### path-059793

```text
(config)# default do-exec test subscriber policy service-start session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-a0ad4d43cf0cf1b8](../../evidence/conditions-sets-062.md#c-a0ad4d43cf0cf1b8) · [参数 P-9a05bf3f9bba2324](../../evidence/parameters-sets-012.md#p-9a05bf3f9bba2324) · [状态效果 S-1461fc4e58104c1e](../../evidence/state_effects-sets-005.md#s-1461fc4e58104c1e)

### path-059791

```text
(config)# default do-exec test subscriber policy service-stop session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-fb4246fffc93af2d](../../evidence/conditions-sets-097.md#c-fb4246fffc93af2d) · [参数 P-51e8af1a53cec40c](../../evidence/parameters-sets-007.md#p-51e8af1a53cec40c) · [状态效果 S-acb045f49cc45df7](../../evidence/state_effects-sets-037.md#s-acb045f49cc45df7)

### path-057502

```text
(config)# default do-exec test subscriber policy session-deactivated session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-fd4c0db705194bf5](../../evidence/conditions-sets-098.md#c-fd4c0db705194bf5) · [参数 P-806442e5184ce743](../../evidence/parameters-sets-010.md#p-806442e5184ce743) · [状态效果 S-ade5d584b679a363](../../evidence/state_effects-sets-037.md#s-ade5d584b679a363)

### path-045976

```text
(config)# default do-exec test subscriber policy tcsession-req <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9844943ad3ba4816](../../evidence/conditions-sets-059.md#c-9844943ad3ba4816) · [状态效果 S-5035785bf3f8c702](../../evidence/state_effects-sets-018.md#s-5035785bf3f8c702)

### path-059803

```text
(config)# default do-exec test subscriber policy update session <number:0..4294967295> attr-list <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` AAA attribute list name。

[条件 C-9315976898b97646](../../evidence/conditions-sets-057.md#c-9315976898b97646) · [参数 P-2dc1c4b05030fe7a](../../evidence/parameters-sets-004.md#p-2dc1c4b05030fe7a) · [状态效果 S-e402acd5bd2073ea](../../evidence/state_effects-sets-048.md#s-e402acd5bd2073ea)

### path-045834

```text
(config)# default do-exec test sw-vlan show data <cr>
```

Handler ` RVA 0x15C8E860 `；selector ` 0 `；EOL ` RVA 0x35DFE5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-19d6abbf3e222af0](../../evidence/conditions-sets-010.md#c-19d6abbf3e222af0) · [状态效果 S-0ae84ef39756d39f](../../evidence/state_effects-sets-003.md#s-0ae84ef39756d39f)

### path-047356

```text
(config)# default do-exec test system secure db <cr>
```

Handler ` RVA 0xE031AB0 `；selector ` 0 `；EOL ` RVA 0x3416FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-24afc98ec552b9d7](../../evidence/state_effects-sets-008.md#s-24afc98ec552b9d7)

### path-030226

```text
(config)# default do-exec test tcp delay <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 2 `；EOL ` RVA 0x33CF79B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` number。

[条件 C-397b2eadc1c9d97a](../../evidence/conditions-sets-022.md#c-397b2eadc1c9d97a) · [参数 P-dbbc7c51a2581030](../../evidence/parameters-sets-017.md#p-dbbc7c51a2581030) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-030186

```text
(config)# default do-exec test tcp drop <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 1 `；EOL ` RVA 0x33CF7978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` number。

[条件 C-7785e56df8dc792f](../../evidence/conditions-sets-046.md#c-7785e56df8dc792f) · [参数 P-9905a3044e6cc7c3](../../evidence/parameters-sets-012.md#p-9905a3044e6cc7c3) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-030270

```text
(config)# default do-exec test tcp line <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 0 `；EOL ` RVA 0x33CF7C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` number。

[条件 C-c91eaf6135760655](../../evidence/conditions-sets-077.md#c-c91eaf6135760655) · [参数 P-168d315b78b62806](../../evidence/parameters-sets-002.md#p-168d315b78b62806) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-030302

```text
(config)# default do-exec test tcp random <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 3 `；EOL ` RVA 0x33CF7EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` number。

[条件 C-d6b8fc13d6ae7f81](../../evidence/conditions-sets-083.md#c-d6b8fc13d6ae7f81) · [参数 P-d316af619bb90043](../../evidence/parameters-sets-016.md#p-d316af619bb90043) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059350

```text
(config)# default do-exec test template scope global <string> bind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 0 `；EOL ` RVA 0x33ED94B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059355

```text
(config)# default do-exec test template scope global <string> unbind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 1 `；EOL ` RVA 0x33ED9780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060071

```text
(config)# default do-exec test template scope interface <string> bind static merge interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 2 `；EOL ` RVA 0x33ED86E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-9498fe37630ac328](../../evidence/conditions-sets-057.md#c-9498fe37630ac328) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060074

```text
(config)# default do-exec test template scope interface <string> bind static replace interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 3 `；EOL ` RVA 0x33ED89B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-9498fe37630ac328](../../evidence/conditions-sets-057.md#c-9498fe37630ac328) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059859

```text
(config)# default do-exec test template scope interface <string> unbind static interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 4 `；EOL ` RVA 0x33ED90F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-9498fe37630ac328](../../evidence/conditions-sets-057.md#c-9498fe37630ac328) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-058006

```text
(config)# default do-exec test template scope interface nvgen interface-global <cr>
```

Handler ` RVA 0xD6DAF30 `；selector ` 0 `；EOL ` RVA 0x33ED7EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-037802

```text
(config)# default do-exec test tenant-mgr disable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35849178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec2270a6067721e6](../../evidence/conditions-sets-091.md#c-ec2270a6067721e6) · [状态效果 S-919f3d975d9e6772](../../evidence/state_effects-sets-031.md#s-919f3d975d9e6772)

### path-037745

```text
(config)# default do-exec test tenant-mgr enable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35848EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ec2270a6067721e6](../../evidence/conditions-sets-091.md#c-ec2270a6067721e6) · [状态效果 S-c92afa1d26985514](../../evidence/state_effects-sets-043.md#s-c92afa1d26985514)

### path-045085

```text
(config)# default do-exec test timer-wheel process create <cr>
```

Handler ` RVA 0xD7AC900 `；selector ` 0 `；EOL ` RVA 0x33EEEF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1597b37888df441b](../../evidence/conditions-sets-009.md#c-1597b37888df441b) · [状态效果 S-732a781f6366b2d3](../../evidence/state_effects-sets-024.md#s-732a781f6366b2d3)

### path-035773

```text
(config)# default do-exec test topology clients <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 11 `；EOL ` RVA 0x33FE4560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045648

```text
(config)# default do-exec test topology create ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 1 `；EOL ` RVA 0x33FE5EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94b8dca91a9ab089](../../evidence/conditions-sets-058.md#c-94b8dca91a9ab089) · [状态效果 S-cd8534f6110e37b3](../../evidence/state_effects-sets-044.md#s-cd8534f6110e37b3)

### path-045596

```text
(config)# default do-exec test topology delete ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 7 `；EOL ` RVA 0x33FE5A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94b8dca91a9ab089](../../evidence/conditions-sets-058.md#c-94b8dca91a9ab089) · [状态效果 S-536d48f3ea3f0ac0](../../evidence/state_effects-sets-018.md#s-536d48f3ea3f0ac0)

### path-045538

```text
(config)# default do-exec test topology lookup ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 2 `；EOL ` RVA 0x33FE53D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-a7f33ec0af7b6d44](../../evidence/state_effects-sets-035.md#s-a7f33ec0af7b6d44)

### path-035990

```text
(config)# default do-exec test topology walk <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 14 `；EOL ` RVA 0x33FE4B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fcb690536ca205a0](../../evidence/conditions-sets-098.md#c-fcb690536ca205a0) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057245

```text
(config)# default do-exec test track map name <string> create <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 1 `；EOL ` RVA 0x34216BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tracked object string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057310

```text
(config)# default do-exec test track map name <string> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 5 `；EOL ` RVA 0x34217100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tracked object string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057281

```text
(config)# default do-exec test track map name <string> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 2 `；EOL ` RVA 0x34216E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tracked object string。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057307

```text
(config)# default do-exec test track map num <number:1..32767> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 4 `；EOL ` RVA 0x342176D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057271

```text
(config)# default do-exec test track map num <number:1..32767> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 3 `；EOL ` RVA 0x34217430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-052995

```text
(config)# default do-exec test track service <string> up <cr>
```

Handler ` RVA 0xE14F670 `；selector ` 0 `；EOL ` RVA 0x34216180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tracked service name。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-8b58f3bab75800c0](../../evidence/parameters-sets-011.md#p-8b58f3bab75800c0) · [状态效果 S-c77acf50a4912c2a](../../evidence/state_effects-sets-042.md#s-c77acf50a4912c2a)

### path-035677

```text
(config)# default do-exec test track white-box <cr>
```

Handler ` RVA 0xE14F7A0 `；selector ` 0 `；EOL ` RVA 0x34215DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4fd28978f6871800](../../evidence/conditions-sets-031.md#c-4fd28978f6871800) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057767

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> add <cr>
```

Handler ` RVA 0xB516500 `；selector ` 0 `；EOL ` RVA 0x33792A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-1bd963aded0ee02e](../../evidence/conditions-sets-011.md#c-1bd963aded0ee02e) · [参数 P-816d5b8c6fbe0a85](../../evidence/parameters-sets-010.md#p-816d5b8c6fbe0a85) · [状态效果 S-83b730d465741cdb](../../evidence/state_effects-sets-028.md#s-83b730d465741cdb)

### path-059820

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> add ipv4 V1 <cr>
```

Handler ` RVA 0xB513640 `；selector ` 0 `；EOL ` RVA 0x33790108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-9f301395e684c5a1](../../evidence/state_effects-sets-034.md#s-9f301395e684c5a1)

### path-057837

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> clear <cr>
```

Handler ` RVA 0xB513640 `；selector ` 6 `；EOL ` RVA 0x337916D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-9a40061ad2667b04](../../evidence/state_effects-sets-033.md#s-9a40061ad2667b04)

### path-057730

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 1 `；EOL ` RVA 0x33790440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-9a40061ad2667b04](../../evidence/state_effects-sets-033.md#s-9a40061ad2667b04)

### path-059288

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> df-bit set <cr>
```

Handler ` RVA 0xB513640 `；selector ` 5 `；EOL ` RVA 0x33791448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-9a40061ad2667b04](../../evidence/state_effects-sets-033.md#s-9a40061ad2667b04)

### path-059826

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB513640 `；selector ` 7 `；EOL ` RVA 0x33790AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-9a40061ad2667b04](../../evidence/state_effects-sets-033.md#s-9a40061ad2667b04)

### path-059832

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 8 `；EOL ` RVA 0x33790D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-9a40061ad2667b04](../../evidence/state_effects-sets-033.md#s-9a40061ad2667b04)

### path-059268

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB513640 `；selector ` 2 `；EOL ` RVA 0x33790750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-e6be5b1d139a5d51](../../evidence/conditions-sets-089.md#c-e6be5b1d139a5d51) · [参数 P-de0e272fb87adafa](../../evidence/parameters-sets-017.md#p-de0e272fb87adafa) · [状态效果 S-9a40061ad2667b04](../../evidence/state_effects-sets-033.md#s-9a40061ad2667b04)

### path-057733

```text
(config)# default do-exec test tunnel Groups wccp <number:0..9> unsource <cr>
```

Handler ` RVA 0xB514190 `；selector ` 0 `；EOL ` RVA 0x33792060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-c2b7d57abb0f4b71](../../evidence/conditions-sets-075.md#c-c2b7d57abb0f4b71) · [参数 P-ccb3e85e97e2dec4](../../evidence/parameters-sets-016.md#p-ccb3e85e97e2dec4) · [状态效果 S-46fefaa677e8e263](../../evidence/state_effects-sets-016.md#s-46fefaa677e8e263)

### path-046174

```text
(config)# default do-exec test tunnel tos enable <cr>
```

Handler ` RVA 0xFB8F9A0 `；selector ` 0 `；EOL ` RVA 0x34830B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [状态效果 S-f365d99af10e07d9](../../evidence/state_effects-sets-051.md#s-f365d99af10e07d9)

### path-059814

```text
(config)# default do-exec test tunnel tun-to <number:0..9> add transport ipv4 none <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 1 `；EOL ` RVA 0x33794348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-258c15a8ca3df44c](../../evidence/conditions-sets-015.md#c-258c15a8ca3df44c) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-931ffdaa82e85271](../../evidence/state_effects-sets-031.md#s-931ffdaa82e85271)

### path-053775

```text
(config)# default do-exec test tunnel tun-to <number:0..9> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 2 `；EOL ` RVA 0x33794638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057805

```text
(config)# default do-exec test tunnel tun-to <number:0..9> display <number:0..160> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 7 `；EOL ` RVA 0x337968F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` unsigned_number ` Indent。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-c32407e8d350360d](../../evidence/parameters-sets-015.md#p-c32407e8d350360d) · [状态效果 S-7f8e7f61fc7437e8](../../evidence/state_effects-sets-027.md#s-7f8e7f61fc7437e8)

### path-059258

```text
(config)# default do-exec test tunnel tun-to <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 13 `；EOL ` RVA 0x33795110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059271

```text
(config)# default do-exec test tunnel tun-to <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 14 `；EOL ` RVA 0x337953B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-059280

```text
(config)# default do-exec test tunnel tun-to <number:0..9> feature enable post-encap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 9 `；EOL ` RVA 0x33796C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-f63824b3dd74110b](../../evidence/state_effects-sets-052.md#s-f63824b3dd74110b)

### path-059289

```text
(config)# default do-exec test tunnel tun-to <number:0..9> feature enable pre-decap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 10 `；EOL ` RVA 0x33796EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-f63824b3dd74110b](../../evidence/state_effects-sets-052.md#s-f63824b3dd74110b)

### path-059264

```text
(config)# default do-exec test tunnel tun-to <number:0..9> gre key disable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 8 `；EOL ` RVA 0x33796538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-62f399fdf264725f](../../evidence/state_effects-sets-021.md#s-62f399fdf264725f)

### path-059251

```text
(config)# default do-exec test tunnel tun-to <number:0..9> payload ipv4 enable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 11 `；EOL ` RVA 0x33795DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-3e74c4e5aa3d4c6a](../../evidence/conditions-sets-024.md#c-3e74c4e5aa3d4c6a) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-e8c84b047ec17ea4](../../evidence/state_effects-sets-049.md#s-e8c84b047ec17ea4)

### path-059822

```text
(config)# default do-exec test tunnel tun-to <number:0..9> payload ipv4 mtu default <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 12 `；EOL ` RVA 0x337960C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-3e74c4e5aa3d4c6a](../../evidence/conditions-sets-024.md#c-3e74c4e5aa3d4c6a) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-e8425d4d836e00fc](../../evidence/state_effects-sets-049.md#s-e8425d4d836e00fc)

### path-057657

```text
(config)# default do-exec test tunnel tun-to <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 3 `；EOL ` RVA 0x33794948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-cad5a7fea59f4cc9](../../evidence/conditions-sets-078.md#c-cad5a7fea59f4cc9) · [参数 P-b5fd48203094e8df](../../evidence/parameters-sets-014.md#p-b5fd48203094e8df) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-040036

```text
(config)# default do-exec test uninstall <string> <cr>
```

Handler ` RVA 0x15A6CC70 `；selector ` 0 `；EOL ` RVA 0x35DE37F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-8e5bac707605508a](../../evidence/conditions-sets-055.md#c-8e5bac707605508a) · [参数 P-7b9316c0493b1273](../../evidence/parameters-sets-010.md#p-7b9316c0493b1273) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057228

```text
(config)# default do-exec test vrrs client add <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 9 `；EOL ` RVA 0x342A0CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-c1faf0a01590e7c1](../../evidence/parameters-sets-015.md#p-c1faf0a01590e7c1) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-053060

```text
(config)# default do-exec test vrrs client register <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 11 `；EOL ` RVA 0x342A0678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-dfe2be5a59cb5d99](../../evidence/parameters-sets-017.md#p-dfe2be5a59cb5d99) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-057248

```text
(config)# default do-exec test vrrs client remove <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 8 `；EOL ` RVA 0x342A0FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-912dcfafa5af0bac](../../evidence/parameters-sets-011.md#p-912dcfafa5af0bac) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-052997

```text
(config)# default do-exec test vrrs client unregister <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 10 `；EOL ` RVA 0x342A0988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-e7f6bd64325acaf4](../../evidence/parameters-sets-017.md#p-e7f6bd64325acaf4) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-057418

```text
(config)# default do-exec test vrrs pathway name <string> disconnect <cr>
```

Handler ` RVA 0x133F9580 `；selector ` 0 `；EOL ` RVA 0x35A8B960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the VRRS tag associated with pathways。

[条件 C-966f3f4db04d8f90](../../evidence/conditions-sets-058.md#c-966f3f4db04d8f90) · [参数 P-b55499403f5cacac](../../evidence/parameters-sets-014.md#p-b55499403f5cacac) · [状态效果 S-ed54546f0912c22d](../../evidence/state_effects-sets-050.md#s-ed54546f0912c22d)

### path-044004

```text
(config)# default do-exec test vrrs plugin server <cr>
```

Handler ` RVA 0xE2FF4F0 `；selector ` 0 `；EOL ` RVA 0x342A69C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1827a8e6f0d8dd8c](../../evidence/conditions-sets-009.md#c-1827a8e6f0d8dd8c) · [状态效果 S-cdd2f787845d6893](../../evidence/state_effects-sets-044.md#s-cdd2f787845d6893)

### path-059125

```text
(config)# default do-exec test vrrs server add <string> vip <address> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 7 `；EOL ` RVA 0x342A15D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` group name string；` address ` VRRP group's virtual address。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-1c35fd9c9703b522](../../evidence/parameters-sets-003.md#p-1c35fd9c9703b522) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-053074

```text
(config)# default do-exec test vrrs server delete <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 5 `；EOL ` RVA 0x342A1F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-3c862bfbe3046baa](../../evidence/parameters-sets-005.md#p-3c862bfbe3046baa) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-053227

```text
(config)# default do-exec test vrrs server update <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 6 `；EOL ` RVA 0x342A1BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` group name string。

[条件 C-f63c794e08a3aa53](../../evidence/conditions-sets-095.md#c-f63c794e08a3aa53) · [参数 P-6c0f2e263c8af654](../../evidence/parameters-sets-009.md#p-6c0f2e263c8af654) · [状态效果 S-f7de19749a09e7fc](../../evidence/state_effects-sets-052.md#s-f7de19749a09e7fc)

### path-057461

```text
(config)# default do-exec test wccp ip web-cache assignment hash <cr>
```

Handler ` RVA 0x10AE0FA0 `；selector ` 0 `；EOL ` RVA 0x34CA15E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-00a73cc4271e7434](../../evidence/conditions-sets-001.md#c-00a73cc4271e7434) · [状态效果 S-8cbca1fa25ddedc6](../../evidence/state_effects-sets-030.md#s-8cbca1fa25ddedc6)

### path-053513

```text
(config)# default do-exec test wccp ip web-cache capabilities <cr>
```

Handler ` RVA 0x10AE0C00 `；selector ` 0 `；EOL ` RVA 0x34CA11B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eebebb687cfef849](../../evidence/conditions-sets-092.md#c-eebebb687cfef849) · [状态效果 S-544b08bcfb3afbf9](../../evidence/state_effects-sets-018.md#s-544b08bcfb3afbf9)

### path-059767

```text
(config)# default do-exec test wccp ip web-cache service <number:0..255> <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10AE0A90 `；selector ` 0 `；EOL ` RVA 0x34CA1C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` WCCP service priority；` unsigned_number ` WCCP service protocol；` unsigned_number ` WCCP service flags。

[条件 C-84c16de96cd6cea1](../../evidence/conditions-sets-051.md#c-84c16de96cd6cea1) · [参数 P-71b77f6b738f2f59](../../evidence/parameters-sets-009.md#p-71b77f6b738f2f59) · [状态效果 S-544b08bcfb3afbf9](../../evidence/state_effects-sets-018.md#s-544b08bcfb3afbf9)

### path-039451

```text
(config)# default do-exec test wsma history <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 1 `；EOL ` RVA 0x3463D0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048527

```text
(config)# default do-exec test wsma listener <string> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 2 `；EOL ` RVA 0x3463D6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Specify the transport。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-9f474f72af6c782b](../../evidence/parameters-sets-012.md#p-9f474f72af6c782b) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-048585

```text
(config)# default do-exec test wsma max-priv-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 4 `；EOL ` RVA 0x3463D960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enforce max priv or not。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [参数 P-d3faea102e025dae](../../evidence/parameters-sets-016.md#p-d3faea102e025dae) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-039505

```text
(config)# default do-exec test wsma summary <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 3 `；EOL ` RVA 0x3463D390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-045388

```text
(config)# default do-exec test x25 dbit <number:0..1000> <cr>
```

Handler ` RVA 0x1061D5B0 `；selector ` 0 `；EOL ` RVA 0x34BD4DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` D-bit interval (packets)。

[条件 C-4c469b247959c3aa](../../evidence/conditions-sets-030.md#c-4c469b247959c3aa) · [参数 P-f4144dc0d3cc9c91](../../evidence/parameters-sets-018.md#p-f4144dc0d3cc9c91) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046379

```text
(config)# default do-exec test xdr create-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7830 `；selector ` 0 `；EOL ` RVA 0x34CFDE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` ID of test stream to create。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-d155c8fe88eef6d1](../../evidence/parameters-sets-016.md#p-d155c8fe88eef6d1) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046320

```text
(config)# default do-exec test xdr destroy-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7890 `；selector ` 0 `；EOL ` RVA 0x34CFDB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` ID of test stream to destroy。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-c2413738ef352aaf](../../evidence/parameters-sets-015.md#p-c2413738ef352aaf) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036586

```text
(config)# default do-exec test xdr disable <cr>
```

Handler ` RVA 0x10C75EA0 `；selector ` 0 `；EOL ` RVA 0x34CF46D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fd1bed760fb9c021](../../evidence/conditions-sets-098.md#c-fd1bed760fb9c021) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-036587

```text
(config)# default do-exec test xdr enable <cr>
```

Handler ` RVA 0x10C75E20 `；selector ` 0 `；EOL ` RVA 0x34CF4988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-12dd95f8ed5d6c5f](../../evidence/conditions-sets-007.md#c-12dd95f8ed5d6c5f) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057827

```text
(config)# default do-exec test xdr fragment <number:1..1000000> to_slots High-queue <cr>
```

Handler ` RVA 0x10CA78F0 `；selector ` 0 `；EOL ` RVA 0x34CFEF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` fragment size (in Bytes)。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-7258ec243930115d](../../evidence/parameters-sets-009.md#p-7258ec243930115d) · [状态效果 S-43480ce1247963da](../../evidence/state_effects-sets-015.md#s-43480ce1247963da)

### path-057601

```text
(config)# default do-exec test xdr ping to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA7E20 `；selector ` 0 `；EOL ` RVA 0x34CFD028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-b75cb2e4c5728f3a](../../evidence/parameters-sets-014.md#p-b75cb2e4c5728f3a) · [状态效果 S-4395a729ba5f0eef](../../evidence/state_effects-sets-015.md#s-4395a729ba5f0eef)

### path-046484

```text
(config)# default do-exec test xdr push start <cr>
```

Handler ` RVA 0x10CA7B40 `；selector ` 0 `；EOL ` RVA 0x34CFE3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-060172

```text
(config)# default do-exec test xdr push stream <number:1..20> count <number:0..200000> to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA75D0 `；selector ` 0 `；EOL ` RVA 0x34CFE818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [参数 P-92fc2dc68416fcec](../../evidence/parameters-sets-011.md#p-92fc2dc68416fcec) · [状态效果 S-a5cd18d11351421b](../../evidence/state_effects-sets-035.md#s-a5cd18d11351421b)

### path-037024

```text
(config)# default do-exec test xdr show-streams <cr>
```

Handler ` RVA 0x10CA76F0 `；selector ` 0 `；EOL ` RVA 0x34CFE0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-046279

```text
(config)# default do-exec test xdr split allow <cr>
```

Handler ` RVA 0x10CA7D50 `；selector ` 0 `；EOL ` RVA 0x34CFD7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b18c482d6446841c](../../evidence/conditions-sets-069.md#c-b18c482d6446841c) · [状态效果 S-5918848dd8dd41fd](../../evidence/state_effects-sets-019.md#s-5918848dd8dd41fd)

### path-046687

```text
(config)# default do-exec test xdr state-change IPC_START_SENDING <cr>
```

Handler ` RVA 0x10C913F0 `；selector ` 0 `；EOL ` RVA 0x34CFF320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ef3cee784612cf50](../../evidence/conditions-sets-092.md#c-ef3cee784612cf50) · [状态效果 S-653095cfa5c3f85a](../../evidence/state_effects-sets-022.md#s-653095cfa5c3f85a)

### path-059804

```text
(config)# default do-exec test xdr statistics client test-stats-1 create <number:1..1000000> <number:1..6000> <cr>
```

Handler ` RVA 0xB315AB0 `；selector ` 0 `；EOL ` RVA 0x33737890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Num counters for this client；` unsigned_number ` Update interval for this client (s)。

[条件 C-1e4face58ff1c1c7](../../evidence/conditions-sets-012.md#c-1e4face58ff1c1c7) · [参数 P-022205fef7e7929e](../../evidence/parameters-sets-001.md#p-022205fef7e7929e) · [状态效果 S-21e78549fe12ae12](../../evidence/state_effects-sets-008.md#s-21e78549fe12ae12)

### path-057674

```text
(config)# default do-exec test xdr statistics client test-stats-1 req-stats <cr>
```

Handler ` RVA 0xB2B2B70 `；selector ` 0 `；EOL ` RVA 0x3372F4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9b6c9b0a0770911](../../evidence/conditions-sets-090.md#c-e9b6c9b0a0770911) · [状态效果 S-06a6eae8f66e88a7](../../evidence/state_effects-sets-002.md#s-06a6eae8f66e88a7)

### path-057710

```text
(config)# default do-exec test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB3157E0 `；selector ` 0 `；EOL ` RVA 0x33737E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1e4face58ff1c1c7](../../evidence/conditions-sets-012.md#c-1e4face58ff1c1c7) · [状态效果 S-2c5669b3bd92cecf](../../evidence/state_effects-sets-010.md#s-2c5669b3bd92cecf)

### path-057742

```text
(config)# default do-exec test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB2B2770 `；selector ` 0 `；EOL ` RVA 0x3372FCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9b6c9b0a0770911](../../evidence/conditions-sets-090.md#c-e9b6c9b0a0770911) · [状态效果 S-05be62f7e0213c05](../../evidence/state_effects-sets-002.md#s-05be62f7e0213c05)

### path-053795

```text
(config)# default do-exec test xdr statistics selftest <number:0..64> <cr>
```

Handler ` RVA 0xB2B3280 `；selector ` 0 `；EOL ` RVA 0x33730148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` slot_id。

[条件 C-f7aef6601c77bc03](../../evidence/conditions-sets-096.md#c-f7aef6601c77bc03) · [参数 P-a26de8620aef734b](../../evidence/parameters-sets-012.md#p-a26de8620aef734b) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-031747

```text
(config)# default do-exec test xtf-policy-shim <cr>
```

Handler ` RVA 0x128866D0 `；selector ` 0 `；EOL ` RVA 0x358F6488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-399221088f6c6de6](../../evidence/conditions-sets-022.md#c-399221088f6c6de6) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-026693

```text
(config)# default do-exec traceroute <cr>
```

Handler ` RVA 0xE00FAA0 `；selector ` 0 `；EOL ` RVA 0x3415C008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d2d51f748f49cf43](../../evidence/conditions-sets-081.md#c-d2d51f748f49cf43) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-057054

```text
(config)# default do-exec traceroute ethernet <address> domain <string> port <cr>
```

Handler ` RVA 0xBD664C0 `；selector ` 0 `；EOL ` RVA 0x338E2680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Remote Maintenance Point MAC Address；` string ` maintenance domain name。

[条件 C-ea9bd3859077cfe4](../../evidence/conditions-sets-091.md#c-ea9bd3859077cfe4) · [参数 P-938128e39050e564](../../evidence/parameters-sets-011.md#p-938128e39050e564) · [状态效果 S-6593c38db8508e10](../../evidence/state_effects-sets-022.md#s-6593c38db8508e10)

### path-027833

```text
(config)# default do-exec trigger <string> <cr>
```

Handler ` RVA 0xDF79070 `；selector ` 0 `；EOL ` RVA 0x340B8D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trigger identifier for the trigger to be created or executed。

[条件 C-ca1ed1bb35931af0](../../evidence/conditions-sets-078.md#c-ca1ed1bb35931af0) · [参数 P-8105354b13a9d4eb](../../evidence/parameters-sets-010.md#p-8105354b13a9d4eb) · [状态效果 S-9a2a814ab02c374e](../../evidence/state_effects-sets-033.md#s-9a2a814ab02c374e)

### path-029078

```text
(config)# default do-exec tunnel <string> <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33D2A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Address or hostname of a remote system。

[条件 C-1dfed2db29fc3190](../../evidence/conditions-sets-012.md#c-1dfed2db29fc3190) · [参数 P-4279d2faf8428569](../../evidence/parameters-sets-006.md#p-4279d2faf8428569) · [状态效果 S-349b1e2258a1d20f](../../evidence/state_effects-sets-012.md#s-349b1e2258a1d20f)

### path-034557

```text
(config)# default do-exec undebug ACM all <cr>
```

Handler ` RVA 0xDEDBDB0 `；selector ` 0 `；EOL ` RVA 0x34096D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-0b52d47af7a0f0f6](../../evidence/state_effects-sets-003.md#s-0b52d47af7a0f0f6)

### path-034472

```text
(config)# default do-exec undebug ACM error <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 1 `；EOL ` RVA 0x340967E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-0b52d47af7a0f0f6](../../evidence/state_effects-sets-003.md#s-0b52d47af7a0f0f6)

### path-034523

```text
(config)# default do-exec undebug ACM event <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 0 `；EOL ` RVA 0x34096A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-0b52d47af7a0f0f6](../../evidence/state_effects-sets-003.md#s-0b52d47af7a0f0f6)

### path-042173

```text
(config)# default do-exec undebug LDAP all <cr>
```

Handler ` RVA 0x11AC30E0 `；selector ` 0 `；EOL ` RVA 0x3560CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-36ea7b9a8d187008](../../evidence/state_effects-sets-012.md#s-36ea7b9a8d187008)

### path-042111

```text
(config)# default do-exec undebug LDAP error <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 1 `；EOL ` RVA 0x3560C2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-36ea7b9a8d187008](../../evidence/state_effects-sets-012.md#s-36ea7b9a8d187008)

### path-042132

```text
(config)# default do-exec undebug LDAP event <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 0 `；EOL ` RVA 0x3560C568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-36ea7b9a8d187008](../../evidence/state_effects-sets-012.md#s-36ea7b9a8d187008)

### path-042153

```text
(config)# default do-exec undebug LDAP legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3560C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-36ea7b9a8d187008](../../evidence/state_effects-sets-012.md#s-36ea7b9a8d187008)

### path-042087

```text
(config)# default do-exec undebug LDAP packet <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 2 `；EOL ` RVA 0x3560C018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-096d11ed63a2ea43](../../evidence/conditions-sets-004.md#c-096d11ed63a2ea43) · [状态效果 S-36ea7b9a8d187008](../../evidence/state_effects-sets-012.md#s-36ea7b9a8d187008)

### path-035213

```text
(config)# default do-exec undebug aaa accounting <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 16 `；EOL ` RVA 0x341B80C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035262

```text
(config)# default do-exec undebug aaa administrative <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 17 `；EOL ` RVA 0x341B8368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036501

```text
(config)# default do-exec undebug aaa api <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 35 `；EOL ` RVA 0x341BC6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045848

```text
(config)# default do-exec undebug aaa api attr <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 36 `；EOL ` RVA 0x341BC680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036399

```text
(config)# default do-exec undebug aaa attr <cr>
```

Handler ` RVA 0xDD3A410 `；selector ` 26 `；EOL ` RVA 0x341BB120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045628

```text
(config)# default do-exec undebug aaa attr add <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 30 `；EOL ` RVA 0x341BABA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045573

```text
(config)# default do-exec undebug aaa attr alloc-free <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 31 `；EOL ` RVA 0x341BA900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045513

```text
(config)# default do-exec undebug aaa attr error <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 32 `；EOL ` RVA 0x341BA658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045452

```text
(config)# default do-exec undebug aaa attr handle <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 27 `；EOL ` RVA 0x341BA3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045754

```text
(config)# default do-exec undebug aaa attr info <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 28 `；EOL ` RVA 0x341BB0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045687

```text
(config)# default do-exec undebug aaa attr update <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 29 `；EOL ` RVA 0x341BAE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035111

```text
(config)# default do-exec undebug aaa authentication <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 12 `；EOL ` RVA 0x341B7B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035166

```text
(config)# default do-exec undebug aaa authorization <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 15 `；EOL ` RVA 0x341B7E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035319

```text
(config)# default do-exec undebug aaa boundary <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 56 `；EOL ` RVA 0x341B8610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-044677

```text
(config)# default do-exec undebug aaa cache filterserver <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 50 `；EOL ` RVA 0x341B7040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-044733

```text
(config)# default do-exec undebug aaa cache group <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 51 `；EOL ` RVA 0x341B72E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035376

```text
(config)# default do-exec undebug aaa cca <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 57 `；EOL ` RVA 0x341B88B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035700

```text
(config)# default do-exec undebug aaa coa <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 25 `；EOL ` RVA 0x341B98A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036747

```text
(config)# default do-exec undebug aaa common-criteria <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 55 `；EOL ` RVA 0x341BD9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-305bd1d1fbc899f1](../../evidence/conditions-sets-019.md#c-305bd1d1fbc899f1) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036189

```text
(config)# default do-exec undebug aaa db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 38 `；EOL ` RVA 0x341BBB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045944

```text
(config)# default do-exec undebug aaa dead-criteria transaction <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 42 `；EOL ` RVA 0x341BD188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036789

```text
(config)# default do-exec undebug aaa green <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 69 `；EOL ` RVA 0x341BDC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89fb90ca84e0b9a0](../../evidence/conditions-sets-053.md#c-89fb90ca84e0b9a0) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036320

```text
(config)# default do-exec undebug aaa id <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 37 `；EOL ` RVA 0x341BC0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036037

```text
(config)# default do-exec undebug aaa ipc <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 33 `；EOL ` RVA 0x341BB628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035891

```text
(config)# default do-exec undebug aaa memory <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 13 `；EOL ` RVA 0x341BA0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035484

```text
(config)# default do-exec undebug aaa mlist-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 44 `；EOL ` RVA 0x341B8E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036651

```text
(config)# default do-exec undebug aaa mlist-state <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 45 `；EOL ` RVA 0x341BD6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035648

```text
(config)# default do-exec undebug aaa per-user <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 18 `；EOL ` RVA 0x341B9600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035760

```text
(config)# default do-exec undebug aaa pod <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 24 `；EOL ` RVA 0x341B9B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-044773

```text
(config)# default do-exec undebug aaa profile db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 52 `；EOL ` RVA 0x341B78E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045893

```text
(config)# default do-exec undebug aaa protocol local <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 40 `；EOL ` RVA 0x341BCBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-045955

```text
(config)# default do-exec undebug aaa protocol radius <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 41 `；EOL ` RVA 0x341BCE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035829

```text
(config)# default do-exec undebug aaa proxy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 23 `；EOL ` RVA 0x341B9DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036790

```text
(config)# default do-exec undebug aaa redundancy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 54 `；EOL ` RVA 0x341BDF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3604d86012653633](../../evidence/conditions-sets-021.md#c-3604d86012653633) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035594

```text
(config)# default do-exec undebug aaa server-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 46 `；EOL ` RVA 0x341B9358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035537

```text
(config)# default do-exec undebug aaa sg-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 47 `；EOL ` RVA 0x341B90B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-035434

```text
(config)# default do-exec undebug aaa sg-server-selection <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 48 `；EOL ` RVA 0x341B8B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-044727

```text
(config)# default do-exec undebug aaa subscriber profile <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 53 `；EOL ` RVA 0x341B75E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036116

```text
(config)# default do-exec undebug aaa subsys <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 34 `；EOL ` RVA 0x341BB8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036608

```text
(config)# default do-exec undebug aaa testing <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 43 `；EOL ` RVA 0x341BD418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-044728

```text
(config)# default do-exec undebug aaa tools memleak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x35C0DA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-12e4c40b4015e892](../../evidence/state_effects-sets-004.md#s-12e4c40b4015e892)

### path-036382

```text
(config)# default do-exec undebug aaa traceback <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 14 `；EOL ` RVA 0x341BC370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-036251

```text
(config)# default do-exec undebug aaa userdb <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 39 `；EOL ` RVA 0x341BBE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-e58363c40ff34fa9](../../evidence/state_effects-sets-049.md#s-e58363c40ff34fa9)

### path-033364

```text
(config)# default do-exec undebug access-expression <cr>
```

Handler ` RVA 0xF2A3970 `；selector ` 0 `；EOL ` RVA 0x345E4A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-0d34c453655cbfd4](../../evidence/state_effects-sets-003.md#s-0d34c453655cbfd4)

### path-042521

```text
(config)# default do-exec undebug access-session all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 4 `；EOL ` RVA 0x33BAEA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-93f380e729d32794](../../evidence/state_effects-sets-031.md#s-93f380e729d32794)

### path-042509

```text
(config)# default do-exec undebug access-session detail <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 2 `；EOL ` RVA 0x33BAE7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-93f380e729d32794](../../evidence/state_effects-sets-031.md#s-93f380e729d32794)

### path-042479

```text
(config)# default do-exec undebug access-session errors <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 0 `；EOL ` RVA 0x33BAE258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-93f380e729d32794](../../evidence/state_effects-sets-031.md#s-93f380e729d32794)

### path-042496

```text
(config)# default do-exec undebug access-session events <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 1 `；EOL ` RVA 0x33BAE500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-93f380e729d32794](../../evidence/state_effects-sets-031.md#s-93f380e729d32794)

### path-051099

```text
(config)# default do-exec undebug access-session feature all <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 5 `；EOL ` RVA 0x33BAF118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4802142fc34a1456](../../evidence/conditions-sets-028.md#c-4802142fc34a1456) · [状态效果 S-93f380e729d32794](../../evidence/state_effects-sets-031.md#s-93f380e729d32794)

### path-051222

```text
(config)# default do-exec undebug access-session rcl_server all <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 3 `；EOL ` RVA 0x33BAD888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-a275f6d98972e5e5](../../evidence/state_effects-sets-034.md#s-a275f6d98972e5e5)

### path-051216

```text
(config)# default do-exec undebug access-session rcl_server detail <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 2 `；EOL ` RVA 0x33BAD5E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-a275f6d98972e5e5](../../evidence/state_effects-sets-034.md#s-a275f6d98972e5e5)

### path-051208

```text
(config)# default do-exec undebug access-session rcl_server error <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 0 `；EOL ` RVA 0x33BAD338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-a275f6d98972e5e5](../../evidence/state_effects-sets-034.md#s-a275f6d98972e5e5)

### path-051199

```text
(config)# default do-exec undebug access-session rcl_server event <cr>
```

Handler ` RVA 0xCAF9B10 `；selector ` 1 `；EOL ` RVA 0x33BAD090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-a275f6d98972e5e5](../../evidence/state_effects-sets-034.md#s-a275f6d98972e5e5)

### path-042555

```text
(config)# default do-exec undebug access-session sync <cr>
```

Handler ` RVA 0xCAFB1B0 `；selector ` 3 `；EOL ` RVA 0x33BAED38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c36acfc192c3f5c](../../evidence/conditions-sets-005.md#c-0c36acfc192c3f5c) · [状态效果 S-93f380e729d32794](../../evidence/state_effects-sets-031.md#s-93f380e729d32794)

### path-047294

```text
(config)# default do-exec undebug acl cca error <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x3447D290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-041bca6672497185](../../evidence/state_effects-sets-001.md#s-041bca6672497185)

### path-047331

```text
(config)# default do-exec undebug acl cca event <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x3447D538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-041bca6672497185](../../evidence/state_effects-sets-001.md#s-041bca6672497185)

### path-030599

```text
(config)# default do-exec undebug adjacency <cr>
```

Handler ` RVA 0xB559CD0 `；selector ` 0 `；EOL ` RVA 0x3379B6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f773847018d57e5e](../../evidence/conditions-sets-096.md#c-f773847018d57e5e) · [状态效果 S-7dfe01d6343cb253](../../evidence/state_effects-sets-027.md#s-7dfe01d6343cb253)

### path-037441

```text
(config)# default do-exec undebug alg all <cr>
```

Handler ` RVA 0xCD3BF50 `；selector ` 1 `；EOL ` RVA 0x33CD4910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-1835e414a09d7bfa](../../evidence/state_effects-sets-006.md#s-1835e414a09d7bfa)

### path-037563

```text
(config)# default do-exec undebug alg info <cr>
```

Handler ` RVA 0xE002120 `；selector ` 2 `；EOL ` RVA 0x33CD5108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-1835e414a09d7bfa](../../evidence/state_effects-sets-006.md#s-1835e414a09d7bfa)

### path-037526

```text
(config)# default do-exec undebug alg trace <cr>
```

Handler ` RVA 0xE002120 `；selector ` 1 `；EOL ` RVA 0x33CD4E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-1835e414a09d7bfa](../../evidence/state_effects-sets-006.md#s-1835e414a09d7bfa)

### path-037478

```text
(config)# default do-exec undebug alg warn <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x33CD4BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-1835e414a09d7bfa](../../evidence/state_effects-sets-006.md#s-1835e414a09d7bfa)

### path-028138

```text
(config)# default do-exec undebug all <cr>
```

Handler ` RVA 0xE002630 `；selector ` 0 `；EOL ` RVA 0x34121818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-051601

```text
(config)# default do-exec undebug alps ascu event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 3 `；EOL ` RVA 0x3541C160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dec29db2ab391490](../../evidence/conditions-sets-086.md#c-dec29db2ab391490) · [状态效果 S-ced09f368ada6bb4](../../evidence/state_effects-sets-044.md#s-ced09f368ada6bb4)

### path-051557

```text
(config)# default do-exec undebug alps circuit event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 2 `；EOL ` RVA 0x3541BCD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-12c5397c59c6b30e](../../evidence/state_effects-sets-004.md#s-12c5397c59c6b30e)

### path-051558

```text
(config)# default do-exec undebug alps peer event <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 1 `；EOL ` RVA 0x3541B960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-2d3464a434f4db86](../../evidence/state_effects-sets-010.md#s-2d3464a434f4db86)

### path-043116

```text
(config)# default do-exec undebug alps snmp <cr>
```

Handler ` RVA 0x1121A510 `；selector ` 4 `；EOL ` RVA 0x3541C6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-041726

```text
(config)# default do-exec undebug analyze memory-leak <cr>
```

Handler ` RVA 0xE002120 `；selector ` 0 `；EOL ` RVA 0x341F0BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-57872e0efd72043a](../../evidence/conditions-sets-034.md#c-57872e0efd72043a) · [状态效果 S-1c94c1cb5eddae4c](../../evidence/state_effects-sets-007.md#s-1c94c1cb5eddae4c)

### path-036766

```text
(config)# default do-exec undebug ancp adjacency <cr>
```

Handler ` RVA 0xB258990 `；selector ` 0 `；EOL ` RVA 0x336D7DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-044a2e7014c9ffd4](../../evidence/state_effects-sets-001.md#s-044a2e7014c9ffd4)

### path-041443

```text
(config)# default do-exec undebug application db <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 7 `；EOL ` RVA 0x358DCD80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-041480

```text
(config)# default do-exec undebug application detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 2 `；EOL ` RVA 0x358DD028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-041380

```text
(config)# default do-exec undebug application event <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 5 `；EOL ` RVA 0x358DC578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-041599

```text
(config)# default do-exec undebug application ha <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 8 `；EOL ` RVA 0x358DD660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-050424

```text
(config)# default do-exec undebug application ha detail <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 9 `；EOL ` RVA 0x358DD638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-056015

```text
(config)# default do-exec undebug application route <address> <address> <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 1 `；EOL ` RVA 0x358DD378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination prefix；` address ` Destination prefix mask。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [参数 P-3fadc80999e697ce](../../evidence/parameters-sets-005.md#p-3fadc80999e697ce) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-041447

```text
(config)# default do-exec undebug application rwatch <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 3 `；EOL ` RVA 0x358DC8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-050352

```text
(config)# default do-exec undebug application rwatch rib <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 4 `；EOL ` RVA 0x358DC888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-041358

```text
(config)# default do-exec undebug application summary <cr>
```

Handler ` RVA 0x12810B70 `；selector ` 6 `；EOL ` RVA 0x358DC2D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-3637c563707761d8](../../evidence/state_effects-sets-012.md#s-3637c563707761d8)

### path-051214

```text
(config)# default do-exec undebug archive config differences <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-5c6fbdae6e69c79e](../../evidence/state_effects-sets-020.md#s-5c6fbdae6e69c79e)

### path-051229

```text
(config)# default do-exec undebug archive config ha <cr>
```

Handler ` RVA 0xDEDE750 `；selector ` 1 `；EOL ` RVA 0x3409D5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f676b5924dded8ec](../../evidence/conditions-sets-095.md#c-f676b5924dded8ec) · [状态效果 S-8eec57c72be5010f](../../evidence/state_effects-sets-030.md#s-8eec57c72be5010f)
