# ethernet-evc-config · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009528

```text
(config-evc)# default exit <cr>
```

Handler ` RVA 0xBFFE880 `；selector ` 0 `；EOL ` RVA 0x33974780 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-394e6068fa57899a](../../evidence/state_effects-sets-013.md#s-394e6068fa57899a)

### observed_connections-009531

```text
(config-evc)# default oam protocol <cr>
```

Handler ` RVA 0xBFFE9D0 `；selector ` 3 `；EOL ` RVA 0x33974FE0 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed6948a990fb90ab](../../evidence/conditions-sets-092.md#c-ed6948a990fb90ab) · [状态效果 S-394e6068fa57899a](../../evidence/state_effects-sets-013.md#s-394e6068fa57899a)

### observed_connections-009532

```text
(config-evc)# default uni count <cr>
```

Handler ` RVA 0xBFFE9D0 `；selector ` 1 `；EOL ` RVA 0x33974BC0 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1c11f1dcf120a36e](../../evidence/conditions-sets-011.md#c-1c11f1dcf120a36e) · [状态效果 S-394e6068fa57899a](../../evidence/state_effects-sets-013.md#s-394e6068fa57899a)

### observed_connections-009526

```text
(config-evc)# exit <cr>
```

Handler ` RVA 0xBFFE880 `；selector ` 0 `；EOL ` RVA 0x33974780 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-009527

```text
(config-evc)# no exit <cr>
```

Handler ` RVA 0xBFFE880 `；selector ` 0 `；EOL ` RVA 0x33974780 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-6ca72b6810aa276f](../../evidence/state_effects-sets-023.md#s-6ca72b6810aa276f)

### observed_connections-009529

```text
(config-evc)# no oam protocol <cr>
```

Handler ` RVA 0xBFFE9D0 `；selector ` 3 `；EOL ` RVA 0x33974FE0 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cc2b9ebb6604fbd8](../../evidence/conditions-sets-079.md#c-cc2b9ebb6604fbd8) · [状态效果 S-6ca72b6810aa276f](../../evidence/state_effects-sets-023.md#s-6ca72b6810aa276f)

### observed_connections-009530

```text
(config-evc)# no uni count <cr>
```

Handler ` RVA 0xBFFE9D0 `；selector ` 1 `；EOL ` RVA 0x33974BC0 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-03891caa8f53f336](../../evidence/conditions-sets-002.md#c-03891caa8f53f336) · [状态效果 S-6ca72b6810aa276f](../../evidence/state_effects-sets-023.md#s-6ca72b6810aa276f)

### observed_connections-009533

```text
(config-evc)# oam protocol ldp <cr>
```

Handler ` RVA 0xBFFE9D0 `；selector ` 3 `；EOL ` RVA 0x33974FE0 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-426fc841ab00db0e](../../evidence/conditions-sets-026.md#c-426fc841ab00db0e) · [状态效果 S-a1cf91f6428432a9](../../evidence/state_effects-sets-034.md#s-a1cf91f6428432a9)

### observed_connections-009534

```text
(config-evc)# uni count <number:2..1024> <cr>
```

Handler ` RVA 0xBFFE9D0 `；selector ` 1 `；EOL ` RVA 0x33974BC0 `。

模式根 ` RVA 0x33974730 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` UNI COUNT required, range 2 - 1024。

[条件 C-9a413a729cbf86ae](../../evidence/conditions-sets-060.md#c-9a413a729cbf86ae) · [参数 P-45d1a12da5026b17](../../evidence/parameters-sets-006.md#p-45d1a12da5026b17)
