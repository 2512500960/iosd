# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-026397

```text
(config)# aaa accounting delay-start <cr>
```

Handler ` RVA 0xDD42010 `；selector ` 1 `；EOL ` RVA 0x3419FD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-40035e3c2d1b1012](../../evidence/conditions-sets-025.md#c-40035e3c2d1b1012) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-062745

```text
(config)# aaa accounting dot1x default <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 42 `；EOL ` RVA 0x341A3388 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c0d0d187ff63b10b](../../evidence/conditions-sets-074.md#c-c0d0d187ff63b10b) · [缺口 G-64bb94558b443569](../../evidence/gaps-sets-004.md#g-64bb94558b443569) · [状态效果 S-94d5663149fc03cc](../../evidence/state_effects-sets-032.md#s-94d5663149fc03cc)

### path-028424

```text
(config)# aaa accounting dot1x guarantee-first <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 52 `；EOL ` RVA 0x341A4410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d5f3ed96229dafe](../../evidence/conditions-sets-024.md#c-3d5f3ed96229dafe) · [状态效果 S-162a5bb0b88d4b5b](../../evidence/state_effects-sets-005.md#s-162a5bb0b88d4b5b)

### path-028423

```text
(config)# aaa accounting dot1x local <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 78 `；EOL ` RVA 0x341A40E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0c5cf52e587909f](../../evidence/conditions-sets-093.md#c-f0c5cf52e587909f) · [状态效果 S-162a5bb0b88d4b5b](../../evidence/state_effects-sets-005.md#s-162a5bb0b88d4b5b)

### path-028387

```text
(config)# aaa accounting dot1x visible-keys <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 77 `；EOL ` RVA 0x341A3E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0c5cf52e587909f](../../evidence/conditions-sets-093.md#c-f0c5cf52e587909f) · [状态效果 S-162a5bb0b88d4b5b](../../evidence/state_effects-sets-005.md#s-162a5bb0b88d4b5b)

### path-026486

```text
(config)# aaa accounting gigawords <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 45 `；EOL ` RVA 0x341A0D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-034337

```text
(config)# aaa accounting include auth-profile framed-ip-address <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 58 `；EOL ` RVA 0x341A2128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-751ab6ab05b18373](../../evidence/conditions-sets-045.md#c-751ab6ab05b18373) · [状态效果 S-a389c1dbc07ceac8](../../evidence/state_effects-sets-035.md#s-a389c1dbc07ceac8)

### path-034276

```text
(config)# aaa accounting jitter maximum <number:0..2147483> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 50 `；EOL ` RVA 0x341A1778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum jitter value for periodic interval(in seconds), default is 300 seconds。

[条件 C-e8506b221c50f4cc](../../evidence/conditions-sets-090.md#c-e8506b221c50f4cc) · [参数 P-51d96bccf6fed32b](../../evidence/parameters-sets-007.md#p-51d96bccf6fed32b) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-026516

```text
(config)# aaa accounting nested <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 51 `；EOL ` RVA 0x341A0A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-028470

```text
(config)# aaa accounting redundancy new-session <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 47 `；EOL ` RVA 0x341A1388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-7ed7789f31a6f027](../../evidence/state_effects-sets-027.md#s-7ed7789f31a6f027)

### path-034467

```text
(config)# aaa accounting redundancy suppress system-records <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 49 `；EOL ` RVA 0x341A10C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-034241

```text
(config)# aaa accounting send counters ipv6 <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 46 `；EOL ` RVA 0x3419F8F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a6f61dd0cc6d253](../../evidence/conditions-sets-054.md#c-8a6f61dd0cc6d253) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-034279

```text
(config)# aaa accounting send stop-record always <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 74 `；EOL ` RVA 0x3419F620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3af7dabdbb2a4835](../../evidence/conditions-sets-023.md#c-3af7dabdbb2a4835) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-044107

```text
(config)# aaa accounting send stop-record authentication failure <cr>
```

Handler ` RVA 0xDD42010 `；selector ` 2 `；EOL ` RVA 0x3419EF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ccf09763ed1de79](../../evidence/conditions-sets-042.md#c-6ccf09763ed1de79) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-052160

```text
(config)# aaa accounting send stop-record authentication success remote-server <cr>
```

Handler ` RVA 0xDD42010 `；selector ` 3 `；EOL ` RVA 0x3419F318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cee9cfa414babd5e](../../evidence/conditions-sets-080.md#c-cee9cfa414babd5e) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-028319

```text
(config)# aaa accounting session-duration ntp-adjusted <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 65 `；EOL ` RVA 0x341A0708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-034362

```text
(config)# aaa accounting suppress attributes vpdn-endpoints <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 44 `；EOL ` RVA 0x341A03F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-028289

```text
(config)# aaa accounting suppress null-username <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 43 `；EOL ` RVA 0x341A0110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-c53e9fc235420a6d](../../evidence/state_effects-sets-042.md#s-c53e9fc235420a6d)

### path-028337

```text
(config)# aaa accounting update newinfo <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 53 `；EOL ` RVA 0x341A1B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ce657ec8494f450](../../evidence/conditions-sets-048.md#c-7ce657ec8494f450) · [状态效果 S-5f0307c9b2911164](../../evidence/state_effects-sets-020.md#s-5f0307c9b2911164)

### path-043908

```text
(config)# aaa archives enable-data index <number:1..5> <string> <cr>
```

Handler ` RVA 0xDD198E0 `；selector ` 83 `；EOL ` RVA 0x3419CD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Index number；` string ` Archive Data content。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-3a6444ba6d1ad9fb](../../evidence/parameters-sets-005.md#p-3a6444ba6d1ad9fb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052044

```text
(config)# aaa archives user-data <string> index <number:1..5> <string> <cr>
```

Handler ` RVA 0xDD198E0 `；selector ` 82 `；EOL ` RVA 0x3419C988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AAA user name(max length 63, longer name will be truncated)；` unsigned_number ` Index number；` string ` Archive Data content。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-cc9087697fe17aac](../../evidence/parameters-sets-015.md#p-cc9087697fe17aac) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028088

```text
(config)# aaa attribute list <string> <cr>
```

Handler ` RVA 0xCD2E990 `；selector ` 16 `；EOL ` RVA 0x341B1A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name。

[条件 C-9b655c64430bb7a9](../../evidence/conditions-sets-060.md#c-9b655c64430bb7a9) · [参数 P-27a95c96116b782c](../../evidence/parameters-sets-003.md#p-27a95c96116b782c) · [状态效果 S-dba2c2cac0c9dc34](../../evidence/state_effects-sets-046.md#s-dba2c2cac0c9dc34)

### path-034274

```text
(config)# aaa authentication attempts login <number:1..25> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 29 `；EOL ` RVA 0x341A7AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify value for the number of attempts。

[条件 C-b115887852580738](../../evidence/conditions-sets-068.md#c-b115887852580738) · [参数 P-a291fbfe45c63f22](../../evidence/parameters-sets-012.md#p-a291fbfe45c63f22) · [状态效果 S-a3c9e1773af0c0ca](../../evidence/state_effects-sets-035.md#s-a3c9e1773af0c0ca)

### path-028293

```text
(config)# aaa authentication banner <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 27 `；EOL ` RVA 0x341A7E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` c message-text c, where 'c' is a delimiting character。

[条件 C-f74d74377f690332](../../evidence/conditions-sets-096.md#c-f74d74377f690332) · [参数 P-8fbb7cce3b106082](../../evidence/parameters-sets-011.md#p-8fbb7cce3b106082) · [状态效果 S-a3c9e1773af0c0ca](../../evidence/state_effects-sets-035.md#s-a3c9e1773af0c0ca)

### path-028326

```text
(config)# aaa authentication fail-message <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 26 `；EOL ` RVA 0x341A8180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` c message-text c, where 'c' is a delimiting character。

[条件 C-bb1ef03d1f822572](../../evidence/conditions-sets-072.md#c-bb1ef03d1f822572) · [参数 P-a4be2b3f26f53664](../../evidence/parameters-sets-013.md#p-a4be2b3f26f53664) · [状态效果 S-a3c9e1773af0c0ca](../../evidence/state_effects-sets-035.md#s-a3c9e1773af0c0ca)

### path-062741

```text
(config)# aaa authentication login default <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 24 `；EOL ` RVA 0x341A88F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-98892eae7eb4f13f](../../evidence/conditions-sets-059.md#c-98892eae7eb4f13f) · [缺口 G-ee106c63e4227bb1](../../evidence/gaps-sets-008.md#g-ee106c63e4227bb1) · [状态效果 S-e927787e99cb0838](../../evidence/state_effects-sets-049.md#s-e927787e99cb0838)

### path-028356

```text
(config)# aaa authentication password-prompt <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 25 `；EOL ` RVA 0x341A84D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Text of prompt。

[条件 C-cb9956097f33bccc](../../evidence/conditions-sets-078.md#c-cb9956097f33bccc) · [参数 P-cfe4dc6f422d6c2c](../../evidence/parameters-sets-016.md#p-cfe4dc6f422d6c2c) · [状态效果 S-14f594620762880a](../../evidence/state_effects-sets-005.md#s-14f594620762880a)

### path-056888

```text
(config)# aaa authentication rejected <number:1..65535> in <number:1..65535> ban <number:1..65535> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 79 `；EOL ` RVA 0x341AA580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Fail attempts max value；` unsigned_number ` Time period in seconds；` unsigned_number ` Time period in seconds。

[条件 C-a9f6e75913a3fb97](../../evidence/conditions-sets-066.md#c-a9f6e75913a3fb97) · [参数 P-c13c1c7dbb5b0dc2](../../evidence/parameters-sets-015.md#p-c13c1c7dbb5b0dc2) · [状态效果 S-a3c9e1773af0c0ca](../../evidence/state_effects-sets-035.md#s-a3c9e1773af0c0ca)

### path-028177

```text
(config)# aaa authentication suppress null-username <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 30 `；EOL ` RVA 0x341A7768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b115887852580738](../../evidence/conditions-sets-068.md#c-b115887852580738) · [状态效果 S-a3c9e1773af0c0ca](../../evidence/state_effects-sets-035.md#s-a3c9e1773af0c0ca)

### path-034647

```text
(config)# aaa authentication token key <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 75 `；EOL ` RVA 0x341AA0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The UNENCRYPTED token key 。

[条件 C-fd3e59c01e895a0b](../../evidence/conditions-sets-098.md#c-fd3e59c01e895a0b) · [参数 P-92659d782811ef9c](../../evidence/parameters-sets-011.md#p-92659d782811ef9c) · [状态效果 S-a3c9e1773af0c0ca](../../evidence/state_effects-sets-035.md#s-a3c9e1773af0c0ca)

### path-026412

```text
(config)# aaa authorization address-authorization-exec <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 39 `；EOL ` RVA 0x341A5550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-ea441b490e4180f2](../../evidence/state_effects-sets-050.md#s-ea441b490e4180f2)

### path-026386

```text
(config)# aaa authorization config-commands <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 38 `；EOL ` RVA 0x341A52A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-ea441b490e4180f2](../../evidence/state_effects-sets-050.md#s-ea441b490e4180f2)

### path-026348

```text
(config)# aaa authorization console <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 40 `；EOL ` RVA 0x341A4D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-ea441b490e4180f2](../../evidence/state_effects-sets-050.md#s-ea441b490e4180f2)

### path-062742

```text
(config)# aaa authorization network default <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 31 `；EOL ` RVA 0x341A5F48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e4f8c51cd202460b](../../evidence/conditions-sets-088.md#c-e4f8c51cd202460b) · [缺口 G-e6aad825e3df4110](../../evidence/gaps-sets-008.md#g-e6aad825e3df4110) · [状态效果 S-9ad4fa00b77db25f](../../evidence/state_effects-sets-033.md#s-9ad4fa00b77db25f)

### path-028298

```text
(config)# aaa authorization network visible-keys <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 76 `；EOL ` RVA 0x341A5C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46033a7fc7a8407b](../../evidence/conditions-sets-027.md#c-46033a7fc7a8407b) · [状态效果 S-9273e84715b7c28a](../../evidence/state_effects-sets-031.md#s-9273e84715b7c28a)

### path-028222

```text
(config)# aaa authorization suppress null-username <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 81 `；EOL ` RVA 0x341A5018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-ea441b490e4180f2](../../evidence/state_effects-sets-050.md#s-ea441b490e4180f2)

### path-026436

```text
(config)# aaa authorization template <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 41 `；EOL ` RVA 0x341A57F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-ea441b490e4180f2](../../evidence/state_effects-sets-050.md#s-ea441b490e4180f2)

### path-026235

```text
(config)# aaa cache filterserver <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 15 `；EOL ` RVA 0x341B1030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a13ce26d85708235](../../evidence/conditions-sets-062.md#c-a13ce26d85708235) · [状态效果 S-dba2c2cac0c9dc34](../../evidence/state_effects-sets-046.md#s-dba2c2cac0c9dc34)

### path-028064

```text
(config)# aaa cache profile <string> <cr>
```

Handler ` RVA 0xCD83BC0 `；selector ` 0 `；EOL ` RVA 0x341B1350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Cache profile name。

[条件 C-a13ce26d85708235](../../evidence/conditions-sets-062.md#c-a13ce26d85708235) · [参数 P-c045549dd3aef44c](../../evidence/parameters-sets-015.md#p-c045549dd3aef44c) · [状态效果 S-dba2c2cac0c9dc34](../../evidence/state_effects-sets-046.md#s-dba2c2cac0c9dc34)

### path-028087

```text
(config)# aaa common-criteria policy <string> <cr>
```

Handler ` RVA 0xDD6C420 `；selector ` 0 `；EOL ` RVA 0x341B1708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Policy name (max of 128 characters)。

[条件 C-37fc62d47b80b8b9](../../evidence/conditions-sets-022.md#c-37fc62d47b80b8b9) · [参数 P-ab3ad3ab6970872b](../../evidence/parameters-sets-013.md#p-ab3ad3ab6970872b) · [状态效果 S-dba2c2cac0c9dc34](../../evidence/state_effects-sets-046.md#s-dba2c2cac0c9dc34)

### path-062736

```text
(config)# aaa configuration config-username <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 32 `；EOL ` RVA 0x341B1EF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` username。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [参数 P-b4a8db17da99b826](../../evidence/parameters-sets-014.md#p-b4a8db17da99b826) · [状态效果 S-e5a85ea7d4c486c9](../../evidence/state_effects-sets-049.md#s-e5a85ea7d4c486c9)

### path-062775

```text
(config)# aaa configuration pool username <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 34 `；EOL ` RVA 0x341B22F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` The username。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [参数 P-3c9355905b2f8517](../../evidence/parameters-sets-005.md#p-3c9355905b2f8517) · [状态效果 S-af23ea8ed889623c](../../evidence/state_effects-sets-037.md#s-af23ea8ed889623c)

### path-062776

```text
(config)# aaa configuration route username <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 36 `；EOL ` RVA 0x341B2828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` The username。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [参数 P-e48994052ad777c0](../../evidence/parameters-sets-017.md#p-e48994052ad777c0) · [状态效果 S-888df576f4bcf7d0](../../evidence/state_effects-sets-029.md#s-888df576f4bcf7d0)

### path-062856

```text
(config)# aaa dnis map <string> accounting network none <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 5 `；EOL ` RVA 0x3419E398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` DNIS number。

[条件 C-8aec5913aac04cd0](../../evidence/conditions-sets-054.md#c-8aec5913aac04cd0) · [缺口 G-3e48e569588ea99f](../../evidence/gaps-sets-003.md#g-3e48e569588ea99f) · [参数 P-bfb9721d7e9db5ea](../../evidence/parameters-sets-015.md#p-bfb9721d7e9db5ea) · [状态效果 S-56b95da988c48ab2](../../evidence/state_effects-sets-019.md#s-56b95da988c48ab2)

### path-056909

```text
(config)# aaa dnis map <string> authentication ppp group <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 4 `；EOL ` RVA 0x3419DE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS number；` string ` Server-group name。

[条件 C-9281243555c2c5b7](../../evidence/conditions-sets-057.md#c-9281243555c2c5b7) · [参数 P-d2699241aa64d289](../../evidence/parameters-sets-016.md#p-d2699241aa64d289) · [状态效果 S-c57506ec61f5cc13](../../evidence/state_effects-sets-042.md#s-c57506ec61f5cc13)

### path-062242

```text
(config)# aaa dnis map <string> authentication ppp group tacacs+ <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 4 `；EOL ` RVA 0x3419DE70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` DNIS number。

[条件 C-a66cb102042009cc](../../evidence/conditions-sets-064.md#c-a66cb102042009cc) · [缺口 G-e504771e2ecee7d1](../../evidence/gaps-sets-008.md#g-e504771e2ecee7d1) · [参数 P-bfb9721d7e9db5ea](../../evidence/parameters-sets-015.md#p-bfb9721d7e9db5ea) · [状态效果 S-8c6d431a491e90a3](../../evidence/state_effects-sets-030.md#s-8c6d431a491e90a3)

### path-056897

```text
(config)# aaa dnis map <string> authorization network group <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 3 `；EOL ` RVA 0x3419D928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS number；` string ` Server-group name。

[条件 C-5f3475ed8f580338](../../evidence/conditions-sets-037.md#c-5f3475ed8f580338) · [参数 P-494dff0e3bc64319](../../evidence/parameters-sets-006.md#p-494dff0e3bc64319) · [状态效果 S-3919b142971e051c](../../evidence/state_effects-sets-013.md#s-3919b142971e051c)

### path-062240

```text
(config)# aaa dnis map <string> authorization network group tacacs+ <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 3 `；EOL ` RVA 0x3419D928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` DNIS number。

[条件 C-c9acbb509f98e4fa](../../evidence/conditions-sets-078.md#c-c9acbb509f98e4fa) · [缺口 G-520e7fbbfb5febc5](../../evidence/gaps-sets-003.md#g-520e7fbbfb5febc5) · [参数 P-bfb9721d7e9db5ea](../../evidence/parameters-sets-015.md#p-bfb9721d7e9db5ea) · [状态效果 S-124ae3dbf6628661](../../evidence/state_effects-sets-004.md#s-124ae3dbf6628661)

### path-028219

```text
(config)# aaa dnis map enable <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 1 `；EOL ` RVA 0x3419D468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2bc7aed0e14d5b12](../../evidence/conditions-sets-017.md#c-2bc7aed0e14d5b12) · [状态效果 S-717af5896ca58f32](../../evidence/state_effects-sets-024.md#s-717af5896ca58f32)

### path-034245

```text
(config)# aaa group server tacacs+ <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 11 `；EOL ` RVA 0x341AAC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Server-group name with max string length 32。

[条件 C-724bb4672860d337](../../evidence/conditions-sets-044.md#c-724bb4672860d337) · [参数 P-bb25f0f3662e2333](../../evidence/parameters-sets-014.md#p-bb25f0f3662e2333) · [状态效果 S-39c6b5f9911949e9](../../evidence/state_effects-sets-013.md#s-39c6b5f9911949e9)

### path-044003

```text
(config)# aaa local authentication attempts max-fail <number:1..65535> <cr>
```

Handler ` RVA 0xD505370 `；selector ` 1 `；EOL ` RVA 0x33E6FC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify the value for max failed attempts。

[条件 C-1bb0ab905e894f39](../../evidence/conditions-sets-011.md#c-1bb0ab905e894f39) · [参数 P-0f230ff033c7ea72](../../evidence/parameters-sets-002.md#p-0f230ff033c7ea72) · [状态效果 S-b63e93d9c13a6d4e](../../evidence/state_effects-sets-039.md#s-b63e93d9c13a6d4e)

### path-043995

```text
(config)# aaa local authentication default authorization default <cr>
```

Handler ` RVA 0xD505370 `；selector ` 5 `；EOL ` RVA 0x33E70010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b2f0a854e6e7ca2](../../evidence/conditions-sets-029.md#c-4b2f0a854e6e7ca2) · [状态效果 S-cc9f2d59499e9f6e](../../evidence/state_effects-sets-043.md#s-cc9f2d59499e9f6e)

### path-062737

```text
(config)# aaa login display last-success <cr>
```

Handler ` RVA 0xDD11EB0 `；selector ` 19 `；EOL ` RVA 0x341B3AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ce1b133fba411bd0](../../evidence/conditions-sets-079.md#c-ce1b133fba411bd0) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-db39ab22d2543550](../../evidence/state_effects-sets-046.md#s-db39ab22d2543550)

### path-062703

```text
(config)# aaa login success-track-conf-time <number:0..24> <cr>
```

Handler ` RVA 0xDD11EB0 `；selector ` 5 `；EOL ` RVA 0x341B3A70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Configure time period (Hours)。

[条件 C-da4658d64f20ed90](../../evidence/conditions-sets-084.md#c-da4658d64f20ed90) · [缺口 G-6b0100b943080cf2](../../evidence/gaps-sets-004.md#g-6b0100b943080cf2) · [参数 P-6c0a5082f934fc6c](../../evidence/parameters-sets-009.md#p-6c0a5082f934fc6c) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062705

```text
(config)# aaa max-sessions <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 66 `；EOL ` RVA 0x341B5B30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-327412eafa026c27](../../evidence/conditions-sets-020.md#c-327412eafa026c27) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062779

```text
(config)# aaa memory threshold accounting disable <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 68 `；EOL ` RVA 0x341B6960 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-0741c6701df4554e](../../evidence/conditions-sets-003.md#c-0741c6701df4554e) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062778

```text
(config)# aaa memory threshold authentication reject <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 69 `；EOL ` RVA 0x341B65E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f1194fdc5dd2125f](../../evidence/conditions-sets-093.md#c-f1194fdc5dd2125f) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062710

```text
(config)# aaa nas description <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 6 `；EOL ` RVA 0x341B3120 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-18a02d3f1028dcf4](../../evidence/conditions-sets-010.md#c-18a02d3f1028dcf4) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062738

```text
(config)# aaa nas port extended <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 7 `；EOL ` RVA 0x341B3440 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-a8006490375db353](../../evidence/state_effects-sets-035.md#s-a8006490375db353)

### path-062709

```text
(config)# aaa nas redirected-station <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 18 `；EOL ` RVA 0x341B3738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-025568

```text
(config)# aaa new-model <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 0 `；EOL ` RVA 0x3419D068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ca3d23611b3ebd3](../../evidence/conditions-sets-060.md#c-9ca3d23611b3ebd3) · [状态效果 S-20af4524ea5182ce](../../evidence/state_effects-sets-007.md#s-20af4524ea5182ce)

### path-062716

```text
(config)# aaa password restriction <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 73 `；EOL ` RVA 0x341B6CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2dd26e0b8df7b570](../../evidence/conditions-sets-018.md#c-2dd26e0b8df7b570) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062711

```text
(config)# aaa pod server <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 9 `；EOL ` RVA 0x341B48B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eaf425d4346c0f41](../../evidence/conditions-sets-091.md#c-eaf425d4346c0f41) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062743

```text
(config)# aaa policy interface-config allow-subinterface <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 71 `；EOL ` RVA 0x341B5E60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7fc3a9d0230c148](../../evidence/conditions-sets-096.md#c-f7fc3a9d0230c148) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062702

```text
(config)# aaa preauth <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 14 `；EOL ` RVA 0x341B50C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2b55664c42211d4b](../../evidence/conditions-sets-017.md#c-2b55664c42211d4b) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062740

```text
(config)# aaa remote username <string> <cr>
```

Handler ` RVA 0xDD11EB0 `；selector ` 80 `；EOL ` RVA 0x341B4100 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` AAA user name(max length 63, longer name will be truncated)。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [参数 P-63c256743cd7d294](../../evidence/parameters-sets-008.md#p-63c256743cd7d294) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062706

```text
(config)# aaa route <cr>
```

Handler ` RVA 0xCF9ADF0 `；selector ` 0 `；EOL ` RVA 0x342890E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-eb2ab8ff9786d063](../../evidence/conditions-sets-091.md#c-eb2ab8ff9786d063) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062735

```text
(config)# aaa serial-authentication exec-failure disconnect <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 13 `；EOL ` RVA 0x341B2D60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-4255f2f4fac21ea7](../../evidence/state_effects-sets-015.md#s-4255f2f4fac21ea7)

### path-062739

```text
(config)# aaa server radius sesm <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 12 `；EOL ` RVA 0x341B4448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-69fe13645483e4b3](../../evidence/conditions-sets-041.md#c-69fe13645483e4b3) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-9957d00ba7705e14](../../evidence/state_effects-sets-033.md#s-9957d00ba7705e14)

### path-062744

```text
(config)# aaa service-profile key username-with-nasport <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 70 `；EOL ` RVA 0x341B61A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7fc3a9d0230c148](../../evidence/conditions-sets-096.md#c-f7fc3a9d0230c148) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-062714

```text
(config)# aaa session-id common <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 64 `；EOL ` RVA 0x341B5478 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7fc3a9d0230c148](../../evidence/conditions-sets-096.md#c-f7fc3a9d0230c148) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-362f9ad66a2ba29b](../../evidence/state_effects-sets-012.md#s-362f9ad66a2ba29b)

### path-052059

```text
(config)# aaa tools memleak mode manual count <number:2..64> <cr>
```

Handler ` RVA 0x1371D3C0 `；selector ` 0 `；EOL ` RVA 0x35C0E270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum Sample Count。

[条件 C-bee57da99df13989](../../evidence/conditions-sets-074.md#c-bee57da99df13989) · [参数 P-c896a77975cd77b0](../../evidence/parameters-sets-015.md#p-c896a77975cd77b0) · [状态效果 S-db8e708045201456](../../evidence/state_effects-sets-046.md#s-db8e708045201456)

### path-062713

```text
(config)# aaa traceback recording <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 67 `；EOL ` RVA 0x341B57D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f7fc3a9d0230c148](../../evidence/conditions-sets-096.md#c-f7fc3a9d0230c148) · [缺口 G-ebe0bb2470964046](../../evidence/gaps-sets-008.md#g-ebe0bb2470964046) · [状态效果 S-98a64d532145df74](../../evidence/state_effects-sets-032.md#s-98a64d532145df74)

### path-028130

```text
(config)# aaa user profile <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 62 `；EOL ` RVA 0x341AB2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` AAA user name(max length 63, longer name will be truncated)。

[条件 C-c1044df77e05c547](../../evidence/conditions-sets-075.md#c-c1044df77e05c547) · [参数 P-5fcac73fb916b7fb](../../evidence/parameters-sets-008.md#p-5fcac73fb916b7fb) · [状态效果 S-d2bcdd8c01e8049b](../../evidence/state_effects-sets-045.md#s-d2bcdd8c01e8049b)

### path-060393

```text
(config)# access-list <?dumper_command_func@5555892a2f88> <number:1..99> <cr>
```

Handler ` RVA 0xCEEBE50 `；selector ` 0 `；EOL ` RVA 0x33D4F138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP standard access list。

[条件 C-ff25512e2f872c45](../../evidence/conditions-sets-098.md#c-ff25512e2f872c45) · [缺口 G-2d616a2ef61b6963](../../evidence/gaps-sets-002.md#g-2d616a2ef61b6963) · [参数 P-89fd5208547ecf8d](../../evidence/parameters-sets-011.md#p-89fd5208547ecf8d) · [状态效果 S-efdfdc8aeff450e0](../../evidence/state_effects-sets-051.md#s-efdfdc8aeff450e0)

### path-060396

```text
(config)# access-list <?dumper_command_func@5555892a2f88> <number:100..199> <cr>
```

Handler ` RVA 0xCEFA590 `；selector ` 1 `；EOL ` RVA 0x33D53AE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` IP extended access list。

[条件 C-b4730987dfd3f3bf](../../evidence/conditions-sets-070.md#c-b4730987dfd3f3bf) · [缺口 G-2d616a2ef61b6963](../../evidence/gaps-sets-002.md#g-2d616a2ef61b6963) · [参数 P-c83d442d78966795](../../evidence/parameters-sets-015.md#p-c83d442d78966795) · [状态效果 S-efdfdc8aeff450e0](../../evidence/state_effects-sets-051.md#s-efdfdc8aeff450e0)

### path-026768

```text
(config)# access-list acl-ace-limit <number:1..4294967295> <cr>
```

Handler ` RVA 0xCEE2FE0 `；selector ` 0 `；EOL ` RVA 0x33D54550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max ace limit for all ACLs。

[条件 C-b215c87710384363](../../evidence/conditions-sets-069.md#c-b215c87710384363) · [参数 P-d0da9036a0742944](../../evidence/parameters-sets-016.md#p-d0da9036a0742944) · [状态效果 S-fb1b390ac53cef3a](../../evidence/state_effects-sets-053.md#s-fb1b390ac53cef3a)

### path-026745

```text
(config)# access-list acl-limit <number:1..65535> <cr>
```

Handler ` RVA 0xCEE2E30 `；selector ` 0 `；EOL ` RVA 0x33D541B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max ACL Limit。

[条件 C-8425e44e7574d7a6](../../evidence/conditions-sets-051.md#c-8425e44e7574d7a6) · [参数 P-6aba35685483f094](../../evidence/parameters-sets-008.md#p-6aba35685483f094) · [状态效果 S-2b51ce8ca73f7c4f](../../evidence/state_effects-sets-010.md#s-2b51ce8ca73f7c4f)

### path-025717

```text
(config)# access-list dynamic-extended <cr>
```

Handler ` RVA 0xCEFA1C0 `；selector ` 1 `；EOL ` RVA 0x33D53DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f27fcd8c8da52abe](../../evidence/conditions-sets-094.md#c-f27fcd8c8da52abe) · [状态效果 S-efdfdc8aeff450e0](../../evidence/state_effects-sets-051.md#s-efdfdc8aeff450e0)

### path-026785

```text
(config)# access-list global-ace-limit <number:1..4294967295> <cr>
```

Handler ` RVA 0xCEE31A0 `；selector ` 0 `；EOL ` RVA 0x33D548C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` max ace limit for the entire system。

[条件 C-fb61bddf5e914b98](../../evidence/conditions-sets-097.md#c-fb61bddf5e914b98) · [参数 P-68847638e1f65bb4](../../evidence/parameters-sets-008.md#p-68847638e1f65bb4) · [状态效果 S-db8646637780b28b](../../evidence/state_effects-sets-046.md#s-db8646637780b28b)

### path-028868

```text
(config)# access-list rate-limit <number:100..199> <address> <cr>
```

Handler ` RVA 0x10C68030 `；selector ` 0 `；EOL ` RVA 0x34CECFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` MAC address ACL index；` address ` MAC address。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-4a897af35f274644](../../evidence/parameters-sets-006.md#p-4a897af35f274644) · [状态效果 S-efdfdc8aeff450e0](../../evidence/state_effects-sets-051.md#s-efdfdc8aeff450e0)

### path-025737

```text
(config)# access-list template <cr>
```

Handler ` RVA 0xEBB9980 `；selector ` 0 `；EOL ` RVA 0x343D1858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-656eb8ce347bda10](../../evidence/conditions-sets-039.md#c-656eb8ce347bda10) · [状态效果 S-efdfdc8aeff450e0](../../evidence/state_effects-sets-051.md#s-efdfdc8aeff450e0)

### path-053350

```text
(config)# access-session accounting attributes filter-spec include list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 14 `；EOL ` RVA 0x33BA3958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` list name。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [参数 P-cb160a75f6835c4b](../../evidence/parameters-sets-015.md#p-cb160a75f6835c4b) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-027177

```text
(config)# access-session accounting interim-disable <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 25 `；EOL ` RVA 0x33BA3568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [状态效果 S-6fc0e4d6783ec73d](../../evidence/state_effects-sets-024.md#s-6fc0e4d6783ec73d)

### path-030379

```text
(config)# access-session acl ack-timer <number:20..300> <cr>
```

Handler ` RVA 0xCB45380 `；selector ` 0 `；EOL ` RVA 0x33BDA750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter a timeout value (in seconds) between 20 and 300。

[条件 C-2060ed424c9576d9](../../evidence/conditions-sets-013.md#c-2060ed424c9576d9) · [参数 P-3687a3ecbb410b2c](../../evidence/parameters-sets-005.md#p-3687a3ecbb410b2c) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-030308

```text
(config)# access-session acl default passthrough <cr>
```

Handler ` RVA 0xCB451F0 `；selector ` 2 `；EOL ` RVA 0x33BDA420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22163e1f1326ce85](../../evidence/conditions-sets-013.md#c-22163e1f1326ce85) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-036280

```text
(config)# access-session attributes filter-list list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 12 `；EOL ` RVA 0x33BA2E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` list name。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [参数 P-5ba1cde7f6c0e13e](../../evidence/parameters-sets-007.md#p-5ba1cde7f6c0e13e) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-053271

```text
(config)# access-session authentication attributes filter-spec include list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 13 `；EOL ` RVA 0x33BA3250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` list name。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [参数 P-d43c8b724db9727a](../../evidence/parameters-sets-016.md#p-d43c8b724db9727a) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-060510

```text
(config)# access-session bridge-mode vm-policy <?option@5555890f84c8> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 24 `；EOL ` RVA 0x33BA44F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a318b7a34596e14b](../../evidence/conditions-sets-063.md#c-a318b7a34596e14b) · [缺口 G-2930900b189e1f11](../../evidence/gaps-sets-002.md#g-2930900b189e1f11) · [状态效果 S-ce1002d4446b9888](../../evidence/state_effects-sets-044.md#s-ce1002d4446b9888)

### path-030213

```text
(config)# access-session cache limit <number:0..24000> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 7 `；EOL ` RVA 0x33BA1E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Limit。

[条件 C-2a117e9269a61e43](../../evidence/conditions-sets-016.md#c-2a117e9269a61e43) · [参数 P-90b8361aa24f3a8f](../../evidence/parameters-sets-011.md#p-90b8361aa24f3a8f) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-025840

```text
(config)# access-session cui-enable <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 23 `；EOL ` RVA 0x33BA40C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7060d85cd77cba2f](../../evidence/conditions-sets-043.md#c-7060d85cd77cba2f) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-053135

```text
(config)# access-session event-logging enable session-limit <number:1..4000> event-limit <number:1..800> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 16 `；EOL ` RVA 0x33BA0348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session Limit or max sessions to be logged；` unsigned_number ` Event Limit per session。

[条件 C-67735fdc381e6a2b](../../evidence/conditions-sets-040.md#c-67735fdc381e6a2b) · [参数 P-b9ec9a2fd4b932d0](../../evidence/parameters-sets-014.md#p-b9ec9a2fd4b932d0) · [状态效果 S-6e4dc92232482a78](../../evidence/state_effects-sets-023.md#s-6e4dc92232482a78)

### path-027335

```text
(config)# access-session interface-template sticky <cr>
```

Handler ` RVA 0xCB48060 `；selector ` 0 `；EOL ` RVA 0x33BDD190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-22163e1f1326ce85](../../evidence/conditions-sets-013.md#c-22163e1f1326ce85) · [状态效果 S-68e50c9646737e15](../../evidence/state_effects-sets-022.md#s-68e50c9646737e15)

### path-036526

```text
(config)# access-session limit profile name <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 20 `；EOL ` RVA 0x33BA1740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` session limit profile name maximum 32 characters。

[条件 C-d9db9146b1433406](../../evidence/conditions-sets-084.md#c-d9db9146b1433406) · [参数 P-8dcb75c2b8917640](../../evidence/parameters-sets-011.md#p-8dcb75c2b8917640) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-027163

```text
(config)# access-session mac-move deny <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 2 `；EOL ` RVA 0x33BA0878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a4b6f81f236ad7c](../../evidence/conditions-sets-053.md#c-8a4b6f81f236ad7c) · [状态效果 S-e552117975a66319](../../evidence/state_effects-sets-048.md#s-e552117975a66319)

### path-025869

```text
(config)# access-session monitor <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 1 `；EOL ` RVA 0x33BA3CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1953bbbd1a40eb74](../../evidence/conditions-sets-010.md#c-1953bbbd1a40eb74) · [状态效果 S-72d8924e8e2ff487](../../evidence/state_effects-sets-024.md#s-72d8924e8e2ff487)

### path-036763

```text
(config)# access-session passthru-access-group <string> passthru-domain-list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 8 `；EOL ` RVA 0x33BA2228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name of IP access-list；` string ` Domain name list mapped to FQDN ACL。

[条件 C-e0dc9286a8880d8c](../../evidence/conditions-sets-087.md#c-e0dc9286a8880d8c) · [参数 P-25b997fc59273ecd](../../evidence/parameters-sets-003.md#p-25b997fc59273ecd) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-027199

```text
(config)# access-session pqc-type pqc <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 26 `；EOL ` RVA 0x33BA1230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-058377ecf1757eb1](../../evidence/conditions-sets-003.md#c-058377ecf1757eb1) · [状态效果 S-4f6edd633a5e41c2](../../evidence/state_effects-sets-017.md#s-4f6edd633a5e41c2)

### path-060418

```text
(config)# access-session single-policy <interface> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 21 `；EOL ` RVA 0x33BA26D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c9b2abdd603d463f](../../evidence/conditions-sets-078.md#c-c9b2abdd603d463f) · [缺口 G-4f817c4487f944d2](../../evidence/gaps-sets-003.md#g-4f817c4487f944d2) · [参数 P-15d952abe238cf14](../../evidence/parameters-sets-002.md#p-15d952abe238cf14) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-060631

```text
(config)# access-session single-policy <interface> forced <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 22 `；EOL ` RVA 0x33BA26B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c9b2abdd603d463f](../../evidence/conditions-sets-078.md#c-c9b2abdd603d463f) · [缺口 G-4f817c4487f944d2](../../evidence/gaps-sets-003.md#g-4f817c4487f944d2) · [参数 P-15d952abe238cf14](../../evidence/parameters-sets-002.md#p-15d952abe238cf14) · [状态效果 S-7728159a70bb8ce6](../../evidence/state_effects-sets-025.md#s-7728159a70bb8ce6)

### path-027191

```text
(config)# access-session tls-version all <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 19 `；EOL ` RVA 0x33BA0DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c84c1a774fdb6dd](../../evidence/conditions-sets-005.md#c-0c84c1a774fdb6dd) · [状态效果 S-bf88cc90af3f4881](../../evidence/state_effects-sets-041.md#s-bf88cc90af3f4881)

### path-027275

```text
(config)# access-session voice skip-data-vlan <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 18 `；EOL ` RVA 0x33BA1AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c0eb91c8012f907d](../../evidence/conditions-sets-074.md#c-c0eb91c8012f907d) · [状态效果 S-b0abde10c84aaf60](../../evidence/state_effects-sets-037.md#s-b0abde10c84aaf60)

### path-034003

```text
(config)# accounting group <string> list <string> <cr>
```

Handler ` RVA 0x10D13C90 `；selector ` 0 `；EOL ` RVA 0x34D11E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Accounting group name；` string ` Accounting list name。

[条件 C-65412258c56d71bc](../../evidence/conditions-sets-039.md#c-65412258c56d71bc) · [参数 P-d82b638ac8a38fd3](../../evidence/parameters-sets-016.md#p-d82b638ac8a38fd3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061993

```text
(config)# alg sip blacklist trigger-period <number:10..60000> trigger-size <number:1..65535> <cr>
```

Handler ` RVA 0xCD3C1C0 `；selector ` 2 `；EOL ` RVA 0x33CD5AF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` The trigger period in milliseconds. Maximum 60000ms (1 minute)；` unsigned_number ` The minimum number of events within the trigger period。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-febd72be09846217](../../evidence/parameters-sets-019.md#p-febd72be09846217) · [状态效果 S-8b0e17f503d09ef7](../../evidence/state_effects-sets-030.md#s-8b0e17f503d09ef7)

### path-061410

```text
(config)# alg sip processor session max-backlog <number:1..20> <cr>
```

Handler ` RVA 0xCD3C1C0 `；selector ` 1 `；EOL ` RVA 0x33CD6118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Maximum number of concurrent processor usage。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-c0c5f5166b3a44f4](../../evidence/parameters-sets-015.md#p-c0c5f5166b3a44f4) · [状态效果 S-10cc612ed555408c](../../evidence/state_effects-sets-004.md#s-10cc612ed555408c)

### path-060914

```text
(config)# alg sip timer max-call-duration <number:0..65535> <cr>
```

Handler ` RVA 0xCD3C1C0 `；selector ` 0 `；EOL ` RVA 0x33CD6588 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Maximum call duration in seconds. Default 36000s。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-0dbbc8e94d4dc9d7](../../evidence/parameters-sets-002.md#p-0dbbc8e94d4dc9d7) · [状态效果 S-d1e18d508abc24fa](../../evidence/state_effects-sets-044.md#s-d1e18d508abc24fa)

### path-060658

```text
(config)# alg vtcp service sip <cr>
```

Handler ` RVA 0xCD3C1C0 `；selector ` 3 `；EOL ` RVA 0x33CD54D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-062724

```text
(config)# alias <?sync_force_action@55558960ebb0> <?mode_action@55558960ebf0> <cr>
```

Handler ` RVA 0xDEFFA90 `；selector ` 0 `；EOL ` RVA 0x340BAD38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-545c33b75b0f801a](../../evidence/conditions-sets-033.md#c-545c33b75b0f801a) · [缺口 G-a821b09efd8c5420](../../evidence/gaps-sets-006.md#g-a821b09efd8c5420) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026405

```text
(config)# alps circuit <string> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 5 `；EOL ` RVA 0x35421EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ASCU ckt name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-d7eaa09ed9c5dfea](../../evidence/parameters-sets-016.md#p-d7eaa09ed9c5dfea) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060768

```text
(config)# alps enable-alarms ascu <interface> <number:33..126> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 3 `；EOL ` RVA 0x35421100 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Interchange address。

[条件 C-7e144c878fbb44ac](../../evidence/conditions-sets-049.md#c-7e144c878fbb44ac) · [缺口 G-31a910e27de04fca](../../evidence/gaps-sets-002.md#g-31a910e27de04fca) · [参数 P-80942fd2e52cdfce](../../evidence/parameters-sets-010.md#p-80942fd2e52cdfce) · [状态效果 S-623ea03fc6a8db89](../../evidence/state_effects-sets-021.md#s-623ea03fc6a8db89)

### path-026392

```text
(config)# alps enable-alarms peer <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 3 `；EOL ` RVA 0x35421100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-3eda6a71ebb2216f](../../evidence/state_effects-sets-014.md#s-3eda6a71ebb2216f)

### path-025638

```text
(config)# alps keepalive <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 1 `；EOL ` RVA 0x354209A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-576918d46c3ce422](../../evidence/state_effects-sets-019.md#s-576918d46c3ce422)

### path-026343

```text
(config)# alps local-peer <address> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 0 `；EOL ` RVA 0x354205A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for local peer。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-53a99e23d8383f0b](../../evidence/parameters-sets-007.md#p-53a99e23d8383f0b) · [状态效果 S-464a51ebeddfb93a](../../evidence/state_effects-sets-015.md#s-464a51ebeddfb93a)

### path-025651

```text
(config)# alps matip-host-emulation <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 6 `；EOL ` RVA 0x35422138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026552

```text
(config)# alps remote-peer <address> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 4 `；EOL ` RVA 0x35421B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address for remote peer。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-c6c0a71085917c44](../../evidence/parameters-sets-015.md#p-c6c0a71085917c44) · [状态效果 S-2731cfc80492f2e6](../../evidence/state_effects-sets-009.md#s-2731cfc80492f2e6)

### path-044056

```text
(config)# alps service-msg-list <number:1..8> number <number:1..8> <string> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 2 `；EOL ` RVA 0x35420D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Service message list number；` unsigned_number ` Service message number；` string ` Service message description。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-265dbe293b4e50d3](../../evidence/parameters-sets-003.md#p-265dbe293b4e50d3) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028383

```text
(config)# ancp adjacency timer <number:1..255> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 1 `；EOL ` RVA 0x336DFFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` timer value in 100 milliseconds。

[条件 C-5d556adf9182f106](../../evidence/conditions-sets-036.md#c-5d556adf9182f106) · [参数 P-b9b8fc7816710534](../../evidence/parameters-sets-014.md#p-b9b8fc7816710534) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034413

```text
(config)# ancp atm shaper percent-factor <number:1..100> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 3 `；EOL ` RVA 0x336DF8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Percent Factor。

[条件 C-e5a94dd09ada46a3](../../evidence/conditions-sets-089.md#c-e5a94dd09ada46a3) · [参数 P-d44cf8cbe037f18e](../../evidence/parameters-sets-016.md#p-d44cf8cbe037f18e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034414

```text
(config)# ancp atm shaper percent-factor <number:1..100> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 2 `；EOL ` RVA 0x336DFB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Percent Factor。

[条件 C-2035f65b63b0ee4f](../../evidence/conditions-sets-013.md#c-2035f65b63b0ee4f) · [参数 P-d44cf8cbe037f18e](../../evidence/parameters-sets-016.md#p-d44cf8cbe037f18e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026489

```text
(config)# ancp enable test-configuration <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 6 `；EOL ` RVA 0x336E02F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-30629b4383108cd4](../../evidence/conditions-sets-019.md#c-30629b4383108cd4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044288

```text
(config)# ancp neighbor name <string> id <string> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 4 `；EOL ` RVA 0x336E09C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ANCP neighbor name；` string ` ANCP neighbor ID。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-adf739dccc7a9655](../../evidence/parameters-sets-013.md#p-adf739dccc7a9655) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026502

```text
(config)# ancp source-ip <address> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 5 `；EOL ` RVA 0x336E0610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` ANCP source IP address。

[条件 C-43b17cd4c6fb8898](../../evidence/conditions-sets-026.md#c-43b17cd4c6fb8898) · [参数 P-df61d1091ab2219d](../../evidence/parameters-sets-017.md#p-df61d1091ab2219d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026408

```text
(config)# ancp truncate <number:1..128> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 7 `；EOL ` RVA 0x336DF488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum value to truncate (in kbps)。

[条件 C-0821ac5c91954b5b](../../evidence/conditions-sets-004.md#c-0821ac5c91954b5b) · [参数 P-da5228c22cf3b694](../../evidence/parameters-sets-016.md#p-da5228c22cf3b694) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-063025

```text
(config)# app-hosting appid <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E0F3D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-00ba32b2fa68bbf0](../../evidence/conditions-sets-001.md#c-00ba32b2fa68bbf0) · [缺口 G-6bfd5c50dd12fec4](../../evidence/gaps-sets-004.md#g-6bfd5c50dd12fec4) · [状态效果 S-22f6f69e89686f7b](../../evidence/state_effects-sets-008.md#s-22f6f69e89686f7b)

### path-063034

```text
(config)# app-hosting appid <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37DF8A48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` no description。

[条件 C-897ebc0072bb0e68](../../evidence/conditions-sets-053.md#c-897ebc0072bb0e68) · [缺口 G-e6841642c2d9b00a](../../evidence/gaps-sets-008.md#g-e6841642c2d9b00a) · [参数 P-25fdce7bc06f55bb](../../evidence/parameters-sets-003.md#p-25fdce7bc06f55bb) · [状态效果 S-0bd301d8a37249ef](../../evidence/state_effects-sets-003.md#s-0bd301d8a37249ef)

### path-063035

```text
(config)# app-hosting appid <string> <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFFBAE29C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` no description。

[条件 C-989258ed5aa59075](../../evidence/conditions-sets-059.md#c-989258ed5aa59075) · [缺口 G-0e13b8d453e242d4](../../evidence/gaps-sets-001.md#g-0e13b8d453e242d4) · [参数 P-25fdce7bc06f55bb](../../evidence/parameters-sets-003.md#p-25fdce7bc06f55bb) · [状态效果 S-e1562d1dc4852824](../../evidence/state_effects-sets-048.md#s-e1562d1dc4852824)

### path-063022

```text
(config)# app-hosting signed-verification <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37DF7860 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-87ac5067934547bc](../../evidence/conditions-sets-052.md#c-87ac5067934547bc) · [缺口 G-6496fcb554bcb405](../../evidence/gaps-sets-004.md#g-6496fcb554bcb405) · [状态效果 S-78bacb637f4e5c3a](../../evidence/state_effects-sets-026.md#s-78bacb637f4e5c3a)

### path-063023

```text
(config)# app-hosting signed-verification <cr>
```

Handler ` RVA 0xDF978A0 `；selector ` 0 `；EOL ` 历史 VA 0x7FFF37E0F340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9f35a2aa42c473ea](../../evidence/conditions-sets-062.md#c-9f35a2aa42c473ea) · [缺口 G-0ba416174e499d7d](../../evidence/gaps-sets-001.md#g-0ba416174e499d7d) · [状态效果 S-4622020f9b5b6ac7](../../evidence/state_effects-sets-015.md#s-4622020f9b5b6ac7)

### path-025484

```text
(config)# archive <cr>
```

Handler ` RVA 0xDEC8E00 `；selector ` 0 `；EOL ` RVA 0x34099E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029236

```text
(config)# arp <address> <address> arpa <cr>
```

Handler ` RVA 0xCF5BAE0 `；selector ` 0 `；EOL ` RVA 0x33D292C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of ARP entry；` address ` 48-bit hardware address of ARP entry。

[条件 C-04229396ca36b073](../../evidence/conditions-sets-002.md#c-04229396ca36b073) · [参数 P-8f474ed25224183c](../../evidence/parameters-sets-011.md#p-8f474ed25224183c) · [状态效果 S-5f043ad5d9c7b377](../../evidence/state_effects-sets-020.md#s-5f043ad5d9c7b377)

### path-060818

```text
(config)# arp <address> <address> arpa <interface> <cr>
```

Handler ` RVA 0xCF5BAE0 `；selector ` 0 `；EOL ` RVA 0x33D292C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of ARP entry；` address ` 48-bit hardware address of ARP entry。

[条件 C-1641310b88e8b53d](../../evidence/conditions-sets-009.md#c-1641310b88e8b53d) · [缺口 G-f4f8d3a5973418fe](../../evidence/gaps-sets-008.md#g-f4f8d3a5973418fe) · [参数 P-c9a4d60dc979f3a5](../../evidence/parameters-sets-015.md#p-c9a4d60dc979f3a5) · [状态效果 S-5f043ad5d9c7b377](../../evidence/state_effects-sets-020.md#s-5f043ad5d9c7b377)

### path-028993

```text
(config)# arp entries interface-limit <number:1..2147483647> <cr>
```

Handler ` RVA 0xCF5C9D0 `；selector ` 0 `；EOL ` RVA 0x33D28E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ARP Entry count limit。

[条件 C-36e51e76efdb799d](../../evidence/conditions-sets-021.md#c-36e51e76efdb799d) · [参数 P-243b9b40490af6ce](../../evidence/parameters-sets-003.md#p-243b9b40490af6ce) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027234

```text
(config)# async-bootp bootfile <string> <cr>
```

Handler ` RVA 0xD344030 `；selector ` 0 `；EOL ` RVA 0x33E1AC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A name surrounded by quotes (")。

[条件 C-4cf04161dc9f21ae](../../evidence/conditions-sets-030.md#c-4cf04161dc9f21ae) · [参数 P-f6b35979a068aea6](../../evidence/parameters-sets-018.md#p-f6b35979a068aea6) · [状态效果 S-f3f59da55fe992ef](../../evidence/state_effects-sets-052.md#s-f3f59da55fe992ef)

### path-029968

```text
(config)# authentication command bounce-port ignore <cr>
```

Handler ` RVA 0xCB0E770 `；selector ` 2 `；EOL ` RVA 0x33BB1730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc51fcb87e18e11e](../../evidence/conditions-sets-085.md#c-dc51fcb87e18e11e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030007

```text
(config)# authentication command disable-port ignore <cr>
```

Handler ` RVA 0xCB0E770 `；selector ` 3 `；EOL ` RVA 0x33BB1A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dc51fcb87e18e11e](../../evidence/conditions-sets-085.md#c-dc51fcb87e18e11e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027118

```text
(config)# authentication convert-to new-style <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 6 `；EOL ` RVA 0x33B93368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0be4311d10d7daa](../../evidence/conditions-sets-093.md#c-f0be4311d10d7daa) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029768

```text
(config)# authentication convert-to new-style forced <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 7 `；EOL ` RVA 0x33B93340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0be4311d10d7daa](../../evidence/conditions-sets-093.md#c-f0be4311d10d7daa) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060848

```text
(config)# authentication convert-to new-style single-policy <interface> <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 8 `；EOL ` RVA 0x33B92E30 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-605e05cb52b215c3](../../evidence/conditions-sets-037.md#c-605e05cb52b215c3) · [缺口 G-17c6aa5a51e32a2f](../../evidence/gaps-sets-001.md#g-17c6aa5a51e32a2f) · [参数 P-a0cfd6ac72fe4b09](../../evidence/parameters-sets-012.md#p-a0cfd6ac72fe4b09) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061301

```text
(config)# authentication convert-to new-style single-policy <interface> forced <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 9 `；EOL ` RVA 0x33B92E08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-605e05cb52b215c3](../../evidence/conditions-sets-037.md#c-605e05cb52b215c3) · [缺口 G-17c6aa5a51e32a2f](../../evidence/gaps-sets-001.md#g-17c6aa5a51e32a2f) · [参数 P-a0cfd6ac72fe4b09](../../evidence/parameters-sets-012.md#p-a0cfd6ac72fe4b09) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-036288

```text
(config)# authentication critical recovery delay <number:1..10000> <cr>
```

Handler ` RVA 0xCAB9CD0 `；selector ` 0 `；EOL ` RVA 0x33B81610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Critical Authentication Recovery delay in milliseconds。

[条件 C-35eb6486fef7a9a0](../../evidence/conditions-sets-021.md#c-35eb6486fef7a9a0) · [参数 P-d79c910404ec58d0](../../evidence/parameters-sets-016.md#p-d79c910404ec58d0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025830

```text
(config)# authentication dis-scale-opt <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 5 `；EOL ` RVA 0x33B92328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41f7ee7f503f70ed](../../evidence/conditions-sets-026.md#c-41f7ee7f503f70ed) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027185

```text
(config)# authentication logging session-terminate <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 10 `；EOL ` RVA 0x33B92990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9e4607a60f8f449c](../../evidence/conditions-sets-061.md#c-9e4607a60f8f449c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027169

```text
(config)# authentication logging verbose <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 4 `；EOL ` RVA 0x33B926B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8a04d3018353785f](../../evidence/conditions-sets-053.md#c-8a04d3018353785f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027107

```text
(config)# authentication mac-move permit <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 1 `；EOL ` RVA 0x33B92030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41f7ee7f503f70ed](../../evidence/conditions-sets-026.md#c-41f7ee7f503f70ed) · [状态效果 S-4ce013ea58e4cdcb](../../evidence/state_effects-sets-017.md#s-4ce013ea58e4cdcb)

### path-025559

```text
(config)# autoconf enable <cr>
```

Handler ` RVA 0xCAEF6F0 `；selector ` 10 `；EOL ` RVA 0x33BAA4B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025457

```text
(config)# avc <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 45 `；EOL ` RVA 0x35240F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b80575e83a50d9d](../../evidence/conditions-sets-030.md#c-4b80575e83a50d9d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025793

```text
(config)# avc sd-service <cr>
```

Handler ` RVA 0x10F26570 `；selector ` 25 `；EOL ` RVA 0x35240CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee3c9205f596a7f6](../../evidence/conditions-sets-092.md#c-ee3c9205f596a7f6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025914

```text
(config)# banner <string> <cr>
```

Handler ` RVA 0xDFEC4A0 `；selector ` 0 `；EOL ` RVA 0x340BA1C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` c banner-text c, where 'c' is a delimiting character。

[条件 C-b0eb493f01a4b337](../../evidence/conditions-sets-068.md#c-b0eb493f01a4b337) · [参数 P-f83754161b2a0b70](../../evidence/parameters-sets-019.md#p-f83754161b2a0b70) · [状态效果 S-11a52ce8c6663545](../../evidence/state_effects-sets-004.md#s-11a52ce8c6663545)

### path-026188

```text
(config)# bba-group pppoe global <cr>
```

Handler ` RVA 0x112543E0 `；selector ` 0 `；EOL ` RVA 0x35434960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-2bf5d63ab7a53bde](../../evidence/state_effects-sets-010.md#s-2bf5d63ab7a53bde)

### path-028069

```text
(config)# beep channel limit <number:257..4294967295> <cr>
```

Handler ` RVA 0xEF604D0 `；selector ` 3 `；EOL ` RVA 0x3448AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum BEEP channels。

[条件 C-172d2b19b84aae43](../../evidence/conditions-sets-009.md#c-172d2b19b84aae43) · [参数 P-47a871d8c3ea43b6](../../evidence/parameters-sets-006.md#p-47a871d8c3ea43b6) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025553

```text
(config)# bfd fast-timers-on-slow-interface <cr>
```

Handler ` RVA 0x10B1F7C0 `；selector ` 0 `；EOL ` RVA 0x34CAEBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026136

```text
(config)# bfd l2cos <number:0..7> <cr>
```

Handler ` RVA 0x10B1D4A0 `；selector ` 0 `；EOL ` RVA 0x34CAE590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value of L2 COS for BFD Pkts over VLAN interfaces。

[条件 C-af7be7ca88ef22ca](../../evidence/conditions-sets-068.md#c-af7be7ca88ef22ca) · [参数 P-b5c73a280c6638ad](../../evidence/parameters-sets-014.md#p-b5c73a280c6638ad) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027942

```text
(config)# bfd l3cos ipv6 <number:0..7> <cr>
```

Handler ` RVA 0x10B1D370 `；selector ` 0 `；EOL ` RVA 0x34CAE920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value of IPV6 L3 COS for BFD packets。

[条件 C-1b94fd1945070017](../../evidence/conditions-sets-011.md#c-1b94fd1945070017) · [参数 P-b725415be63f1cda](../../evidence/parameters-sets-014.md#p-b725415be63f1cda) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060763

```text
(config)# bfd map ipv4 <prefix:dynamic> <string> <cr>
```

Handler ` RVA 0x10B31E90 `；selector ` 5 `；EOL ` RVA 0x34CAFCC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Destination IP prefix/len；` string ` bfd template name。

[条件 C-4efe895f2faa4a85](../../evidence/conditions-sets-031.md#c-4efe895f2faa4a85) · [缺口 G-b359a3589f6cae44](../../evidence/gaps-sets-006.md#g-b359a3589f6cae44) · [参数 P-157c11ec5bd99570](../../evidence/parameters-sets-002.md#p-157c11ec5bd99570) · [状态效果 S-30b12676d611c0a1](../../evidence/state_effects-sets-011.md#s-30b12676d611c0a1)

### path-034093

```text
(config)# bfd neighbor multihop-ipv4 <address> <address> <cr>
```

Handler ` RVA 0x10B4B590 `；selector ` 0 `；EOL ` RVA 0x34CAF4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP Address；` address ` Source IP Address。

[条件 C-6a1fc372ca36852b](../../evidence/conditions-sets-041.md#c-6a1fc372ca36852b) · [参数 P-e5aa527419715a10](../../evidence/parameters-sets-017.md#p-e5aa527419715a10) · [状态效果 S-39c776abce17d12c](../../evidence/state_effects-sets-013.md#s-39c776abce17d12c)

### path-026118

```text
(config)# bfd slow-timers <number:1000..30000> <cr>
```

Handler ` RVA 0x10B1D240 `；selector ` 0 `；EOL ` RVA 0x34CAE240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Value in ms to use for slow timers。

[条件 C-a344bdee8c98f9e5](../../evidence/conditions-sets-063.md#c-a344bdee8c98f9e5) · [参数 P-f375e5037e7b200f](../../evidence/parameters-sets-018.md#p-f375e5037e7b200f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027938

```text
(config)# bfd snmp traps more <cr>
```

Handler ` RVA 0x10B1F6D0 `；selector ` 0 `；EOL ` RVA 0x34CAEF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026114

```text
(config)# bfd-template single-hop <string> <cr>
```

Handler ` RVA 0x10B2F000 `；selector ` 0 `；EOL ` RVA 0x34CB0370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` BFD template name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-70ff01e2ede31908](../../evidence/parameters-sets-009.md#p-70ff01e2ede31908) · [状态效果 S-0288e13b12c38509](../../evidence/state_effects-sets-001.md#s-0288e13b12c38509)

### path-060368

```text
(config)# boot bootldr <url:dynamic> <cr>
```

Handler ` RVA 0xD556020 `；selector ` 0 `；EOL ` RVA 0x33E81818 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ed1aec969a40199f](../../evidence/conditions-sets-092.md#c-ed1aec969a40199f) · [缺口 G-bdffa27e7a39b846](../../evidence/gaps-sets-007.md#g-bdffa27e7a39b846) · [参数 P-699f202968dadc49](../../evidence/parameters-sets-008.md#p-699f202968dadc49) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026070

```text
(config)# boot bootstrap flash <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x341453C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d32d60a6fc9294b5](../../evidence/conditions-sets-081.md#c-d32d60a6fc9294b5) · [状态效果 S-9d87ab08d7b28997](../../evidence/state_effects-sets-033.md#s-9d87ab08d7b28997)

### path-060502

```text
(config)# boot bootstrap flash <url:dynamic> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x341453C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1631b7bc18a2f5b6](../../evidence/conditions-sets-009.md#c-1631b7bc18a2f5b6) · [缺口 G-0d8f40c83d475267](../../evidence/gaps-sets-001.md#g-0d8f40c83d475267) · [参数 P-0a3bd4b5e25a62ac](../../evidence/parameters-sets-001.md#p-0a3bd4b5e25a62ac) · [状态效果 S-9d87ab08d7b28997](../../evidence/state_effects-sets-033.md#s-9d87ab08d7b28997)

### path-027921

```text
(config)# boot bootstrap ftp <string> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x33D86D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` System image filename。

[条件 C-922dfa0fbfa41580](../../evidence/conditions-sets-056.md#c-922dfa0fbfa41580) · [参数 P-64b7b29e25e7ff85](../../evidence/parameters-sets-008.md#p-64b7b29e25e7ff85) · [状态效果 S-a22d7572759a8bac](../../evidence/state_effects-sets-034.md#s-a22d7572759a8bac)

### path-062733

```text
(config)# boot bootstrap ftp <string> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x33D86D10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` System image filename。

[条件 C-d2f354558d377b28](../../evidence/conditions-sets-081.md#c-d2f354558d377b28) · [缺口 G-2a833aead6da2030](../../evidence/gaps-sets-002.md#g-2a833aead6da2030) · [参数 P-64b7b29e25e7ff85](../../evidence/parameters-sets-008.md#p-64b7b29e25e7ff85) · [状态效果 S-46d826979fd82def](../../evidence/state_effects-sets-015.md#s-46d826979fd82def)

### path-027909

```text
(config)# boot bootstrap rcp <string> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x33D7EA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` System image filename。

[条件 C-8033b211b17ecfca](../../evidence/conditions-sets-050.md#c-8033b211b17ecfca) · [参数 P-128ed92b1c40c013](../../evidence/parameters-sets-002.md#p-128ed92b1c40c013) · [状态效果 S-db99d69b925df2aa](../../evidence/state_effects-sets-046.md#s-db99d69b925df2aa)

### path-062732

```text
(config)# boot bootstrap rcp <string> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x33D7EA00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` System image filename。

[条件 C-e2fba0d56e418cf8](../../evidence/conditions-sets-087.md#c-e2fba0d56e418cf8) · [缺口 G-2a833aead6da2030](../../evidence/gaps-sets-002.md#g-2a833aead6da2030) · [参数 P-128ed92b1c40c013](../../evidence/parameters-sets-002.md#p-128ed92b1c40c013) · [状态效果 S-8eb44b27aa37a4d6](../../evidence/state_effects-sets-030.md#s-8eb44b27aa37a4d6)

### path-025425

```text
(config)# boot buffersize <number:0..4294967295> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 6 `；EOL ` RVA 0x34144CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Buffer size。

[条件 C-e37b7e2674cde392](../../evidence/conditions-sets-088.md#c-e37b7e2674cde392) · [参数 P-ce19a8e5817809dd](../../evidence/parameters-sets-016.md#p-ce19a8e5817809dd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060369

```text
(config)# boot config <url:dynamic> <cr>
```

Handler ` RVA 0xE94C290 `；selector ` 0 `；EOL ` RVA 0x343517F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9ba606ef39f42338](../../evidence/conditions-sets-060.md#c-9ba606ef39f42338) · [缺口 G-b64b9251ad9287a7](../../evidence/gaps-sets-006.md#g-b64b9251ad9287a7) · [参数 P-4f63fc9936c26427](../../evidence/parameters-sets-007.md#p-4f63fc9936c26427) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025427

```text
(config)# boot-end-marker <cr>
```

Handler ` RVA 0xDE7FE20 `；selector ` 0 `；EOL ` RVA 0x341460E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f18f2011c5d14bb](../../evidence/conditions-sets-006.md#c-0f18f2011c5d14bb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025426

```text
(config)# boot-start-marker <cr>
```

Handler ` RVA 0xDE7FD60 `；selector ` 0 `；EOL ` RVA 0x34144A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f18f2011c5d14bb](../../evidence/conditions-sets-006.md#c-0f18f2011c5d14bb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060317

```text
(config)# bridge <number:1..255> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 0 `；EOL ` RVA 0x345E3DC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-56b12c7413d2dbcd](../../evidence/conditions-sets-034.md#c-56b12c7413d2dbcd) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060419

```text
(config)# bridge <number:1..255> acquire <cr>
```

Handler ` RVA 0xF282470 `；selector ` 1 `；EOL ` RVA 0x345E19E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060644

```text
(config)# bridge <number:1..255> address <address> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 2 `；EOL ` RVA 0x345E1D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` address ` Ethernet address。

[条件 C-26eedbefa413bc9f](../../evidence/conditions-sets-015.md#c-26eedbefa413bc9f) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-3ba8095abf9448f5](../../evidence/parameters-sets-005.md#p-3ba8095abf9448f5) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060304

```text
(config)# bridge <number:1..255> aging-time <number:10..1000000> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 4 `；EOL ` RVA 0x345E2258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Seconds。

[条件 C-29b532cd54ae546e](../../evidence/conditions-sets-016.md#c-29b532cd54ae546e) · [缺口 G-2e66173b5a8013e3](../../evidence/gaps-sets-002.md#g-2e66173b5a8013e3) · [参数 P-98ae9c81aed69833](../../evidence/parameters-sets-012.md#p-98ae9c81aed69833) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060414

```text
(config)# bridge <number:1..255> bitswap-layer3-addresses <cr>
```

Handler ` RVA 0xF282470 `；selector ` 23 `；EOL ` RVA 0x345E09F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-062754

```text
(config)# bridge <number:1..255> bridge <?protoname_action@555589b35730> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 20 `；EOL ` RVA 0x345E1768 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-33dba5a5323ac4c7](../../evidence/gaps-sets-002.md#g-33dba5a5323ac4c7) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060653

```text
(config)# bridge <number:1..255> circuit-group <number:1..9> pause <number:0..10000> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 13 `；EOL ` RVA 0x345E3560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Circuit group number；` unsigned_number ` Circuit group pause interval。

[条件 C-a4ef9536a32bd92d](../../evidence/conditions-sets-064.md#c-a4ef9536a32bd92d) · [缺口 G-c8db4032d2feca9e](../../evidence/gaps-sets-007.md#g-c8db4032d2feca9e) · [参数 P-1c160380d31eb000](../../evidence/parameters-sets-003.md#p-1c160380d31eb000) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060906

```text
(config)# bridge <number:1..255> circuit-group <number:1..9> slow-convergence <cr>
```

Handler ` RVA 0xF282470 `；selector ` 15 `；EOL ` RVA 0x345E3848 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Circuit group number。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-f7e7cc54da606e01](../../evidence/parameters-sets-018.md#p-f7e7cc54da606e01) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060910

```text
(config)# bridge <number:1..255> circuit-group <number:1..9> source-based <cr>
```

Handler ` RVA 0xF282470 `；selector ` 14 `；EOL ` RVA 0x345E3AF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Circuit group number。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-f7e7cc54da606e01](../../evidence/parameters-sets-018.md#p-f7e7cc54da606e01) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060302

```text
(config)# bridge <number:1..255> domain <number:1..10> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 3 `；EOL ` RVA 0x345E1CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Domain number。

[条件 C-e823bff39c5ae75e](../../evidence/conditions-sets-090.md#c-e823bff39c5ae75e) · [缺口 G-2bb16d333e6a99ba](../../evidence/gaps-sets-002.md#g-2bb16d333e6a99ba) · [参数 P-1706ba9633de785b](../../evidence/parameters-sets-002.md#p-1706ba9633de785b) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060305

```text
(config)# bridge <number:1..255> forward-time <number:4..200> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 5 `；EOL ` RVA 0x345E24F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Seconds。

[条件 C-303ae07bf8d42ce4](../../evidence/conditions-sets-019.md#c-303ae07bf8d42ce4) · [缺口 G-ba88019b07fbd8b5](../../evidence/gaps-sets-007.md#g-ba88019b07fbd8b5) · [参数 P-dcac039e08326a61](../../evidence/parameters-sets-017.md#p-dcac039e08326a61) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060307

```text
(config)# bridge <number:1..255> hello-time <number:1..10> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 6 `；EOL ` RVA 0x345E2798 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Seconds。

[条件 C-31e76dd0fd3457d2](../../evidence/conditions-sets-020.md#c-31e76dd0fd3457d2) · [缺口 G-38c2cb7aec284d61](../../evidence/gaps-sets-002.md#g-38c2cb7aec284d61) · [参数 P-520b75e38823ede4](../../evidence/parameters-sets-007.md#p-520b75e38823ede4) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060424

```text
(config)# bridge <number:1..255> lat-service-filtering <cr>
```

Handler ` RVA 0xF282470 `；selector ` 11 `；EOL ` RVA 0x345E2CD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-061346

```text
(config)# bridge <number:1..255> management-domain <string> vlan-id <number:1..1005> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 21 `；EOL ` RVA 0x345E0DB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` string ` Name of the management domain；` unsigned_number ` The VLAN ID associated with the bridge group。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-60ad9e6b81e45b8b](../../evidence/parameters-sets-008.md#p-60ad9e6b81e45b8b) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060310

```text
(config)# bridge <number:1..255> max-age <number:6..200> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 7 `；EOL ` RVA 0x345E2D00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Seconds。

[条件 C-87d3bf11e7d9d86c](../../evidence/conditions-sets-053.md#c-87d3bf11e7d9d86c) · [缺口 G-7cf9dd41b761b20c](../../evidence/gaps-sets-005.md#g-7cf9dd41b761b20c) · [参数 P-a1a15c2bf12b001e](../../evidence/parameters-sets-012.md#p-a1a15c2bf12b001e) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060313

```text
(config)# bridge <number:1..255> priority <number:0..65535> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 9 `；EOL ` RVA 0x345E2F80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.；` unsigned_number ` Priority (low priority more likely to be root)。

[条件 C-e204b25795e2ea29](../../evidence/conditions-sets-087.md#c-e204b25795e2ea29) · [缺口 G-20a4d35acc18ee26](../../evidence/gaps-sets-002.md#g-20a4d35acc18ee26) · [参数 P-2bdce6ce591cae86](../../evidence/parameters-sets-004.md#p-2bdce6ce591cae86) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060416

```text
(config)# bridge <number:1..255> protocol <cr>
```

Handler ` RVA 0xF282470 `；selector ` 10 `；EOL ` RVA 0x345E0448 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-b6b9548c28ae5326](../../evidence/conditions-sets-071.md#c-b6b9548c28ae5326) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-062752

```text
(config)# bridge <number:1..255> route <?protoname_action@555589b35418> <cr>
```

Handler ` RVA 0xF282470 `；selector ` 19 `；EOL ` RVA 0x345E1450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-ac7b4f4c8078d622](../../evidence/gaps-sets-006.md#g-ac7b4f4c8078d622) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-9ceda5b3b9ae21c8](../../evidence/state_effects-sets-033.md#s-9ceda5b3b9ae21c8)

### path-060420

```text
(config)# bridge <number:1..255> subscriber-policy <cr>
```

Handler ` RVA 0xF282470 `；selector ` 22 `；EOL ` RVA 0x345E10F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Bridge Group number for Bridging.。

[条件 C-00421c3a5c9a18a2](../../evidence/conditions-sets-001.md#c-00421c3a5c9a18a2) · [缺口 G-57b630c224bf965c](../../evidence/gaps-sets-004.md#g-57b630c224bf965c) · [参数 P-16811c6203f5919d](../../evidence/parameters-sets-002.md#p-16811c6203f5919d) · [状态效果 S-b3246947e3979265](../../evidence/state_effects-sets-038.md#s-b3246947e3979265)

### path-025616

```text
(config)# bridge crb <cr>
```

Handler ` RVA 0xF282470 `；selector ` 17 `；EOL ` RVA 0x345E8740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7b718e2fdaf7840](../../evidence/conditions-sets-096.md#c-f7b718e2fdaf7840) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025618

```text
(config)# bridge irb <cr>
```

Handler ` RVA 0xF282470 `；selector ` 18 `；EOL ` RVA 0x345E89E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f7b718e2fdaf7840](../../evidence/conditions-sets-096.md#c-f7b718e2fdaf7840) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025621

```text
(config)# bridge mac-address-table limit <number:0..1000200> <cr>
```

Handler ` RVA 0xF285B00 `；selector ` 24 `；EOL ` RVA 0x345E8C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Entries (0 disables limit,others rounded up to multiple of 300)。

[条件 C-e400a682a85e60cb](../../evidence/conditions-sets-088.md#c-e400a682a85e60cb) · [参数 P-8d53b5916eb41edf](../../evidence/parameters-sets-011.md#p-8d53b5916eb41edf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060287

```text
(config)# bridge-domain <number:dynamic> <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 1 `；EOL ` RVA 0x3395A310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` bridge-domain ID。

[条件 C-d220c8383e8a1b0d](../../evidence/conditions-sets-081.md#c-d220c8383e8a1b0d) · [缺口 G-07ec2ab967fec45c](../../evidence/gaps-sets-001.md#g-07ec2ab967fec45c) · [参数 P-4b0a5806e2d2136e](../../evidence/parameters-sets-006.md#p-4b0a5806e2d2136e) · [状态效果 S-e9567302d7d6095f](../../evidence/state_effects-sets-049.md#s-e9567302d7d6095f)

### path-060516

```text
(config)# bridge-domain c-mac aging-time <number:dynamic> <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 2 `；EOL ` RVA 0x3395A7A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Aging time in second, default 300 seconds (or 1800 seconds for overlay bridge domains)。

[条件 C-7cd2a9df6abed307](../../evidence/conditions-sets-048.md#c-7cd2a9df6abed307) · [缺口 G-e3bce02c090b3c8c](../../evidence/gaps-sets-008.md#g-e3bce02c090b3c8c) · [参数 P-679f03bc65ef2033](../../evidence/parameters-sets-008.md#p-679f03bc65ef2033) · [状态效果 S-e9567302d7d6095f](../../evidence/state_effects-sets-049.md#s-e9567302d7d6095f)

### path-060765

```text
(config)# bridge-domain otv default age-time <number:dynamic> <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 3 `；EOL ` RVA 0x3395AC28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Default aging time in seconds for overlay bridge domains。

[条件 C-de0b8321593406c3](../../evidence/conditions-sets-086.md#c-de0b8321593406c3) · [缺口 G-c50d803b195564d3](../../evidence/gaps-sets-007.md#g-c50d803b195564d3) · [参数 P-2a644fe097e2fc1a](../../evidence/parameters-sets-004.md#p-2a644fe097e2fc1a) · [状态效果 S-e9567302d7d6095f](../../evidence/state_effects-sets-049.md#s-e9567302d7d6095f)

### path-026232

```text
(config)# bridge-domain parameterized vlan <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 1 `；EOL ` RVA 0x3395A310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43135ad2f0a46eea](../../evidence/conditions-sets-026.md#c-43135ad2f0a46eea) · [状态效果 S-770570f992de80eb](../../evidence/state_effects-sets-025.md#s-770570f992de80eb)

### path-026458

```text
(config)# bstun keepalive-count <number:2..10> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 3 `；EOL ` RVA 0x354BDB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of retries must be between 2 and 10。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [参数 P-d3ed36225ef390ec](../../evidence/parameters-sets-016.md#p-d3ed36225ef390ec) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026367

```text
(config)# bstun lisnsap <number:0..255> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 4 `；EOL ` RVA 0x354BCEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` listening SAP。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [参数 P-5e09a37a7c45525f](../../evidence/parameters-sets-008.md#p-5e09a37a7c45525f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026409

```text
(config)# bstun peer-name <address> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 0 `；EOL ` RVA 0x354BD1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address which identifies this BSTUN peer。

[条件 C-b17301b62b73069b](../../evidence/conditions-sets-069.md#c-b17301b62b73069b) · [参数 P-1d53f73fd992625f](../../evidence/parameters-sets-003.md#p-1d53f73fd992625f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028285

```text
(config)# bstun protocol-group <number:1..255> <string> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 1 `；EOL ` RVA 0x354BD560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` A BSTUN protocol group number；` string ` Protocol name (max 20 characters)。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [参数 P-13d35ab50d14ac7e](../../evidence/parameters-sets-002.md#p-13d35ab50d14ac7e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025662

```text
(config)# bstun remote-peer-keepalive <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 2 `；EOL ` RVA 0x354BD890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [状态效果 S-aea64587352c5c32](../../evidence/state_effects-sets-037.md#s-aea64587352c5c32)

### path-060387

```text
(config)# buffers <interface> permanent <cr>
```

Handler ` RVA 0xE3E06B0 `；selector ` 0 `；EOL ` RVA 0x342BB760 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a8f6a5bbf7f2ce14](../../evidence/conditions-sets-065.md#c-a8f6a5bbf7f2ce14) · [缺口 G-62dd2cb446eb5381](../../evidence/gaps-sets-004.md#g-62dd2cb446eb5381) · [参数 P-ebc430337b68e89f](../../evidence/parameters-sets-018.md#p-ebc430337b68e89f) · [状态效果 S-5bc541d517ccd282](../../evidence/state_effects-sets-020.md#s-5bc541d517ccd282)

### path-028137

```text
(config)# buffers element permanent <number:100..500> <cr>
```

Handler ` RVA 0xE3E08A0 `；selector ` 0 `；EOL ` RVA 0x342BAF18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of minimum elements。

[条件 C-03d86c2727661d4d](../../evidence/conditions-sets-002.md#c-03d86c2727661d4d) · [参数 P-dbd2657b59fc4dfd](../../evidence/parameters-sets-017.md#p-dbd2657b59fc4dfd) · [状态效果 S-c09ddbca209fdc7a](../../evidence/state_effects-sets-041.md#s-c09ddbca209fdc7a)

### path-028228

```text
(config)# buffers header permanent <number:256..65535> <cr>
```

Handler ` RVA 0xE3E06B0 `；selector ` 0 `；EOL ` RVA 0x342BB760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of header particles。

[条件 C-4174dd04b7fca8bb](../../evidence/conditions-sets-026.md#c-4174dd04b7fca8bb) · [参数 P-61d08c38a9d68c84](../../evidence/parameters-sets-008.md#p-61d08c38a9d68c84) · [状态效果 S-f3dddf3862d800f1](../../evidence/state_effects-sets-052.md#s-f3dddf3862d800f1)

### path-026311

```text
(config)# buffers particle-clone <number:1..65535> <cr>
```

Handler ` RVA 0xE3E0700 `；selector ` 0 `；EOL ` RVA 0x342BB348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of particle clones to grow。

[条件 C-4ba5aef31712da2e](../../evidence/conditions-sets-030.md#c-4ba5aef31712da2e) · [参数 P-14976883970c510b](../../evidence/parameters-sets-002.md#p-14976883970c510b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026455

```text
(config)# buffers tune automatic <cr>
```

Handler ` RVA 0xE3E0AC0 `；selector ` 0 `；EOL ` RVA 0x342BC060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060473

```text
(config)# bulkstat data <string> <cr>
```

Handler ` RVA 0xBC67E60 `；selector ` 0 `；EOL ` RVA 0x3387FEE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Data-set name。

[条件 C-0d0d838fbb5db4ad](../../evidence/conditions-sets-005.md#c-0d0d838fbb5db4ad) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-8bbae91b8ae80aef](../../evidence/parameters-sets-011.md#p-8bbae91b8ae80aef) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060482

```text
(config)# bulkstat data-group <string> <cr>
```

Handler ` RVA 0xBC67580 `；selector ` 0 `；EOL ` RVA 0x33880970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Data-group Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-f9831b4aa7d39088](../../evidence/parameters-sets-019.md#p-f9831b4aa7d39088) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060477

```text
(config)# bulkstat filter <string> <cr>
```

Handler ` RVA 0xBC67A20 `；selector ` 0 `；EOL ` RVA 0x33880648 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` filter-set name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-54692b5a968bcca2](../../evidence/parameters-sets-007.md#p-54692b5a968bcca2) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060479

```text
(config)# bulkstat instance <string> <cr>
```

Handler ` RVA 0xBC68440 `；selector ` 0 `；EOL ` RVA 0x338802C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Instance-set name。

[条件 C-1068973eb0bd2d6b](../../evidence/conditions-sets-007.md#c-1068973eb0bd2d6b) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-b12602b327cdb46f](../../evidence/parameters-sets-013.md#p-b12602b327cdb46f) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060487

```text
(config)# bulkstat profile <string> <cr>
```

Handler ` RVA 0xBC670D0 `；selector ` 0 `；EOL ` RVA 0x33880C90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` profile name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-8a3a3a59486849a2](../../evidence/parameters-sets-011.md#p-8a3a3a59486849a2) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060485

```text
(config)# bulkstat resource limit memory <number:20..100> <cr>
```

Handler ` RVA 0xBC68A10 `；selector ` 0 `；EOL ` RVA 0x33880F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` % of memory resource。

[条件 C-7f52c1d7fe9c0314](../../evidence/conditions-sets-049.md#c-7f52c1d7fe9c0314) · [缺口 G-157347f82e78cc72](../../evidence/gaps-sets-001.md#g-157347f82e78cc72) · [参数 P-cbcdbfcd10be6809](../../evidence/parameters-sets-015.md#p-cbcdbfcd10be6809) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060493

```text
(config)# bulkstat schedule <string> <cr>
```

Handler ` RVA 0xBC6DE70 `；selector ` 0 `；EOL ` RVA 0x33881328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` The name of this calendar shchedule。

[条件 C-7cf183d34babfe61](../../evidence/conditions-sets-048.md#c-7cf183d34babfe61) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-76f18b5cdebd013a](../../evidence/parameters-sets-009.md#p-76f18b5cdebd013a) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-026739

```text
(config)# busy-message <string> <string> <cr>
```

Handler ` RVA 0xCCF4560 `；selector ` 127 `；EOL ` RVA 0x33C60A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Hostname；` string ` Busy Message。

[条件 C-fc99c5089340eb06](../../evidence/conditions-sets-097.md#c-fc99c5089340eb06) · [参数 P-a160e476de0ef396](../../evidence/parameters-sets-012.md#p-a160e476de0ef396) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028918

```text
(config)# call admission cpu-limit <number:0..100> <cr>
```

Handler ` RVA 0xDEB0F40 `；selector ` 0 `；EOL ` RVA 0x3408D738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CPU load at which CAC should reject (newmodel)。

[条件 C-c8f9108955eb5f9b](../../evidence/conditions-sets-077.md#c-c8f9108955eb5f9b) · [参数 P-9496c47f4f0afec7](../../evidence/parameters-sets-011.md#p-9496c47f4f0afec7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028972

```text
(config)# call admission cpu-load 5sec-cpu-load <cr>
```

Handler ` RVA 0xDEB0FE0 `；selector ` 0 `；EOL ` RVA 0x3408DA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aeda781354f400ef](../../evidence/conditions-sets-068.md#c-aeda781354f400ef) · [状态效果 S-d35c2b5a9d584f1d](../../evidence/state_effects-sets-045.md#s-d35c2b5a9d584f1d)

### path-035238

```text
(config)# call admission ike <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 4 `；EOL ` RVA 0x3408EB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [参数 P-290d5e8e909d7201](../../evidence/parameters-sets-004.md#p-290d5e8e909d7201) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035049

```text
(config)# call admission ip <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 3 `；EOL ` RVA 0x3408DDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [参数 P-0f63ad6b4db446cf](../../evidence/parameters-sets-002.md#p-0f63ad6b4db446cf) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028811

```text
(config)# call admission limit <number:0..100000> <cr>
```

Handler ` RVA 0xDEB0D00 `；selector ` 0 `；EOL ` RVA 0x3408D108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Total charge。

[条件 C-03f1dd0bbd616c22](../../evidence/conditions-sets-002.md#c-03f1dd0bbd616c22) · [参数 P-91fecd55ec124826](../../evidence/parameters-sets-011.md#p-91fecd55ec124826) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035346

```text
(config)# call admission load <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 5 `；EOL ` RVA 0x3408EE68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Multiplier, value at 100% load；` unsigned_number ` Load Metric Poll Rate (seconds)。

[条件 C-b41b55a8f971f5cc](../../evidence/conditions-sets-070.md#c-b41b55a8f971f5cc) · [参数 P-6a97b0517a61ce85](../../evidence/parameters-sets-008.md#p-6a97b0517a61ce85) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026916

```text
(config)# call admission new-model <cr>
```

Handler ` RVA 0xDEB11C0 `；selector ` 0 `；EOL ` RVA 0x3408F3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026890

```text
(config)# call admission padr <cr>
```

Handler ` RVA 0xDEB1160 `；selector ` 0 `；EOL ` RVA 0x3408F138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035191

```text
(config)# call admission pppoa <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 2 `；EOL ` RVA 0x3408E470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-5ad4ed3e60890e6c](../../evidence/conditions-sets-036.md#c-5ad4ed3e60890e6c) · [参数 P-f3120ec65d402de5](../../evidence/parameters-sets-018.md#p-f3120ec65d402de5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035136

```text
(config)# call admission pppoe <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 1 `；EOL ` RVA 0x3408E110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-e32ad50f655dbf8d](../../evidence/conditions-sets-087.md#c-e32ad50f655dbf8d) · [参数 P-268decfafca8fd6d](../../evidence/parameters-sets-003.md#p-268decfafca8fd6d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028875

```text
(config)# call admission session-limit <number:0..1280000> <cr>
```

Handler ` RVA 0xDEB0EA0 `；selector ` 0 `；EOL ` RVA 0x3408D420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Total Number of Sessions。

[条件 C-06d1da45a193ce64](../../evidence/conditions-sets-003.md#c-06d1da45a193ce64) · [参数 P-5e3852db19c6a435](../../evidence/parameters-sets-008.md#p-5e3852db19c6a435) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035244

```text
(config)# call admission vpdn <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 0 `；EOL ` RVA 0x3408E7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-ec736277ca0a844c](../../evidence/conditions-sets-091.md#c-ec736277ca0a844c) · [参数 P-cdaa29a8eb82638d](../../evidence/parameters-sets-016.md#p-cdaa29a8eb82638d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060566

```text
(config)# call filter match-list <?gcfm_matchlist_voice_cmd@55558b5afcc8> <cr>
```

Handler ` RVA 0x16988170 `；selector ` 1 `；EOL ` RVA 0x3605B748 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-73bac8fb899f0385](../../evidence/conditions-sets-045.md#c-73bac8fb899f0385) · [缺口 G-df6c73332fb6b400](../../evidence/gaps-sets-008.md#g-df6c73332fb6b400) · [状态效果 S-98569a2057671d8a](../../evidence/state_effects-sets-032.md#s-98569a2057671d8a)

### path-060814

```text
(config)# call filter match-list <?gcfm_matchlist_voice_cmd@55558b5afcc8> gatekeeper <cr>
```

Handler ` RVA 0x16988170 `；selector ` 2 `；EOL ` RVA 0x3605B7F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e977f980dc771ed](../../evidence/conditions-sets-061.md#c-9e977f980dc771ed) · [缺口 G-df6c73332fb6b400](../../evidence/gaps-sets-008.md#g-df6c73332fb6b400) · [状态效果 S-98569a2057671d8a](../../evidence/state_effects-sets-032.md#s-98569a2057671d8a)

### path-029157

```text
(config)# call filter match-list gatekeeper <cr>
```

Handler ` RVA 0x16988170 `；selector ` 2 `；EOL ` RVA 0x3605B7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8215da2fe78c01f](../../evidence/conditions-sets-083.md#c-d8215da2fe78c01f) · [状态效果 S-98569a2057671d8a](../../evidence/state_effects-sets-032.md#s-98569a2057671d8a)

### path-029066

```text
(config)# call filter match-list voice <cr>
```

Handler ` RVA 0x16988170 `；selector ` 1 `；EOL ` RVA 0x3605B748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc25383658f409c7](../../evidence/conditions-sets-097.md#c-fc25383658f409c7) · [状态效果 S-98569a2057671d8a](../../evidence/state_effects-sets-032.md#s-98569a2057671d8a)

### path-025490

```text
(config)# call-history-mib max-size <number:0..500> <cr>
```

Handler ` RVA 0x1612B140 `；selector ` 0 `；EOL ` RVA 0x35EE00C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries in the call history mib table。

[条件 C-f357413bdb2dcf08](../../evidence/conditions-sets-094.md#c-f357413bdb2dcf08) · [参数 P-14db4e7c8bd805d4](../../evidence/parameters-sets-002.md#p-14db4e7c8bd805d4) · [状态效果 S-5a131b77a46b690c](../../evidence/state_effects-sets-019.md#s-5a131b77a46b690c)

### path-025489

```text
(config)# call-history-mib retain-timer <number:0..500> <cr>
```

Handler ` RVA 0x1612B140 `；selector ` 1 `；EOL ` RVA 0x35EE0068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time (in minutes) for removing an entry。

[条件 C-cbc0ce08f05626f4](../../evidence/conditions-sets-078.md#c-cbc0ce08f05626f4) · [参数 P-9d3a7ccb2ce8a748](../../evidence/parameters-sets-012.md#p-9d3a7ccb2ce8a748) · [状态效果 S-5a131b77a46b690c](../../evidence/state_effects-sets-019.md#s-5a131b77a46b690c)

### path-060280

```text
(config)# call-home <cr>
```

Handler ` RVA 0xB6C7C50 `；selector ` 0 `；EOL ` RVA 0x337EE900 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d3837a84f518b99f](../../evidence/conditions-sets-082.md#c-d3837a84f518b99f) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060440

```text
(config)# call-home reporting anonymous <cr>
```

Handler ` RVA 0xB6D0B80 `；selector ` 0 `；EOL ` RVA 0x337EE530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-48a579e09c86df4f](../../evidence/conditions-sets-029.md#c-48a579e09c86df4f) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-5e4c58ee7b5576aa](../../evidence/state_effects-sets-020.md#s-5e4c58ee7b5576aa)

### path-062946

```text
(config)# card type t1 <number:dynamic> <cr>
```

Handler ` RVA 0xED7E290 `；selector ` 0 `；EOL ` RVA 0x34421BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Card slot number。

[条件 C-cf3a4aaad5c787cb](../../evidence/conditions-sets-080.md#c-cf3a4aaad5c787cb) · [缺口 G-3043846df2675db9](../../evidence/gaps-sets-002.md#g-3043846df2675db9) · [参数 P-af624c103f5218ad](../../evidence/parameters-sets-013.md#p-af624c103f5218ad) · [状态效果 S-0fc0b96091d6a27f](../../evidence/state_effects-sets-004.md#s-0fc0b96091d6a27f)

### path-025949

```text
(config)# carrier-id <string> <cr>
```

Handler ` RVA 0x1E3CD110 `；selector ` 14 `；EOL ` RVA 0x37908E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Carrier identifier。

[条件 C-dbf6109ea713c24f](../../evidence/conditions-sets-085.md#c-dbf6109ea713c24f) · [参数 P-62becbd9c2cf4815](../../evidence/parameters-sets-008.md#p-62becbd9c2cf4815) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027436

```text
(config)# carrier-id <string> cic <cr>
```

Handler ` RVA 0x1E3CD110 `；selector ` 15 `；EOL ` RVA 0x37908EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Carrier identifier。

[条件 C-dbf6109ea713c24f](../../evidence/conditions-sets-085.md#c-dbf6109ea713c24f) · [参数 P-62becbd9c2cf4815](../../evidence/parameters-sets-008.md#p-62becbd9c2cf4815) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025562

```text
(config)# cdp advertise-v2 <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 4 `；EOL ` RVA 0x33CE2238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-06df25eb97fd6633](../../evidence/conditions-sets-003.md#c-06df25eb97fd6633) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026322

```text
(config)# cdp filter-tlv-list <string> <cr>
```

Handler ` RVA 0xCD9E990 `；selector ` 0 `；EOL ` RVA 0x33CE3FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Filter tlv-list。

[条件 C-5b7d8887077493a1](../../evidence/conditions-sets-036.md#c-5b7d8887077493a1) · [参数 P-c824308fcdb2caee](../../evidence/parameters-sets-015.md#p-c824308fcdb2caee) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025433

```text
(config)# cdp holdtime <number:10..255> <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 2 `；EOL ` RVA 0x33CE24E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Length of time (in sec) that receiver must keep this packet 。

[条件 C-36b763a93cd5054a](../../evidence/conditions-sets-021.md#c-36b763a93cd5054a) · [参数 P-c2def3c9b98a80c4](../../evidence/parameters-sets-015.md#p-c2def3c9b98a80c4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028006

```text
(config)# cdp log mismatch duplex <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 6 `；EOL ` RVA 0x33CE2B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1a3d3d7ed5c4d4fa](../../evidence/conditions-sets-010.md#c-1a3d3d7ed5c4d4fa) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060512

```text
(config)# cdp mgmt-address ipv4 <address> <cr>
```

Handler ` RVA 0xCDA0260 `；selector ` 1 `；EOL ` RVA 0x33CE1C68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IP address of switch。

[条件 C-b2340e63386c0a34](../../evidence/conditions-sets-069.md#c-b2340e63386c0a34) · [缺口 G-9281bac5dfc4af0b](../../evidence/gaps-sets-005.md#g-9281bac5dfc4af0b) · [参数 P-175b49b5a6f47524](../../evidence/parameters-sets-002.md#p-175b49b5a6f47524) · [状态效果 S-e91b44de505928ec](../../evidence/state_effects-sets-049.md#s-e91b44de505928ec)

### path-060513

```text
(config)# cdp mgmt-address ipv6 <address> <cr>
```

Handler ` RVA 0xCDA0AD0 `；selector ` 1 `；EOL ` RVA 0x33CE1FA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` IPV6 address of switch。

[条件 C-b2340e63386c0a34](../../evidence/conditions-sets-069.md#c-b2340e63386c0a34) · [缺口 G-1743d5b39c40d055](../../evidence/gaps-sets-001.md#g-1743d5b39c40d055) · [参数 P-91670a2062f46016](../../evidence/parameters-sets-011.md#p-91670a2062f46016) · [状态效果 S-2be9a8458a71009b](../../evidence/state_effects-sets-010.md#s-2be9a8458a71009b)

### path-025605

```text
(config)# cdp run <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 0 `；EOL ` RVA 0x33CE3250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9bbbf4f0d591d83f](../../evidence/conditions-sets-060.md#c-9bbbf4f0d591d83f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060376

```text
(config)# cdp source-interface <interface> <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 5 `；EOL ` RVA 0x33CE2EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bd8caa604735ff86](../../evidence/conditions-sets-073.md#c-bd8caa604735ff86) · [缺口 G-a8a642edb6ea4d47](../../evidence/gaps-sets-006.md#g-a8a642edb6ea4d47) · [参数 P-39813cce4c36213e](../../evidence/parameters-sets-005.md#p-39813cce4c36213e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025431

```text
(config)# cdp timer <number:5..254> <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 1 `；EOL ` RVA 0x33CE2260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rate at which CDP packets are sent (in sec)。

[条件 C-9bdc022dccbda10d](../../evidence/conditions-sets-060.md#c-9bdc022dccbda10d) · [参数 P-b6a707b5ca92eea9](../../evidence/parameters-sets-014.md#p-b6a707b5ca92eea9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026334

```text
(config)# cdp tlv app <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 8 `；EOL ` RVA 0x33CE38F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3c22a7479591fc0](../../evidence/conditions-sets-076.md#c-c3c22a7479591fc0) · [状态效果 S-980d2f65907c41a5](../../evidence/state_effects-sets-032.md#s-980d2f65907c41a5)

### path-026289

```text
(config)# cdp tlv location <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 8 `；EOL ` RVA 0x33CE35B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3504ec8090020a69](../../evidence/conditions-sets-021.md#c-3504ec8090020a69) · [状态效果 S-9351f403fd2ff079](../../evidence/state_effects-sets-031.md#s-9351f403fd2ff079)

### path-026306

```text
(config)# cdp tlv-list <string> <cr>
```

Handler ` RVA 0xCD9DBD0 `；selector ` 0 `；EOL ` RVA 0x33CE3CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Tlv-list。

[条件 C-549e45da6980b349](../../evidence/conditions-sets-033.md#c-549e45da6980b349) · [参数 P-af7cf7003dc8a9d1](../../evidence/parameters-sets-013.md#p-af7cf7003dc8a9d1) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025619

```text
(config)# cef common <cr>
```

Handler ` RVA 0xB5AEF90 `；selector ` 0 `；EOL ` RVA 0x337AE698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-00573d6238a90e3d](../../evidence/conditions-sets-001.md#c-00573d6238a90e3d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028408

```text
(config)# cef table consistency-check IPv4 <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 1 `；EOL ` RVA 0x337AFCD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-108862e71d524c23](../../evidence/conditions-sets-007.md#c-108862e71d524c23) · [状态效果 S-3883e13083543607](../../evidence/state_effects-sets-013.md#s-3883e13083543607)

### path-034547

```text
(config)# cef table consistency-check IPv4 auto-repair <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 3 `；EOL ` RVA 0x337AFD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-baaa236f7dfc6ec9](../../evidence/conditions-sets-072.md#c-baaa236f7dfc6ec9) · [状态效果 S-3883e13083543607](../../evidence/state_effects-sets-013.md#s-3883e13083543607)

### path-034304

```text
(config)# cef table consistency-check IPv4 data-checking <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 4 `；EOL ` RVA 0x337AF720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf71e5d6bf7e76f4](../../evidence/conditions-sets-080.md#c-cf71e5d6bf7e76f4) · [状态效果 S-3883e13083543607](../../evidence/state_effects-sets-013.md#s-3883e13083543607)

### path-034338

```text
(config)# cef table consistency-check IPv4 error-message <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 2 `；EOL ` RVA 0x337AF9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cf71e5d6bf7e76f4](../../evidence/conditions-sets-080.md#c-cf71e5d6bf7e76f4) · [状态效果 S-3883e13083543607](../../evidence/state_effects-sets-013.md#s-3883e13083543607)

### path-061217

```text
(config)# cef table consistency-check IPv4 type <?option@555588d03198> <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 0 `；EOL ` RVA 0x337AF298 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-caee63450992c378](../../evidence/conditions-sets-078.md#c-caee63450992c378) · [缺口 G-23fdc2f228fdf65c](../../evidence/gaps-sets-002.md#g-23fdc2f228fdf65c) · [状态效果 S-3883e13083543607](../../evidence/state_effects-sets-013.md#s-3883e13083543607)

### path-044265

```text
(config)# cef table download recursive-dependents priority 1 <cr>
```

Handler ` RVA 0xB2D7FF0 `；selector ` 0 `；EOL ` RVA 0x33734250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d6c4f2e0e562255](../../evidence/conditions-sets-024.md#c-3d6c4f2e0e562255) · [状态效果 S-14f2f17616ee9b29](../../evidence/state_effects-sets-005.md#s-14f2f17616ee9b29)

### path-034416

```text
(config)# cef table output-chain build inplace-modify <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 6 `；EOL ` RVA 0x337B0728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-cb64bd0ab942a115](../../evidence/state_effects-sets-043.md#s-cb64bd0ab942a115)

### path-028248

```text
(config)# cef table rate-monitor-period <number:1..60> <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 7 `；EOL ` RVA 0x337B0390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Period in minutes。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-8b1a86b9e0c550f0](../../evidence/parameters-sets-011.md#p-8b1a86b9e0c550f0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-052158

```text
(config)# cef table vrf tree ipv4 type mtrie <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 5 `；EOL ` RVA 0x337AEAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-551965890a6ebe57](../../evidence/conditions-sets-033.md#c-551965890a6ebe57) · [状态效果 S-0e1d5db1d7f2eede](../../evidence/state_effects-sets-003.md#s-0e1d5db1d7f2eede)

### path-060278

```text
(config)# cfg-mode <cr>
```

Handler ` RVA 0xDF03C10 `；selector ` 15 `；EOL ` RVA 0x340BBA78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-027358

```text
(config)# chat-script <string> <string> <cr>
```

Handler ` RVA 0xF2F26F0 `；selector ` 0 `；EOL ` RVA 0x34603588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of chat script；` string ` Chat script in form EXPECT SEND EXPECT SEND ...。

[条件 C-61fe69aff56b2646](../../evidence/conditions-sets-038.md#c-61fe69aff56b2646) · [参数 P-93121ef6fe6c4947](../../evidence/parameters-sets-011.md#p-93121ef6fe6c4947) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025640

```text
(config)# cisp enable <cr>
```

Handler ` RVA 0xCB250A0 `；selector ` 1 `；EOL ` RVA 0x33BB5180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025631

```text
(config)# class-map <string> <cr>
```

Handler ` RVA 0xD8806E0 `；selector ` 0 `；EOL ` RVA 0x33F141E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` class-map name。

[条件 C-46ffbf7f816d27a4](../../evidence/conditions-sets-028.md#c-46ffbf7f816d27a4) · [参数 P-2990068f5234917c](../../evidence/parameters-sets-004.md#p-2990068f5234917c) · [状态效果 S-0f656c09c41cd71c](../../evidence/state_effects-sets-004.md#s-0f656c09c41cd71c)

### path-028586

```text
(config)# class-map type control <string> <cr>
```

Handler ` RVA 0x10A59FE0 `；selector ` 0 `；EOL ` RVA 0x34C21928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of class-map。

[条件 C-691e8554f9f8451b](../../evidence/conditions-sets-041.md#c-691e8554f9f8451b) · [参数 P-8bacc2b4896dc45c](../../evidence/parameters-sets-011.md#p-8bacc2b4896dc45c) · [状态效果 S-f899988972801792](../../evidence/state_effects-sets-053.md#s-f899988972801792)

### path-044306

```text
(config)# class-map type control subscriber match-all <string> <cr>
```

Handler ` RVA 0xCB630C0 `；selector ` 0 `；EOL ` RVA 0x33BF7BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of identity class-map。

[条件 C-584eb74e3857a35d](../../evidence/conditions-sets-035.md#c-584eb74e3857a35d) · [参数 P-2b4f16183757da84](../../evidence/parameters-sets-004.md#p-2b4f16183757da84) · [状态效果 S-ad46c04aa7cae038](../../evidence/state_effects-sets-037.md#s-ad46c04aa7cae038)

### path-028155

```text
(config)# class-map type multicast-flows <string> <cr>
```

Handler ` RVA 0xF6D0ED0 `；selector ` 0 `；EOL ` RVA 0x34738730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of class-map。

[条件 C-1b7b4ab2000998e9](../../evidence/conditions-sets-011.md#c-1b7b4ab2000998e9) · [参数 P-0b0642b12039a44e](../../evidence/parameters-sets-001.md#p-0b0642b12039a44e) · [状态效果 S-32497c579b32f3c3](../../evidence/state_effects-sets-011.md#s-32497c579b32f3c3)

### path-034251

```text
(config)# class-map type traffic match-any <string> <cr>
```

Handler ` RVA 0x10A611B0 `；selector ` 0 `；EOL ` RVA 0x34C271A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of traffic class-map。

[条件 C-1b7b4ab2000998e9](../../evidence/conditions-sets-011.md#c-1b7b4ab2000998e9) · [参数 P-798833a87dab9b8e](../../evidence/parameters-sets-009.md#p-798833a87dab9b8e) · [状态效果 S-ba068dab8e65b976](../../evidence/state_effects-sets-039.md#s-ba068dab8e65b976)

### path-026664

```text
(config)# classmap-template <string> <string> <cr>
```

Handler ` RVA 0x10564EB0 `；selector ` 0 `；EOL ` RVA 0x34B598C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` base class name；` string ` comma delimited string containingacl entries to be added to filters in parameterized class。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-8ff252b3b27ee04a](../../evidence/parameters-sets-011.md#p-8ff252b3b27ee04a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025812

```text
(config)# clns cache-invalidate-delay <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 35 `；EOL ` RVA 0x34B84EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b892a67102252f56](../../evidence/conditions-sets-071.md#c-b892a67102252f56) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025466

```text
(config)# clns configuration-time <number:1..65535> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 21 `；EOL ` RVA 0x34B924E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Rate at which ESH and ISH packets are sent。

[条件 C-ba918133eece1403](../../evidence/conditions-sets-072.md#c-ba918133eece1403) · [参数 P-0c5384e742a775e2](../../evidence/parameters-sets-001.md#p-0c5384e742a775e2) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027423

```text
(config)# clns filter-expr <string> <cr>
```

Handler ` RVA 0x10583A90 `；selector ` 0 `；EOL ` RVA 0x34B93ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of filter expression。

[条件 C-0a7d429b8b4c1011](../../evidence/conditions-sets-004.md#c-0a7d429b8b4c1011) · [参数 P-22091aedf3a32734](../../evidence/parameters-sets-003.md#p-22091aedf3a32734) · [状态效果 S-49948404a6992fc9](../../evidence/state_effects-sets-016.md#s-49948404a6992fc9)

### path-027391

```text
(config)# clns filter-set <string> <cr>
```

Handler ` RVA 0x10582270 `；selector ` 0 `；EOL ` RVA 0x34B93A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of filter set。

[条件 C-2877d7e40a4961dc](../../evidence/conditions-sets-016.md#c-2877d7e40a4961dc) · [参数 P-6fbf2ba30783234e](../../evidence/parameters-sets-009.md#p-6fbf2ba30783234e) · [状态效果 S-0ce9aac606a891a0](../../evidence/state_effects-sets-003.md#s-0ce9aac606a891a0)

### path-025468

```text
(config)# clns holding-time <number:1..65535> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 23 `；EOL ` RVA 0x34B92548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Holdtime advertised in ESH/ISH PDUs。

[条件 C-5914c828ec637836](../../evidence/conditions-sets-035.md#c-5914c828ec637836) · [参数 P-f44c85f4e076325a](../../evidence/parameters-sets-018.md#p-f44c85f4e076325a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-029494

```text
(config)# clns host <string> <address> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 22 `；EOL ` RVA 0x34B842F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name to give to a NSAP；` address ` NSAP address to assign name to。

[条件 C-bbcc92e015da8967](../../evidence/conditions-sets-073.md#c-bbcc92e015da8967) · [参数 P-1c258efbeae8da1b](../../evidence/parameters-sets-003.md#p-1c258efbeae8da1b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027252

```text
(config)# clns net <address> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 1 `；EOL ` RVA 0x34B92B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` CLNS address or host name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-385ff22fa02bd36c](../../evidence/parameters-sets-005.md#p-385ff22fa02bd36c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025471

```text
(config)# clns packet-lifetime <number:1..255> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 24 `；EOL ` RVA 0x34B92DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Initial lifetime for locally generated packets。

[条件 C-932676f34ebbc51d](../../evidence/conditions-sets-057.md#c-932676f34ebbc51d) · [参数 P-649642de6f5b55f7](../../evidence/parameters-sets-008.md#p-649642de6f5b55f7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025474

```text
(config)# clns queue-depth <number:1..2147483647> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 36 `；EOL ` RVA 0x34B92DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` CLNS queue depth。

[条件 C-3324c6131e4115ee](../../evidence/conditions-sets-020.md#c-3324c6131e4115ee) · [参数 P-bc080f1a3dd74f7d](../../evidence/parameters-sets-014.md#p-bc080f1a3dd74f7d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027083

```text
(config)# clns route <address> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 25 `；EOL ` RVA 0x34B84990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-df617c3c7aff4e3c](../../evidence/conditions-sets-086.md#c-df617c3c7aff4e3c) · [参数 P-757361b9ee4e7b69](../../evidence/parameters-sets-009.md#p-757361b9ee4e7b69) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060406

```text
(config)# clns route default <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 25 `；EOL ` RVA 0x34B84990 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9e06bf9d5d9e39c0](../../evidence/conditions-sets-061.md#c-9e06bf9d5d9e39c0) · [缺口 G-6c35b04a6f54291b](../../evidence/gaps-sets-004.md#g-6c35b04a6f54291b) · [状态效果 S-f6ba30e21c380299](../../evidence/state_effects-sets-052.md#s-f6ba30e21c380299)

### path-025905

```text
(config)# clns routing <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 27 `；EOL ` RVA 0x34B94AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eccc7cb2f71a5877](../../evidence/conditions-sets-091.md#c-eccc7cb2f71a5877) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060303

```text
(config)# clns security pass-through <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 32 `；EOL ` RVA 0x34B933A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1b11477c8d2d8476](../../evidence/conditions-sets-011.md#c-1b11477c8d2d8476) · [缺口 G-053e0bfd69029ff5](../../evidence/gaps-sets-001.md#g-053e0bfd69029ff5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030475

```text
(config)# clns template-alias <string> <string> <cr>
```

Handler ` RVA 0x10581EE0 `；selector ` 0 `；EOL ` RVA 0x34B94788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Template name；` string ` Address template。

[条件 C-715b23fa2d0bca7f](../../evidence/conditions-sets-044.md#c-715b23fa2d0bca7f) · [参数 P-c375a00a89f9da61](../../evidence/parameters-sets-015.md#p-c375a00a89f9da61) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025909

```text
(config)# clns want-erpdu <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 28 `；EOL ` RVA 0x34B93650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025610

```text
(config)# clock calendar-valid <cr>
```

Handler ` RVA 0xE039CE0 `；selector ` 0 `；EOL ` RVA 0x34172EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ed34bcb46f1c734a](../../evidence/conditions-sets-092.md#c-ed34bcb46f1c734a) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026304

```text
(config)# clock initialize nvram <cr>
```

Handler ` RVA 0xD70B0E0 `；selector ` 0 `；EOL ` RVA 0x341735A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7b4effcd8baa15d](../../evidence/conditions-sets-077.md#c-c7b4effcd8baa15d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028159

```text
(config)# clock save interval <number:8..24> <cr>
```

Handler ` RVA 0xE039E60 `；selector ` 0 `；EOL ` RVA 0x341732C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` clock backup update in hours。

[条件 C-e77a2869f6d940e5](../../evidence/conditions-sets-089.md#c-e77a2869f6d940e5) · [参数 P-e78ed62551215976](../../evidence/parameters-sets-017.md#p-e78ed62551215976) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-063020

```text
(config)# clock summer-time <string> date <?month_action@5555896c6900> <number:1993..2035> <hh:mm> <?month_action@5555896c6aa8> <number:1993..2035> <hh:mm> <cr>
```

Handler ` RVA 0xE038CB0 `；selector ` 0 `；EOL ` RVA 0x34172460 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` name of time zone in summer；` unsigned_number ` Year to start；` time_hm ` Time to start (hh:mm)；` unsigned_number ` Year to end；` time_hm ` Time to end (hh:mm)。

[条件 C-b27bd15b21590917](../../evidence/conditions-sets-069.md#c-b27bd15b21590917) · [缺口 G-46761371a6f90f59](../../evidence/gaps-sets-003.md#g-46761371a6f90f59) · [参数 P-36665ab91642756d](../../evidence/parameters-sets-005.md#p-36665ab91642756d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028174

```text
(config)# clock summer-time <string> recurring <cr>
```

Handler ` RVA 0xE038CB0 `；selector ` 0 `；EOL ` RVA 0x34172460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name of time zone in summer。

[条件 C-6cf8a4bafee9282e](../../evidence/conditions-sets-042.md#c-6cf8a4bafee9282e) · [参数 P-a858d7d4e4a9d1ef](../../evidence/parameters-sets-013.md#p-a858d7d4e4a9d1ef) · [状态效果 S-90fd9a528f380ef5](../../evidence/state_effects-sets-031.md#s-90fd9a528f380ef5)

### path-060355

```text
(config)# cns aaa <cr>
```

Handler ` RVA 0xF352130 `；selector ` 2 `；EOL ` RVA 0x34615710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8b8d57242d9654a3](../../evidence/conditions-sets-054.md#c-8b8d57242d9654a3) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060489

```text
(config)# cns config initial <cr>
```

Handler ` RVA 0xF317DC0 `；selector ` 1 `；EOL ` RVA 0x346060F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-21760c2cade49aa5](../../evidence/conditions-sets-013.md#c-21760c2cade49aa5) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060490

```text
(config)# cns config notify <cr>
```

Handler ` RVA 0xF32C950 `；selector ` 3 `；EOL ` RVA 0x34610310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa76ba8fde7a8b0e](../../evidence/conditions-sets-066.md#c-aa76ba8fde7a8b0e) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060492

```text
(config)# cns config partial <cr>
```

Handler ` RVA 0xF31B340 `；selector ` 2 `；EOL ` RVA 0x34606C08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-525a7f06d9b70724](../../evidence/conditions-sets-032.md#c-525a7f06d9b70724) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060363

```text
(config)# cns connect <cr>
```

Handler ` RVA 0xF322950 `；selector ` 0 `；EOL ` RVA 0x34608378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d2354d2d1cece6c2](../../evidence/conditions-sets-081.md#c-d2354d2d1cece6c2) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060361

```text
(config)# cns dhcp <cr>
```

Handler ` RVA 0xF30B8B0 `；selector ` 0 `；EOL ` RVA 0x34607D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-df0fb378346aad82](../../evidence/conditions-sets-086.md#c-df0fb378346aad82) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060359

```text
(config)# cns event <cr>
```

Handler ` RVA 0xF35F1A0 `；selector ` 0 `；EOL ` RVA 0x34616580 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4e5c4097f1b53ef0](../../evidence/conditions-sets-031.md#c-4e5c4097f1b53ef0) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060693

```text
(config)# cns event <string> backup <cr>
```

Handler ` RVA 0xF35F1A0 `；selector ` 1 `；EOL ` RVA 0x34615FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Host name or ip address of event gateway。

[条件 C-5a576c7b422395f2](../../evidence/conditions-sets-035.md#c-5a576c7b422395f2) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-3461d5687c2d49f9](../../evidence/parameters-sets-004.md#p-3461d5687c2d49f9) · [状态效果 S-42be229a296b19e0](../../evidence/state_effects-sets-015.md#s-42be229a296b19e0)

### path-060365

```text
(config)# cns exec <cr>
```

Handler ` RVA 0xF3671C0 `；selector ` 1 `；EOL ` RVA 0x34619050 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b30d6fc18c3dc210](../../evidence/conditions-sets-069.md#c-b30d6fc18c3dc210) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-370ec31144551a06](../../evidence/state_effects-sets-012.md#s-370ec31144551a06)

### path-060484

```text
(config)# cns id hostname <cr>
```

Handler ` RVA 0xF34BEA0 `；selector ` 0 `；EOL ` RVA 0x34614710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f2af4731ebe2fa6f](../../evidence/conditions-sets-094.md#c-f2af4731ebe2fa6f) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-024e7263b0bdfcfe](../../evidence/state_effects-sets-001.md#s-024e7263b0bdfcfe)

### path-060364

```text
(config)# cns image <cr>
```

Handler ` RVA 0xF36CB80 `；selector ` 1 `；EOL ` RVA 0x3461ACF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060494

```text
(config)# cns image password <cr>
```

Handler ` RVA 0xF36CB80 `；selector ` 2 `；EOL ` RVA 0x3461AA48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e897d548a04d6c39](../../evidence/conditions-sets-090.md#c-e897d548a04d6c39) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060491

```text
(config)# cns image retry <cr>
```

Handler ` RVA 0xF36CB80 `；selector ` 3 `；EOL ` RVA 0x3461A730 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-371e89f807f22c55](../../evidence/conditions-sets-021.md#c-371e89f807f22c55) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060694

```text
(config)# cns mib-access encapsulation snmp <cr>
```

Handler ` RVA 0xF3806A0 `；selector ` 0 `；EOL ` RVA 0x3461DF40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-d44c741db5054e0a](../../evidence/state_effects-sets-045.md#s-d44c741db5054e0a)

### path-060347

```text
(config)# cns password <cr>
```

Handler ` RVA 0xF3385F0 `；selector ` 1 `；EOL ` RVA 0x34612A20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4e6ab555092c6ab1](../../evidence/conditions-sets-031.md#c-4e6ab555092c6ab1) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060495

```text
(config)# cns template connect <cr>
```

Handler ` RVA 0xF324ED0 `；selector ` 0 `；EOL ` RVA 0x34608838 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e004e7f9bd70879d](../../evidence/conditions-sets-086.md#c-e004e7f9bd70879d) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [状态效果 S-9969179893d99381](../../evidence/state_effects-sets-033.md#s-9969179893d99381)

### path-060683

```text
(config)# cns trusted-server event <string> <cr>
```

Handler ` RVA 0xF341660 `；selector ` 1 `；EOL ` RVA 0x346138D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Host name or address of trusted-server。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [缺口 G-919c15a2726448fb](../../evidence/gaps-sets-005.md#g-919c15a2726448fb) · [参数 P-3d8ce25e9d81eee5](../../evidence/parameters-sets-005.md#p-3d8ce25e9d81eee5) · [状态效果 S-9fa1c014897c8a25](../../evidence/state_effects-sets-034.md#s-9fa1c014897c8a25)

### path-025601

```text
(config)# config-register <number:0..65535> <cr>
```

Handler ` RVA 0xE950C70 `；selector ` 0 `；EOL ` RVA 0x34352370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Config register number。

[条件 C-6bf448aea841b0d7](../../evidence/conditions-sets-042.md#c-6bf448aea841b0d7) · [参数 P-b7ac583127223f94](../../evidence/parameters-sets-014.md#p-b7ac583127223f94) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027287

```text
(config)# configuration mode exclusive <cr>
```

Handler ` RVA 0xDFE8B80 `；selector ` 0 `；EOL ` RVA 0x340BD418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a0cc17f653eabd3b](../../evidence/conditions-sets-062.md#c-a0cc17f653eabd3b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025751

```text
(config)# connect <string> <cr>
```

Handler ` RVA 0xF43ABC0 `；selector ` 0 `；EOL ` RVA 0x34648398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name for this connection。

[条件 C-4c173fb7764ae0d3](../../evidence/conditions-sets-030.md#c-4c173fb7764ae0d3) · [参数 P-162edcd88fb53fb2](../../evidence/parameters-sets-002.md#p-162edcd88fb53fb2) · [状态效果 S-207f2eed0030f6ce](../../evidence/state_effects-sets-007.md#s-207f2eed0030f6ce)

### path-062824

```text
(config)# connect <string> <interface> <number:16..1007> <interface> <number:16..1007> <cr>
```

Handler ` RVA 0xF43ABC0 `；selector ` 0 `；EOL ` RVA 0x34648398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Name for this connection；` unsigned_number ` Frame Relay DLCI；` unsigned_number ` Frame Relay DLCI。

[条件 C-8f1f4506de50c10f](../../evidence/conditions-sets-055.md#c-8f1f4506de50c10f) · [缺口 G-63338fd95b2eca72](../../evidence/gaps-sets-004.md#g-63338fd95b2eca72) · [参数 P-3f51f5b91606821d](../../evidence/parameters-sets-005.md#p-3f51f5b91606821d) · [状态效果 S-3c1b9df9846bfec5](../../evidence/state_effects-sets-013.md#s-3c1b9df9846bfec5)

### path-025464

```text
(config)# control-plane <cr>
```

Handler ` RVA 0xE47F430 `；selector ` 0 `；EOL ` RVA 0x342C5210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8259f9a4af6fc6d4](../../evidence/conditions-sets-051.md#c-8259f9a4af6fc6d4) · [状态效果 S-78cc14f3a5db04c3](../../evidence/state_effects-sets-026.md#s-78cc14f3a5db04c3)

### path-060283

```text
(config)# controller <?controller_action@55558994b0d8> <cr>
```

Handler ` RVA 0xECFE920 `；selector ` 0 `；EOL ` RVA 0x343F7100 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f53c0439f791afe2](../../evidence/conditions-sets-095.md#c-f53c0439f791afe2) · [缺口 G-721f461dc9e93926](../../evidence/gaps-sets-004.md#g-721f461dc9e93926) · [状态效果 S-340f74ab51782926](../../evidence/state_effects-sets-012.md#s-340f74ab51782926)

### path-028681

```text
(config)# cops ip dscp ef <cr>
```

Handler ` RVA 0xF446FF0 `；selector ` 0 `；EOL ` RVA 0x3464BDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc5e34f955776611](../../evidence/conditions-sets-097.md#c-fc5e34f955776611) · [状态效果 S-04c3265ca8f41ab6](../../evidence/state_effects-sets-001.md#s-04c3265ca8f41ab6)

### path-026656

```text
(config)# cops listener access-list <cr>
```

Handler ` RVA 0xF446CF0 `；selector ` 0 `；EOL ` RVA 0x3464B5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ea3639a89de26ca](../../evidence/conditions-sets-018.md#c-2ea3639a89de26ca) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028644

```text
(config)# cops tcp window-size <number:516..65535> <cr>
```

Handler ` RVA 0xF4470B0 `；selector ` 0 `；EOL ` RVA 0x3464BA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Size in bytes。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-7dba7e155c120e9f](../../evidence/parameters-sets-010.md#p-7dba7e155c120e9f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-025992

```text
(config)# coverage history <number:1..100000> <cr>
```

Handler ` RVA 0xDE877E0 `；selector ` 0 `；EOL ` RVA 0x341478C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Size of history ring。

[条件 C-68d9bcb117563d08](../../evidence/conditions-sets-041.md#c-68d9bcb117563d08) · [参数 P-18e178a2909b7bd8](../../evidence/parameters-sets-002.md#p-18e178a2909b7bd8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-034177

```text
(config)# crypto RSA-key-pair <string> <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35838CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Key pair name；` unsigned_number ` Usage；` unsigned_number ` Generation Timestamp。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-12a1347439a1f629](../../evidence/parameters-sets-002.md#p-12a1347439a1f629) · [状态效果 S-b3b58cfd6d9631a9](../../evidence/state_effects-sets-038.md#s-b3b58cfd6d9631a9)

### path-028098

```text
(config)# crypto dh lifetime <number:0..86400> <cr>
```

Handler ` RVA 0x120F3D30 `；selector ` 0 `；EOL ` RVA 0x3579ECD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Reusage lifetime (in seconds)。

[条件 C-c25d64b92378957f](../../evidence/conditions-sets-075.md#c-c25d64b92378957f) · [参数 P-b4091bd5898dd950](../../evidence/parameters-sets-014.md#p-b4091bd5898dd950) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028131

```text
(config)# crypto dh pregen <number:0..20> <cr>
```

Handler ` RVA 0x120F3C30 `；selector ` 0 `；EOL ` RVA 0x3579EFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of pregenerated DH values。

[条件 C-931d4fa6df0a7264](../../evidence/conditions-sets-057.md#c-931d4fa6df0a7264) · [参数 P-4a9462d364c151ea](../../evidence/parameters-sets-006.md#p-4a9462d364c151ea) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026518

```text
(config)# crypto engine accelerator <cr>
```

Handler ` RVA 0x120CB850 `；selector ` 0 `；EOL ` RVA 0x3578DFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-32a577c754b5f541](../../evidence/conditions-sets-020.md#c-32a577c754b5f541) · [状态效果 S-10c73b7cc4a69029](../../evidence/state_effects-sets-004.md#s-10c73b7cc4a69029)

### path-060536

```text
(config)# crypto engine accelerator <number:dynamic> <cr>
```

Handler ` RVA 0x120CB850 `；selector ` 0 `；EOL ` RVA 0x3578DFA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Card slot number。

[条件 C-992cb001774bb717](../../evidence/conditions-sets-059.md#c-992cb001774bb717) · [缺口 G-94ea303b1be8c03a](../../evidence/gaps-sets-005.md#g-94ea303b1be8c03a) · [参数 P-a957a523194b1fc6](../../evidence/parameters-sets-013.md#p-a957a523194b1fc6) · [状态效果 S-10c73b7cc4a69029](../../evidence/state_effects-sets-004.md#s-10c73b7cc4a69029)

### path-034206

```text
(config)# crypto engine compliance shield disable <cr>
```

Handler ` RVA 0x1210A590 `；selector ` 0 `；EOL ` RVA 0x357A8190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52e7a03fba828590](../../evidence/conditions-sets-032.md#c-52e7a03fba828590) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028203

```text
(config)# crypto engine nm <number:0..3> <cr>
```

Handler ` RVA 0x120CB3B0 `；selector ` 0 `；EOL ` RVA 0x3578D7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` NM slot number &lt;0-3&gt;。

[条件 C-ed3286a9813faa7e](../../evidence/conditions-sets-092.md#c-ed3286a9813faa7e) · [参数 P-83ac0da268e733c3](../../evidence/parameters-sets-010.md#p-83ac0da268e733c3) · [状态效果 S-b233c2e99d700e76](../../evidence/state_effects-sets-038.md#s-b233c2e99d700e76)

### path-060525

```text
(config)# crypto engine onboard <number:dynamic> <cr>
```

Handler ` RVA 0x120CB3B0 `；selector ` 0 `；EOL ` RVA 0x3578D7B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Onboard Crypto Engine。

[条件 C-266f7b9ab5f6d077](../../evidence/conditions-sets-015.md#c-266f7b9ab5f6d077) · [缺口 G-c76f20ae147b8b45](../../evidence/gaps-sets-007.md#g-c76f20ae147b8b45) · [参数 P-309f0cf1593e43dd](../../evidence/parameters-sets-004.md#p-309f0cf1593e43dd) · [状态效果 S-f9efd688f93646fc](../../evidence/state_effects-sets-053.md#s-f9efd688f93646fc)

### path-028129

```text
(config)# crypto engine queue-size <number:50..500> <cr>
```

Handler ` RVA 0x12119480 `；selector ` 0 `；EOL ` RVA 0x357A78A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Crypto engine queue size, default is 500。

[条件 C-4797b3b903be6348](../../evidence/conditions-sets-028.md#c-4797b3b903be6348) · [参数 P-b73244a5036254a8](../../evidence/parameters-sets-014.md#p-b73244a5036254a8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028081

```text
(config)# crypto engine software ipsec <cr>
```

Handler ` RVA 0x121195B0 `；selector ` 0 `；EOL ` RVA 0x357A7B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028121

```text
(config)# crypto engine software isakmp <cr>
```

Handler ` RVA 0x121196E0 `；selector ` 0 `；EOL ` RVA 0x357A7E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028437

```text
(config)# crypto key decrypt rsa <cr>
```

Handler ` RVA 0x123A3E60 `；selector ` 1 `；EOL ` RVA 0x35835120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-30793147c5c04870](../../evidence/state_effects-sets-011.md#s-30793147c5c04870)

### path-028403

```text
(config)# crypto key encrypt rsa <cr>
```

Handler ` RVA 0x123A3E60 `；selector ` 0 `；EOL ` RVA 0x35834C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-d9aaae7067570a52](../../evidence/state_effects-sets-046.md#s-d9aaae7067570a52)

### path-058895

```text
(config)# crypto key export ec <string> pem terminal 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35837268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` ec key label；` string ` Passphrase used to protect the private key。

[条件 C-467425c52844b023](../../evidence/conditions-sets-028.md#c-467425c52844b023) · [参数 P-4d8bba577b7ab7b7](../../evidence/parameters-sets-006.md#p-4d8bba577b7ab7b7) · [状态效果 S-36b57169bbf81eaf](../../evidence/state_effects-sets-012.md#s-36b57169bbf81eaf)

### path-062586

```text
(config)# crypto key export ec <string> pem url <url:dynamic> 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35837268 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` ec key label；` string ` Passphrase used to protect the private key。

[条件 C-957ceec71a1d9174](../../evidence/conditions-sets-058.md#c-957ceec71a1d9174) · [缺口 G-cd36f0f7a1393c52](../../evidence/gaps-sets-007.md#g-cd36f0f7a1393c52) · [参数 P-5f74d4290fba6e37](../../evidence/parameters-sets-008.md#p-5f74d4290fba6e37) · [状态效果 S-36b57169bbf81eaf](../../evidence/state_effects-sets-012.md#s-36b57169bbf81eaf)

### path-058892

```text
(config)# crypto key export rsa <string> pem terminal 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` RSA key label；` string ` Passphrase used to protect the private key。

[条件 C-5d5bd329befeaec5](../../evidence/conditions-sets-036.md#c-5d5bd329befeaec5) · [参数 P-5e7b35cad7819108](../../evidence/parameters-sets-008.md#p-5e7b35cad7819108) · [状态效果 S-3a7495abf54176ba](../../evidence/state_effects-sets-013.md#s-3a7495abf54176ba)

### path-062585

```text
(config)# crypto key export rsa <string> pem url <url:dynamic> 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RSA key label；` string ` Passphrase used to protect the private key。

[条件 C-df7dcae03535fba0](../../evidence/conditions-sets-086.md#c-df7dcae03535fba0) · [缺口 G-df24901e65646f0e](../../evidence/gaps-sets-008.md#g-df24901e65646f0e) · [参数 P-a2a79fdd4a0157bf](../../evidence/parameters-sets-012.md#p-a2a79fdd4a0157bf) · [状态效果 S-3a7495abf54176ba](../../evidence/state_effects-sets-013.md#s-3a7495abf54176ba)

### path-044053

```text
(config)# crypto key generate ec keysize <number:256..256> <cr>
```

Handler ` RVA 0x123A92D0 `；selector ` 3 `；EOL ` RVA 0x358346E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` 256 bit keys。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-343b4cf8bed1ae88](../../evidence/parameters-sets-004.md#p-343b4cf8bed1ae88) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028281

```text
(config)# crypto key generate rsa <cr>
```

Handler ` RVA 0x123AA0C0 `；selector ` 15 `；EOL ` RVA 0x358341D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1be4983520a27cec](../../evidence/conditions-sets-011.md#c-1be4983520a27cec) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-061223

```text
(config)# crypto key generate rsa modulus <number:dynamic> <cr>
```

Handler ` RVA 0x123AA0C0 `；selector ` 15 `；EOL ` RVA 0x358341D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` size of the key modulus。

[条件 C-e06f4836502d63ea](../../evidence/conditions-sets-086.md#c-e06f4836502d63ea) · [缺口 G-7420a30e2e2cde46](../../evidence/gaps-sets-004.md#g-7420a30e2e2cde46) · [参数 P-85814004592f1c05](../../evidence/parameters-sets-010.md#p-85814004592f1c05) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044133

```text
(config)# crypto key import ec <string> terminal <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x358381B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` EC key label。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-e69a93f63ee3b0a6](../../evidence/parameters-sets-017.md#p-e69a93f63ee3b0a6) · [状态效果 S-d557e0c30da27c4d](../../evidence/state_effects-sets-045.md#s-d557e0c30da27c4d)

### path-061845

```text
(config)# crypto key import ec <string> url <url:dynamic> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x358381B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` EC key label。

[条件 C-bc7f147719906994](../../evidence/conditions-sets-073.md#c-bc7f147719906994) · [缺口 G-7e5adcf59fca07b8](../../evidence/gaps-sets-005.md#g-7e5adcf59fca07b8) · [参数 P-e0a7cee6e7e61fcd](../../evidence/parameters-sets-017.md#p-e0a7cee6e7e61fcd) · [状态效果 S-d557e0c30da27c4d](../../evidence/state_effects-sets-045.md#s-d557e0c30da27c4d)

### path-044226

```text
(config)# crypto key import rsa <string> terminal <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35837D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` RSA key label。

[条件 C-330b9cbc88e262c8](../../evidence/conditions-sets-020.md#c-330b9cbc88e262c8) · [参数 P-b0a9c3bfc80636fc](../../evidence/parameters-sets-013.md#p-b0a9c3bfc80636fc) · [状态效果 S-9803b5ecb22f9476](../../evidence/state_effects-sets-032.md#s-9803b5ecb22f9476)

### path-061850

```text
(config)# crypto key import rsa <string> url <url:dynamic> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35837D20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` RSA key label。

[条件 C-a0735d59d52731c0](../../evidence/conditions-sets-062.md#c-a0735d59d52731c0) · [缺口 G-5bb97c374747e74c](../../evidence/gaps-sets-004.md#g-5bb97c374747e74c) · [参数 P-58de2fe08387903d](../../evidence/parameters-sets-007.md#p-58de2fe08387903d) · [状态效果 S-9803b5ecb22f9476](../../evidence/state_effects-sets-032.md#s-9803b5ecb22f9476)

### path-034232

```text
(config)# crypto key move rsa <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` RSA key label。

[条件 C-e1f88ae436324afa](../../evidence/conditions-sets-087.md#c-e1f88ae436324afa) · [参数 P-444babfe34822919](../../evidence/parameters-sets-006.md#p-444babfe34822919) · [状态效果 S-59cf403fa7ddec36](../../evidence/state_effects-sets-019.md#s-59cf403fa7ddec36)

### path-028204

```text
(config)# crypto key pubkey-chain rsa <cr>
```

Handler ` RVA 0x123A6B80 `；selector ` 0 `；EOL ` RVA 0x35838568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1400f325728c920](../../evidence/conditions-sets-081.md#c-d1400f325728c920) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028256

```text
(config)# crypto key storage <string> <cr>
```

Handler ` RVA 0x121535B0 `；selector ` 17 `；EOL ` RVA 0x35838898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` keypair storage location。

[条件 C-2a5ab40bbb537c00](../../evidence/conditions-sets-017.md#c-2a5ab40bbb537c00) · [参数 P-f11a3971eee1b18e](../../evidence/parameters-sets-018.md#p-f11a3971eee1b18e) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026337

```text
(config)# crypto key zeroize <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-131cf39f683a1a39](../../evidence/state_effects-sets-004.md#s-131cf39f683a1a39)

### path-030786

```text
(config)# crypto pki authenticate <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 1 `；EOL ` RVA 0x3574A628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-a493bd4fde1f6f87](../../evidence/parameters-sets-013.md#p-a493bd4fde1f6f87) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037945

```text
(config)# crypto pki certificate chain <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 18 `；EOL ` RVA 0x3574D400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-877c0bda626030dd](../../evidence/parameters-sets-010.md#p-877c0bda626030dd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047218

```text
(config)# crypto pki certificate map <string> <number:1..65535> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 23 `；EOL ` RVA 0x3574D080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Certificate attribute map tag；` unsigned_number ` Sequence to insert into certificate map entry。

[条件 C-fa341a1cfdc3b2ed](../../evidence/conditions-sets-097.md#c-fa341a1cfdc3b2ed) · [参数 P-be84f85b13d6a408](../../evidence/parameters-sets-014.md#p-be84f85b13d6a408) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031018

```text
(config)# crypto pki certificate pool <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 112 `；EOL ` RVA 0x3574D6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030904

```text
(config)# crypto pki certificate query <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 3 `；EOL ` RVA 0x3574CC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047397

```text
(config)# crypto pki certificate self-signed hash sha1 <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 120 `；EOL ` RVA 0x3574E2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-52f8a2fdbaa6f300](../../evidence/conditions-sets-032.md#c-52f8a2fdbaa6f300) · [状态效果 S-4f7dfa1593ee46b2](../../evidence/state_effects-sets-017.md#s-4f7dfa1593ee46b2)

### path-031213

```text
(config)# crypto pki certificate storage <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 50 `；EOL ` RVA 0x3574DD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0c3453cf7031291c](../../evidence/conditions-sets-005.md#c-0c3453cf7031291c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060958

```text
(config)# crypto pki certificate storage <url:dynamic> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 50 `；EOL ` RVA 0x3574DD10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-23124f9e9b470106](../../evidence/conditions-sets-014.md#c-23124f9e9b470106) · [缺口 G-ad1649d516a86aa5](../../evidence/gaps-sets-006.md#g-ad1649d516a86aa5) · [参数 P-8559107441f213d8](../../evidence/parameters-sets-010.md#p-8559107441f213d8) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037981

```text
(config)# crypto pki certificate validate <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 36 `；EOL ` RVA 0x3574D9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` trust point。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b01d97b8ece37da7](../../evidence/parameters-sets-013.md#p-b01d97b8ece37da7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047271

```text
(config)# crypto pki crl cache size <number:0..131072> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 31 `；EOL ` RVA 0x3574FEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum size of the CRL cache in kilobytes。

[条件 C-b3d8156ab0da3e2f](../../evidence/conditions-sets-070.md#c-b3d8156ab0da3e2f) · [参数 P-6639bae9c1c37d82](../../evidence/parameters-sets-008.md#p-6639bae9c1c37d82) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-054346

```text
(config)# crypto pki crl download schedule prepublish <number:0..65535> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 117 `；EOL ` RVA 0x3574EC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time interval to Pre-download CRL before CRL expiry。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-5b262c73fd51666f](../../evidence/parameters-sets-007.md#p-5b262c73fd51666f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-054363

```text
(config)# crypto pki crl download schedule retries <number:1..15> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 119 `；EOL ` RVA 0x3574EF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` number of retries。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-d282ece9b775b32f](../../evidence/parameters-sets-016.md#p-d282ece9b775b32f) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062348

```text
(config)# crypto pki crl download schedule time Sunday <hh:mm> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 118 `；EOL ` RVA 0x3574F340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` time_hm ` Request auto-download CRL at this time。

[条件 C-98e86a28fd5c415e](../../evidence/conditions-sets-059.md#c-98e86a28fd5c415e) · [缺口 G-d9fe08cf7bc435f4](../../evidence/gaps-sets-008.md#g-d9fe08cf7bc435f4) · [参数 P-12281124a6a1145d](../../evidence/parameters-sets-002.md#p-12281124a6a1145d) · [状态效果 S-b548b31be108e607](../../evidence/state_effects-sets-038.md#s-b548b31be108e607)

### path-047266

```text
(config)# crypto pki crl download trustpoint <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 116 `；EOL ` RVA 0x3574FB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of Trustpoint to use for CRL download。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-aa72afc5dc21aaf4](../../evidence/parameters-sets-013.md#p-aa72afc5dc21aaf4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047318

```text
(config)# crypto pki crl download url <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 115 `；EOL ` RVA 0x3574F778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` http or ldap url。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-f7d977c82f857994](../../evidence/parameters-sets-018.md#p-f7d977c82f857994) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-062350

```text
(config)# crypto pki crl download url <string> source-interface <interface> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 115 `；EOL ` RVA 0x3574F778 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` http or ldap url。

[条件 C-6fb1c46c9d42bf7d](../../evidence/conditions-sets-043.md#c-6fb1c46c9d42bf7d) · [缺口 G-bdfd4fbe979f09bf](../../evidence/gaps-sets-007.md#g-bdfd4fbe979f09bf) · [参数 P-d8ef9d503841e33b](../../evidence/parameters-sets-016.md#p-d8ef9d503841e33b) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037871

```text
(config)# crypto pki crl request <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 17 `；EOL ` RVA 0x3574E848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b94220b02a9d2fc4](../../evidence/parameters-sets-014.md#p-b94220b02a9d2fc4) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030844

```text
(config)# crypto pki enroll <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 15 `；EOL ` RVA 0x3574A978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-1f830e14f538908c](../../evidence/parameters-sets-003.md#p-1f830e14f538908c) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047252

```text
(config)# crypto pki export <string> pem terminal <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 9 `；EOL ` RVA 0x3574C450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with。

[条件 C-f14fc9b7c9d7ff3f](../../evidence/conditions-sets-093.md#c-f14fc9b7c9d7ff3f) · [参数 P-9546f4da27c00d6b](../../evidence/parameters-sets-011.md#p-9546f4da27c00d6b) · [状态效果 S-20e595b8cf194b3a](../../evidence/state_effects-sets-007.md#s-20e595b8cf194b3a)

### path-054316

```text
(config)# crypto pki export <string> pem terminal rollover <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 10 `；EOL ` RVA 0x3574C070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-9546f4da27c00d6b](../../evidence/parameters-sets-011.md#p-9546f4da27c00d6b) · [状态效果 S-f695fc22bbd2c7e0](../../evidence/state_effects-sets-052.md#s-f695fc22bbd2c7e0)

### path-062032

```text
(config)# crypto pki export <string> pem url <url:dynamic> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 9 `；EOL ` RVA 0x3574C450 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with。

[条件 C-38e0221ca67fd535](../../evidence/conditions-sets-022.md#c-38e0221ca67fd535) · [缺口 G-90806186d10f3e34](../../evidence/gaps-sets-005.md#g-90806186d10f3e34) · [参数 P-b38ee388d79363cc](../../evidence/parameters-sets-014.md#p-b38ee388d79363cc) · [状态效果 S-20e595b8cf194b3a](../../evidence/state_effects-sets-007.md#s-20e595b8cf194b3a)

### path-062342

```text
(config)# crypto pki export <string> pkcs12 <url:dynamic> password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 6 `；EOL ` RVA 0x3574BC68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with；` string ` Passphrase used to protect the pkcs12 file。

[条件 C-60142ea682598512](../../evidence/conditions-sets-037.md#c-60142ea682598512) · [缺口 G-d0c01b53fc874eab](../../evidence/gaps-sets-007.md#g-d0c01b53fc874eab) · [参数 P-5786a653c32fec11](../../evidence/parameters-sets-007.md#p-5786a653c32fec11) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057935

```text
(config)# crypto pki export <string> pkcs12 terminal password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 6 `；EOL ` RVA 0x3574BC68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with；` string ` Passphrase used to protect the pkcs12 file。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-7ef11695fcfc8786](../../evidence/parameters-sets-010.md#p-7ef11695fcfc8786) · [状态效果 S-e799199b13dd720b](../../evidence/state_effects-sets-049.md#s-e799199b13dd720b)

### path-037993

```text
(config)# crypto pki http max-buffer-size <number:1..100> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 122 `；EOL ` RVA 0x35750280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Specify the size in MB。

[条件 C-314087f38263da32](../../evidence/conditions-sets-019.md#c-314087f38263da32) · [参数 P-cea1ae393ca64e91](../../evidence/parameters-sets-016.md#p-cea1ae393ca64e91) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037795

```text
(config)# crypto pki import <string> certificate <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 16 `；EOL ` RVA 0x3574B7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b66c5879120dbef0](../../evidence/parameters-sets-014.md#p-b66c5879120dbef0) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057962

```text
(config)# crypto pki import <string> pem terminal password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 7 `；EOL ` RVA 0x3574B4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with；` string ` Passphrase used to protect the private key。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-018311bd803f2671](../../evidence/parameters-sets-001.md#p-018311bd803f2671) · [状态效果 S-d605b7d83e8f0030](../../evidence/state_effects-sets-045.md#s-d605b7d83e8f0030)

### path-062529

```text
(config)# crypto pki import <string> pem url <url:dynamic> password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 7 `；EOL ` RVA 0x3574B4B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with；` string ` Passphrase used to protect the private key。

[条件 C-a4590b8464270854](../../evidence/conditions-sets-063.md#c-a4590b8464270854) · [缺口 G-be41b65ed32ae3d3](../../evidence/gaps-sets-007.md#g-be41b65ed32ae3d3) · [参数 P-1a901362f502e8b3](../../evidence/parameters-sets-002.md#p-1a901362f502e8b3) · [状态效果 S-d605b7d83e8f0030](../../evidence/state_effects-sets-045.md#s-d605b7d83e8f0030)

