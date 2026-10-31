# evpn-es · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009301

```text
(config-evpn-es)# default df-election preempt-time <cr>
```

Handler ` RVA 0x12524280 `；selector ` 0 `；EOL ` RVA 0x3588ABA8 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c678eff1d959530e](../../evidence/conditions-sets-076.md#c-c678eff1d959530e) · [状态效果 S-74ff99c10e6ca134](../../evidence/state_effects-sets-025.md#s-74ff99c10e6ca134)

### observed_connections-009295

```text
(config-evpn-es)# default identifier <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588A118 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3126afc73763a2ae](../../evidence/conditions-sets-019.md#c-3126afc73763a2ae) · [状态效果 S-86ba6c35a525e917](../../evidence/state_effects-sets-029.md#s-86ba6c35a525e917)

### observed_connections-009297

```text
(config-evpn-es)# default redundancy <cr>
```

Handler ` RVA 0x12523FC0 `；selector ` 0 `；EOL ` RVA 0x3588A750 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-47a759883a39965b](../../evidence/conditions-sets-028.md#c-47a759883a39965b) · [状态效果 S-86ba6c35a525e917](../../evidence/state_effects-sets-029.md#s-86ba6c35a525e917)

### observed_connections-009293

```text
(config-evpn-es)# default system-mac <cr>
```

Handler ` RVA 0x12523560 `；selector ` 0 `；EOL ` RVA 0x35889E08 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9f65c3c6f7f3e4a9](../../evidence/conditions-sets-062.md#c-9f65c3c6f7f3e4a9) · [状态效果 S-86ba6c35a525e917](../../evidence/state_effects-sets-029.md#s-86ba6c35a525e917)

### observed_connections-009300

```text
(config-evpn-es)# df-election preempt-time <number:1..3600> <cr>
```

Handler ` RVA 0x12524280 `；selector ` 0 `；EOL ` RVA 0x3588ABA8 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of seconds to wait before advertising Ethernet Segment routes。

[条件 C-a8be4147f2757ad7](../../evidence/conditions-sets-065.md#c-a8be4147f2757ad7) · [参数 P-ab067fd4dbe5205b](../../evidence/parameters-sets-013.md#p-ab067fd4dbe5205b) · [状态效果 S-fe81a90131b24d16](../../evidence/state_effects-sets-054.md#s-fe81a90131b24d16)

### observed_connections-009290

```text
(config-evpn-es)# exit <cr>
```

Handler ` RVA 0x1251A790 `；selector ` 0 `；EOL ` RVA 0x3587C688 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f8f164a9e2429906](../../evidence/conditions-sets-096.md#c-f8f164a9e2429906)

### observed_connections-009303

```text
(config-evpn-es)# identifier type 0 <number:0..255> <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588A118 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-319ae7d96884ad0f](../../evidence/conditions-sets-019.md#c-319ae7d96884ad0f) · [缺口 G-5a21c188dca3adad](../../evidence/gaps-sets-004.md#g-5a21c188dca3adad) · [参数 P-eaa0dee151af2bb4](../../evidence/parameters-sets-018.md#p-eaa0dee151af2bb4) · [状态效果 S-f3d8b3f68d35fd16](../../evidence/state_effects-sets-052.md#s-f3d8b3f68d35fd16)

### observed_connections-009302

```text
(config-evpn-es)# identifier type 3 system-mac <address> <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588A118 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-d8eba6ef0574255f](../../evidence/conditions-sets-083.md#c-d8eba6ef0574255f) · [参数 P-8819ea4a8a1bcfe7](../../evidence/parameters-sets-011.md#p-8819ea4a8a1bcfe7) · [状态效果 S-235b82a97f161e74](../../evidence/state_effects-sets-008.md#s-235b82a97f161e74)

### observed_connections-009299

```text
(config-evpn-es)# no df-election preempt-time <cr>
```

Handler ` RVA 0x12524280 `；selector ` 0 `；EOL ` RVA 0x3588ABA8 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d66434d327a03853](../../evidence/conditions-sets-083.md#c-d66434d327a03853) · [状态效果 S-ade75167876be149](../../evidence/state_effects-sets-037.md#s-ade75167876be149)

### observed_connections-009294

```text
(config-evpn-es)# no identifier <cr>
```

Handler ` RVA 0x125239A0 `；selector ` 0 `；EOL ` RVA 0x3588A118 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-be434de612cbaafb](../../evidence/conditions-sets-073.md#c-be434de612cbaafb) · [状态效果 S-6cb16c3b4bf1e77f](../../evidence/state_effects-sets-023.md#s-6cb16c3b4bf1e77f)

### observed_connections-009296

```text
(config-evpn-es)# no redundancy <cr>
```

Handler ` RVA 0x12523FC0 `；selector ` 0 `；EOL ` RVA 0x3588A750 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8a2d747eea381c67](../../evidence/conditions-sets-053.md#c-8a2d747eea381c67) · [状态效果 S-6cb16c3b4bf1e77f](../../evidence/state_effects-sets-023.md#s-6cb16c3b4bf1e77f)

### observed_connections-009291

```text
(config-evpn-es)# no system-mac <cr>
```

Handler ` RVA 0x12523560 `；selector ` 0 `；EOL ` RVA 0x35889E08 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-73744f47d141f529](../../evidence/conditions-sets-045.md#c-73744f47d141f529) · [状态效果 S-6cb16c3b4bf1e77f](../../evidence/state_effects-sets-023.md#s-6cb16c3b4bf1e77f)

### observed_connections-009298

```text
(config-evpn-es)# redundancy all-active <cr>
```

Handler ` RVA 0x12523FC0 `；selector ` 0 `；EOL ` RVA 0x3588A750 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bcb76fb886f945af](../../evidence/conditions-sets-073.md#c-bcb76fb886f945af) · [状态效果 S-3c7920f4ed05516a](../../evidence/state_effects-sets-013.md#s-3c7920f4ed05516a)

### observed_connections-009292

```text
(config-evpn-es)# system-mac <address> <cr>
```

Handler ` RVA 0x12523560 `；selector ` 0 `；EOL ` RVA 0x35889E08 `。

模式根 ` RVA 0x3587BBA0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-4badf52b8db8033d](../../evidence/conditions-sets-030.md#c-4badf52b8db8033d) · [参数 P-0c46bfd1b7ed7e70](../../evidence/parameters-sets-001.md#p-0c46bfd1b7ed7e70)
