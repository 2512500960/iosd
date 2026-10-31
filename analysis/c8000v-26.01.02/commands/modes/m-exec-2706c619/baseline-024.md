# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-019736

```text
(exec)# do-exec pnpa service correlator-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 75 `；EOL ` RVA 0x33B66678 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Correlator check: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4a9d32d3aa341999](../../evidence/parameters-sets-006.md#p-4a9d32d3aa341999) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019722

```text
(exec)# do-exec pnpa service device-id-cert <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 76 `；EOL ` RVA 0x33B66388 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) device-id-cert。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bd8ddb0fee9cd6de](../../evidence/parameters-sets-014.md#p-bd8ddb0fee9cd6de) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020034

```text
(exec)# do-exec pnpa service diag <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 6 `；EOL ` RVA 0x33B71458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Diag level: 0-none, 1-all。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8ef001bbcd9e88c1](../../evidence/parameters-sets-011.md#p-8ef001bbcd9e88c1) · [状态效果 S-2d9a0996a2b729af](../../evidence/state_effects-sets-010.md#s-2d9a0996a2b729af)

### path-020202

```text
(exec)# do-exec pnpa service discovery abort-autoinstall <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 7 `；EOL ` RVA 0x33B71028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023086

```text
(exec)# do-exec pnpa service discovery bypass-auto-install <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 8 `；EOL ` RVA 0x33B70DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7f4f54823086e1ad](../../evidence/parameters-sets-010.md#p-7f4f54823086e1ad) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023083

```text
(exec)# do-exec pnpa service discovery bypass-cellular-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 9 `；EOL ` RVA 0x33B70AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass cellular-check: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6bfeb9065172b03e](../../evidence/parameters-sets-009.md#p-6bfeb9065172b03e) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023080

```text
(exec)# do-exec pnpa service discovery bypass-connectivity-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 10 `；EOL ` RVA 0x33B707C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass connectivity-check: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d33d16eb50948d01](../../evidence/parameters-sets-016.md#p-d33d16eb50948d01) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023077

```text
(exec)# do-exec pnpa service discovery bypass-disc-summary <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 11 `；EOL ` RVA 0x33B704D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8b96e58952d2d5ff](../../evidence/parameters-sets-011.md#p-8b96e58952d2d5ff) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023076

```text
(exec)# do-exec pnpa service discovery bypass-dns-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 12 `；EOL ` RVA 0x33B701E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-421bea45088742c0](../../evidence/parameters-sets-006.md#p-421bea45088742c0) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023070

```text
(exec)# do-exec pnpa service discovery bypass-https-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 13 `；EOL ` RVA 0x33B6FEF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass https-enforcement: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-78a3b7af483fb70c](../../evidence/parameters-sets-009.md#p-78a3b7af483fb70c) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023065

```text
(exec)# do-exec pnpa service discovery bypass-napp-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 14 `；EOL ` RVA 0x33B6FC00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass napp check: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7c9aff8094b54082](../../evidence/parameters-sets-010.md#p-7c9aff8094b54082) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023060

```text
(exec)# do-exec pnpa service discovery bypass-startup-config <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 15 `；EOL ` RVA 0x33B6F910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8fe566dc6aeaefb0](../../evidence/parameters-sets-011.md#p-8fe566dc6aeaefb0) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023054

```text
(exec)# do-exec pnpa service discovery bypass-webui-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 16 `；EOL ` RVA 0x33B6F620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass webui check: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-005812e8002c86c7](../../evidence/parameters-sets-001.md#p-005812e8002c86c7) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023049

```text
(exec)# do-exec pnpa service discovery bypass-wizard-input <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 17 `；EOL ` RVA 0x33B6F330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bypass wizard: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-823f4c048ce7250d](../../evidence/parameters-sets-010.md#p-823f4c048ce7250d) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020135

```text
(exec)# do-exec pnpa service discovery clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 18 `；EOL ` RVA 0x33B6F020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024501

```text
(exec)# do-exec pnpa service discovery dhcp ipv4 <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 19 `；EOL ` RVA 0x33B6ED88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify a DHCP op43 string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b249e0108e8433a5](../../evidence/parameters-sets-014.md#p-b249e0108e8433a5) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024495

```text
(exec)# do-exec pnpa service discovery dhcp ipv6 <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 20 `；EOL ` RVA 0x33B6EAC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify a DHCP op17 string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-797f0695c9572a5c](../../evidence/parameters-sets-009.md#p-797f0695c9572a5c) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020120

```text
(exec)# do-exec pnpa service discovery dns-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 21 `；EOL ` RVA 0x33B6E750 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023041

```text
(exec)# do-exec pnpa service discovery dns-set <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 22 `；EOL ` RVA 0x33B6E4D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the DNS domain-name-cache。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e8db970f70a49b74](../../evidence/parameters-sets-017.md#p-e8db970f70a49b74) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023039

```text
(exec)# do-exec pnpa service discovery method-disable <number:0..15> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 23 `；EOL ` RVA 0x33B6E1E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` discovery method。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-932466822764f01b](../../evidence/parameters-sets-011.md#p-932466822764f01b) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023036

```text
(exec)# do-exec pnpa service discovery method-enable <number:0..15> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 24 `；EOL ` RVA 0x33B6DEF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` discovery method。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f8ffaac76d709e73](../../evidence/parameters-sets-019.md#p-f8ffaac76d709e73) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020103

```text
(exec)# do-exec pnpa service discovery method-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 25 `；EOL ` RVA 0x33B6DBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020094

```text
(exec)# do-exec pnpa service discovery no-shutdown <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 26 `；EOL ` RVA 0x33B6D938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-023016

```text
(exec)# do-exec pnpa service discovery server-credential <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 27 `；EOL ` RVA 0x33B6D6B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Server Credential: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-6fe7d1a6a6e7cd5c](../../evidence/parameters-sets-009.md#p-6fe7d1a6a6e7cd5c) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020076

```text
(exec)# do-exec pnpa service discovery setup-abort <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 28 `；EOL ` RVA 0x33B6D3A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020070

```text
(exec)# do-exec pnpa service discovery shutdown <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 29 `；EOL ` RVA 0x33B6D0F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020058

```text
(exec)# do-exec pnpa service discovery start <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 30 `；EOL ` RVA 0x33B6CE50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020047

```text
(exec)# do-exec pnpa service discovery stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 31 `；EOL ` RVA 0x33B6CBA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024467

```text
(exec)# do-exec pnpa service discovery terminate <number:0..11> <number:0..14> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 32 `；EOL ` RVA 0x33B6C920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Requested By；` unsigned_number ` Reason。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-18dd944bfc769b57](../../evidence/parameters-sets-002.md#p-18dd944bfc769b57) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022984

```text
(exec)# do-exec pnpa service discovery wait-for-stop <number:0..7200> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 33 `；EOL ` RVA 0x33B6C5E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Max wait time in seconds。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5100fe36e66f0cae](../../evidence/parameters-sets-007.md#p-5100fe36e66f0cae) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-020021

```text
(exec)# do-exec pnpa service do-change-mode <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 34 `；EOL ` RVA 0x33B6C298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` node mode - autonomous, controller。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2bfc1edfe80ede81](../../evidence/parameters-sets-004.md#p-2bfc1edfe80ede81) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015826

```text
(exec)# do-exec pnpa service do-write-erase <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 35 `；EOL ` RVA 0x33B6BF88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015816

```text
(exec)# do-exec pnpa service do-write-memory <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 36 `；EOL ` RVA 0x33B6BCE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019709

```text
(exec)# do-exec pnpa service eem-proxy <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 77 `；EOL ` RVA 0x33B66098 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) eem-proxy。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-773136487d0b76af](../../evidence/parameters-sets-009.md#p-773136487d0b76af) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024442

```text
(exec)# do-exec pnpa service event-notify <number:0..29> <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 37 `；EOL ` RVA 0x33B6AEE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` event to notify；` string ` notified by；` string ` notified reason。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-f5bb9b810c9641cc](../../evidence/parameters-sets-018.md#p-f5bb9b810c9641cc) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019684

```text
(exec)# do-exec pnpa service fault-control <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 78 `；EOL ` RVA 0x33B65A48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` fault-control level: 1-strict, 0-none。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bbf3a30fd9ffe120](../../evidence/parameters-sets-014.md#p-bbf3a30fd9ffe120) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024900

```text
(exec)# do-exec pnpa service hello <string> <string> <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 38 `；EOL ` RVA 0x33B6AB38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the protocol；` string ` Specify the host, ipv4, or ipv6；` string ` Specify the host or ipaddr；` unsigned_number ` Specify the hello port。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4c01acc227679362](../../evidence/parameters-sets-006.md#p-4c01acc227679362) · [状态效果 S-bb532e8b52939855](../../evidence/state_effects-sets-040.md#s-bb532e8b52939855)

### path-019960

```text
(exec)# do-exec pnpa service image-install <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 39 `；EOL ` RVA 0x33B6A080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the Image source file path。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-756361a048212659](../../evidence/parameters-sets-009.md#p-756361a048212659) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015736

```text
(exec)# do-exec pnpa service image-install-commit <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 41 `；EOL ` RVA 0x33B6A468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015744

```text
(exec)# do-exec pnpa service image-remove-inactive <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 40 `；EOL ` RVA 0x33B6A710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-017839

```text
(exec)# do-exec pnpa service internal <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 79 `；EOL ` RVA 0x33B530C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` service-control: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b3d83bc3bb62d34d](../../evidence/parameters-sets-014.md#p-b3d83bc3bb62d34d) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022795

```text
(exec)# do-exec pnpa service location-tag <number:0..1> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 80 `；EOL ` RVA 0x33B65760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) location tag；` string ` Specify location tag。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3c6c42bcdf2c6780](../../evidence/parameters-sets-005.md#p-3c6c42bcdf2c6780) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019670

```text
(exec)# do-exec pnpa service lock-bypass <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 81 `；EOL ` RVA 0x33B65428 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-b2dd957f6c9ed270](../../evidence/parameters-sets-014.md#p-b2dd957f6c9ed270) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015359

```text
(exec)# do-exec pnpa service lock-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 82 `；EOL ` RVA 0x33B65118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015347

```text
(exec)# do-exec pnpa service lock-exec <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 83 `；EOL ` RVA 0x33B64E70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019643

```text
(exec)# do-exec pnpa service monvar-diag <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 84 `；EOL ` RVA 0x33B64BF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` diag monvar string (null to reset)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fb47b9e711cb8226](../../evidence/parameters-sets-019.md#p-fb47b9e711cb8226) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019605

```text
(exec)# do-exec pnpa service must-ignore-config-reg <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 86 `；EOL ` RVA 0x33B64320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore config-reg: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-de80c47601a0703a](../../evidence/parameters-sets-017.md#p-de80c47601a0703a) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019618

```text
(exec)# do-exec pnpa service must-ignore-config-rollback <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 87 `；EOL ` RVA 0x33B64610 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore config-rollback: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-82d10f2cdf8d90c8](../../evidence/parameters-sets-010.md#p-82d10f2cdf8d90c8) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019592

```text
(exec)# do-exec pnpa service must-ignore-dir-walk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 88 `；EOL ` RVA 0x33B64030 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore dir-walk: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e79ae40db74922a6](../../evidence/parameters-sets-017.md#p-e79ae40db74922a6) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019578

```text
(exec)# do-exec pnpa service must-ignore-ifs-walk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 89 `；EOL ` RVA 0x33B63D40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore ifs-walk: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3e18d8cfbde56d01](../../evidence/parameters-sets-005.md#p-3e18d8cfbde56d01) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019564

```text
(exec)# do-exec pnpa service must-ignore-image-signature <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 90 `；EOL ` RVA 0x33B63A50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore image-signature: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cba6357f2c967325](../../evidence/parameters-sets-015.md#p-cba6357f2c967325) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019548

```text
(exec)# do-exec pnpa service must-ignore-reload-info <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 91 `；EOL ` RVA 0x33B63760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore reload_info: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-901d0977f1754861](../../evidence/parameters-sets-011.md#p-901d0977f1754861) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019629

```text
(exec)# do-exec pnpa service must-ignore-reload-info <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 85 `；EOL ` RVA 0x33B64900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must block reload-info: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-75b90c2e33b7f873](../../evidence/parameters-sets-009.md#p-75b90c2e33b7f873) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019539

```text
(exec)# do-exec pnpa service must-ignore-save-tech <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 92 `；EOL ` RVA 0x33B63470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore save-tech: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-46b4ad70bc846593](../../evidence/parameters-sets-006.md#p-46b4ad70bc846593) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019528

```text
(exec)# do-exec pnpa service must-ignore-terminate-now <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 93 `；EOL ` RVA 0x33B63180 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must ignore terminate now: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-df4cb64e4a88b1b6](../../evidence/parameters-sets-017.md#p-df4cb64e4a88b1b6) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019515

```text
(exec)# do-exec pnpa service must-keep-backup <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 94 `；EOL ` RVA 0x33B62E90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Must keep backup: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-17d217b95f009eb6](../../evidence/parameters-sets-002.md#p-17d217b95f009eb6) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019521

```text
(exec)# do-exec pnpa service napp-client <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 95 `；EOL ` RVA 0x33B62BA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NAPP Client: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cf109c9cb28e456d](../../evidence/parameters-sets-016.md#p-cf109c9cb28e456d) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019504

```text
(exec)# do-exec pnpa service napp-connect <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 96 `；EOL ` RVA 0x33B62870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` device SN。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-00c5eff6a64f2197](../../evidence/parameters-sets-001.md#p-00c5eff6a64f2197) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015135

```text
(exec)# do-exec pnpa service napp-http-server <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 97 `；EOL ` RVA 0x33B62540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019487

```text
(exec)# do-exec pnpa service napp-server <number:0..2> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 98 `；EOL ` RVA 0x33B62250 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NAPP Server: 2-enable-chunking, 1-enable-no-chunking, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bf25eff6457a3b12](../../evidence/parameters-sets-015.md#p-bf25eff6457a3b12) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015086

```text
(exec)# do-exec pnpa service napp-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 99 `；EOL ` RVA 0x33B61EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019468

```text
(exec)# do-exec pnpa service napp-tag <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 100 `；EOL ` RVA 0x33B61C78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` device SN。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8b528813987481c3](../../evidence/parameters-sets-011.md#p-8b528813987481c3) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019901

```text
(exec)# do-exec pnpa service notify-now <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 42 `；EOL ` RVA 0x33B69BA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Profile to be notified。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-68f9ccd4c3539287](../../evidence/parameters-sets-008.md#p-68f9ccd4c3539287) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024896

```text
(exec)# do-exec pnpa service notify-service <string> <string> <string> <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 43 `；EOL ` RVA 0x33B698B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the notification type: syslog, snmp；` string ` Specify the severity；` string ` Specify the recipient；` unsigned_number ` Notify control: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-70161dd8932d3652](../../evidence/parameters-sets-009.md#p-70161dd8932d3652) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019880

```text
(exec)# do-exec pnpa service notify-state <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 44 `；EOL ` RVA 0x33B69510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` state msg to be notified。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d4291a2f9dc3d499](../../evidence/parameters-sets-016.md#p-d4291a2f9dc3d499) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019436

```text
(exec)# do-exec pnpa service post-reload-priv <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 101 `；EOL ` RVA 0x33B61948 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Load(1) or save(0) post-reload-priv。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a9530d319e417cdb](../../evidence/parameters-sets-013.md#p-a9530d319e417cdb) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019440

```text
(exec)# do-exec pnpa service proxy-control <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 102 `；EOL ` RVA 0x33B61658 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Proxy control: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d5e8c07eed1f0020](../../evidence/parameters-sets-016.md#p-d5e8c07eed1f0020) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019416

```text
(exec)# do-exec pnpa service python-listener <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 111 `；EOL ` RVA 0x33B61320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Python Listener: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-c6f3c8aa68a370fd](../../evidence/parameters-sets-015.md#p-c6f3c8aa68a370fd) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-025072

```text
(exec)# do-exec pnpa service query-to-client <string> <string> <string> configlet <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 112 `；EOL ` RVA 0x33B61028 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` napp version string；` string ` UDI string；` string ` transaction id string；` string ` configlet string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0e1b8d2f679cba72](../../evidence/parameters-sets-002.md#p-0e1b8d2f679cba72) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024309

```text
(exec)# do-exec pnpa service query-to-server <string> <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 113 `；EOL ` RVA 0x33B60C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` napp version string；` string ` UDI string；` string ` transaction id string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fa2c7c877e60c096](../../evidence/parameters-sets-019.md#p-fa2c7c877e60c096) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022880

```text
(exec)# do-exec pnpa service redirect-backup <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 46 `；EOL ` RVA 0x33B69220 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the redierction profile；` unsigned_number ` Specify redirection port (0 for as-is)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a45206e0307fbffc](../../evidence/parameters-sets-013.md#p-a45206e0307fbffc) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022874

```text
(exec)# do-exec pnpa service redirect-primary <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 47 `；EOL ` RVA 0x33B68EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the redierction profile；` unsigned_number ` Specify redirection port (0 for as-is)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-194db4a6cc116691](../../evidence/parameters-sets-002.md#p-194db4a6cc116691) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019892

```text
(exec)# do-exec pnpa service reload cancel <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 48 `；EOL ` RVA 0x33B68928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fc5a157def6e81f3](../../evidence/state_effects-sets-053.md#s-fc5a157def6e81f3)

### path-015452

```text
(exec)# do-exec pnpa service reset <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 45 `；EOL ` RVA 0x33B65D88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019381

```text
(exec)# do-exec pnpa service resolve-discovery <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 114 `；EOL ` RVA 0x33B608A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` hostname string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-9752fb71a61bd149](../../evidence/parameters-sets-012.md#p-9752fb71a61bd149) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019365

```text
(exec)# do-exec pnpa service resolve-dns <number:0..4> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 115 `；EOL ` RVA 0x33B605B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Resolution: 0-default, 1-v4-only, 2-v6-only, 3-v4-first, 4-v6-first。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fecb2817928f3c6a](../../evidence/parameters-sets-019.md#p-fecb2817928f3c6a) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019373

```text
(exec)# do-exec pnpa service resolve-hostname <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 116 `；EOL ` RVA 0x33B602C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` hostname string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-82fa424a0db43254](../../evidence/parameters-sets-010.md#p-82fa424a0db43254) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015643

```text
(exec)# do-exec pnpa service save-tech <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 49 `；EOL ` RVA 0x33B68520 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019850

```text
(exec)# do-exec pnpa service script <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 50 `；EOL ` RVA 0x33B68190 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Location of the script。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-588eb97ffa148d20](../../evidence/parameters-sets-007.md#p-588eb97ffa148d20) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015782

```text
(exec)# do-exec pnpa service sdwan-ready <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 53 `；EOL ` RVA 0x33B6B4A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019996

```text
(exec)# do-exec pnpa service sdwan-start <number:0..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 51 `；EOL ` RVA 0x33B6BA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sdwan use case。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-4916a1a60f87a02b](../../evidence/parameters-sets-006.md#p-4916a1a60f87a02b) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-015791

```text
(exec)# do-exec pnpa service sdwan-stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 52 `；EOL ` RVA 0x33B6B748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019328

```text
(exec)# do-exec pnpa service security-ending-max <number:1..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 117 `；EOL ` RVA 0x33B5FF90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` security ending max length。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-e9119277ed6a8fe9](../../evidence/parameters-sets-017.md#p-e9119277ed6a8fe9) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019318

```text
(exec)# do-exec pnpa service security-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 118 `；EOL ` RVA 0x33B5FCA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enforce security: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-298e91827eac381c](../../evidence/parameters-sets-004.md#p-298e91827eac381c) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019194

```text
(exec)# do-exec pnpa service server-identity-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 124 `；EOL ` RVA 0x33B5E210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Server ID validation: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-da1cfe4bd7b3fe2c](../../evidence/parameters-sets-016.md#p-da1cfe4bd7b3fe2c) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019288

```text
(exec)# do-exec pnpa service show-file <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 54 `；EOL ` RVA 0x33B5F9B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ee232f3ef7c1c75f](../../evidence/parameters-sets-018.md#p-ee232f3ef7c1c75f) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014927

```text
(exec)# do-exec pnpa service show-running-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 55 `；EOL ` RVA 0x33B5F6A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014913

```text
(exec)# do-exec pnpa service show-startup-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 56 `；EOL ` RVA 0x33B5F400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022554

```text
(exec)# do-exec pnpa service sid auth-only <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 119 `；EOL ` RVA 0x33B5F138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SID auth only: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-90477e5f166ab209](../../evidence/parameters-sets-011.md#p-90477e5f166ab209) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022527

```text
(exec)# do-exec pnpa service sid must-renew <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 121 `；EOL ` RVA 0x33B5EB80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SID must renew: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-32c2d63e16682f7f](../../evidence/parameters-sets-004.md#p-32c2d63e16682f7f) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022543

```text
(exec)# do-exec pnpa service sid must-validate <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 120 `；EOL ` RVA 0x33B5EE70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SID must validate: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-12062fb47306577e](../../evidence/parameters-sets-002.md#p-12062fb47306577e) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024276

```text
(exec)# do-exec pnpa service sid update <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 122 `；EOL ` RVA 0x33B5E898 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the new sid；` string ` Specify the profile。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-47ee00b12a0b4c47](../../evidence/parameters-sets-006.md#p-47ee00b12a0b4c47) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-022482

```text
(exec)# do-exec pnpa service sid validation <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 123 `；EOL ` RVA 0x33B5E568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SID validation: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a88bef6bb1b4f758](../../evidence/parameters-sets-013.md#p-a88bef6bb1b4f758) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019164

```text
(exec)# do-exec pnpa service sleep-for <number:1..3600> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 125 `；EOL ` RVA 0x33B5DF20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` sleep time in seconds (No ctrl-C)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7a7e08538b1b49a5](../../evidence/parameters-sets-010.md#p-7a7e08538b1b49a5) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019148

```text
(exec)# do-exec pnpa service smu-task-activate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 57 `；EOL ` RVA 0x33B5DC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d1cb7f9bcdcf753d](../../evidence/parameters-sets-016.md#p-d1cb7f9bcdcf753d) · [状态效果 S-32e6bdcfea4262fa](../../evidence/state_effects-sets-011.md#s-32e6bdcfea4262fa)

### path-022432

```text
(exec)# do-exec pnpa service smu-task-add <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 58 `；EOL ` RVA 0x33B5D920 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the bundle name；` string ` Specify the bundle URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3dbbe73eff66b8a0](../../evidence/parameters-sets-005.md#p-3dbbe73eff66b8a0) · [状态效果 S-3f6c28582650e08c](../../evidence/state_effects-sets-014.md#s-3f6c28582650e08c)

### path-014835

```text
(exec)# do-exec pnpa service smu-task-clear-all <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 59 `；EOL ` RVA 0x33B5D548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-267285140fb11c38](../../evidence/state_effects-sets-009.md#s-267285140fb11c38)

### path-014816

```text
(exec)# do-exec pnpa service smu-task-commit <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 60 `；EOL ` RVA 0x33B5D290 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2e0fcf488becc151](../../evidence/state_effects-sets-010.md#s-2e0fcf488becc151)

### path-019046

```text
(exec)# do-exec pnpa service smu-task-deactivate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 61 `；EOL ` RVA 0x33B5D010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-5b889fd0e2d4722a](../../evidence/parameters-sets-007.md#p-5b889fd0e2d4722a) · [状态效果 S-a80750de4820bdab](../../evidence/state_effects-sets-035.md#s-a80750de4820bdab)

### path-019014

```text
(exec)# do-exec pnpa service smu-task-remove <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 62 `；EOL ` RVA 0x33B5CD18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-ee910b235e862416](../../evidence/parameters-sets-018.md#p-ee910b235e862416) · [状态效果 S-1ca7a679a946ad24](../../evidence/state_effects-sets-007.md#s-1ca7a679a946ad24)

### path-014767

```text
(exec)# do-exec pnpa service smu-task-run <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 63 `；EOL ` RVA 0x33B5C9E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3a4b68675ecd42f2](../../evidence/state_effects-sets-013.md#s-3a4b68675ecd42f2)

### path-014753

```text
(exec)# do-exec pnpa service smu-task-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 64 `；EOL ` RVA 0x33B5C730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f39e96b498fd7bf1](../../evidence/state_effects-sets-051.md#s-f39e96b498fd7bf1)

### path-018954

```text
(exec)# do-exec pnpa service smu-verify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 65 `；EOL ` RVA 0x33B5C490 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-cc0b46ba0581021b](../../evidence/parameters-sets-015.md#p-cc0b46ba0581021b) · [状态效果 S-6980a22c72583acf](../../evidence/state_effects-sets-023.md#s-6980a22c72583acf)

### path-018863

```text
(exec)# do-exec pnpa service snmp <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 126 `；EOL ` RVA 0x33B5C130 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the request SNMP PDU in Base64。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-94473c5c84f29ce8](../../evidence/parameters-sets-011.md#p-94473c5c84f29ce8) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-024151

```text
(exec)# do-exec pnpa service snooping <number:0..1> <number:0..4094> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 127 `；EOL ` RVA 0x33B5BE48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enforce snooping: 1-enable, 0-disable；` unsigned_number ` vlan id；` string ` Specify the dhcp option string (null to unset)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d9f80e33b5e3a816](../../evidence/parameters-sets-016.md#p-d9f80e33b5e3a816) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018767

```text
(exec)# do-exec pnpa service stack-renumber <number:1..9> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 128 `；EOL ` RVA 0x33B5B7D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Top of stack switch number: 1-9。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1800deaa8355c918](../../evidence/parameters-sets-002.md#p-1800deaa8355c918) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018805

```text
(exec)# do-exec pnpa service stack-reorder <number:1..9> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 129 `；EOL ` RVA 0x33B5BAC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Top of stack switch number: 1-9。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a790aecbeed8eeb9](../../evidence/parameters-sets-013.md#p-a790aecbeed8eeb9) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-019981

```text
(exec)# do-exec pnpa service tls-tunnel-notify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 152 `；EOL ` RVA 0x33B6B218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` tls tunnel name。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1da18c2d26058ef1](../../evidence/parameters-sets-003.md#p-1da18c2d26058ef1) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018738

```text
(exec)# do-exec pnpa service token-auth-set <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 130 `；EOL ` RVA 0x33B5B4F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the token-auth string。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b905f8bac36bef9](../../evidence/parameters-sets-010.md#p-7b905f8bac36bef9) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-021944

```text
(exec)# do-exec pnpa service trustpoint-install <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 153 `；EOL ` RVA 0x33B57AC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the trustpoint label；` string ` Specify the certificate URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-d3f8cd0bf21cc6a9](../../evidence/parameters-sets-016.md#p-d3f8cd0bf21cc6a9) · [状态效果 S-78b8513e786bdb59](../../evidence/state_effects-sets-026.md#s-78b8513e786bdb59)

### path-018221

```text
(exec)# do-exec pnpa service trustpoint-uninstall <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 154 `；EOL ` RVA 0x33B57720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the trustpoint label。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fcbe95cdcfbd4544](../../evidence/parameters-sets-019.md#p-fcbe95cdcfbd4544) · [状态效果 S-94d4cf1b960aebd2](../../evidence/state_effects-sets-032.md#s-94d4cf1b960aebd2)

### path-018233

```text
(exec)# do-exec pnpa service trustpool-install <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 155 `；EOL ` RVA 0x33B57408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the bundle URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-043798f3537f3872](../../evidence/parameters-sets-001.md#p-043798f3537f3872) · [状态效果 S-6f6d68490401ab72](../../evidence/state_effects-sets-024.md#s-6f6d68490401ab72)

### path-014233

```text
(exec)# do-exec pnpa service trustpool-uninstall <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 156 `；EOL ` RVA 0x33B57070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3af4d7c07ae5888a](../../evidence/state_effects-sets-013.md#s-3af4d7c07ae5888a)

### path-018709

```text
(exec)# do-exec pnpa service udi-checking <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 131 `；EOL ` RVA 0x33B5B200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Enforce udi checking: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-47ae8fb6c02bac0d](../../evidence/parameters-sets-006.md#p-47ae8fb6c02bac0d) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014609

```text
(exec)# do-exec pnpa service udi-refresh <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 132 `；EOL ` RVA 0x33B5AEF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014583

```text
(exec)# do-exec pnpa service unlock-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 133 `；EOL ` RVA 0x33B5AC48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014564

```text
(exec)# do-exec pnpa service unlock-exec <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 134 `；EOL ` RVA 0x33B5A9A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018602

```text
(exec)# do-exec pnpa service use-ntp-server <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 135 `；EOL ` RVA 0x33B5A720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the ntp server name (null to unset)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-dd997acde6d6e31b](../../evidence/parameters-sets-017.md#p-dd997acde6d6e31b) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018574

```text
(exec)# do-exec pnpa service use-src-intf <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 136 `；EOL ` RVA 0x33B5A438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the source interface name (null to unset)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7b726c2f0dd3a7ec](../../evidence/parameters-sets-010.md#p-7b726c2f0dd3a7ec) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018551

```text
(exec)# do-exec pnpa service use-unix-disk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 137 `；EOL ` RVA 0x33B5A148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Use Unix disk: 1-Yes, 0-No。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2757a78edd0c9a69](../../evidence/parameters-sets-003.md#p-2757a78edd0c9a69) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018526

```text
(exec)# do-exec pnpa service use-vrf <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 138 `；EOL ` RVA 0x33B59E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the vrf name (null to unset)。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-51080c07389089a0](../../evidence/parameters-sets-007.md#p-51080c07389089a0) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018197

```text
(exec)# do-exec pnpa service validate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 157 `；EOL ` RVA 0x33B56DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2cd423664f9b5606](../../evidence/parameters-sets-004.md#p-2cd423664f9b5606) · [状态效果 S-16ec0250ab84fe76](../../evidence/state_effects-sets-005.md#s-16ec0250ab84fe76)

### path-017849

```text
(exec)# do-exec pnpa service verbose <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 139 `；EOL ` RVA 0x33B533B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` verbose-control: 1-enable, 0-disable。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-be51a107b43ad9ed](../../evidence/parameters-sets-014.md#p-be51a107b43ad9ed) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018184

```text
(exec)# do-exec pnpa service verify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 158 `；EOL ` RVA 0x33B56A50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-24b3cb7039281dd9](../../evidence/parameters-sets-003.md#p-24b3cb7039281dd9) · [状态效果 S-93c2de614276ace7](../../evidence/state_effects-sets-031.md#s-93c2de614276ace7)

### path-018163

```text
(exec)# do-exec pnpa service wait-time <number:0..100> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 159 `；EOL ` RVA 0x33B566C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` wait type。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-2cca3fb3c6cbf767](../../evidence/parameters-sets-004.md#p-2cca3fb3c6cbf767) · [状态效果 S-e81c33b99d42ed8d](../../evidence/state_effects-sets-049.md#s-e81c33b99d42ed8d)

### path-014496

```text
(exec)# do-exec pnpa service wakeup <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 140 `；EOL ` RVA 0x33B59B78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014161

```text
(exec)# do-exec pnpa service watch-ack-notifications <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 160 `；EOL ` RVA 0x33B56338 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014149

```text
(exec)# do-exec pnpa service watch-all <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 161 `；EOL ` RVA 0x33B56090 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014135

```text
(exec)# do-exec pnpa service watch-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 162 `；EOL ` RVA 0x33B55DE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014122

```text
(exec)# do-exec pnpa service watch-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 163 `；EOL ` RVA 0x33B55B40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018043

```text
(exec)# do-exec pnpa service watch-default-action <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 164 `；EOL ` RVA 0x33B55810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` action to take - wakeup-pnp-server-now, notify-pnp-server-now, syslog, etc.。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-eb9e86917c1668d8](../../evidence/parameters-sets-018.md#p-eb9e86917c1668d8) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-021860

```text
(exec)# do-exec pnpa service watch-disable <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 165 `；EOL ` RVA 0x33B554C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` watch_id；` string ` event to unwatch。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-bc901cb7b87b0261](../../evidence/parameters-sets-014.md#p-bc901cb7b87b0261) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-025042

```text
(exec)# do-exec pnpa service watch-enable <string> <string> <string> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 166 `；EOL ` RVA 0x33B550E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` watch_id；` string ` event to watch；` string ` event param str ("null" for default)；` unsigned_number ` event param value；` string ` action to take - wakeup-pnp-server-now, notify-pnp-server-now, syslog, etc.。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-eb5241440f036fd2](../../evidence/parameters-sets-018.md#p-eb5241440f036fd2) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014063

```text
(exec)# do-exec pnpa service watch-pnp-profile <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 167 `；EOL ` RVA 0x33B54C68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014041

```text
(exec)# do-exec pnpa service watch-pnp-server <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 168 `；EOL ` RVA 0x33B549C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014025

```text
(exec)# do-exec pnpa service watch-pnp-service <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 169 `；EOL ` RVA 0x33B54718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014009

```text
(exec)# do-exec pnpa service watch-pnp-state <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 170 `；EOL ` RVA 0x33B54470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-013988

```text
(exec)# do-exec pnpa service watch-system <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 171 `；EOL ` RVA 0x33B541C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-013970

```text
(exec)# do-exec pnpa service watch-tls-tunnel <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 172 `；EOL ` RVA 0x33B53F20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-017900

```text
(exec)# do-exec pnpa service webui set <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 173 `；EOL ` RVA 0x33B53C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-017883

```text
(exec)# do-exec pnpa service webui start <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 175 `；EOL ` RVA 0x33B53998 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-017864

```text
(exec)# do-exec pnpa service webui stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 174 `；EOL ` RVA 0x33B536A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014454

```text
(exec)# do-exec pnpa service xep-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 141 `；EOL ` RVA 0x33B59868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018447

```text
(exec)# do-exec pnpa service xep-ignore-disconnect <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 142 `；EOL ` RVA 0x33B595E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Ignore Disconnect: 0-no, 1-yes。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a80109c842869060](../../evidence/parameters-sets-013.md#p-a80109c842869060) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014417

```text
(exec)# do-exec pnpa service xep-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 143 `；EOL ` RVA 0x33B592D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018395

```text
(exec)# do-exec pnpa service xep-tracking <number:0..4> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 144 `；EOL ` RVA 0x33B59048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` xep-tracking: 0-none, 1-all, 2-Rx, 3-Tx, 4-Drop。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-869afff84899f879](../../evidence/parameters-sets-010.md#p-869afff84899f879) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014387

```text
(exec)# do-exec pnpa service xml-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 145 `；EOL ` RVA 0x33B58D38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018346

```text
(exec)# do-exec pnpa service xml-process <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 146 `；EOL ` RVA 0x33B58AB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the URL of a text file containing the XML message。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-7a094047a2aab620](../../evidence/parameters-sets-010.md#p-7a094047a2aab620) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-025053

```text
(exec)# do-exec pnpa service xml-profile <string> <string> <string> <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 147 `；EOL ` RVA 0x33B587C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the profile for XML encoding；` string ` Specify the protocol；` string ` Specify the host, ipv4, or ipv6；` string ` Specify the host or ipaddr；` unsigned_number ` Specify the svc_xml_profile port。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0c96bbfdba221420](../../evidence/parameters-sets-001.md#p-0c96bbfdba221420) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-014337

```text
(exec)# do-exec pnpa service xml-replay <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 148 `；EOL ` RVA 0x33B583B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-018271

```text
(exec)# do-exec pnpa service xml-udi <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 149 `；EOL ` RVA 0x33B58138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the udi for XML encoding。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-75dab89d28d346c4](../../evidence/parameters-sets-009.md#p-75dab89d28d346c4) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-021954

```text
(exec)# do-exec pnpa service xml-usr <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 150 `；EOL ` RVA 0x33B57E48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the usr for XML encoding；` string ` Specify the pwd for XML encoding。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8a1bb1606a99457c](../../evidence/parameters-sets-011.md#p-8a1bb1606a99457c) · [状态效果 S-65fe7650aa30143c](../../evidence/state_effects-sets-022.md#s-65fe7650aa30143c)

### path-012540

```text
(exec)# do-exec pnpa summary <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 151 `；EOL ` RVA 0x33B52D60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-024550

```text
(exec)# do-exec processes cpu pid <number:1..4294967295> autoprofile threshold <number:50..400> <cr>
```

Handler ` RVA 0xE086C10 `；selector ` 2 `；EOL ` RVA 0x341DB8E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

参数提示：` unsigned_number ` Process ID to use；` unsigned_number ` Threshold (in msec) after which profiling is turned on。

[条件 C-a952545d99f90774](../../evidence/conditions-sets-065.md#c-a952545d99f90774) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-69efa937186747a6](../../evidence/parameters-sets-008.md#p-69efa937186747a6) · [状态效果 S-f80634651e1461e1](../../evidence/state_effects-sets-052.md#s-f80634651e1461e1)

### path-023331

```text
(exec)# do-exec processes cpu pid <number:1..4294967295> priority low <cr>
```

Handler ` RVA 0xE0877D0 `；selector ` 0 `；EOL ` RVA 0x341DBBE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

参数提示：` unsigned_number ` Process ID to use。

[条件 C-fdd09317c23a9f7e](../../evidence/conditions-sets-098.md#c-fdd09317c23a9f7e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-47072628751ce24e](../../evidence/parameters-sets-006.md#p-47072628751ce24e) · [状态效果 S-c5b9c194c35d84ab](../../evidence/state_effects-sets-042.md#s-c5b9c194c35d84ab)

### path-023340

```text
(exec)# do-exec processes cpu pid <number:1..4294967295> quantum <number:20..200> <cr>
```

Handler ` RVA 0xE087650 `；selector ` 0 `；EOL ` RVA 0x341DBFD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [1,null,0] `。

参数提示：` unsigned_number ` Process ID to use；` unsigned_number ` quantum value in msec。

[条件 C-bd4372c855e9b561](../../evidence/conditions-sets-073.md#c-bd4372c855e9b561) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-49d326b177f30f6d](../../evidence/parameters-sets-006.md#p-49d326b177f30f6d) · [状态效果 S-f80634651e1461e1](../../evidence/state_effects-sets-052.md#s-f80634651e1461e1)

### path-012289

```text
(exec)# do-exec profile hogs <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 4 `；EOL ` RVA 0x34122D98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc6dc89545a92ace](../../evidence/conditions-sets-079.md#c-cc6dc89545a92ace) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b8a6dbe3ca7fbffb](../../evidence/state_effects-sets-039.md#s-b8a6dbe3ca7fbffb)

### path-012282

```text
(exec)# do-exec profile start <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 2 `；EOL ` RVA 0x34122848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc6dc89545a92ace](../../evidence/conditions-sets-079.md#c-cc6dc89545a92ace) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b8a6dbe3ca7fbffb](../../evidence/state_effects-sets-039.md#s-b8a6dbe3ca7fbffb)

### path-012286

```text
(exec)# do-exec profile stop <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 3 `；EOL ` RVA 0x34122AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc6dc89545a92ace](../../evidence/conditions-sets-079.md#c-cc6dc89545a92ace) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b8a6dbe3ca7fbffb](../../evidence/state_effects-sets-039.md#s-b8a6dbe3ca7fbffb)

### path-012268

```text
(exec)# do-exec pwd <cr>
```

Handler ` RVA 0xD6577A0 `；selector ` 0 `；EOL ` RVA 0x33EB9310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-beed373e83d64ab3](../../evidence/conditions-sets-074.md#c-beed373e83d64ab3) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-023394

```text
(exec)# do-exec redundancy application reload group <number:1..2> peer <cr>
```

Handler ` RVA 0xCC27200 `；selector ` 0 `；EOL ` RVA 0x33C22148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group number。

[条件 C-3b1be56d8c475878](../../evidence/conditions-sets-023.md#c-3b1be56d8c475878) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1ea83a5be9f8743b](../../evidence/parameters-sets-003.md#p-1ea83a5be9f8743b) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-023408

```text
(exec)# do-exec redundancy application reload group <number:1..2> self <cr>
```

Handler ` RVA 0xCC27140 `；selector ` 0 `；EOL ` RVA 0x33C223F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` group number。

[条件 C-3b1be56d8c475878](../../evidence/conditions-sets-023.md#c-3b1be56d8c475878) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1ea83a5be9f8743b](../../evidence/parameters-sets-003.md#p-1ea83a5be9f8743b) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-016996

```text
(exec)# do-exec redundancy application test-client disable <cr>
```

Handler ` RVA 0xCC25820 `；selector ` 0 `；EOL ` RVA 0x33C21B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b1be56d8c475878](../../evidence/conditions-sets-023.md#c-3b1be56d8c475878) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-016972

```text
(exec)# do-exec redundancy application test-client enable <cr>
```

Handler ` RVA 0xCC257D0 `；selector ` 0 `；EOL ` RVA 0x33C21870 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b1be56d8c475878](../../evidence/conditions-sets-023.md#c-3b1be56d8c475878) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-012419

```text
(exec)# do-exec redundancy force-switchover <cr>
```

Handler ` RVA 0xD527E60 `；selector ` 0 `；EOL ` RVA 0x33E7AA40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-38c6521e7bd5223d](../../evidence/conditions-sets-022.md#c-38c6521e7bd5223d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-013049

```text
(exec)# do-exec redundancy keepalive enable <cr>
```

Handler ` RVA 0xD527AA0 `；selector ` 0 `；EOL ` RVA 0x33E7A638 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3b1be56d8c475878](../../evidence/conditions-sets-023.md#c-3b1be56d8c475878) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fe64553e3f2b91af](../../evidence/state_effects-sets-054.md#s-fe64553e3f2b91af)

### path-013015

```text
(exec)# do-exec redundancy reload peer <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 8 `；EOL ` RVA 0x33FDA628 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-711679b50eea45f7](../../evidence/conditions-sets-044.md#c-711679b50eea45f7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-013087

```text
(exec)# do-exec redundancy reload shelf <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 9 `；EOL ` RVA 0x33FDAA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6abd2416ff0206b9](../../evidence/conditions-sets-041.md#c-6abd2416ff0206b9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-56ab7332bc811cef](../../evidence/state_effects-sets-019.md#s-56ab7332bc811cef)

### path-012379

```text
(exec)# do-exec redundancy switch-activity <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 6 `；EOL ` RVA 0x33FDA2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-56e4535b3e3848c8](../../evidence/conditions-sets-034.md#c-56e4535b3e3848c8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-bb48cfa3d9a1a82a](../../evidence/state_effects-sets-040.md#s-bb48cfa3d9a1a82a)

### path-012238

```text
(exec)# do-exec reload <cr>
```

Handler ` RVA 0xE004870 `；selector ` 0 `；EOL ` RVA 0x341641B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-21a4e765c37e9f92](../../evidence/conditions-sets-013.md#c-21a4e765c37e9f92) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016725

```text
(exec)# do-exec request consent-token generate-challenge shell-access <cr>
```

Handler ` RVA 0x156982F0 `；selector ` 0 `；EOL ` RVA 0x35D7BAC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ed57db85d0f9e61a](../../evidence/conditions-sets-092.md#c-ed57db85d0f9e61a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ed355d21d6669e7a](../../evidence/state_effects-sets-050.md#s-ed355d21d6669e7a)

### path-012839

```text
(exec)# do-exec request license new-udi <cr>
```

Handler ` RVA 0xBB696E0 `；selector ` 0 `；EOL ` RVA 0x3386A530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4d35e25a34df3c46](../../evidence/conditions-sets-030.md#c-4d35e25a34df3c46) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ce3d030c3c6b5eb9](../../evidence/state_effects-sets-044.md#s-ce3d030c3c6b5eb9)

### path-024534

```text
(exec)# do-exec request platform software netconf-yang key generate rsa <cr>
```

Handler ` RVA 0xE9DA2E0 `；selector ` 0 `；EOL ` RVA 0x34382DD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b003ae83986b21b9](../../evidence/conditions-sets-068.md#c-b003ae83986b21b9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012294

```text
(exec)# do-exec request tech-support <cr>
```

Handler ` RVA 0xEB1FF10 `；selector ` 0 `；EOL ` RVA 0x343B4048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e27e7a595a6840b7](../../evidence/conditions-sets-087.md#c-e27e7a595a6840b7) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-b22113929fef5dcd](../../evidence/state_effects-sets-038.md#s-b22113929fef5dcd)

### path-012249

```text
(exec)# do-exec restart <cr>
```

Handler ` RVA 0xF43B510 `；selector ` 0 `；EOL ` RVA 0x34648EA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c3c1af09156dc8b6](../../evidence/conditions-sets-076.md#c-c3c1af09156dc8b6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-013278

```text
(exec)# do-exec routing-context vrf global <cr>
```

Handler ` RVA 0xE24C600 `；selector ` 0 `；EOL ` RVA 0x34280D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7c9ac1b066f9cc43](../../evidence/conditions-sets-048.md#c-7c9ac1b066f9cc43) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-960648b409e9d0fe](../../evidence/state_effects-sets-032.md#s-960648b409e9d0fe)

### path-013185

```text
(exec)# do-exec rsh <string> <string> <cr>
```

Handler ` RVA 0xD004170 `；selector ` 0 `；EOL ` RVA 0x33D7B938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP address or hostname of rsh server；` string ` Command to be executed remotely。

[条件 C-f40d2a6a2faa6395](../../evidence/conditions-sets-094.md#c-f40d2a6a2faa6395) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-a830d8d1cbc4fe2c](../../evidence/parameters-sets-013.md#p-a830d8d1cbc4fe2c) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-020740

```text
(exec)# do-exec set memory debug incremental starting-time <cr>
```

Handler ` RVA 0xE08DB90 `；selector ` 0 `；EOL ` RVA 0x341E7B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bccacac9276d8f80](../../evidence/conditions-sets-073.md#c-bccacac9276d8f80) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9d285ada20f843a8](../../evidence/state_effects-sets-033.md#s-9d285ada20f843a8)

### path-012228

```text
(exec)# do-exec setup <cr>
```

Handler ` RVA 0xE006400 `；selector ` 0 `；EOL ` RVA 0x341657D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bc27884cd2020a2c](../../evidence/conditions-sets-073.md#c-bc27884cd2020a2c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-012218

```text
(exec)# do-exec show <cr>
```

Handler ` RVA 0xE006240 `；selector ` 0 `；EOL ` RVA 0x34123660 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2908695ef9c4d455](../../evidence/conditions-sets-016.md#c-2908695ef9c4d455) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3417c1d210a6b0dd](../../evidence/state_effects-sets-012.md#s-3417c1d210a6b0dd)

### path-016370

```text
(exec)# do-exec show aaa acct-stop-cache <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 22 `；EOL ` RVA 0x34049A40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7414d56c431002a9](../../evidence/state_effects-sets-025.md#s-7414d56c431002a9)

### path-016241

```text
(exec)# do-exec show aaa attributes <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 1 `；EOL ` RVA 0x34046A68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023122

```text
(exec)# do-exec show aaa cache filterserver acl <cr>
```

Handler ` RVA 0xCD2A340 `；selector ` 0 `；EOL ` RVA 0x34045CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b7bf39aaeae04414](../../evidence/conditions-sets-071.md#c-b7bf39aaeae04414) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023130

```text
(exec)# do-exec show aaa cache filterserver pending <cr>
```

Handler ` RVA 0xCD2A2F0 `；selector ` 0 `；EOL ` RVA 0x34045F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b7bf39aaeae04414](../../evidence/conditions-sets-071.md#c-b7bf39aaeae04414) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024522

```text
(exec)# do-exec show aaa cache group <string> all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 13 `；EOL ` RVA 0x340462F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` AAA SG Cache。

[条件 C-b7bf39aaeae04414](../../evidence/conditions-sets-071.md#c-b7bf39aaeae04414) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-3dca316610ef6909](../../evidence/parameters-sets-005.md#p-3dca316610ef6909) · [状态效果 S-995af3a4c325d8e2](../../evidence/state_effects-sets-033.md#s-995af3a4c325d8e2)

### path-016308

```text
(exec)# do-exec show aaa clients <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 10 `；EOL ` RVA 0x34048400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020424

```text
(exec)# do-exec show aaa command handler <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 11 `；EOL ` RVA 0x34048708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023138

```text
(exec)# do-exec show aaa common-criteria policy all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 23 `；EOL ` RVA 0x34046718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6751fdd54e7ce380](../../evidence/conditions-sets-040.md#c-6751fdd54e7ce380) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016197

```text
(exec)# do-exec show aaa counters <cr>
```

Handler ` RVA 0xDD43740 `；selector ` 0 `；EOL ` RVA 0x340455E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023184

```text
(exec)# do-exec show aaa dead-criteria radius <address> <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 18 `；EOL ` RVA 0x34047E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of the server。

[条件 C-e90777a24d77436b](../../evidence/conditions-sets-090.md#c-e90777a24d77436b) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-78e08a15bf119a7a](../../evidence/parameters-sets-009.md#p-78e08a15bf119a7a) · [状态效果 S-6502ad738310ce2f](../../evidence/state_effects-sets-022.md#s-6502ad738310ce2f)

### path-016444

```text
(exec)# do-exec show aaa fqdn <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 26 `；EOL ` RVA 0x3404A668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-528735a45aa8f970](../../evidence/conditions-sets-032.md#c-528735a45aa8f970) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a0d462f559f12f07](../../evidence/state_effects-sets-034.md#s-a0d462f559f12f07)

### path-016279

```text
(exec)# do-exec show aaa hash <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 4 `；EOL ` RVA 0x340477F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016167

```text
(exec)# do-exec show aaa idmgr <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 20 `；EOL ` RVA 0x340452D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024526

```text
(exec)# do-exec show aaa ipv6 tacacs source-interface global <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 27 `；EOL ` RVA 0x3404AB08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1593c7f239eaac61](../../evidence/state_effects-sets-005.md#s-1593c7f239eaac61)

### path-023128

```text
(exec)# do-exec show aaa local admin_user all <cr>
```

Handler ` RVA 0xDDDD5F0 `；selector ` 0 `；EOL ` RVA 0x33E70E10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-93ec131e2c0c11a5](../../evidence/conditions-sets-057.md#c-93ec131e2c0c11a5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a31515eb9b7148d9](../../evidence/state_effects-sets-035.md#s-a31515eb9b7148d9)

### path-020304

```text
(exec)# do-exec show aaa local statistics <cr>
```

Handler ` RVA 0xD5070E0 `；selector ` 0 `；EOL ` RVA 0x33E70AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023125

```text
(exec)# do-exec show aaa local user blocked <cr>
```

Handler ` RVA 0xD505370 `；selector ` 6 `；EOL ` RVA 0x33E70818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-448af597196fb518](../../evidence/conditions-sets-027.md#c-448af597196fb518) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023114

```text
(exec)# do-exec show aaa local user lockout <cr>
```

Handler ` RVA 0xD505370 `；selector ` 2 `；EOL ` RVA 0x33E70530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016409

```text
(exec)# do-exec show aaa memory <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 19 `；EOL ` RVA 0x34049E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-db749148afcebb55](../../evidence/state_effects-sets-046.md#s-db749148afcebb55)

### path-023195

```text
(exec)# do-exec show aaa memory stats all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 21 `；EOL ` RVA 0x3404A148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-9e5ec921131d7535](../../evidence/state_effects-sets-034.md#s-9e5ec921131d7535)

### path-020337

```text
(exec)# do-exec show aaa method-lists authentication <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 2 `；EOL ` RVA 0x34046D98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-73dc4ff02b7626ed](../../evidence/state_effects-sets-025.md#s-73dc4ff02b7626ed)

### path-020363

```text
(exec)# do-exec show aaa requests statistics <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 24 `；EOL ` RVA 0x34047500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016339

```text
(exec)# do-exec show aaa server-private <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 9 `；EOL ` RVA 0x34048E28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7414d56c431002a9](../../evidence/state_effects-sets-025.md#s-7414d56c431002a9)

### path-016357

```text
(exec)# do-exec show aaa servers <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 8 `；EOL ` RVA 0x34048AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-1b24feb894dbaa64](../../evidence/state_effects-sets-006.md#s-1b24feb894dbaa64)

### path-016365

```text
(exec)# do-exec show aaa service-profiles <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 6 `；EOL ` RVA 0x34049798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7414d56c431002a9](../../evidence/state_effects-sets-025.md#s-7414d56c431002a9)

### path-016347

```text
(exec)# do-exec show aaa sessions <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 5 `；EOL ` RVA 0x340490D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7414d56c431002a9](../../evidence/state_effects-sets-025.md#s-7414d56c431002a9)

### path-020476

```text
(exec)# do-exec show aaa sp-cache all-list <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 7 `；EOL ` RVA 0x34049458 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-3b8bc8f62300069a](../../evidence/state_effects-sets-013.md#s-3b8bc8f62300069a)

### path-020325

```text
(exec)# do-exec show aaa subscriber profile <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 14 `；EOL ` RVA 0x34045958 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9bde7229b9e23164](../../evidence/conditions-sets-060.md#c-9bde7229b9e23164) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023118

```text
(exec)# do-exec show aaa tools memleak statistics <cr>
```

Handler ` RVA 0x1371D720 `；selector ` 0 `；EOL ` RVA 0x35C0D690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d314eccf7019fc9e](../../evidence/state_effects-sets-045.md#s-d314eccf7019fc9e)

### path-016276

```text
(exec)# do-exec show aaa tracebacks <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 12 `；EOL ` RVA 0x34047A98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020347

```text
(exec)# do-exec show aaa user <number:1..4294967295> <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 3 `；EOL ` RVA 0x340471B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Unique Id for a single user。

[条件 C-8c1c7d29f0316f95](../../evidence/conditions-sets-054.md#c-8c1c7d29f0316f95) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-1b01084d2bf088cf](../../evidence/parameters-sets-003.md#p-1b01084d2bf088cf) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012767

```text
(exec)# do-exec show access-expression <cr>
```

Handler ` RVA 0x1E3FDC10 `；selector ` 0 `；EOL ` RVA 0x345E8370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2c3304b68926bad8](../../evidence/conditions-sets-017.md#c-2c3304b68926bad8) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012428

```text
(exec)# do-exec show access-lists <cr>
```

Handler ` RVA 0xE0AE9A0 `；selector ` 0 `；EOL ` RVA 0x34185F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-233bdd092bc14bbb](../../evidence/conditions-sets-014.md#c-233bdd092bc14bbb) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013221

```text
(exec)# do-exec show access-lists acl-limit <cr>
```

Handler ` RVA 0xE0AEF10 `；selector ` 0 `；EOL ` RVA 0x34CEF048 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017075

```text
(exec)# do-exec show access-lists fqdn client <cr>
```

Handler ` RVA 0xCF22230 `；selector ` 0 `；EOL ` RVA 0x33D65A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d7341e3a6db63f3b](../../evidence/state_effects-sets-046.md#s-d7341e3a6db63f3b)

### path-017054

```text
(exec)# do-exec show access-lists fqdn pending-mappings <cr>
```

Handler ` RVA 0xCF24260 `；selector ` 0 `；EOL ` RVA 0x33D65CC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d7341e3a6db63f3b](../../evidence/state_effects-sets-046.md#s-d7341e3a6db63f3b)

### path-017085

```text
(exec)# do-exec show access-lists fqdn statistics <cr>
```

Handler ` RVA 0xCF1BE90 `；selector ` 0 `；EOL ` RVA 0x33D65FB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d7341e3a6db63f3b](../../evidence/state_effects-sets-046.md#s-d7341e3a6db63f3b)

### path-013158

```text
(exec)# do-exec show access-lists ipc <cr>
```

Handler ` RVA 0xCF05960 `；selector ` 0 `；EOL ` RVA 0x33D63E88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013226

```text
(exec)# do-exec show access-lists rate-limit <cr>
```

Handler ` RVA 0x10C68E60 `；selector ` 0 `；EOL ` RVA 0x34CEED88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017080

```text
(exec)# do-exec show access-lists template summary <cr>
```

Handler ` RVA 0xEBB9030 `；selector ` 0 `；EOL ` RVA 0x343D13B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-698ad36d853e3793](../../evidence/conditions-sets-041.md#c-698ad36d853e3793) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a55e6af194c57103](../../evidence/state_effects-sets-035.md#s-a55e6af194c57103)

### path-022695

```text
(exec)# do-exec show access-session limit profile details <cr>
```

Handler ` RVA 0xCAD3890 `；selector ` 0 `；EOL ` RVA 0x33B961C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-776f508d71ee3be9](../../evidence/conditions-sets-046.md#c-776f508d71ee3be9) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-ca75223793c6a88f](../../evidence/state_effects-sets-043.md#s-ca75223793c6a88f)

### path-015493

```text
(exec)# do-exec show accounting group <cr>
```

Handler ` RVA 0x10D141B0 `；selector ` 1 `；EOL ` RVA 0x34D10A60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1bfc402a1db507e5](../../evidence/conditions-sets-011.md#c-1bfc402a1db507e5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019731

```text
(exec)# do-exec show accounting group <string> <cr>
```

Handler ` RVA 0x10D141B0 `；selector ` 2 `；EOL ` RVA 0x34D10A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Group name。

[条件 C-1bfc402a1db507e5](../../evidence/conditions-sets-011.md#c-1bfc402a1db507e5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0cff7b130b46abb3](../../evidence/parameters-sets-001.md#p-0cff7b130b46abb3) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015514

```text
(exec)# do-exec show accounting session <cr>
```

Handler ` RVA 0x10D15B60 `；selector ` 3 `；EOL ` RVA 0x34D10F88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1bfc402a1db507e5](../../evidence/conditions-sets-011.md#c-1bfc402a1db507e5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019743

```text
(exec)# do-exec show accounting session <number:1..100000> <cr>
```

Handler ` RVA 0x10D15B60 `；selector ` 4 `；EOL ` RVA 0x34D10F60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Session id。

[条件 C-1bfc402a1db507e5](../../evidence/conditions-sets-011.md#c-1bfc402a1db507e5) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-fe468869032ecf3b](../../evidence/parameters-sets-019.md#p-fe468869032ecf3b) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013031

```text
(exec)# do-exec show acm rules <cr>
```

Handler ` RVA 0xDECF5D0 `；selector ` 0 `；EOL ` RVA 0x340C69D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012545

```text
(exec)# do-exec show adjacency <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 1 `；EOL ` RVA 0x3379D448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-261d9cd7ea398cff](../../evidence/conditions-sets-015.md#c-261d9cd7ea398cff) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013798

```text
(exec)# do-exec show adjacency connid-mgr <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 2 `；EOL ` RVA 0x3379C200 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013853

```text
(exec)# do-exec show adjacency summary <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 0 `；EOL ` RVA 0x3379C5F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-510494f0d4cb1b1f](../../evidence/conditions-sets-032.md#c-510494f0d4cb1b1f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013963

```text
(exec)# do-exec show alg sip <cr>
```

Handler ` RVA 0xCD3D500 `；selector ` 0 `；EOL ` RVA 0x33CD4600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012461

```text
(exec)# do-exec show alignment <cr>
```

Handler ` RVA 0xE8F39E0 `；selector ` 0 `；EOL ` RVA 0x3433E688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016493

```text
(exec)# do-exec show alps circuits <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 1 `；EOL ` RVA 0x3541B060 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016472

```text
(exec)# do-exec show alps peers <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 0 `；EOL ` RVA 0x3541AC50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017820

```text
(exec)# do-exec show ancp an-port summary <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 8 `；EOL ` RVA 0x336DA170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-fe6aa08376d29b56](../../evidence/state_effects-sets-054.md#s-fe6aa08376d29b56)

### path-013927

```text
(exec)# do-exec show ancp neighbor <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 7 `；EOL ` RVA 0x336D8FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2278ed85571dae1a](../../evidence/state_effects-sets-008.md#s-2278ed85571dae1a)

### path-017773

```text
(exec)# do-exec show ancp neighbor brief <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 1 `；EOL ` RVA 0x336D8B48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-c7d6971567fadfe7](../../evidence/state_effects-sets-042.md#s-c7d6971567fadfe7)

### path-013857

```text
(exec)# do-exec show ancp port <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 3 `；EOL ` RVA 0x336D86D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-37a715b2d8ce8ea6](../../evidence/conditions-sets-022.md#c-37a715b2d8ce8ea6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013856

```text
(exec)# do-exec show ancp session <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 4 `；EOL ` RVA 0x336D9690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013819

```text
(exec)# do-exec show ancp statistics <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 5 `；EOL ` RVA 0x336D9A68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019934

```text
(exec)# do-exec show application ha statistics <cr>
```

Handler ` RVA 0x12802A90 `；selector ` 0 `；EOL ` RVA 0x358D9A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7d31fc47fdde15c6](../../evidence/conditions-sets-049.md#c-7d31fc47fdde15c6) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-dc215703988eb96b](../../evidence/state_effects-sets-047.md#s-dc215703988eb96b)

### path-015634

```text
(exec)# do-exec show application summary <cr>
```

Handler ` RVA 0x1280F4C0 `；selector ` 0 `；EOL ` RVA 0x358DA110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012753

```text
(exec)# do-exec show archive <cr>
```

Handler ` RVA 0xDECC9F0 `；selector ` 0 `；EOL ` RVA 0x3409C008 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023146

```text
(exec)# do-exec show archive config rollback timer <cr>
```

Handler ` RVA 0xDFDCFE0 `；selector ` 0 `；EOL ` RVA 0x340CD868 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024523

```text
(exec)# do-exec show archive log config all persistent <cr>
```

Handler ` RVA 0xDF14700 `；selector ` 0 `；EOL ` RVA 0x340A2B20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-4b9a160f560bbee5](../../evidence/state_effects-sets-017.md#s-4b9a160f560bbee5)

### path-023142

```text
(exec)# do-exec show archive log config statistics <cr>
```

Handler ` RVA 0xDF0B2B0 `；selector ` 0 `；EOL ` RVA 0x340A27D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-7bd553b9d7729237](../../evidence/state_effects-sets-026.md#s-7bd553b9d7729237)

### path-012818

```text
(exec)# do-exec show asp <cr>
```

Handler ` RVA 0x113A1300 `；selector ` 0 `；EOL ` RVA 0x354A39B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015352

```text
(exec)# do-exec show async bootp <cr>
```

Handler ` RVA 0xD3448C0 `；selector ` 0 `；EOL ` RVA 0x349343F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015369

```text
(exec)# do-exec show async status <cr>
```

Handler ` RVA 0xFF3FE50 `；selector ` 0 `；EOL ` RVA 0x349346A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016726

```text
(exec)# do-exec show auto install status <cr>
```

Handler ` RVA 0xFFA8E70 `；selector ` 0 `；EOL ` RVA 0x349433F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9587f696076fc8ab](../../evidence/conditions-sets-058.md#c-9587f696076fc8ab) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016737

```text
(exec)# do-exec show auto install tech-support <cr>
```

Handler ` RVA 0xFFAE9B0 `；selector ` 0 `；EOL ` RVA 0x34943698 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9587f696076fc8ab](../../evidence/conditions-sets-058.md#c-9587f696076fc8ab) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016743

```text
(exec)# do-exec show auto install trace <cr>
```

Handler ` RVA 0xFFAE910 `；selector ` 0 `；EOL ` RVA 0x34943940 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9587f696076fc8ab](../../evidence/conditions-sets-058.md#c-9587f696076fc8ab) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016717

```text
(exec)# do-exec show auto secure config <cr>
```

Handler ` RVA 0xB246B10 `；selector ` 0 `；EOL ` RVA 0x336D4EB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9587f696076fc8ab](../../evidence/conditions-sets-058.md#c-9587f696076fc8ab) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015717

```text
(exec)# do-exec show autoip status <cr>
```

Handler ` RVA 0xB286210 `；selector ` 0 `；EOL ` RVA 0x3372CA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-019886

```text
(exec)# do-exec show autoip status detail <cr>
```

Handler ` RVA 0xB286260 `；selector ` 0 `；EOL ` RVA 0x3372CA30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012624

```text
(exec)# do-exec show avc <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 89 `；EOL ` RVA 0x35254938 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2b31f69ff8edbc5c](../../evidence/conditions-sets-017.md#c-2b31f69ff8edbc5c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022622

```text
(exec)# do-exec show avc sd-service info cmds <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 87 `；EOL ` RVA 0x3524EA68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024301

```text
(exec)# do-exec show avc sd-service info cmds config <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 86 `；EOL ` RVA 0x3524EA40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024296

```text
(exec)# do-exec show avc sd-service info cmds status <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 88 `；EOL ` RVA 0x3524E798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022600

```text
(exec)# do-exec show avc sd-service info detailed <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 61 `；EOL ` RVA 0x3524EF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-852c282cfe469497](../../evidence/state_effects-sets-028.md#s-852c282cfe469497)

### path-022734

```text
(exec)# do-exec show avc sd-service info ent <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 66 `；EOL ` RVA 0x35253A08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024341

```text
(exec)# do-exec show avc sd-service info ent config <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 72 `；EOL ` RVA 0x35252720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024877

```text
(exec)# do-exec show avc sd-service info ent device-health db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 75 `；EOL ` RVA 0x35253FF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025077

```text
(exec)# do-exec show avc sd-service info ent device-health export last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 76 `；EOL ` RVA 0x35253D58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025076

```text
(exec)# do-exec show avc sd-service info ent device-health export stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 77 `；EOL ` RVA 0x35253AB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024879

```text
(exec)# do-exec show avc sd-service info ent device-health interfaces <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 74 `；EOL ` RVA 0x35254298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024372

```text
(exec)# do-exec show avc sd-service info ent export <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 70 `；EOL ` RVA 0x352534F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024874

```text
(exec)# do-exec show avc sd-service info ent export current <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 68 `；EOL ` RVA 0x35252F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024878

```text
(exec)# do-exec show avc sd-service info ent export keys-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 73 `；EOL ` RVA 0x352534D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-313407d5f45e6393](../../evidence/conditions-sets-019.md#c-313407d5f45e6393) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024875

```text
(exec)# do-exec show avc sd-service info ent export last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 69 `；EOL ` RVA 0x35253228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024348

```text
(exec)# do-exec show avc sd-service info ent fields-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 71 `；EOL ` RVA 0x352529C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fc0f01b356af64db](../../evidence/conditions-sets-097.md#c-fc0f01b356af64db) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024355

```text
(exec)# do-exec show avc sd-service info ent symbol-table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 67 `；EOL ` RVA 0x35252C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f11598370d270f32](../../evidence/conditions-sets-093.md#c-f11598370d270f32) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024336

```text
(exec)# do-exec show avc sd-service info export flow-counters <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 63 `；EOL ` RVA 0x35250B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f0905fc82c349b96](../../evidence/conditions-sets-093.md#c-f0905fc82c349b96) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8161294b12ba28af](../../evidence/state_effects-sets-027.md#s-8161294b12ba28af)

### path-024337

```text
(exec)# do-exec show avc sd-service info export l3-cache <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 55 `；EOL ` RVA 0x3524FF38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8161294b12ba28af](../../evidence/state_effects-sets-027.md#s-8161294b12ba28af)

### path-024333

```text
(exec)# do-exec show avc sd-service info export npc-info <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 62 `；EOL ` RVA 0x35250880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9066f4718e74ca64](../../evidence/conditions-sets-056.md#c-9066f4718e74ca64) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8161294b12ba28af](../../evidence/state_effects-sets-027.md#s-8161294b12ba28af)

### path-024352

```text
(exec)# do-exec show avc sd-service info export socket-cache <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 56 `；EOL ` RVA 0x352505A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8161294b12ba28af](../../evidence/state_effects-sets-027.md#s-8161294b12ba28af)

### path-024329

```text
(exec)# do-exec show avc sd-service info import dump <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F6D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-2bf77e59bb22cafa](../../evidence/state_effects-sets-010.md#s-2bf77e59bb22cafa)

### path-024865

```text
(exec)# do-exec show avc sd-service info import dump l3-rules <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F3F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-96f00fefa0f62360](../../evidence/state_effects-sets-032.md#s-96f00fefa0f62360)

### path-024868

```text
(exec)# do-exec show avc sd-service info import dump l4-rules <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F6A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4ad9eda7fddbfcd](../../evidence/conditions-sets-094.md#c-f4ad9eda7fddbfcd) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f7bb8e27713c2f92](../../evidence/state_effects-sets-052.md#s-f7bb8e27713c2f92)

### path-024343

```text
(exec)# do-exec show avc sd-service info tls-fp clear-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 85 `；EOL ` RVA 0x35251648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd2e98df5f43098c](../../evidence/conditions-sets-073.md#c-bd2e98df5f43098c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024361

```text
(exec)# do-exec show avc sd-service info tls-fp clear-stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 82 `；EOL ` RVA 0x352523F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d1bb8d6ae248fd6d](../../evidence/conditions-sets-081.md#c-d1bb8d6ae248fd6d) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024345

```text
(exec)# do-exec show avc sd-service info tls-fp dump-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 83 `；EOL ` RVA 0x35251178 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5de3690c4e9829ad](../../evidence/conditions-sets-037.md#c-5de3690c4e9829ad) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024869

```text
(exec)# do-exec show avc sd-service info tls-fp dump-db detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 84 `；EOL ` RVA 0x35251150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-36ca02c0b2d1848c](../../evidence/conditions-sets-021.md#c-36ca02c0b2d1848c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024876

```text
(exec)# do-exec show avc sd-service info tls-fp fingerprint-db dump <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 80 `；EOL ` RVA 0x35251F10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-04b08acdd42cec8f](../../evidence/conditions-sets-002.md#c-04b08acdd42cec8f) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-025075

```text
(exec)# do-exec show avc sd-service info tls-fp fingerprint-db dump detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 81 `；EOL ` RVA 0x35251EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-70ba635db5171b22](../../evidence/conditions-sets-044.md#c-70ba635db5171b22) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024873

```text
(exec)# do-exec show avc sd-service info tls-fp fingerprint-db info <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 79 `；EOL ` RVA 0x35251C00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b20727b1fc5b224c](../../evidence/conditions-sets-069.md#c-b20727b1fc5b224c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-024350

```text
(exec)# do-exec show avc sd-service info tls-fp show-stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 78 `；EOL ` RVA 0x352518F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66bd3f33d7403e02](../../evidence/conditions-sets-040.md#c-66bd3f33d7403e02) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012466

```text
(exec)# do-exec show backup <cr>
```

Handler ` RVA 0xEF363F0 `；selector ` 0 `；EOL ` RVA 0x34483370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012996

```text
(exec)# do-exec show banner login <cr>
```

Handler ` RVA 0xDEFB260 `；selector ` 0 `；EOL ` RVA 0x340C5CD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-8a8c723f779d0c94](../../evidence/state_effects-sets-029.md#s-8a8c723f779d0c94)

### path-015831

```text
(exec)# do-exec show beep blocked <cr>
```

Handler ` RVA 0xEF60FC0 `；selector ` 1 `；EOL ` RVA 0x3448BFE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69f38aae4dcfcfee](../../evidence/conditions-sets-041.md#c-69f38aae4dcfcfee) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-015846

```text
(exec)# do-exec show beep session <cr>
```

Handler ` RVA 0xEF60FC0 `；selector ` 3 `；EOL ` RVA 0x3448BD48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69f38aae4dcfcfee](../../evidence/conditions-sets-041.md#c-69f38aae4dcfcfee) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f6f7e9e07fb7ae80](../../evidence/state_effects-sets-052.md#s-f6f7e9e07fb7ae80)

### path-014566

```text
(exec)# do-exec show bfd clients <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 1 `；EOL ` RVA 0x34CB4440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014578

```text
(exec)# do-exec show bfd drops <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 4 `；EOL ` RVA 0x34CB49E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014661

```text
(exec)# do-exec show bfd fast-timers-on-slow-int <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 8 `；EOL ` RVA 0x34CB54E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014587

```text
(exec)# do-exec show bfd hardware <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 5 `；EOL ` RVA 0x34CB4748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014627

```text
(exec)# do-exec show bfd idbs <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 13 `；EOL ` RVA 0x34CB4F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014603

```text
(exec)# do-exec show bfd interface <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 2 `；EOL ` RVA 0x34CB4C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014531

```text
(exec)# do-exec show bfd internal <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 0 `；EOL ` RVA 0x34CB2A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a0c97758fe8dc7dd](../../evidence/state_effects-sets-034.md#s-a0c97758fe8dc7dd)

### path-014663

```text
(exec)# do-exec show bfd map <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 6 `；EOL ` RVA 0x34CB5248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014520

```text
(exec)# do-exec show bfd summary <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 3 `；EOL ` RVA 0x34CB21C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-54722afed7b23d17](../../evidence/state_effects-sets-018.md#s-54722afed7b23d17)

### path-018802

```text
(exec)# do-exec show bfd target-identifier all <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 9 `；EOL ` RVA 0x34CB57D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-018908

```text
(exec)# do-exec show bfd target-identifier interface <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 12 `；EOL ` RVA 0x34CB5FC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54a9554d62fd7353](../../evidence/conditions-sets-033.md#c-54a9554d62fd7353) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-018842

```text
(exec)# do-exec show bfd target-identifier local <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 10 `；EOL ` RVA 0x34CB5A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-018870

```text
(exec)# do-exec show bfd target-identifier remote <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 11 `；EOL ` RVA 0x34CB5D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-f47200ed8543f000](../../evidence/state_effects-sets-052.md#s-f47200ed8543f000)

### path-014929

```text
(exec)# do-exec show bgp memory <cr>
```

Handler ` RVA 0xF028050 `；selector ` 0 `；EOL ` RVA 0x344FA0C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6ecc7e18221db618](../../evidence/conditions-sets-043.md#c-6ecc7e18221db618) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014932

```text
(exec)# do-exec show bgp sr-color <cr>
```

Handler ` RVA 0xF1D04C0 `；selector ` 0 `；EOL ` RVA 0x344FA3A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-898df15e9c172892](../../evidence/conditions-sets-053.md#c-898df15e9c172892) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012497

```text
(exec)# do-exec show bootvar <cr>
```

Handler ` RVA 0xD556740 `；selector ` 0 `；EOL ` RVA 0x33E811B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013603

```text
(exec)# do-exec show bootvar config-file <cr>
```

Handler ` RVA 0xD556740 `；selector ` 2 `；EOL ` RVA 0x33E80EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013617

```text
(exec)# do-exec show bootvar system <cr>
```

Handler ` RVA 0xD556740 `；selector ` 1 `；EOL ` RVA 0x33E81190 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016399

```text
(exec)# do-exec show bridge circuit-group <cr>
```

Handler ` RVA 0xF27F440 `；selector ` 0 `；EOL ` RVA 0x345E8038 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cdf5b4c3539f5b86](../../evidence/conditions-sets-079.md#c-cdf5b4c3539f5b86) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016383

```text
(exec)# do-exec show bridge group <cr>
```

Handler ` RVA 0xF28F690 `；selector ` 0 `；EOL ` RVA 0x345E7CE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cdf5b4c3539f5b86](../../evidence/conditions-sets-079.md#c-cdf5b4c3539f5b86) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012548

```text
(exec)# do-exec show bridge-domain <cr>
```

Handler ` RVA 0xBF37660 `；selector ` 0 `；EOL ` RVA 0x33952B98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-37f6322a0dc9ce84](../../evidence/conditions-sets-022.md#c-37f6322a0dc9ce84) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013952

```text
(exec)# do-exec show bridge-domain c-mac <cr>
```

Handler ` RVA 0xBF38D70 `；selector ` 0 `；EOL ` RVA 0x33953B28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f81fb1d8fa8d1c91](../../evidence/conditions-sets-096.md#c-f81fb1d8fa8d1c91) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013918

```text
(exec)# do-exec show bridge-domain external-ports <cr>
```

Handler ` RVA 0xBF37390 `；selector ` 0 `；EOL ` RVA 0x33953748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4acb0fa9f37613ec](../../evidence/conditions-sets-029.md#c-4acb0fa9f37613ec) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017802

```text
(exec)# do-exec show bridge-domain route stats <cr>
```

Handler ` RVA 0xBF373F0 `；selector ` 0 `；EOL ` RVA 0x33952848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d8ada47583390f6c](../../evidence/conditions-sets-083.md#c-d8ada47583390f6c) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-a35a212a6e503628](../../evidence/state_effects-sets-035.md#s-a35a212a6e503628)

### path-012796

```text
(exec)# do-exec show bsc <cr>
```

Handler ` RVA 0x113C32F0 `；selector ` 0 `；EOL ` RVA 0x354B5910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012798

```text
(exec)# do-exec show bstun <cr>
```

Handler ` RVA 0x113E0EA0 `；selector ` 0 `；EOL ` RVA 0x354BC670 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012769

```text
(exec)# do-exec show buffers <cr>
```

Handler ` RVA 0xE3DFC30 `；selector ` 0 `；EOL ` RVA 0x342B96A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d8d22e01fc83c059](../../evidence/state_effects-sets-046.md#s-d8d22e01fc83c059)

### path-016328

```text
(exec)# do-exec show buffers failures <cr>
```

Handler ` RVA 0xE3E0BD0 `；selector ` 0 `；EOL ` RVA 0x342B9360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016455

```text
(exec)# do-exec show buffers leak <cr>
```

Handler ` RVA 0xE3DED00 `；selector ` 0 `；EOL ` RVA 0x342BA2E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d8d22e01fc83c059](../../evidence/state_effects-sets-046.md#s-d8d22e01fc83c059)

### path-023202

```text
(exec)# do-exec show buffers leak resource user <cr>
```

Handler ` RVA 0xE3DF2C0 `；selector ` 0 `；EOL ` RVA 0x342BA320 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d8d22e01fc83c059](../../evidence/state_effects-sets-046.md#s-d8d22e01fc83c059)

### path-016453

```text
(exec)# do-exec show buffers tune <cr>
```

Handler ` RVA 0xE3DF810 `；selector ` 0 `；EOL ` RVA 0x342BA800 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d8d22e01fc83c059](../../evidence/state_effects-sets-046.md#s-d8d22e01fc83c059)

### path-016443

```text
(exec)# do-exec show buffers usage <cr>
```

Handler ` RVA 0xE3DE890 `；selector ` 0 `；EOL ` RVA 0x342B9D40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-d8d22e01fc83c059](../../evidence/state_effects-sets-046.md#s-d8d22e01fc83c059)

### path-023200

```text
(exec)# do-exec show buffers usage pool <string> <cr>
```

Handler ` RVA 0xE3DE150 `；selector ` 0 `；EOL ` RVA 0x342B9D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of pool to display buffers from。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-0c1e5d0ea68dc78e](../../evidence/parameters-sets-001.md#p-0c1e5d0ea68dc78e) · [状态效果 S-d8d22e01fc83c059](../../evidence/state_effects-sets-046.md#s-d8d22e01fc83c059)

### path-016610

```text
(exec)# do-exec show bulkstat data-group <cr>
```

Handler ` RVA 0xBC6B490 `；selector ` 0 `；EOL ` RVA 0x33884570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-023288

```text
(exec)# do-exec show bulkstat data-group <string> process <cr>
```

Handler ` RVA 0xBC88BD0 `；selector ` 0 `；EOL ` RVA 0x33894480 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name of data-group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-af5b0e6e47e3ffab](../../evidence/parameters-sets-013.md#p-af5b0e6e47e3ffab) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016618

```text
(exec)# do-exec show bulkstat pre-defined <cr>
```

Handler ` RVA 0xBC6C900 `；selector ` 0 `；EOL ` RVA 0x338876A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020674

```text
(exec)# do-exec show bulkstat pre-defined data <cr>
```

Handler ` RVA 0xBC6C200 `；selector ` 0 `；EOL ` RVA 0x33887110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020677

```text
(exec)# do-exec show bulkstat pre-defined data-group <cr>
```

Handler ` RVA 0xBC6C630 `；selector ` 0 `；EOL ` RVA 0x33887400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020680

```text
(exec)# do-exec show bulkstat pre-defined instance <cr>
```

Handler ` RVA 0xBC6BE40 `；selector ` 0 `；EOL ` RVA 0x338876E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-016611

```text
(exec)# do-exec show bulkstat profile <cr>
```

Handler ` RVA 0xBC6B220 `；selector ` 0 `；EOL ` RVA 0x338848D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012498

```text
(exec)# do-exec show calendar <cr>
```

Handler ` RVA 0xE038750 `；selector ` 0 `；EOL ` RVA 0x34171B18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ae8a8d611186038e](../../evidence/conditions-sets-067.md#c-ae8a8d611186038e) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-54d44a34f869d29b](../../evidence/state_effects-sets-018.md#s-54d44a34f869d29b)

### path-015844

```text
(exec)# do-exec show call admission <cr>
```

Handler ` RVA 0xDEB05F0 `；selector ` 0 `；EOL ` RVA 0x3408CA08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020035

```text
(exec)# do-exec show call filter component <cr>
```

Handler ` RVA 0x16987360 `；selector ` 20 `；EOL ` RVA 0x3605ACB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-020040

```text
(exec)# do-exec show call filter match-list <cr>
```

Handler ` RVA 0x16987110 `；selector ` 21 `；EOL ` RVA 0x3605A7F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-022983

```text
(exec)# do-exec show call filter match-list <number:1..16> <cr>
```

Handler ` RVA 0x16987360 `；selector ` 21 `；EOL ` RVA 0x3605A7C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` The unique Tag for this filter。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-8da4415909c6b70d](../../evidence/parameters-sets-011.md#p-8da4415909c6b70d) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-012549

```text
(exec)# do-exec show call-home <cr>
```

Handler ` RVA 0xB6D5350 `；selector ` 4 `；EOL ` RVA 0x337EBFE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-549ef0f05f705380](../../evidence/conditions-sets-033.md#c-549ef0f05f705380) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013864

```text
(exec)# do-exec show call-home alert-group <cr>
```

Handler ` RVA 0xB6D5300 `；selector ` 0 `；EOL ` RVA 0x337EAAB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-013842

```text
(exec)# do-exec show call-home detail <cr>
```

Handler ` RVA 0xB6D5350 `；selector ` 5 `；EOL ` RVA 0x337EA810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-014047

```text
(exec)# do-exec show call-home diagnostic-signature <cr>
```

Handler ` RVA 0x128FEF40 `；selector ` 0 `；EOL ` RVA 0x337ECD90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-018048

```text
(exec)# do-exec show call-home diagnostic-signature <number:1..99999999> <cr>
```

Handler ` RVA 0x128FEE70 `；selector ` 0 `；EOL ` RVA 0x337ED900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021837

```text
(exec)# do-exec show call-home diagnostic-signature <number:1..99999999> actions <cr>
```

Handler ` RVA 0x128FECD0 `；selector ` 0 `；EOL ` RVA 0x337ED080 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021832

```text
(exec)# do-exec show call-home diagnostic-signature <number:1..99999999> events <cr>
```

Handler ` RVA 0x128FEDA0 `；selector ` 0 `；EOL ` RVA 0x337ECDD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021852

```text
(exec)# do-exec show call-home diagnostic-signature <number:1..99999999> prerequisite <cr>
```

Handler ` RVA 0x128FEB20 `；selector ` 0 `；EOL ` RVA 0x337ED5D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-fd009c3f42622234](../../evidence/state_effects-sets-054.md#s-fd009c3f42622234)

### path-021844

```text
(exec)# do-exec show call-home diagnostic-signature <number:1..99999999> prompt <cr>
```

Handler ` RVA 0x128FEC00 `；selector ` 0 `；EOL ` RVA 0x337ED328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-021870

```text
(exec)# do-exec show call-home diagnostic-signature <number:1..99999999> variables <cr>
```

Handler ` RVA 0x128FEA50 `；selector ` 0 `；EOL ` RVA 0x337ED8D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017934

```text
(exec)# do-exec show call-home diagnostic-signature failure <cr>
```

Handler ` RVA 0x128FE5F0 `；selector ` 0 `；EOL ` RVA 0x337EC570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017901

```text
(exec)# do-exec show call-home diagnostic-signature info <cr>
```

Handler ` RVA 0x128FE890 `；selector ` 0 `；EOL ` RVA 0x337EC020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017915

```text
(exec)# do-exec show call-home diagnostic-signature register <cr>
```

Handler ` RVA 0x128FE7B0 `；selector ` 0 `；EOL ` RVA 0x337EC2C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)

### path-017963

```text
(exec)# do-exec show call-home diagnostic-signature statistics <cr>
```

Handler ` RVA 0x128FE6D0 `；selector ` 0 `；EOL ` RVA 0x337EC8A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [缺口 G-96f4196304222449](../../evidence/gaps-sets-006.md#g-96f4196304222449) · [状态效果 S-86242100813c5da9](../../evidence/state_effects-sets-028.md#s-86242100813c5da9)
