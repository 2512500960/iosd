# subscriber-policy · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009103

```text
(config-policy)# arp deny <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 0 `；EOL ` RVA 0x345ED358 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c35abffd5d628e03](../../evidence/conditions-sets-075.md#c-c35abffd5d628e03) · [状态效果 S-b269388802636a65](../../evidence/state_effects-sets-038.md#s-b269388802636a65)

### observed_connections-009109

```text
(config-policy)# broadcast deny <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 1 `；EOL ` RVA 0x345ED9A8 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f65b862c280a057](../../evidence/conditions-sets-031.md#c-4f65b862c280a057) · [状态效果 S-e7baf3740fc6d21a](../../evidence/state_effects-sets-049.md#s-e7baf3740fc6d21a)

### observed_connections-009115

```text
(config-policy)# cdp deny <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 4 `；EOL ` RVA 0x345EDFF8 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a473265fbdb2e1e4](../../evidence/conditions-sets-063.md#c-a473265fbdb2e1e4) · [状态效果 S-1634f493f288169d](../../evidence/state_effects-sets-005.md#s-1634f493f288169d)

### observed_connections-009104

```text
(config-policy)# default arp <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 0 `；EOL ` RVA 0x345ED358 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-10042eaabb0dc9eb](../../evidence/conditions-sets-006.md#c-10042eaabb0dc9eb) · [状态效果 S-cc5397b44d345dbb](../../evidence/state_effects-sets-043.md#s-cc5397b44d345dbb)

### observed_connections-009110

```text
(config-policy)# default broadcast <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 1 `；EOL ` RVA 0x345ED9A8 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-80d1f47da2e2d120](../../evidence/conditions-sets-050.md#c-80d1f47da2e2d120) · [状态效果 S-cc5397b44d345dbb](../../evidence/state_effects-sets-043.md#s-cc5397b44d345dbb)

### observed_connections-009116

```text
(config-policy)# default cdp <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 4 `；EOL ` RVA 0x345EDFF8 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-766e225146a16a70](../../evidence/conditions-sets-046.md#c-766e225146a16a70) · [状态效果 S-cc5397b44d345dbb](../../evidence/state_effects-sets-043.md#s-cc5397b44d345dbb)

### observed_connections-009107

```text
(config-policy)# default multicast <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 2 `；EOL ` RVA 0x345ED680 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-433c71d9fc382d5e](../../evidence/conditions-sets-026.md#c-433c71d9fc382d5e) · [状态效果 S-cc5397b44d345dbb](../../evidence/state_effects-sets-043.md#s-cc5397b44d345dbb)

### observed_connections-009119

```text
(config-policy)# default stp <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 5 `；EOL ` RVA 0x345EE320 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b18570120631562](../../evidence/conditions-sets-054.md#c-8b18570120631562) · [状态效果 S-cc5397b44d345dbb](../../evidence/state_effects-sets-043.md#s-cc5397b44d345dbb)

### observed_connections-009113

```text
(config-policy)# default unknown-destination <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 3 `；EOL ` RVA 0x345EDCD0 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7930353028b6267c](../../evidence/conditions-sets-047.md#c-7930353028b6267c) · [状态效果 S-cc5397b44d345dbb](../../evidence/state_effects-sets-043.md#s-cc5397b44d345dbb)

### observed_connections-009101

```text
(config-policy)# exit <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 7 `；EOL ` RVA 0x345EE638 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff66bd9dbfda0dc3](../../evidence/conditions-sets-098.md#c-ff66bd9dbfda0dc3)

### observed_connections-009106

```text
(config-policy)# multicast deny <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 2 `；EOL ` RVA 0x345ED680 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3dc08ba818c93f2a](../../evidence/conditions-sets-024.md#c-3dc08ba818c93f2a) · [状态效果 S-c8e773dc0b347978](../../evidence/state_effects-sets-043.md#s-c8e773dc0b347978)

### observed_connections-009102

```text
(config-policy)# no arp <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 0 `；EOL ` RVA 0x345ED358 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-78accacf3f3aeb57](../../evidence/conditions-sets-047.md#c-78accacf3f3aeb57) · [状态效果 S-655c1f41876af2f6](../../evidence/state_effects-sets-022.md#s-655c1f41876af2f6)

### observed_connections-009108

```text
(config-policy)# no broadcast <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 1 `；EOL ` RVA 0x345ED9A8 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-878044a46046ab79](../../evidence/conditions-sets-052.md#c-878044a46046ab79) · [状态效果 S-655c1f41876af2f6](../../evidence/state_effects-sets-022.md#s-655c1f41876af2f6)

### observed_connections-009114

```text
(config-policy)# no cdp <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 4 `；EOL ` RVA 0x345EDFF8 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-54352d8af14f85ff](../../evidence/conditions-sets-033.md#c-54352d8af14f85ff) · [状态效果 S-655c1f41876af2f6](../../evidence/state_effects-sets-022.md#s-655c1f41876af2f6)

### observed_connections-009105

```text
(config-policy)# no multicast <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 2 `；EOL ` RVA 0x345ED680 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-081b60e7906fea9e](../../evidence/conditions-sets-004.md#c-081b60e7906fea9e) · [状态效果 S-655c1f41876af2f6](../../evidence/state_effects-sets-022.md#s-655c1f41876af2f6)

### observed_connections-009117

```text
(config-policy)# no stp <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 5 `；EOL ` RVA 0x345EE320 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1328b22d74ce5442](../../evidence/conditions-sets-008.md#c-1328b22d74ce5442) · [状态效果 S-655c1f41876af2f6](../../evidence/state_effects-sets-022.md#s-655c1f41876af2f6)

### observed_connections-009111

```text
(config-policy)# no unknown-destination <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 3 `；EOL ` RVA 0x345EDCD0 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c443d9cf3dd01831](../../evidence/conditions-sets-076.md#c-c443d9cf3dd01831) · [状态效果 S-655c1f41876af2f6](../../evidence/state_effects-sets-022.md#s-655c1f41876af2f6)

### observed_connections-009118

```text
(config-policy)# stp deny <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 5 `；EOL ` RVA 0x345EE320 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f3c3507d7d40a345](../../evidence/conditions-sets-094.md#c-f3c3507d7d40a345) · [状态效果 S-e9a27ce1bd8f3e0e](../../evidence/state_effects-sets-049.md#s-e9a27ce1bd8f3e0e)

### observed_connections-009112

```text
(config-policy)# unknown-destination deny <cr>
```

Handler ` RVA 0xF281D10 `；selector ` 3 `；EOL ` RVA 0x345EDCD0 `。

模式根 ` RVA 0x345E0268 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6bf7c1e6fd80a24d](../../evidence/conditions-sets-042.md#c-6bf7c1e6fd80a24d) · [状态效果 S-a76dea410ab2afb3](../../evidence/state_effects-sets-035.md#s-a76dea410ab2afb3)
