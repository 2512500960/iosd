# lw-vlan-range · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009755

```text
(config-if-vlan-range)# default exit-vlan-config <cr>
```

Handler ` RVA 0x11D3AE30 `；selector ` 0 `；EOL ` RVA 0x356D45F8 `。

模式根 ` RVA 0x356D3600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-15be3351a2bfb6c6](../../evidence/state_effects-sets-005.md#s-15be3351a2bfb6c6)

### observed_connections-009757

```text
(config-if-vlan-range)# default pppoe enable <cr>
```

Handler ` RVA 0x11C6D030 `；selector ` 0 `；EOL ` RVA 0x356B7130 `。

模式根 ` RVA 0x356D3600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-039f5f7e0becccbf](../../evidence/conditions-sets-002.md#c-039f5f7e0becccbf) · [状态效果 S-15be3351a2bfb6c6](../../evidence/state_effects-sets-005.md#s-15be3351a2bfb6c6)

### observed_connections-009753

```text
(config-if-vlan-range)# exit-vlan-config <cr>
```

Handler ` RVA 0x11D3AE30 `；selector ` 0 `；EOL ` RVA 0x356D45F8 `。

模式根 ` RVA 0x356D3600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009754

```text
(config-if-vlan-range)# no exit-vlan-config <cr>
```

Handler ` RVA 0x11D3AE30 `；selector ` 0 `；EOL ` RVA 0x356D45F8 `。

模式根 ` RVA 0x356D3600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-f9dbad11568e97c5](../../evidence/state_effects-sets-053.md#s-f9dbad11568e97c5)

### observed_connections-009756

```text
(config-if-vlan-range)# no pppoe enable <cr>
```

Handler ` RVA 0x11C6D030 `；selector ` 0 `；EOL ` RVA 0x356B7130 `。

模式根 ` RVA 0x356D3600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dc1a5dd44a403068](../../evidence/conditions-sets-085.md#c-dc1a5dd44a403068) · [状态效果 S-f9dbad11568e97c5](../../evidence/state_effects-sets-053.md#s-f9dbad11568e97c5)

### observed_connections-009758

```text
(config-if-vlan-range)# pppoe enable group global <cr>
```

Handler ` RVA 0x11C6D030 `；selector ` 0 `；EOL ` RVA 0x356B7130 `。

模式根 ` RVA 0x356D3600 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1068ae3fc2f8c4bf](../../evidence/conditions-sets-007.md#c-1068ae3fc2f8c4bf) · [状态效果 S-0c0a79a3eba3967a](../../evidence/state_effects-sets-003.md#s-0c0a79a3eba3967a)
