# template · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008408

```text
(config-template)# carrier-delay <number:0..60> <cr>
```

Handler ` RVA 0xE40DD00 `；selector ` 2 `；EOL ` RVA 0x342BF070 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Carrier Transitions delay seconds。

[条件 C-b0a91a9ae8579ce2](../../evidence/conditions-sets-068.md#c-b0a91a9ae8579ce2) · [参数 P-b4034c00710c5f56](../../evidence/parameters-sets-014.md#p-b4034c00710c5f56)

### observed_connections-008419

```text
(config-template)# carrier-delay up <number:0..60> <cr>
```

Handler ` RVA 0xE40DCB0 `；selector ` 0 `；EOL ` RVA 0x342BEC80 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Carrier Up/Down Transitions delay seconds。

[条件 C-bc2b2e4eaea12b02](../../evidence/conditions-sets-073.md#c-bc2b2e4eaea12b02) · [参数 P-cba583b59b44aca6](../../evidence/parameters-sets-015.md#p-cba583b59b44aca6) · [状态效果 S-45726e1ea473025c](../../evidence/state_effects-sets-015.md#s-45726e1ea473025c)

### observed_connections-008407

```text
(config-template)# default carrier-delay <cr>
```

Handler ` RVA 0xE40DD00 `；selector ` 2 `；EOL ` RVA 0x342BF070 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c5e6106a75b5993e](../../evidence/conditions-sets-076.md#c-c5e6106a75b5993e) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008420

```text
(config-template)# default carrier-delay up <cr>
```

Handler ` RVA 0xE40DCB0 `；selector ` 0 `；EOL ` RVA 0x342BEC80 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2710d0a43c872ba3](../../evidence/conditions-sets-015.md#c-2710d0a43c872ba3) · [状态效果 S-c476ffef55d30cc2](../../evidence/state_effects-sets-042.md#s-c476ffef55d30cc2)

### observed_connections-008404

```text
(config-template)# default description <cr>
```

Handler ` RVA 0xE40C850 `；selector ` 3 `；EOL ` RVA 0x342BF4D8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c2ec2007ddeea307](../../evidence/conditions-sets-075.md#c-c2ec2007ddeea307) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008422

```text
(config-template)# default dialer idle-timeout <cr>
```

Handler ` RVA 0xF4C7E40 `；selector ` 0 `；EOL ` RVA 0x34669000 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6794f6896694ab87](../../evidence/conditions-sets-040.md#c-6794f6896694ab87) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008398

```text
(config-template)# default dialer-group <cr>
```

Handler ` RVA 0xF4C7E40 `；selector ` 1 `；EOL ` RVA 0x34669380 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb29707052809a7c](../../evidence/conditions-sets-097.md#c-fb29707052809a7c) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008415

```text
(config-template)# default hold-queue in <cr>
```

Handler ` RVA 0xE4086F0 `；selector ` 5 `；EOL ` RVA 0x342BFC78 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-20d00780888073b1](../../evidence/conditions-sets-013.md#c-20d00780888073b1) · [状态效果 S-451fb894e1c8342a](../../evidence/state_effects-sets-015.md#s-451fb894e1c8342a)

### observed_connections-008417

```text
(config-template)# default hold-queue out <cr>
```

Handler ` RVA 0xE4086F0 `；selector ` 6 `；EOL ` RVA 0x342BFF70 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-feca91683af0e35f](../../evidence/conditions-sets-098.md#c-feca91683af0e35f) · [状态效果 S-7f49193f16e4d4f2](../../evidence/state_effects-sets-027.md#s-7f49193f16e4d4f2)

### observed_connections-008396

```text
(config-template)# default load-interval <cr>
```

Handler ` RVA 0xE40DC60 `；selector ` 4 `；EOL ` RVA 0x342BF838 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9aea015aa5682539](../../evidence/conditions-sets-060.md#c-9aea015aa5682539) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008400

```text
(config-template)# default negate <cr>
```

Handler ` RVA 0xD6D8F20 `；selector ` 2 `；EOL ` RVA 0x33EDA938 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008413

```text
(config-template)# default pppoe follow <cr>
```

Handler ` RVA 0x11C52E90 `；selector ` 0 `；EOL ` RVA 0x356A9B30 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e08bb67fe3ee8455](../../evidence/conditions-sets-086.md#c-e08bb67fe3ee8455) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008402

```text
(config-template)# default remark <cr>
```

Handler ` RVA 0xD6D8F20 `；selector ` 0 `；EOL ` RVA 0x33EDAC80 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1f0bce7888782bae](../../evidence/conditions-sets-012.md#c-1f0bce7888782bae) · [状态效果 S-8f20c6f8152a82e1](../../evidence/state_effects-sets-030.md#s-8f20c6f8152a82e1)

### observed_connections-008425

```text
(config-template)# default service-policy input <string> <cr>
```

Handler ` RVA 0xD88ED70 `；selector ` 0 `；EOL ` RVA 0x33F134D8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy-map name。

[条件 C-6159d429b7eba5ae](../../evidence/conditions-sets-038.md#c-6159d429b7eba5ae) · [参数 P-23cea49528a3785c](../../evidence/parameters-sets-003.md#p-23cea49528a3785c) · [状态效果 S-5668f44822e1f950](../../evidence/state_effects-sets-019.md#s-5668f44822e1f950)

### observed_connections-008427

```text
(config-template)# default service-policy output <string> <cr>
```

Handler ` RVA 0xD88ED70 `；selector ` 1 `；EOL ` RVA 0x33F13798 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` policy-map name。

[条件 C-6159d429b7eba5ae](../../evidence/conditions-sets-038.md#c-6159d429b7eba5ae) · [参数 P-889620a54e86d185](../../evidence/parameters-sets-011.md#p-889620a54e86d185) · [状态效果 S-5668f44822e1f950](../../evidence/state_effects-sets-019.md#s-5668f44822e1f950)

### observed_connections-008405

```text
(config-template)# description <string> <cr>
```

Handler ` RVA 0xE40C850 `；selector ` 3 `；EOL ` RVA 0x342BF4D8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Up to 230 characters describing this interface。

[条件 C-63a8e3192dd1dc73](../../evidence/conditions-sets-039.md#c-63a8e3192dd1dc73) · [参数 P-cf21ef2b9fdfd687](../../evidence/parameters-sets-016.md#p-cf21ef2b9fdfd687)

### observed_connections-008423

```text
(config-template)# dialer idle-timeout <number:0..2147483> <cr>
```

Handler ` RVA 0xF4C7E40 `；selector ` 0 `；EOL ` RVA 0x34669000 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Idle timeout beforedisconnecting a call。

[条件 C-bfb92f6c66229a92](../../evidence/conditions-sets-074.md#c-bfb92f6c66229a92) · [参数 P-f0392cf8fe1741ca](../../evidence/parameters-sets-018.md#p-f0392cf8fe1741ca)

### observed_connections-008391

```text
(config-template)# dialer-group <number:1..128> <cr>
```

Handler ` RVA 0xF4C7E40 `；selector ` 1 `；EOL ` RVA 0x34669380 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer list number。

[条件 C-b37ecdfd4475692a](../../evidence/conditions-sets-069.md#c-b37ecdfd4475692a) · [参数 P-92df16c72cede92c](../../evidence/parameters-sets-011.md#p-92df16c72cede92c)

### observed_connections-008392

```text
(config-template)# exit <cr>
```

Handler ` RVA 0xD6D9F10 `；selector ` 0 `；EOL ` RVA 0x33EDAFE8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0b2fa8a0b76c0ee](../../evidence/conditions-sets-074.md#c-c0b2fa8a0b76c0ee)

### observed_connections-008428

```text
(config-template)# hold-queue <number:dynamic> in <cr>
```

Handler ` RVA 0xE4086F0 `；selector ` 5 `；EOL ` RVA 0x342BFC78 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Queue length。

[条件 C-5015f2d277a3009c](../../evidence/conditions-sets-031.md#c-5015f2d277a3009c) · [缺口 G-c1b7728f2580b6f7](../../evidence/gaps-sets-007.md#g-c1b7728f2580b6f7) · [参数 P-512a76b8cef220d0](../../evidence/parameters-sets-007.md#p-512a76b8cef220d0) · [状态效果 S-32138ec06b6b19d3](../../evidence/state_effects-sets-011.md#s-32138ec06b6b19d3)

### observed_connections-008429

```text
(config-template)# hold-queue <number:dynamic> out <cr>
```

Handler ` RVA 0xE4086F0 `；selector ` 6 `；EOL ` RVA 0x342BFF70 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Queue length。

[条件 C-68d126584e5f833f](../../evidence/conditions-sets-041.md#c-68d126584e5f833f) · [缺口 G-c1b7728f2580b6f7](../../evidence/gaps-sets-007.md#g-c1b7728f2580b6f7) · [参数 P-512a76b8cef220d0](../../evidence/parameters-sets-007.md#p-512a76b8cef220d0) · [状态效果 S-af872a9099deba7f](../../evidence/state_effects-sets-037.md#s-af872a9099deba7f)

### observed_connections-008390

```text
(config-template)# load-interval <number:30..600> <cr>
```

Handler ` RVA 0xE40DC60 `；selector ` 4 `；EOL ` RVA 0x342BF838 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load interval delay in seconds。

[条件 C-f357449bb8b214ab](../../evidence/conditions-sets-094.md#c-f357449bb8b214ab) · [参数 P-16cf7003cf979e0e](../../evidence/parameters-sets-002.md#p-16cf7003cf979e0e)

### observed_connections-008393

```text
(config-template)# negate <cr>
```

Handler ` RVA 0xD6D8F20 `；selector ` 2 `；EOL ` RVA 0x33EDA938 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008406

```text
(config-template)# no carrier-delay <cr>
```

Handler ` RVA 0xE40DD00 `；selector ` 2 `；EOL ` RVA 0x342BF070 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d25ae906286efc19](../../evidence/conditions-sets-081.md#c-d25ae906286efc19) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008418

```text
(config-template)# no carrier-delay up <cr>
```

Handler ` RVA 0xE40DCB0 `；selector ` 0 `；EOL ` RVA 0x342BEC80 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8b09d3dec5034b8b](../../evidence/conditions-sets-054.md#c-8b09d3dec5034b8b) · [状态效果 S-c91de76fe9f92e5a](../../evidence/state_effects-sets-043.md#s-c91de76fe9f92e5a)

### observed_connections-008403

```text
(config-template)# no description <cr>
```

Handler ` RVA 0xE40C850 `；selector ` 3 `；EOL ` RVA 0x342BF4D8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-914a1e649c75e95d](../../evidence/conditions-sets-056.md#c-914a1e649c75e95d) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008421

```text
(config-template)# no dialer idle-timeout <cr>
```

Handler ` RVA 0xF4C7E40 `；selector ` 0 `；EOL ` RVA 0x34669000 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c8cc604ffc89fbfc](../../evidence/conditions-sets-077.md#c-c8cc604ffc89fbfc) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008397

```text
(config-template)# no dialer-group <cr>
```

Handler ` RVA 0xF4C7E40 `；selector ` 1 `；EOL ` RVA 0x34669380 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fb29707052809a7c](../../evidence/conditions-sets-097.md#c-fb29707052809a7c) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008414

```text
(config-template)# no hold-queue in <cr>
```

Handler ` RVA 0xE4086F0 `；selector ` 5 `；EOL ` RVA 0x342BFC78 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-20d00780888073b1](../../evidence/conditions-sets-013.md#c-20d00780888073b1) · [状态效果 S-82d969c4b12f0f67](../../evidence/state_effects-sets-028.md#s-82d969c4b12f0f67)

### observed_connections-008416

```text
(config-template)# no hold-queue out <cr>
```

Handler ` RVA 0xE4086F0 `；selector ` 6 `；EOL ` RVA 0x342BFF70 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-feca91683af0e35f](../../evidence/conditions-sets-098.md#c-feca91683af0e35f) · [状态效果 S-92d9d7db7b7655e5](../../evidence/state_effects-sets-031.md#s-92d9d7db7b7655e5)

### observed_connections-008395

```text
(config-template)# no load-interval <cr>
```

Handler ` RVA 0xE40DC60 `；selector ` 4 `；EOL ` RVA 0x342BF838 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9aea015aa5682539](../../evidence/conditions-sets-060.md#c-9aea015aa5682539) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008399

```text
(config-template)# no negate <cr>
```

Handler ` RVA 0xD6D8F20 `；selector ` 2 `；EOL ` RVA 0x33EDA938 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008410

```text
(config-template)# no pppoe follow <cr>
```

Handler ` RVA 0x11C52E90 `；selector ` 0 `；EOL ` RVA 0x356A9B30 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-620a3b65d4d2b33e](../../evidence/conditions-sets-038.md#c-620a3b65d4d2b33e) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008401

```text
(config-template)# no remark <cr>
```

Handler ` RVA 0xD6D8F20 `；selector ` 0 `；EOL ` RVA 0x33EDAC80 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fe6ef773cf44a3b5](../../evidence/conditions-sets-098.md#c-fe6ef773cf44a3b5) · [状态效果 S-75c356b17da2c4f1](../../evidence/state_effects-sets-025.md#s-75c356b17da2c4f1)

### observed_connections-008424

```text
(config-template)# no service-policy input <string> <cr>
```

Handler ` RVA 0xD88ED70 `；selector ` 0 `；EOL ` RVA 0x33F134D8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` policy-map name。

[条件 C-6159d429b7eba5ae](../../evidence/conditions-sets-038.md#c-6159d429b7eba5ae) · [参数 P-23cea49528a3785c](../../evidence/parameters-sets-003.md#p-23cea49528a3785c) · [状态效果 S-4c60f6dc606cbea7](../../evidence/state_effects-sets-017.md#s-4c60f6dc606cbea7)

### observed_connections-008426

```text
(config-template)# no service-policy output <string> <cr>
```

Handler ` RVA 0xD88ED70 `；selector ` 1 `；EOL ` RVA 0x33F13798 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` policy-map name。

[条件 C-6159d429b7eba5ae](../../evidence/conditions-sets-038.md#c-6159d429b7eba5ae) · [参数 P-889620a54e86d185](../../evidence/parameters-sets-011.md#p-889620a54e86d185) · [状态效果 S-4c60f6dc606cbea7](../../evidence/state_effects-sets-017.md#s-4c60f6dc606cbea7)

### observed_connections-008412

```text
(config-template)# pppoe follow <string> <cr>
```

Handler ` RVA 0x11C52E90 `；selector ` 0 `；EOL ` RVA 0x356A9B30 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-c0d7d916a9e24005](../../evidence/conditions-sets-074.md#c-c0d7d916a9e24005) · [参数 P-ecda5725703b4544](../../evidence/parameters-sets-018.md#p-ecda5725703b4544)

### observed_connections-008394

```text
(config-template)# remark <cr>
```

Handler ` RVA 0xD6D8F20 `；selector ` 0 `；EOL ` RVA 0x33EDAC80 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1bb45ce038f8dda](../../evidence/conditions-sets-062.md#c-a1bb45ce038f8dda)

### observed_connections-008409

```text
(config-template)# service-policy input <string> <cr>
```

Handler ` RVA 0xD88ED70 `；selector ` 0 `；EOL ` RVA 0x33F134D8 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` policy-map name。

[条件 C-6159d429b7eba5ae](../../evidence/conditions-sets-038.md#c-6159d429b7eba5ae) · [参数 P-23cea49528a3785c](../../evidence/parameters-sets-003.md#p-23cea49528a3785c) · [状态效果 S-307bd836d6db7020](../../evidence/state_effects-sets-011.md#s-307bd836d6db7020)

### observed_connections-008411

```text
(config-template)# service-policy output <string> <cr>
```

Handler ` RVA 0xD88ED70 `；selector ` 1 `；EOL ` RVA 0x33F13798 `。

模式根 ` RVA 0x33ECF6D8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` policy-map name。

[条件 C-6159d429b7eba5ae](../../evidence/conditions-sets-038.md#c-6159d429b7eba5ae) · [参数 P-889620a54e86d185](../../evidence/parameters-sets-011.md#p-889620a54e86d185) · [状态效果 S-307bd836d6db7020](../../evidence/state_effects-sets-011.md#s-307bd836d6db7020)

