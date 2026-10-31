# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-011650

```text
(exec)# test platform software macsec pattern-delete name <string> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 54 `；EOL ` RVA 0x35ECA218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pattern name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-2b96e7d041d5508f](../../evidence/parameters-sets-004.md#p-2b96e7d041d5508f)

### path-024616

```text
(exec)# test platform software macsec pattern-detach name <string> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 56 `；EOL ` RVA 0x35ECA610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pattern name。

[条件 C-4d7de9fd0841184b](../../evidence/conditions-sets-030.md#c-4d7de9fd0841184b) · [缺口 G-fe5b4b62c2cee16f](../../evidence/gaps-sets-009.md#g-fe5b4b62c2cee16f) · [参数 P-ca7f81b167576206](../../evidence/parameters-sets-015.md#p-ca7f81b167576206)

### path-012213

```text
(exec)# test platform software macsec pattern-name name <string> is-control yes has-vlan-tag yes has-vlan-inner-tag yes vlan-id <number:0..65535> inner-vlan-id <number:0..65535> priority <number:0..15> header <string> header-length <number:0..65535> control-frame dmac dest-mac <address> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 55 `；EOL ` RVA 0x35EC94B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` pattern name；` unsigned_number ` outer vlan id；` unsigned_number ` inner vlan id；` unsigned_number ` priority level；` string ` header pattern；` unsigned_number ` header pattern length；` address ` MAC address。

[条件 C-329b24473abbc62e](../../evidence/conditions-sets-020.md#c-329b24473abbc62e) · [参数 P-8671486ebe6bccdf](../../evidence/parameters-sets-010.md#p-8671486ebe6bccdf) · [状态效果 S-6434d4199d8c0c52](../../evidence/state_effects-sets-021.md#s-6434d4199d8c0c52)

### path-025231

```text
(exec)# test platform software macsec pattern-set name <string> action controlled-port direction ingress <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 53 `；EOL ` RVA 0x35EC9D30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` pattern name。

[条件 C-4667cddd27955b97](../../evidence/conditions-sets-027.md#c-4667cddd27955b97) · [缺口 G-c00353e2cbfa174c](../../evidence/gaps-sets-007.md#g-c00353e2cbfa174c) · [参数 P-0fc900d7b707bda3](../../evidence/parameters-sets-002.md#p-0fc900d7b707bda3) · [状态效果 S-0fc9e5c4028275eb](../../evidence/state_effects-sets-004.md#s-0fc9e5c4028275eb)

### path-021202

```text
(exec)# test platform software macsec post <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 20 `；EOL ` RVA 0x35ECF688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-db9e1f36408c8dd0](../../evidence/conditions-sets-085.md#c-db9e1f36408c8dd0) · [缺口 G-25885e093e8090a4](../../evidence/gaps-sets-002.md#g-25885e093e8090a4) · [参数 P-f4c1fe614c8b6c78](../../evidence/parameters-sets-018.md#p-f4c1fe614c8b6c78)

### path-025249

```text
(exec)# test platform software macsec rx sa delete an <number:0..3> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 35 `；EOL ` RVA 0x35ECBFF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0-3 association；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-d30fe117c88cab3b](../../evidence/conditions-sets-081.md#c-d30fe117c88cab3b) · [缺口 G-cd4a4aef3c784a18](../../evidence/gaps-sets-007.md#g-cd4a4aef3c784a18) · [参数 P-df88aa5f11f5e897](../../evidence/parameters-sets-017.md#p-df88aa5f11f5e897)

### path-025255

```text
(exec)# test platform software macsec rx sa lowest-pn <number:0..4294967295> an <number:0..3> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 37 `；EOL ` RVA 0x35ECC578 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 32 bit lowest packet number；` unsigned_number ` 0-3 association；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-7105535de97e2c74](../../evidence/conditions-sets-044.md#c-7105535de97e2c74) · [缺口 G-4ce08f20ba6e0a8c](../../evidence/gaps-sets-003.md#g-4ce08f20ba6e0a8c) · [参数 P-66fc7c05f2c52f4a](../../evidence/parameters-sets-008.md#p-66fc7c05f2c52f4a)

### path-025270

```text
(exec)# test platform software macsec rx sa set an <number:0..3> lowest-pn <number:0..4294967295> sak <string> length <number:0..4294967295> hash-key <string> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 36 `；EOL ` RVA 0x35ECBA68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0-3 association；` unsigned_number ` 32 bit packet number；` string ` pre shared key；` unsigned_number ` SAK length；` string ` hash key (128 bit or 16 character)；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-d1d829dcd87fe027](../../evidence/conditions-sets-081.md#c-d1d829dcd87fe027) · [缺口 G-7b52350f05401203](../../evidence/gaps-sets-005.md#g-7b52350f05401203) · [参数 P-2368a3845190d6fb](../../evidence/parameters-sets-003.md#p-2368a3845190d6fb)

### path-025257

```text
(exec)# test platform software macsec rx sc add mac-addr <address> vport <number:0..65535> mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 24 `；EOL ` RVA 0x35ECB248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` unsigned_number ` 16 bit port id；` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-0e6bd92af8426832](../../evidence/conditions-sets-006.md#c-0e6bd92af8426832) · [缺口 G-2c399004a64e4196](../../evidence/gaps-sets-002.md#g-2c399004a64e4196) · [参数 P-df797416e89fb5ac](../../evidence/parameters-sets-017.md#p-df797416e89fb5ac) · [状态效果 S-8626a3f37ae26685](../../evidence/state_effects-sets-028.md#s-8626a3f37ae26685)

### path-025272

```text
(exec)# test platform software macsec secy create cipher 128 offset none mac-addr <address> replay-enable no protect yes sci yes es yes scb yes validate-frames check <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 3 `；EOL ` RVA 0x35ECE5A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address。

[条件 C-e40dcde2f49087c9](../../evidence/conditions-sets-088.md#c-e40dcde2f49087c9) · [缺口 G-13cb7245c71a585f](../../evidence/gaps-sets-001.md#g-13cb7245c71a585f) · [参数 P-19758993ed4d3727](../../evidence/parameters-sets-002.md#p-19758993ed4d3727) · [状态效果 S-b8c3c5a0762a2361](../../evidence/state_effects-sets-039.md#s-b8c3c5a0762a2361)

### path-023493

```text
(exec)# test platform software macsec secy delete <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 2 `；EOL ` RVA 0x35ECEEA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-13faa8d577427700](../../evidence/conditions-sets-008.md#c-13faa8d577427700) · [缺口 G-fcdc387cad429372](../../evidence/gaps-sets-009.md#g-fcdc387cad429372) · [参数 P-860da46be79bd41a](../../evidence/parameters-sets-010.md#p-860da46be79bd41a)

### path-023508

```text
(exec)# test platform software macsec secy enable <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 1 `；EOL ` RVA 0x35ECF288 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6afde6a519ca5c8a](../../evidence/conditions-sets-041.md#c-6afde6a519ca5c8a) · [缺口 G-e29ca66b2e98b5a0](../../evidence/gaps-sets-008.md#g-e29ca66b2e98b5a0) · [参数 P-ba022531a42377d2](../../evidence/parameters-sets-014.md#p-ba022531a42377d2) · [状态效果 S-1a2c4ab58e6f50c9](../../evidence/state_effects-sets-006.md#s-1a2c4ab58e6f50c9)

### path-025232

```text
(exec)# test platform software macsec tag-clear-mode vlan-tag <number:0..65535> header-len <number:0..65535> header-etype <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 63 `；EOL ` RVA 0x35ECAB60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` number of vlans in the clear；` unsigned_number ` length of header；` unsigned_number ` length of header。

[条件 C-60b6ff363682ca8e](../../evidence/conditions-sets-038.md#c-60b6ff363682ca8e) · [缺口 G-d0ca0274cf2c33d2](../../evidence/gaps-sets-007.md#g-d0ca0274cf2c33d2) · [参数 P-0e6575adb123ccfc](../../evidence/parameters-sets-002.md#p-0e6575adb123ccfc)

### path-025123

```text
(exec)# test platform software macsec tx sa delete an <number:0..3> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 34 `；EOL ` RVA 0x35ECD950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` 0-3 association。

[条件 C-7efbc81e30e5bc5b](../../evidence/conditions-sets-049.md#c-7efbc81e30e5bc5b) · [缺口 G-e2ebf7c1f1a4d54d](../../evidence/gaps-sets-008.md#g-e2ebf7c1f1a4d54d) · [参数 P-b74f7ede1251bb1d](../../evidence/parameters-sets-014.md#p-b74f7ede1251bb1d)

### path-025271

```text
(exec)# test platform software macsec tx sa set mac-addr <address> vport <number:0..65535> an <number:0..3> pn <number:0..4294967295> confidence yes sak <string> length <number:0..4294967295> hash-key <string> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 33 `；EOL ` RVA 0x35ECD478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` unsigned_number ` &lt;0-65535&gt; 16 bit port id；` unsigned_number ` 0-3 association；` unsigned_number ` 32 bit packet number；` string ` pre shared key；` unsigned_number ` SAK length；` string ` hash key (128 bit or 16 character)。

[条件 C-d7bfb88fbf65979c](../../evidence/conditions-sets-083.md#c-d7bfb88fbf65979c) · [缺口 G-539fb1e95aa3965d](../../evidence/gaps-sets-003.md#g-539fb1e95aa3965d) · [参数 P-de9006aee71b5e11](../../evidence/parameters-sets-017.md#p-de9006aee71b5e11) · [状态效果 S-b4fcbf3f7cf3d4b5](../../evidence/state_effects-sets-038.md#s-b4fcbf3f7cf3d4b5)

### path-025233

```text
(exec)# test platform software macsec tx sc add mac-addr <address> vport <number:0..65535> <interface> <cr>
```

Handler ` RVA 0x160D7490 `；selector ` 23 `；EOL ` RVA 0x35ECCB90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address；` unsigned_number ` 16 bit port id。

[条件 C-0359a61fbb4fb086](../../evidence/conditions-sets-002.md#c-0359a61fbb4fb086) · [缺口 G-05038b7c1783bb47](../../evidence/gaps-sets-001.md#g-05038b7c1783bb47) · [参数 P-358e19e1a5cc21e5](../../evidence/parameters-sets-005.md#p-358e19e1a5cc21e5) · [状态效果 S-126eec8d24d35bf4](../../evidence/state_effects-sets-004.md#s-126eec8d24d35bf4)

### path-008252

```text
(exec)# test platform software multicast join <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 1 `；EOL ` RVA 0x3430E098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008265

```text
(exec)# test platform software multicast leave <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 2 `；EOL ` RVA 0x3430E340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-025187

```text
(exec)# test platform software multicast parameters in igmp <interface> <address> <address> <number:1..500000> <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 5 `；EOL ` RVA 0x3430D5D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv4 address for peer；` address ` Group IPv4 address；` unsigned_number ` grp count。

[条件 C-eed0defdd02c525e](../../evidence/conditions-sets-092.md#c-eed0defdd02c525e) · [缺口 G-c82d1ee6d0ed0a5c](../../evidence/gaps-sets-007.md#g-c82d1ee6d0ed0a5c) · [参数 P-494ffb635ff795f4](../../evidence/parameters-sets-006.md#p-494ffb635ff795f4) · [状态效果 S-562aba14b6f383b0](../../evidence/state_effects-sets-019.md#s-562aba14b6f383b0)

### path-025189

```text
(exec)# test platform software multicast parameters in mld <interface> <address> <address> <number:1..500000> <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 5 `；EOL ` RVA 0x3430DAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPv6 address for peer (must be linklocal address)；` address ` Group IPv6 address；` unsigned_number ` grp count。

[条件 C-8540d2deb429ddf8](../../evidence/conditions-sets-052.md#c-8540d2deb429ddf8) · [缺口 G-59bb43c19dc28393](../../evidence/gaps-sets-004.md#g-59bb43c19dc28393) · [参数 P-adde99e1afd051dd](../../evidence/parameters-sets-013.md#p-adde99e1afd051dd) · [状态效果 S-3d0d690d1367ef75](../../evidence/state_effects-sets-013.md#s-3d0d690d1367ef75)

### path-010524

```text
(exec)# test platform software multicast shim dynamic <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 9 `；EOL ` RVA 0x3430C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010528

```text
(exec)# test platform software multicast shim notdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 10 `；EOL ` RVA 0x3430CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010508

```text
(exec)# test platform software multicast shim off <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 6 `；EOL ` RVA 0x3430C2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010499

```text
(exec)# test platform software multicast shim on <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 7 `；EOL ` RVA 0x3430C018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010517

```text
(exec)# test platform software multicast shim sticky <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 8 `；EOL ` RVA 0x3430C568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-010536

```text
(exec)# test platform software multicast shim tdl <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 11 `；EOL ` RVA 0x3430CD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008231

```text
(exec)# test platform software multicast start <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 0 `；EOL ` RVA 0x3430DDF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008200

```text
(exec)# test platform software multicast status <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 4 `；EOL ` RVA 0x3430D028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008277

```text
(exec)# test platform software multicast stop <cr>
```

Handler ` RVA 0xE6FA7C0 `；selector ` 3 `；EOL ` RVA 0x3430E5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008134

```text
(exec)# test platform software peer timeout <cr>
```

Handler ` RVA 0xE9492B0 `；selector ` 0 `；EOL ` RVA 0x34350DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-768f0591ca6906dc](../../evidence/conditions-sets-046.md#c-768f0591ca6906dc)

### path-010606

```text
(exec)# test platform software plim qos class-map <cr>
```

Handler ` RVA 0xE93D510 `；selector ` 0 `；EOL ` RVA 0x3434D0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [状态效果 S-d381c20700bb0da3](../../evidence/state_effects-sets-045.md#s-d381c20700bb0da3)

### path-023464

```text
(exec)# test platform software plim qos interface <interface> <cr>
```

Handler ` RVA 0xE93D510 `；selector ` 0 `；EOL ` RVA 0x3434D0F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b59f71e3dbedf578](../../evidence/conditions-sets-070.md#c-b59f71e3dbedf578) · [缺口 G-9b5c1bcd71990603](../../evidence/gaps-sets-006.md#g-9b5c1bcd71990603) · [参数 P-add3fa87332fcad1](../../evidence/parameters-sets-013.md#p-add3fa87332fcad1) · [状态效果 S-4fad826b77658b91](../../evidence/state_effects-sets-017.md#s-4fad826b77658b91)

### path-024618

```text
(exec)# test platform software plim qos vlan-bmap-tbl subslot <?slotcard_func_action@5555898a15f0> <cr>
```

Handler ` RVA 0xE93D460 `；selector ` 0 `；EOL ` RVA 0x3434D630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [缺口 G-782fd99b1cee3216](../../evidence/gaps-sets-005.md#g-782fd99b1cee3216)

### path-008331

```text
(exec)# test platform software product-analytics fast-grace-period <cr>
```

Handler ` RVA 0x1658B060 `；selector ` 0 `；EOL ` RVA 0x35FA4068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-675816c748cdb369](../../evidence/conditions-sets-040.md#c-675816c748cdb369)

### path-008294

```text
(exec)# test platform software product-analytics sa-notify-false <cr>
```

Handler ` RVA 0x1658ADB0 `；selector ` 0 `；EOL ` RVA 0x35FA3B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5902331f63975401](../../evidence/conditions-sets-035.md#c-5902331f63975401)

### path-008310

```text
(exec)# test platform software product-analytics sa-notify-true <cr>
```

Handler ` RVA 0x1658AFD0 `；selector ` 0 `；EOL ` RVA 0x35FA3DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b5ff565f8fbf6b15](../../evidence/conditions-sets-070.md#c-b5ff565f8fbf6b15)

### path-008349

```text
(exec)# test platform software product-analytics timer <cr>
```

Handler ` RVA 0x1658B100 `；selector ` 0 `；EOL ` RVA 0x35FA4310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8ab9b7f5fa8c7370](../../evidence/conditions-sets-054.md#c-8ab9b7f5fa8c7370)

### path-008124

```text
(exec)# test platform software punt-keepalive ignore-fault <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 1 `；EOL ` RVA 0x3439C158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-008139

```text
(exec)# test platform software punt-keepalive trigger-failure <cr>
```

Handler ` RVA 0xEA60F20 `；selector ` 0 `；EOL ` RVA 0x3439C400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011954

```text
(exec)# test platform software qos statistics <number:1..50000> <number:1..100000> <number:1..100> <cr>
```

Handler ` RVA 0x10DA0020 `；selector ` 1 `；EOL ` RVA 0x34D1B8C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` dpidx from sh pl so dbidx swidb；` unsigned_number ` num queries；` unsigned_number ` num of query in parallel。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-65b36f41d2d9da61](../../evidence/parameters-sets-008.md#p-65b36f41d2d9da61)

### path-008207

```text
(exec)# test platform software redundancy use-vmac <cr>
```

Handler ` RVA 0x15A6EA80 `；selector ` 0 `；EOL ` RVA 0x35DE5530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011622

```text
(exec)# test platform software rg ar_alwys_dvrt <number:0..4> <number:0..12> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 7 `；EOL ` RVA 0x3432BC80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-4ffd42aa3d1d5e77](../../evidence/parameters-sets-007.md#p-4ffd42aa3d1d5e77)

### path-025248

```text
(exec)# test platform software rg interface <number:0..10> <interface> ar_intf <number:0..10> <address> <address> <number:0..10> <number:0..2048> <number:0..2048> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 9 `；EOL ` RVA 0x3432D688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id；` address ` IPv4 src address；` address ` IPv4 dst address；` unsigned_number ` l4 protocol；` unsigned_number ` src port；` unsigned_number ` dst port。

[条件 C-aed84341101a063f](../../evidence/conditions-sets-068.md#c-aed84341101a063f) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-34f8a15207b22a8f](../../evidence/parameters-sets-005.md#p-34f8a15207b22a8f)

### path-024598

```text
(exec)# test platform software rg interface <number:0..10> <interface> ar_vi_intf_assoc <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 8 `；EOL ` RVA 0x3432D248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action。

[条件 C-aed84341101a063f](../../evidence/conditions-sets-068.md#c-aed84341101a063f) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-2a7191613b999463](../../evidence/parameters-sets-004.md#p-2a7191613b999463)

### path-024957

```text
(exec)# test platform software rg interface <number:0..10> <interface> rg <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 4 `；EOL ` RVA 0x3432CCD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id。

[条件 C-aed84341101a063f](../../evidence/conditions-sets-068.md#c-aed84341101a063f) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-946f87fe654a121b](../../evidence/parameters-sets-011.md#p-946f87fe654a121b)

### path-024960

```text
(exec)# test platform software rg interface <number:0..10> <interface> rii <number:0..16000> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 6 `；EOL ` RVA 0x3432CFC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rii id。

[条件 C-aed84341101a063f](../../evidence/conditions-sets-068.md#c-aed84341101a063f) · [缺口 G-fee64ad37a0f2010](../../evidence/gaps-sets-009.md#g-fee64ad37a0f2010) · [参数 P-8caa816559fc637b](../../evidence/parameters-sets-011.md#p-8caa816559fc637b)

### path-011957

```text
(exec)# test platform software rg notify bulksync <number:0..10> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 2 `；EOL ` RVA 0x3432C378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` result。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-5e3b6cf8076791cc](../../evidence/parameters-sets-008.md#p-5e3b6cf8076791cc)

### path-012082

```text
(exec)# test platform software rg notify transport <number:0..10> <number:1..100000> <number:0..10> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 1 `；EOL ` RVA 0x3432C068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` rg id；` unsigned_number ` handler；` unsigned_number ` state。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-769bf5d82d2ae140](../../evidence/parameters-sets-009.md#p-769bf5d82d2ae140)

### path-012184

```text
(exec)# test platform software rg services parameters <number:0..10> <number:0..10> <number:0..10> <number:0..1> <number:0..1> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 0 `；EOL ` RVA 0x3432B938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` action；` unsigned_number ` rg id；` unsigned_number ` rg state；` unsigned_number ` transport request；` unsigned_number ` bulk sync request。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-7c5e56bce406174a](../../evidence/parameters-sets-010.md#p-7c5e56bce406174a)

### path-008351

```text
(exec)# test platform software rg tc-req <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 5 `；EOL ` RVA 0x3432D980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-012195

```text
(exec)# test platform software rg transport parameters <number:1..100000> <number:0..10> <address> <address> <number:0..10> <number:0..2048> <number:0..2048> <cr>
```

Handler ` RVA 0xE75D020 `；selector ` 3 `；EOL ` RVA 0x3432C860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handler；` unsigned_number ` application；` address ` IPv4 src address；` address ` IPv4 dst address；` unsigned_number ` l4 protocol；` unsigned_number ` src port；` unsigned_number ` dst port。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-82c662ee053c7586](../../evidence/parameters-sets-010.md#p-82c662ee053c7586)

### path-024592

```text
(exec)# test platform software shell command connection <number:dynamic> disconnect <cr>
```

Handler ` RVA 0xEB0CD80 `；selector ` 0 `；EOL ` RVA 0x343B1E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Connection number。

[条件 C-886abb14d2fa0a66](../../evidence/conditions-sets-053.md#c-886abb14d2fa0a66) · [缺口 G-1d711ad5d63397b8](../../evidence/gaps-sets-001.md#g-1d711ad5d63397b8) · [参数 P-71f354a74f64b80b](../../evidence/parameters-sets-009.md#p-71f354a74f64b80b)

### path-011966

```text
(exec)# test platform software shell command handler automore disable <cr>
```

Handler ` RVA 0xEB0C800 `；selector ` 0 `；EOL ` RVA 0x343B1310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011963

```text
(exec)# test platform software shell command handler automore manual <cr>
```

Handler ` RVA 0xEB0C900 `；selector ` 0 `；EOL ` RVA 0x343B1068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011641

```text
(exec)# test platform software shell command handler basic <cr>
```

Handler ` RVA 0xEB0C720 `；selector ` 0 `；EOL ` RVA 0x343B15A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011644

```text
(exec)# test platform software shell command handler null <cr>
```

Handler ` RVA 0xEB0C640 `；selector ` 0 `；EOL ` RVA 0x343B1850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011961

```text
(exec)# test platform software shell command handler output redirect <cr>
```

Handler ` RVA 0xEB0CA90 `；selector ` 0 `；EOL ` RVA 0x343B0D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011647

```text
(exec)# test platform software shell command handler space <cr>
```

Handler ` RVA 0xEB0C560 `；selector ` 0 `；EOL ` RVA 0x343B1AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011634

```text
(exec)# test platform software shell command set delete <cr>
```

Handler ` RVA 0xEB0CD30 `；selector ` 0 `；EOL ` RVA 0x343B0A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011633

```text
(exec)# test platform software shell command set load <cr>
```

Handler ` RVA 0xEB0CCE0 `；selector ` 0 `；EOL ` RVA 0x343B0760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-011589

```text
(exec)# test platform software stdout log running-config enable <cr>
```

Handler ` RVA 0xE950340 `；selector ` 0 `；EOL ` RVA 0x34351DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-171e533f08adcc33](../../evidence/conditions-sets-009.md#c-171e533f08adcc33) · [状态效果 S-7aa757f44819de9e](../../evidence/state_effects-sets-026.md#s-7aa757f44819de9e)

### path-010504

```text
(exec)# test platform software tdl ping rp <cr>
```

Handler ` RVA 0xE90CE60 `；selector ` 0 `；EOL ` RVA 0x343432E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41716d36e9f6688b](../../evidence/conditions-sets-026.md#c-41716d36e9f6688b) · [状态效果 S-1c7f5632423adad6](../../evidence/state_effects-sets-006.md#s-1c7f5632423adad6)

### path-011601

```text
(exec)# test platform software tdl ping rp stats <cr>
```

Handler ` RVA 0xE90F1B0 `；selector ` 0 `；EOL ` RVA 0x34343800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41716d36e9f6688b](../../evidence/conditions-sets-026.md#c-41716d36e9f6688b) · [状态效果 S-1c7f5632423adad6](../../evidence/state_effects-sets-006.md#s-1c7f5632423adad6)

### path-011934

```text
(exec)# test platform software tdl ping rp stats clear <cr>
```

Handler ` RVA 0xE90F090 `；selector ` 0 `；EOL ` RVA 0x343437D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41716d36e9f6688b](../../evidence/conditions-sets-026.md#c-41716d36e9f6688b) · [状态效果 S-1c7f5632423adad6](../../evidence/state_effects-sets-006.md#s-1c7f5632423adad6)

### path-023363

```text
(exec)# test platform software tdl ping subslot <?slotcard_func_action@555589897d40> <cr>
```

Handler ` RVA 0xE90CE60 `；selector ` 0 `；EOL ` RVA 0x343432E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-898ec82e7d0a5aae](../../evidence/conditions-sets-053.md#c-898ec82e7d0a5aae) · [缺口 G-217d0a7de67c3a33](../../evidence/gaps-sets-002.md#g-217d0a7de67c3a33) · [状态效果 S-70dd538f22425f46](../../evidence/state_effects-sets-024.md#s-70dd538f22425f46)

### path-024556

```text
(exec)# test platform software tdl ping subslot <?slotcard_func_action@555589897d40> stats <cr>
```

Handler ` RVA 0xE90F1B0 `；selector ` 0 `；EOL ` RVA 0x34343800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-898ec82e7d0a5aae](../../evidence/conditions-sets-053.md#c-898ec82e7d0a5aae) · [缺口 G-217d0a7de67c3a33](../../evidence/gaps-sets-002.md#g-217d0a7de67c3a33) · [状态效果 S-70dd538f22425f46](../../evidence/state_effects-sets-024.md#s-70dd538f22425f46)

### path-024928

```text
(exec)# test platform software tdl ping subslot <?slotcard_func_action@555589897d40> stats clear <cr>
```

Handler ` RVA 0xE90F090 `；selector ` 0 `；EOL ` RVA 0x343437D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-898ec82e7d0a5aae](../../evidence/conditions-sets-053.md#c-898ec82e7d0a5aae) · [缺口 G-217d0a7de67c3a33](../../evidence/gaps-sets-002.md#g-217d0a7de67c3a33) · [状态效果 S-70dd538f22425f46](../../evidence/state_effects-sets-024.md#s-70dd538f22425f46)

### path-024949

```text
(exec)# test platform software timestamp-engine oam y1731 default disable <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 3 `；EOL ` RVA 0x35DE75F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c51db39c7210292c](../../evidence/conditions-sets-076.md#c-c51db39c7210292c) · [缺口 G-a391e1e42775fa9f](../../evidence/gaps-sets-006.md#g-a391e1e42775fa9f) · [参数 P-5cde95e6de438324](../../evidence/parameters-sets-007.md#p-5cde95e6de438324)

### path-012083

```text
(exec)# test platform software timestamp-engine oam y1731 default disable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 4 `；EOL ` RVA 0x35DE78A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-84323e8725be7784](../../evidence/conditions-sets-051.md#c-84323e8725be7784)

### path-024948

```text
(exec)# test platform software timestamp-engine oam y1731 default enable <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 1 `；EOL ` RVA 0x35DE6FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-57f58e32415723db](../../evidence/conditions-sets-034.md#c-57f58e32415723db) · [缺口 G-00a913919e724e19](../../evidence/gaps-sets-001.md#g-00a913919e724e19) · [参数 P-1ccc1d5f4b9219b8](../../evidence/parameters-sets-003.md#p-1ccc1d5f4b9219b8)

### path-012080

```text
(exec)# test platform software timestamp-engine oam y1731 default enable all <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 2 `；EOL ` RVA 0x35DE7268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0a0f248ebabea68c](../../evidence/conditions-sets-004.md#c-0a0f248ebabea68c)

### path-025104

```text
(exec)# test platform software timestamp-engine ptp clock-domain <number:0..255> ip <address> <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 0 `；EOL ` RVA 0x35DE6B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` clk domain；` address ` IPv4 address。

[条件 C-0d82ec57f12e64ce](../../evidence/conditions-sets-005.md#c-0d82ec57f12e64ce) · [缺口 G-1fc38f152d5663e4](../../evidence/gaps-sets-002.md#g-1fc38f152d5663e4) · [参数 P-0c109254b97f8ff6](../../evidence/parameters-sets-001.md#p-0c109254b97f8ff6)

### path-025190

```text
(exec)# test platform software timestamp-engine tod load sec-hi <number:0..65535> sec-lo <number:0..4294967295> <interface> <cr>
```

Handler ` RVA 0x15A9EA30 `；selector ` 5 `；EOL ` RVA 0x35DE7DB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Upper 16 bits of seconds from epoch；` unsigned_number ` Upper 32 bits of seconds from epoch。

[条件 C-d33d87641bca01ea](../../evidence/conditions-sets-081.md#c-d33d87641bca01ea) · [缺口 G-40ae7ad6b9fdd093](../../evidence/gaps-sets-003.md#g-40ae7ad6b9fdd093) · [参数 P-33b87f8f71142462](../../evidence/parameters-sets-004.md#p-33b87f8f71142462)

### path-010582

```text
(exec)# test platform software uidp batch-count <number:0..1000> <cr>
```

Handler ` RVA 0x1599CE30 `；selector ` 0 `；EOL ` RVA 0x35DCF728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of user sessions per batch。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-7c336c4b98660031](../../evidence/parameters-sets-010.md#p-7c336c4b98660031)

### path-010577

```text
(exec)# test platform software uidp binding clear <cr>
```

Handler ` RVA 0x1599C3F0 `；selector ` 0 `；EOL ` RVA 0x35DCEE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980)

### path-012155

```text
(exec)# test platform software uidp binding ip-user add <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 0 `；EOL ` RVA 0x35DCE1B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-168aba61599d0180](../../evidence/parameters-sets-002.md#p-168aba61599d0180)

### path-012156

```text
(exec)# test platform software uidp binding ip-user delete <address> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x1599C4A0 `；selector ` 1 `；EOL ` RVA 0x35DCE4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address；` unsigned_number ` VPN ID；` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-82cd5055a6ddb96f](../../evidence/parameters-sets-010.md#p-82cd5055a6ddb96f)

### path-011968

```text
(exec)# test platform software uidp binding user-usergroup add <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 2 `；EOL ` RVA 0x35DCE8A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-12f4f3bbd76a04fe](../../evidence/parameters-sets-002.md#p-12f4f3bbd76a04fe)

### path-011969

```text
(exec)# test platform software uidp binding user-usergroup delete <string> <cr>
```

Handler ` RVA 0x1599C7F0 `；selector ` 3 `；EOL ` RVA 0x35DCEBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-1defe1bf1a446589](../../evidence/parameters-sets-003.md#p-1defe1bf1a446589)

### path-010585

```text
(exec)# test platform software uidp dwnld-timer <number:100..2000> <cr>
```

Handler ` RVA 0x1599CEA0 `；selector ` 0 `；EOL ` RVA 0x35DCF9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pause time for downloading batch of sessions。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-72b2461fd4b2a57e](../../evidence/parameters-sets-009.md#p-72b2461fd4b2a57e)

### path-021057

```text
(exec)# test platform software uidp load-file <url:dynamic> <cr>
```

Handler ` RVA 0x1599B640 `；selector ` 0 `；EOL ` RVA 0x35DCDD58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-53e23cf69e664667](../../evidence/conditions-sets-033.md#c-53e23cf69e664667) · [缺口 G-19dfe392d297c07f](../../evidence/gaps-sets-001.md#g-19dfe392d297c07f) · [参数 P-bdaadc3b21fb155e](../../evidence/parameters-sets-014.md#p-bdaadc3b21fb155e)

### path-010568

```text
(exec)# test platform software uidp user <string> <cr>
```

Handler ` RVA 0x1599CCD0 `；selector ` 4 `；EOL ` RVA 0x35DCF150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-0fa27b7ec79838bd](../../evidence/parameters-sets-002.md#p-0fa27b7ec79838bd)

### path-010574

```text
(exec)# test platform software uidp user-group <string> <cr>
```

Handler ` RVA 0x1599CD80 `；selector ` 5 `；EOL ` RVA 0x35DCF440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` User group name。

[条件 C-08887210fc1bc980](../../evidence/conditions-sets-004.md#c-08887210fc1bc980) · [参数 P-a9f2b7b5d4e2e4fa](../../evidence/parameters-sets-013.md#p-a9f2b7b5d4e2e4fa)

### path-011971

```text
(exec)# test platform software usb slot <number:1..4294967295> usbflash0 fake-remove <cr>
```

Handler ` RVA 0xE9C72A0 `；selector ` 0 `；EOL ` RVA 0x3437C7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot/switch Number。

[条件 C-ea27f0cd7abfbb35](../../evidence/conditions-sets-090.md#c-ea27f0cd7abfbb35) · [参数 P-8880f5ca265b7b86](../../evidence/parameters-sets-011.md#p-8880f5ca265b7b86) · [状态效果 S-d67598f454582624](../../evidence/state_effects-sets-045.md#s-d67598f454582624)

### path-002418

```text
(exec)# test pm <string> <cr>
```

Handler ` RVA 0x15DD1600 `；selector ` 0 `；EOL ` RVA 0x35E22898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ...。

[条件 C-8b704234a4206d3d](../../evidence/conditions-sets-054.md#c-8b704234a4206d3d) · [参数 P-bc02e5e87b3d0fdc](../../evidence/parameters-sets-014.md#p-bc02e5e87b3d0fdc)

### path-018931

```text
(exec)# test pm error <interface> none <cr>
```

Handler ` RVA 0x15DD1740 `；selector ` 0 `；EOL ` RVA 0x35E22170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc0d974dab311c87](../../evidence/conditions-sets-097.md#c-fc0d974dab311c87) · [缺口 G-e7c06410305acf2f](../../evidence/gaps-sets-008.md#g-e7c06410305acf2f) · [参数 P-f52bb39e2fab6521](../../evidence/parameters-sets-018.md#p-f52bb39e2fab6521) · [状态效果 S-29bd35e11acdc175](../../evidence/state_effects-sets-009.md#s-29bd35e11acdc175)

### path-006002

```text
(exec)# test policy-manager appl-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b246bbfb40a9cba1](../../evidence/conditions-sets-069.md#c-b246bbfb40a9cba1) · [状态效果 S-47c93f26f9589f3a](../../evidence/state_effects-sets-016.md#s-47c93f26f9589f3a)

### path-006030

```text
(exec)# test policy-manager wd-timer-event create <cr>
```

Handler ` RVA 0xE110C00 `；selector ` 0 `；EOL ` RVA 0x34205F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43b1e6628be5a68e](../../evidence/conditions-sets-026.md#c-43b1e6628be5a68e) · [状态效果 S-f81a6c5679c38450](../../evidence/state_effects-sets-053.md#s-f81a6c5679c38450)

### path-016816

```text
(exec)# test ppp packet <interface> <string> <cr>
```

Handler ` RVA 0xFEDEDA0 `；selector ` 0 `；EOL ` RVA 0x34909C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2bebc712f81fe995](../../evidence/conditions-sets-017.md#c-2bebc712f81fe995) · [缺口 G-639070fd7e588553](../../evidence/gaps-sets-004.md#g-639070fd7e588553) · [参数 P-35b51fbb7a8e5629](../../evidence/parameters-sets-005.md#p-35b51fbb7a8e5629)

### path-016806

```text
(exec)# test ppp packet <interface> echo <cr>
```

Handler ` RVA 0xFEDEDA0 `；selector ` 1 `；EOL ` RVA 0x34909930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a57547df10dd6b7b](../../evidence/conditions-sets-064.md#c-a57547df10dd6b7b) · [缺口 G-639070fd7e588553](../../evidence/gaps-sets-004.md#g-639070fd7e588553) · [参数 P-d6f9f077cb6da492](../../evidence/parameters-sets-016.md#p-d6f9f077cb6da492)

### path-012170

```text
(exec)# test pppatm subscriber delay <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <number:0..30000> <cr>
```

Handler ` RVA 0x1111E220 `；selector ` 0 `；EOL ` RVA 0x35401D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` msecs. for subscriber msgs；` unsigned_number ` msecs. for ppp msgs；` unsigned_number ` msecs. for peer msgs；` unsigned_number ` msecs. for feature msgs；` unsigned_number ` msecs. for incoming calls；` unsigned_number ` msecs. for vaccess。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-9a76ee1c5bfa38c4](../../evidence/parameters-sets-012.md#p-9a76ee1c5bfa38c4) · [状态效果 S-31d1bbfdcf890b34](../../evidence/state_effects-sets-011.md#s-31d1bbfdcf890b34)

### path-021785

```text
(exec)# test pppatm subscriber normal interface <interface> <cr>
```

Handler ` RVA 0x1111E220 `；selector ` 0 `；EOL ` RVA 0x35401D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41ffe58e1bf224a4](../../evidence/conditions-sets-026.md#c-41ffe58e1bf224a4) · [缺口 G-51fba122ca367221](../../evidence/gaps-sets-003.md#g-51fba122ca367221) · [参数 P-b9f7c416d8d36dab](../../evidence/parameters-sets-014.md#p-b9f7c416d8d36dab) · [状态效果 S-b019afe18c5266af](../../evidence/state_effects-sets-037.md#s-b019afe18c5266af)

### path-000278

```text
(exec)# test pppoe <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 0 `；EOL ` RVA 0x356B32E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-f0634c39047c00de](../../evidence/state_effects-sets-051.md#s-f0634c39047c00de)

### path-012560

```text
(exec)# test pppoe <number:dynamic> <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 0 `；EOL ` RVA 0x356B32E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number of PPPoE sessions to be opened。

[条件 C-e9dd7d1768271008](../../evidence/conditions-sets-090.md#c-e9dd7d1768271008) · [缺口 G-b33c5386ae50588d](../../evidence/gaps-sets-006.md#g-b33c5386ae50588d) · [参数 P-cb85bb7f12418403](../../evidence/parameters-sets-015.md#p-cb85bb7f12418403) · [状态效果 S-f0634c39047c00de](../../evidence/state_effects-sets-051.md#s-f0634c39047c00de)

### path-005428

```text
(exec)# test pppoe init-session-num <number:1..65535> <cr>
```

Handler ` RVA 0x11CB06C0 `；selector ` 12 `；EOL ` RVA 0x356B3650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Starting PPPoE Session Number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-465592a267d1213c](../../evidence/parameters-sets-006.md#p-465592a267d1213c) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-009075

```text
(exec)# test pppoe session <number:1..20000> autogrant <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 2 `；EOL ` RVA 0x356B48A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011059

```text
(exec)# test pppoe session <number:1..20000> autogrant on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 1 `；EOL ` RVA 0x356B45F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011067

```text
(exec)# test pppoe session <number:1..20000> grant-threshold <number:0..65534> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 6 `；EOL ` RVA 0x356B56E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set grant credit unit threshold 。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-c52715e3f07536be](../../evidence/parameters-sets-015.md#p-c52715e3f07536be) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-009063

```text
(exec)# test pppoe session <number:1..20000> headDropping <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 16 `；EOL ` RVA 0x356B3D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011053

```text
(exec)# test pppoe session <number:1..20000> headDropping on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 15 `；EOL ` RVA 0x356B3AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-009067

```text
(exec)# test pppoe session <number:1..20000> inband-credits <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 14 `；EOL ` RVA 0x356B42F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011056

```text
(exec)# test pppoe session <number:1..20000> inband-credits on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 13 `；EOL ` RVA 0x356B4050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011077

```text
(exec)# test pppoe session <number:1..20000> local-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 10 `；EOL ` RVA 0x356B5CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credits。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-1eb21824c744cc30](../../evidence/parameters-sets-003.md#p-1eb21824c744cc30) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011063

```text
(exec)# test pppoe session <number:1..20000> max-grant <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 5 `；EOL ` RVA 0x356B53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Set maximum number of credit units per grant。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-513dc72ce2a78132](../../evidence/parameters-sets-007.md#p-513dc72ce2a78132) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011069

```text
(exec)# test pppoe session <number:1..20000> padg <number:1..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 7 `；EOL ` RVA 0x356B50F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` Number of PPPoE credit units to grant。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-18fe21eb467de39c](../../evidence/parameters-sets-002.md#p-18fe21eb467de39c) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011064

```text
(exec)# test pppoe session <number:1..20000> padg off <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 3 `；EOL ` RVA 0x356B4E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011060

```text
(exec)# test pppoe session <number:1..20000> padg on <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 4 `；EOL ` RVA 0x356B4BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-011105

```text
(exec)# test pppoe session <number:1..20000> padq receive-only <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 8 `；EOL ` RVA 0x356B6218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b01c122e4339bfe](../../evidence/parameters-sets-010.md#p-7b01c122e4339bfe) · [状态效果 S-64361701001367e5](../../evidence/state_effects-sets-021.md#s-64361701001367e5)

### path-011072

```text
(exec)# test pppoe session <number:1..20000> peer-credits <number:0..65535> <cr>
```

Handler ` RVA 0x11CB0650 `；selector ` 9 `；EOL ` RVA 0x356B59D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` PPPoE Session Number to touch；` unsigned_number ` local credit units。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-cec15d709fc4fb0a](../../evidence/parameters-sets-016.md#p-cec15d709fc4fb0a) · [状态效果 S-cc103376ec8d66b4](../../evidence/state_effects-sets-043.md#s-cc103376ec8d66b4)

### path-010458

```text
(exec)# test process create <number:1..5000> <number:1..10000> <number:1..5000> <cr>
```

Handler ` RVA 0xD6D2550 `；selector ` 0 `；EOL ` RVA 0x33ECDDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter time to run for (ms)；` unsigned_number ` Enter time to sleep for (ms)；` unsigned_number ` Enter time to susp after (ms)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f57e4b11ecf3ba88](../../evidence/parameters-sets-018.md#p-f57e4b11ecf3ba88)

### path-004341

```text
(exec)# test process kill <number:1..4294967295> <cr>
```

Handler ` RVA 0xD6D2A10 `；selector ` 0 `；EOL ` RVA 0x33ECE140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pid to kill。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-cca3915cfbc7547d](../../evidence/parameters-sets-016.md#p-cca3915cfbc7547d)

### path-000298

```text
(exec)# test rfd <cr>
```

Handler ` RVA 0xD7C53C0 `；selector ` 0 `；EOL ` RVA 0x33EF4C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f5abec7b990c5a9](../../evidence/conditions-sets-006.md#c-0f5abec7b990c5a9)

### path-008953

```text
(exec)# test rib application create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 5 `；EOL ` RVA 0x3400B460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Application instance name。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [参数 P-44a7689de98431a1](../../evidence/parameters-sets-006.md#p-44a7689de98431a1)

### path-008940

```text
(exec)# test rib application delete <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 6 `；EOL ` RVA 0x3400B198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [参数 P-84485f3ce4166b87](../../evidence/parameters-sets-010.md#p-84485f3ce4166b87)

### path-008915

```text
(exec)# test rib client create <string> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 0 `；EOL ` RVA 0x34009A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-6fbb31bff7eebb42](../../evidence/parameters-sets-009.md#p-6fbb31bff7eebb42)

### path-008866

```text
(exec)# test rib client delete <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 1 `；EOL ` RVA 0x34009758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-61bebf93f1ef1e6e](../../evidence/parameters-sets-008.md#p-61bebf93f1ef1e6e)

### path-008970

```text
(exec)# test rib firsthop <address> <number:0..65535> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 7 `；EOL ` RVA 0x3400AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` destination address；` unsigned_number ` Multipath path select index。

[条件 C-8e1ea9b8464e5b80](../../evidence/conditions-sets-055.md#c-8e1ea9b8464e5b80) · [参数 P-adbd895aad18df4d](../../evidence/parameters-sets-013.md#p-adbd895aad18df4d)

### path-021709

```text
(exec)# test rib firsthop <address> <number:0..65535> <interface> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 7 `；EOL ` RVA 0x3400AE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` destination address；` unsigned_number ` Multipath path select index。

[条件 C-ed96c74c6ccc9b54](../../evidence/conditions-sets-092.md#c-ed96c74c6ccc9b54) · [缺口 G-f83c84aa036ace52](../../evidence/gaps-sets-009.md#g-f83c84aa036ace52) · [参数 P-e378a7c7d30f8d22](../../evidence/parameters-sets-017.md#p-e378a7c7d30f8d22)

### path-025358

```text
(exec)# test rib route delete <number:1..2147483647> <?router_action_proc_vpn@55558955e160> <interface> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 2 `；EOL ` RVA 0x3400A250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-5b0146db028d56f6](../../evidence/conditions-sets-036.md#c-5b0146db028d56f6) · [缺口 G-de012a9bc4214c67](../../evidence/gaps-sets-008.md#g-de012a9bc4214c67) · [参数 P-be2bb44230acb3b7](../../evidence/parameters-sets-014.md#p-be2bb44230acb3b7)

### path-008918

```text
(exec)# test rib route show <number:1..2147483647> <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 3 `；EOL ` RVA 0x3400A550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` handle number。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [参数 P-8d99215107ac3986](../../evidence/parameters-sets-011.md#p-8d99215107ac3986)

### path-008930

```text
(exec)# test rib table set forwarding-base <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 4 `；EOL ` RVA 0x3400A950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6591baf7ee82edc1](../../evidence/conditions-sets-039.md#c-6591baf7ee82edc1) · [状态效果 S-85d7c878968893ac](../../evidence/state_effects-sets-028.md#s-85d7c878968893ac)

### path-001463

```text
(exec)# test rib ut <cr>
```

Handler ` RVA 0xDC0CAC0 `；selector ` 8 `；EOL ` RVA 0x34009DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b1badac532a448c4](../../evidence/conditions-sets-069.md#c-b1badac532a448c4)

### path-009274

```text
(exec)# test rmi create user-type <string> <cr>
```

Handler ` RVA 0xE081680 `；selector ` 0 `；EOL ` RVA 0x341D60C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Resource User-Type Name。

[条件 C-632c0786f9acbf2f](../../evidence/conditions-sets-038.md#c-632c0786f9acbf2f) · [参数 P-71c7f62eb30da67d](../../evidence/parameters-sets-009.md#p-71c7f62eb30da67d) · [状态效果 S-b30c4043dec4bc98](../../evidence/state_effects-sets-038.md#s-b30c4043dec4bc98)

### path-002287

```text
(exec)# test rmi entphyind <cr>
```

Handler ` RVA 0xD695F20 `；selector ` 0 `；EOL ` RVA 0x341D7518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-012032

```text
(exec)# test rmon hc-alarms <number:1..65535> Low32bitvalue <number:0..4294967295> High32bitvalue <number:0..4294967295> <cr>
```

Handler ` RVA 0xC4F9D90 `；selector ` 0 `；EOL ` RVA 0x33AADCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hc alarm index；` unsigned_number ` Low32bitvalue；` unsigned_number ` High32bitvalue。

[条件 C-2fad28d0f75b0dcd](../../evidence/conditions-sets-019.md#c-2fad28d0f75b0dcd) · [参数 P-88ec7857607f280e](../../evidence/parameters-sets-011.md#p-88ec7857607f280e)

### path-024753

```text
(exec)# test rsvp lockout psb <number:0..4294967295> set interface <interface> <cr>
```

Handler ` RVA 0x10078C60 `；selector ` 0 `；EOL ` RVA 0x34A3F910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` PSB handle for lockout in hex。

[条件 C-7087820412fb37c8](../../evidence/conditions-sets-043.md#c-7087820412fb37c8) · [缺口 G-678b1c17d3c60157](../../evidence/gaps-sets-004.md#g-678b1c17d3c60157) · [参数 P-a7e66a588bfa8991](../../evidence/parameters-sets-013.md#p-a7e66a588bfa8991) · [状态效果 S-7ee53137f06a3ee8](../../evidence/state_effects-sets-027.md#s-7ee53137f06a3ee8)

### path-012118

```text
(exec)# test rsvp metadata forward <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <cr>
```

Handler ` RVA 0x100784A0 `；selector ` 0 `；EOL ` RVA 0x34A3F398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port。

[条件 C-41f80aa269af6c7b](../../evidence/conditions-sets-026.md#c-41f80aa269af6c7b) · [参数 P-164d4baefc6af40a](../../evidence/parameters-sets-002.md#p-164d4baefc6af40a) · [状态效果 S-c81e6c8294e69fb0](../../evidence/state_effects-sets-042.md#s-c81e6c8294e69fb0)

### path-005345

```text
(exec)# test rsvp nsr disable <cr>
```

Handler ` RVA 0x10078B00 `；selector ` 0 `；EOL ` RVA 0x34A3ED00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005339

```text
(exec)# test rsvp nsr enable <cr>
```

Handler ` RVA 0x100789F0 `；selector ` 0 `；EOL ` RVA 0x34A3EA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005332

```text
(exec)# test rsvp nsr incr <cr>
```

Handler ` RVA 0x100788E0 `；selector ` 0 `；EOL ` RVA 0x34A3E7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005321

```text
(exec)# test rsvp nsr start <cr>
```

Handler ` RVA 0x100787C0 `；selector ` 0 `；EOL ` RVA 0x34A3E508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-012202

```text
(exec)# test rsvp transport send path <address> <address> <number:0..255> <number:0..65535> <number:0..65535> <number:1..65535> <address> <number:1..65535> data <string> <cr>
```

Handler ` RVA 0x1005D100 `；selector ` 0 `；EOL ` RVA 0x34A3DFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination address；` address ` Source address；` unsigned_number ` IP Protocol；` unsigned_number ` Destination port；` unsigned_number ` Source port；` unsigned_number ` Client Identifier；` address ` Initiator Id；` unsigned_number ` Instance Id；` string ` RSVP Transport message。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-c024f648c9188b95](../../evidence/parameters-sets-015.md#p-c024f648c9188b95) · [状态效果 S-1bddcd302179039b](../../evidence/state_effects-sets-006.md#s-1bddcd302179039b)

### path-006431

```text
(exec)# test rtty <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xCC38580 `；selector ` 0 `；EOL ` RVA 0x33C237D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Remote Seat ID(in hexadecimal)；` string ` Command String。

[条件 C-38a2391f4af8366c](../../evidence/conditions-sets-022.md#c-38a2391f4af8366c) · [参数 P-87096cdef34360d5](../../evidence/parameters-sets-010.md#p-87096cdef34360d5)

### path-006503

```text
(exec)# test rtty statistics disable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 0 `；EOL ` RVA 0x33C23D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3775814f8e22baa](../../evidence/conditions-sets-075.md#c-c3775814f8e22baa)

### path-006467

```text
(exec)# test rtty statistics enable <cr>
```

Handler ` RVA 0xCC382E0 `；selector ` 1 `；EOL ` RVA 0x33C23A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7290dc6daf97f920](../../evidence/conditions-sets-044.md#c-7290dc6daf97f920)

### path-006529

```text
(exec)# test rtty statistics print <cr>
```

Handler ` RVA 0xCC38340 `；selector ` 0 `；EOL ` RVA 0x33C23FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3f789b060de15d04](../../evidence/conditions-sets-025.md#c-3f789b060de15d04)

### path-011863

```text
(exec)# test sasl client ip <address> port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 1 `；EOL ` RVA 0x34B14C98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-0a6a0a313046b956](../../evidence/parameters-sets-001.md#p-0a6a0a313046b956)

### path-012133

```text
(exec)# test sasl client ip <address> port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 2 `；EOL ` RVA 0x34B14F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for outgoing connection；` unsigned_number ` Port value for outgoing connection；` string ` SASL profile name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f6b83400a54cfc55](../../evidence/parameters-sets-018.md#p-f6b83400a54cfc55)

### path-009634

```text
(exec)# test sasl server port <number:0..65535> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 3 `；EOL ` RVA 0x34B153F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port value for SASL listening。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f5808002237e59f6](../../evidence/parameters-sets-018.md#p-f5808002237e59f6)

### path-011861

```text
(exec)# test sasl server port <number:0..65535> profile <string> <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 4 `；EOL ` RVA 0x34B156E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port value for SASL listening；` string ` SASL profile name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7fbae1e202e71069](../../evidence/parameters-sets-010.md#p-7fbae1e202e71069)

### path-006569

```text
(exec)# test sasl server stop <cr>
```

Handler ` RVA 0x103D1180 `；selector ` 5 `；EOL ` RVA 0x34B15978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-000581

```text
(exec)# test save snapshot <cr>
```

Handler ` RVA 0xD6D2B10 `；selector ` 0 `；EOL ` RVA 0x33ECE430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005223

```text
(exec)# test scheduler trash edisms <cr>
```

Handler ` RVA 0xD7A41D0 `；selector ` 0 `；EOL ` RVA 0x33EEE678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-17b5add80072111f](../../evidence/conditions-sets-009.md#c-17b5add80072111f) · [状态效果 S-0f7b3431a198baaf](../../evidence/state_effects-sets-004.md#s-0f7b3431a198baaf)

### path-001055

```text
(exec)# test scheduler watched-message <cr>
```

Handler ` RVA 0xD79FA20 `；selector ` 0 `；EOL ` RVA 0x33EED500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5026f314b64ffa47](../../evidence/conditions-sets-031.md#c-5026f314b64ffa47) · [状态效果 S-bba3a7167bf2a7b9](../../evidence/state_effects-sets-040.md#s-bba3a7167bf2a7b9)

### path-005201

```text
(exec)# test sctp association create <cr>
```

Handler ` RVA 0xCE848E0 `；selector ` 0 `；EOL ` RVA 0x33D12C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001408

```text
(exec)# test sctp delete <cr>
```

Handler ` RVA 0xCE84E80 `；selector ` 0 `；EOL ` RVA 0x33D12690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-005187

```text
(exec)# test sctp instance create <cr>
```

Handler ` RVA 0xCE828C0 `；selector ` 0 `；EOL ` RVA 0x33D12308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008825

```text
(exec)# test sctp instance delete <number:1..65535> <cr>
```

Handler ` RVA 0xCE847D0 `；selector ` 0 `；EOL ` RVA 0x33D12668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Local port of instance to delete。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-b7f8a9d96e4fa6a8](../../evidence/parameters-sets-014.md#p-b7f8a9d96e4fa6a8)

### path-008920

```text
(exec)# test sctp parameters burstsize <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 8 `；EOL ` RVA 0x33D0FE28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets to burst。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-5f332658bcc3b1ba](../../evidence/parameters-sets-008.md#p-5f332658bcc3b1ba)

### path-011044

```text
(exec)# test sctp parameters congabate <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 17 `；EOL ` RVA 0x33D11C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Congestion level to define abate value；` unsigned_number ` Value for congestion abate。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-6e3b56e35279f34e](../../evidence/parameters-sets-009.md#p-6e3b56e35279f34e)

### path-009004

```text
(exec)# test sctp parameters conglevels <number:0..3> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 15 `；EOL ` RVA 0x33D115A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of congestion levels to define。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-90dac4eb92412f64](../../evidence/parameters-sets-011.md#p-90dac4eb92412f64)

### path-011040

```text
(exec)# test sctp parameters congonset <number:1..3> <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 16 `；EOL ` RVA 0x33D118E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Congestion level to define onset value；` unsigned_number ` Value for congestion onset。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-07fdbf832d65708c](../../evidence/parameters-sets-001.md#p-07fdbf832d65708c)

### path-008931

```text
(exec)# test sctp parameters delay <number:0..60000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 9 `；EOL ` RVA 0x33D10118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay (msecs) between bursts。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-a85ef6772e443ce4](../../evidence/parameters-sets-013.md#p-a85ef6772e443ce4)

### path-005397

```text
(exec)# test sctp parameters display <cr>
```

Handler ` RVA 0xCE6FC00 `；selector ` 0 `；EOL ` RVA 0x33D11EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-008857

```text
(exec)# test sctp parameters fixedparams <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 4 `；EOL ` RVA 0x33D0F268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Use fixed params (FALSE=0/TRUE=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-148bb4a30eac7147](../../evidence/parameters-sets-002.md#p-148bb4a30eac7147)

### path-008942

```text
(exec)# test sctp parameters hbenabled <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 10 `；EOL ` RVA 0x33D10408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Heartbeat dest addrs (FALSE=0/TRUE=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-acd27b8447a1b688](../../evidence/parameters-sets-013.md#p-acd27b8447a1b688)

### path-008954

```text
(exec)# test sctp parameters hbtimeout <number:0..600000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 11 `；EOL ` RVA 0x33D106F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Heartbeat timer value。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-001bdbe6024b7fc0](../../evidence/parameters-sets-001.md#p-001bdbe6024b7fc0)

### path-008807

```text
(exec)# test sctp parameters instreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 1 `；EOL ` RVA 0x33D0E998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of inbound streams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f60c7b1ad05500ca](../../evidence/parameters-sets-018.md#p-f60c7b1ad05500ca)

### path-008984

```text
(exec)# test sctp parameters maxRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 13 `；EOL ` RVA 0x33D10FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max retrans timer value (ms)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-656c5afea3fc72ab](../../evidence/parameters-sets-008.md#p-656c5afea3fc72ab)

### path-008905

```text
(exec)# test sctp parameters maxoutstand <number:0..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 7 `；EOL ` RVA 0x33D0FB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of packets outstanding。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-565a162e37a45ac2](../../evidence/parameters-sets-007.md#p-565a162e37a45ac2)

### path-008885

```text
(exec)# test sctp parameters maxpackets <number:0..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 6 `；EOL ` RVA 0x33D0F848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of packets to send (9999=inf)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-7b10493dc6084a57](../../evidence/parameters-sets-010.md#p-7b10493dc6084a57)

### path-008841

```text
(exec)# test sctp parameters maxpdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 3 `；EOL ` RVA 0x33D0EF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-0cff93470ff98b66](../../evidence/parameters-sets-001.md#p-0cff93470ff98b66)

### path-008973

```text
(exec)# test sctp parameters minRTO <number:300..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 12 `；EOL ` RVA 0x33D10CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Min retrans timer value (ms)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f7c8c4e77b4b985e](../../evidence/parameters-sets-018.md#p-f7c8c4e77b4b985e)

### path-008795

```text
(exec)# test sctp parameters outstreams <number:1..1024> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 0 `；EOL ` RVA 0x33D0E6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of outbound streams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-71ac10a0fbb6fc04](../../evidence/parameters-sets-009.md#p-71ac10a0fbb6fc04)

### path-008826

```text
(exec)# test sctp parameters pdusize <number:4..10000> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 2 `；EOL ` RVA 0x33D0EC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Pdu size of test dgrams。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-6fa3fc9c170f9a06](../../evidence/parameters-sets-009.md#p-6fa3fc9c170f9a06)

### path-008996

```text
(exec)# test sctp parameters rcvwin <number:1500..65535> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 14 `；EOL ` RVA 0x33D112B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Local receive window value (bytes)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-ac176c644c368388](../../evidence/parameters-sets-013.md#p-ac176c644c368388)

### path-008963

```text
(exec)# test sctp parameters testtype <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 18 `；EOL ` RVA 0x33D109E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Test type (SIMPLE=0/LOOPREQ=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-ed32cc90492c4587](../../evidence/parameters-sets-018.md#p-ed32cc90492c4587)

### path-008868

```text
(exec)# test sctp parameters usealladdrs <number:0..1> <cr>
```

Handler ` RVA 0xCE81EE0 `；selector ` 5 `；EOL ` RVA 0x33D0F558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Use all dest addrs (FALSE=0/TRUE=1)?。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-64b63411945a3011](../../evidence/parameters-sets-008.md#p-64b63411945a3011)

### path-005927

```text
(exec)# test sdb add <string> <cr>
```

Handler ` RVA 0xDEC82E0 `；selector ` 0 `；EOL ` RVA 0x34093138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-5c1d0be0e07d0031](../../evidence/parameters-sets-007.md#p-5c1d0be0e07d0031)

### path-005955

```text
(exec)# test sdb remove <string> <cr>
```

Handler ` RVA 0xDEC8430 `；selector ` 0 `；EOL ` RVA 0x34093420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-5c6127879750809b](../../evidence/parameters-sets-007.md#p-5c6127879750809b)

### path-005980

```text
(exec)# test sdb search <string> <cr>
```

Handler ` RVA 0xDEC8550 `；selector ` 0 `；EOL ` RVA 0x340936E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-427368a9e0878d44](../../evidence/parameters-sets-006.md#p-427368a9e0878d44)

### path-005250

```text
(exec)# test service-overlay application register <cr>
```

Handler ` RVA 0x108F5810 `；selector ` 1 `；EOL ` RVA 0x34BF7E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca3239a195954f20](../../evidence/conditions-sets-078.md#c-ca3239a195954f20) · [状态效果 S-f53eafa2319505a9](../../evidence/state_effects-sets-052.md#s-f53eafa2319505a9)

### path-011054

```text
(exec)# test service-routing api debug <number:0..4294967295> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 17 `；EOL ` RVA 0x34B2F8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Debug flags。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-fc2096c688c2da52](../../evidence/parameters-sets-019.md#p-fc2096c688c2da52)

### path-012211

```text
(exec)# test service-routing api publish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:1..4294967295> <number:0..32768> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 21 `；EOL ` RVA 0x34B2E0F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Service-sequence；` unsigned_number ` Service-size。

[条件 C-8fe40725bca2e0f1](../../evidence/conditions-sets-056.md#c-8fe40725bca2e0f1) · [参数 P-bbe7af018acbc6ac](../../evidence/parameters-sets-014.md#p-bbe7af018acbc6ac)

### path-009027

```text
(exec)# test service-routing api register-client <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 24 `；EOL ` RVA 0x34B2D520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client context。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-c58be6cbdbca42b7](../../evidence/parameters-sets-015.md#p-c58be6cbdbca42b7)

### path-011043

```text
(exec)# test service-routing api register-client <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 23 `；EOL ` RVA 0x34B2D4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client context；` string ` Client name。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-28a8a8d90e5fc0a1](../../evidence/parameters-sets-004.md#p-28a8a8d90e5fc0a1)

### path-012210

```text
(exec)# test service-routing api subscribe-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <number:0..255> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 19 `；EOL ` RVA 0x34B2F088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` Maximum-paths。

[条件 C-481470e3392e4e91](../../evidence/conditions-sets-028.md#c-481470e3392e4e91) · [参数 P-7447444ab7796741](../../evidence/parameters-sets-009.md#p-7447444ab7796741)

### path-012207

```text
(exec)# test service-routing api unpublish-service <number:1..4294967295> <number:0..65535> : <number:0..65535> : <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> . <number:0..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 20 `；EOL ` RVA 0x34B2E898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance；` unsigned_number ` (A:B:X-X-X-X-X) Service:Sub-Service:Instance。

[条件 C-a2427361eb345980](../../evidence/conditions-sets-063.md#c-a2427361eb345980) · [参数 P-6205f9bccb319166](../../evidence/parameters-sets-008.md#p-6205f9bccb319166)

### path-009024

```text
(exec)# test service-routing api unregister-client <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 22 `；EOL ` RVA 0x34B2DA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-fd4fdd18c511da0a](../../evidence/parameters-sets-019.md#p-fd4fdd18c511da0a)

### path-011050

```text
(exec)# test service-routing api unsubscribe-service <number:1..4294967295> <number:1..4294967295> <cr>
```

Handler ` RVA 0x10452690 `；selector ` 18 `；EOL ` RVA 0x34B2F598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service-Routing sf-client handle；` unsigned_number ` Subscription handle。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-ea16afa033846cd9](../../evidence/parameters-sets-018.md#p-ea16afa033846cd9)

### path-005367

```text
(exec)# test service-routing api version <cr>
```

Handler ` RVA 0x10452690 `；selector ` 25 `；EOL ` RVA 0x34B2D1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b)

### path-012022

```text
(exec)# test service-routing capabilities-manager api register <string> <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Component；` string ` Capability；` string ` Capability Data。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-2cd42d186cef97f3](../../evidence/parameters-sets-004.md#p-2cd42d186cef97f3) · [状态效果 S-fec3b990618a13ed](../../evidence/state_effects-sets-054.md#s-fec3b990618a13ed)

### path-011773

```text
(exec)# test service-routing capabilities-manager api unregister <string> <string> <cr>
```

Handler ` RVA 0x1045B700 `；selector ` 80 `；EOL ` RVA 0x34B34A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Component；` string ` Capability。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-ca371a52bc56aa69](../../evidence/parameters-sets-015.md#p-ca371a52bc56aa69)

### path-009015

```text
(exec)# test service-routing capabilities-manager api version <cr>
```

Handler ` RVA 0x1045B660 `；selector ` 79 `；EOL ` RVA 0x34B34CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b)

### path-011772

```text
(exec)# test service-routing xmcp client <number:0..4294967295> error-response <number:100..699> <cr>
```

Handler ` RVA 0x10472C70 `；selector ` 56 `；EOL ` RVA 0x34B37C48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Client handle；` unsigned_number ` Error code。

[条件 C-3a6355524661c11b](../../evidence/conditions-sets-023.md#c-3a6355524661c11b) · [参数 P-82ab05eb296bdede](../../evidence/parameters-sets-010.md#p-82ab05eb296bdede)

### path-025141

```text
(exec)# test session-mgr <interface> client-id <number:1..255> mac <address> mlist <string> dot1x <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B96F08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enter a value between 1 and 255；` address ` MAC address；` string ` Name of authentication method list。

[条件 C-24c7f4760d219b92](../../evidence/conditions-sets-014.md#c-24c7f4760d219b92) · [缺口 G-2cf92449e95aad04](../../evidence/gaps-sets-002.md#g-2cf92449e95aad04) · [参数 P-d0d17b1f4f9abc7d](../../evidence/parameters-sets-016.md#p-d0d17b1f4f9abc7d) · [状态效果 S-29b9d060da859073](../../evidence/state_effects-sets-009.md#s-29b9d060da859073)

### path-013727

```text
(exec)# test session-mgr <interface> fips <cr>
```

Handler ` RVA 0xCAFC7F0 `；selector ` 0 `；EOL ` RVA 0x33BAFBA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-24c7f4760d219b92](../../evidence/conditions-sets-014.md#c-24c7f4760d219b92) · [缺口 G-2cf92449e95aad04](../../evidence/gaps-sets-002.md#g-2cf92449e95aad04) · [参数 P-11ec98d89dbdd7bc](../../evidence/parameters-sets-002.md#p-11ec98d89dbdd7bc) · [状态效果 S-0b8a720970847dd4](../../evidence/state_effects-sets-003.md#s-0b8a720970847dd4)

### path-005224

```text
(exec)# test session-mgr acct-stats start <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [状态效果 S-7fed9bc76f543a70](../../evidence/state_effects-sets-027.md#s-7fed9bc76f543a70)

### path-008883

```text
(exec)# test session-mgr cga-remote-auth authc <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [参数 P-da2f08bdc200c03c](../../evidence/parameters-sets-016.md#p-da2f08bdc200c03c) · [状态效果 S-900d60f708847ff4](../../evidence/state_effects-sets-031.md#s-900d60f708847ff4)

### path-010995

```text
(exec)# test session-mgr crimson table mab create <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [状态效果 S-ecb6492cbf1653d5](../../evidence/state_effects-sets-050.md#s-ecb6492cbf1653d5)

### path-012000

```text
(exec)# test session-mgr event send async start handle <number:1..4294967295> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B96910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Handle value。

[条件 C-de0a4b74d86f6344](../../evidence/conditions-sets-086.md#c-de0a4b74d86f6344) · [参数 P-96568601ab7c7b37](../../evidence/parameters-sets-012.md#p-96568601ab7c7b37) · [状态效果 S-b871db46c6d3541a](../../evidence/state_effects-sets-039.md#s-b871db46c6d3541a)

### path-008917

```text
(exec)# test session-mgr fqdn-epm-notify <number:1..4294967295> <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Handle value；` address ` IP address to notify。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [参数 P-d0e66e8ab24af0c2](../../evidence/parameters-sets-016.md#p-d0e66e8ab24af0c2) · [状态效果 S-b4b0fd02401d9f02](../../evidence/state_effects-sets-038.md#s-b4b0fd02401d9f02)

### path-005319

```text
(exec)# test session-mgr green create <cr>
```

Handler ` RVA 0xCAD3E50 `；selector ` 0 `；EOL ` RVA 0x33B99460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [状态效果 S-143acbc32cf32bd5](../../evidence/state_effects-sets-005.md#s-143acbc32cf32bd5)

### path-012018

```text
(exec)# test session-mgr identity mac <address> add ip <address> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B9A048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address；` address ` IP address。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [参数 P-bb158b26fcbfa514](../../evidence/parameters-sets-014.md#p-bb158b26fcbfa514) · [状态效果 S-35da208c62e1d82d](../../evidence/state_effects-sets-012.md#s-35da208c62e1d82d)

### path-025038

```text
(exec)# test session-mgr session push mac <address> <interface> source switch-pi <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B9A950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` MAC address。

[条件 C-acb84273e5626acd](../../evidence/conditions-sets-067.md#c-acb84273e5626acd) · [缺口 G-6ed41314c5e36b64](../../evidence/gaps-sets-004.md#g-6ed41314c5e36b64) · [参数 P-e04940707f210ada](../../evidence/parameters-sets-017.md#p-e04940707f210ada) · [状态效果 S-f9c7f483d49844e5](../../evidence/state_effects-sets-053.md#s-f9c7f483d49844e5)

### path-005208

```text
(exec)# test session-mgr sm-client register <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [状态效果 S-6693d1cb603d6ce2](../../evidence/state_effects-sets-022.md#s-6693d1cb603d6ce2)

### path-021616

```text
(exec)# test session-mgr spi server start <interface> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B97480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-95fa7b7ee8853a6b](../../evidence/conditions-sets-058.md#c-95fa7b7ee8853a6b) · [缺口 G-6b745a88bd4ac37d](../../evidence/gaps-sets-004.md#g-6b745a88bd4ac37d) · [参数 P-8cbb6dd19a760537](../../evidence/parameters-sets-011.md#p-8cbb6dd19a760537) · [状态效果 S-fe62bcbcd92586db](../../evidence/state_effects-sets-054.md#s-fe62bcbcd92586db)

### path-011752

```text
(exec)# test session-mgr test-vlan <string> <number:1..4095> <number:1..4> <number:1..1000> <cr>
```

Handler ` RVA 0xCAF8B40 `；selector ` 0 `；EOL ` RVA 0x33B98808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the vlan group；` unsigned_number ` Value of the vlan；` unsigned_number ` 1 to add any other value to remove；` unsigned_number ` Number of users。

[条件 C-4c8d5440f97c91e1](../../evidence/conditions-sets-030.md#c-4c8d5440f97c91e1) · [参数 P-8f6fc02bc311139a](../../evidence/parameters-sets-011.md#p-8f6fc02bc311139a) · [状态效果 S-e75d6793d04b6387](../../evidence/state_effects-sets-049.md#s-e75d6793d04b6387)

### path-005116

```text
(exec)# test snmp cpu-stats start <cr>
```

Handler ` RVA 0xCC7C220 `；selector ` 0 `；EOL ` RVA 0x33C3C500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7f320a5aecb2b08](../../evidence/conditions-sets-090.md#c-e7f320a5aecb2b08) · [状态效果 S-f4d7e5e55472229d](../../evidence/state_effects-sets-052.md#s-f4d7e5e55472229d)

### path-005234

```text
(exec)# test snmp trap config-copy <cr>
```

Handler ` RVA 0x104C05D0 `；selector ` 41 `；EOL ` RVA 0x33C3C888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-36a5f3afb4745d3a](../../evidence/state_effects-sets-012.md#s-36a5f3afb4745d3a)

### path-008604

```text
(exec)# test ssm asynchronous throttling print <cr>
```

Handler ` RVA 0x10433590 `；selector ` 0 `；EOL ` RVA 0x34B25118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-3a61c248e707209e](../../evidence/state_effects-sets-013.md#s-3a61c248e707209e)

### path-004832

```text
(exec)# test ssm counters enable <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B23798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-69b2b59a33516be5](../../evidence/state_effects-sets-023.md#s-69b2b59a33516be5)

### path-010648

```text
(exec)# test ssm fcdb nosupport <number:1..25> <number:0..2> <cr>
```

Handler ` RVA 0x104365F0 `；selector ` 0 `；EOL ` RVA 0x34B23BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` feature type；` unsigned_number ` nosupport action (0=ignore, 1=punt, 2=teardown seg)。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-23be321c29567b35](../../evidence/parameters-sets-003.md#p-23be321c29567b35) · [状态效果 S-cf8fc4968c01daef](../../evidence/state_effects-sets-044.md#s-cf8fc4968c01daef)

### path-004955

```text
(exec)# test ssm feature status <cr>
```

Handler ` RVA 0x10435390 `；selector ` 0 `；EOL ` RVA 0x34B24850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-e5e9542ef187aa88](../../evidence/state_effects-sets-049.md#s-e5e9542ef187aa88)

### path-008517

```text
(exec)# test ssm repop <number:1..14> <number:0..2> <cr>
```

Handler ` RVA 0x104331B0 `；selector ` 0 `；EOL ` RVA 0x34B234A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` switch type : 1-AC/AC, 2-AC/ATOM, 3-AC/L2TP, 4-AC/VFI, 5-VFI/AToM, 6-VFI/L2TP, 7-All；` unsigned_number ` segment class type : 1-SSS, 2-HW, 3-ALL。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-53f05257c23695ba](../../evidence/parameters-sets-007.md#p-53f05257c23695ba)

### path-008572

```text
(exec)# test ssm segment lock <number:1..4294967295> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` segment id。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-921027c1fa5afe65](../../evidence/parameters-sets-011.md#p-921027c1fa5afe65) · [状态效果 S-5cb4ab1443ed41da](../../evidence/state_effects-sets-020.md#s-5cb4ab1443ed41da)

### path-010661

```text
(exec)# test ssm segment support enable <number:1..41> <cr>
```

Handler ` RVA 0x104332C0 `；selector ` 0 `；EOL ` RVA 0x34B24110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` segment type value。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-35adb604690ed821](../../evidence/parameters-sets-005.md#p-35adb604690ed821) · [状态效果 S-95d70024c13b5a87](../../evidence/state_effects-sets-032.md#s-95d70024c13b5a87)

### path-011679

```text
(exec)# test subscriber feature accounting accuracy throttling print <cr>
```

Handler ` RVA 0x1093B5A0 `；selector ` 0 `；EOL ` RVA 0x34C06558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d87bd9cfcbfa1377](../../evidence/conditions-sets-083.md#c-d87bd9cfcbfa1377) · [状态效果 S-6ca47ab626381bd9](../../evidence/state_effects-sets-023.md#s-6ca47ab626381bd9)

### path-010714

```text
(exec)# test subscriber feature timer acceleration enable <cr>
```

Handler ` RVA 0x1093F020 `；selector ` 0 `；EOL ` RVA 0x34C06130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9dda1e763caecc9c](../../evidence/conditions-sets-061.md#c-9dda1e763caecc9c) · [状态效果 S-4479d06006e3f543](../../evidence/state_effects-sets-015.md#s-4479d06006e3f543)

### path-010827

```text
(exec)# test subscriber policy account-logon session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-06651ce7f985b3d5](../../evidence/conditions-sets-003.md#c-06651ce7f985b3d5) · [参数 P-a89542a0c784be09](../../evidence/parameters-sets-013.md#p-a89542a0c784be09) · [状态效果 S-d02d5ea6eab34a7a](../../evidence/state_effects-sets-044.md#s-d02d5ea6eab34a7a)

### path-010740

```text
(exec)# test subscriber policy condition-map <string> <string> <cr>
```

Handler ` RVA 0x10A59C40 `；selector ` 0 `；EOL ` RVA 0x34C749F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The condition map to be tested for equality；` string ` The condition map to be used as the identifier source。

[条件 C-b4ffff23a5042390](../../evidence/conditions-sets-070.md#c-b4ffff23a5042390) · [参数 P-10987eb1655aac27](../../evidence/parameters-sets-002.md#p-10987eb1655aac27)

### path-005020

```text
(exec)# test subscriber policy dummy <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93d2a17b5dec9b02](../../evidence/conditions-sets-057.md#c-93d2a17b5dec9b02) · [状态效果 S-8e1a14ebde532c3d](../../evidence/state_effects-sets-030.md#s-8e1a14ebde532c3d)

### path-012192

```text
(exec)# test subscriber policy epd accounting-req start session-guid <string> epd-flow-id <number:0..32> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE8A740 `；selector ` 0 `；EOL ` RVA 0x34C53288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter ISG Session GUID；` unsigned_number ` Enter EPD Flow Id；` address ` Enter EPD Device IP Address。

[条件 C-4763399528953cb2](../../evidence/conditions-sets-028.md#c-4763399528953cb2) · [参数 P-c12bb31bafc45042](../../evidence/parameters-sets-015.md#p-c12bb31bafc45042) · [状态效果 S-2687138c0d0af5b5](../../evidence/state_effects-sets-009.md#s-2687138c0d0af5b5)

### path-012196

```text
(exec)# test subscriber policy epd conn_mgmt-query version <string> command <string> peer-ip <address> keepalive <number:0..3600> <cr>
```

Handler ` RVA 0xFE89ED0 `；selector ` 0 `；EOL ` RVA 0x34C54440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Version string, only "1.0" is valid；` string ` Command string (establish, disestablish, keepalive)；` address ` IP address of the peer；` unsigned_number ` keepalive value(0 not to send)。

[条件 C-bbcb2e42ba704f3c](../../evidence/conditions-sets-073.md#c-bbcb2e42ba704f3c) · [参数 P-528cd97ddb37152d](../../evidence/parameters-sets-007.md#p-528cd97ddb37152d) · [状态效果 S-20b9a77afb9d9608](../../evidence/state_effects-sets-007.md#s-20b9a77afb9d9608)

### path-011994

```text
(exec)# test subscriber policy epd conn_mgmt-ses-test <number:1..2> <number:0..30> <string> <cr>
```

Handler ` RVA 0xFE89E20 `；selector ` 0 `；EOL ` RVA 0x34C547F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 1 - to add, 2 to remove；` unsigned_number ` conn id ；` string ` session guid string  。

[条件 C-cec82ced6be4ec31](../../evidence/conditions-sets-080.md#c-cec82ced6be4ec31) · [参数 P-2f90b406a6098bc7](../../evidence/parameters-sets-004.md#p-2f90b406a6098bc7)

### path-012165

```text
(exec)# test subscriber policy epd handler coa-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F1A0 `；selector ` 0 `；EOL ` RVA 0x34C537B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-1e7275fc08b650dd](../../evidence/conditions-sets-012.md#c-1e7275fc08b650dd) · [参数 P-69204721b34e1501](../../evidence/parameters-sets-008.md#p-69204721b34e1501)

### path-012166

```text
(exec)# test subscriber policy epd handler disconnect-request epd-ipaddress <address> attr-list <string> <cr>
```

Handler ` RVA 0xFE7F290 `；selector ` 0 `；EOL ` RVA 0x34C53B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Enter Session IP Address；` string ` Attribute list name。

[条件 C-d6c38bbd31ca6fde](../../evidence/conditions-sets-083.md#c-d6c38bbd31ca6fde) · [参数 P-c47ed38e510f496d](../../evidence/parameters-sets-015.md#p-c47ed38e510f496d)

### path-010820

```text
(exec)# test subscriber policy epd handler stop <cr>
```

Handler ` RVA 0xFE7ECD0 `；selector ` 0 `；EOL ` RVA 0x34C53E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1dfdb0194b9ea2d6](../../evidence/conditions-sets-012.md#c-1dfdb0194b9ea2d6)

### path-011988

```text
(exec)# test subscriber policy epd session-mgmt-req activate-policy-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A1B0 `；selector ` 0 `；EOL ` RVA 0x34C52850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-200ceed63b6498f6](../../evidence/conditions-sets-012.md#c-200ceed63b6498f6) · [参数 P-ef7400e9df8d5866](../../evidence/parameters-sets-018.md#p-ef7400e9df8d5866) · [状态效果 S-099eaa182cb854b4](../../evidence/state_effects-sets-002.md#s-099eaa182cb854b4)

### path-012102

```text
(exec)# test subscriber policy epd session-query-req session-ipaddress <address> epd-ipaddress <address> <cr>
```

Handler ` RVA 0xFE89C40 `；selector ` 0 `；EOL ` RVA 0x34C52328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Enter ISG Session IP Address；` address ` Enter EPD Device IP Address。

[条件 C-72b61c76aa8a7e5d](../../evidence/conditions-sets-044.md#c-72b61c76aa8a7e5d) · [参数 P-995339be86ea8070](../../evidence/parameters-sets-012.md#p-995339be86ea8070)

### path-011688

```text
(exec)# test subscriber policy epd session-terminate-req session-handle <number:0..4294967295> <cr>
```

Handler ` RVA 0xFE8A610 `；selector ` 0 `；EOL ` RVA 0x34C52DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter ISG Session Handle。

[条件 C-47af2e91d2f4da8b](../../evidence/conditions-sets-028.md#c-47af2e91d2f4da8b) · [参数 P-bfaf933945c5acf1](../../evidence/parameters-sets-015.md#p-bfaf933945c5acf1)

### path-010884

```text
(exec)# test subscriber policy insert circuit-id <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C575A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Circuit Id to be inserted for testing, enter "none" to disable。

[条件 C-efa0088ed9ef5241](../../evidence/conditions-sets-093.md#c-efa0088ed9ef5241) · [参数 P-01f789955e639dbf](../../evidence/parameters-sets-001.md#p-01f789955e639dbf) · [状态效果 S-c591367e41c346e9](../../evidence/state_effects-sets-042.md#s-c591367e41c346e9)

### path-024672

```text
(exec)# test subscriber policy mlpbundle-req bundle <?general_pointer_number_action@55558a1a9ec0> session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` First MLP link Subscriber Service Switch session id value。

[条件 C-548463a6ece321f8](../../evidence/conditions-sets-033.md#c-548463a6ece321f8) · [缺口 G-683891788f0963a2](../../evidence/gaps-sets-004.md#g-683891788f0963a2) · [参数 P-0aba5c74a4fe1221](../../evidence/parameters-sets-001.md#p-0aba5c74a4fe1221) · [状态效果 S-c70ef454a62d9f6d](../../evidence/state_effects-sets-042.md#s-c70ef454a62d9f6d)

### path-010783

```text
(exec)# test subscriber policy mlplink-added session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MLP link Subscriber Service Switch session id value。

[条件 C-e973006d32405abe](../../evidence/conditions-sets-090.md#c-e973006d32405abe) · [参数 P-eca3557bd67d1f82](../../evidence/parameters-sets-018.md#p-eca3557bd67d1f82) · [状态效果 S-73f6a28f3809a0a9](../../evidence/state_effects-sets-025.md#s-73f6a28f3809a0a9)

### path-012164

```text
(exec)# test subscriber policy policy-client session <number:0..4294967295> client Radius-Proxy event start <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C550E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-e8a69ba24f434aeb](../../evidence/conditions-sets-090.md#c-e8a69ba24f434aeb) · [参数 P-43db9ec51cad8b99](../../evidence/parameters-sets-006.md#p-43db9ec51cad8b99) · [状态效果 S-3a41ef9adf887bca](../../evidence/state_effects-sets-013.md#s-3a41ef9adf887bca)

### path-010868

```text
(exec)# test subscriber policy send-session-log session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-5ec07cd416f9fcdd](../../evidence/conditions-sets-037.md#c-5ec07cd416f9fcdd) · [参数 P-2db34b641405b555](../../evidence/parameters-sets-004.md#p-2db34b641405b555) · [状态效果 S-8557de7f7ebf1dfa](../../evidence/state_effects-sets-028.md#s-8557de7f7ebf1dfa)

### path-008642

```text
(exec)# test subscriber policy service-profile-download <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C54BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` service profile key name。

[条件 C-adb4c1b45a70ee9a](../../evidence/conditions-sets-067.md#c-adb4c1b45a70ee9a) · [参数 P-6e2772433acac708](../../evidence/parameters-sets-009.md#p-6e2772433acac708) · [状态效果 S-83f6166564a12019](../../evidence/state_effects-sets-028.md#s-83f6166564a12019)

### path-011998

```text
(exec)# test subscriber policy service-start session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-fef27d83fbb9a421](../../evidence/conditions-sets-098.md#c-fef27d83fbb9a421) · [参数 P-9a05bf3f9bba2324](../../evidence/parameters-sets-012.md#p-9a05bf3f9bba2324) · [状态效果 S-1c1a4372ac42c3c5](../../evidence/state_effects-sets-006.md#s-1c1a4372ac42c3c5)

### path-011997

```text
(exec)# test subscriber policy service-stop session <number:0..4294967295> name <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` Service name to download。

[条件 C-9fae708052294c4a](../../evidence/conditions-sets-062.md#c-9fae708052294c4a) · [参数 P-51e8af1a53cec40c](../../evidence/parameters-sets-007.md#p-51e8af1a53cec40c) · [状态效果 S-d60129153db124b3](../../evidence/state_effects-sets-045.md#s-d60129153db124b3)

### path-010809

```text
(exec)# test subscriber policy session-deactivated session <number:0..4294967295> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C56310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value。

[条件 C-72e4ae20c2fc54a9](../../evidence/conditions-sets-044.md#c-72e4ae20c2fc54a9) · [参数 P-806442e5184ce743](../../evidence/parameters-sets-010.md#p-806442e5184ce743) · [状态效果 S-5f0d3c138cc40554](../../evidence/state_effects-sets-020.md#s-5f0d3c138cc40554)

### path-005036

```text
(exec)# test subscriber policy tcsession-req <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C55830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d57c69eee85e66b](../../evidence/conditions-sets-018.md#c-2d57c69eee85e66b) · [状态效果 S-8ec437709aa8d536](../../evidence/state_effects-sets-030.md#s-8ec437709aa8d536)

### path-012002

```text
(exec)# test subscriber policy update session <number:0..4294967295> attr-list <string> <cr>
```

Handler ` RVA 0x109D50A0 `；selector ` 0 `；EOL ` RVA 0x34C57AD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Subscriber Service Switch session id value；` string ` AAA attribute list name。

[条件 C-e18801909d3aaabf](../../evidence/conditions-sets-087.md#c-e18801909d3aaabf) · [参数 P-2dc1c4b05030fe7a](../../evidence/parameters-sets-004.md#p-2dc1c4b05030fe7a) · [状态效果 S-9e1f302198979395](../../evidence/state_effects-sets-034.md#s-9e1f302198979395)

### path-017459

```text
(exec)# test sw-vlan pruning <interface> status <cr>
```

Handler ` RVA 0x15C8FDA0 `；selector ` 0 `；EOL ` RVA 0x35DFEA50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7316d08a2218b577](../../evidence/conditions-sets-045.md#c-7316d08a2218b577) · [缺口 G-b6b9b1ce41a2f5ca](../../evidence/gaps-sets-006.md#g-b6b9b1ce41a2f5ca) · [参数 P-9cb2e20eebfd85fa](../../evidence/parameters-sets-012.md#p-9cb2e20eebfd85fa) · [状态效果 S-3bae861e7fb22031](../../evidence/state_effects-sets-013.md#s-3bae861e7fb22031)

### path-004985

```text
(exec)# test sw-vlan show data <cr>
```

Handler ` RVA 0x15C8E860 `；selector ` 0 `；EOL ` RVA 0x35DFE5A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e371a26ff3529e46](../../evidence/conditions-sets-088.md#c-e371a26ff3529e46) · [状态效果 S-4fecd803dab9cd21](../../evidence/state_effects-sets-017.md#s-4fecd803dab9cd21)

### path-005548

```text
(exec)# test system secure db <cr>
```

Handler ` RVA 0xE031AB0 `；selector ` 0 `；EOL ` RVA 0x3416FBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-0188aeb898ae4796](../../evidence/state_effects-sets-001.md#s-0188aeb898ae4796)

### path-000225

```text
(exec)# test tcp delay <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 2 `；EOL ` RVA 0x33CF79B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-5c20245c40e38ef4](../../evidence/conditions-sets-036.md#c-5c20245c40e38ef4) · [参数 P-dbbc7c51a2581030](../../evidence/parameters-sets-017.md#p-dbbc7c51a2581030)

### path-000221

```text
(exec)# test tcp drop <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 1 `；EOL ` RVA 0x33CF7978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-8f3facb558df6ea2](../../evidence/conditions-sets-055.md#c-8f3facb558df6ea2) · [参数 P-9905a3044e6cc7c3](../../evidence/parameters-sets-012.md#p-9905a3044e6cc7c3)

### path-000227

```text
(exec)# test tcp line <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 0 `；EOL ` RVA 0x33CF7C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-b91d82a80754ef06](../../evidence/conditions-sets-071.md#c-b91d82a80754ef06) · [参数 P-168d315b78b62806](../../evidence/parameters-sets-002.md#p-168d315b78b62806)

### path-000229

```text
(exec)# test tcp random <number:0..2147483647> <cr>
```

Handler ` RVA 0xCDFACC0 `；selector ` 3 `；EOL ` RVA 0x33CF7EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number。

[条件 C-a6b91ffd578c2532](../../evidence/conditions-sets-064.md#c-a6b91ffd578c2532) · [参数 P-d316af619bb90043](../../evidence/parameters-sets-016.md#p-d316af619bb90043)

### path-011785

```text
(exec)# test template scope global <string> bind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 0 `；EOL ` RVA 0x33ED94B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af)

### path-011788

```text
(exec)# test template scope global <string> unbind dynamic <cr>
```

Handler ` RVA 0xD6DF7A0 `；selector ` 1 `；EOL ` RVA 0x33ED9780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-635b9257d1a441af](../../evidence/parameters-sets-008.md#p-635b9257d1a441af)

### path-025046

```text
(exec)# test template scope interface <string> bind dynamic interface <interface> <cr>
```

Handler ` RVA 0xD6D9FC0 `；selector ` 0 `；EOL ` RVA 0x33ED8370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-2340fceaaf76b4a0](../../evidence/conditions-sets-014.md#c-2340fceaaf76b4a0) · [缺口 G-43f87bfb76bc1d11](../../evidence/gaps-sets-003.md#g-43f87bfb76bc1d11) · [参数 P-ddaa6dab3e069515](../../evidence/parameters-sets-017.md#p-ddaa6dab3e069515)

### path-012120

```text
(exec)# test template scope interface <string> bind static merge interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 2 `；EOL ` RVA 0x33ED86E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-b1fd3797155aba51](../../evidence/conditions-sets-069.md#c-b1fd3797155aba51) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5)

### path-012122

```text
(exec)# test template scope interface <string> bind static replace interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 3 `；EOL ` RVA 0x33ED89B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-b1fd3797155aba51](../../evidence/conditions-sets-069.md#c-b1fd3797155aba51) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5)

### path-025047

```text
(exec)# test template scope interface <string> unbind dynamic interface <interface> <cr>
```

Handler ` RVA 0xD6D9FC0 `；selector ` 1 `；EOL ` RVA 0x33ED8DE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Template name。

[条件 C-839671409cf07f1a](../../evidence/conditions-sets-051.md#c-839671409cf07f1a) · [缺口 G-4c77652b9cce4e73](../../evidence/gaps-sets-003.md#g-4c77652b9cce4e73) · [参数 P-192ef1b35ceca6e4](../../evidence/parameters-sets-002.md#p-192ef1b35ceca6e4)

### path-012028

```text
(exec)# test template scope interface <string> unbind static interface-global <cr>
```

Handler ` RVA 0xD6DAD60 `；selector ` 4 `；EOL ` RVA 0x33ED90F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name。

[条件 C-b1fd3797155aba51](../../evidence/conditions-sets-069.md#c-b1fd3797155aba51) · [参数 P-e9b79b38c71467c5](../../evidence/parameters-sets-017.md#p-e9b79b38c71467c5)

### path-024774

```text
(exec)# test template scope interface apply common-config interface <interface> <cr>
```

Handler ` RVA 0xD6DAEC0 `；selector ` 1 `；EOL ` RVA 0x33ED7B70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-22d2a6526b0265b7](../../evidence/conditions-sets-014.md#c-22d2a6526b0265b7) · [缺口 G-bbb78dbe26e32634](../../evidence/gaps-sets-007.md#g-bbb78dbe26e32634) · [参数 P-09e959048d046c6b](../../evidence/parameters-sets-001.md#p-09e959048d046c6b)

### path-011079

```text
(exec)# test template scope interface nvgen interface-global <cr>
```

Handler ` RVA 0xD6DAF30 `；selector ` 0 `；EOL ` RVA 0x33ED7EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-001668

```text
(exec)# test tenant-mgr disable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35849178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0aaa69a59207310](../../evidence/conditions-sets-074.md#c-c0aaa69a59207310) · [状态效果 S-58f9eaa42e5aefbe](../../evidence/state_effects-sets-019.md#s-58f9eaa42e5aefbe)

### path-001649

```text
(exec)# test tenant-mgr enable-cfg <cr>
```

Handler ` RVA 0x123E7200 `；selector ` 0 `；EOL ` RVA 0x35848EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0aaa69a59207310](../../evidence/conditions-sets-074.md#c-c0aaa69a59207310) · [状态效果 S-7f027ca8be9fd236](../../evidence/state_effects-sets-027.md#s-7f027ca8be9fd236)

### path-004743

```text
(exec)# test timer-wheel process create <cr>
```

Handler ` RVA 0xD7AC900 `；selector ` 0 `；EOL ` RVA 0x33EEEF30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-298ec59a9772bd58](../../evidence/conditions-sets-016.md#c-298ec59a9772bd58) · [状态效果 S-b2c8022a0687eb2a](../../evidence/state_effects-sets-038.md#s-b2c8022a0687eb2a)

### path-001104

```text
(exec)# test topology clients <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 11 `；EOL ` RVA 0x33FE4560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004931

```text
(exec)# test topology create ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 1 `；EOL ` RVA 0x33FE5EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d7c11cfa6860d7e](../../evidence/conditions-sets-042.md#c-6d7c11cfa6860d7e) · [状态效果 S-f7048065acb0e89e](../../evidence/state_effects-sets-052.md#s-f7048065acb0e89e)

### path-004911

```text
(exec)# test topology delete ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 7 `；EOL ` RVA 0x33FE5A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d7c11cfa6860d7e](../../evidence/conditions-sets-042.md#c-6d7c11cfa6860d7e) · [状态效果 S-3f86f4ca5c7841e0](../../evidence/state_effects-sets-014.md#s-3f86f4ca5c7841e0)

### path-004884

```text
(exec)# test topology lookup ipv6 <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 2 `；EOL ` RVA 0x33FE53D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [状态效果 S-56ec032430ccb72f](../../evidence/state_effects-sets-019.md#s-56ec032430ccb72f)

### path-001144

```text
(exec)# test topology walk <cr>
```

Handler ` RVA 0xDB76190 `；selector ` 14 `；EOL ` RVA 0x33FE4B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46f8604fe47e8e34](../../evidence/conditions-sets-028.md#c-46f8604fe47e8e34)

### path-010662

```text
(exec)# test track map name <string> create <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 1 `；EOL ` RVA 0x34216BB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked object string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c)

### path-010697

```text
(exec)# test track map name <string> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 5 `；EOL ` RVA 0x34217100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked object string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c)

### path-010680

```text
(exec)# test track map name <string> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 2 `；EOL ` RVA 0x34216E58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked object string。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-f066051966eee05c](../../evidence/parameters-sets-018.md#p-f066051966eee05c)

### path-010695

```text
(exec)# test track map num <number:1..32767> del <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 4 `；EOL ` RVA 0x342176D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685)

### path-010674

```text
(exec)# test track map num <number:1..32767> get <cr>
```

Handler ` RVA 0xE14F560 `；selector ` 3 `；EOL ` RVA 0x34217430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Track number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-57c3eb8779535685](../../evidence/parameters-sets-007.md#p-57c3eb8779535685)

### path-008530

```text
(exec)# test track service <string> up <cr>
```

Handler ` RVA 0xE14F670 `；selector ` 0 `；EOL ` RVA 0x34216180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tracked service name。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-8b58f3bab75800c0](../../evidence/parameters-sets-011.md#p-8b58f3bab75800c0) · [状态效果 S-391eac7ba8a34ad6](../../evidence/state_effects-sets-013.md#s-391eac7ba8a34ad6)

### path-001082

```text
(exec)# test track white-box <cr>
```

Handler ` RVA 0xE14F7A0 `；selector ` 0 `；EOL ` RVA 0x34215DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-51ab530bbb573823](../../evidence/conditions-sets-032.md#c-51ab530bbb573823)

### path-024027

```text
(exec)# test trunkgroup <?show_tg_cmd@55558ce57570> preemption-pending flash-override data <number:1..2147483647> <cr>
```

Handler ` RVA 0x1E3C1110 `；selector ` 1 `；EOL ` RVA 0x37903B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Call Reference Id。

[条件 C-61fc7098854f5914](../../evidence/conditions-sets-038.md#c-61fc7098854f5914) · [缺口 G-3c24b5e558ad4dc0](../../evidence/gaps-sets-003.md#g-3c24b5e558ad4dc0) · [参数 P-accf59baec26636a](../../evidence/parameters-sets-013.md#p-accf59baec26636a) · [状态效果 S-868f122b8fa6027a](../../evidence/state_effects-sets-029.md#s-868f122b8fa6027a)

### path-018231

```text
(exec)# test trunkgroup <?show_tg_cmd@55558ce57570> set_tgCic <number:1..65535> <cr>
```

Handler ` RVA 0x1E3CF1F0 `；selector ` 0 `；EOL ` RVA 0x379036C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` TRUNKGROUP CIC Number。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [缺口 G-3c24b5e558ad4dc0](../../evidence/gaps-sets-003.md#g-3c24b5e558ad4dc0) · [参数 P-5cd29f6ad2bad388](../../evidence/parameters-sets-007.md#p-5cd29f6ad2bad388) · [状态效果 S-e7bbb78e47f8252f](../../evidence/state_effects-sets-049.md#s-e7bbb78e47f8252f)

### path-021539

```text
(exec)# test tunnel <interface> config destination dynamic <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 9 `；EOL ` RVA 0x34831460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-52100868f2ed13bf](../../evidence/conditions-sets-032.md#c-52100868f2ed13bf) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-7c6b836a7deca93f](../../evidence/state_effects-sets-026.md#s-7c6b836a7deca93f)

### path-021551

```text
(exec)# test tunnel <interface> config dst-port <number:0..65535> <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 30 `；EOL ` RVA 0x34831828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` tunnel destination port number。

[条件 C-818e8c2681c52121](../../evidence/conditions-sets-050.md#c-818e8c2681c52121) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-6304a1ea7ef5cef4](../../evidence/parameters-sets-008.md#p-6304a1ea7ef5cef4)

### path-021524

```text
(exec)# test tunnel <interface> config source dynamic <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 10 `；EOL ` RVA 0x34830F98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2320145baa22e991](../../evidence/conditions-sets-014.md#c-2320145baa22e991) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-f61bccecaff99462](../../evidence/state_effects-sets-052.md#s-f61bccecaff99462)

### path-021574

```text
(exec)# test tunnel <interface> config src-port <number:0..65535> <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 31 `；EOL ` RVA 0x34831B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel Source port number。

[条件 C-d507e11a66adbf70](../../evidence/conditions-sets-082.md#c-d507e11a66adbf70) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-1d60903cb544d4d7](../../evidence/parameters-sets-003.md#p-1d60903cb544d4d7)

### path-013665

```text
(exec)# test tunnel <interface> decap <cr>
```

Handler ` RVA 0xFB8FC80 `；selector ` 23 `；EOL ` RVA 0x34833C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d)

### path-021615

```text
(exec)# test tunnel <interface> endpoints add <address> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 2 `；EOL ` RVA 0x34832038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` overlay ip address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-f0432e4861384a95](../../evidence/parameters-sets-018.md#p-f0432e4861384a95)

### path-021606

```text
(exec)# test tunnel <interface> endpoints auto-adj-mtu enable <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 6 `；EOL ` RVA 0x348338D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-de77310d8e129f78](../../evidence/conditions-sets-086.md#c-de77310d8e129f78) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-024144bc3cfc7889](../../evidence/state_effects-sets-001.md#s-024144bc3cfc7889)

### path-021534

```text
(exec)# test tunnel <interface> endpoints delete <address> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 1 `；EOL ` RVA 0x34832738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` overlay ip address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-f3b06952e2b4f70c](../../evidence/parameters-sets-018.md#p-f3b06952e2b4f70c)

### path-023795

```text
(exec)# test tunnel <interface> endpoints find transport <address> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 0 `；EOL ` RVA 0x34832AD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-078211b1f83acf51](../../evidence/parameters-sets-001.md#p-078211b1f83acf51) · [状态效果 S-477caace89cd607a](../../evidence/state_effects-sets-016.md#s-477caace89cd607a)

### path-024704

```text
(exec)# test tunnel <interface> endpoints ref transport <address> <number:0..1000000> <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 3 `；EOL ` RVA 0x34832F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address；` unsigned_number ` refcount。

[条件 C-964e63bed94ad8be](../../evidence/conditions-sets-058.md#c-964e63bed94ad8be) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-fd86cf69070b5df9](../../evidence/parameters-sets-019.md#p-fd86cf69070b5df9) · [状态效果 S-2d44d71dd0e5811e](../../evidence/state_effects-sets-010.md#s-2d44d71dd0e5811e)

### path-025016

```text
(exec)# test tunnel <interface> endpoints service-policy output <string> <address> add <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 4 `；EOL ` RVA 0x34833348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` QoS policy-map name；` address ` transport ip address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-7ca721b4af31f699](../../evidence/parameters-sets-010.md#p-7ca721b4af31f699)

### path-025020

```text
(exec)# test tunnel <interface> endpoints service-policy output <string> <address> delete <cr>
```

Handler ` RVA 0xFBAB130 `；selector ` 5 `；EOL ` RVA 0x348335F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` QoS policy-map name；` address ` transport ip address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-7ca721b4af31f699](../../evidence/parameters-sets-010.md#p-7ca721b4af31f699)

### path-025018

```text
(exec)# test tunnel <interface> key add p2mp <number:0..4294967295> <number:0..4294967295> <address> <cr>
```

Handler ` RVA 0xFBC5ED0 `；selector ` 0 `；EOL ` RVA 0x34834150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` receive key；` unsigned_number ` transmit key；` address ` Overlay ipv4 address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-bbb06155c8fdfa8b](../../evidence/parameters-sets-014.md#p-bbb06155c8fdfa8b) · [状态效果 S-02bbd4b90362d679](../../evidence/state_effects-sets-001.md#s-02bbd4b90362d679)

### path-024696

```text
(exec)# test tunnel <interface> subblock add endpoint transport <address> <cr>
```

Handler ` RVA 0xFB7BB40 `；selector ` 0 `；EOL ` RVA 0x34826C40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` ip address。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-48d3fa64684472b9](../../evidence/parameters-sets-006.md#p-48d3fa64684472b9) · [状态效果 S-724b235aea0e9cd2](../../evidence/state_effects-sets-024.md#s-724b235aea0e9cd2)

### path-021522

```text
(exec)# test tunnel <interface> subblock add interface <cr>
```

Handler ` RVA 0xFB7BB40 `；selector ` 1 `；EOL ` RVA 0x348268E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-974d518c73ab19a1](../../evidence/state_effects-sets-032.md#s-974d518c73ab19a1)

### path-017547

```text
(exec)# test tunnel <interface> tos enable <cr>
```

Handler ` RVA 0xFB8F9A0 `；selector ` 0 `；EOL ` RVA 0x34830B90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60b2b76a7f23863e](../../evidence/conditions-sets-038.md#c-60b2b76a7f23863e) · [缺口 G-0b7d269385369c4a](../../evidence/gaps-sets-001.md#g-0b7d269385369c4a) · [参数 P-b2cffede053a7a8d](../../evidence/parameters-sets-014.md#p-b2cffede053a7a8d) · [状态效果 S-9ff687ee11aa890d](../../evidence/state_effects-sets-034.md#s-9ff687ee11aa890d)

### path-010968

```text
(exec)# test tunnel Groups wccp <number:0..9> add <cr>
```

Handler ` RVA 0xB516500 `；selector ` 0 `；EOL ` RVA 0x33792A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-ce6ef86e74b6a0f0](../../evidence/conditions-sets-079.md#c-ce6ef86e74b6a0f0) · [参数 P-816d5b8c6fbe0a85](../../evidence/parameters-sets-010.md#p-816d5b8c6fbe0a85) · [状态效果 S-68adc1c71274a3fe](../../evidence/state_effects-sets-022.md#s-68adc1c71274a3fe)

### path-012011

```text
(exec)# test tunnel Groups wccp <number:0..9> add ipv4 V1 <cr>
```

Handler ` RVA 0xB513640 `；selector ` 0 `；EOL ` RVA 0x33790108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-48bdf627336a94aa](../../evidence/state_effects-sets-016.md#s-48bdf627336a94aa)

### path-011002

```text
(exec)# test tunnel Groups wccp <number:0..9> clear <cr>
```

Handler ` RVA 0xB513640 `；selector ` 6 `；EOL ` RVA 0x337916D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-010947

```text
(exec)# test tunnel Groups wccp <number:0..9> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 1 `；EOL ` RVA 0x33790440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-011758

```text
(exec)# test tunnel Groups wccp <number:0..9> df-bit set <cr>
```

Handler ` RVA 0xB513640 `；selector ` 5 `；EOL ` RVA 0x33791448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-f4d83aaa6eb40d39](../../evidence/parameters-sets-018.md#p-f4d83aaa6eb40d39) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-012013

```text
(exec)# test tunnel Groups wccp <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB513640 `；selector ` 7 `；EOL ` RVA 0x33790AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-012015

```text
(exec)# test tunnel Groups wccp <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB513640 `；selector ` 8 `；EOL ` RVA 0x33790D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-d106356a47c3c452](../../evidence/parameters-sets-016.md#p-d106356a47c3c452) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-011747

```text
(exec)# test tunnel Groups wccp <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB513640 `；selector ` 2 `；EOL ` RVA 0x33790750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Overlay Group ID；` address ` IPv4 address。

[条件 C-47a1cfc600ac9dd9](../../evidence/conditions-sets-028.md#c-47a1cfc600ac9dd9) · [参数 P-de0e272fb87adafa](../../evidence/parameters-sets-017.md#p-de0e272fb87adafa) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-023851

```text
(exec)# test tunnel Groups wccp <number:0..9> source-if <interface> <cr>
```

Handler ` RVA 0xB514190 `；selector ` 0 `；EOL ` RVA 0x33792060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-67032688e5c664e2](../../evidence/conditions-sets-040.md#c-67032688e5c664e2) · [缺口 G-638bea1b3cb44416](../../evidence/gaps-sets-004.md#g-638bea1b3cb44416) · [参数 P-1400d1d8336b2244](../../evidence/parameters-sets-002.md#p-1400d1d8336b2244) · [状态效果 S-d27815381afe540a](../../evidence/state_effects-sets-045.md#s-d27815381afe540a)

### path-023907

```text
(exec)# test tunnel Groups wccp <number:0..9> unnumbered <interface> <cr>
```

Handler ` RVA 0xB513640 `；selector ` 3 `；EOL ` RVA 0x33791120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Overlay Group ID。

[条件 C-49e2525f5595c4b6](../../evidence/conditions-sets-029.md#c-49e2525f5595c4b6) · [缺口 G-4d973959b4f976be](../../evidence/gaps-sets-003.md#g-4d973959b4f976be) · [参数 P-4d4e6c62c08c8969](../../evidence/parameters-sets-006.md#p-4d4e6c62c08c8969) · [状态效果 S-238a6d1c15b62941](../../evidence/state_effects-sets-008.md#s-238a6d1c15b62941)

### path-010949

```text
(exec)# test tunnel Groups wccp <number:0..9> unsource <cr>
```

Handler ` RVA 0xB514190 `；selector ` 0 `；EOL ` RVA 0x33792060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` service group ID。

[条件 C-fe6ccd9023d833b6](../../evidence/conditions-sets-098.md#c-fe6ccd9023d833b6) · [参数 P-ccb3e85e97e2dec4](../../evidence/parameters-sets-016.md#p-ccb3e85e97e2dec4) · [状态效果 S-4bb9bec91ef469ae](../../evidence/state_effects-sets-017.md#s-4bb9bec91ef469ae)

### path-005103

```text
(exec)# test tunnel tos enable <cr>
```

Handler ` RVA 0xFB8F9A0 `；selector ` 0 `；EOL ` RVA 0x34830B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [状态效果 S-9ff687ee11aa890d](../../evidence/state_effects-sets-034.md#s-9ff687ee11aa890d)

### path-012008

```text
(exec)# test tunnel tun-to <number:0..9> add transport ipv4 none <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 1 `；EOL ` RVA 0x33794348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-7d9fb058237a4a07](../../evidence/conditions-sets-049.md#c-7d9fb058237a4a07) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-b693f2d0ed32cb23](../../evidence/state_effects-sets-039.md#s-b693f2d0ed32cb23)

### path-008830

```text
(exec)# test tunnel tun-to <number:0..9> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 2 `；EOL ` RVA 0x33794638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526)

### path-010985

```text
(exec)# test tunnel tun-to <number:0..9> display <number:0..160> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 7 `；EOL ` RVA 0x337968F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` unsigned_number ` Indent。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-c32407e8d350360d](../../evidence/parameters-sets-015.md#p-c32407e8d350360d) · [状态效果 S-94b5d6b60e5b26ac](../../evidence/state_effects-sets-032.md#s-94b5d6b60e5b26ac)

### path-011741

```text
(exec)# test tunnel tun-to <number:0..9> endpoint <address> add <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 13 `；EOL ` RVA 0x33795110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28)

### path-011750

```text
(exec)# test tunnel tun-to <number:0..9> endpoint <address> delete <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 14 `；EOL ` RVA 0x337953B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-e18f04e057ad6e28](../../evidence/parameters-sets-017.md#p-e18f04e057ad6e28)

### path-025032

```text
(exec)# test tunnel tun-to <number:0..9> endpoint <address> redirect <interface> disable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 16 `；EOL ` RVA 0x33795A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-6836ca5be70f314b](../../evidence/conditions-sets-040.md#c-6836ca5be70f314b) · [缺口 G-aeb93bfcdfaa0a3e](../../evidence/gaps-sets-006.md#g-aeb93bfcdfaa0a3e) · [参数 P-2f3d36d1a44d7406](../../evidence/parameters-sets-004.md#p-2f3d36d1a44d7406)

### path-025028

```text
(exec)# test tunnel tun-to <number:0..9> endpoint <address> redirect <interface> enable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 15 `；EOL ` RVA 0x33795760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-6836ca5be70f314b](../../evidence/conditions-sets-040.md#c-6836ca5be70f314b) · [缺口 G-aeb93bfcdfaa0a3e](../../evidence/gaps-sets-006.md#g-aeb93bfcdfaa0a3e) · [参数 P-2f3d36d1a44d7406](../../evidence/parameters-sets-004.md#p-2f3d36d1a44d7406)

### path-011755

```text
(exec)# test tunnel tun-to <number:0..9> feature enable post-encap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 9 `；EOL ` RVA 0x33796C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-856cfcbfb50e343e](../../evidence/state_effects-sets-028.md#s-856cfcbfb50e343e)

### path-011759

```text
(exec)# test tunnel tun-to <number:0..9> feature enable pre-decap <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 10 `；EOL ` RVA 0x33796EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-856cfcbfb50e343e](../../evidence/state_effects-sets-028.md#s-856cfcbfb50e343e)

### path-011744

```text
(exec)# test tunnel tun-to <number:0..9> gre key disable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 8 `；EOL ` RVA 0x33796538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-62e83f2881daa14e](../../evidence/state_effects-sets-021.md#s-62e83f2881daa14e)

### path-011738

```text
(exec)# test tunnel tun-to <number:0..9> payload ipv4 enable <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 11 `；EOL ` RVA 0x33795DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-d139ea25f94f0916](../../evidence/conditions-sets-081.md#c-d139ea25f94f0916) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-494578db784e877a](../../evidence/state_effects-sets-016.md#s-494578db784e877a)

### path-012012

```text
(exec)# test tunnel tun-to <number:0..9> payload ipv4 mtu default <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 12 `；EOL ` RVA 0x337960C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-d139ea25f94f0916](../../evidence/conditions-sets-081.md#c-d139ea25f94f0916) · [参数 P-695815f3b54ec526](../../evidence/parameters-sets-008.md#p-695815f3b54ec526) · [状态效果 S-6bed73b7ca0d5cb9](../../evidence/state_effects-sets-023.md#s-6bed73b7ca0d5cb9)

### path-010908

```text
(exec)# test tunnel tun-to <number:0..9> source <address> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 3 `；EOL ` RVA 0x33794948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier；` address ` IPv4 address。

[条件 C-8c48dfc36479b2a5](../../evidence/conditions-sets-054.md#c-8c48dfc36479b2a5) · [参数 P-b5fd48203094e8df](../../evidence/parameters-sets-014.md#p-b5fd48203094e8df)

### path-021634

```text
(exec)# test tunnel tun-to <number:0..9> source <interface> <cr>
```

Handler ` RVA 0xB51A690 `；selector ` 4 `；EOL ` RVA 0x33794CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Tunnel-to test handle identifier。

[条件 C-bd632317ea035665](../../evidence/conditions-sets-073.md#c-bd632317ea035665) · [缺口 G-e0c458f4d5299bd1](../../evidence/gaps-sets-008.md#g-e0c458f4d5299bd1) · [参数 P-4356715a4b94a73e](../../evidence/parameters-sets-006.md#p-4356715a4b94a73e)

### path-002462

```text
(exec)# test uninstall <string> <cr>
```

Handler ` RVA 0x15A6CC70 `；selector ` 0 `；EOL ` RVA 0x35DE37F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Virtual-service name。

[条件 C-e0e7243124538125](../../evidence/conditions-sets-087.md#c-e0e7243124538125) · [参数 P-7b9316c0493b1273](../../evidence/parameters-sets-010.md#p-7b9316c0493b1273)

### path-017378

```text
(exec)# test vlan-autoconfig <interface> <number:1..4096> <number:1..4096> <cr>
```

Handler ` RVA 0x112B7720 `；selector ` 0 `；EOL ` RVA 0x35450498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Begin VLAN；` unsigned_number ` End VLAN。

[条件 C-9b25929d4361022f](../../evidence/conditions-sets-060.md#c-9b25929d4361022f) · [缺口 G-dd7d4d75d0ddffb2](../../evidence/gaps-sets-008.md#g-dd7d4d75d0ddffb2) · [参数 P-0d9c3b97f8d0dcc0](../../evidence/parameters-sets-001.md#p-0d9c3b97f8d0dcc0)

### path-010650

```text
(exec)# test vrrs client add <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 9 `；EOL ` RVA 0x342A0CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-c1faf0a01590e7c1](../../evidence/parameters-sets-015.md#p-c1faf0a01590e7c1) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-008557

```text
(exec)# test vrrs client register <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 11 `；EOL ` RVA 0x342A0678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-dfe2be5a59cb5d99](../../evidence/parameters-sets-017.md#p-dfe2be5a59cb5d99) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-010663

```text
(exec)# test vrrs client remove <number:1..31> <string> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 8 `；EOL ` RVA 0x342A0FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id；` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-912dcfafa5af0bac](../../evidence/parameters-sets-011.md#p-912dcfafa5af0bac) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-008532

```text
(exec)# test vrrs client unregister <number:1..31> <cr>
```

Handler ` RVA 0xE305C00 `；selector ` 10 `；EOL ` RVA 0x342A0988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` client id。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-e7f6bd64325acaf4](../../evidence/parameters-sets-017.md#p-e7f6bd64325acaf4) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-010756

```text
(exec)# test vrrs pathway name <string> disconnect <cr>
```

Handler ` RVA 0x133F9580 `；selector ` 0 `；EOL ` RVA 0x35A8B960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the VRRS tag associated with pathways。

[条件 C-463a0f267f49a4f6](../../evidence/conditions-sets-027.md#c-463a0f267f49a4f6) · [参数 P-b55499403f5cacac](../../evidence/parameters-sets-014.md#p-b55499403f5cacac) · [状态效果 S-89b02780f3c3fac7](../../evidence/state_effects-sets-029.md#s-89b02780f3c3fac7)

### path-004301

```text
(exec)# test vrrs plugin server <cr>
```

Handler ` RVA 0xE2FF4F0 `；selector ` 0 `；EOL ` RVA 0x342A69C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4877c057cb96702c](../../evidence/conditions-sets-028.md#c-4877c057cb96702c) · [状态效果 S-dc6ebcf9cab88335](../../evidence/state_effects-sets-047.md#s-dc6ebcf9cab88335)

### path-011677

```text
(exec)# test vrrs server add <string> vip <address> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 7 `；EOL ` RVA 0x342A15D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name string；` address ` VRRP group's virtual address。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-1c35fd9c9703b522](../../evidence/parameters-sets-003.md#p-1c35fd9c9703b522) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-008560

```text
(exec)# test vrrs server delete <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 5 `；EOL ` RVA 0x342A1F08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-3c862bfbe3046baa](../../evidence/parameters-sets-005.md#p-3c862bfbe3046baa) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-008616

```text
(exec)# test vrrs server update <string> <cr>
```

Handler ` RVA 0xE306550 `；selector ` 6 `；EOL ` RVA 0x342A1BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` group name string。

[条件 C-aa03cd9592f17c46](../../evidence/conditions-sets-066.md#c-aa03cd9592f17c46) · [参数 P-6c0f2e263c8af654](../../evidence/parameters-sets-009.md#p-6c0f2e263c8af654) · [状态效果 S-d20500182274a653](../../evidence/state_effects-sets-044.md#s-d20500182274a653)

### path-010781

```text
(exec)# test wccp ip web-cache assignment hash <cr>
```

Handler ` RVA 0x10AE0FA0 `；selector ` 0 `；EOL ` RVA 0x34CA15E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab6f89db78e80bdb](../../evidence/conditions-sets-066.md#c-ab6f89db78e80bdb) · [状态效果 S-9db8978f3ad2f584](../../evidence/state_effects-sets-033.md#s-9db8978f3ad2f584)

### path-008726

```text
(exec)# test wccp ip web-cache capabilities <cr>
```

Handler ` RVA 0x10AE0C00 `；selector ` 0 `；EOL ` RVA 0x34CA11B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af97d057c7bd2c8a](../../evidence/conditions-sets-068.md#c-af97d057c7bd2c8a) · [状态效果 S-4d8aa525db3c6cf8](../../evidence/state_effects-sets-017.md#s-4d8aa525db3c6cf8)

### path-024650

```text
(exec)# test wccp ip web-cache client <address> <interface> add <cr>
```

Handler ` RVA 0x10AE07A0 `；selector ` 1 `；EOL ` RVA 0x34CA07B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Client IPv4 address。

[条件 C-d93deed09475f014](../../evidence/conditions-sets-084.md#c-d93deed09475f014) · [缺口 G-406cfbfa190f2d4b](../../evidence/gaps-sets-003.md#g-406cfbfa190f2d4b) · [参数 P-fa6891eb35ef32da](../../evidence/parameters-sets-019.md#p-fa6891eb35ef32da) · [状态效果 S-4d8aa525db3c6cf8](../../evidence/state_effects-sets-017.md#s-4d8aa525db3c6cf8)

### path-024660

```text
(exec)# test wccp ip web-cache client <address> <interface> remove <cr>
```

Handler ` RVA 0x10AE07A0 `；selector ` 2 `；EOL ` RVA 0x34CA0A58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Client IPv4 address。

[条件 C-7b89c4a752dc64c8](../../evidence/conditions-sets-048.md#c-7b89c4a752dc64c8) · [缺口 G-406cfbfa190f2d4b](../../evidence/gaps-sets-003.md#g-406cfbfa190f2d4b) · [参数 P-fa6891eb35ef32da](../../evidence/parameters-sets-019.md#p-fa6891eb35ef32da) · [状态效果 S-4d8aa525db3c6cf8](../../evidence/state_effects-sets-017.md#s-4d8aa525db3c6cf8)

### path-011987

```text
(exec)# test wccp ip web-cache service <number:0..255> <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x10AE0A90 `；selector ` 0 `；EOL ` RVA 0x34CA1C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` WCCP service priority；` unsigned_number ` WCCP service protocol；` unsigned_number ` WCCP service flags。

[条件 C-4caa14063efcbaa3](../../evidence/conditions-sets-030.md#c-4caa14063efcbaa3) · [参数 P-71b77f6b738f2f59](../../evidence/parameters-sets-009.md#p-71b77f6b738f2f59) · [状态效果 S-4d8aa525db3c6cf8](../../evidence/state_effects-sets-017.md#s-4d8aa525db3c6cf8)

### path-002275

```text
(exec)# test wsma history <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 1 `；EOL ` RVA 0x3463D0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-006235

```text
(exec)# test wsma listener <string> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 2 `；EOL ` RVA 0x3463D6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the transport。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-9f474f72af6c782b](../../evidence/parameters-sets-012.md#p-9f474f72af6c782b)

### path-006268

```text
(exec)# test wsma max-priv-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 4 `；EOL ` RVA 0x3463D960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enforce max priv or not。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb) · [参数 P-d3faea102e025dae](../../evidence/parameters-sets-016.md#p-d3faea102e025dae)

### path-002296

```text
(exec)# test wsma summary <cr>
```

Handler ` RVA 0xF3EC9F0 `；selector ` 3 `；EOL ` RVA 0x3463D390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-004831

```text
(exec)# test x25 dbit <number:0..1000> <cr>
```

Handler ` RVA 0x1061D5B0 `；selector ` 0 `；EOL ` RVA 0x34BD4DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` D-bit interval (packets)。

[条件 C-24513ddd0c676292](../../evidence/conditions-sets-014.md#c-24513ddd0c676292) · [参数 P-f4144dc0d3cc9c91](../../evidence/parameters-sets-018.md#p-f4144dc0d3cc9c91)

### path-005176

```text
(exec)# test xdr create-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7830 `；selector ` 0 `；EOL ` RVA 0x34CFDE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ID of test stream to create。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [参数 P-d155c8fe88eef6d1](../../evidence/parameters-sets-016.md#p-d155c8fe88eef6d1)

### path-005159

```text
(exec)# test xdr destroy-stream <number:1..20> <cr>
```

Handler ` RVA 0x10CA7890 `；selector ` 0 `；EOL ` RVA 0x34CFDB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ID of test stream to destroy。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [参数 P-c2413738ef352aaf](../../evidence/parameters-sets-015.md#p-c2413738ef352aaf)

### path-001273

```text
(exec)# test xdr disable <cr>
```

Handler ` RVA 0x10C75EA0 `；selector ` 0 `；EOL ` RVA 0x34CF46D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88f99a190082320b](../../evidence/conditions-sets-053.md#c-88f99a190082320b)

### path-001274

```text
(exec)# test xdr enable <cr>
```

Handler ` RVA 0x10C75E20 `；selector ` 0 `；EOL ` RVA 0x34CF4988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e4c3b7ef72defc89](../../evidence/conditions-sets-088.md#c-e4c3b7ef72defc89)

### path-010999

```text
(exec)# test xdr fragment <number:1..1000000> to_slots High-queue <cr>
```

Handler ` RVA 0x10CA78F0 `；selector ` 0 `；EOL ` RVA 0x34CFEF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` fragment size (in Bytes)。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [参数 P-7258ec243930115d](../../evidence/parameters-sets-009.md#p-7258ec243930115d) · [状态效果 S-b8b7d5a88c82a2e3](../../evidence/state_effects-sets-039.md#s-b8b7d5a88c82a2e3)

### path-025325

```text
(exec)# test xdr join <number:dynamic> to <number:dynamic> <cr>
```

Handler ` RVA 0x10CA7B90 `；selector ` 0 `；EOL ` RVA 0x34CFD4C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Group containing this linecard as a member；` unsigned_number_dynamic ` Group containing this linecard as a member。

[条件 C-f9b97a0e0126a409](../../evidence/conditions-sets-096.md#c-f9b97a0e0126a409) · [缺口 G-4ac3da73487c730b](../../evidence/gaps-sets-003.md#g-4ac3da73487c730b) · [参数 P-089665b9a1263322](../../evidence/parameters-sets-001.md#p-089665b9a1263322) · [状态效果 S-55ce6cb5ed14cea1](../../evidence/state_effects-sets-019.md#s-55ce6cb5ed14cea1)

### path-010879

```text
(exec)# test xdr ping to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA7E20 `；selector ` 0 `；EOL ` RVA 0x34CFD028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [参数 P-b75cb2e4c5728f3a](../../evidence/parameters-sets-014.md#p-b75cb2e4c5728f3a) · [状态效果 S-1c2d1e7352d1c06c](../../evidence/state_effects-sets-006.md#s-1c2d1e7352d1c06c)

### path-005210

```text
(exec)# test xdr push start <cr>
```

Handler ` RVA 0x10CA7B40 `；selector ` 0 `；EOL ` RVA 0x34CFE3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a)

### path-012169

```text
(exec)# test xdr push stream <number:1..20> count <number:0..200000> to_linecards <number:0..2147483647> High-queue <cr>
```

Handler ` RVA 0x10CA75D0 `；selector ` 0 `；EOL ` RVA 0x34CFE818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number of XDRs to send；` unsigned_number ` Number representing the bitmask of the linecards。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [参数 P-92fc2dc68416fcec](../../evidence/parameters-sets-011.md#p-92fc2dc68416fcec) · [状态效果 S-56643959b08e86ce](../../evidence/state_effects-sets-019.md#s-56643959b08e86ce)

### path-001393

```text
(exec)# test xdr show-streams <cr>
```

Handler ` RVA 0x10CA76F0 `；selector ` 0 `；EOL ` RVA 0x34CFE0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a)

### path-005144

```text
(exec)# test xdr split allow <cr>
```

Handler ` RVA 0x10CA7D50 `；selector ` 0 `；EOL ` RVA 0x34CFD7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39f5ff1698c94a1a](../../evidence/conditions-sets-022.md#c-39f5ff1698c94a1a) · [状态效果 S-364eda318df86cd2](../../evidence/state_effects-sets-012.md#s-364eda318df86cd2)

### path-017710

```text
(exec)# test xdr state-change <number:dynamic> up <cr>
```

Handler ` RVA 0x10C913F0 `；selector ` 0 `；EOL ` RVA 0x34CFF320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number。

[条件 C-a51a1279444fe160](../../evidence/conditions-sets-064.md#c-a51a1279444fe160) · [缺口 G-f1c4b55ebaa95cca](../../evidence/gaps-sets-008.md#g-f1c4b55ebaa95cca) · [参数 P-175b50d7b53a64f0](../../evidence/parameters-sets-002.md#p-175b50d7b53a64f0) · [状态效果 S-5452d8749d05208d](../../evidence/state_effects-sets-018.md#s-5452d8749d05208d)

### path-005266

```text
(exec)# test xdr state-change IPC_START_SENDING <cr>
```

Handler ` RVA 0x10C913F0 `；selector ` 0 `；EOL ` RVA 0x34CFF320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3d40e9bf840d793](../../evidence/conditions-sets-070.md#c-b3d40e9bf840d793) · [状态效果 S-b5ff89d8c82b8a14](../../evidence/state_effects-sets-039.md#s-b5ff89d8c82b8a14)

### path-012003

```text
(exec)# test xdr statistics client test-stats-1 create <number:1..1000000> <number:1..6000> <cr>
```

Handler ` RVA 0xB315AB0 `；selector ` 0 `；EOL ` RVA 0x33737890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Num counters for this client；` unsigned_number ` Update interval for this client (s)。

[条件 C-9e8d2f8ada02ca9c](../../evidence/conditions-sets-061.md#c-9e8d2f8ada02ca9c) · [参数 P-022205fef7e7929e](../../evidence/parameters-sets-001.md#p-022205fef7e7929e) · [状态效果 S-5ebc5ed3a82a5639](../../evidence/state_effects-sets-020.md#s-5ebc5ed3a82a5639)

### path-010917

```text
(exec)# test xdr statistics client test-stats-1 req-stats <cr>
```

Handler ` RVA 0xB2B2B70 `；selector ` 0 `；EOL ` RVA 0x3372F4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55f1bb7516490603](../../evidence/conditions-sets-034.md#c-55f1bb7516490603) · [状态效果 S-5a65694e7c2f8544](../../evidence/state_effects-sets-019.md#s-5a65694e7c2f8544)

### path-010935

```text
(exec)# test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB3157E0 `；selector ` 0 `；EOL ` RVA 0x33737E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e8d2f8ada02ca9c](../../evidence/conditions-sets-061.md#c-9e8d2f8ada02ca9c) · [状态效果 S-cc1b72df9231eade](../../evidence/state_effects-sets-043.md#s-cc1b72df9231eade)

### path-010955

```text
(exec)# test xdr statistics client test-stats-1 show <cr>
```

Handler ` RVA 0xB2B2770 `；selector ` 0 `；EOL ` RVA 0x3372FCE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55f1bb7516490603](../../evidence/conditions-sets-034.md#c-55f1bb7516490603) · [状态效果 S-96b173bff9fe8a48](../../evidence/state_effects-sets-032.md#s-96b173bff9fe8a48)

### path-008839

```text
(exec)# test xdr statistics selftest <number:0..64> <cr>
```

Handler ` RVA 0xB2B3280 `；selector ` 0 `；EOL ` RVA 0x33730148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` slot_id。

[条件 C-6c74c69bb8bd70de](../../evidence/conditions-sets-042.md#c-6c74c69bb8bd70de) · [参数 P-a26de8620aef734b](../../evidence/parameters-sets-012.md#p-a26de8620aef734b)

### path-000310

```text
(exec)# test xtf-policy-shim <cr>
```

Handler ` RVA 0x128866D0 `；selector ` 0 `；EOL ` RVA 0x358F6488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4db37065731260bb](../../evidence/conditions-sets-030.md#c-4db37065731260bb)

### path-000028

```text
(exec)# traceroute <cr>
```

Handler ` RVA 0xE00FAA0 `；selector ` 0 `；EOL ` RVA 0x3415C008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e14ec55b45eaf509](../../evidence/conditions-sets-087.md#c-e14ec55b45eaf509)

### path-010572

```text
(exec)# traceroute ethernet <address> domain <string> port <cr>
```

Handler ` RVA 0xBD664C0 `；selector ` 0 `；EOL ` RVA 0x338E2680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote Maintenance Point MAC Address；` string ` maintenance domain name。

[条件 C-929c3c6ad592ed8c](../../evidence/conditions-sets-057.md#c-929c3c6ad592ed8c) · [参数 P-938128e39050e564](../../evidence/parameters-sets-011.md#p-938128e39050e564) · [状态效果 S-827ba1ad86de8098](../../evidence/state_effects-sets-028.md#s-827ba1ad86de8098)

### path-000051

```text
(exec)# trigger <string> <cr>
```

Handler ` RVA 0xDF79070 `；selector ` 0 `；EOL ` RVA 0x340B8D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trigger identifier for the trigger to be created or executed。

[条件 C-dba12bc9c2f286c9](../../evidence/conditions-sets-085.md#c-dba12bc9c2f286c9) · [参数 P-8105354b13a9d4eb](../../evidence/parameters-sets-010.md#p-8105354b13a9d4eb)

### path-000178

```text
(exec)# tunnel <string> <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33D2A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Address or hostname of a remote system。

[条件 C-30b0899d435cd28f](../../evidence/conditions-sets-019.md#c-30b0899d435cd28f) · [参数 P-4279d2faf8428569](../../evidence/parameters-sets-006.md#p-4279d2faf8428569) · [状态效果 S-e343617f989b5464](../../evidence/state_effects-sets-048.md#s-e343617f989b5464)

### path-000664

```text
(exec)# undebug ACM all <cr>
```

Handler ` RVA 0xDEDBDB0 `；selector ` 0 `；EOL ` RVA 0x34096D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-e940085102f8db0b](../../evidence/state_effects-sets-049.md#s-e940085102f8db0b)

### path-000638

```text
(exec)# undebug ACM error <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 1 `；EOL ` RVA 0x340967E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-e940085102f8db0b](../../evidence/state_effects-sets-049.md#s-e940085102f8db0b)

### path-000652

```text
(exec)# undebug ACM event <cr>
```

Handler ` RVA 0xDEDBD60 `；selector ` 0 `；EOL ` RVA 0x34096A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-e940085102f8db0b](../../evidence/state_effects-sets-049.md#s-e940085102f8db0b)

### path-003436

```text
(exec)# undebug LDAP all <cr>
```

Handler ` RVA 0x11AC30E0 `；selector ` 0 `；EOL ` RVA 0x3560CAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [状态效果 S-f35ca9bd3798f381](../../evidence/state_effects-sets-051.md#s-f35ca9bd3798f381)

### path-003405

```text
(exec)# undebug LDAP error <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 1 `；EOL ` RVA 0x3560C2C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [状态效果 S-f35ca9bd3798f381](../../evidence/state_effects-sets-051.md#s-f35ca9bd3798f381)

### path-003417

```text
(exec)# undebug LDAP event <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 0 `；EOL ` RVA 0x3560C568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [状态效果 S-f35ca9bd3798f381](../../evidence/state_effects-sets-051.md#s-f35ca9bd3798f381)

### path-003428

```text
(exec)# undebug LDAP legacy <cr>
```

Handler ` RVA 0xE002120 `；selector ` 3 `；EOL ` RVA 0x3560C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [状态效果 S-f35ca9bd3798f381](../../evidence/state_effects-sets-051.md#s-f35ca9bd3798f381)

### path-003393

```text
(exec)# undebug LDAP packet <cr>
```

Handler ` RVA 0xDD48D90 `；selector ` 2 `；EOL ` RVA 0x3560C018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2105136e024fa964](../../evidence/conditions-sets-013.md#c-2105136e024fa964) · [状态效果 S-f35ca9bd3798f381](../../evidence/state_effects-sets-051.md#s-f35ca9bd3798f381)

### path-000947

```text
(exec)# undebug aaa accounting <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 16 `；EOL ` RVA 0x341B80C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-000963

```text
(exec)# undebug aaa administrative <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 17 `；EOL ` RVA 0x341B8368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001252

```text
(exec)# undebug aaa api <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 35 `；EOL ` RVA 0x341BC6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004992

```text
(exec)# undebug aaa api attr <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 36 `；EOL ` RVA 0x341BC680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001232

```text
(exec)# undebug aaa attr <cr>
```

Handler ` RVA 0xDD3A410 `；selector ` 26 `；EOL ` RVA 0x341BB120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004922

```text
(exec)# undebug aaa attr add <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 30 `；EOL ` RVA 0x341BABA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004900

```text
(exec)# undebug aaa attr alloc-free <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 31 `；EOL ` RVA 0x341BA900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004873

```text
(exec)# undebug aaa attr error <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 32 `；EOL ` RVA 0x341BA658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004850

```text
(exec)# undebug aaa attr handle <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 27 `；EOL ` RVA 0x341BA3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004961

```text
(exec)# undebug aaa attr info <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 28 `；EOL ` RVA 0x341BB0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004940

```text
(exec)# undebug aaa attr update <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 29 `；EOL ` RVA 0x341BAE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-000911

```text
(exec)# undebug aaa authentication <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 12 `；EOL ` RVA 0x341B7B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-000930

```text
(exec)# undebug aaa authorization <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 15 `；EOL ` RVA 0x341B7E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-000978

```text
(exec)# undebug aaa boundary <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 56 `；EOL ` RVA 0x341B8610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004603

```text
(exec)# undebug aaa cache filterserver <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 50 `；EOL ` RVA 0x341B7040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004623

```text
(exec)# undebug aaa cache group <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 51 `；EOL ` RVA 0x341B72E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-000997

```text
(exec)# undebug aaa cca <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 57 `；EOL ` RVA 0x341B88B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001088

```text
(exec)# undebug aaa coa <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 25 `；EOL ` RVA 0x341B98A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001320

```text
(exec)# undebug aaa common-criteria <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 55 `；EOL ` RVA 0x341BD9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-179869b93942c777](../../evidence/conditions-sets-009.md#c-179869b93942c777) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001187

```text
(exec)# undebug aaa db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 38 `；EOL ` RVA 0x341BBB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-005025

```text
(exec)# undebug aaa dead-criteria transaction <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 42 `；EOL ` RVA 0x341BD188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001328

```text
(exec)# undebug aaa green <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 69 `；EOL ` RVA 0x341BDC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-198ff8ab84026fa0](../../evidence/conditions-sets-010.md#c-198ff8ab84026fa0) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001218

```text
(exec)# undebug aaa id <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 37 `；EOL ` RVA 0x341BC0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001155

```text
(exec)# undebug aaa ipc <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 33 `；EOL ` RVA 0x341BB628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001132

```text
(exec)# undebug aaa memory <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 13 `；EOL ` RVA 0x341BA0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001025

```text
(exec)# undebug aaa mlist-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 44 `；EOL ` RVA 0x341B8E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001297

```text
(exec)# undebug aaa mlist-state <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 45 `；EOL ` RVA 0x341BD6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001074

```text
(exec)# undebug aaa per-user <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 18 `；EOL ` RVA 0x341B9600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001101

```text
(exec)# undebug aaa pod <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 24 `；EOL ` RVA 0x341B9B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-004631

```text
(exec)# undebug aaa profile db <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 52 `；EOL ` RVA 0x341B78E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-005009

```text
(exec)# undebug aaa protocol local <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 40 `；EOL ` RVA 0x341BCBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-005028

```text
(exec)# undebug aaa protocol radius <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 41 `；EOL ` RVA 0x341BCE88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001114

```text
(exec)# undebug aaa proxy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 23 `；EOL ` RVA 0x341B9DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001329

```text
(exec)# undebug aaa redundancy <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 54 `；EOL ` RVA 0x341BDF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8acdae59c3d89d4d](../../evidence/conditions-sets-054.md#c-8acdae59c3d89d4d) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001060

```text
(exec)# undebug aaa server-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 46 `；EOL ` RVA 0x341B9358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001040

```text
(exec)# undebug aaa sg-ref-count <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 47 `；EOL ` RVA 0x341B90B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

### path-001011

```text
(exec)# undebug aaa sg-server-selection <cr>
```

Handler ` RVA 0xDD48D40 `；selector ` 48 `；EOL ` RVA 0x341B8B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a7e992b2c3fb2eba](../../evidence/conditions-sets-065.md#c-a7e992b2c3fb2eba) · [状态效果 S-fb0b03fd9a5821f5](../../evidence/state_effects-sets-053.md#s-fb0b03fd9a5821f5)

