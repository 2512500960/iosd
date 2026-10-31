# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-062971

```text
(config)# do-exec ping interface <interface> <?number_func_nows_action@555588c3d250> / <number:dynamic> <cr>
```

Handler ` RVA 0xB276180 `；selector ` 0 `；EOL ` RVA 0x336E9348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Enter the starting VCI value。

[条件 C-15e53d0ab9bd65b1](../../evidence/conditions-sets-009.md#c-15e53d0ab9bd65b1) · [缺口 G-0a513966d94ea955](../../evidence/gaps-sets-001.md#g-0a513966d94ea955) · [参数 P-b6b31fc8eb3849d1](../../evidence/parameters-sets-014.md#p-b6b31fc8eb3849d1) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-041703

```text
(config)# do-exec pnpa service abort-on-fault <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 67 `；EOL ` RVA 0x33B67E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable or disable abort-on-fault。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-00c44352ff5bf053](../../evidence/parameters-sets-001.md#p-00c44352ff5bf053) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041679

```text
(config)# do-exec pnpa service act2-sudi <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 69 `；EOL ` RVA 0x33B67B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable or disable act2 sudi during device-auth。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-60cbb82cb3693034](../../evidence/parameters-sets-008.md#p-60cbb82cb3693034) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041660

```text
(config)# do-exec pnpa service ap-extension <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 68 `；EOL ` RVA 0x33B67858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable or disable ap extension。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-377b4054c7c00a81](../../evidence/parameters-sets-005.md#p-377b4054c7c00a81) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042316

```text
(config)# do-exec pnpa service backoff-reset <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 0 `；EOL ` RVA 0x33B72BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the profile name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-058304f630d6240e](../../evidence/parameters-sets-001.md#p-058304f630d6240e) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050998

```text
(config)# do-exec pnpa service certify <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 2 `；EOL ` RVA 0x33B72520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the file URL；` string ` Specify the verify URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-49cc79f37c311cf3](../../evidence/parameters-sets-006.md#p-49cc79f37c311cf3) · [状态效果 S-e110bc989409fc0a](../../evidence/state_effects-sets-048.md#s-e110bc989409fc0a)

### path-050980

```text
(config)# do-exec pnpa service check-server-id <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 3 `；EOL ` RVA 0x33B72180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the server id (hostname or ip)；` unsigned_number ` Specify the server port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d239d744d63a6987](../../evidence/parameters-sets-016.md#p-d239d744d63a6987) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050967

```text
(config)# do-exec pnpa service check-ssl-handshake <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 4 `；EOL ` RVA 0x33B71E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the server id (hostname or ip)；` unsigned_number ` Specify the server port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b82d299d4798187f](../../evidence/parameters-sets-014.md#p-b82d299d4798187f) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041640

```text
(config)# do-exec pnpa service config-control <number:0..3> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 70 `；EOL ` RVA 0x33B67568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` config-control level: 3-strict, 2-all-check, 1-basic-check, 0-none。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-35ffbdd0c7542d73](../../evidence/parameters-sets-005.md#p-35ffbdd0c7542d73) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041614

```text
(config)# do-exec pnpa service config-monitor <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 71 `；EOL ` RVA 0x33B67278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable or disable config-monitor。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7e47f765fa9d8e62](../../evidence/parameters-sets-010.md#p-7e47f765fa9d8e62) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041586

```text
(config)# do-exec pnpa service config-reserve <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 72 `；EOL ` RVA 0x33B66F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify profile to reserve。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cfbbd60413864266](../../evidence/parameters-sets-016.md#p-cfbbd60413864266) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050422

```text
(config)# do-exec pnpa service config-retry <number:0..10000> <number:0..10000> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 73 `；EOL ` RVA 0x33B66CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Set config max retry；` unsigned_number ` Set config-retry interval in ms。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-f18c8e5fdb7e24ec](../../evidence/parameters-sets-018.md#p-f18c8e5fdb7e24ec) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042312

```text
(config)# do-exec pnpa service config-upgrade <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 5 `；EOL ` RVA 0x33B71938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the config source file path。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3e7e69dbed315fde](../../evidence/parameters-sets-005.md#p-3e7e69dbed315fde) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041508

```text
(config)# do-exec pnpa service connectivity-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 74 `；EOL ` RVA 0x33B66968 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enforce connectivity: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-303a3e7c7e3edb16](../../evidence/parameters-sets-004.md#p-303a3e7c7e3edb16) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051020

```text
(config)# do-exec pnpa service copy <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 1 `；EOL ` RVA 0x33B728E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the source file URL；` string ` Specify the destination file path。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a6f5c788bce058d4](../../evidence/parameters-sets-013.md#p-a6f5c788bce058d4) · [状态效果 S-331fae549a01209f](../../evidence/state_effects-sets-011.md#s-331fae549a01209f)

### path-041469

```text
(config)# do-exec pnpa service correlator-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 75 `；EOL ` RVA 0x33B66678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Correlator check: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-4a9d32d3aa341999](../../evidence/parameters-sets-006.md#p-4a9d32d3aa341999) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041436

```text
(config)# do-exec pnpa service device-id-cert <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 76 `；EOL ` RVA 0x33B66388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) device-id-cert。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bd8ddb0fee9cd6de](../../evidence/parameters-sets-014.md#p-bd8ddb0fee9cd6de) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042205

```text
(config)# do-exec pnpa service diag <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 6 `；EOL ` RVA 0x33B71458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Diag level: 0-none, 1-all。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8ef001bbcd9e88c1](../../evidence/parameters-sets-011.md#p-8ef001bbcd9e88c1) · [状态效果 S-ee8f608cd1bb3f76](../../evidence/state_effects-sets-050.md#s-ee8f608cd1bb3f76)

### path-042605

```text
(config)# do-exec pnpa service discovery abort-autoinstall <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 7 `；EOL ` RVA 0x33B71028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051186

```text
(config)# do-exec pnpa service discovery bypass-auto-install <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 8 `；EOL ` RVA 0x33B70DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7f4f54823086e1ad](../../evidence/parameters-sets-010.md#p-7f4f54823086e1ad) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051179

```text
(config)# do-exec pnpa service discovery bypass-cellular-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 9 `；EOL ` RVA 0x33B70AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass cellular-check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-6bfeb9065172b03e](../../evidence/parameters-sets-009.md#p-6bfeb9065172b03e) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051170

```text
(config)# do-exec pnpa service discovery bypass-connectivity-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 10 `；EOL ` RVA 0x33B707C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass connectivity-check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d33d16eb50948d01](../../evidence/parameters-sets-016.md#p-d33d16eb50948d01) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051159

```text
(config)# do-exec pnpa service discovery bypass-disc-summary <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 11 `；EOL ` RVA 0x33B704D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8b96e58952d2d5ff](../../evidence/parameters-sets-011.md#p-8b96e58952d2d5ff) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051152

```text
(config)# do-exec pnpa service discovery bypass-dns-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 12 `；EOL ` RVA 0x33B701E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-421bea45088742c0](../../evidence/parameters-sets-006.md#p-421bea45088742c0) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051140

```text
(config)# do-exec pnpa service discovery bypass-https-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 13 `；EOL ` RVA 0x33B6FEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass https-enforcement: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-78a3b7af483fb70c](../../evidence/parameters-sets-009.md#p-78a3b7af483fb70c) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051128

```text
(config)# do-exec pnpa service discovery bypass-napp-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 14 `；EOL ` RVA 0x33B6FC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass napp check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7c9aff8094b54082](../../evidence/parameters-sets-010.md#p-7c9aff8094b54082) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051117

```text
(config)# do-exec pnpa service discovery bypass-startup-config <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 15 `；EOL ` RVA 0x33B6F910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass startup: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8fe566dc6aeaefb0](../../evidence/parameters-sets-011.md#p-8fe566dc6aeaefb0) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051102

```text
(config)# do-exec pnpa service discovery bypass-webui-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 16 `；EOL ` RVA 0x33B6F620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass webui check: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-005812e8002c86c7](../../evidence/parameters-sets-001.md#p-005812e8002c86c7) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051090

```text
(config)# do-exec pnpa service discovery bypass-wizard-input <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 17 `；EOL ` RVA 0x33B6F330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bypass wizard: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-823f4c048ce7250d](../../evidence/parameters-sets-010.md#p-823f4c048ce7250d) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042435

```text
(config)# do-exec pnpa service discovery clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 18 `；EOL ` RVA 0x33B6F020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-056408

```text
(config)# do-exec pnpa service discovery dhcp ipv4 <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 19 `；EOL ` RVA 0x33B6ED88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify a DHCP op43 string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b249e0108e8433a5](../../evidence/parameters-sets-014.md#p-b249e0108e8433a5) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-056400

```text
(config)# do-exec pnpa service discovery dhcp ipv6 <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 20 `；EOL ` RVA 0x33B6EAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify a DHCP op17 string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-797f0695c9572a5c](../../evidence/parameters-sets-009.md#p-797f0695c9572a5c) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042402

```text
(config)# do-exec pnpa service discovery dns-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 21 `；EOL ` RVA 0x33B6E750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051052

```text
(config)# do-exec pnpa service discovery dns-set <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 22 `；EOL ` RVA 0x33B6E4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the DNS domain-name-cache。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-e8db970f70a49b74](../../evidence/parameters-sets-017.md#p-e8db970f70a49b74) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051046

```text
(config)# do-exec pnpa service discovery method-disable <number:0..15> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 23 `；EOL ` RVA 0x33B6E1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` discovery method。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-932466822764f01b](../../evidence/parameters-sets-011.md#p-932466822764f01b) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-051039

```text
(config)# do-exec pnpa service discovery method-enable <number:0..15> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 24 `；EOL ` RVA 0x33B6DEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` discovery method。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-f8ffaac76d709e73](../../evidence/parameters-sets-019.md#p-f8ffaac76d709e73) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042345

```text
(config)# do-exec pnpa service discovery method-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 25 `；EOL ` RVA 0x33B6DBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042324

```text
(config)# do-exec pnpa service discovery no-shutdown <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 26 `；EOL ` RVA 0x33B6D938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050988

```text
(config)# do-exec pnpa service discovery server-credential <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 27 `；EOL ` RVA 0x33B6D6B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Server Credential: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-6fe7d1a6a6e7cd5c](../../evidence/parameters-sets-009.md#p-6fe7d1a6a6e7cd5c) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042280

```text
(config)# do-exec pnpa service discovery setup-abort <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 28 `；EOL ` RVA 0x33B6D3A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042266

```text
(config)# do-exec pnpa service discovery shutdown <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 29 `；EOL ` RVA 0x33B6D0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042244

```text
(config)# do-exec pnpa service discovery start <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 30 `；EOL ` RVA 0x33B6CE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042226

```text
(config)# do-exec pnpa service discovery stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 31 `；EOL ` RVA 0x33B6CBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-056312

```text
(config)# do-exec pnpa service discovery terminate <number:0..11> <number:0..14> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 32 `；EOL ` RVA 0x33B6C920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Requested By；` unsigned_number ` Reason。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-18dd944bfc769b57](../../evidence/parameters-sets-002.md#p-18dd944bfc769b57) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050897

```text
(config)# do-exec pnpa service discovery wait-for-stop <number:0..7200> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 33 `；EOL ` RVA 0x33B6C5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max wait time in seconds。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-5100fe36e66f0cae](../../evidence/parameters-sets-007.md#p-5100fe36e66f0cae) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042169

```text
(config)# do-exec pnpa service do-change-mode <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 34 `；EOL ` RVA 0x33B6C298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` node mode - autonomous, controller。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2bfc1edfe80ede81](../../evidence/parameters-sets-004.md#p-2bfc1edfe80ede81) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032972

```text
(config)# do-exec pnpa service do-write-erase <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 35 `；EOL ` RVA 0x33B6BF88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032960

```text
(config)# do-exec pnpa service do-write-memory <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 36 `；EOL ` RVA 0x33B6BCE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041404

```text
(config)# do-exec pnpa service eem-proxy <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 77 `；EOL ` RVA 0x33B66098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) eem-proxy。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-773136487d0b76af](../../evidence/parameters-sets-009.md#p-773136487d0b76af) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-056246

```text
(config)# do-exec pnpa service event-notify <number:0..29> <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 37 `；EOL ` RVA 0x33B6AEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` event to notify；` string ` notified by；` string ` notified reason。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-f5bb9b810c9641cc](../../evidence/parameters-sets-018.md#p-f5bb9b810c9641cc) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041357

```text
(config)# do-exec pnpa service fault-control <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 78 `；EOL ` RVA 0x33B65A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` fault-control level: 1-strict, 0-none。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bbf3a30fd9ffe120](../../evidence/parameters-sets-014.md#p-bbf3a30fd9ffe120) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-058755

```text
(config)# do-exec pnpa service hello <string> <string> <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 38 `；EOL ` RVA 0x33B6AB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the protocol；` string ` Specify the host, ipv4, or ipv6；` string ` Specify the host or ipaddr；` unsigned_number ` Specify the hello port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-4c01acc227679362](../../evidence/parameters-sets-006.md#p-4c01acc227679362) · [状态效果 S-a2924e905b1a8676](../../evidence/state_effects-sets-034.md#s-a2924e905b1a8676)

### path-042038

```text
(config)# do-exec pnpa service image-install <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 39 `；EOL ` RVA 0x33B6A080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the Image source file path。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-756361a048212659](../../evidence/parameters-sets-009.md#p-756361a048212659) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032870

```text
(config)# do-exec pnpa service image-install-commit <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 41 `；EOL ` RVA 0x33B6A468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032882

```text
(config)# do-exec pnpa service image-remove-inactive <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 40 `；EOL ` RVA 0x33B6A710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-037545

```text
(config)# do-exec pnpa service internal <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 79 `；EOL ` RVA 0x33B530C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` service-control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b3d83bc3bb62d34d](../../evidence/parameters-sets-014.md#p-b3d83bc3bb62d34d) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050319

```text
(config)# do-exec pnpa service location-tag <number:0..1> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 80 `；EOL ` RVA 0x33B65760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0) location tag；` string ` Specify location tag。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3c6c42bcdf2c6780](../../evidence/parameters-sets-005.md#p-3c6c42bcdf2c6780) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041301

```text
(config)# do-exec pnpa service lock-bypass <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 81 `；EOL ` RVA 0x33B65428 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enable(1) or disable(0)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-b2dd957f6c9ed270](../../evidence/parameters-sets-014.md#p-b2dd957f6c9ed270) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032477

```text
(config)# do-exec pnpa service lock-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 82 `；EOL ` RVA 0x33B65118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032463

```text
(config)# do-exec pnpa service lock-exec <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 83 `；EOL ` RVA 0x33B64E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041206

```text
(config)# do-exec pnpa service monvar-diag <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 84 `；EOL ` RVA 0x33B64BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` diag monvar string (null to reset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fb47b9e711cb8226](../../evidence/parameters-sets-019.md#p-fb47b9e711cb8226) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041118

```text
(config)# do-exec pnpa service must-ignore-config-reg <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 86 `；EOL ` RVA 0x33B64320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore config-reg: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-de80c47601a0703a](../../evidence/parameters-sets-017.md#p-de80c47601a0703a) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041147

```text
(config)# do-exec pnpa service must-ignore-config-rollback <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 87 `；EOL ` RVA 0x33B64610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore config-rollback: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-82d10f2cdf8d90c8](../../evidence/parameters-sets-010.md#p-82d10f2cdf8d90c8) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041088

```text
(config)# do-exec pnpa service must-ignore-dir-walk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 88 `；EOL ` RVA 0x33B64030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore dir-walk: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-e79ae40db74922a6](../../evidence/parameters-sets-017.md#p-e79ae40db74922a6) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041052

```text
(config)# do-exec pnpa service must-ignore-ifs-walk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 89 `；EOL ` RVA 0x33B63D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore ifs-walk: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3e18d8cfbde56d01](../../evidence/parameters-sets-005.md#p-3e18d8cfbde56d01) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041015

```text
(config)# do-exec pnpa service must-ignore-image-signature <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 90 `；EOL ` RVA 0x33B63A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore image-signature: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cba6357f2c967325](../../evidence/parameters-sets-015.md#p-cba6357f2c967325) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040975

```text
(config)# do-exec pnpa service must-ignore-reload-info <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 91 `；EOL ` RVA 0x33B63760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore reload_info: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-901d0977f1754861](../../evidence/parameters-sets-011.md#p-901d0977f1754861) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041173

```text
(config)# do-exec pnpa service must-ignore-reload-info <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 85 `；EOL ` RVA 0x33B64900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must block reload-info: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-75b90c2e33b7f873](../../evidence/parameters-sets-009.md#p-75b90c2e33b7f873) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040942

```text
(config)# do-exec pnpa service must-ignore-save-tech <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 92 `；EOL ` RVA 0x33B63470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore save-tech: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-46b4ad70bc846593](../../evidence/parameters-sets-006.md#p-46b4ad70bc846593) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040909

```text
(config)# do-exec pnpa service must-ignore-terminate-now <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 93 `；EOL ` RVA 0x33B63180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must ignore terminate now: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-df4cb64e4a88b1b6](../../evidence/parameters-sets-017.md#p-df4cb64e4a88b1b6) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040880

```text
(config)# do-exec pnpa service must-keep-backup <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 94 `；EOL ` RVA 0x33B62E90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Must keep backup: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-17d217b95f009eb6](../../evidence/parameters-sets-002.md#p-17d217b95f009eb6) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040896

```text
(config)# do-exec pnpa service napp-client <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 95 `；EOL ` RVA 0x33B62BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NAPP Client: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cf109c9cb28e456d](../../evidence/parameters-sets-016.md#p-cf109c9cb28e456d) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040865

```text
(config)# do-exec pnpa service napp-connect <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 96 `；EOL ` RVA 0x33B62870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` device SN。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-00c5eff6a64f2197](../../evidence/parameters-sets-001.md#p-00c5eff6a64f2197) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032236

```text
(config)# do-exec pnpa service napp-http-server <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 97 `；EOL ` RVA 0x33B62540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040807

```text
(config)# do-exec pnpa service napp-server <number:0..2> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 98 `；EOL ` RVA 0x33B62250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NAPP Server: 2-enable-chunking, 1-enable-no-chunking, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bf25eff6457a3b12](../../evidence/parameters-sets-015.md#p-bf25eff6457a3b12) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032188

```text
(config)# do-exec pnpa service napp-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 99 `；EOL ` RVA 0x33B61EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040748

```text
(config)# do-exec pnpa service napp-tag <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 100 `；EOL ` RVA 0x33B61C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` device SN。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8b528813987481c3](../../evidence/parameters-sets-011.md#p-8b528813987481c3) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041911

```text
(config)# do-exec pnpa service notify-now <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 42 `；EOL ` RVA 0x33B69BA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile to be notified。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-68f9ccd4c3539287](../../evidence/parameters-sets-008.md#p-68f9ccd4c3539287) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-058722

```text
(config)# do-exec pnpa service notify-service <string> <string> <string> <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 43 `；EOL ` RVA 0x33B698B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the notification type: syslog, snmp；` string ` Specify the severity；` string ` Specify the recipient；` unsigned_number ` Notify control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-70161dd8932d3652](../../evidence/parameters-sets-009.md#p-70161dd8932d3652) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041856

```text
(config)# do-exec pnpa service notify-state <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 44 `；EOL ` RVA 0x33B69510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` state msg to be notified。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d4291a2f9dc3d499](../../evidence/parameters-sets-016.md#p-d4291a2f9dc3d499) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040676

```text
(config)# do-exec pnpa service post-reload-priv <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 101 `；EOL ` RVA 0x33B61948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load(1) or save(0) post-reload-priv。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a9530d319e417cdb](../../evidence/parameters-sets-013.md#p-a9530d319e417cdb) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040691

```text
(config)# do-exec pnpa service proxy-control <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 102 `；EOL ` RVA 0x33B61658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Proxy control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d5e8c07eed1f0020](../../evidence/parameters-sets-016.md#p-d5e8c07eed1f0020) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040632

```text
(config)# do-exec pnpa service python-listener <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 111 `；EOL ` RVA 0x33B61320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Python Listener: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-c6f3c8aa68a370fd](../../evidence/parameters-sets-015.md#p-c6f3c8aa68a370fd) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-059515

```text
(config)# do-exec pnpa service query-to-client <string> <string> <string> configlet <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 112 `；EOL ` RVA 0x33B61028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` napp version string；` string ` UDI string；` string ` transaction id string；` string ` configlet string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-0e1b8d2f679cba72](../../evidence/parameters-sets-002.md#p-0e1b8d2f679cba72) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-055671

```text
(config)# do-exec pnpa service query-to-server <string> <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 113 `；EOL ` RVA 0x33B60C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` napp version string；` string ` UDI string；` string ` transaction id string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fa2c7c877e60c096](../../evidence/parameters-sets-019.md#p-fa2c7c877e60c096) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050606

```text
(config)# do-exec pnpa service redirect-backup <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 46 `；EOL ` RVA 0x33B69220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the redierction profile；` unsigned_number ` Specify redirection port (0 for as-is)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a45206e0307fbffc](../../evidence/parameters-sets-013.md#p-a45206e0307fbffc) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-050590

```text
(config)# do-exec pnpa service redirect-primary <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 47 `；EOL ` RVA 0x33B68EF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the redierction profile；` unsigned_number ` Specify redirection port (0 for as-is)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-194db4a6cc116691](../../evidence/parameters-sets-002.md#p-194db4a6cc116691) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-062191

```text
(config)# do-exec pnpa service reload as-is in <number:0..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 48 `；EOL ` RVA 0x33B68928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-237fd522c912c806](../../evidence/conditions-sets-014.md#c-237fd522c912c806) · [缺口 G-efae66d056b57871](../../evidence/gaps-sets-008.md#g-efae66d056b57871) · [参数 P-7e45b0769024b616](../../evidence/parameters-sets-010.md#p-7e45b0769024b616) · [状态效果 S-2202176addf9aad7](../../evidence/state_effects-sets-008.md#s-2202176addf9aad7)

### path-041890

```text
(config)# do-exec pnpa service reload cancel <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 48 `；EOL ` RVA 0x33B68928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-42d73ec1e0952f31](../../evidence/state_effects-sets-015.md#s-42d73ec1e0952f31)

### path-032576

```text
(config)# do-exec pnpa service reset <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 45 `；EOL ` RVA 0x33B65D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040551

```text
(config)# do-exec pnpa service resolve-discovery <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 114 `；EOL ` RVA 0x33B608A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` hostname string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-9752fb71a61bd149](../../evidence/parameters-sets-012.md#p-9752fb71a61bd149) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040523

```text
(config)# do-exec pnpa service resolve-dns <number:0..4> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 115 `；EOL ` RVA 0x33B605B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Resolution: 0-default, 1-v4-only, 2-v6-only, 3-v4-first, 4-v6-first。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fecb2817928f3c6a](../../evidence/parameters-sets-019.md#p-fecb2817928f3c6a) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040540

```text
(config)# do-exec pnpa service resolve-hostname <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 116 `；EOL ` RVA 0x33B602C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` hostname string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-82fa424a0db43254](../../evidence/parameters-sets-010.md#p-82fa424a0db43254) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032769

```text
(config)# do-exec pnpa service save-tech <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 49 `；EOL ` RVA 0x33B68520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-041769

```text
(config)# do-exec pnpa service script <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 50 `；EOL ` RVA 0x33B68190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Location of the script。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-588eb97ffa148d20](../../evidence/parameters-sets-007.md#p-588eb97ffa148d20) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032926

```text
(config)# do-exec pnpa service sdwan-ready <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 53 `；EOL ` RVA 0x33B6B4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042110

```text
(config)# do-exec pnpa service sdwan-start <number:0..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 51 `；EOL ` RVA 0x33B6BA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` sdwan use case。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-4916a1a60f87a02b](../../evidence/parameters-sets-006.md#p-4916a1a60f87a02b) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032935

```text
(config)# do-exec pnpa service sdwan-stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 52 `；EOL ` RVA 0x33B6B748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040468

```text
(config)# do-exec pnpa service security-ending-max <number:1..4294967295> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 117 `；EOL ` RVA 0x33B5FF90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` security ending max length。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-e9119277ed6a8fe9](../../evidence/parameters-sets-017.md#p-e9119277ed6a8fe9) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040439

```text
(config)# do-exec pnpa service security-enforcement <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 118 `；EOL ` RVA 0x33B5FCA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enforce security: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-298e91827eac381c](../../evidence/parameters-sets-004.md#p-298e91827eac381c) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040252

```text
(config)# do-exec pnpa service server-identity-check <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 124 `；EOL ` RVA 0x33B5E210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Server ID validation: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-da1cfe4bd7b3fe2c](../../evidence/parameters-sets-016.md#p-da1cfe4bd7b3fe2c) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040399

```text
(config)# do-exec pnpa service show-file <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 54 `；EOL ` RVA 0x33B5F9B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-ee232f3ef7c1c75f](../../evidence/parameters-sets-018.md#p-ee232f3ef7c1c75f) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032018

```text
(config)# do-exec pnpa service show-running-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 55 `；EOL ` RVA 0x33B5F6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-032001

```text
(config)# do-exec pnpa service show-startup-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 56 `；EOL ` RVA 0x33B5F400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-049578

```text
(config)# do-exec pnpa service sid auth-only <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 119 `；EOL ` RVA 0x33B5F138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SID auth only: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-90477e5f166ab209](../../evidence/parameters-sets-011.md#p-90477e5f166ab209) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-049488

```text
(config)# do-exec pnpa service sid must-renew <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 121 `；EOL ` RVA 0x33B5EB80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SID must renew: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-32c2d63e16682f7f](../../evidence/parameters-sets-004.md#p-32c2d63e16682f7f) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-049530

```text
(config)# do-exec pnpa service sid must-validate <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 120 `；EOL ` RVA 0x33B5EE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SID must validate: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-12062fb47306577e](../../evidence/parameters-sets-002.md#p-12062fb47306577e) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-055487

```text
(config)# do-exec pnpa service sid update <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 122 `；EOL ` RVA 0x33B5E898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the new sid；` string ` Specify the profile。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-47ee00b12a0b4c47](../../evidence/parameters-sets-006.md#p-47ee00b12a0b4c47) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-049376

```text
(config)# do-exec pnpa service sid validation <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 123 `；EOL ` RVA 0x33B5E568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SID validation: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a88bef6bb1b4f758](../../evidence/parameters-sets-013.md#p-a88bef6bb1b4f758) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040204

```text
(config)# do-exec pnpa service sleep-for <number:1..3600> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 125 `；EOL ` RVA 0x33B5DF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` sleep time in seconds (No ctrl-C)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7a7e08538b1b49a5](../../evidence/parameters-sets-010.md#p-7a7e08538b1b49a5) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-040166

```text
(config)# do-exec pnpa service smu-task-activate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 57 `；EOL ` RVA 0x33B5DC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d1cb7f9bcdcf753d](../../evidence/parameters-sets-016.md#p-d1cb7f9bcdcf753d) · [状态效果 S-af5439e5e7123e23](../../evidence/state_effects-sets-037.md#s-af5439e5e7123e23)

### path-049243

```text
(config)# do-exec pnpa service smu-task-add <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 58 `；EOL ` RVA 0x33B5D920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the bundle name；` string ` Specify the bundle URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-3dbbe73eff66b8a0](../../evidence/parameters-sets-005.md#p-3dbbe73eff66b8a0) · [状态效果 S-3fc2cfd480b5cb54](../../evidence/state_effects-sets-014.md#s-3fc2cfd480b5cb54)

### path-031909

```text
(config)# do-exec pnpa service smu-task-clear-all <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 59 `；EOL ` RVA 0x33B5D548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-7c0514d9a17d7dcb](../../evidence/state_effects-sets-026.md#s-7c0514d9a17d7dcb)

### path-031891

```text
(config)# do-exec pnpa service smu-task-commit <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 60 `；EOL ` RVA 0x33B5D290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-36603bc2bf7d389c](../../evidence/state_effects-sets-012.md#s-36603bc2bf7d389c)

### path-039992

```text
(config)# do-exec pnpa service smu-task-deactivate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 61 `；EOL ` RVA 0x33B5D010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-5b889fd0e2d4722a](../../evidence/parameters-sets-007.md#p-5b889fd0e2d4722a) · [状态效果 S-21708cabfde20d9a](../../evidence/state_effects-sets-008.md#s-21708cabfde20d9a)

### path-039945

```text
(config)# do-exec pnpa service smu-task-remove <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 62 `；EOL ` RVA 0x33B5CD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the bundle name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-ee910b235e862416](../../evidence/parameters-sets-018.md#p-ee910b235e862416) · [状态效果 S-fe2df4dedcdb1a86](../../evidence/state_effects-sets-054.md#s-fe2df4dedcdb1a86)

### path-031842

```text
(config)# do-exec pnpa service smu-task-run <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 63 `；EOL ` RVA 0x33B5C9E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-4de4dc217624a94c](../../evidence/state_effects-sets-017.md#s-4de4dc217624a94c)

### path-031825

```text
(config)# do-exec pnpa service smu-task-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 64 `；EOL ` RVA 0x33B5C730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-af2004863d242c74](../../evidence/state_effects-sets-037.md#s-af2004863d242c74)

### path-039863

```text
(config)# do-exec pnpa service smu-verify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 65 `；EOL ` RVA 0x33B5C490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-cc0b46ba0581021b](../../evidence/parameters-sets-015.md#p-cc0b46ba0581021b) · [状态效果 S-80cd9f79ba73bfc7](../../evidence/state_effects-sets-027.md#s-80cd9f79ba73bfc7)

### path-039720

```text
(config)# do-exec pnpa service snmp <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 126 `；EOL ` RVA 0x33B5C130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the request SNMP PDU in Base64。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-94473c5c84f29ce8](../../evidence/parameters-sets-011.md#p-94473c5c84f29ce8) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-054987

```text
(config)# do-exec pnpa service snooping <number:0..1> <number:0..4094> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 127 `；EOL ` RVA 0x33B5BE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enforce snooping: 1-enable, 0-disable；` unsigned_number ` vlan id；` string ` Specify the dhcp option string (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d9f80e33b5e3a816](../../evidence/parameters-sets-016.md#p-d9f80e33b5e3a816) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039554

```text
(config)# do-exec pnpa service stack-renumber <number:1..9> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 128 `；EOL ` RVA 0x33B5B7D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Top of stack switch number: 1-9。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-1800deaa8355c918](../../evidence/parameters-sets-002.md#p-1800deaa8355c918) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039616

```text
(config)# do-exec pnpa service stack-reorder <number:1..9> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 129 `；EOL ` RVA 0x33B5BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Top of stack switch number: 1-9。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a790aecbeed8eeb9](../../evidence/parameters-sets-013.md#p-a790aecbeed8eeb9) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-042079

```text
(config)# do-exec pnpa service tls-tunnel-notify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 152 `；EOL ` RVA 0x33B6B218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` tls tunnel name。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-1da18c2d26058ef1](../../evidence/parameters-sets-003.md#p-1da18c2d26058ef1) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039498

```text
(config)# do-exec pnpa service token-auth-set <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 130 `；EOL ` RVA 0x33B5B4F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the token-auth string。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7b905f8bac36bef9](../../evidence/parameters-sets-010.md#p-7b905f8bac36bef9) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-047693

```text
(config)# do-exec pnpa service trustpoint-install <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 153 `；EOL ` RVA 0x33B57AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the trustpoint label；` string ` Specify the certificate URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-d3f8cd0bf21cc6a9](../../evidence/parameters-sets-016.md#p-d3f8cd0bf21cc6a9) · [状态效果 S-179c0bf9976693ff](../../evidence/state_effects-sets-005.md#s-179c0bf9976693ff)

### path-038472

```text
(config)# do-exec pnpa service trustpoint-uninstall <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 154 `；EOL ` RVA 0x33B57720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the trustpoint label。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-fcbe95cdcfbd4544](../../evidence/parameters-sets-019.md#p-fcbe95cdcfbd4544) · [状态效果 S-682cb798621414e9](../../evidence/state_effects-sets-022.md#s-682cb798621414e9)

### path-038504

```text
(config)# do-exec pnpa service trustpool-install <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 155 `；EOL ` RVA 0x33B57408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the bundle URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-043798f3537f3872](../../evidence/parameters-sets-001.md#p-043798f3537f3872) · [状态效果 S-75288578afc3e427](../../evidence/state_effects-sets-025.md#s-75288578afc3e427)

### path-031228

```text
(config)# do-exec pnpa service trustpool-uninstall <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 156 `；EOL ` RVA 0x33B57070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-203e541ae7da8043](../../evidence/state_effects-sets-007.md#s-203e541ae7da8043)

### path-039449

```text
(config)# do-exec pnpa service udi-checking <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 131 `；EOL ` RVA 0x33B5B200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enforce udi checking: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-47ae8fb6c02bac0d](../../evidence/parameters-sets-006.md#p-47ae8fb6c02bac0d) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031668

```text
(config)# do-exec pnpa service udi-refresh <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 132 `；EOL ` RVA 0x33B5AEF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031643

```text
(config)# do-exec pnpa service unlock-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 133 `；EOL ` RVA 0x33B5AC48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031622

```text
(config)# do-exec pnpa service unlock-exec <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 134 `；EOL ` RVA 0x33B5A9A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039247

```text
(config)# do-exec pnpa service use-ntp-server <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 135 `；EOL ` RVA 0x33B5A720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the ntp server name (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-dd997acde6d6e31b](../../evidence/parameters-sets-017.md#p-dd997acde6d6e31b) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039197

```text
(config)# do-exec pnpa service use-src-intf <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 136 `；EOL ` RVA 0x33B5A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the source interface name (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7b726c2f0dd3a7ec](../../evidence/parameters-sets-010.md#p-7b726c2f0dd3a7ec) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039152

```text
(config)# do-exec pnpa service use-unix-disk <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 137 `；EOL ` RVA 0x33B5A148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Use Unix disk: 1-Yes, 0-No。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2757a78edd0c9a69](../../evidence/parameters-sets-003.md#p-2757a78edd0c9a69) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-039099

```text
(config)# do-exec pnpa service use-vrf <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 138 `；EOL ` RVA 0x33B59E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the vrf name (null to unset)。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-51080c07389089a0](../../evidence/parameters-sets-007.md#p-51080c07389089a0) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038419

```text
(config)# do-exec pnpa service validate <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 157 `；EOL ` RVA 0x33B56DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2cd423664f9b5606](../../evidence/parameters-sets-004.md#p-2cd423664f9b5606) · [状态效果 S-0a5995051e651098](../../evidence/state_effects-sets-003.md#s-0a5995051e651098)

### path-037574

```text
(config)# do-exec pnpa service verbose <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 139 `；EOL ` RVA 0x33B533B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` verbose-control: 1-enable, 0-disable。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-be51a107b43ad9ed](../../evidence/parameters-sets-014.md#p-be51a107b43ad9ed) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038379

```text
(config)# do-exec pnpa service verify <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 158 `；EOL ` RVA 0x33B56A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the file URL。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-24b3cb7039281dd9](../../evidence/parameters-sets-003.md#p-24b3cb7039281dd9) · [状态效果 S-3a97328cdb6deee7](../../evidence/state_effects-sets-013.md#s-3a97328cdb6deee7)

### path-038325

```text
(config)# do-exec pnpa service wait-time <number:0..100> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 159 `；EOL ` RVA 0x33B566C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` wait type。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-2cca3fb3c6cbf767](../../evidence/parameters-sets-004.md#p-2cca3fb3c6cbf767) · [状态效果 S-5783e794e57d35f7](../../evidence/state_effects-sets-019.md#s-5783e794e57d35f7)

### path-031547

```text
(config)# do-exec pnpa service wakeup <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 140 `；EOL ` RVA 0x33B59B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031137

```text
(config)# do-exec pnpa service watch-ack-notifications <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 160 `；EOL ` RVA 0x33B56338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031117

```text
(config)# do-exec pnpa service watch-all <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 161 `；EOL ` RVA 0x33B56090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031090

```text
(config)# do-exec pnpa service watch-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 162 `；EOL ` RVA 0x33B55DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031071

```text
(config)# do-exec pnpa service watch-config <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 163 `；EOL ` RVA 0x33B55B40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038102

```text
(config)# do-exec pnpa service watch-default-action <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 164 `；EOL ` RVA 0x33B55810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` action to take - wakeup-pnp-server-now, notify-pnp-server-now, syslog, etc.。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-eb9e86917c1668d8](../../evidence/parameters-sets-018.md#p-eb9e86917c1668d8) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-047253

```text
(config)# do-exec pnpa service watch-disable <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 165 `；EOL ` RVA 0x33B554C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` watch_id；` string ` event to unwatch。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-bc901cb7b87b0261](../../evidence/parameters-sets-014.md#p-bc901cb7b87b0261) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-059346

```text
(config)# do-exec pnpa service watch-enable <string> <string> <string> <number:0..4294967295> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 166 `；EOL ` RVA 0x33B550E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` watch_id；` string ` event to watch；` string ` event param str ("null" for default)；` unsigned_number ` event param value；` string ` action to take - wakeup-pnp-server-now, notify-pnp-server-now, syslog, etc.。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-eb5241440f036fd2](../../evidence/parameters-sets-018.md#p-eb5241440f036fd2) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-030983

```text
(config)# do-exec pnpa service watch-pnp-profile <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 167 `；EOL ` RVA 0x33B54C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-030958

```text
(config)# do-exec pnpa service watch-pnp-server <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 168 `；EOL ` RVA 0x33B549C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-030937

```text
(config)# do-exec pnpa service watch-pnp-service <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 169 `；EOL ` RVA 0x33B54718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-030917

```text
(config)# do-exec pnpa service watch-pnp-state <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 170 `；EOL ` RVA 0x33B54470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-030888

```text
(config)# do-exec pnpa service watch-system <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 171 `；EOL ` RVA 0x33B541C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-030864

```text
(config)# do-exec pnpa service watch-tls-tunnel <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 172 `；EOL ` RVA 0x33B53F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-037693

```text
(config)# do-exec pnpa service webui set <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 173 `；EOL ` RVA 0x33B53C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-037656

```text
(config)# do-exec pnpa service webui start <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 175 `；EOL ` RVA 0x33B53998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-037611

```text
(config)# do-exec pnpa service webui stop <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 174 `；EOL ` RVA 0x33B536A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031499

```text
(config)# do-exec pnpa service xep-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 141 `；EOL ` RVA 0x33B59868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038940

```text
(config)# do-exec pnpa service xep-ignore-disconnect <number:0..1> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 142 `；EOL ` RVA 0x33B595E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Ignore Disconnect: 0-no, 1-yes。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-a80109c842869060](../../evidence/parameters-sets-013.md#p-a80109c842869060) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031461

```text
(config)# do-exec pnpa service xep-show <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 143 `；EOL ` RVA 0x33B592D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038850

```text
(config)# do-exec pnpa service xep-tracking <number:0..4> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 144 `；EOL ` RVA 0x33B59048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` xep-tracking: 0-none, 1-all, 2-Rx, 3-Tx, 4-Drop。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-869afff84899f879](../../evidence/parameters-sets-010.md#p-869afff84899f879) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031431

```text
(config)# do-exec pnpa service xml-clear <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 145 `；EOL ` RVA 0x33B58D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038758

```text
(config)# do-exec pnpa service xml-process <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 146 `；EOL ` RVA 0x33B58AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the URL of a text file containing the XML message。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-7a094047a2aab620](../../evidence/parameters-sets-010.md#p-7a094047a2aab620) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-059396

```text
(config)# do-exec pnpa service xml-profile <string> <string> <string> <string> <number:0..65535> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 147 `；EOL ` RVA 0x33B587C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the profile for XML encoding；` string ` Specify the protocol；` string ` Specify the host, ipv4, or ipv6；` string ` Specify the host or ipaddr；` unsigned_number ` Specify the svc_xml_profile port。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-0c96bbfdba221420](../../evidence/parameters-sets-001.md#p-0c96bbfdba221420) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-031365

```text
(config)# do-exec pnpa service xml-replay <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 148 `；EOL ` RVA 0x33B583B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-038606

```text
(config)# do-exec pnpa service xml-udi <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 149 `；EOL ` RVA 0x33B58138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the udi for XML encoding。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-75dab89d28d346c4](../../evidence/parameters-sets-009.md#p-75dab89d28d346c4) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-047723

```text
(config)# do-exec pnpa service xml-usr <string> <string> <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 150 `；EOL ` RVA 0x33B57E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Specify the usr for XML encoding；` string ` Specify the pwd for XML encoding。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [参数 P-8a1bb1606a99457c](../../evidence/parameters-sets-011.md#p-8a1bb1606a99457c) · [状态效果 S-c52a69a432877fdb](../../evidence/state_effects-sets-042.md#s-c52a69a432877fdb)

### path-027462

```text
(config)# do-exec pnpa summary <cr>
```

Handler ` RVA 0xC98AC60 `；selector ` 151 `；EOL ` RVA 0x33B52D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-056821

```text
(config)# do-exec processes cpu pid <number:1..4294967295> autoprofile threshold <number:50..400> <cr>
```

Handler ` RVA 0xE086C10 `；selector ` 2 `；EOL ` RVA 0x341DB8E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Process ID to use；` unsigned_number ` Threshold (in msec) after which profiling is turned on。

[条件 C-4df3d781550062a7](../../evidence/conditions-sets-031.md#c-4df3d781550062a7) · [参数 P-69efa937186747a6](../../evidence/parameters-sets-008.md#p-69efa937186747a6) · [状态效果 S-fc6088fe24d965bb](../../evidence/state_effects-sets-053.md#s-fc6088fe24d965bb)

### path-052236

```text
(config)# do-exec processes cpu pid <number:1..4294967295> priority low <cr>
```

Handler ` RVA 0xE0877D0 `；selector ` 0 `；EOL ` RVA 0x341DBBE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Process ID to use。

[条件 C-47ae5bd399012d8d](../../evidence/conditions-sets-028.md#c-47ae5bd399012d8d) · [参数 P-47072628751ce24e](../../evidence/parameters-sets-006.md#p-47072628751ce24e) · [状态效果 S-6ed3e24858b08cb7](../../evidence/state_effects-sets-024.md#s-6ed3e24858b08cb7)

### path-052263

```text
(config)# do-exec processes cpu pid <number:1..4294967295> quantum <number:20..200> <cr>
```

Handler ` RVA 0xE087650 `；selector ` 0 `；EOL ` RVA 0x341DBFD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Process ID to use；` unsigned_number ` quantum value in msec。

[条件 C-6a3dbba5b699088f](../../evidence/conditions-sets-041.md#c-6a3dbba5b699088f) · [参数 P-49d326b177f30f6d](../../evidence/parameters-sets-006.md#p-49d326b177f30f6d) · [状态效果 S-fc6088fe24d965bb](../../evidence/state_effects-sets-053.md#s-fc6088fe24d965bb)

### path-026167

```text
(config)# do-exec profile hogs <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 4 `；EOL ` RVA 0x34122D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ff61e0a82c1c3c7](../../evidence/conditions-sets-012.md#c-1ff61e0a82c1c3c7) · [状态效果 S-cb033872d6bbfcfe](../../evidence/state_effects-sets-043.md#s-cb033872d6bbfcfe)

### path-026134

```text
(config)# do-exec profile start <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 2 `；EOL ` RVA 0x34122848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ff61e0a82c1c3c7](../../evidence/conditions-sets-012.md#c-1ff61e0a82c1c3c7) · [状态效果 S-cb033872d6bbfcfe](../../evidence/state_effects-sets-043.md#s-cb033872d6bbfcfe)

### path-026154

```text
(config)# do-exec profile stop <cr>
```

Handler ` RVA 0xD7AFAE0 `；selector ` 3 `；EOL ` RVA 0x34122AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ff61e0a82c1c3c7](../../evidence/conditions-sets-012.md#c-1ff61e0a82c1c3c7) · [状态效果 S-cb033872d6bbfcfe](../../evidence/state_effects-sets-043.md#s-cb033872d6bbfcfe)

### path-060514

```text
(config)# do-exec profile task <number:0..4294967295> <cr>
```

Handler ` RVA 0xD7AFF90 `；selector ` 0 `；EOL ` RVA 0x34122548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` list of specific process ids (pids)。

[条件 C-f9701d05580cee09](../../evidence/conditions-sets-096.md#c-f9701d05580cee09) · [缺口 G-d0ce743b5c174f98](../../evidence/gaps-sets-007.md#g-d0ce743b5c174f98) · [参数 P-82300bf882015674](../../evidence/parameters-sets-010.md#p-82300bf882015674) · [状态效果 S-279889439fa87589](../../evidence/state_effects-sets-009.md#s-279889439fa87589)

### path-025947

```text
(config)# do-exec pwd <cr>
```

Handler ` RVA 0xD6577A0 `；selector ` 0 `；EOL ` RVA 0x33EB9310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1560fa3b6bd78342](../../evidence/conditions-sets-008.md#c-1560fa3b6bd78342) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-052465

```text
(config)# do-exec redundancy application reload group <number:1..2> peer <cr>
```

Handler ` RVA 0xCC27200 `；selector ` 0 `；EOL ` RVA 0x33C22148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group number。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [参数 P-1ea83a5be9f8743b](../../evidence/parameters-sets-003.md#p-1ea83a5be9f8743b) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-052498

```text
(config)# do-exec redundancy application reload group <number:1..2> self <cr>
```

Handler ` RVA 0xCC27140 `；selector ` 0 `；EOL ` RVA 0x33C223F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` group number。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [参数 P-1ea83a5be9f8743b](../../evidence/parameters-sets-003.md#p-1ea83a5be9f8743b) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-034941

```text
(config)# do-exec redundancy application test-client disable <cr>
```

Handler ` RVA 0xCC25820 `；selector ` 0 `；EOL ` RVA 0x33C21B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-034876

```text
(config)# do-exec redundancy application test-client enable <cr>
```

Handler ` RVA 0xCC257D0 `；selector ` 0 `；EOL ` RVA 0x33C21870 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-026755

```text
(config)# do-exec redundancy force-switchover <cr>
```

Handler ` RVA 0xD527E60 `；selector ` 0 `；EOL ` RVA 0x33E7AA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01ef9b57c5950e3d](../../evidence/conditions-sets-001.md#c-01ef9b57c5950e3d) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-028685

```text
(config)# do-exec redundancy keepalive enable <cr>
```

Handler ` RVA 0xD527AA0 `；selector ` 0 `；EOL ` RVA 0x33E7A638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be23f1c11078db98](../../evidence/conditions-sets-073.md#c-be23f1c11078db98) · [状态效果 S-2e3df9d835f81c0f](../../evidence/state_effects-sets-010.md#s-2e3df9d835f81c0f)

### path-028613

```text
(config)# do-exec redundancy reload peer <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 8 `；EOL ` RVA 0x33FDA628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d55ca44b6a1e097](../../evidence/conditions-sets-042.md#c-6d55ca44b6a1e097) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-028747

```text
(config)# do-exec redundancy reload shelf <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 9 `；EOL ` RVA 0x33FDAA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34d2e9539c53f5e4](../../evidence/conditions-sets-021.md#c-34d2e9539c53f5e4) · [状态效果 S-2cfe662f30f360b3](../../evidence/state_effects-sets-010.md#s-2cfe662f30f360b3)

### path-060793

```text
(config)# do-exec redundancy reload shelf <number:dynamic> <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 9 `；EOL ` RVA 0x33FDAA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` shelf id。

[条件 C-1881ee6371129614](../../evidence/conditions-sets-010.md#c-1881ee6371129614) · [缺口 G-ab7e900701b1f55d](../../evidence/gaps-sets-006.md#g-ab7e900701b1f55d) · [参数 P-17b95e6b31b93d8e](../../evidence/parameters-sets-002.md#p-17b95e6b31b93d8e) · [状态效果 S-6faf987aa688118f](../../evidence/state_effects-sets-024.md#s-6faf987aa688118f)

### path-026616

```text
(config)# do-exec redundancy switch-activity <cr>
```

Handler ` RVA 0xDB568D0 `；selector ` 6 `；EOL ` RVA 0x33FDA2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c9fa8d0bafacac50](../../evidence/conditions-sets-078.md#c-c9fa8d0bafacac50) · [状态效果 S-fe686af237f62fd1](../../evidence/state_effects-sets-054.md#s-fe686af237f62fd1)

### path-060646

```text
(config)# do-exec release dhcp <interface> <cr>
```

Handler ` RVA 0xF4794E0 `；selector ` 0 `；EOL ` RVA 0x34653360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2d8a5de41c589406](../../evidence/conditions-sets-018.md#c-2d8a5de41c589406) · [缺口 G-a3752b1a07f5b193](../../evidence/gaps-sets-006.md#g-a3752b1a07f5b193) · [参数 P-3975f2ca50233cdd](../../evidence/parameters-sets-005.md#p-3975f2ca50233cdd) · [状态效果 S-7cba0e745d28bd38](../../evidence/state_effects-sets-026.md#s-7cba0e745d28bd38)

### path-025711

```text
(config)# do-exec reload <cr>
```

Handler ` RVA 0xE004870 `；selector ` 0 `；EOL ` RVA 0x341641B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88af6400836c226f](../../evidence/conditions-sets-053.md#c-88af6400836c226f) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060535

```text
(config)# do-exec reload slot <number:dynamic> <cr>
```

Handler ` RVA 0xE004870 `；selector ` 0 `；EOL ` RVA 0x341641B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Slot number of RP or line card。

[条件 C-5246cfd250633293](../../evidence/conditions-sets-032.md#c-5246cfd250633293) · [缺口 G-a45562584972e93f](../../evidence/gaps-sets-006.md#g-a45562584972e93f) · [参数 P-eed18e0eb10fe701](../../evidence/parameters-sets-018.md#p-eed18e0eb10fe701) · [状态效果 S-8ff239f8f55e83e9](../../evidence/state_effects-sets-031.md#s-8ff239f8f55e83e9)

### path-060677

```text
(config)# do-exec rename <url:dynamic> <string> <cr>
```

Handler ` RVA 0xD65D020 `；selector ` 0 `；EOL ` RVA 0x33EBA2F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Destination file path。

[条件 C-34833549a5bf344d](../../evidence/conditions-sets-020.md#c-34833549a5bf344d) · [缺口 G-e4f125c3ef67426c](../../evidence/gaps-sets-008.md#g-e4f125c3ef67426c) · [参数 P-8601446a200039dc](../../evidence/parameters-sets-010.md#p-8601446a200039dc) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060647

```text
(config)# do-exec renew dhcp <interface> <cr>
```

Handler ` RVA 0xF4794E0 `；selector ` 0 `；EOL ` RVA 0x34658298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d08d649bfaf077b4](../../evidence/conditions-sets-080.md#c-d08d649bfaf077b4) · [缺口 G-0117a53496e03d45](../../evidence/gaps-sets-001.md#g-0117a53496e03d45) · [参数 P-b068d272c435e85b](../../evidence/parameters-sets-013.md#p-b068d272c435e85b) · [状态效果 S-e2fd40d4dd6c5811](../../evidence/state_effects-sets-048.md#s-e2fd40d4dd6c5811)

### path-061247

```text
(config)# do-exec renew ip dhcp snooping database <cr>
```

Handler ` RVA 0x15FAA0C0 `；selector ` 0 `；EOL ` RVA 0x35E7FB30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ecc2ebebae670d73](../../evidence/conditions-sets-091.md#c-ecc2ebebae670d73) · [缺口 G-850c42c32eed8d3c](../../evidence/gaps-sets-005.md#g-850c42c32eed8d3c) · [状态效果 S-216639b6ee999b32](../../evidence/state_effects-sets-008.md#s-216639b6ee999b32)

### path-034156

```text
(config)# do-exec request consent-token generate-challenge shell-access <cr>
```

Handler ` RVA 0x156982F0 `；selector ` 0 `；EOL ` RVA 0x35D7BAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5f7494206c386f65](../../evidence/conditions-sets-037.md#c-5f7494206c386f65) · [状态效果 S-4a443b4ea79cfddb](../../evidence/state_effects-sets-016.md#s-4a443b4ea79cfddb)

### path-061838

```text
(config)# do-exec request consent-token generate-challenge shell-access auth-timeout <number:dynamic> <cr>
```

Handler ` RVA 0x156982F0 `；selector ` 0 `；EOL ` RVA 0x35D7BAC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` authentication validity timeout in minutes。

[条件 C-625ae03e2b37d0c9](../../evidence/conditions-sets-038.md#c-625ae03e2b37d0c9) · [缺口 G-dbfc9c0e01b0083a](../../evidence/gaps-sets-008.md#g-dbfc9c0e01b0083a) · [参数 P-5f50ae2e5821ee3a](../../evidence/parameters-sets-008.md#p-5f50ae2e5821ee3a) · [状态效果 S-4a443b4ea79cfddb](../../evidence/state_effects-sets-016.md#s-4a443b4ea79cfddb)

### path-028057

```text
(config)# do-exec request license new-udi <cr>
```

Handler ` RVA 0xBB696E0 `；selector ` 0 `；EOL ` RVA 0x3386A530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d752cf956ddab6b](../../evidence/conditions-sets-042.md#c-6d752cf956ddab6b) · [状态效果 S-dab3c8b1531ec9c8](../../evidence/state_effects-sets-046.md#s-dab3c8b1531ec9c8)

### path-056780

```text
(config)# do-exec request platform software netconf-yang key generate rsa <cr>
```

Handler ` RVA 0xE9DA2E0 `；selector ` 0 `；EOL ` RVA 0x34382DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-504957a3650c2448](../../evidence/conditions-sets-031.md#c-504957a3650c2448) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-026267

```text
(config)# do-exec request tech-support <cr>
```

Handler ` RVA 0xEB1FF10 `；selector ` 0 `；EOL ` RVA 0x343B4048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d7673a4a02446503](../../evidence/conditions-sets-083.md#c-d7673a4a02446503) · [状态效果 S-ccba5233851438dc](../../evidence/state_effects-sets-043.md#s-ccba5233851438dc)

### path-025770

```text
(config)# do-exec restart <cr>
```

Handler ` RVA 0xF43B510 `；selector ` 0 `；EOL ` RVA 0x34648EA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ccb755ee6423829e](../../evidence/conditions-sets-079.md#c-ccb755ee6423829e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025666

```text
(config)# do-exec resume <cr>
```

Handler ` RVA 0xDE857D0 `；selector ` 0 `；EOL ` RVA 0x341875E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-290b33e33c70fc4e](../../evidence/conditions-sets-016.md#c-290b33e33c70fc4e) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060384

```text
(config)# do-exec resume <number:dynamic> <cr>
```

Handler ` RVA 0xDE857D0 `；selector ` 0 `；EOL ` RVA 0x341875E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` The number of an active network connection。

[条件 C-377fbeedc508744c](../../evidence/conditions-sets-022.md#c-377fbeedc508744c) · [缺口 G-0e54e099ac4787e7](../../evidence/gaps-sets-001.md#g-0e54e099ac4787e7) · [参数 P-572844a6669cc50b](../../evidence/parameters-sets-007.md#p-572844a6669cc50b) · [状态效果 S-600fb67f34ddfa84](../../evidence/state_effects-sets-021.md#s-600fb67f34ddfa84)

### path-060609

```text
(config)# do-exec rlogin <string> <?tcpport_action@5555892487d8> <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 1 `；EOL ` RVA 0x33CF53F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-47ff2d2ae61d543a](../../evidence/conditions-sets-028.md#c-47ff2d2ae61d543a) · [缺口 G-85ce6e95092955f7](../../evidence/gaps-sets-005.md#g-85ce6e95092955f7) · [参数 P-bb3844a5f8368b87](../../evidence/parameters-sets-014.md#p-bb3844a5f8368b87) · [状态效果 S-4dc20353b1619995](../../evidence/state_effects-sets-017.md#s-4dc20353b1619995)

### path-060614

```text
(config)# do-exec rlogin <string> <?tcpport_action@5555892487d8> <cr>
```

Handler ` RVA 0xDE84C20 `；selector ` 0 `；EOL ` RVA 0x33CF56B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-4d9b6fa0c139819a](../../evidence/conditions-sets-030.md#c-4d9b6fa0c139819a) · [缺口 G-85ce6e95092955f7](../../evidence/gaps-sets-005.md#g-85ce6e95092955f7) · [参数 P-bb3844a5f8368b87](../../evidence/parameters-sets-014.md#p-bb3844a5f8368b87) · [状态效果 S-4dc20353b1619995](../../evidence/state_effects-sets-017.md#s-4dc20353b1619995)

### path-060615

```text
(config)# do-exec rlogin <string> <?tcpport_action@5555892487d8> <cr>
```

Handler ` RVA 0xCE631F0 `；selector ` 0 `；EOL ` RVA 0x33CF56E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IP address or hostname of a remote system。

[条件 C-475eba479418c391](../../evidence/conditions-sets-028.md#c-475eba479418c391) · [缺口 G-85ce6e95092955f7](../../evidence/gaps-sets-005.md#g-85ce6e95092955f7) · [参数 P-bb3844a5f8368b87](../../evidence/parameters-sets-014.md#p-bb3844a5f8368b87) · [状态效果 S-4dc20353b1619995](../../evidence/state_effects-sets-017.md#s-4dc20353b1619995)

### path-025943

```text
(config)# do-exec rmdir <cr>
```

Handler ` RVA 0xD658590 `；selector ` 0 `；EOL ` RVA 0x33EB8A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0bbc4036072e55c5](../../evidence/conditions-sets-005.md#c-0bbc4036072e55c5) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060436

```text
(config)# do-exec rmdir <url:dynamic> <cr>
```

Handler ` RVA 0xD658590 `；selector ` 0 `；EOL ` RVA 0x33EB8A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-16d4ae28f490e4a5](../../evidence/conditions-sets-009.md#c-16d4ae28f490e4a5) · [缺口 G-539c2195a156d44f](../../evidence/gaps-sets-003.md#g-539c2195a156d44f) · [参数 P-d0ba7c517bbda24b](../../evidence/parameters-sets-016.md#p-d0ba7c517bbda24b) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062750

```text
(config)# do-exec routing-context vrf <?option@5555897d50b8> <cr>
```

Handler ` RVA 0xE24C600 `；selector ` 0 `；EOL ` RVA 0x34280D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-02638373a0178941](../../evidence/conditions-sets-001.md#c-02638373a0178941) · [缺口 G-f45d51381c495d7b](../../evidence/gaps-sets-008.md#g-f45d51381c495d7b) · [状态效果 S-fd53d52aeb17f0dc](../../evidence/state_effects-sets-054.md#s-fd53d52aeb17f0dc)

### path-029297

```text
(config)# do-exec routing-context vrf global <cr>
```

Handler ` RVA 0xE24C600 `；selector ` 0 `；EOL ` RVA 0x34280D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb79c8341d670e8e](../../evidence/conditions-sets-097.md#c-fb79c8341d670e8e) · [状态效果 S-193f76043f15e12a](../../evidence/state_effects-sets-006.md#s-193f76043f15e12a)

### path-029021

```text
(config)# do-exec rsh <string> <string> <cr>
```

Handler ` RVA 0xD004170 `；selector ` 0 `；EOL ` RVA 0x33D7B938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IP address or hostname of rsh server；` string ` Command to be executed remotely。

[条件 C-90ebb260ac291ec8](../../evidence/conditions-sets-056.md#c-90ebb260ac291ec8) · [参数 P-a830d8d1cbc4fe2c](../../evidence/parameters-sets-013.md#p-a830d8d1cbc4fe2c) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-060943

```text
(config)# do-exec sdlc test <interface> <number:1..255> <cr>
```

Handler ` RVA 0x114DF750 `；selector ` 1 `；EOL ` RVA 0x355000C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SDLC Address in Hex。

[条件 C-6a00209749765c07](../../evidence/conditions-sets-041.md#c-6a00209749765c07) · [缺口 G-8d5b1ab578ec3754](../../evidence/gaps-sets-005.md#g-8d5b1ab578ec3754) · [参数 P-550616efa9a6b674](../../evidence/parameters-sets-007.md#p-550616efa9a6b674) · [状态效果 S-ad168f003573995b](../../evidence/state_effects-sets-037.md#s-ad168f003573995b)

### path-060381

```text
(config)# do-exec send <?ttyline_action@5555896b7ae8> <cr>
```

Handler ` RVA 0xE006590 `；selector ` 0 `；EOL ` RVA 0x34163B10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d76c28d80d0ecb12](../../evidence/conditions-sets-083.md#c-d76c28d80d0ecb12) · [缺口 G-b795364aa7c83513](../../evidence/gaps-sets-006.md#g-b795364aa7c83513) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-043932

```text
(config)# do-exec set memory debug incremental starting-time <cr>
```

Handler ` RVA 0xE08DB90 `；selector ` 0 `；EOL ` RVA 0x341E7B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2929b8a3861e6914](../../evidence/conditions-sets-016.md#c-2929b8a3861e6914) · [状态效果 S-f6419f16ddc3cf9e](../../evidence/state_effects-sets-052.md#s-f6419f16ddc3cf9e)

### path-025643

```text
(config)# do-exec setup <cr>
```

Handler ` RVA 0xE006400 `；selector ` 0 `；EOL ` RVA 0x341657D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-53911967820a073d](../../evidence/conditions-sets-033.md#c-53911967820a073d) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-061207

```text
(config)# do-exec shell environment load <url:dynamic> merge <cr>
```

Handler ` RVA 0xDF794B0 `；selector ` 0 `；EOL ` RVA 0x340B9478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7f04bc0f089a03fa](../../evidence/conditions-sets-049.md#c-7f04bc0f089a03fa) · [缺口 G-ff22c90e8cfd72c0](../../evidence/gaps-sets-009.md#g-ff22c90e8cfd72c0) · [参数 P-32ee07971d829bee](../../evidence/parameters-sets-004.md#p-32ee07971d829bee) · [状态效果 S-978d99fbd3242df2](../../evidence/state_effects-sets-032.md#s-978d99fbd3242df2)

### path-060754

```text
(config)# do-exec shell environment save <url:dynamic> <cr>
```

Handler ` RVA 0xDF79D90 `；selector ` 0 `；EOL ` RVA 0x340B9148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cc5457c27c769651](../../evidence/conditions-sets-079.md#c-cc5457c27c769651) · [缺口 G-15dc29355a4b3ec2](../../evidence/gaps-sets-001.md#g-15dc29355a4b3ec2) · [参数 P-4b1c324a2a2ecd05](../../evidence/parameters-sets-006.md#p-4b1c324a2a2ecd05) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-025574

```text
(config)# do-exec show <cr>
```

Handler ` RVA 0xE006240 `；selector ` 0 `；EOL ` RVA 0x34123660 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd4d3448e3cd0877](../../evidence/conditions-sets-079.md#c-cd4d3448e3cd0877) · [状态效果 S-433297f154b97a7a](../../evidence/state_effects-sets-015.md#s-433297f154b97a7a)

### path-062729

```text
(config)# do-exec show <url:dynamic> <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 3 `；EOL ` RVA 0x33EC1888 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-70948ea6f4cdbcac](../../evidence/conditions-sets-044.md#c-70948ea6f4cdbcac) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062768

```text
(config)# do-exec show <url:dynamic> all <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 1 `；EOL ` RVA 0x33EC0CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-3c94a183d9482661](../../evidence/conditions-sets-024.md#c-3c94a183d9482661) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062771

```text
(config)# do-exec show <url:dynamic> chips <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 2 `；EOL ` RVA 0x33EC15D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-414279ac1bd0228b](../../evidence/conditions-sets-026.md#c-414279ac1bd0228b) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062770

```text
(config)# do-exec show <url:dynamic> detailed <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 4 `；EOL ` RVA 0x33EC12D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-9f6b045539abdbc1](../../evidence/conditions-sets-062.md#c-9f6b045539abdbc1) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062769

```text
(config)# do-exec show <url:dynamic> err <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 5 `；EOL ` RVA 0x33EC0FE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-687148dc9b247525](../../evidence/conditions-sets-040.md#c-687148dc9b247525) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062772

```text
(config)# do-exec show <url:dynamic> filesys <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 6 `；EOL ` RVA 0x33EC18C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-0b430342590263a4](../../evidence/conditions-sets-005.md#c-0b430342590263a4) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062767

```text
(config)# do-exec show <url:dynamic> namesort <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 9 `；EOL ` RVA 0x33EC09F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-0581d5a969d26f5e](../../evidence/conditions-sets-003.md#c-0581d5a969d26f5e) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062764

```text
(config)# do-exec show <url:dynamic> sizesort <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 11 `；EOL ` RVA 0x33EC0400 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-9f35bea95e9eab8f](../../evidence/conditions-sets-062.md#c-9f35bea95e9eab8f) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062765

```text
(config)# do-exec show <url:dynamic> summary <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 7 `；EOL ` RVA 0x33EC0108 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-87781c6354fef4d0](../../evidence/conditions-sets-052.md#c-87781c6354fef4d0) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-062766

```text
(config)# do-exec show <url:dynamic> timesort <cr>
```

Handler ` RVA 0xD65F5E0 `；selector ` 10 `；EOL ` RVA 0x33EC06F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` url_dynamic ` display information about %s file system。

[条件 C-8e44ad32eb8c830e](../../evidence/conditions-sets-055.md#c-8e44ad32eb8c830e) · [缺口 G-93cd64d04639a41b](../../evidence/gaps-sets-005.md#g-93cd64d04639a41b) · [参数 P-a402fd26c08737b0](../../evidence/parameters-sets-012.md#p-a402fd26c08737b0) · [状态效果 S-f08acb41a0c0a222](../../evidence/state_effects-sets-051.md#s-f08acb41a0c0a222)

### path-033584

```text
(config)# do-exec show aaa acct-stop-cache <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 22 `；EOL ` RVA 0x34049A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-6bfa3ebe589dede1](../../evidence/state_effects-sets-023.md#s-6bfa3ebe589dede1)

### path-033430

```text
(config)# do-exec show aaa attributes <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 1 `；EOL ` RVA 0x34046A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051372

```text
(config)# do-exec show aaa cache filterserver acl <cr>
```

Handler ` RVA 0xCD2A340 `；selector ` 0 `；EOL ` RVA 0x34045CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce9ab917f0bc63ef](../../evidence/conditions-sets-080.md#c-ce9ab917f0bc63ef) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051393

```text
(config)# do-exec show aaa cache filterserver pending <cr>
```

Handler ` RVA 0xCD2A2F0 `；selector ` 0 `；EOL ` RVA 0x34045F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ce9ab917f0bc63ef](../../evidence/conditions-sets-080.md#c-ce9ab917f0bc63ef) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056557

```text
(config)# do-exec show aaa cache group <string> all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 13 `；EOL ` RVA 0x340462F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AAA SG Cache。

[条件 C-ce9ab917f0bc63ef](../../evidence/conditions-sets-080.md#c-ce9ab917f0bc63ef) · [参数 P-3dca316610ef6909](../../evidence/parameters-sets-005.md#p-3dca316610ef6909) · [状态效果 S-77581ae1377f846a](../../evidence/state_effects-sets-025.md#s-77581ae1377f846a)

### path-033507

```text
(config)# do-exec show aaa clients <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 10 `；EOL ` RVA 0x34048400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043092

```text
(config)# do-exec show aaa command handler <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 11 `；EOL ` RVA 0x34048708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051423

```text
(config)# do-exec show aaa common-criteria policy all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 23 `；EOL ` RVA 0x34046718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a1bdbb74d45f98c](../../evidence/conditions-sets-035.md#c-5a1bdbb74d45f98c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033380

```text
(config)# do-exec show aaa counters <cr>
```

Handler ` RVA 0xDD43740 `；selector ` 0 `；EOL ` RVA 0x340455E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051624

```text
(config)# do-exec show aaa dead-criteria radius <address> <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 18 `；EOL ` RVA 0x34047E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of the server。

[条件 C-1de3d9df4fc4acb6](../../evidence/conditions-sets-012.md#c-1de3d9df4fc4acb6) · [参数 P-78e08a15bf119a7a](../../evidence/parameters-sets-009.md#p-78e08a15bf119a7a) · [状态效果 S-eefcc9b5e1675c8f](../../evidence/state_effects-sets-051.md#s-eefcc9b5e1675c8f)

### path-033664

```text
(config)# do-exec show aaa fqdn <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 26 `；EOL ` RVA 0x3404A668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d37179533b37c123](../../evidence/conditions-sets-082.md#c-d37179533b37c123) · [状态效果 S-1d2acf7c3166eca5](../../evidence/state_effects-sets-007.md#s-1d2acf7c3166eca5)

### path-033475

```text
(config)# do-exec show aaa hash <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 4 `；EOL ` RVA 0x340477F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033343

```text
(config)# do-exec show aaa idmgr <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 20 `；EOL ` RVA 0x340452D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056639

```text
(config)# do-exec show aaa ipv6 tacacs source-interface global <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 27 `；EOL ` RVA 0x3404AB08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-52cf840d106be0c6](../../evidence/state_effects-sets-018.md#s-52cf840d106be0c6)

### path-051390

```text
(config)# do-exec show aaa local admin_user all <cr>
```

Handler ` RVA 0xDDDD5F0 `；selector ` 0 `；EOL ` RVA 0x33E70E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-510cdccc6fb71311](../../evidence/conditions-sets-032.md#c-510cdccc6fb71311) · [状态效果 S-650e3dae60f1366b](../../evidence/state_effects-sets-022.md#s-650e3dae60f1366b)

### path-042853

```text
(config)# do-exec show aaa local statistics <cr>
```

Handler ` RVA 0xD5070E0 `；selector ` 0 `；EOL ` RVA 0x33E70AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051378

```text
(config)# do-exec show aaa local user blocked <cr>
```

Handler ` RVA 0xD505370 `；selector ` 6 `；EOL ` RVA 0x33E70818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-502313fa57050bd0](../../evidence/conditions-sets-031.md#c-502313fa57050bd0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051338

```text
(config)# do-exec show aaa local user lockout <cr>
```

Handler ` RVA 0xD505370 `；selector ` 2 `；EOL ` RVA 0x33E70530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033628

```text
(config)# do-exec show aaa memory <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 19 `；EOL ` RVA 0x34049E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-5050de57831d2416](../../evidence/state_effects-sets-018.md#s-5050de57831d2416)

### path-051682

```text
(config)# do-exec show aaa memory stats all <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 21 `；EOL ` RVA 0x3404A148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-f18b04a0f81392d5](../../evidence/state_effects-sets-051.md#s-f18b04a0f81392d5)

### path-042930

```text
(config)# do-exec show aaa method-lists authentication <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 2 `；EOL ` RVA 0x34046D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-439db28f247fc425](../../evidence/state_effects-sets-015.md#s-439db28f247fc425)

### path-042976

```text
(config)# do-exec show aaa requests statistics <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 24 `；EOL ` RVA 0x34047500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033543

```text
(config)# do-exec show aaa server-private <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 9 `；EOL ` RVA 0x34048E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-6bfa3ebe589dede1](../../evidence/state_effects-sets-023.md#s-6bfa3ebe589dede1)

### path-033566

```text
(config)# do-exec show aaa servers <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 8 `；EOL ` RVA 0x34048AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-60cb343e2aa43335](../../evidence/state_effects-sets-021.md#s-60cb343e2aa43335)

### path-033575

```text
(config)# do-exec show aaa service-profiles <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 6 `；EOL ` RVA 0x34049798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-6bfa3ebe589dede1](../../evidence/state_effects-sets-023.md#s-6bfa3ebe589dede1)

### path-033552

```text
(config)# do-exec show aaa sessions <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 5 `；EOL ` RVA 0x340490D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-6bfa3ebe589dede1](../../evidence/state_effects-sets-023.md#s-6bfa3ebe589dede1)

### path-043223

```text
(config)# do-exec show aaa sp-cache all-list <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 7 `；EOL ` RVA 0x34049458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-77b2f2adcf84cb0f](../../evidence/state_effects-sets-025.md#s-77b2f2adcf84cb0f)

### path-042908

```text
(config)# do-exec show aaa subscriber profile <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 14 `；EOL ` RVA 0x34045958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7ebb0b463d465ec](../../evidence/conditions-sets-071.md#c-b7ebb0b463d465ec) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-051359

```text
(config)# do-exec show aaa tools memleak statistics <cr>
```

Handler ` RVA 0x1371D720 `；selector ` 0 `；EOL ` RVA 0x35C0D690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-faa516ddea04f10f](../../evidence/state_effects-sets-053.md#s-faa516ddea04f10f)

### path-033472

```text
(config)# do-exec show aaa tracebacks <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 12 `；EOL ` RVA 0x34047A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042951

```text
(config)# do-exec show aaa user <number:1..4294967295> <cr>
```

Handler ` RVA 0xDD6BF10 `；selector ` 3 `；EOL ` RVA 0x340471B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Unique Id for a single user。

[条件 C-5183ce2eae66230b](../../evidence/conditions-sets-032.md#c-5183ce2eae66230b) · [参数 P-1b01084d2bf088cf](../../evidence/parameters-sets-003.md#p-1b01084d2bf088cf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027763

```text
(config)# do-exec show access-expression <cr>
```

Handler ` RVA 0x1E3FDC10 `；selector ` 0 `；EOL ` RVA 0x345E8370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-755f3c0916a9e689](../../evidence/conditions-sets-046.md#c-755f3c0916a9e689) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026791

```text
(config)# do-exec show access-lists <cr>
```

Handler ` RVA 0xE0AE9A0 `；selector ` 0 `；EOL ` RVA 0x34185F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0855b1d6143262fb](../../evidence/conditions-sets-004.md#c-0855b1d6143262fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029107

```text
(config)# do-exec show access-lists acl-limit <cr>
```

Handler ` RVA 0xE0AEF10 `；selector ` 0 `；EOL ` RVA 0x34CEF048 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035182

```text
(config)# do-exec show access-lists fqdn client <cr>
```

Handler ` RVA 0xCF22230 `；selector ` 0 `；EOL ` RVA 0x33D65A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2fad42d2895fb792](../../evidence/state_effects-sets-011.md#s-2fad42d2895fb792)

### path-035100

```text
(config)# do-exec show access-lists fqdn pending-mappings <cr>
```

Handler ` RVA 0xCF24260 `；selector ` 0 `；EOL ` RVA 0x33D65CC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2fad42d2895fb792](../../evidence/state_effects-sets-011.md#s-2fad42d2895fb792)

### path-035224

```text
(config)# do-exec show access-lists fqdn statistics <cr>
```

Handler ` RVA 0xCF1BE90 `；selector ` 0 `；EOL ` RVA 0x33D65FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2fad42d2895fb792](../../evidence/state_effects-sets-011.md#s-2fad42d2895fb792)

### path-028927

```text
(config)# do-exec show access-lists ipc <cr>
```

Handler ` RVA 0xCF05960 `；selector ` 0 `；EOL ` RVA 0x33D63E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029116

```text
(config)# do-exec show access-lists rate-limit <cr>
```

Handler ` RVA 0x10C68E60 `；selector ` 0 `；EOL ` RVA 0x34CEED88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035202

```text
(config)# do-exec show access-lists template summary <cr>
```

Handler ` RVA 0xEBB9030 `；selector ` 0 `；EOL ` RVA 0x343D13B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3464939f8c60a665](../../evidence/conditions-sets-020.md#c-3464939f8c60a665) · [状态效果 S-9fef273e89bfc6b8](../../evidence/state_effects-sets-034.md#s-9fef273e89bfc6b8)

### path-049968

```text
(config)# do-exec show access-session limit profile details <cr>
```

Handler ` RVA 0xCAD3890 `；selector ` 0 `；EOL ` RVA 0x33B961C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4ee3d35e56eaffb9](../../evidence/conditions-sets-031.md#c-4ee3d35e56eaffb9) · [状态效果 S-cb9d1f588cb84c4c](../../evidence/state_effects-sets-043.md#s-cb9d1f588cb84c4c)

### path-032612

```text
(config)# do-exec show accounting group <cr>
```

Handler ` RVA 0x10D141B0 `；selector ` 1 `；EOL ` RVA 0x34D10A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041463

```text
(config)# do-exec show accounting group <string> <cr>
```

Handler ` RVA 0x10D141B0 `；selector ` 2 `；EOL ` RVA 0x34D10A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Group name。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [参数 P-0cff7b130b46abb3](../../evidence/parameters-sets-001.md#p-0cff7b130b46abb3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032637

```text
(config)# do-exec show accounting session <cr>
```

Handler ` RVA 0x10D15B60 `；selector ` 3 `；EOL ` RVA 0x34D10F88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041506

```text
(config)# do-exec show accounting session <number:1..100000> <cr>
```

Handler ` RVA 0x10D15B60 `；selector ` 4 `；EOL ` RVA 0x34D10F60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session id。

[条件 C-248ad275e30c5896](../../evidence/conditions-sets-014.md#c-248ad275e30c5896) · [参数 P-fe468869032ecf3b](../../evidence/parameters-sets-019.md#p-fe468869032ecf3b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028648

```text
(config)# do-exec show acm rules <cr>
```

Handler ` RVA 0xDECF5D0 `；selector ` 0 `；EOL ` RVA 0x340C69D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027482

```text
(config)# do-exec show adjacency <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 1 `；EOL ` RVA 0x3379D448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-48322428610b04c9](../../evidence/conditions-sets-028.md#c-48322428610b04c9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060684

```text
(config)# do-exec show adjacency <interface> <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 1 `；EOL ` RVA 0x3379D448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a165c3c86da66a9a](../../evidence/conditions-sets-062.md#c-a165c3c86da66a9a) · [缺口 G-48a0ab98d2e722ef](../../evidence/gaps-sets-003.md#g-48a0ab98d2e722ef) · [参数 P-a56945f1b8c7445e](../../evidence/parameters-sets-013.md#p-a56945f1b8c7445e) · [状态效果 S-4e20d24d1d3d72a4](../../evidence/state_effects-sets-017.md#s-4e20d24d1d3d72a4)

### path-030620

```text
(config)# do-exec show adjacency connid-mgr <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 2 `；EOL ` RVA 0x3379C200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030701

```text
(config)# do-exec show adjacency summary <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 0 `；EOL ` RVA 0x3379C5F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7f655aa64276ff61](../../evidence/conditions-sets-049.md#c-7f655aa64276ff61) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060920

```text
(config)# do-exec show adjacency summary <interface> <cr>
```

Handler ` RVA 0xB5711C0 `；selector ` 0 `；EOL ` RVA 0x3379C5F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b3fef00b316ba02](../../evidence/conditions-sets-005.md#c-0b3fef00b316ba02) · [缺口 G-51e76149eec81a09](../../evidence/gaps-sets-003.md#g-51e76149eec81a09) · [参数 P-991145414d0888ba](../../evidence/parameters-sets-012.md#p-991145414d0888ba) · [状态效果 S-dbed8070bb143f17](../../evidence/state_effects-sets-047.md#s-dbed8070bb143f17)

### path-030855

```text
(config)# do-exec show alg sip <cr>
```

Handler ` RVA 0xCD3D500 `；selector ` 0 `；EOL ` RVA 0x33CD4600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060540

```text
(config)# do-exec show aliases <?mode_action@5555896193e0> <cr>
```

Handler ` RVA 0xDF00610 `；selector ` 0 `；EOL ` RVA 0x340C5420 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [缺口 G-12902ea0b090e399](../../evidence/gaps-sets-001.md#g-12902ea0b090e399) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027011

```text
(config)# do-exec show alignment <cr>
```

Handler ` RVA 0xE8F39E0 `；selector ` 0 `；EOL ` RVA 0x3433E688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033761

```text
(config)# do-exec show alps ascu <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 2 `；EOL ` RVA 0x3541B4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-881910bb7a44a5a4](../../evidence/conditions-sets-053.md#c-881910bb7a44a5a4) · [状态效果 S-bc085098764e1452](../../evidence/state_effects-sets-040.md#s-bc085098764e1452)

### path-061189

```text
(config)# do-exec show alps ascu <interface> <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 2 `；EOL ` RVA 0x3541B4D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8cf66d6232077bde](../../evidence/conditions-sets-055.md#c-8cf66d6232077bde) · [缺口 G-2116775fe6d76afb](../../evidence/gaps-sets-002.md#g-2116775fe6d76afb) · [参数 P-e8b81f7d0e6d6789](../../evidence/parameters-sets-017.md#p-e8b81f7d0e6d6789) · [状态效果 S-bc085098764e1452](../../evidence/state_effects-sets-040.md#s-bc085098764e1452)

### path-033727

```text
(config)# do-exec show alps circuits <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 1 `；EOL ` RVA 0x3541B060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033705

```text
(config)# do-exec show alps peers <cr>
```

Handler ` RVA 0x112143F0 `；selector ` 0 `；EOL ` RVA 0x3541AC50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061431

```text
(config)# do-exec show ancp an-port interface <interface> <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 8 `；EOL ` RVA 0x336DA170 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-78a425855c4b5ce9](../../evidence/conditions-sets-047.md#c-78a425855c4b5ce9) · [缺口 G-343e5161ee73bb7d](../../evidence/gaps-sets-002.md#g-343e5161ee73bb7d) · [参数 P-f6f09b567c47457e](../../evidence/parameters-sets-018.md#p-f6f09b567c47457e) · [状态效果 S-19e887c9039709d5](../../evidence/state_effects-sets-006.md#s-19e887c9039709d5)

### path-037498

```text
(config)# do-exec show ancp an-port summary <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 8 `；EOL ` RVA 0x336DA170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-84e74642a87e20c7](../../evidence/state_effects-sets-028.md#s-84e74642a87e20c7)

### path-030804

```text
(config)# do-exec show ancp neighbor <cr>
```

Handler ` RVA 0xB26EF90 `；selector ` 7 `；EOL ` RVA 0x336D8FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-9903a027146c1ce8](../../evidence/state_effects-sets-033.md#s-9903a027146c1ce8)

### path-037349

```text
(config)# do-exec show ancp neighbor brief <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 1 `；EOL ` RVA 0x336D8B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-463bfb692d9669e3](../../evidence/state_effects-sets-015.md#s-463bfb692d9669e3)

### path-030705

```text
(config)# do-exec show ancp port <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 3 `；EOL ` RVA 0x336D86D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a602d1be8f2a9bab](../../evidence/conditions-sets-064.md#c-a602d1be8f2a9bab) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030704

```text
(config)# do-exec show ancp session <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 4 `；EOL ` RVA 0x336D9690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061988

```text
(config)# do-exec show ancp session adjacency name <hex-string> <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 4 `；EOL ` RVA 0x336D9690 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Neighbor's MAC。

[条件 C-9dce4566ec9a99c0](../../evidence/conditions-sets-061.md#c-9dce4566ec9a99c0) · [缺口 G-3ecc7b1531ecd0df](../../evidence/gaps-sets-003.md#g-3ecc7b1531ecd0df) · [参数 P-1bd018bfd47b95bc](../../evidence/parameters-sets-003.md#p-1bd018bfd47b95bc) · [状态效果 S-94bdf8cedb85bd24](../../evidence/state_effects-sets-032.md#s-94bdf8cedb85bd24)

### path-030653

```text
(config)# do-exec show ancp statistics <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 5 `；EOL ` RVA 0x336D9A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030731

```text
(config)# do-exec show ancp status <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 6 `；EOL ` RVA 0x336D9DF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8968d7fbd30f19b7](../../evidence/conditions-sets-053.md#c-8968d7fbd30f19b7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060918

```text
(config)# do-exec show ancp status <interface> <cr>
```

Handler ` RVA 0xB263FA0 `；selector ` 6 `；EOL ` RVA 0x336D9DF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-18d7f540ea849a34](../../evidence/conditions-sets-010.md#c-18d7f540ea849a34) · [缺口 G-be530c0ed6f8bf54](../../evidence/gaps-sets-007.md#g-be530c0ed6f8bf54) · [参数 P-a3100cdf2d598c80](../../evidence/parameters-sets-012.md#p-a3100cdf2d598c80) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061132

```text
(config)# do-exec show application * route <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 5 `；EOL ` RVA 0x358DAC38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a19849a99b0040a3](../../evidence/conditions-sets-062.md#c-a19849a99b0040a3) · [缺口 G-1f373e157b60a0c5](../../evidence/gaps-sets-002.md#g-1f373e157b60a0c5) · [状态效果 S-f21d3063edb2cb7e](../../evidence/state_effects-sets-051.md#s-f21d3063edb2cb7e)

### path-062448

```text
(config)# do-exec show application * route application <string> summary <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 2 `；EOL ` RVA 0x358DA6C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Application name。

[条件 C-1081a624a857020a](../../evidence/conditions-sets-007.md#c-1081a624a857020a) · [缺口 G-1f373e157b60a0c5](../../evidence/gaps-sets-002.md#g-1f373e157b60a0c5) · [参数 P-a7b5cfc24129c4ef](../../evidence/parameters-sets-013.md#p-a7b5cfc24129c4ef) · [状态效果 S-f21d3063edb2cb7e](../../evidence/state_effects-sets-051.md#s-f21d3063edb2cb7e)

### path-041988

```text
(config)# do-exec show application ha statistics <cr>
```

Handler ` RVA 0x12802A90 `；selector ` 0 `；EOL ` RVA 0x358D9A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1bccf2487d5955e5](../../evidence/conditions-sets-011.md#c-1bccf2487d5955e5) · [状态效果 S-e1469525a42ea475](../../evidence/state_effects-sets-048.md#s-e1469525a42ea475)

### path-042059

```text
(config)# do-exec show application ip route <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 5 `；EOL ` RVA 0x358DAC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7a4815c79326b1a6](../../evidence/conditions-sets-047.md#c-7a4815c79326b1a6) · [状态效果 S-7096b690c25ee43f](../../evidence/state_effects-sets-024.md#s-7096b690c25ee43f)

### path-061748

```text
(config)# do-exec show application ip route <prefix:dynamic> <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 3 `；EOL ` RVA 0x358DA990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-2e732c8de607f55f](../../evidence/conditions-sets-018.md#c-2e732c8de607f55f) · [缺口 G-46a902d8d7154767](../../evidence/gaps-sets-003.md#g-46a902d8d7154767) · [参数 P-fabff58a3e5a98f1](../../evidence/parameters-sets-019.md#p-fabff58a3e5a98f1) · [状态效果 S-7096b690c25ee43f](../../evidence/state_effects-sets-024.md#s-7096b690c25ee43f)

### path-058731

```text
(config)# do-exec show application ip route application <string> summary <cr>
```

Handler ` RVA 0x1280F550 `；selector ` 2 `；EOL ` RVA 0x358DA6C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Application name。

[条件 C-680144e3598ff1f5](../../evidence/conditions-sets-040.md#c-680144e3598ff1f5) · [参数 P-a7b5cfc24129c4ef](../../evidence/parameters-sets-013.md#p-a7b5cfc24129c4ef) · [状态效果 S-7096b690c25ee43f](../../evidence/state_effects-sets-024.md#s-7096b690c25ee43f)

### path-032759

```text
(config)# do-exec show application summary <cr>
```

Handler ` RVA 0x1280F4C0 `；selector ` 0 `；EOL ` RVA 0x358DA110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027749

```text
(config)# do-exec show archive <cr>
```

Handler ` RVA 0xDECC9F0 `；selector ` 0 `；EOL ` RVA 0x3409C008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-042994

```text
(config)# do-exec show archive config differences <cr>
```

Handler ` RVA 0xDFDC970 `；selector ` 0 `；EOL ` RVA 0x340CD168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-885ca7908e011d51](../../evidence/state_effects-sets-029.md#s-885ca7908e011d51)

### path-061783

```text
(config)# do-exec show archive config differences <url:dynamic> <cr>
```

Handler ` RVA 0xDFDC970 `；selector ` 0 `；EOL ` RVA 0x340CD168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6772e9f9f48c6e38](../../evidence/conditions-sets-040.md#c-6772e9f9f48c6e38) · [缺口 G-2ec270c6b5c95c86](../../evidence/gaps-sets-002.md#g-2ec270c6b5c95c86) · [参数 P-0e4cbc00b7b4f48f](../../evidence/parameters-sets-002.md#p-0e4cbc00b7b4f48f) · [状态效果 S-885ca7908e011d51](../../evidence/state_effects-sets-029.md#s-885ca7908e011d51)

### path-061784

```text
(config)# do-exec show archive config incremental-diffs <url:dynamic> <cr>
```

Handler ` RVA 0xDFDC970 `；selector ` 0 `；EOL ` RVA 0x340CD588 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-11b996df50fa2eea](../../evidence/conditions-sets-007.md#c-11b996df50fa2eea) · [缺口 G-4ba8ce1b158c6505](../../evidence/gaps-sets-003.md#g-4ba8ce1b158c6505) · [参数 P-9cbb71193e4b63d4](../../evidence/parameters-sets-012.md#p-9cbb71193e4b63d4) · [状态效果 S-66592e1573792c82](../../evidence/state_effects-sets-022.md#s-66592e1573792c82)

### path-062219

```text
(config)# do-exec show archive config rollback commands <url:dynamic> <cr>
```

Handler ` RVA 0xDFDC970 `；selector ` 0 `；EOL ` RVA 0x340CDBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d7c283ce400ed5ae](../../evidence/conditions-sets-083.md#c-d7c283ce400ed5ae) · [缺口 G-7ac612fb00636f93](../../evidence/gaps-sets-005.md#g-7ac612fb00636f93) · [参数 P-b33158af91d8d479](../../evidence/parameters-sets-014.md#p-b33158af91d8d479) · [状态效果 S-1b045efac4ed1878](../../evidence/state_effects-sets-006.md#s-1b045efac4ed1878)

### path-051459

```text
(config)# do-exec show archive config rollback timer <cr>
```

Handler ` RVA 0xDFDCFE0 `；selector ` 0 `；EOL ` RVA 0x340CD868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056576

```text
(config)# do-exec show archive log config all persistent <cr>
```

Handler ` RVA 0xDF14700 `；selector ` 0 `；EOL ` RVA 0x340A2B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6497dbd8c00ea1c2](../../evidence/state_effects-sets-022.md#s-6497dbd8c00ea1c2)

### path-051432

```text
(config)# do-exec show archive log config statistics <cr>
```

Handler ` RVA 0xDF0B2B0 `；selector ` 0 `；EOL ` RVA 0x340A27D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-ba141a30cbdb6998](../../evidence/state_effects-sets-039.md#s-ba141a30cbdb6998)

### path-027576

```text
(config)# do-exec show arp <cr>
```

Handler ` RVA 0xCD4CF60 `；selector ` 0 `；EOL ` RVA 0x33D29978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-650a0de43e577f20](../../evidence/conditions-sets-039.md#c-650a0de43e577f20) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060705

```text
(config)# do-exec show arp <interface> <cr>
```

Handler ` RVA 0xCD4CF60 `；selector ` 0 `；EOL ` RVA 0x33D29978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b2cc9ca406960aac](../../evidence/conditions-sets-069.md#c-b2cc9ca406960aac) · [缺口 G-42e0c982bbf87824](../../evidence/gaps-sets-003.md#g-42e0c982bbf87824) · [参数 P-95540b0c015a2a06](../../evidence/parameters-sets-011.md#p-95540b0c015a2a06) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027812

```text
(config)# do-exec show asp <cr>
```

Handler ` RVA 0x113A1300 `；selector ` 0 `；EOL ` RVA 0x354A39B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032470

```text
(config)# do-exec show async bootp <cr>
```

Handler ` RVA 0xD3448C0 `；selector ` 0 `；EOL ` RVA 0x349343F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032488

```text
(config)# do-exec show async status <cr>
```

Handler ` RVA 0xFF3FE50 `；selector ` 0 `；EOL ` RVA 0x349346A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-034159

```text
(config)# do-exec show auto install status <cr>
```

Handler ` RVA 0xFFA8E70 `；selector ` 0 `；EOL ` RVA 0x349433F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-034196

```text
(config)# do-exec show auto install tech-support <cr>
```

Handler ` RVA 0xFFAE9B0 `；selector ` 0 `；EOL ` RVA 0x34943698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-034224

```text
(config)# do-exec show auto install trace <cr>
```

Handler ` RVA 0xFFAE910 `；selector ` 0 `；EOL ` RVA 0x34943940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-034135

```text
(config)# do-exec show auto secure config <cr>
```

Handler ` RVA 0xB246B10 `；selector ` 0 `；EOL ` RVA 0x336D4EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0e45fc452402454](../../evidence/conditions-sets-093.md#c-f0e45fc452402454) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032846

```text
(config)# do-exec show autoip status <cr>
```

Handler ` RVA 0xB286210 `；selector ` 0 `；EOL ` RVA 0x3372CA58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041881

```text
(config)# do-exec show autoip status detail <cr>
```

Handler ` RVA 0xB286260 `；selector ` 0 `；EOL ` RVA 0x3372CA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027634

```text
(config)# do-exec show avc <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 89 `；EOL ` RVA 0x35254938 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f267040d57d4ceb6](../../evidence/conditions-sets-094.md#c-f267040d57d4ceb6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049758

```text
(config)# do-exec show avc sd-service info cmds <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 87 `；EOL ` RVA 0x3524EA68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055625

```text
(config)# do-exec show avc sd-service info cmds config <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 86 `；EOL ` RVA 0x3524EA40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055596

```text
(config)# do-exec show avc sd-service info cmds status <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 88 `；EOL ` RVA 0x3524E798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049704

```text
(config)# do-exec show avc sd-service info detailed <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 61 `；EOL ` RVA 0x3524EF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-a34e9eaa6d2deeca](../../evidence/state_effects-sets-035.md#s-a34e9eaa6d2deeca)

### path-050087

```text
(config)# do-exec show avc sd-service info ent <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 66 `；EOL ` RVA 0x35253A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055774

```text
(config)# do-exec show avc sd-service info ent config <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 72 `；EOL ` RVA 0x35252720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058627

```text
(config)# do-exec show avc sd-service info ent device-health db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 75 `；EOL ` RVA 0x35253FF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059543

```text
(config)# do-exec show avc sd-service info ent device-health export last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 76 `；EOL ` RVA 0x35253D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059538

```text
(config)# do-exec show avc sd-service info ent device-health export stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 77 `；EOL ` RVA 0x35253AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058637

```text
(config)# do-exec show avc sd-service info ent device-health interfaces <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 74 `；EOL ` RVA 0x35254298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055903

```text
(config)# do-exec show avc sd-service info ent export <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 70 `；EOL ` RVA 0x352534F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058607

```text
(config)# do-exec show avc sd-service info ent export current <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 68 `；EOL ` RVA 0x35252F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058629

```text
(config)# do-exec show avc sd-service info ent export keys-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 73 `；EOL ` RVA 0x352534D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e75e7c5f49467991](../../evidence/conditions-sets-089.md#c-e75e7c5f49467991) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058618

```text
(config)# do-exec show avc sd-service info ent export last <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 69 `；EOL ` RVA 0x35253228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055798

```text
(config)# do-exec show avc sd-service info ent fields-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 71 `；EOL ` RVA 0x352529C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-408faba1da1d990a](../../evidence/conditions-sets-025.md#c-408faba1da1d990a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055815

```text
(config)# do-exec show avc sd-service info ent symbol-table <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 67 `；EOL ` RVA 0x35252C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8bde9d2728f9f1a](../../evidence/conditions-sets-077.md#c-c8bde9d2728f9f1a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055761

```text
(config)# do-exec show avc sd-service info export flow-counters <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 63 `；EOL ` RVA 0x35250B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b12b55aa16da627d](../../evidence/conditions-sets-068.md#c-b12b55aa16da627d) · [状态效果 S-a44b14ab1f2b08d3](../../evidence/state_effects-sets-035.md#s-a44b14ab1f2b08d3)

### path-055765

```text
(config)# do-exec show avc sd-service info export l3-cache <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 55 `；EOL ` RVA 0x3524FF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-a44b14ab1f2b08d3](../../evidence/state_effects-sets-035.md#s-a44b14ab1f2b08d3)

### path-062925

```text
(config)# do-exec show avc sd-service info export l3-cache attribute <?option@55558a7a3cf8> <?option@55558a7a3e08> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 55 `；EOL ` RVA 0x3524FF38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ea5af0ac05511eb6](../../evidence/conditions-sets-091.md#c-ea5af0ac05511eb6) · [缺口 G-175308ea9c5e1ef9](../../evidence/gaps-sets-001.md#g-175308ea9c5e1ef9) · [状态效果 S-5d30b0fb372567fe](../../evidence/state_effects-sets-020.md#s-5d30b0fb372567fe)

### path-055748

```text
(config)# do-exec show avc sd-service info export npc-info <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 62 `；EOL ` RVA 0x35250880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a32f3f16c88a2c74](../../evidence/conditions-sets-063.md#c-a32f3f16c88a2c74) · [状态效果 S-a44b14ab1f2b08d3](../../evidence/state_effects-sets-035.md#s-a44b14ab1f2b08d3)

### path-055811

```text
(config)# do-exec show avc sd-service info export socket-cache <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 56 `；EOL ` RVA 0x352505A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-a44b14ab1f2b08d3](../../evidence/state_effects-sets-035.md#s-a44b14ab1f2b08d3)

### path-062926

```text
(config)# do-exec show avc sd-service info export socket-cache attribute <?option@55558a7a42c8> <?option@55558a7a43d8> <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 56 `；EOL ` RVA 0x352505A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b1eaf463a714f2b](../../evidence/conditions-sets-048.md#c-7b1eaf463a714f2b) · [缺口 G-1b01db7d17474edb](../../evidence/gaps-sets-001.md#g-1b01db7d17474edb) · [状态效果 S-04fdfb435ae6caa2](../../evidence/state_effects-sets-002.md#s-04fdfb435ae6caa2)

### path-055738

```text
(config)# do-exec show avc sd-service info import dump <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F6D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-05b402105ed2f0d2](../../evidence/state_effects-sets-002.md#s-05b402105ed2f0d2)

### path-058528

```text
(config)# do-exec show avc sd-service info import dump l3-rules <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F3F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-d5778709b49defed](../../evidence/state_effects-sets-045.md#s-d5778709b49defed)

### path-058535

```text
(config)# do-exec show avc sd-service info import dump l4-rules <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 57 `；EOL ` RVA 0x3524F6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f44551935f70224](../../evidence/conditions-sets-006.md#c-0f44551935f70224) · [状态效果 S-8232fc9221afaf0c](../../evidence/state_effects-sets-028.md#s-8232fc9221afaf0c)

### path-055781

```text
(config)# do-exec show avc sd-service info tls-fp clear-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 85 `；EOL ` RVA 0x35251648 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a281251bbcdf2caf](../../evidence/conditions-sets-063.md#c-a281251bbcdf2caf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055834

```text
(config)# do-exec show avc sd-service info tls-fp clear-stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 82 `；EOL ` RVA 0x352523F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57e0a4ed47b4aa96](../../evidence/conditions-sets-034.md#c-57e0a4ed47b4aa96) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055785

```text
(config)# do-exec show avc sd-service info tls-fp dump-db <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 83 `；EOL ` RVA 0x35251178 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-08f104f9e5675f7a](../../evidence/conditions-sets-004.md#c-08f104f9e5675f7a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058558

```text
(config)# do-exec show avc sd-service info tls-fp dump-db detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 84 `；EOL ` RVA 0x35251150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a19795555946921](../../evidence/conditions-sets-016.md#c-2a19795555946921) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058623

```text
(config)# do-exec show avc sd-service info tls-fp fingerprint-db dump <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 80 `；EOL ` RVA 0x35251F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9f5a3c9b6d75e25f](../../evidence/conditions-sets-062.md#c-9f5a3c9b6d75e25f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-059534

```text
(config)# do-exec show avc sd-service info tls-fp fingerprint-db dump detail <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 81 `；EOL ` RVA 0x35251EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dad1ba29aa9615e1](../../evidence/conditions-sets-084.md#c-dad1ba29aa9615e1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058596

```text
(config)# do-exec show avc sd-service info tls-fp fingerprint-db info <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 79 `；EOL ` RVA 0x35251C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-818143645fa9c448](../../evidence/conditions-sets-050.md#c-818143645fa9c448) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055801

```text
(config)# do-exec show avc sd-service info tls-fp show-stats <cr>
```

Handler ` RVA 0x10F36700 `；selector ` 78 `；EOL ` RVA 0x352518F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6d0955a494ab5957](../../evidence/conditions-sets-042.md#c-6d0955a494ab5957) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027047

```text
(config)# do-exec show backup <cr>
```

Handler ` RVA 0xEF363F0 `；selector ` 0 `；EOL ` RVA 0x34483370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028573

```text
(config)# do-exec show banner login <cr>
```

Handler ` RVA 0xDEFB260 `；selector ` 0 `；EOL ` RVA 0x340C5CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-7644968657c516e2](../../evidence/state_effects-sets-025.md#s-7644968657c516e2)

### path-032978

```text
(config)# do-exec show beep blocked <cr>
```

Handler ` RVA 0xEF60FC0 `；selector ` 1 `；EOL ` RVA 0x3448BFE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-289de11ffdfbb361](../../evidence/conditions-sets-016.md#c-289de11ffdfbb361) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032998

```text
(config)# do-exec show beep session <cr>
```

Handler ` RVA 0xEF60FC0 `；selector ` 3 `；EOL ` RVA 0x3448BD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-289de11ffdfbb361](../../evidence/conditions-sets-016.md#c-289de11ffdfbb361) · [状态效果 S-248d3175ccafbd9a](../../evidence/state_effects-sets-008.md#s-248d3175ccafbd9a)

### path-031624

```text
(config)# do-exec show bfd clients <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 1 `；EOL ` RVA 0x34CB4440 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031638

```text
(config)# do-exec show bfd drops <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 4 `；EOL ` RVA 0x34CB49E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031722

```text
(config)# do-exec show bfd fast-timers-on-slow-int <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 8 `；EOL ` RVA 0x34CB54E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031647

```text
(config)# do-exec show bfd hardware <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 5 `；EOL ` RVA 0x34CB4748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031688

```text
(config)# do-exec show bfd idbs <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 13 `；EOL ` RVA 0x34CB4F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031662

```text
(config)# do-exec show bfd interface <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 2 `；EOL ` RVA 0x34CB4C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031586

```text
(config)# do-exec show bfd internal <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 0 `；EOL ` RVA 0x34CB2A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-8dbabedccf133c24](../../evidence/state_effects-sets-030.md#s-8dbabedccf133c24)

### path-031724

```text
(config)# do-exec show bfd map <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 6 `；EOL ` RVA 0x34CB5248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-061524

```text
(config)# do-exec show bfd neighbors interface <interface> <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 0 `；EOL ` RVA 0x34CB2A90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b64deeae16b94da9](../../evidence/conditions-sets-070.md#c-b64deeae16b94da9) · [缺口 G-8cf6f0fa6ab662fd](../../evidence/gaps-sets-005.md#g-8cf6f0fa6ab662fd) · [参数 P-5690ff51baa75a5b](../../evidence/parameters-sets-007.md#p-5690ff51baa75a5b) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-031575

```text
(config)# do-exec show bfd summary <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 3 `；EOL ` RVA 0x34CB21C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-e4c648c96f794c7a](../../evidence/state_effects-sets-048.md#s-e4c648c96f794c7a)

### path-039613

```text
(config)# do-exec show bfd target-identifier all <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 9 `；EOL ` RVA 0x34CB57D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-039796

```text
(config)# do-exec show bfd target-identifier interface <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 12 `；EOL ` RVA 0x34CB5FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-accf9c8dabd2c0cb](../../evidence/conditions-sets-067.md#c-accf9c8dabd2c0cb) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-039675

```text
(config)# do-exec show bfd target-identifier local <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 10 `；EOL ` RVA 0x34CB5A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-039731

```text
(config)# do-exec show bfd target-identifier remote <cr>
```

Handler ` RVA 0x10B36FE0 `；selector ` 11 `；EOL ` RVA 0x34CB5D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-cd8d107fa4603419](../../evidence/state_effects-sets-044.md#s-cd8d107fa4603419)

### path-060726

```text
(config)# do-exec show bgp * <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 0 `；EOL ` RVA 0x344CA860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fb943e7199ddf331](../../evidence/conditions-sets-097.md#c-fb943e7199ddf331) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-060731

```text
(config)# do-exec show bgp * <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 13 `；EOL ` RVA 0x34500CA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6b0455927b234c8b](../../evidence/conditions-sets-041.md#c-6b0455927b234c8b) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-062426

```text
(config)# do-exec show bgp * all route-type <number:1..7> <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344C8570 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Multicast VPN NLRI route-type；` address ` Route-type 1 originator ID。

[条件 C-74539f6295fac58b](../../evidence/conditions-sets-045.md#c-74539f6295fac58b) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-1b8a4dec5fa285d3](../../evidence/parameters-sets-003.md#p-1b8a4dec5fa285d3) · [状态效果 S-f9da68abd11704e8](../../evidence/state_effects-sets-053.md#s-f9da68abd11704e8)

### path-062428

```text
(config)# do-exec show bgp * all route-type <number:1..7> <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344CB0F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Multicast VPN NLRI route-type；` address ` Route-type 1 originator ID。

[条件 C-13982bb2f381e0d2](../../evidence/conditions-sets-008.md#c-13982bb2f381e0d2) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-fe3de206dc5b3918](../../evidence/parameters-sets-019.md#p-fe3de206dc5b3918) · [状态效果 S-a70218d1fa7d7119](../../evidence/state_effects-sets-035.md#s-a70218d1fa7d7119)

### path-061662

```text
(config)# do-exec show bgp * aspath hash <cr>
```

Handler ` RVA 0xF1723F0 `；selector ` 0 `；EOL ` RVA 0x344BE710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b8a725ecb10e763e](../../evidence/conditions-sets-071.md#c-b8a725ecb10e763e) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061660

```text
(config)# do-exec show bgp * attr hash <cr>
```

Handler ` RVA 0xF1729B0 `；selector ` 0 `；EOL ` RVA 0x344BDC98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad54435c5beb5b98](../../evidence/conditions-sets-067.md#c-ad54435c5beb5b98) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061663

```text
(config)# do-exec show bgp * attr nexthop <cr>
```

Handler ` RVA 0xF172000 `；selector ` 0 `；EOL ` RVA 0x344BDF78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-49e0fea5d939d1ce](../../evidence/conditions-sets-029.md#c-49e0fea5d939d1ce) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061043

```text
(config)# do-exec show bgp * binding-sid <cr>
```

Handler ` RVA 0xF1CFDA0 `；selector ` 0 `；EOL ` RVA 0x344BC410 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0861513cb2690be2](../../evidence/conditions-sets-004.md#c-0861513cb2690be2) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061099

```text
(config)# do-exec show bgp * cidr-only <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 4 `；EOL ` RVA 0x344C25B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c58e04eead694ee3](../../evidence/conditions-sets-076.md#c-c58e04eead694ee3) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061081

```text
(config)# do-exec show bgp * cluster-ids <cr>
```

Handler ` RVA 0xF185F30 `；selector ` 39 `；EOL ` RVA 0x344C0470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-25b88931e3c31370](../../evidence/conditions-sets-015.md#c-25b88931e3c31370) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061672

```text
(config)# do-exec show bgp * cluster-ids internal <cr>
```

Handler ` RVA 0xF185F30 `；selector ` 38 `；EOL ` RVA 0x344C0448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-44d632f3be1dfd16](../../evidence/conditions-sets-027.md#c-44d632f3be1dfd16) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061131

```text
(config)# do-exec show bgp * community <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 7 `；EOL ` RVA 0x34501500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0b751e425da76848](../../evidence/conditions-sets-005.md#c-0b751e425da76848) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061731

```text
(config)# do-exec show bgp * community-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 8 `；EOL ` RVA 0x34501A18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` community-list number。

[条件 C-c2cb134565256770](../../evidence/conditions-sets-075.md#c-c2cb134565256770) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-a5a54df05ee65623](../../evidence/parameters-sets-013.md#p-a5a54df05ee65623) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061087

```text
(config)# do-exec show bgp * dampened-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 12 `；EOL ` RVA 0x344C1470 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-40b2cb21150fb9fa](../../evidence/conditions-sets-025.md#c-40b2cb21150fb9fa) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061678

```text
(config)# do-exec show bgp * dampening parameters <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 14 `；EOL ` RVA 0x344C11C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-25b88931e3c31370](../../evidence/conditions-sets-015.md#c-25b88931e3c31370) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-718b55ac6700c9c8](../../evidence/state_effects-sets-024.md#s-718b55ac6700c9c8)

### path-061032

```text
(config)# do-exec show bgp * default <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 32 `；EOL ` RVA 0x344C5448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d913b53b2cfaae72](../../evidence/conditions-sets-084.md#c-d913b53b2cfaae72) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-8515cd9adc35862a](../../evidence/state_effects-sets-028.md#s-8515cd9adc35862a)

### path-061044

```text
(config)# do-exec show bgp * detail <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 44 `；EOL ` RVA 0x344C8F50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bacb85438843b612](../../evidence/conditions-sets-072.md#c-bacb85438843b612) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061654

```text
(config)# do-exec show bgp * detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 52 `；EOL ` RVA 0x344C8F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` L2VPN EVPN Route。

[条件 C-bacb85438843b612](../../evidence/conditions-sets-072.md#c-bacb85438843b612) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-faf666212ecfdfb5](../../evidence/parameters-sets-019.md#p-faf666212ecfdfb5) · [状态效果 S-b03e3ce23ce25b41](../../evidence/state_effects-sets-037.md#s-b03e3ce23ce25b41)

### path-061656

```text
(config)# do-exec show bgp * detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 53 `；EOL ` RVA 0x344C94F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv4 MVPN Route。

[条件 C-71b0d09d8874ef9f](../../evidence/conditions-sets-044.md#c-71b0d09d8874ef9f) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-f14d7edbc095e8f7](../../evidence/parameters-sets-018.md#p-f14d7edbc095e8f7) · [状态效果 S-dc40e952c331209f](../../evidence/state_effects-sets-047.md#s-dc40e952c331209f)

### path-061658

```text
(config)# do-exec show bgp * detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 54 `；EOL ` RVA 0x344C9810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` IPv6 MVPN Route。

[条件 C-4bcffea8401daca7](../../evidence/conditions-sets-030.md#c-4bcffea8401daca7) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-8e299cbbeb9d5d4c](../../evidence/parameters-sets-011.md#p-8e299cbbeb9d5d4c) · [状态效果 S-cfaabf442d91aac0](../../evidence/state_effects-sets-044.md#s-cfaabf442d91aac0)

### path-061634

```text
(config)# do-exec show bgp * evi context <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 47 `；EOL ` RVA 0x344C5C70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a5562e1be0e4ee6e](../../evidence/conditions-sets-064.md#c-a5562e1be0e4ee6e) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)

### path-061737

```text
(config)# do-exec show bgp * extcommunity-list <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 11 `；EOL ` RVA 0x34502620 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` extcommunity-list name。

[条件 C-cc3977db09fd86fa](../../evidence/conditions-sets-079.md#c-cc3977db09fd86fa) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-16c46cd5a4132de6](../../evidence/parameters-sets-002.md#p-16c46cd5a4132de6) · [状态效果 S-d2cfbc9b94ff930e](../../evidence/state_effects-sets-045.md#s-d2cfbc9b94ff930e)
