# custom · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008868

```text
(config-custom)# direction source <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 6 `；EOL ` RVA 0x3525C668 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c4dcbf48555b2959](../../evidence/conditions-sets-076.md#c-c4dcbf48555b2959) · [状态效果 S-2ba0b03a010fd301](../../evidence/state_effects-sets-010.md#s-2ba0b03a010fd301)

### observed_connections-008876

```text
(config-custom)# dscp <?common_dscp_value_action@55558a7b0a38> <?common_dscp_value_action@55558a7b0a88> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 7 `；EOL ` RVA 0x3525CD00 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-30b28a1744724f1e](../../evidence/conditions-sets-019.md#c-30b28a1744724f1e) · [缺口 G-532a6c1a1a981bf0](../../evidence/gaps-sets-003.md#g-532a6c1a1a981bf0) · [状态效果 S-1d940b82c02f38af](../../evidence/state_effects-sets-007.md#s-1d940b82c02f38af)

### observed_connections-008862

```text
(config-custom)# exit <cr>
```

Handler ` RVA 0x10F25F40 `；selector ` 0 `；EOL ` RVA 0x3526F9B8 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c5da90950655a0a](../../evidence/conditions-sets-042.md#c-6c5da90950655a0a)

### observed_connections-008863

```text
(config-custom)# ip <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 0 `；EOL ` RVA 0x3525DCE8 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-727d78d7091346c3](../../evidence/conditions-sets-044.md#c-727d78d7091346c3)

### observed_connections-008873

```text
(config-custom)# ip subnet <address> <number:0..32> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 1 `；EOL ` RVA 0x3525E140 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Subnet IP；` unsigned_number ` Subnet mask length。

[条件 C-ff5430d931d7b168](../../evidence/conditions-sets-098.md#c-ff5430d931d7b168) · [参数 P-aaccc065768a78ec](../../evidence/parameters-sets-013.md#p-aaccc065768a78ec)

### observed_connections-008872

```text
(config-custom)# ipv6 address <address> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 2 `；EOL ` RVA 0x3525E450 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` List of up to 8 IPs separated by white-spaces.。

[条件 C-50f11b4ad80a9737](../../evidence/conditions-sets-032.md#c-50f11b4ad80a9737) · [参数 P-1b69704d6617b161](../../evidence/parameters-sets-003.md#p-1b69704d6617b161)

### observed_connections-008874

```text
(config-custom)# ipv6 subnet <address> <number:0..128> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 3 `；EOL ` RVA 0x3525E738 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Subnet IPV6；` unsigned_number ` Subnet mask length。

[条件 C-50f11b4ad80a9737](../../evidence/conditions-sets-032.md#c-50f11b4ad80a9737) · [参数 P-be84bd034c5553af](../../evidence/parameters-sets-014.md#p-be84bd034c5553af)

### observed_connections-008869

```text
(config-custom)# no direction <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 6 `；EOL ` RVA 0x3525C668 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bf4eac3ce4f1cdf4](../../evidence/conditions-sets-074.md#c-bf4eac3ce4f1cdf4) · [状态效果 S-80ff111aa7fe5ca1](../../evidence/state_effects-sets-027.md#s-80ff111aa7fe5ca1)

### observed_connections-008870

```text
(config-custom)# no dscp <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 7 `；EOL ` RVA 0x3525CD00 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a443542d61af9578](../../evidence/conditions-sets-063.md#c-a443542d61af9578) · [状态效果 S-31fbf216fe2db11f](../../evidence/state_effects-sets-011.md#s-31fbf216fe2db11f)

### observed_connections-008865

```text
(config-custom)# no ip <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 0 `；EOL ` RVA 0x3525DCE8 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-727d78d7091346c3](../../evidence/conditions-sets-044.md#c-727d78d7091346c3) · [状态效果 S-80ff111aa7fe5ca1](../../evidence/state_effects-sets-027.md#s-80ff111aa7fe5ca1)

### observed_connections-008875

```text
(config-custom)# no ip subnet <address> <number:0..32> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 1 `；EOL ` RVA 0x3525E140 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Subnet IP；` unsigned_number ` Subnet mask length。

[条件 C-ff5430d931d7b168](../../evidence/conditions-sets-098.md#c-ff5430d931d7b168) · [参数 P-aaccc065768a78ec](../../evidence/parameters-sets-013.md#p-aaccc065768a78ec) · [状态效果 S-80ff111aa7fe5ca1](../../evidence/state_effects-sets-027.md#s-80ff111aa7fe5ca1)

### observed_connections-008867

```text
(config-custom)# no ipv6 <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 2 `；EOL ` RVA 0x3525E450 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b3659dcbbf95b5f6](../../evidence/conditions-sets-069.md#c-b3659dcbbf95b5f6) · [状态效果 S-80ff111aa7fe5ca1](../../evidence/state_effects-sets-027.md#s-80ff111aa7fe5ca1)

### observed_connections-008866

```text
(config-custom)# no port <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 4 `；EOL ` RVA 0x3525D0C0 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-13db74258d99c06f](../../evidence/conditions-sets-008.md#c-13db74258d99c06f) · [状态效果 S-80ff111aa7fe5ca1](../../evidence/state_effects-sets-027.md#s-80ff111aa7fe5ca1)

### observed_connections-008864

```text
(config-custom)# port <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 5 `；EOL ` RVA 0x3525D678 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e5dec2efcf2f37ca](../../evidence/conditions-sets-089.md#c-e5dec2efcf2f37ca) · [状态效果 S-8cebe9ddf6e417d5](../../evidence/state_effects-sets-030.md#s-8cebe9ddf6e417d5)

### observed_connections-008871

```text
(config-custom)# port <number:1..65535> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 4 `；EOL ` RVA 0x3525D0C0 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Up to 8 port numbers separated by white-spaces。

[条件 C-c11a07e5b4635ed5](../../evidence/conditions-sets-075.md#c-c11a07e5b4635ed5) · [参数 P-38ab48103931a221](../../evidence/parameters-sets-005.md#p-38ab48103931a221) · [状态效果 S-8cebe9ddf6e417d5](../../evidence/state_effects-sets-030.md#s-8cebe9ddf6e417d5)

### observed_connections-008877

```text
(config-custom)# port range <number:1..65535> <number:dynamic> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 5 `；EOL ` RVA 0x3525D678 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter Start port number for Range；` unsigned_number_dynamic ` Enter End port number for Range.。

[条件 C-8a5f960582b1edf2](../../evidence/conditions-sets-054.md#c-8a5f960582b1edf2) · [缺口 G-c2289a58e0bb9608](../../evidence/gaps-sets-007.md#g-c2289a58e0bb9608) · [参数 P-d00586051a637bc8](../../evidence/parameters-sets-016.md#p-d00586051a637bc8) · [状态效果 S-087ed181f98c4824](../../evidence/state_effects-sets-002.md#s-087ed181f98c4824)

### observed_connections-008878

```text
(config-custom)# port range <number:1..65535> <number:dynamic> <number:1..65535> <cr>
```

Handler ` RVA 0x10F3A140 `；selector ` 4 `；EOL ` RVA 0x3525D0C0 `。

模式根 ` RVA 0x352395B0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter Start port number for Range；` unsigned_number_dynamic ` Enter End port number for Range.；` unsigned_number ` Up to 8 port numbers separated by white-spaces。

[条件 C-7b2c87f5854e566b](../../evidence/conditions-sets-048.md#c-7b2c87f5854e566b) · [缺口 G-c2289a58e0bb9608](../../evidence/gaps-sets-007.md#g-c2289a58e0bb9608) · [参数 P-b593cfd1a592c75b](../../evidence/parameters-sets-014.md#p-b593cfd1a592c75b) · [状态效果 S-087ed181f98c4824](../../evidence/state_effects-sets-002.md#s-087ed181f98c4824)
