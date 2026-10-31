# sd-service-controller · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008451

```text
(config-sd-service-controller)# address <address> <address> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 32 `；EOL ` RVA 0x35260E38 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Primary controller's IPv6 address；` address ` Secondary controller's IPv6 address。

[条件 C-05e02f3b636a3a43](../../evidence/conditions-sets-003.md#c-05e02f3b636a3a43) · [参数 P-676b87bff504f3a1](../../evidence/parameters-sets-008.md#p-676b87bff504f3a1)

### observed_connections-008440

```text
(config-sd-service-controller)# address <address> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 31 `；EOL ` RVA 0x35260D00 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Primary controller's IPv6 address。

[条件 C-8e88597685ee0cb5](../../evidence/conditions-sets-055.md#c-8e88597685ee0cb5) · [参数 P-ba46e3cc8f7e5bd2](../../evidence/parameters-sets-014.md#p-ba46e3cc8f7e5bd2)

### observed_connections-008432

```text
(config-sd-service-controller)# authentication-mode thousandeyes <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 42 `；EOL ` RVA 0x3525FFC8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5dcd3839c7156e34](../../evidence/conditions-sets-037.md#c-5dcd3839c7156e34) · [状态效果 S-08b6321bfbfd800d](../../evidence/state_effects-sets-002.md#s-08b6321bfbfd800d)

### observed_connections-008433

```text
(config-sd-service-controller)# authentication-token <string> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 43 `；EOL ` RVA 0x352602F8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter a token string.。

[条件 C-9f89c142ca3f7572](../../evidence/conditions-sets-062.md#c-9f89c142ca3f7572) · [参数 P-2ab7d1fa7e4805e6](../../evidence/parameters-sets-004.md#p-2ab7d1fa7e4805e6)

### observed_connections-008446

```text
(config-sd-service-controller)# destination-ports application-updates <number:1..65535> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 33 `；EOL ` RVA 0x35261508 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port value。

[条件 C-9763069e4838881d](../../evidence/conditions-sets-058.md#c-9763069e4838881d) · [参数 P-72ae1229fa60090d](../../evidence/parameters-sets-009.md#p-72ae1229fa60090d) · [状态效果 S-bf6cee0de90654a6](../../evidence/state_effects-sets-040.md#s-bf6cee0de90654a6)

### observed_connections-008448

```text
(config-sd-service-controller)# destination-ports sensor-exporter <number:1..65535> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 34 `；EOL ` RVA 0x35261808 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port value。

[条件 C-b23c5f800047eb88](../../evidence/conditions-sets-069.md#c-b23c5f800047eb88) · [参数 P-47122189a3c06446](../../evidence/parameters-sets-006.md#p-47122189a3c06446) · [状态效果 S-a022c75cf4c54d97](../../evidence/state_effects-sets-034.md#s-a022c75cf4c54d97)

### observed_connections-008435

```text
(config-sd-service-controller)# dscp <number:0..63> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 30 `；EOL ` RVA 0x352609E8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DSCP value。

[条件 C-6818154f7bf1e405](../../evidence/conditions-sets-040.md#c-6818154f7bf1e405) · [参数 P-d491b942a793ee98](../../evidence/parameters-sets-016.md#p-d491b942a793ee98) · [状态效果 S-bc5a4c379dadc41b](../../evidence/state_effects-sets-040.md#s-bc5a4c379dadc41b)

### observed_connections-008430

```text
(config-sd-service-controller)# exit <cr>
```

Handler ` RVA 0x10F266E0 `；selector ` 0 `；EOL ` RVA 0x352701A8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-223ced88ad043903](../../evidence/conditions-sets-013.md#c-223ced88ad043903)

### observed_connections-008439

```text
(config-sd-service-controller)# hostname <string> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 38 `；EOL ` RVA 0x35261B10 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Primary controller's hostname。

[条件 C-42cbb155ad55262f](../../evidence/conditions-sets-026.md#c-42cbb155ad55262f) · [参数 P-2183544ef9aa40b3](../../evidence/parameters-sets-003.md#p-2183544ef9aa40b3)

### observed_connections-008450

```text
(config-sd-service-controller)# hostname <string> <string> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 39 `；EOL ` RVA 0x35261BA0 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Primary controller's hostname；` string ` Secondary controller's hostname。

[条件 C-42cbb155ad55262f](../../evidence/conditions-sets-026.md#c-42cbb155ad55262f) · [参数 P-791d7af8e03993c6](../../evidence/parameters-sets-009.md#p-791d7af8e03993c6)

### observed_connections-008437

```text
(config-sd-service-controller)# no address <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 31 `；EOL ` RVA 0x35260D00 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-eafb6498ca21cd10](../../evidence/conditions-sets-091.md#c-eafb6498ca21cd10) · [状态效果 S-43db3d21b1d3b8dd](../../evidence/state_effects-sets-015.md#s-43db3d21b1d3b8dd)

### observed_connections-008442

```text
(config-sd-service-controller)# no authentication-mode thousandeyes <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 42 `；EOL ` RVA 0x3525FFC8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5dcd3839c7156e34](../../evidence/conditions-sets-037.md#c-5dcd3839c7156e34) · [状态效果 S-4b82de7a9559c732](../../evidence/state_effects-sets-017.md#s-4b82de7a9559c732)

### observed_connections-008444

```text
(config-sd-service-controller)# no authentication-token <string> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 43 `；EOL ` RVA 0x352602F8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Enter a token string.。

[条件 C-9f89c142ca3f7572](../../evidence/conditions-sets-062.md#c-9f89c142ca3f7572) · [参数 P-2ab7d1fa7e4805e6](../../evidence/parameters-sets-004.md#p-2ab7d1fa7e4805e6) · [状态效果 S-43db3d21b1d3b8dd](../../evidence/state_effects-sets-015.md#s-43db3d21b1d3b8dd)

### observed_connections-008447

```text
(config-sd-service-controller)# no destination-ports application-updates <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 33 `；EOL ` RVA 0x35261508 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-950f3b977dd220ff](../../evidence/conditions-sets-058.md#c-950f3b977dd220ff) · [状态效果 S-cec02a1a98a3d4d4](../../evidence/state_effects-sets-044.md#s-cec02a1a98a3d4d4)

### observed_connections-008449

```text
(config-sd-service-controller)# no destination-ports sensor-exporter <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 34 `；EOL ` RVA 0x35261808 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-591b9948661fbe53](../../evidence/conditions-sets-035.md#c-591b9948661fbe53) · [状态效果 S-d34115e19596995b](../../evidence/state_effects-sets-045.md#s-d34115e19596995b)

### observed_connections-008436

```text
(config-sd-service-controller)# no dscp <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 30 `；EOL ` RVA 0x352609E8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6116101a349b6179](../../evidence/conditions-sets-038.md#c-6116101a349b6179) · [状态效果 S-0f6b6f59cb7146dc](../../evidence/state_effects-sets-004.md#s-0f6b6f59cb7146dc)

### observed_connections-008438

```text
(config-sd-service-controller)# no hostname <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 38 `；EOL ` RVA 0x35261B10 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ec52cb75fc2d6da4](../../evidence/conditions-sets-091.md#c-ec52cb75fc2d6da4) · [状态效果 S-43db3d21b1d3b8dd](../../evidence/state_effects-sets-015.md#s-43db3d21b1d3b8dd)

### observed_connections-008434

```text
(config-sd-service-controller)# no source-interface <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 29 `；EOL ` RVA 0x35260608 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2d05bdbe655bfd3c](../../evidence/conditions-sets-018.md#c-2d05bdbe655bfd3c) · [状态效果 S-43db3d21b1d3b8dd](../../evidence/state_effects-sets-015.md#s-43db3d21b1d3b8dd)

### observed_connections-008443

```text
(config-sd-service-controller)# no transport application-updates <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 36 `；EOL ` RVA 0x3525F8B8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75da990e4851671c](../../evidence/conditions-sets-046.md#c-75da990e4851671c) · [状态效果 S-43db3d21b1d3b8dd](../../evidence/state_effects-sets-015.md#s-43db3d21b1d3b8dd)

### observed_connections-008452

```text
(config-sd-service-controller)# no transport sensor-exporter udp <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 37 `；EOL ` RVA 0x3525FC68 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74e8906f0e796d30](../../evidence/conditions-sets-045.md#c-74e8906f0e796d30) · [状态效果 S-1cfb4195f82a7425](../../evidence/state_effects-sets-007.md#s-1cfb4195f82a7425)

### observed_connections-008431

```text
(config-sd-service-controller)# no vrf <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 28 `；EOL ` RVA 0x3525F390 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-98ff8f5f122de419](../../evidence/conditions-sets-059.md#c-98ff8f5f122de419) · [状态效果 S-69c8977b90318065](../../evidence/state_effects-sets-023.md#s-69c8977b90318065)

### observed_connections-008454

```text
(config-sd-service-controller)# source-interface <interface> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 29 `；EOL ` RVA 0x35260608 `。

模式根 ` RVA 0x35239650 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d2f66131fa41b70a](../../evidence/conditions-sets-081.md#c-d2f66131fa41b70a) · [缺口 G-2c19ed58492d8165](../../evidence/gaps-sets-002.md#g-2c19ed58492d8165) · [参数 P-4744516dd2670e06](../../evidence/parameters-sets-006.md#p-4744516dd2670e06)

### observed_connections-008445

```text
(config-sd-service-controller)# transport application-updates http <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 36 `；EOL ` RVA 0x3525F8B8 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b793f024eb5a1ae3](../../evidence/conditions-sets-071.md#c-b793f024eb5a1ae3) · [状态效果 S-50550a7c4c271e6d](../../evidence/state_effects-sets-018.md#s-50550a7c4c271e6d)

### observed_connections-008441

```text
(config-sd-service-controller)# transport sensor-exporter udp <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 37 `；EOL ` RVA 0x3525FC68 `。

模式根 ` RVA 0x35239650 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-74e8906f0e796d30](../../evidence/conditions-sets-045.md#c-74e8906f0e796d30) · [状态效果 S-05d745cb1b8d28ff](../../evidence/state_effects-sets-002.md#s-05d745cb1b8d28ff)

### observed_connections-008453

```text
(config-sd-service-controller)# vrf <string> <cr>
```

Handler ` RVA 0x10F35310 `；selector ` 28 `；EOL ` RVA 0x3525F390 `。

模式根 ` RVA 0x35239650 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-24afaf682bd0b374](../../evidence/conditions-sets-014.md#c-24afaf682bd0b374) · [缺口 G-9a58508d04bff653](../../evidence/gaps-sets-006.md#g-9a58508d04bff653) · [参数 P-615eb8471f47c353](../../evidence/parameters-sets-008.md#p-615eb8471f47c353) · [状态效果 S-751ea014b567d88e](../../evidence/state_effects-sets-025.md#s-751ea014b567d88e)

