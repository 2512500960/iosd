# pm-endpoint · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008716

```text
(config-pm-ep)# default <cr>
```

Handler ` RVA 0x1ACFA0B0 `；selector ` 0 `；EOL ` RVA 0x36DC3EB0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008719

```text
(config-pm-ep)# default delay-measurement <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008734

```text
(config-pm-ep)# default delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Profile name。

[参数 P-b695e46c7785141e](../../evidence/parameters-sets-014.md#p-b695e46c7785141e) · [状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008732

```text
(config-pm-ep)# default destination-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA520 `；selector ` 0 `；EOL ` RVA 0x36DC23F0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 endpoint address。

[参数 P-2b63d45ccd1050c4](../../evidence/parameters-sets-004.md#p-2b63d45ccd1050c4) · [状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008723

```text
(config-pm-ep)# default segment-list <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008738

```text
(config-pm-ep)# default segment-list forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Identifying name for segment-list。

[参数 P-ad1fa3ff5e2c2b78](../../evidence/parameters-sets-013.md#p-ad1fa3ff5e2c2b78) · [状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008740

```text
(config-pm-ep)# default segment-list reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Identifying name for reverse path segment-list。

[参数 P-1d628917302bc153](../../evidence/parameters-sets-003.md#p-1d628917302bc153) · [状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008721

```text
(config-pm-ep)# default shutdown <cr>
```

Handler ` RVA 0x1ACFA990 `；selector ` 0 `；EOL ` RVA 0x36DC3C08 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008736

```text
(config-pm-ep)# default source-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA400 `；selector ` 0 `；EOL ` RVA 0x36DC2D78 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 source address。

[参数 P-6ae47aa8f290513a](../../evidence/parameters-sets-008.md#p-6ae47aa8f290513a) · [状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008728

```text
(config-pm-ep)# default vrf <string> <cr>
```

Handler ` RVA 0x1ACFA640 `；selector ` 0 `；EOL ` RVA 0x36DC30D0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` VRF Name。

[参数 P-70291308bcd07f60](../../evidence/parameters-sets-009.md#p-70291308bcd07f60) · [状态效果 S-49607e42bfe05131](../../evidence/state_effects-sets-016.md#s-49607e42bfe05131)

### observed_connections-008712

```text
(config-pm-ep)# delay-measurement <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008725

```text
(config-pm-ep)# delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile name。

[参数 P-b695e46c7785141e](../../evidence/parameters-sets-014.md#p-b695e46c7785141e)

### observed_connections-008724

```text
(config-pm-ep)# destination-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA520 `；selector ` 0 `；EOL ` RVA 0x36DC23F0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 endpoint address。

[参数 P-2b63d45ccd1050c4](../../evidence/parameters-sets-004.md#p-2b63d45ccd1050c4)

### observed_connections-008711

```text
(config-pm-ep)# exit <cr>
```

Handler ` RVA 0x1ACF3980 `；selector ` 0 `；EOL ` RVA 0x36DE22B0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2931f64bf0ffd587](../../evidence/conditions-sets-016.md#c-2931f64bf0ffd587)

### observed_connections-008714

```text
(config-pm-ep)# no <cr>
```

Handler ` RVA 0x1ACFA0B0 `；selector ` 0 `；EOL ` RVA 0x36DC3EB0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008717

```text
(config-pm-ep)# no delay-measurement <cr>
```

Handler ` RVA 0x1ACFA820 `；selector ` 0 `；EOL ` RVA 0x36DC2A30 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008733

```text
(config-pm-ep)# no delay-measurement profile <string> <cr>
```

Handler ` RVA 0x1ACFAA20 `；selector ` 0 `；EOL ` RVA 0x36DC27B0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Profile name。

[参数 P-b695e46c7785141e](../../evidence/parameters-sets-014.md#p-b695e46c7785141e) · [状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008731

```text
(config-pm-ep)# no destination-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA520 `；selector ` 0 `；EOL ` RVA 0x36DC23F0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 endpoint address。

[参数 P-2b63d45ccd1050c4](../../evidence/parameters-sets-004.md#p-2b63d45ccd1050c4) · [状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008722

```text
(config-pm-ep)# no segment-list <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008737

```text
(config-pm-ep)# no segment-list forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Identifying name for segment-list。

[参数 P-ad1fa3ff5e2c2b78](../../evidence/parameters-sets-013.md#p-ad1fa3ff5e2c2b78) · [状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008739

```text
(config-pm-ep)# no segment-list reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Identifying name for reverse path segment-list。

[参数 P-1d628917302bc153](../../evidence/parameters-sets-003.md#p-1d628917302bc153) · [状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008720

```text
(config-pm-ep)# no shutdown <cr>
```

Handler ` RVA 0x1ACFA990 `；selector ` 0 `；EOL ` RVA 0x36DC3C08 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008735

```text
(config-pm-ep)# no source-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA400 `；selector ` 0 `；EOL ` RVA 0x36DC2D78 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` IPv4 source address。

[参数 P-6ae47aa8f290513a](../../evidence/parameters-sets-008.md#p-6ae47aa8f290513a) · [状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008727

```text
(config-pm-ep)# no vrf <string> <cr>
```

Handler ` RVA 0x1ACFA640 `；selector ` 0 `；EOL ` RVA 0x36DC30D0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` VRF Name。

[参数 P-70291308bcd07f60](../../evidence/parameters-sets-009.md#p-70291308bcd07f60) · [状态效果 S-a18f36285825124c](../../evidence/state_effects-sets-034.md#s-a18f36285825124c)

### observed_connections-008715

```text
(config-pm-ep)# segment-list <cr>
```

Handler ` RVA 0x1ACFA770 `；selector ` 0 `；EOL ` RVA 0x36DC3988 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008729

```text
(config-pm-ep)# segment-list forward-path <string> <cr>
```

Handler ` RVA 0x1ACFAB50 `；selector ` 0 `；EOL ` RVA 0x36DC3420 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Identifying name for segment-list。

[参数 P-ad1fa3ff5e2c2b78](../../evidence/parameters-sets-013.md#p-ad1fa3ff5e2c2b78)

### observed_connections-008730

```text
(config-pm-ep)# segment-list reverse-path <string> <cr>
```

Handler ` RVA 0x1ACFACB0 `；selector ` 0 `；EOL ` RVA 0x36DC3708 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Identifying name for reverse path segment-list。

[参数 P-1d628917302bc153](../../evidence/parameters-sets-003.md#p-1d628917302bc153)

### observed_connections-008713

```text
(config-pm-ep)# shutdown <cr>
```

Handler ` RVA 0x1ACFA990 `；selector ` 0 `；EOL ` RVA 0x36DC3C08 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008726

```text
(config-pm-ep)# source-address ipv4 <address> <cr>
```

Handler ` RVA 0x1ACFA400 `；selector ` 0 `；EOL ` RVA 0x36DC2D78 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 source address。

[参数 P-6ae47aa8f290513a](../../evidence/parameters-sets-008.md#p-6ae47aa8f290513a)

### observed_connections-008718

```text
(config-pm-ep)# vrf <string> <cr>
```

Handler ` RVA 0x1ACFA640 `；selector ` 0 `；EOL ` RVA 0x36DC30D0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF Name。

[参数 P-70291308bcd07f60](../../evidence/parameters-sets-009.md#p-70291308bcd07f60)

### observed_connections-008710

```text
(config-pm-ep)# <cr>
```

Handler ` RVA 0x1ACFA0B0 `；selector ` 0 `；EOL ` RVA 0x36DC3EB0 `。

模式根 ` RVA 0x36DC1DB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
