# line · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-072986

```text
(config-line)# absolute-timeout <number:0..10000> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Absolute timeout interval in minutes。

[条件 C-082e80361b5bc7b1](../../evidence/conditions-sets-004.md#c-082e80361b5bc7b1) · [参数 P-267260ddd09478b7](../../evidence/parameters-sets-003.md#p-267260ddd09478b7)

### path-073053

```text
(config-line)# access-class <number:1..199> out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` IP access list。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [参数 P-b42407ad4477584d](../../evidence/parameters-sets-014.md#p-b42407ad4477584d) · [状态效果 S-e3cc46ae11d15085](../../evidence/state_effects-sets-048.md#s-e3cc46ae11d15085)

### path-073101

```text
(config-line)# accounting resource default <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2048167873fb6c15](../../evidence/conditions-sets-013.md#c-2048167873fb6c15) · [状态效果 S-c69f4018d604c403](../../evidence/state_effects-sets-042.md#s-c69f4018d604c403)

### path-073149

```text
(config-line)# activation-character <?char_number_action@5555891b7498> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 110 `；EOL ` RVA 0x33C634C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-93ac5cdf11071272](../../evidence/conditions-sets-057.md#c-93ac5cdf11071272) · [缺口 G-f2c45d2da9feca49](../../evidence/gaps-sets-008.md#g-f2c45d2da9feca49)

### path-073095

```text
(config-line)# authorization reverse-access default <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a78264870e4f58ce](../../evidence/conditions-sets-065.md#c-a78264870e4f58ce) · [状态效果 S-84cde79cd28f566b](../../evidence/state_effects-sets-028.md#s-84cde79cd28f566b)

### path-072892

```text
(config-line)# autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d19d0d1a44fb0d8](../../evidence/conditions-sets-011.md#c-1d19d0d1a44fb0d8) · [状态效果 S-27da9f98150f4fe6](../../evidence/state_effects-sets-009.md#s-27da9f98150f4fe6)

### path-073037

```text
(config-line)# autocommand <string> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Appropriate EXEC command。

[条件 C-d56524b560c4a268](../../evidence/conditions-sets-082.md#c-d56524b560c4a268) · [参数 P-1da426af8757be3b](../../evidence/parameters-sets-003.md#p-1da426af8757be3b)

### path-073159

```text
(config-line)# autocommand-options abort-character <?char_number_action@5555896d4808> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c36b983bc43fc52f](../../evidence/conditions-sets-075.md#c-c36b983bc43fc52f) · [缺口 G-563171475adf2a58](../../evidence/gaps-sets-003.md#g-563171475adf2a58) · [状态效果 S-24640911b71e5899](../../evidence/state_effects-sets-008.md#s-24640911b71e5899)

### path-073043

```text
(config-line)# autocommand-options nohangup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8cb4960d778ef1d5](../../evidence/conditions-sets-054.md#c-8cb4960d778ef1d5) · [状态效果 S-caca87bd7cab724f](../../evidence/state_effects-sets-043.md#s-caca87bd7cab724f)

### path-072894

```text
(config-line)# autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072977

```text
(config-line)# autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072996

```text
(config-line)# autohost <string> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Host to automatically connect to。

[条件 C-258e990a069c7aba](../../evidence/conditions-sets-015.md#c-258e990a069c7aba) · [参数 P-0c16133141743476](../../evidence/parameters-sets-001.md#p-0c16133141743476)

### path-072901

```text
(config-line)# autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072970

```text
(config-line)# autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-1632f291dead775c](../../evidence/state_effects-sets-005.md#s-1632f291dead775c)

### path-072864

```text
(config-line)# buffer-length <number:16..1536> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` buffer length in bytes。

[条件 C-293888dfac8cfadc](../../evidence/conditions-sets-016.md#c-293888dfac8cfadc) · [参数 P-c1be88f0a8e29c00](../../evidence/parameters-sets-015.md#p-c1be88f0a8e29c00)

### path-072862

```text
(config-line)# data-character-bits <number:7..8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bits per character。

[条件 C-32190f3d94072090](../../evidence/conditions-sets-020.md#c-32190f3d94072090) · [参数 P-8925e9101d554722](../../evidence/parameters-sets-011.md#p-8925e9101d554722)

### path-073012

```text
(config-line)# databits 5 <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-303e3169b34199d9](../../evidence/conditions-sets-019.md#c-303e3169b34199d9) · [状态效果 S-db0adb654898a051](../../evidence/state_effects-sets-046.md#s-db0adb654898a051)

### path-072989

```text
(config-line)# default absolute-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3628bfc47d2a78a1](../../evidence/conditions-sets-021.md#c-3628bfc47d2a78a1) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073057

```text
(config-line)# default access-class out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3553415c5bc395cc](../../evidence/conditions-sets-021.md#c-3553415c5bc395cc) · [状态效果 S-8c05c84cf7d1c64e](../../evidence/state_effects-sets-030.md#s-8c05c84cf7d1c64e)

### path-073105

```text
(config-line)# default accounting resource <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8377cda2cd438bc4](../../evidence/conditions-sets-051.md#c-8377cda2cd438bc4) · [状态效果 S-83e484b3c691cc20](../../evidence/state_effects-sets-028.md#s-83e484b3c691cc20)

### path-072965

```text
(config-line)# default activation-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 110 `；EOL ` RVA 0x33C634C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f4bfd51ac361f32](../../evidence/conditions-sets-049.md#c-7f4bfd51ac361f32) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073098

```text
(config-line)# default authorization reverse-access <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9c1cf71cf580ac7](../../evidence/conditions-sets-090.md#c-e9c1cf71cf580ac7) · [状态效果 S-15ff28610305e256](../../evidence/state_effects-sets-005.md#s-15ff28610305e256)

### path-072974

```text
(config-line)# default autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1d19d0d1a44fb0d8](../../evidence/conditions-sets-011.md#c-1d19d0d1a44fb0d8) · [状态效果 S-0bd869fad311febd](../../evidence/state_effects-sets-003.md#s-0bd869fad311febd)

### path-073029

```text
(config-line)# default autocommand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e745dcf1b565bb0f](../../evidence/conditions-sets-089.md#c-e745dcf1b565bb0f) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073035

```text
(config-line)# default autocommand-options <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-26288db5234dfd0b](../../evidence/conditions-sets-015.md#c-26288db5234dfd0b) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072988

```text
(config-line)# default autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073092

```text
(config-line)# default autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073000

```text
(config-line)# default autohost <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f03548a8912681d5](../../evidence/conditions-sets-093.md#c-f03548a8912681d5) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073026

```text
(config-line)# default autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073073

```text
(config-line)# default autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-0bb143535f08b5eb](../../evidence/state_effects-sets-003.md#s-0bb143535f08b5eb)

### path-072886

```text
(config-line)# default buffer-length <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4d9a28b405e0e965](../../evidence/conditions-sets-030.md#c-4d9a28b405e0e965) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072869

```text
(config-line)# default data-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a9ce9d6b7bedb05](../../evidence/conditions-sets-004.md#c-0a9ce9d6b7bedb05) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073032

```text
(config-line)# default databits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e66cc91620aa263](../../evidence/conditions-sets-055.md#c-8e66cc91620aa263) · [状态效果 S-e687ce7277879a99](../../evidence/state_effects-sets-049.md#s-e687ce7277879a99)

### path-072969

```text
(config-line)# default disconnect-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 113 `；EOL ` RVA 0x33C63810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0693ad11e0c8f89f](../../evidence/conditions-sets-003.md#c-0693ad11e0c8f89f) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073018

```text
(config-line)# default dispatch-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1da0473f329610f9](../../evidence/conditions-sets-011.md#c-1da0473f329610f9) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072966

```text
(config-line)# default dispatch-machine <cr>
```

Handler ` RVA 0xDE9D520 `；selector ` 0 `；EOL ` RVA 0x33C63168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-412c53c49c43996f](../../evidence/conditions-sets-025.md#c-412c53c49c43996f) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072896

```text
(config-line)# default dispatch-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 114 `；EOL ` RVA 0x33C61B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-61641745abe373dd](../../evidence/conditions-sets-038.md#c-61641745abe373dd) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072930

```text
(config-line)# default domain-lookup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 2 `；EOL ` RVA 0x34128800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072921

```text
(config-line)# default download <cr>
```

Handler ` RVA 0xE05E330 `；selector ` 138 `；EOL ` RVA 0x3417D940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-69fe14440175699b](../../evidence/conditions-sets-041.md#c-69fe14440175699b) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072949

```text
(config-line)# default editing <cr>
```

Handler ` RVA 0xE059390 `；selector ` 137 `；EOL ` RVA 0x3412A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072994

```text
(config-line)# default escape-character <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 5 `；EOL ` RVA 0x341607F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bfd506ace8770013](../../evidence/conditions-sets-074.md#c-bfd506ace8770013) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072937

```text
(config-line)# default exec <cr>
```

Handler ` RVA 0xE059390 `；selector ` 125 `；EOL ` RVA 0x34129088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e4cd11f0371c2bbd](../../evidence/conditions-sets-088.md#c-e4cd11f0371c2bbd) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073131

```text
(config-line)# default exec prompt expand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 40 `；EOL ` RVA 0x34128B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073133

```text
(config-line)# default exec prompt timestamp <cr>
```

Handler ` RVA 0xE059390 `；selector ` 38 `；EOL ` RVA 0x34128DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072922

```text
(config-line)# default exec-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 11 `；EOL ` RVA 0x3412B998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072928

```text
(config-line)# default exec-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 134 `；EOL ` RVA 0x34128270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-93ac0e44f3551c79](../../evidence/conditions-sets-057.md#c-93ac0e44f3551c79) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072933

```text
(config-line)# default exec-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 13 `；EOL ` RVA 0x3412BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-924a0d7ff2706cbd](../../evidence/conditions-sets-056.md#c-924a0d7ff2706cbd) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073123

```text
(config-line)# default flowcontrol software <cr>
```

Handler ` RVA 0xE056390 `；selector ` 104 `；EOL ` RVA 0x34183DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5b4d6e13e59d582b](../../evidence/conditions-sets-036.md#c-5b4d6e13e59d582b) · [状态效果 S-d3db0f2cf66b642b](../../evidence/state_effects-sets-045.md#s-d3db0f2cf66b642b)

### path-072957

```text
(config-line)# default flush-at-activation <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 164 `；EOL ` RVA 0x33C62DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072956

```text
(config-line)# default full-help <cr>
```

Handler ` RVA 0xE059390 `；selector ` 139 `；EOL ` RVA 0x3412A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072951

```text
(config-line)# default history <cr>
```

Handler ` RVA 0xE059390 `；selector ` 135 `；EOL ` RVA 0x34129D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072944

```text
(config-line)# default history size <cr>
```

Handler ` RVA 0xE059390 `；selector ` 136 `；EOL ` RVA 0x34129CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b2122c1cc0d973b6](../../evidence/conditions-sets-069.md#c-b2122c1cc0d973b6) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073027

```text
(config-line)# default hold-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 122 `；EOL ` RVA 0x33C62820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3b8c23f1001aa671](../../evidence/conditions-sets-023.md#c-3b8c23f1001aa671) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073016

```text
(config-line)# default insecure <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 22 `；EOL ` RVA 0x33C65158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072952

```text
(config-line)# default international <cr>
```

Handler ` RVA 0xE059390 `；selector ` 36 `；EOL ` RVA 0x3412A4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073141

```text
(config-line)# default ip netmask-format hexadecimal <cr>
```

Handler ` RVA 0xE059390 `；selector ` 33 `；EOL ` RVA 0x33D406C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-ac98b9a4e4ecb24b](../../evidence/state_effects-sets-036.md#s-ac98b9a4e4ecb24b)

### path-073093

```text
(config-line)# default ip tcp input-coalesce-threshold <cr>
```

Handler ` RVA 0xE059390 `；selector ` 35 `；EOL ` RVA 0x33D40A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13bb3cc59bb39fd5](../../evidence/conditions-sets-008.md#c-13bb3cc59bb39fd5) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073146

```text
(config-line)# default ipv6 access-class <string> out <cr>
```

Handler ` RVA 0x12165730 `；selector ` 0 `；EOL ` RVA 0x357AFFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Access-list name。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [参数 P-2f4c08e17f96c869](../../evidence/parameters-sets-004.md#p-2f4c08e17f96c869) · [状态效果 S-76db7c8345fc4de2](../../evidence/state_effects-sets-025.md#s-76db7c8345fc4de2)

### path-073129

```text
(config-line)# default ipv6 format scoped_help-string <cr>
```

Handler ` RVA 0x12321A90 `；selector ` 0 `；EOL ` RVA 0x3580DEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-69fe14440175699b](../../evidence/conditions-sets-041.md#c-69fe14440175699b) · [状态效果 S-af8681b88bf84b3e](../../evidence/state_effects-sets-037.md#s-af8681b88bf84b3e)

### path-072948

```text
(config-line)# default length <cr>
```

Handler ` RVA 0xE059390 `；selector ` 0 `；EOL ` RVA 0x34129408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ece84a5eafbd17d](../../evidence/conditions-sets-043.md#c-6ece84a5eafbd17d) · [状态效果 S-a7581042bcccdc36](../../evidence/state_effects-sets-035.md#s-a7581042bcccdc36)

### path-072920

```text
(config-line)# default location <cr>
```

Handler ` RVA 0xE059390 `；selector ` 15 `；EOL ` RVA 0x3412AF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c5d5646c2b799690](../../evidence/conditions-sets-076.md#c-c5d5646c2b799690) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072968

```text
(config-line)# default lockable <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 116 `；EOL ` RVA 0x33C63AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073088

```text
(config-line)# default logging synchronous <cr>
```

Handler ` RVA 0xE054FE0 `；selector ` 0 `；EOL ` RVA 0x3417DD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-17890655ee001dfa](../../evidence/conditions-sets-009.md#c-17890655ee001dfa) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073003

```text
(config-line)# default login <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 16 `；EOL ` RVA 0x3417EA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d3d65af3294161d8](../../evidence/conditions-sets-082.md#c-d3d65af3294161d8) · [状态效果 S-60511410d0a25cc7](../../evidence/state_effects-sets-021.md#s-60511410d0a25cc7)

### path-073107

```text
(config-line)# default login authentication <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 26 `；EOL ` RVA 0x3417E628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4e9400694f537e01](../../evidence/conditions-sets-031.md#c-4e9400694f537e01) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072981

```text
(config-line)# default logout-warning <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 141 `；EOL ` RVA 0x33C63E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0b92095e4f2ffb3](../../evidence/conditions-sets-093.md#c-f0b92095e4f2ffb3) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073120

```text
(config-line)# default modem answer-timeout <cr>
```

Handler ` RVA 0xDE8F510 `；selector ` 0 `；EOL ` RVA 0x3417F1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ea2a232078d944d](../../evidence/conditions-sets-018.md#c-2ea2a232078d944d) · [状态效果 S-a723c03b089159c4](../../evidence/state_effects-sets-035.md#s-a723c03b089159c4)

### path-073126

```text
(config-line)# default modem autoconfigure <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5b68fc8d5919224e](../../evidence/conditions-sets-036.md#c-5b68fc8d5919224e) · [状态效果 S-61d6c8f31b4c7214](../../evidence/state_effects-sets-021.md#s-61d6c8f31b4c7214)

### path-073124

```text
(config-line)# default modem busyout <cr>
```

Handler ` RVA 0xFDCEDB0 `；selector ` 162 `；EOL ` RVA 0x348DBB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bc6eee7f1808dfdd](../../evidence/conditions-sets-073.md#c-bc6eee7f1808dfdd) · [状态效果 S-61d6c8f31b4c7214](../../evidence/state_effects-sets-021.md#s-61d6c8f31b4c7214)

### path-073118

```text
(config-line)# default modem callin <cr>
```

Handler ` RVA 0xDE8F920 `；selector ` 105 `；EOL ` RVA 0x3417F7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-fdecd0467059444a](../../evidence/state_effects-sets-054.md#s-fdecd0467059444a)

### path-073119

```text
(config-line)# default modem dtr-delay <cr>
```

Handler ` RVA 0xDE8F710 `；selector ` 0 `；EOL ` RVA 0x3417F528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0aa180e9316f8243](../../evidence/conditions-sets-004.md#c-0aa180e9316f8243) · [状态效果 S-f585eea797e0633c](../../evidence/state_effects-sets-052.md#s-f585eea797e0633c)

### path-072960

```text
(config-line)# default monitor <cr>
```

Handler ` RVA 0xE060540 `；selector ` 4 `；EOL ` RVA 0x3418FDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072923

```text
(config-line)# default motd-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 12 `；EOL ` RVA 0x3412CA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c67f2357e8242152](../../evidence/conditions-sets-076.md#c-c67f2357e8242152) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072939

```text
(config-line)# default notify <cr>
```

Handler ` RVA 0xE059390 `；selector ` 7 `；EOL ` RVA 0x341299F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073082

```text
(config-line)# default ntp pps-discipline <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 1 `；EOL ` RVA 0x348FB6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eadca0ca33836c5b](../../evidence/conditions-sets-091.md#c-eadca0ca33836c5b) · [状态效果 S-91ec0dd2a3da87f8](../../evidence/state_effects-sets-031.md#s-91ec0dd2a3da87f8)

### path-073059

```text
(config-line)# default ntp refclock <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 0 `；EOL ` RVA 0x348FA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8bb4f0d79de50ae0](../../evidence/conditions-sets-054.md#c-8bb4f0d79de50ae0) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073028

```text
(config-line)# default parity <cr>
```

Handler ` RVA 0xE059390 `；selector ` 101 `；EOL ` RVA 0x34182320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb1ccec72a6dc471](../../evidence/conditions-sets-097.md#c-fb1ccec72a6dc471) · [状态效果 S-77b7beefd71dc4de](../../evidence/state_effects-sets-025.md#s-77b7beefd71dc4de)

### path-072958

```text
(config-line)# default password <cr>
```

Handler ` RVA 0xDDD7F60 `；selector ` 18 `；EOL ` RVA 0x34198A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c5bd20d70684bbc8](../../evidence/conditions-sets-076.md#c-c5bd20d70684bbc8) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073049

```text
(config-line)# default prc expose <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 0 `；EOL ` RVA 0x341279C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073051

```text
(config-line)# default prc hide <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 1 `；EOL ` RVA 0x34127C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073004

```text
(config-line)# default private <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 115 `；EOL ` RVA 0x33C64EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072932

```text
(config-line)# default privilege level <cr>
```

Handler ` RVA 0xE059390 `；selector ` 160 `；EOL ` RVA 0x3412C040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-29ab2d22fe13705f](../../evidence/conditions-sets-016.md#c-29ab2d22fe13705f) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073001

```text
(config-line)# default refuse-message <cr>
```

Handler ` RVA 0xE055DF0 `；selector ` 19 `；EOL ` RVA 0x3417EDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d3cd21c03b874343](../../evidence/conditions-sets-082.md#c-d3cd21c03b874343) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073020

```text
(config-line)# default rotary <cr>
```

Handler ` RVA 0xE059390 `；selector ` 109 `；EOL ` RVA 0x3417FEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-71cca0afedacdbce](../../evidence/conditions-sets-044.md#c-71cca0afedacdbce) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072903

```text
(config-line)# default rxspeed <cr>
```

Handler ` RVA 0xE0552E0 `；selector ` 119 `；EOL ` RVA 0x34183280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-55e2747835787742](../../evidence/conditions-sets-034.md#c-55e2747835787742) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073096

```text
(config-line)# default script activation <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 155 `；EOL ` RVA 0x346027E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-215bf3652502dcc1](../../evidence/conditions-sets-013.md#c-215bf3652502dcc1) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073108

```text
(config-line)# default script arap-callback <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 158 `；EOL ` RVA 0x34602E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4c38063eff5d7d76](../../evidence/conditions-sets-030.md#c-4c38063eff5d7d76) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073114

```text
(config-line)# default script callback <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 157 `；EOL ` RVA 0x34603190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e635e8275c25430](../../evidence/conditions-sets-061.md#c-9e635e8275c25430) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073069

```text
(config-line)# default script connection <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 152 `；EOL ` RVA 0x34601E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-83a0aef5cc692321](../../evidence/conditions-sets-051.md#c-83a0aef5cc692321) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073078

```text
(config-line)# default script dialer <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 154 `；EOL ` RVA 0x34602150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-13c0f7a2f55adda9](../../evidence/conditions-sets-008.md#c-13c0f7a2f55adda9) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073103

```text
(config-line)# default script modem-off-hook <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 159 `；EOL ` RVA 0x34602B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f340bfeeb1e2585f](../../evidence/conditions-sets-094.md#c-f340bfeeb1e2585f) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073089

```text
(config-line)# default script reset <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 153 `；EOL ` RVA 0x34602498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-18a0d0e24d1afb45](../../evidence/conditions-sets-010.md#c-18a0d0e24d1afb45) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073065

```text
(config-line)# default script startup <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 151 `；EOL ` RVA 0x34601AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f043b7bafa43ae19](../../evidence/conditions-sets-093.md#c-f043b7bafa43ae19) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073006

```text
(config-line)# default session-disconnect-warning <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 34 `；EOL ` RVA 0x33C64848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f19bade8631de94d](../../evidence/conditions-sets-093.md#c-f19bade8631de94d) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073019

```text
(config-line)# default session-limit <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 24 `；EOL ` RVA 0x33C64C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-929c86128c416b9f](../../evidence/conditions-sets-057.md#c-929c86128c416b9f) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072911

```text
(config-line)# default session-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 117 `；EOL ` RVA 0x3412ABB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0a2a22a9c9a29073](../../evidence/conditions-sets-004.md#c-0a2a22a9c9a29073) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072924

```text
(config-line)# default shell <cr>
```

Handler ` RVA 0xE059390 `；selector ` 39 `；EOL ` RVA 0x340B9858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2cf532477d6301dd](../../evidence/conditions-sets-018.md#c-2cf532477d6301dd) · [状态效果 S-4bfbcc003a8a1d6e](../../evidence/state_effects-sets-017.md#s-4bfbcc003a8a1d6e)

### path-072875

```text
(config-line)# default special-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 133 `；EOL ` RVA 0x341281C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-829c2bf5996abb15](../../evidence/conditions-sets-051.md#c-829c2bf5996abb15) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073044

```text
(config-line)# default speed <cr>
```

Handler ` RVA 0xE055B70 `；selector ` 118 `；EOL ` RVA 0x34183320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0c9427473ec22fef](../../evidence/conditions-sets-005.md#c-0c9427473ec22fef) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073038

```text
(config-line)# default start-character <cr>
```

Handler ` RVA 0xE059390 `；selector ` 108 `；EOL ` RVA 0x34182C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-02fe6662780beda5](../../evidence/conditions-sets-002.md#c-02fe6662780beda5) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073041

```text
(config-line)# default stop-character <cr>
```

Handler ` RVA 0xE059390 `；selector ` 107 `；EOL ` RVA 0x34182FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a8478c287e81324b](../../evidence/conditions-sets-065.md#c-a8478c287e81324b) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073034

```text
(config-line)# default stopbits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 25 `；EOL ` RVA 0x34182808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b8ea640a2e8f67ad](../../evidence/conditions-sets-071.md#c-b8ea640a2e8f67ad) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073084

```text
(config-line)# default telnet break-on-ip <cr>
```

Handler ` RVA 0xCCF24C0 `；selector ` 100 `；EOL ` RVA 0x33C615A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-9c7fc63dee543bc9](../../evidence/state_effects-sets-033.md#s-9c7fc63dee543bc9)

### path-072910

```text
(config-line)# default terminal-type <cr>
```

Handler ` RVA 0xE059390 `；selector ` 126 `；EOL ` RVA 0x341276A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0dfde72d2fabe292](../../evidence/conditions-sets-006.md#c-0dfde72d2fabe292) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073136

```text
(config-line)# default timeout login response <cr>
```

Handler ` RVA 0xE059390 `；selector ` 37 `；EOL ` RVA 0x3412C788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-96f04445c05131c0](../../evidence/conditions-sets-058.md#c-96f04445c05131c0) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072995

```text
(config-line)# default transport <cr>
```

Handler ` RVA 0xDE835F0 `；selector ` 124 `；EOL ` RVA 0x34188630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0640441ccdc5d0f8](../../evidence/conditions-sets-003.md#c-0640441ccdc5d0f8) · [状态效果 S-8f6ca2eae7eb1c19](../../evidence/state_effects-sets-030.md#s-8f6ca2eae7eb1c19)

### path-072905

```text
(config-line)# default txspeed <cr>
```

Handler ` RVA 0xE055A00 `；selector ` 120 `；EOL ` RVA 0x34183688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2a9ca4e00b5ffca0](../../evidence/conditions-sets-017.md#c-2a9ca4e00b5ffca0) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072982

```text
(config-line)# default vacant-message <cr>
```

Handler ` RVA 0xE053ED0 `；selector ` 20 `；EOL ` RVA 0x3417E200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a947820d1f08f22c](../../evidence/conditions-sets-065.md#c-a947820d1f08f22c) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-072947

```text
(config-line)# default width <cr>
```

Handler ` RVA 0xE059390 `；selector ` 1 `；EOL ` RVA 0x34129768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b568d7f03044fdc5](../../evidence/conditions-sets-070.md#c-b568d7f03044fdc5) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073079

```text
(config-line)# default x25 address <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 33 `；EOL ` RVA 0x34901F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-637c4663d3b728c9](../../evidence/conditions-sets-039.md#c-637c4663d3b728c9) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073061

```text
(config-line)# default x25 subaddress <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 30 `；EOL ` RVA 0x349011C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5845908ab4b79696](../../evidence/conditions-sets-035.md#c-5845908ab4b79696) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073140

```text
(config-line)# default x25 subscribe cug-service <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 26 `；EOL ` RVA 0x34901688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073147

```text
(config-line)# default x25 subscribe local-cug <number:0..9999> <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 27 `；EOL ` RVA 0x34901A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Local CUG number。

[条件 C-b310933ca03f6ac4](../../evidence/conditions-sets-069.md#c-b310933ca03f6ac4) · [参数 P-a7965f83f7539f64](../../evidence/parameters-sets-013.md#p-a7965f83f7539f64) · [状态效果 S-f763653a3c8617be](../../evidence/state_effects-sets-052.md#s-f763653a3c8617be)

### path-073150

```text
(config-line)# disconnect-character <?char_number_action@5555891b77e8> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 113 `；EOL ` RVA 0x33C63810 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e0675cb6ded69577](../../evidence/conditions-sets-086.md#c-e0675cb6ded69577) · [缺口 G-0b70c28933d0c71e](../../evidence/gaps-sets-001.md#g-0b70c28933d0c71e)

### path-073155

```text
(config-line)# dispatch-character <?char_number_action@5555891b63d0> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e86eba117fc2950](../../evidence/conditions-sets-061.md#c-9e86eba117fc2950) · [缺口 G-f124759da8a6a3e5](../../evidence/gaps-sets-008.md#g-f124759da8a6a3e5)

### path-072900

```text
(config-line)# dispatch-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1da0473f329610f9](../../evidence/conditions-sets-011.md#c-1da0473f329610f9)

### path-072963

```text
(config-line)# dispatch-machine <string> <cr>
```

Handler ` RVA 0xDE9D520 `；selector ` 0 `；EOL ` RVA 0x33C63168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a defined state machine。

[条件 C-fee5756eac6261c6](../../evidence/conditions-sets-098.md#c-fee5756eac6261c6) · [参数 P-f427b0e8f3194ab5](../../evidence/parameters-sets-018.md#p-f427b0e8f3194ab5)

### path-072865

```text
(config-line)# dispatch-timeout <number:0..4294967294> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 114 `；EOL ` RVA 0x33C61B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dispatch timer in milliseconds。

[条件 C-0816b1534410391f](../../evidence/conditions-sets-004.md#c-0816b1534410391f) · [参数 P-8d68e5fe16a5b7d4](../../evidence/parameters-sets-011.md#p-8d68e5fe16a5b7d4)

### path-072876

```text
(config-line)# domain-lookup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 2 `；EOL ` RVA 0x34128800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072871

```text
(config-line)# download <cr>
```

Handler ` RVA 0xE05E330 `；selector ` 138 `；EOL ` RVA 0x3417D940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-69fe14440175699b](../../evidence/conditions-sets-041.md#c-69fe14440175699b)

### path-072882

```text
(config-line)# editing <cr>
```

Handler ` RVA 0xE059390 `；selector ` 137 `；EOL ` RVA 0x3412A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-073153

```text
(config-line)# escape-character <?char_number_action@5555896b4d68> <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 5 `；EOL ` RVA 0x341607F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7c7aa9b81c9b4292](../../evidence/conditions-sets-048.md#c-7c7aa9b81c9b4292) · [缺口 G-7143d6067714f959](../../evidence/gaps-sets-004.md#g-7143d6067714f959)

### path-072987

```text
(config-line)# escape-character BREAK <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 30 `；EOL ` RVA 0x34160818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e2ddd2e18db5eaf](../../evidence/conditions-sets-037.md#c-5e2ddd2e18db5eaf)

### path-073015

```text
(config-line)# escape-character DEFAULT <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 32 `；EOL ` RVA 0x34160DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c5675fbbc050563](../../evidence/conditions-sets-036.md#c-5c5675fbbc050563)

### path-072998

```text
(config-line)# escape-character NONE <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 31 `；EOL ` RVA 0x34160AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e2ddd2e18db5eaf](../../evidence/conditions-sets-037.md#c-5e2ddd2e18db5eaf)

### path-072878

```text
(config-line)# exec <cr>
```

Handler ` RVA 0xE059390 `；selector ` 125 `；EOL ` RVA 0x34129088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e4cd11f0371c2bbd](../../evidence/conditions-sets-088.md#c-e4cd11f0371c2bbd)

### path-073054

```text
(config-line)# exec prompt expand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 40 `；EOL ` RVA 0x34128B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-073056

```text
(config-line)# exec prompt timestamp <cr>
```

Handler ` RVA 0xE059390 `；selector ` 38 `；EOL ` RVA 0x34128DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072872

```text
(config-line)# exec-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 11 `；EOL ` RVA 0x3412B998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4)

### path-072926

```text
(config-line)# exec-character-bits <number:7..8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 134 `；EOL ` RVA 0x34128270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bits per character。

[条件 C-d3fdc89b075a0519](../../evidence/conditions-sets-082.md#c-d3fdc89b075a0519) · [参数 P-3949f6c3536b8f7d](../../evidence/parameters-sets-005.md#p-3949f6c3536b8f7d)

### path-072936

```text
(config-line)# exec-timeout <number:0..35791> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 13 `；EOL ` RVA 0x3412BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in minutes。

[条件 C-5230b4a00fcb5bfd](../../evidence/conditions-sets-032.md#c-5230b4a00fcb5bfd) · [参数 P-ebd74b1ab9d8708f](../../evidence/parameters-sets-018.md#p-ebd74b1ab9d8708f)

### path-072880

```text
(config-line)# exit <cr>
```

Handler ` RVA 0xE059390 `；selector ` 14 `；EOL ` RVA 0x3412C3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00b6117321e9310f](../../evidence/conditions-sets-001.md#c-00b6117321e9310f)

### path-073158

```text
(config-line)# flowcontrol <?test_line_action@5555896d7c70> <cr>
```

Handler ` RVA 0xE056390 `；selector ` 104 `；EOL ` RVA 0x34183DA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2a6ae2c5e754777d](../../evidence/conditions-sets-017.md#c-2a6ae2c5e754777d) · [缺口 G-e5d5fb9e0c7aff94](../../evidence/gaps-sets-008.md#g-e5d5fb9e0c7aff94) · [状态效果 S-254be1ef832f85e3](../../evidence/state_effects-sets-008.md#s-254be1ef832f85e3)

### path-073046

```text
(config-line)# flowcontrol software <cr>
```

Handler ` RVA 0xE056390 `；selector ` 104 `；EOL ` RVA 0x34183DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5b4d6e13e59d582b](../../evidence/conditions-sets-036.md#c-5b4d6e13e59d582b) · [状态效果 S-ba7853ccb89fbc4b](../../evidence/state_effects-sets-039.md#s-ba7853ccb89fbc4b)

### path-072888

```text
(config-line)# flush-at-activation <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 164 `；EOL ` RVA 0x33C62DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4)

### path-072887

```text
(config-line)# full-help <cr>
```

Handler ` RVA 0xE059390 `；selector ` 139 `；EOL ` RVA 0x3412A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072891

```text
(config-line)# help <cr>
```

Handler ` RVA 0xE006150 `；selector ` 0 `；EOL ` RVA 0x341667E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b0eb474247bd0b39](../../evidence/conditions-sets-068.md#c-b0eb474247bd0b39)

### path-072883

```text
(config-line)# history <cr>
```

Handler ` RVA 0xE059390 `；selector ` 135 `；EOL ` RVA 0x34129D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072881

```text
(config-line)# history size <number:0..256> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 136 `；EOL ` RVA 0x34129CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Size of history buffer。

[条件 C-a8418cda93a29141](../../evidence/conditions-sets-065.md#c-a8418cda93a29141) · [参数 P-4058fcc1fd27a275](../../evidence/parameters-sets-005.md#p-4058fcc1fd27a275)

### path-073154

```text
(config-line)# hold-character <?char_number_action@5555891b67f8> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 122 `；EOL ` RVA 0x33C62820 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4e87e7970defa5bc](../../evidence/conditions-sets-031.md#c-4e87e7970defa5bc) · [缺口 G-7f5f591a444010ab](../../evidence/gaps-sets-005.md#g-7f5f591a444010ab)

### path-072899

```text
(config-line)# insecure <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 22 `；EOL ` RVA 0x33C65158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4)

### path-072885

```text
(config-line)# international <cr>
```

Handler ` RVA 0xE059390 `；selector ` 36 `；EOL ` RVA 0x3412A4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-073083

```text
(config-line)# ip netmask-format hexadecimal <cr>
```

Handler ` RVA 0xE059390 `；selector ` 33 `；EOL ` RVA 0x33D406C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-36654188f3dfe35c](../../evidence/state_effects-sets-012.md#s-36654188f3dfe35c)

### path-072978

```text
(config-line)# ip tcp input-coalesce-threshold <number:5..255> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 35 `；EOL ` RVA 0x33D40A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of packets。

[条件 C-f55898f42e5e9d61](../../evidence/conditions-sets-095.md#c-f55898f42e5e9d61) · [参数 P-cdd49c8a2d98adbd](../../evidence/parameters-sets-016.md#p-cdd49c8a2d98adbd)

### path-073137

```text
(config-line)# ipv6 access-class <string> out <cr>
```

Handler ` RVA 0x12165730 `；selector ` 0 `；EOL ` RVA 0x357AFFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Access-list name。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [参数 P-2f4c08e17f96c869](../../evidence/parameters-sets-004.md#p-2f4c08e17f96c869) · [状态效果 S-bb6219a22fed8b7b](../../evidence/state_effects-sets-040.md#s-bb6219a22fed8b7b)

### path-073052

```text
(config-line)# ipv6 format scoped_help-string <cr>
```

Handler ` RVA 0x12321A90 `；selector ` 0 `；EOL ` RVA 0x3580DEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-69fe14440175699b](../../evidence/conditions-sets-041.md#c-69fe14440175699b) · [状态效果 S-dab6271009666073](../../evidence/state_effects-sets-046.md#s-dab6271009666073)

### path-072938

```text
(config-line)# length <number:0..512> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 0 `；EOL ` RVA 0x34129408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of lines on screen (0 for no pausing)。

[条件 C-0416f5650c1a3e8c](../../evidence/conditions-sets-002.md#c-0416f5650c1a3e8c) · [参数 P-fc4f04a544e9b33a](../../evidence/parameters-sets-019.md#p-fc4f04a544e9b33a)

### path-072914

```text
(config-line)# location <string> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 15 `；EOL ` RVA 0x3412AF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` One text line describing the terminal's location。

[条件 C-87afb2e71e693c3a](../../evidence/conditions-sets-052.md#c-87afb2e71e693c3a) · [参数 P-74f6b78c098130c7](../../evidence/parameters-sets-009.md#p-74f6b78c098130c7)

### path-072890

```text
(config-line)# lockable <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 116 `；EOL ` RVA 0x33C63AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4)

### path-072993

```text
(config-line)# logging synchronous <cr>
```

Handler ` RVA 0xE054FE0 `；selector ` 0 `；EOL ` RVA 0x3417DD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5caad2395aa00e7d](../../evidence/conditions-sets-036.md#c-5caad2395aa00e7d)

### path-072897

```text
(config-line)# login <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 16 `；EOL ` RVA 0x3417EA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d3d65af3294161d8](../../evidence/conditions-sets-082.md#c-d3d65af3294161d8) · [状态效果 S-4367e902d5fc3402](../../evidence/state_effects-sets-015.md#s-4367e902d5fc3402)

### path-073025

```text
(config-line)# login authentication <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 26 `；EOL ` RVA 0x3417E628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-de30e7f9144a7a66](../../evidence/conditions-sets-086.md#c-de30e7f9144a7a66)

### path-072979

```text
(config-line)# logout-warning <number:0..4294967295> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 141 `；EOL ` RVA 0x33C63E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Warning time in seconds。

[条件 C-004b5143d5b223ed](../../evidence/conditions-sets-001.md#c-004b5143d5b223ed) · [参数 P-5101106393dfce00](../../evidence/parameters-sets-007.md#p-5101106393dfce00)

### path-073110

```text
(config-line)# modem answer-timeout <number:0..65535> <cr>
```

Handler ` RVA 0xDE8F510 `；selector ` 0 `；EOL ` RVA 0x3417F1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Answer timeout in seconds。

[条件 C-b1f458bb2ecd4a56](../../evidence/conditions-sets-069.md#c-b1f458bb2ecd4a56) · [参数 P-d23cc53a18974e7c](../../evidence/parameters-sets-016.md#p-d23cc53a18974e7c) · [状态效果 S-16761376c77ef9d2](../../evidence/state_effects-sets-005.md#s-16761376c77ef9d2)

### path-073127

```text
(config-line)# modem autoconfigure discovery <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29f859009404c539](../../evidence/conditions-sets-016.md#c-29f859009404c539) · [状态效果 S-c3e12b036676d437](../../evidence/state_effects-sets-041.md#s-c3e12b036676d437)

### path-073143

```text
(config-line)# modem autoconfigure type <string> <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Modem type。

[条件 C-29f859009404c539](../../evidence/conditions-sets-016.md#c-29f859009404c539) · [参数 P-c7490d0afda9dc9a](../../evidence/parameters-sets-015.md#p-c7490d0afda9dc9a) · [状态效果 S-53e96261ef74368c](../../evidence/state_effects-sets-018.md#s-53e96261ef74368c)

### path-073047

```text
(config-line)# modem busyout <cr>
```

Handler ` RVA 0xFDCEDB0 `；selector ` 162 `；EOL ` RVA 0x348DBB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bc6eee7f1808dfdd](../../evidence/conditions-sets-073.md#c-bc6eee7f1808dfdd) · [状态效果 S-6ab801f516628643](../../evidence/state_effects-sets-023.md#s-6ab801f516628643)

### path-073014

```text
(config-line)# modem callin <cr>
```

Handler ` RVA 0xDE8F920 `；selector ` 105 `；EOL ` RVA 0x3417F7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-5dbad210cca02333](../../evidence/state_effects-sets-020.md#s-5dbad210cca02333)

### path-073117

```text
(config-line)# modem dtr-delay <number:0..65535> <cr>
```

Handler ` RVA 0xDE8F710 `；selector ` 0 `；EOL ` RVA 0x3417F528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DTR delay in seconds。

[条件 C-d02a7fcacab08ae1](../../evidence/conditions-sets-080.md#c-d02a7fcacab08ae1) · [参数 P-0e646398d88d40ee](../../evidence/parameters-sets-002.md#p-0e646398d88d40ee) · [状态效果 S-91091a68dc9d033c](../../evidence/state_effects-sets-031.md#s-91091a68dc9d033c)

### path-072889

```text
(config-line)# monitor <cr>
```

Handler ` RVA 0xE060540 `；selector ` 4 `；EOL ` RVA 0x3418FDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072873

```text
(config-line)# motd-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 12 `；EOL ` RVA 0x3412CA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c67f2357e8242152](../../evidence/conditions-sets-076.md#c-c67f2357e8242152)

### path-072983

```text
(config-line)# no absolute-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 140 `；EOL ` RVA 0x33C641B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-250c2d1fdf12393c](../../evidence/conditions-sets-014.md#c-250c2d1fdf12393c) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073055

```text
(config-line)# no access-class out <cr>
```

Handler ` RVA 0xE059390 `；selector ` 10 `；EOL ` RVA 0x3412B368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3553415c5bc395cc](../../evidence/conditions-sets-021.md#c-3553415c5bc395cc) · [状态效果 S-014a7f9d7374ae74](../../evidence/state_effects-sets-001.md#s-014a7f9d7374ae74)

### path-073099

```text
(config-line)# no accounting resource <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 28 `；EOL ` RVA 0x34181488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a57f8c3db4efd134](../../evidence/conditions-sets-064.md#c-a57f8c3db4efd134) · [状态效果 S-6a023977e436a4f5](../../evidence/state_effects-sets-023.md#s-6a023977e436a4f5)

### path-072961

```text
(config-line)# no activation-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 110 `；EOL ` RVA 0x33C634C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-efbe44e7ae6acf70](../../evidence/conditions-sets-093.md#c-efbe44e7ae6acf70) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073091

```text
(config-line)# no authorization reverse-access <cr>
```

Handler ` RVA 0xE056B50 `；selector ` 27 `；EOL ` RVA 0x34180E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4961cba47e5aee46](../../evidence/conditions-sets-029.md#c-4961cba47e5aee46) · [状态效果 S-792671e87eac7485](../../evidence/state_effects-sets-026.md#s-792671e87eac7485)

### path-072972

```text
(config-line)# no autobaud <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 106 `；EOL ` RVA 0x33C654B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1d19d0d1a44fb0d8](../../evidence/conditions-sets-011.md#c-1d19d0d1a44fb0d8) · [状态效果 S-020902f455d4f215](../../evidence/state_effects-sets-001.md#s-020902f455d4f215)

### path-073023

```text
(config-line)# no autocommand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 130 `；EOL ` RVA 0x34180340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cc3b28730f5a165](../../evidence/conditions-sets-018.md#c-2cc3b28730f5a165) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073031

```text
(config-line)# no autocommand-options <cr>
```

Handler ` RVA 0xE059390 `；selector ` 144 `；EOL ` RVA 0x34180720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-919a3aae8674e42b](../../evidence/conditions-sets-056.md#c-919a3aae8674e42b) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072980

```text
(config-line)# no autohangup <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 111 `；EOL ` RVA 0x33C61BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073085

```text
(config-line)# no autohangup session-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 165 `；EOL ` RVA 0x33C61B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072990

```text
(config-line)# no autohost <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 131 `；EOL ` RVA 0x33C64500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f81ef50f16593f11](../../evidence/conditions-sets-096.md#c-f81ef50f16593f11) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073010

```text
(config-line)# no autoselect <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 143 `；EOL ` RVA 0x33C611E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073067

```text
(config-line)# no autoselect arap <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 142 `；EOL ` RVA 0x33C60DC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-cc3120249ea7384d](../../evidence/state_effects-sets-043.md#s-cc3120249ea7384d)

### path-072884

```text
(config-line)# no buffer-length <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 146 `；EOL ` RVA 0x33C62AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4d9a28b405e0e965](../../evidence/conditions-sets-030.md#c-4d9a28b405e0e965) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072868

```text
(config-line)# no data-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 132 `；EOL ` RVA 0x34127948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0a9ce9d6b7bedb05](../../evidence/conditions-sets-004.md#c-0a9ce9d6b7bedb05) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073024

```text
(config-line)# no databits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 102 `；EOL ` RVA 0x34181EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b3ab8e8544785280](../../evidence/conditions-sets-069.md#c-b3ab8e8544785280) · [状态效果 S-d4331dace4f3f47e](../../evidence/state_effects-sets-045.md#s-d4331dace4f3f47e)

### path-072967

```text
(config-line)# no disconnect-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 113 `；EOL ` RVA 0x33C63810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ef15109ee7e0796a](../../evidence/conditions-sets-092.md#c-ef15109ee7e0796a) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073007

```text
(config-line)# no dispatch-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 121 `；EOL ` RVA 0x33C624E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-1da0473f329610f9](../../evidence/conditions-sets-011.md#c-1da0473f329610f9) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072962

```text
(config-line)# no dispatch-machine <cr>
```

Handler ` RVA 0xDE9D520 `；selector ` 0 `；EOL ` RVA 0x33C63168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3bbdf4a5b1d425e6](../../evidence/conditions-sets-023.md#c-3bbdf4a5b1d425e6) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072893

```text
(config-line)# no dispatch-timeout <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 114 `；EOL ` RVA 0x33C61B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-61641745abe373dd](../../evidence/conditions-sets-038.md#c-61641745abe373dd) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072927

```text
(config-line)# no domain-lookup <cr>
```

Handler ` RVA 0xE059390 `；selector ` 2 `；EOL ` RVA 0x34128800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072915

```text
(config-line)# no download <cr>
```

Handler ` RVA 0xE05E330 `；selector ` 138 `；EOL ` RVA 0x3417D940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-69fe14440175699b](../../evidence/conditions-sets-041.md#c-69fe14440175699b) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072945

```text
(config-line)# no editing <cr>
```

Handler ` RVA 0xE059390 `；selector ` 137 `；EOL ` RVA 0x3412A1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072984

```text
(config-line)# no escape-character <cr>
```

Handler ` RVA 0xDFE2380 `；selector ` 5 `；EOL ` RVA 0x341607F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5d831859ada70e3a](../../evidence/conditions-sets-036.md#c-5d831859ada70e3a) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072934

```text
(config-line)# no exec <cr>
```

Handler ` RVA 0xE059390 `；selector ` 125 `；EOL ` RVA 0x34129088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e4cd11f0371c2bbd](../../evidence/conditions-sets-088.md#c-e4cd11f0371c2bbd) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073130

```text
(config-line)# no exec prompt expand <cr>
```

Handler ` RVA 0xE059390 `；selector ` 40 `；EOL ` RVA 0x34128B48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073132

```text
(config-line)# no exec prompt timestamp <cr>
```

Handler ` RVA 0xE059390 `；selector ` 38 `；EOL ` RVA 0x34128DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072916

```text
(config-line)# no exec-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 11 `；EOL ` RVA 0x3412B998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072925

```text
(config-line)# no exec-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 134 `；EOL ` RVA 0x34128270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2bd390d23f924aed](../../evidence/conditions-sets-017.md#c-2bd390d23f924aed) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072931

```text
(config-line)# no exec-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 13 `；EOL ` RVA 0x3412BD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-15418e20e5b42501](../../evidence/conditions-sets-008.md#c-15418e20e5b42501) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073121

```text
(config-line)# no flowcontrol software <cr>
```

Handler ` RVA 0xE056390 `；selector ` 104 `；EOL ` RVA 0x34183DA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5b4d6e13e59d582b](../../evidence/conditions-sets-036.md#c-5b4d6e13e59d582b) · [状态效果 S-cb2e74531131ade4](../../evidence/state_effects-sets-043.md#s-cb2e74531131ade4)

### path-072954

```text
(config-line)# no flush-at-activation <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 164 `；EOL ` RVA 0x33C62DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072953

```text
(config-line)# no full-help <cr>
```

Handler ` RVA 0xE059390 `；selector ` 139 `；EOL ` RVA 0x3412A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072946

```text
(config-line)# no history <cr>
```

Handler ` RVA 0xE059390 `；selector ` 135 `；EOL ` RVA 0x34129D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072940

```text
(config-line)# no history size <cr>
```

Handler ` RVA 0xE059390 `；selector ` 136 `；EOL ` RVA 0x34129CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b2122c1cc0d973b6](../../evidence/conditions-sets-069.md#c-b2122c1cc0d973b6) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073021

```text
(config-line)# no hold-character <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 122 `；EOL ` RVA 0x33C62820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d3bdb4d3e2a4be12](../../evidence/conditions-sets-082.md#c-d3bdb4d3e2a4be12) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073005

```text
(config-line)# no insecure <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 22 `；EOL ` RVA 0x33C65158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072950

```text
(config-line)# no international <cr>
```

Handler ` RVA 0xE059390 `；selector ` 36 `；EOL ` RVA 0x3412A4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073139

```text
(config-line)# no ip netmask-format hexadecimal <cr>
```

Handler ` RVA 0xE059390 `；selector ` 33 `；EOL ` RVA 0x33D406C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-a4d354bad6df3c24](../../evidence/state_effects-sets-035.md#s-a4d354bad6df3c24)

### path-073086

```text
(config-line)# no ip tcp input-coalesce-threshold <cr>
```

Handler ` RVA 0xE059390 `；selector ` 35 `；EOL ` RVA 0x33D40A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-13bb3cc59bb39fd5](../../evidence/conditions-sets-008.md#c-13bb3cc59bb39fd5) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073144

```text
(config-line)# no ipv6 access-class <string> out <cr>
```

Handler ` RVA 0x12165730 `；selector ` 0 `；EOL ` RVA 0x357AFFD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Access-list name。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [参数 P-2f4c08e17f96c869](../../evidence/parameters-sets-004.md#p-2f4c08e17f96c869) · [状态效果 S-d4de13f9405586d6](../../evidence/state_effects-sets-045.md#s-d4de13f9405586d6)

### path-073128

```text
(config-line)# no ipv6 format scoped_help-string <cr>
```

Handler ` RVA 0x12321A90 `；selector ` 0 `；EOL ` RVA 0x3580DEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-69fe14440175699b](../../evidence/conditions-sets-041.md#c-69fe14440175699b) · [状态效果 S-84c145165a35c00a](../../evidence/state_effects-sets-028.md#s-84c145165a35c00a)

### path-072942

```text
(config-line)# no length <cr>
```

Handler ` RVA 0xE059390 `；selector ` 0 `；EOL ` RVA 0x34129408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ebf4e4f51a8ee46b](../../evidence/conditions-sets-091.md#c-ebf4e4f51a8ee46b) · [状态效果 S-a3a479d9037fc573](../../evidence/state_effects-sets-035.md#s-a3a479d9037fc573)

### path-072912

```text
(config-line)# no location <cr>
```

Handler ` RVA 0xE059390 `；selector ` 15 `；EOL ` RVA 0x3412AF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2e28eab0c0cbc189](../../evidence/conditions-sets-018.md#c-2e28eab0c0cbc189) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072964

```text
(config-line)# no lockable <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 116 `；EOL ` RVA 0x33C63AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073077

```text
(config-line)# no logging synchronous <cr>
```

Handler ` RVA 0xE054FE0 `；selector ` 0 `；EOL ` RVA 0x3417DD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9b4b2c61139daff3](../../evidence/conditions-sets-060.md#c-9b4b2c61139daff3) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072992

```text
(config-line)# no login <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 16 `；EOL ` RVA 0x3417EA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d3d65af3294161d8](../../evidence/conditions-sets-082.md#c-d3d65af3294161d8) · [状态效果 S-d7fef5542c41f338](../../evidence/state_effects-sets-046.md#s-d7fef5542c41f338)

### path-073102

```text
(config-line)# no login authentication <cr>
```

Handler ` RVA 0xE0541F0 `；selector ` 26 `；EOL ` RVA 0x3417E628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0bac87eef3de0417](../../evidence/conditions-sets-005.md#c-0bac87eef3de0417) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072975

```text
(config-line)# no logout-warning <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 141 `；EOL ` RVA 0x33C63E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4acedebceaf3b1de](../../evidence/conditions-sets-029.md#c-4acedebceaf3b1de) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073115

```text
(config-line)# no modem answer-timeout <cr>
```

Handler ` RVA 0xDE8F510 `；selector ` 0 `；EOL ` RVA 0x3417F1B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2ea2a232078d944d](../../evidence/conditions-sets-018.md#c-2ea2a232078d944d) · [状态效果 S-4b94464f6534ff88](../../evidence/state_effects-sets-017.md#s-4b94464f6534ff88)

### path-073125

```text
(config-line)# no modem autoconfigure <cr>
```

Handler ` RVA 0xFDCE990 `；selector ` 161 `；EOL ` RVA 0x348DB820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e98aeb52723ed779](../../evidence/conditions-sets-090.md#c-e98aeb52723ed779) · [状态效果 S-791ff2b81993c50d](../../evidence/state_effects-sets-026.md#s-791ff2b81993c50d)

### path-073122

```text
(config-line)# no modem busyout <cr>
```

Handler ` RVA 0xFDCEDB0 `；selector ` 162 `；EOL ` RVA 0x348DBB78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-bc6eee7f1808dfdd](../../evidence/conditions-sets-073.md#c-bc6eee7f1808dfdd) · [状态效果 S-791ff2b81993c50d](../../evidence/state_effects-sets-026.md#s-791ff2b81993c50d)

### path-073112

```text
(config-line)# no modem callin <cr>
```

Handler ` RVA 0xDE8F920 `；selector ` 105 `；EOL ` RVA 0x3417F7E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-8acaa70248397a26](../../evidence/state_effects-sets-029.md#s-8acaa70248397a26)

### path-073113

```text
(config-line)# no modem dtr-delay <cr>
```

Handler ` RVA 0xDE8F710 `；selector ` 0 `；EOL ` RVA 0x3417F528 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c1d042dc557d6a1d](../../evidence/conditions-sets-075.md#c-c1d042dc557d6a1d) · [状态效果 S-355e87bd73bd065f](../../evidence/state_effects-sets-012.md#s-355e87bd73bd065f)

### path-072959

```text
(config-line)# no monitor <cr>
```

Handler ` RVA 0xE060540 `；selector ` 4 `；EOL ` RVA 0x3418FDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072917

```text
(config-line)# no motd-banner <cr>
```

Handler ` RVA 0xE059390 `；selector ` 12 `；EOL ` RVA 0x3412CA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c67f2357e8242152](../../evidence/conditions-sets-076.md#c-c67f2357e8242152) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072935

```text
(config-line)# no notify <cr>
```

Handler ` RVA 0xE059390 `；selector ` 7 `；EOL ` RVA 0x341299F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073072

```text
(config-line)# no ntp pps-discipline <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 1 `；EOL ` RVA 0x348FB6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2afef67df8c0059d](../../evidence/conditions-sets-017.md#c-2afef67df8c0059d) · [状态效果 S-c8cb38a69d7aa8b7](../../evidence/state_effects-sets-043.md#s-c8cb38a69d7aa8b7)

### path-073058

```text
(config-line)# no ntp refclock <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 0 `；EOL ` RVA 0x348FA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-08fb3df35fe03c11](../../evidence/conditions-sets-004.md#c-08fb3df35fe03c11) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073022

```text
(config-line)# no parity <cr>
```

Handler ` RVA 0xE059390 `；selector ` 101 `；EOL ` RVA 0x34182320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-7136fe00f7752427](../../evidence/conditions-sets-044.md#c-7136fe00f7752427) · [状态效果 S-da330ca9925768e0](../../evidence/state_effects-sets-046.md#s-da330ca9925768e0)

### path-072955

```text
(config-line)# no password <cr>
```

Handler ` RVA 0xDDD7F60 `；selector ` 18 `；EOL ` RVA 0x34198A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d539742e929f8743](../../evidence/conditions-sets-082.md#c-d539742e929f8743) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073048

```text
(config-line)# no prc expose <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 0 `；EOL ` RVA 0x341279C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073050

```text
(config-line)# no prc hide <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 1 `；EOL ` RVA 0x34127C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072999

```text
(config-line)# no private <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 115 `；EOL ` RVA 0x33C64EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072929

```text
(config-line)# no privilege level <cr>
```

Handler ` RVA 0xE059390 `；selector ` 160 `；EOL ` RVA 0x3412C040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-29ab2d22fe13705f](../../evidence/conditions-sets-016.md#c-29ab2d22fe13705f) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072991

```text
(config-line)# no refuse-message <cr>
```

Handler ` RVA 0xE055DF0 `；selector ` 19 `；EOL ` RVA 0x3417EDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f666857d1cd231bb](../../evidence/conditions-sets-095.md#c-f666857d1cd231bb) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073009

```text
(config-line)# no rotary <cr>
```

Handler ` RVA 0xE059390 `；selector ` 109 `；EOL ` RVA 0x3417FEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-624afe2c57f9acc3](../../evidence/conditions-sets-038.md#c-624afe2c57f9acc3) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072902

```text
(config-line)# no rxspeed <cr>
```

Handler ` RVA 0xE0552E0 `；selector ` 119 `；EOL ` RVA 0x34183280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-55e2747835787742](../../evidence/conditions-sets-034.md#c-55e2747835787742) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073090

```text
(config-line)# no script activation <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 155 `；EOL ` RVA 0x346027E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-364c5d95cdb284e8](../../evidence/conditions-sets-021.md#c-364c5d95cdb284e8) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073104

```text
(config-line)# no script arap-callback <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 158 `；EOL ` RVA 0x34602E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a92914311c9275df](../../evidence/conditions-sets-065.md#c-a92914311c9275df) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073109

```text
(config-line)# no script callback <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 157 `；EOL ` RVA 0x34603190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4c51e7c9437beae1](../../evidence/conditions-sets-030.md#c-4c51e7c9437beae1) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073066

```text
(config-line)# no script connection <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 152 `；EOL ` RVA 0x34601E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9e8e2e03b6bd2a86](../../evidence/conditions-sets-061.md#c-9e8e2e03b6bd2a86) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073070

```text
(config-line)# no script dialer <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 154 `；EOL ` RVA 0x34602150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-336bd6780fb22319](../../evidence/conditions-sets-020.md#c-336bd6780fb22319) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073097

```text
(config-line)# no script modem-off-hook <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 159 `；EOL ` RVA 0x34602B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b686977ef6ea8238](../../evidence/conditions-sets-071.md#c-b686977ef6ea8238) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073080

```text
(config-line)# no script reset <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 153 `；EOL ` RVA 0x34602498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a78d367ce091731a](../../evidence/conditions-sets-065.md#c-a78d367ce091731a) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073062

```text
(config-line)# no script startup <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 151 `；EOL ` RVA 0x34601AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-4f6fe91b2afc9508](../../evidence/conditions-sets-031.md#c-4f6fe91b2afc9508) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073002

```text
(config-line)# no session-disconnect-warning <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 34 `；EOL ` RVA 0x33C64848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-56e58f5f0c162e5a](../../evidence/conditions-sets-034.md#c-56e58f5f0c162e5a) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073008

```text
(config-line)# no session-limit <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 24 `；EOL ` RVA 0x33C64C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-89901693a91aa75b](../../evidence/conditions-sets-053.md#c-89901693a91aa75b) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072907

```text
(config-line)# no session-timeout <cr>
```

Handler ` RVA 0xE059390 `；selector ` 117 `；EOL ` RVA 0x3412ABB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-af3f9d3cf6c14d46](../../evidence/conditions-sets-068.md#c-af3f9d3cf6c14d46) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072919

```text
(config-line)# no shell <cr>
```

Handler ` RVA 0xE059390 `；selector ` 39 `；EOL ` RVA 0x340B9858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2cf532477d6301dd](../../evidence/conditions-sets-018.md#c-2cf532477d6301dd) · [状态效果 S-d159f53adcfd91a6](../../evidence/state_effects-sets-044.md#s-d159f53adcfd91a6)

### path-072870

```text
(config-line)# no special-character-bits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 133 `；EOL ` RVA 0x341281C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-829c2bf5996abb15](../../evidence/conditions-sets-051.md#c-829c2bf5996abb15) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073042

```text
(config-line)# no speed <cr>
```

Handler ` RVA 0xE055B70 `；selector ` 118 `；EOL ` RVA 0x34183320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b97111180680add6](../../evidence/conditions-sets-072.md#c-b97111180680add6) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073036

```text
(config-line)# no start-character <cr>
```

Handler ` RVA 0xE059390 `；selector ` 108 `；EOL ` RVA 0x34182C80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-848c11f54177b9f9](../../evidence/conditions-sets-051.md#c-848c11f54177b9f9) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073039

```text
(config-line)# no stop-character <cr>
```

Handler ` RVA 0xE059390 `；selector ` 107 `；EOL ` RVA 0x34182FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-00cf601567f19a5f](../../evidence/conditions-sets-001.md#c-00cf601567f19a5f) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073030

```text
(config-line)# no stopbits <cr>
```

Handler ` RVA 0xE059390 `；selector ` 25 `；EOL ` RVA 0x34182808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a0494e25c03fd5e1](../../evidence/conditions-sets-062.md#c-a0494e25c03fd5e1) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073074

```text
(config-line)# no telnet break-on-ip <cr>
```

Handler ` RVA 0xCCF24C0 `；selector ` 100 `；EOL ` RVA 0x33C615A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-49f29e3c985250ab](../../evidence/state_effects-sets-016.md#s-49f29e3c985250ab)

### path-072906

```text
(config-line)# no terminal-type <cr>
```

Handler ` RVA 0xE059390 `；selector ` 126 `；EOL ` RVA 0x341276A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f68d9298398a706c](../../evidence/conditions-sets-095.md#c-f68d9298398a706c) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073134

```text
(config-line)# no timeout login response <cr>
```

Handler ` RVA 0xE059390 `；selector ` 37 `；EOL ` RVA 0x3412C788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8035a9333136c1e1](../../evidence/conditions-sets-050.md#c-8035a9333136c1e1) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072985

```text
(config-line)# no transport <cr>
```

Handler ` RVA 0xDE835F0 `；selector ` 124 `；EOL ` RVA 0x34188630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0640441ccdc5d0f8](../../evidence/conditions-sets-003.md#c-0640441ccdc5d0f8) · [状态效果 S-351eae5b0d03f8d2](../../evidence/state_effects-sets-012.md#s-351eae5b0d03f8d2)

### path-072904

```text
(config-line)# no txspeed <cr>
```

Handler ` RVA 0xE055A00 `；selector ` 120 `；EOL ` RVA 0x34183688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-2a9ca4e00b5ffca0](../../evidence/conditions-sets-017.md#c-2a9ca4e00b5ffca0) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072976

```text
(config-line)# no vacant-message <cr>
```

Handler ` RVA 0xE053ED0 `；selector ` 20 `；EOL ` RVA 0x3417E200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-9b2f8bc706b08666](../../evidence/conditions-sets-060.md#c-9b2f8bc706b08666) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072941

```text
(config-line)# no width <cr>
```

Handler ` RVA 0xE059390 `；selector ` 1 `；EOL ` RVA 0x34129768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ae21f259ddffc630](../../evidence/conditions-sets-067.md#c-ae21f259ddffc630) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073071

```text
(config-line)# no x25 address <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 33 `；EOL ` RVA 0x34901F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0c6ee4b232639325](../../evidence/conditions-sets-005.md#c-0c6ee4b232639325) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073060

```text
(config-line)# no x25 subaddress <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 30 `；EOL ` RVA 0x349011C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-dd58bd8551d41ad6](../../evidence/conditions-sets-085.md#c-dd58bd8551d41ad6) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073138

```text
(config-line)# no x25 subscribe cug-service <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 26 `；EOL ` RVA 0x34901688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-073145

```text
(config-line)# no x25 subscribe local-cug <number:0..9999> <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 27 `；EOL ` RVA 0x34901A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Local CUG number。

[条件 C-faa3c0c8e023018d](../../evidence/conditions-sets-097.md#c-faa3c0c8e023018d) · [参数 P-a7965f83f7539f64](../../evidence/parameters-sets-013.md#p-a7965f83f7539f64) · [状态效果 S-030a5da5c0451d32](../../evidence/state_effects-sets-001.md#s-030a5da5c0451d32)

### path-072879

```text
(config-line)# notify <cr>
```

Handler ` RVA 0xE059390 `；selector ` 7 `；EOL ` RVA 0x341299F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-073116

```text
(config-line)# ntp pps-discipline dcd <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 1 `；EOL ` RVA 0x348FB6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9c6311bdc13bd841](../../evidence/conditions-sets-060.md#c-9c6311bdc13bd841) · [状态效果 S-c650ecd607527209](../../evidence/state_effects-sets-042.md#s-c650ecd607527209)

### path-073142

```text
(config-line)# ntp refclock pps none <cr>
```

Handler ` RVA 0xFE52A70 `；selector ` 0 `；EOL ` RVA 0x348FA9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b3f72fe0c4cf28cf](../../evidence/conditions-sets-070.md#c-b3f72fe0c4cf28cf) · [状态效果 S-dbd7f8acc190accc](../../evidence/state_effects-sets-047.md#s-dbd7f8acc190accc)

### path-073152

```text
(config-line)# padding <?char_number_action@5555896d59f8> <cr>
```

Handler ` RVA 0xE054AA0 `；selector ` 3 `；EOL ` RVA 0x34181AC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a0030aec3900514b](../../evidence/conditions-sets-062.md#c-a0030aec3900514b) · [缺口 G-03aaa77df332af87](../../evidence/gaps-sets-001.md#g-03aaa77df332af87)

### path-073011

```text
(config-line)# parity none <cr>
```

Handler ` RVA 0xE059390 `；selector ` 101 `；EOL ` RVA 0x34182320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46d4f08a1a0eb4fd](../../evidence/conditions-sets-028.md#c-46d4f08a1a0eb4fd) · [状态效果 S-cbdcebc0ad7dbf9c](../../evidence/state_effects-sets-043.md#s-cbdcebc0ad7dbf9c)

### path-072971

```text
(config-line)# password <string> <cr>
```

Handler ` RVA 0xDDD7F60 `；selector ` 18 `；EOL ` RVA 0x34198A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED (cleartext) line password。

[条件 C-abfa7f2b29df9bee](../../evidence/conditions-sets-066.md#c-abfa7f2b29df9bee) · [参数 P-1f399906027677a2](../../evidence/parameters-sets-003.md#p-1f399906027677a2)

### path-072908

```text
(config-line)# prc expose <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 0 `；EOL ` RVA 0x341279C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072913

```text
(config-line)# prc hide <cr>
```

Handler ` RVA 0xDEE2F90 `；selector ` 1 `；EOL ` RVA 0x34127C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### path-072898

```text
(config-line)# private <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 115 `；EOL ` RVA 0x33C64EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4)

### path-072877

```text
(config-line)# privilege level <number:0..15> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 160 `；EOL ` RVA 0x3412C040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Default privilege level for line。

[条件 C-b8fbc31cf1a8369c](../../evidence/conditions-sets-071.md#c-b8fbc31cf1a8369c) · [参数 P-e0cad6771f113e3a](../../evidence/parameters-sets-017.md#p-e0cad6771f113e3a)

### path-072997

```text
(config-line)# refuse-message <string> <cr>
```

Handler ` RVA 0xE055DF0 `；selector ` 19 `；EOL ` RVA 0x3417EDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` c refuse-text c, where 'c' is a delimiting character。

[条件 C-2693169b76c2db9a](../../evidence/conditions-sets-015.md#c-2693169b76c2db9a) · [参数 P-f8350f315542bc2d](../../evidence/parameters-sets-019.md#p-f8350f315542bc2d)

### path-073040

```text
(config-line)# rotary <number:1..99> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 109 `；EOL ` RVA 0x3417FEA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rotary group to add line to。

[条件 C-76d301b7c4be9821](../../evidence/conditions-sets-046.md#c-76d301b7c4be9821) · [参数 P-ea5e818b1c24ba8c](../../evidence/parameters-sets-018.md#p-ea5e818b1c24ba8c)

### path-072866

```text
(config-line)# rxspeed <number:0..4294967295> <cr>
```

Handler ` RVA 0xE0552E0 `；selector ` 119 `；EOL ` RVA 0x34183280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Receive speed。

[条件 C-b4e0616ac025853b](../../evidence/conditions-sets-070.md#c-b4e0616ac025853b) · [参数 P-d60586d866c538ae](../../evidence/parameters-sets-016.md#p-d60586d866c538ae)

### path-073094

```text
(config-line)# script activation <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 155 `；EOL ` RVA 0x346027E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-caffd97163c233b0](../../evidence/conditions-sets-078.md#c-caffd97163c233b0) · [参数 P-d4d32b5ef2e6a364](../../evidence/parameters-sets-016.md#p-d4d32b5ef2e6a364)

### path-073106

```text
(config-line)# script arap-callback <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 158 `；EOL ` RVA 0x34602E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-9f3dcbfa1c363e6e](../../evidence/conditions-sets-062.md#c-9f3dcbfa1c363e6e) · [参数 P-36036d37a07627f5](../../evidence/parameters-sets-005.md#p-36036d37a07627f5)

### path-073111

```text
(config-line)# script callback <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 157 `；EOL ` RVA 0x34603190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-dd280c5bdc992be4](../../evidence/conditions-sets-085.md#c-dd280c5bdc992be4) · [参数 P-87d9b8cfd2244241](../../evidence/parameters-sets-010.md#p-87d9b8cfd2244241)

### path-073068

```text
(config-line)# script connection <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 152 `；EOL ` RVA 0x34601E08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-15c76ee507dabffd](../../evidence/conditions-sets-009.md#c-15c76ee507dabffd) · [参数 P-25e3bd6860119a71](../../evidence/parameters-sets-003.md#p-25e3bd6860119a71)

### path-073075

```text
(config-line)# script dialer <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 154 `；EOL ` RVA 0x34602150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-79c80c39723460a7](../../evidence/conditions-sets-047.md#c-79c80c39723460a7) · [参数 P-ac2bae9790890e2c](../../evidence/parameters-sets-013.md#p-ac2bae9790890e2c)

### path-073100

```text
(config-line)# script modem-off-hook <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 159 `；EOL ` RVA 0x34602B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-7cd0fb68bd9c2abb](../../evidence/conditions-sets-048.md#c-7cd0fb68bd9c2abb) · [参数 P-ecb465d779f5bde7](../../evidence/parameters-sets-018.md#p-ecb465d779f5bde7)

### path-073087

```text
(config-line)# script reset <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 153 `；EOL ` RVA 0x34602498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-e23236ce456d9ccf](../../evidence/conditions-sets-087.md#c-e23236ce456d9ccf) · [参数 P-7cd9f1f00d906b6c](../../evidence/parameters-sets-010.md#p-7cd9f1f00d906b6c)

### path-073063

```text
(config-line)# script startup <string> <cr>
```

Handler ` RVA 0xF2F2BD0 `；selector ` 151 `；EOL ` RVA 0x34601AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` chat script name。

[条件 C-80cf795d0ebe4d16](../../evidence/conditions-sets-050.md#c-80cf795d0ebe4d16) · [参数 P-2b95cb621c74179d](../../evidence/parameters-sets-004.md#p-2b95cb621c74179d)

### path-073017

```text
(config-line)# session-disconnect-warning <number:0..4294967295> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 34 `；EOL ` RVA 0x33C64848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session timeout warning in seconds。

[条件 C-729dc3847b35d245](../../evidence/conditions-sets-044.md#c-729dc3847b35d245) · [参数 P-bb51cc97b2a1676f](../../evidence/parameters-sets-014.md#p-bb51cc97b2a1676f)

### path-073013

```text
(config-line)# session-limit <number:0..4294967295> <cr>
```

Handler ` RVA 0xCCF2840 `；selector ` 24 `；EOL ` RVA 0x33C64C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum number of sessions。

[条件 C-57600458e85410b8](../../evidence/conditions-sets-034.md#c-57600458e85410b8) · [参数 P-cb5751fb44c61fd8](../../evidence/parameters-sets-015.md#p-cb5751fb44c61fd8)

### path-072918

```text
(config-line)# session-timeout <number:0..35791> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 117 `；EOL ` RVA 0x3412ABB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session timeout interval in minutes。

[条件 C-c04372eb93658be1](../../evidence/conditions-sets-074.md#c-c04372eb93658be1) · [参数 P-be20710bead49358](../../evidence/parameters-sets-014.md#p-be20710bead49358)

### path-072874

```text
(config-line)# shell <cr>
```

Handler ` RVA 0xE059390 `；selector ` 39 `；EOL ` RVA 0x340B9858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cf532477d6301dd](../../evidence/conditions-sets-018.md#c-2cf532477d6301dd) · [状态效果 S-c50056ef22093884](../../evidence/state_effects-sets-042.md#s-c50056ef22093884)

### path-072863

```text
(config-line)# special-character-bits <number:7..8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 133 `；EOL ` RVA 0x341281C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bits per character。

[条件 C-52cfc3ee436b3ad5](../../evidence/conditions-sets-032.md#c-52cfc3ee436b3ad5) · [参数 P-78353eb85a082180](../../evidence/parameters-sets-009.md#p-78353eb85a082180)

### path-073045

```text
(config-line)# speed <number:0..4294967295> <cr>
```

Handler ` RVA 0xE055B70 `；selector ` 118 `；EOL ` RVA 0x34183320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Transmit and receive speeds。

[条件 C-5657defdc32777cb](../../evidence/conditions-sets-034.md#c-5657defdc32777cb) · [参数 P-ab5aebf82ee0e693](../../evidence/parameters-sets-013.md#p-ab5aebf82ee0e693)

### path-073156

```text
(config-line)# start-character <?char_number_action@5555896d6c58> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 108 `；EOL ` RVA 0x34182C80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5bd0d24b48f76abc](../../evidence/conditions-sets-036.md#c-5bd0d24b48f76abc) · [缺口 G-c2cb72385b470ee6](../../evidence/gaps-sets-007.md#g-c2cb72385b470ee6)

### path-073157

```text
(config-line)# stop-character <?char_number_action@5555896d6fa8> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 107 `；EOL ` RVA 0x34182FD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dfced84d601e19f9](../../evidence/conditions-sets-086.md#c-dfced84d601e19f9) · [缺口 G-148176d01f2481cd](../../evidence/gaps-sets-001.md#g-148176d01f2481cd)

### path-073033

```text
(config-line)# stopbits 1 <cr>
```

Handler ` RVA 0xE059390 `；selector ` 25 `；EOL ` RVA 0x34182808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2e3d1e07b984ffde](../../evidence/conditions-sets-018.md#c-2e3d1e07b984ffde) · [状态效果 S-64397803f64ed4cb](../../evidence/state_effects-sets-021.md#s-64397803f64ed4cb)

### path-072973

```text
(config-line)# telnet break-on-ip <cr>
```

Handler ` RVA 0xCCF24C0 `；selector ` 100 `；EOL ` RVA 0x33C615A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-3bb2cddfc2746e52](../../evidence/state_effects-sets-013.md#s-3bb2cddfc2746e52)

### path-072909

```text
(config-line)# terminal-type <string> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 126 `；EOL ` RVA 0x341276A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Terminal type。

[条件 C-fa70f2e1fa1059bf](../../evidence/conditions-sets-097.md#c-fa70f2e1fa1059bf) · [参数 P-f9e8ea2d9f973391](../../evidence/parameters-sets-019.md#p-f9e8ea2d9f973391)

### path-073135

```text
(config-line)# timeout login response <number:1..300> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 37 `；EOL ` RVA 0x3412C788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-bd6ec6ee6807ade5](../../evidence/conditions-sets-073.md#c-bd6ec6ee6807ade5) · [参数 P-eb260a50ee8ce0e9](../../evidence/parameters-sets-018.md#p-eb260a50ee8ce0e9)

### path-073151

```text
(config-line)# transport <?transport_action@5555896dc658> <cr>
```

Handler ` RVA 0xDE835F0 `；selector ` 124 `；EOL ` RVA 0x34188630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7ab9c09da39994a6](../../evidence/conditions-sets-048.md#c-7ab9c09da39994a6) · [缺口 G-2f983dc8c3821d16](../../evidence/gaps-sets-002.md#g-2f983dc8c3821d16) · [状态效果 S-d2437df9c3fb91ca](../../evidence/state_effects-sets-045.md#s-d2437df9c3fb91ca)

### path-072867

```text
(config-line)# txspeed <number:0..4294967295> <cr>
```

Handler ` RVA 0xE055A00 `；selector ` 120 `；EOL ` RVA 0x34183688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Transmit speed。

[条件 C-477d4f7c9779b904](../../evidence/conditions-sets-028.md#c-477d4f7c9779b904) · [参数 P-8729b8f400a47a34](../../evidence/parameters-sets-010.md#p-8729b8f400a47a34)

### path-072895

```text
(config-line)# vacant-message <cr>
```

Handler ` RVA 0xE053ED0 `；selector ` 20 `；EOL ` RVA 0x3417E200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a9f091a05ca238a3](../../evidence/conditions-sets-066.md#c-a9f091a05ca238a3)

### path-072943

```text
(config-line)# width <number:0..512> <cr>
```

Handler ` RVA 0xE059390 `；selector ` 1 `；EOL ` RVA 0x34129768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of characters on a screen line。

[条件 C-7ddcd128673a9132](../../evidence/conditions-sets-049.md#c-7ddcd128673a9132) · [参数 P-cd3849c8dacb9c67](../../evidence/parameters-sets-016.md#p-cd3849c8dacb9c67)

### path-073076

```text
(config-line)# x25 address <address> <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 33 `；EOL ` RVA 0x34901F20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` X.121 address。

[条件 C-943a92585b4692d4](../../evidence/conditions-sets-057.md#c-943a92585b4692d4) · [参数 P-d77b7dfe67ae32ea](../../evidence/parameters-sets-016.md#p-d77b7dfe67ae32ea)

### path-073064

```text
(config-line)# x25 subaddress line <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 30 `；EOL ` RVA 0x349011C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da7fab2d0d948a76](../../evidence/conditions-sets-084.md#c-da7fab2d0d948a76) · [状态效果 S-d3fe4fad89f2e88b](../../evidence/state_effects-sets-045.md#s-d3fe4fad89f2e88b)

### path-073081

```text
(config-line)# x25 subscribe cug-service <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 26 `；EOL ` RVA 0x34901688 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af01a72203743d4](../../evidence/conditions-sets-023.md#c-3af01a72203743d4)

### path-073148

```text
(config-line)# x25 subscribe local-cug <number:0..9999> network-cug <number:0..9999> <cr>
```

Handler ` RVA 0xFE728D0 `；selector ` 27 `；EOL ` RVA 0x34901A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Local CUG number；` unsigned_number ` Network CUG number。

[条件 C-dcad178e0d48499f](../../evidence/conditions-sets-085.md#c-dcad178e0d48499f) · [参数 P-89c39e0c723031cb](../../evidence/parameters-sets-011.md#p-89c39e0c723031cb)
