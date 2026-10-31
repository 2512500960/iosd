# qosclassmap · 已捕获槽位上的条件安装

[模式索引](README.md) · [总索引](../../README.md)

### conditional_registration_candidates-010660

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match cac status admitted <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 13 `；EOL ` RVA 0x367101B8 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-475418c4ec74cfba](../../evidence/conditional_registrations-sets-001.md#r-475418c4ec74cfba) · [条件 C-6e9d2453442a4e14](../../evidence/conditions-sets-043.md#c-6e9d2453442a4e14) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-0748e24a10b2b82f](../../evidence/state_effects-sets-002.md#s-0748e24a10b2b82f)

### conditional_registration_candidates-010656

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match class-map <string> <cr>
```

Handler ` RVA 0x16A9E1F0 `；selector ` 0 `；EOL ` RVA 0x36084B58 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Match class-map name。

[候选注册 R-28dc60528676867d](../../evidence/conditional_registrations-sets-001.md#r-28dc60528676867d) · [条件 C-6fcf6819d4a4b241](../../evidence/conditions-sets-043.md#c-6fcf6819d4a4b241) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-c2564f36743bd355](../../evidence/parameters-sets-015.md#p-c2564f36743bd355) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010659

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match data-length gt <number:0..4294967295> <cr>
```

Handler ` RVA 0x16AC50E0 `；selector ` 0 `；EOL ` RVA 0x360AD188 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Maximum allowed data transfer in a session。

[候选注册 R-71b4e99a4d062edc](../../evidence/conditional_registrations-sets-002.md#r-71b4e99a4d062edc) · [条件 C-2cd2ef904228e1ad](../../evidence/conditions-sets-018.md#c-2cd2ef904228e1ad) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-441d967ad27920d6](../../evidence/parameters-sets-006.md#p-441d967ad27920d6) · [状态效果 S-e0d3e3dfa386ba65](../../evidence/state_effects-sets-048.md#s-e0d3e3dfa386ba65)

### conditional_registration_candidates-010676

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match identity source user <string> <cr>
```

Handler ` RVA 0x16A9E9F0 `；selector ` 0 `；EOL ` RVA 0x36084800 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Username to match。

[候选注册 R-28dc60528676867d](../../evidence/conditional_registrations-sets-001.md#r-28dc60528676867d) · [条件 C-6fcf6819d4a4b241](../../evidence/conditions-sets-043.md#c-6fcf6819d4a4b241) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-69106f9d77b1b6be](../../evidence/parameters-sets-008.md#p-69106f9d77b1b6be) · [状态效果 S-8b333a8ee99c6f6c](../../evidence/state_effects-sets-030.md#s-8b333a8ee99c6f6c)

### conditional_registration_candidates-010650

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match invalid-command <cr>
```

Handler ` RVA 0x16AA23E0 `；selector ` 0 `；EOL ` RVA 0x360A7F38 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-3e6452e892231968](../../evidence/conditional_registrations-sets-001.md#r-3e6452e892231968) · [条件 C-1d6b624061e2f952](../../evidence/conditions-sets-011.md#c-1d6b624061e2f952) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-f2bac263f27bce24](../../evidence/state_effects-sets-051.md#s-f2bac263f27bce24)

### conditional_registration_candidates-010651

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match message-length <cr>
```

Handler ` RVA 0x16AC8680 `；selector ` 0 `；EOL ` RVA 0x360AE420 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-626b4936a8681bf9](../../evidence/conditional_registrations-sets-001.md#r-626b4936a8681bf9) · [条件 C-5f6c2c5077a6de01](../../evidence/conditions-sets-037.md#c-5f6c2c5077a6de01) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-46652c4bf8aa3757](../../evidence/state_effects-sets-015.md#s-46652c4bf8aa3757)

### conditional_registration_candidates-010652

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match message-length <cr>
```

Handler ` RVA 0x16AC8680 `；selector ` 0 `；EOL ` RVA 0x360AEF90 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-315fa067070bb136](../../evidence/conditional_registrations-sets-001.md#r-315fa067070bb136) · [条件 C-7e12cd4f5c5e9170](../../evidence/conditions-sets-049.md#c-7e12cd4f5c5e9170) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-a1ee820f02e22526](../../evidence/state_effects-sets-034.md#s-a1ee820f02e22526)

### conditional_registration_candidates-010679

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match metadata cac status admitted <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 13 `；EOL ` RVA 0x36711480 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-51a9f3c9289f4a01](../../evidence/conditional_registrations-sets-001.md#r-51a9f3c9289f4a01) · [条件 C-2d7844de520f5a05](../../evidence/conditions-sets-018.md#c-2d7844de520f5a05) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-5ba4fb97cc6d4c21](../../evidence/state_effects-sets-020.md#s-5ba4fb97cc6d4c21)

### conditional_registration_candidates-010666

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match metadata called-uri <string> <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 15 `；EOL ` RVA 0x36710E98 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Called URI string。

[候选注册 R-51a9f3c9289f4a01](../../evidence/conditional_registrations-sets-001.md#r-51a9f3c9289f4a01) · [条件 C-2d7844de520f5a05](../../evidence/conditions-sets-018.md#c-2d7844de520f5a05) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-854100de5e4461eb](../../evidence/parameters-sets-010.md#p-854100de5e4461eb) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010663

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match metadata calling-uri <string> <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 14 `；EOL ` RVA 0x36710BB0 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Calling URI string。

[候选注册 R-51a9f3c9289f4a01](../../evidence/conditional_registrations-sets-001.md#r-51a9f3c9289f4a01) · [条件 C-2d7844de520f5a05](../../evidence/conditions-sets-018.md#c-2d7844de520f5a05) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-66a96f78e55a1f83](../../evidence/parameters-sets-008.md#p-66a96f78e55a1f83) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010668

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match metadata device-model <string> <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 16 `；EOL ` RVA 0x36711180 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Device model string。

[候选注册 R-51a9f3c9289f4a01](../../evidence/conditional_registrations-sets-001.md#r-51a9f3c9289f4a01) · [条件 C-2d7844de520f5a05](../../evidence/conditions-sets-018.md#c-2d7844de520f5a05) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-06897e519d91c733](../../evidence/parameters-sets-001.md#p-06897e519d91c733) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010661

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match metadata global-session-id <string> <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 6 `；EOL ` RVA 0x367105E0 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Global Session ID Value。

[候选注册 R-51a9f3c9289f4a01](../../evidence/conditional_registrations-sets-001.md#r-51a9f3c9289f4a01) · [条件 C-2d7844de520f5a05](../../evidence/conditions-sets-018.md#c-2d7844de520f5a05) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-c570b146053b38c1](../../evidence/parameters-sets-015.md#p-c570b146053b38c1) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010662

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match metadata multi-party-session-id <string> <cr>
```

Handler ` RVA 0x18252C20 `；selector ` 7 `；EOL ` RVA 0x367108C8 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Multi Party Session ID Value。

[候选注册 R-51a9f3c9289f4a01](../../evidence/conditional_registrations-sets-001.md#r-51a9f3c9289f4a01) · [条件 C-2d7844de520f5a05](../../evidence/conditions-sets-018.md#c-2d7844de520f5a05) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-4eb5e26ff952f876](../../evidence/parameters-sets-006.md#p-4eb5e26ff952f876) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010686

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match nbar-protocol <?protoname_action@55558bd0ac20> <cr>
```

Handler ` RVA 0xD844FA0 `；selector ` 0 `；EOL ` RVA 0x367B6C60 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-6db786e351a66251](../../evidence/conditional_registrations-sets-001.md#r-6db786e351a66251) · [条件 C-329e295327d87cbf](../../evidence/conditions-sets-020.md#c-329e295327d87cbf) · [缺口 G-9368ebe40ccf02d4](../../evidence/gaps-sets-005.md#g-9368ebe40ccf02d4) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010654

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match peer <address> <cr>
```

Handler ` RVA 0x18697ED0 `；selector ` 1 `；EOL ` RVA 0x367B6358 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Device ID。

[候选注册 R-6db786e351a66251](../../evidence/conditional_registrations-sets-001.md#r-6db786e351a66251) · [条件 C-329e295327d87cbf](../../evidence/conditions-sets-020.md#c-329e295327d87cbf) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-582d641636920948](../../evidence/parameters-sets-007.md#p-582d641636920948) · [状态效果 S-0be1fda302a34b0a](../../evidence/state_effects-sets-003.md#s-0be1fda302a34b0a)

### conditional_registration_candidates-010655

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match protocol mapi <cr>
```

Handler ` RVA 0x18697ED0 `；selector ` 2 `；EOL ` RVA 0x367B6640 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-6db786e351a66251](../../evidence/conditional_registrations-sets-001.md#r-6db786e351a66251) · [条件 C-329e295327d87cbf](../../evidence/conditions-sets-020.md#c-329e295327d87cbf) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-e03327c11e0a94cf](../../evidence/state_effects-sets-047.md#s-e03327c11e0a94cf)

### conditional_registration_candidates-010653

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match protocol tcp <cr>
```

Handler ` RVA 0x16A9ED10 `；selector ` 0 `；EOL ` RVA 0x360842B8 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-28dc60528676867d](../../evidence/conditional_registrations-sets-001.md#r-28dc60528676867d) · [条件 C-6fcf6819d4a4b241](../../evidence/conditions-sets-043.md#c-6fcf6819d4a4b241) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-f1150362c32e83ea](../../evidence/state_effects-sets-051.md#s-f1150362c32e83ea)

### conditional_registration_candidates-010658

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 31 `；EOL ` RVA 0x360AB048 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-15d43c863824dcb5](../../evidence/conditions-sets-009.md#c-15d43c863824dcb5) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010664

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body java-applet <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 18 `；EOL ` RVA 0x360AC248 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-38de9e06d5745fa5](../../evidence/conditions-sets-022.md#c-38de9e06d5745fa5) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010671

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body length <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 32 `；EOL ` RVA 0x360A91F8 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-bf0eb5f6ce61056a](../../evidence/conditions-sets-074.md#c-bf0eb5f6ce61056a) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010672

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body length <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 28 `；EOL ` RVA 0x360A9478 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-7659f90c1e8e3c66](../../evidence/conditions-sets-046.md#c-7659f90c1e8e3c66) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010673

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body length <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 35 `；EOL ` RVA 0x360A9708 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-c91ace2e4537c28d](../../evidence/conditions-sets-077.md#c-c91ace2e4537c28d) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010674

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body length <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 23 `；EOL ` RVA 0x360A99B0 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-0cb2c41cf557d964](../../evidence/conditions-sets-005.md#c-0cb2c41cf557d964) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010675

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body length <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 24 `；EOL ` RVA 0x360A9C58 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-ee3407ee57195d08](../../evidence/conditions-sets-092.md#c-ee3407ee57195d08) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010680

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body regex-pattern <string> <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 34 `；EOL ` RVA 0x360AA000 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the regex pattern。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-6e87bcc34e3818f5](../../evidence/conditions-sets-043.md#c-6e87bcc34e3818f5) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-5ac7510abc044ad0](../../evidence/parameters-sets-007.md#p-5ac7510abc044ad0) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010681

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body regex-pattern <string> <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 30 `；EOL ` RVA 0x360AA280 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the regex pattern。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-5550a6967488e87d](../../evidence/conditions-sets-033.md#c-5550a6967488e87d) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-5ac7510abc044ad0](../../evidence/parameters-sets-007.md#p-5ac7510abc044ad0) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010682

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body regex-pattern <string> <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 36 `；EOL ` RVA 0x360AA510 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the regex pattern。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-15c34de425e56dea](../../evidence/conditions-sets-009.md#c-15c34de425e56dea) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-5ac7510abc044ad0](../../evidence/parameters-sets-007.md#p-5ac7510abc044ad0) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010683

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body regex-pattern <string> <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 25 `；EOL ` RVA 0x360AA7B8 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the regex pattern。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-0614663fcc32e776](../../evidence/conditions-sets-003.md#c-0614663fcc32e776) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-5ac7510abc044ad0](../../evidence/parameters-sets-007.md#p-5ac7510abc044ad0) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010684

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body regex-pattern <string> <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 37 `；EOL ` RVA 0x360AAA60 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the regex pattern。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-e02f9106f0cf46f9](../../evidence/conditions-sets-086.md#c-e02f9106f0cf46f9) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-5ac7510abc044ad0](../../evidence/parameters-sets-007.md#p-5ac7510abc044ad0) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010685

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request body regex-pattern <string> <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 26 `；EOL ` RVA 0x360AAD08 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Specify the regex pattern。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-3f8e532b2f66aa5d](../../evidence/conditions-sets-025.md#c-3f8e532b2f66aa5d) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [参数 P-5ac7510abc044ad0](../../evidence/parameters-sets-007.md#p-5ac7510abc044ad0) · [状态效果 S-41fd5fd17a77898e](../../evidence/state_effects-sets-014.md#s-41fd5fd17a77898e)

### conditional_registration_candidates-010678

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request header accept chunked <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 20 `；EOL ` RVA 0x360AB370 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-06dae5c2e5d4a2ca](../../evidence/conditions-sets-003.md#c-06dae5c2e5d4a2ca) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-aa6ae92cd23c5286](../../evidence/state_effects-sets-036.md#s-aa6ae92cd23c5286)

### conditional_registration_candidates-010677

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request header accept violation <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 27 `；EOL ` RVA 0x360A86D8 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-6e0d8b1019ad3c87](../../evidence/conditions-sets-043.md#c-6e0d8b1019ad3c87) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-0734b2de72c660c7](../../evidence/state_effects-sets-002.md#s-0734b2de72c660c7)

### conditional_registration_candidates-010669

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request header count <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 33 `；EOL ` RVA 0x360A8AB0 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-1bdc87069242e125](../../evidence/conditions-sets-011.md#c-1bdc87069242e125) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-a5a8516781ffe837](../../evidence/state_effects-sets-035.md#s-a5a8516781ffe837)

### conditional_registration_candidates-010670

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request header count <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 29 `；EOL ` RVA 0x360A8D30 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-d4ac987f733751d3](../../evidence/conditions-sets-082.md#c-d4ac987f733751d3) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-a5a8516781ffe837](../../evidence/state_effects-sets-035.md#s-a5a8516781ffe837)

### conditional_registration_candidates-010665

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request method connect <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 22 `；EOL ` RVA 0x360AC580 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-a70fdd0d50177975](../../evidence/conditions-sets-064.md#c-a70fdd0d50177975) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-4227cc8b4c12a21e](../../evidence/state_effects-sets-014.md#s-4227cc8b4c12a21e)

### conditional_registration_candidates-010667

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request port-misuse im <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 21 `；EOL ` RVA 0x360AC918 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-cf3b9d406ba531ed](../../evidence/conditions-sets-080.md#c-cf3b9d406ba531ed) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-65b5404b1d648206](../../evidence/state_effects-sets-022.md#s-65b5404b1d648206)

### conditional_registration_candidates-010657

```text
(config-cmap)# <?dumper_command_func@55558946b3f8> <?sync_force_action@55558946b458> match request protocol-violation <cr>
```

Handler ` RVA 0x16AA2820 `；selector ` 19 `；EOL ` RVA 0x360ACCC0 `。

模式根 ` RVA 0x33F0EFD0 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[候选注册 R-97d7691792560ddc](../../evidence/conditional_registrations-sets-002.md#r-97d7691792560ddc) · [条件 C-681e5c260492c3d7](../../evidence/conditions-sets-040.md#c-681e5c260492c3d7) · [缺口 G-1a6f024962063875](../../evidence/gaps-sets-001.md#g-1a6f024962063875) · [状态效果 S-a391dfc4d4fdbcce](../../evidence/state_effects-sets-035.md#s-a391dfc4d4fdbcce)
