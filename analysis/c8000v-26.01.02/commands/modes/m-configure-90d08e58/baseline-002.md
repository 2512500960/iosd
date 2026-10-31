# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-062343

```text
(config)# crypto pki import <string> pkcs12 <url:dynamic> password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 4 `；EOL ` RVA 0x3574AF50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with；` string ` Passphrase used to protect the pkcs12 file。

[条件 C-d64ad03dc2dcc569](../../evidence/conditions-sets-083.md#c-d64ad03dc2dcc569) · [缺口 G-f4c21d7a187b9c1b](../../evidence/gaps-sets-008.md#g-f4c21d7a187b9c1b) · [参数 P-74bf048d923822ba](../../evidence/parameters-sets-009.md#p-74bf048d923822ba) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-057936

```text
(config)# crypto pki import <string> pkcs12 terminal password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 4 `；EOL ` RVA 0x3574AF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with；` string ` Passphrase used to protect the pkcs12 file。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-532840c65e552ec1](../../evidence/parameters-sets-007.md#p-532840c65e552ec1) · [状态效果 S-2da5110825ac04d9](../../evidence/state_effects-sets-010.md#s-2da5110825ac04d9)

### path-037838

```text
(config)# crypto pki profile enrollment <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 27 `；EOL ` RVA 0x3574C980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Certificate enrollment profile tag。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-a2210f57c2ffc457](../../evidence/parameters-sets-012.md#p-a2210f57c2ffc457) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030845

```text
(config)# crypto pki server <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 33 `；EOL ` RVA 0x33871378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-27be11738d9231ce](../../evidence/conditions-sets-016.md#c-27be11738d9231ce) · [参数 P-1bed6ccbf092ba27](../../evidence/parameters-sets-003.md#p-1bed6ccbf092ba27) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037766

```text
(config)# crypto pki server <string> rollover <cr>
```

Handler ` RVA 0xBBB8230 `；selector ` 34 `；EOL ` RVA 0x338713E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-081f59a8dd484058](../../evidence/conditions-sets-004.md#c-081f59a8dd484058) · [参数 P-1bed6ccbf092ba27](../../evidence/parameters-sets-003.md#p-1bed6ccbf092ba27) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047070

```text
(config)# crypto pki server <string> rollover cancel <cr>
```

Handler ` RVA 0xBBB8230 `；selector ` 35 `；EOL ` RVA 0x338713B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-081f59a8dd484058](../../evidence/conditions-sets-004.md#c-081f59a8dd484058) · [参数 P-1bed6ccbf092ba27](../../evidence/parameters-sets-003.md#p-1bed6ccbf092ba27) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030774

```text
(config)# crypto pki trustpoint <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 19 `；EOL ` RVA 0x35749928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-bd0edbaeffc60831](../../evidence/parameters-sets-014.md#p-bd0edbaeffc60831) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030807

```text
(config)# crypto pki trustpool clean <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 113 `；EOL ` RVA 0x35749FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-bb4437f758732b33](../../evidence/state_effects-sets-040.md#s-bb4437f758732b33)

### path-061453

```text
(config)# crypto pki trustpool import url <url:dynamic> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 113 `；EOL ` RVA 0x35749FA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dd1c0c0e8ecea24c](../../evidence/conditions-sets-085.md#c-dd1c0c0e8ecea24c) · [缺口 G-213d0c84b2d8e3aa](../../evidence/gaps-sets-002.md#g-213d0c84b2d8e3aa) · [参数 P-6817b87230aa2e55](../../evidence/parameters-sets-008.md#p-6817b87230aa2e55) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-030771

```text
(config)# crypto pki trustpool policy <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 111 `；EOL ` RVA 0x35749C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026285

```text
(config)# crypto provisioning petitioner <cr>
```

Handler ` RVA 0x12E02540 `；selector ` 0 `；EOL ` RVA 0x359E3C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026305

```text
(config)# crypto provisioning registrar <cr>
```

Handler ` RVA 0x12E02540 `；selector ` 1 `；EOL ` RVA 0x359E3F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-027472

```text
(config)# cts cache enable <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 0 `；EOL ` RVA 0x35A161B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8386fff5b05d91a4](../../evidence/conditions-sets-051.md#c-8386fff5b05d91a4) · [状态效果 S-75a0dd8c47291dcc](../../evidence/state_effects-sets-025.md#s-75a0dd8c47291dcc)

### path-062948

```text
(config)# cts cache nv-storage <url:dynamic> <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 0 `；EOL ` RVA 0x35A161B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5929e13dce5112ac](../../evidence/conditions-sets-035.md#c-5929e13dce5112ac) · [缺口 G-c051f0313a3e8d8b](../../evidence/gaps-sets-007.md#g-c051f0313a3e8d8b) · [参数 P-632aeafac340ef46](../../evidence/parameters-sets-008.md#p-632aeafac340ef46) · [状态效果 S-d170cee1dc699ce0](../../evidence/state_effects-sets-044.md#s-d170cee1dc699ce0)

### path-031084

```text
(config)# cts policy-server device-id <string> <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 3 `；EOL ` RVA 0x359F7A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Device ID of this Switch or Router。

[条件 C-795300afebd2c150](../../evidence/conditions-sets-047.md#c-795300afebd2c150) · [参数 P-57b86735dfe507c5](../../evidence/parameters-sets-007.md#p-57b86735dfe507c5) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031000

```text
(config)# cts policy-server name <string> <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 0 `；EOL ` RVA 0x359F6E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name for the policy server configuration。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-b4da26b659e349ff](../../evidence/parameters-sets-014.md#p-b4da26b659e349ff) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-031076

```text
(config)# cts policy-server order random <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 2 `；EOL ` RVA 0x359F7730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1aaba8d22b067d86](../../evidence/conditions-sets-010.md#c-1aaba8d22b067d86) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-047429

```text
(config)# cts policy-server username <string> password <string> <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 1 `；EOL ` RVA 0x359F7198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter the Username；` string ` The UNENCRYPTED(cleartext) password。

[条件 C-64f86f3a79cddb41](../../evidence/conditions-sets-039.md#c-64f86f3a79cddb41) · [参数 P-3f80b34601d23ee7](../../evidence/parameters-sets-005.md#p-3f80b34601d23ee7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026874

```text
(config)# cts role-based enforcement <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 0 `；EOL ` RVA 0x35CFA6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3c2a529e2ab1a1fd](../../evidence/conditions-sets-023.md#c-3c2a529e2ab1a1fd) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-035405

```text
(config)# cts role-based enforcement logging-interval <number:5..86400> <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 14 `；EOL ` RVA 0x35CFA6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter logging interval in seconds。

[条件 C-e8be9f72014ed63c](../../evidence/conditions-sets-090.md#c-e8be9f72014ed63c) · [参数 P-ab0334442b8cbc0d](../../evidence/parameters-sets-013.md#p-ab0334442b8cbc0d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060603

```text
(config)# cts role-based enforcement vlan-list <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 5 `；EOL ` RVA 0x35CF9E50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-66ba6dbb2605782e](../../evidence/conditions-sets-040.md#c-66ba6dbb2605782e) · [缺口 G-75e03c7eb271e314](../../evidence/gaps-sets-005.md#g-75e03c7eb271e314) · [状态效果 S-491b3ac0ddf3e82b](../../evidence/state_effects-sets-016.md#s-491b3ac0ddf3e82b)

### path-026764

```text
(config)# cts role-based ipv6-copy <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 6 `；EOL ` RVA 0x35CE8948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-32732e14c3f77d59](../../evidence/conditions-sets-020.md#c-32732e14c3f77d59) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060826

```text
(config)# cts role-based l2-vrf <string> vlan-list <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 4 `；EOL ` RVA 0x35CE80F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VPN Routing/Forwarding instance name。

[条件 C-d98d4ec5a715035c](../../evidence/conditions-sets-084.md#c-d98d4ec5a715035c) · [缺口 G-1b7be6df63f5c22f](../../evidence/gaps-sets-001.md#g-1b7be6df63f5c22f) · [参数 P-19b6644671a8427f](../../evidence/parameters-sets-002.md#p-19b6644671a8427f) · [状态效果 S-56103d34022a3aa7](../../evidence/state_effects-sets-019.md#s-56103d34022a3aa7)

### path-029053

```text
(config)# cts role-based monitor all <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 12 `；EOL ` RVA 0x35CFB810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14caee070928983d](../../evidence/conditions-sets-008.md#c-14caee070928983d) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060830

```text
(config)# cts role-based monitor permissions default <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 11 `；EOL ` RVA 0x35CFBC78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-14caee070928983d](../../evidence/conditions-sets-008.md#c-14caee070928983d) · [缺口 G-4c514d2425f003ca](../../evidence/gaps-sets-003.md#g-4c514d2425f003ca) · [状态效果 S-db1424aee83773fd](../../evidence/state_effects-sets-046.md#s-db1424aee83773fd)

### path-060593

```text
(config)# cts role-based permissions default <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 1 `；EOL ` RVA 0x35CFB1F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-298b5138446c3a62](../../evidence/conditions-sets-016.md#c-298b5138446c3a62) · [缺口 G-1eb53e557bc5cc0a](../../evidence/gaps-sets-002.md#g-1eb53e557bc5cc0a) · [状态效果 S-54820d153dce7ac5](../../evidence/state_effects-sets-018.md#s-54820d153dce7ac5)

### path-029218

```text
(config)# cts role-based policy priority-static <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 13 `；EOL ` RVA 0x35CFAC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e9f606d272b51a89](../../evidence/conditions-sets-090.md#c-e9f606d272b51a89) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-026876

```text
(config)# cts role-based sgt-caching <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 8 `；EOL ` RVA 0x35CF8668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d1452a1125e391c7](../../evidence/conditions-sets-081.md#c-d1452a1125e391c7) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-060604

```text
(config)# cts role-based sgt-caching vlan-list <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 9 `；EOL ` RVA 0x35CF8788 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-48eabc1814a3a6f9](../../evidence/conditions-sets-029.md#c-48eabc1814a3a6f9) · [缺口 G-8b8463ee5bf6bd74](../../evidence/gaps-sets-005.md#g-8b8463ee5bf6bd74) · [状态效果 S-a981a83febfbd751](../../evidence/state_effects-sets-036.md#s-a981a83febfbd751)

### path-029150

```text
(config)# cts role-based sgt-caching with-enforcement <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 7 `；EOL ` RVA 0x35CF8358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbaf825484834ab9](../../evidence/conditions-sets-078.md#c-cbaf825484834ab9) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-044933

```text
(config)# cts role-based sgt-map <address> sgt <number:2..65521> <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 2 `；EOL ` RVA 0x35CE72E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 host address；` unsigned_number ` Security Group Tag value。

[条件 C-b6436682e0d8a35f](../../evidence/conditions-sets-070.md#c-b6436682e0d8a35f) · [参数 P-ddba27fa94fcb3dc](../../evidence/parameters-sets-017.md#p-ddba27fa94fcb3dc) · [状态效果 S-34f4533ba6feaa15](../../evidence/state_effects-sets-012.md#s-34f4533ba6feaa15)

### path-060576

```text
(config)# cts role-based sgt-map <prefix:dynamic> <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 2 `；EOL ` RVA 0x35CE72E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-3fa2db83a61f73c3](../../evidence/conditions-sets-025.md#c-3fa2db83a61f73c3) · [缺口 G-bf78c4b7beb13756](../../evidence/gaps-sets-007.md#g-bf78c4b7beb13756) · [参数 P-98ded2efaea5d3bb](../../evidence/parameters-sets-012.md#p-98ded2efaea5d3bb) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-037771

```text
(config)# cts server load-balance method least-outstanding <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 4 `；EOL ` RVA 0x35A15D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b80198d8eb4f9ce9](../../evidence/conditions-sets-071.md#c-b80198d8eb4f9ce9) · [状态效果 S-533843fdfac91920](../../evidence/state_effects-sets-018.md#s-533843fdfac91920)

### path-027518

```text
(config)# cts sxp enable <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 49 `；EOL ` RVA 0x35A4D6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [状态效果 S-60fe36590ae1a58a](../../evidence/state_effects-sets-021.md#s-60fe36590ae1a58a)

### path-031027

```text
(config)# cts sxp import-list <string> <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 50 `；EOL ` RVA 0x35A4DA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Import-list name。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-edc86fdb67e73efe](../../evidence/parameters-sets-018.md#p-edc86fdb67e73efe) · [状态效果 S-a5e321d5dce4ddb2](../../evidence/state_effects-sets-035.md#s-a5e321d5dce4ddb2)

### path-047360

```text
(config)# cts sxp limit export peer-sequence-nodes <number:2..64> <cr>
```

Handler ` RVA 0x1322A0D0 `；selector ` 0 `；EOL ` RVA 0x35A4E358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Enter number of nodes。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-d8786f70be9cbf6b](../../evidence/parameters-sets-016.md#p-d8786f70be9cbf6b) · [状态效果 S-6d118461a39e3b1f](../../evidence/state_effects-sets-023.md#s-6d118461a39e3b1f)

### path-060708

```text
(config)# cts sxp node-id <interface> <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 49 `；EOL ` RVA 0x35A4D6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b231c6ecc2eb710](../../evidence/conditions-sets-048.md#c-7b231c6ecc2eb710) · [缺口 G-d9aaaf7e6e1054e5](../../evidence/gaps-sets-008.md#g-d9aaaf7e6e1054e5) · [参数 P-cb23e96d1c84d5cf](../../evidence/parameters-sets-015.md#p-cb23e96d1c84d5cf) · [状态效果 S-ef7a82588adc5414](../../evidence/state_effects-sets-051.md#s-ef7a82588adc5414)

### path-025912

```text
(config)# cwmp agent <cr>
```

Handler ` RVA 0x164722D0 `；selector ` 0 `；EOL ` RVA 0x35F8A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-0109722c766f661b](../../evidence/state_effects-sets-001.md#s-0109722c766f661b)

### path-028273

```text
(config)# default aaa accounting delay-start <cr>
```

Handler ` RVA 0xDD42010 `；selector ` 1 `；EOL ` RVA 0x3419FD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-40035e3c2d1b1012](../../evidence/conditions-sets-025.md#c-40035e3c2d1b1012) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-034487

```text
(config)# default aaa accounting dot1x guarantee-first <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 52 `；EOL ` RVA 0x341A4410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3d5f3ed96229dafe](../../evidence/conditions-sets-024.md#c-3d5f3ed96229dafe) · [状态效果 S-95e772a6c9da1b78](../../evidence/state_effects-sets-032.md#s-95e772a6c9da1b78)

### path-034486

```text
(config)# default aaa accounting dot1x local <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 78 `；EOL ` RVA 0x341A40E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0c5cf52e587909f](../../evidence/conditions-sets-093.md#c-f0c5cf52e587909f) · [状态效果 S-95e772a6c9da1b78](../../evidence/state_effects-sets-032.md#s-95e772a6c9da1b78)

### path-034442

```text
(config)# default aaa accounting dot1x visible-keys <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 77 `；EOL ` RVA 0x341A3E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0c5cf52e587909f](../../evidence/conditions-sets-093.md#c-f0c5cf52e587909f) · [状态效果 S-95e772a6c9da1b78](../../evidence/state_effects-sets-032.md#s-95e772a6c9da1b78)

### path-028389

```text
(config)# default aaa accounting gigawords <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 45 `；EOL ` RVA 0x341A0D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-044147

```text
(config)# default aaa accounting include auth-profile framed-ip-address <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 58 `；EOL ` RVA 0x341A2128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-751ab6ab05b18373](../../evidence/conditions-sets-045.md#c-751ab6ab05b18373) · [状态效果 S-1038c74ce16163e1](../../evidence/state_effects-sets-004.md#s-1038c74ce16163e1)

### path-028210

```text
(config)# default aaa accounting jitter <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 50 `；EOL ` RVA 0x341A1778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6d89329abe5447c5](../../evidence/conditions-sets-042.md#c-6d89329abe5447c5) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-028438

```text
(config)# default aaa accounting nested <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 51 `；EOL ` RVA 0x341A0A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-034556

```text
(config)# default aaa accounting redundancy new-session <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 47 `；EOL ` RVA 0x341A1388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-1e3c59714d011e17](../../evidence/state_effects-sets-007.md#s-1e3c59714d011e17)

### path-044262

```text
(config)# default aaa accounting redundancy suppress system-records <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 49 `；EOL ` RVA 0x341A10C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-044059

```text
(config)# default aaa accounting send counters ipv6 <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 46 `；EOL ` RVA 0x3419F8F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8a6f61dd0cc6d253](../../evidence/conditions-sets-054.md#c-8a6f61dd0cc6d253) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-044099

```text
(config)# default aaa accounting send stop-record always <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 74 `；EOL ` RVA 0x3419F620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3af7dabdbb2a4835](../../evidence/conditions-sets-023.md#c-3af7dabdbb2a4835) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-052141

```text
(config)# default aaa accounting send stop-record authentication failure <cr>
```

Handler ` RVA 0xDD42010 `；selector ` 2 `；EOL ` RVA 0x3419EF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ccf09763ed1de79](../../evidence/conditions-sets-042.md#c-6ccf09763ed1de79) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-056797

```text
(config)# default aaa accounting send stop-record authentication success remote-server <cr>
```

Handler ` RVA 0xDD42010 `；selector ` 3 `；EOL ` RVA 0x3419F318 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cee9cfa414babd5e](../../evidence/conditions-sets-080.md#c-cee9cfa414babd5e) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-034367

```text
(config)# default aaa accounting session-duration ntp-adjusted <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 65 `；EOL ` RVA 0x341A0708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-044170

```text
(config)# default aaa accounting suppress attributes vpdn-endpoints <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 44 `；EOL ` RVA 0x341A03F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-034333

```text
(config)# default aaa accounting suppress null-username <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 43 `；EOL ` RVA 0x341A0110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14ae2d16b776e1eb](../../evidence/conditions-sets-008.md#c-14ae2d16b776e1eb) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-028274

```text
(config)# default aaa accounting update <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 53 `；EOL ` RVA 0x341A1B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9ff00be16e30ce2a](../../evidence/conditions-sets-062.md#c-9ff00be16e30ce2a) · [状态效果 S-6e6024cdfb6a6a60](../../evidence/state_effects-sets-023.md#s-6e6024cdfb6a6a60)

### path-052046

```text
(config)# default aaa archives enable-data index <number:1..5> <string> <cr>
```

Handler ` RVA 0xDD198E0 `；selector ` 83 `；EOL ` RVA 0x3419CD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Index number；` string ` Archive Data content。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-3a6444ba6d1ad9fb](../../evidence/parameters-sets-005.md#p-3a6444ba6d1ad9fb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-056769

```text
(config)# default aaa archives user-data <string> index <number:1..5> <string> <cr>
```

Handler ` RVA 0xDD198E0 `；selector ` 82 `；EOL ` RVA 0x3419C988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` AAA user name(max length 63, longer name will be truncated)；` unsigned_number ` Index number；` string ` Archive Data content。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-cc9087697fe17aac](../../evidence/parameters-sets-015.md#p-cc9087697fe17aac) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034142

```text
(config)# default aaa attribute list <string> <cr>
```

Handler ` RVA 0xCD2E990 `；selector ` 16 `；EOL ` RVA 0x341B1A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` name。

[条件 C-9b655c64430bb7a9](../../evidence/conditions-sets-060.md#c-9b655c64430bb7a9) · [参数 P-27a95c96116b782c](../../evidence/parameters-sets-003.md#p-27a95c96116b782c) · [状态效果 S-5f9e399ff6cba7a0](../../evidence/state_effects-sets-021.md#s-5f9e399ff6cba7a0)

### path-044095

```text
(config)# default aaa authentication attempts login <number:1..25> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 29 `；EOL ` RVA 0x341A7AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Specify value for the number of attempts。

[条件 C-b115887852580738](../../evidence/conditions-sets-068.md#c-b115887852580738) · [参数 P-a291fbfe45c63f22](../../evidence/parameters-sets-012.md#p-a291fbfe45c63f22) · [状态效果 S-8f3885d1563463b2](../../evidence/state_effects-sets-030.md#s-8f3885d1563463b2)

### path-028310

```text
(config)# default aaa authentication banner <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 27 `；EOL ` RVA 0x341A7E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a38ecc091d54cd8f](../../evidence/conditions-sets-063.md#c-a38ecc091d54cd8f) · [状态效果 S-8f3885d1563463b2](../../evidence/state_effects-sets-030.md#s-8f3885d1563463b2)

### path-028340

```text
(config)# default aaa authentication fail-message <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 26 `；EOL ` RVA 0x341A8180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-89ec95532f278ba1](../../evidence/conditions-sets-053.md#c-89ec95532f278ba1) · [状态效果 S-8f3885d1563463b2](../../evidence/state_effects-sets-030.md#s-8f3885d1563463b2)

### path-034287

```text
(config)# default aaa authentication login default <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 24 `；EOL ` RVA 0x341A88F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4aecaf3da87d487e](../../evidence/conditions-sets-029.md#c-4aecaf3da87d487e) · [状态效果 S-d61d1d388726dede](../../evidence/state_effects-sets-045.md#s-d61d1d388726dede)

### path-028369

```text
(config)# default aaa authentication password-prompt <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 25 `；EOL ` RVA 0x341A84D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b598b2a150f1dd6](../../evidence/conditions-sets-042.md#c-6b598b2a150f1dd6) · [状态效果 S-ec0749c467244162](../../evidence/state_effects-sets-050.md#s-ec0749c467244162)

### path-028507

```text
(config)# default aaa authentication rejected <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 79 `；EOL ` RVA 0x341AA580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1f11ec5b895a9aa7](../../evidence/conditions-sets-012.md#c-1f11ec5b895a9aa7) · [状态效果 S-8f3885d1563463b2](../../evidence/state_effects-sets-030.md#s-8f3885d1563463b2)

### path-034216

```text
(config)# default aaa authentication suppress null-username <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 30 `；EOL ` RVA 0x341A7768 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b115887852580738](../../evidence/conditions-sets-068.md#c-b115887852580738) · [状态效果 S-8f3885d1563463b2](../../evidence/state_effects-sets-030.md#s-8f3885d1563463b2)

### path-044427

```text
(config)# default aaa authentication token key <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 75 `；EOL ` RVA 0x341AA0A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` The UNENCRYPTED token key 。

[条件 C-fd3e59c01e895a0b](../../evidence/conditions-sets-098.md#c-fd3e59c01e895a0b) · [参数 P-92659d782811ef9c](../../evidence/parameters-sets-011.md#p-92659d782811ef9c) · [状态效果 S-8f3885d1563463b2](../../evidence/state_effects-sets-030.md#s-8f3885d1563463b2)

### path-028299

```text
(config)# default aaa authorization address-authorization-exec <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 39 `；EOL ` RVA 0x341A5550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-135f57f4623ed85e](../../evidence/state_effects-sets-005.md#s-135f57f4623ed85e)

### path-028257

```text
(config)# default aaa authorization config-commands <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 38 `；EOL ` RVA 0x341A52A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-135f57f4623ed85e](../../evidence/state_effects-sets-005.md#s-135f57f4623ed85e)

### path-028205

```text
(config)# default aaa authorization console <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 40 `；EOL ` RVA 0x341A4D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-135f57f4623ed85e](../../evidence/state_effects-sets-005.md#s-135f57f4623ed85e)

### path-034350

```text
(config)# default aaa authorization network default <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 31 `；EOL ` RVA 0x341A5F48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e3b8d1ac5bec0512](../../evidence/conditions-sets-088.md#c-e3b8d1ac5bec0512) · [状态效果 S-f6de424316eaff3f](../../evidence/state_effects-sets-052.md#s-f6de424316eaff3f)

### path-034345

```text
(config)# default aaa authorization network visible-keys <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 76 `；EOL ` RVA 0x341A5C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-46033a7fc7a8407b](../../evidence/conditions-sets-027.md#c-46033a7fc7a8407b) · [状态效果 S-75a4acbfec4ce52a](../../evidence/state_effects-sets-025.md#s-75a4acbfec4ce52a)

### path-034267

```text
(config)# default aaa authorization suppress null-username <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 81 `；EOL ` RVA 0x341A5018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-135f57f4623ed85e](../../evidence/state_effects-sets-005.md#s-135f57f4623ed85e)

### path-028329

```text
(config)# default aaa authorization template <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 41 `；EOL ` RVA 0x341A57F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fb3c63e25196c01b](../../evidence/conditions-sets-097.md#c-fb3c63e25196c01b) · [状态效果 S-135f57f4623ed85e](../../evidence/state_effects-sets-005.md#s-135f57f4623ed85e)

### path-028033

```text
(config)# default aaa cache filterserver <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 15 `；EOL ` RVA 0x341B1030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a13ce26d85708235](../../evidence/conditions-sets-062.md#c-a13ce26d85708235) · [状态效果 S-5f9e399ff6cba7a0](../../evidence/state_effects-sets-021.md#s-5f9e399ff6cba7a0)

### path-034126

```text
(config)# default aaa cache profile <string> <cr>
```

Handler ` RVA 0xCD83BC0 `；selector ` 0 `；EOL ` RVA 0x341B1350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Cache profile name。

[条件 C-a13ce26d85708235](../../evidence/conditions-sets-062.md#c-a13ce26d85708235) · [参数 P-c045549dd3aef44c](../../evidence/parameters-sets-015.md#p-c045549dd3aef44c) · [状态效果 S-5f9e399ff6cba7a0](../../evidence/state_effects-sets-021.md#s-5f9e399ff6cba7a0)

### path-034141

```text
(config)# default aaa common-criteria policy <string> <cr>
```

Handler ` RVA 0xDD6C420 `；selector ` 0 `；EOL ` RVA 0x341B1708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy name (max of 128 characters)。

[条件 C-37fc62d47b80b8b9](../../evidence/conditions-sets-022.md#c-37fc62d47b80b8b9) · [参数 P-ab3ad3ab6970872b](../../evidence/parameters-sets-013.md#p-ab3ad3ab6970872b) · [状态效果 S-5f9e399ff6cba7a0](../../evidence/state_effects-sets-021.md#s-5f9e399ff6cba7a0)

### path-052319

```text
(config)# default aaa dnis map <string> accounting network <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 5 `；EOL ` RVA 0x3419E398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS number。

[条件 C-a1df414dad303253](../../evidence/conditions-sets-063.md#c-a1df414dad303253) · [参数 P-bfb9721d7e9db5ea](../../evidence/parameters-sets-015.md#p-bfb9721d7e9db5ea) · [状态效果 S-8c8d5420b67a2c63](../../evidence/state_effects-sets-030.md#s-8c8d5420b67a2c63)

### path-052299

```text
(config)# default aaa dnis map <string> authentication ppp <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 4 `；EOL ` RVA 0x3419DE70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS number。

[条件 C-7ae6557539a3a333](../../evidence/conditions-sets-048.md#c-7ae6557539a3a333) · [参数 P-bfb9721d7e9db5ea](../../evidence/parameters-sets-015.md#p-bfb9721d7e9db5ea) · [状态效果 S-1d62fab619f0bc89](../../evidence/state_effects-sets-007.md#s-1d62fab619f0bc89)

### path-052278

```text
(config)# default aaa dnis map <string> authorization network <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 3 `；EOL ` RVA 0x3419D928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` DNIS number。

[条件 C-46c588a3428db701](../../evidence/conditions-sets-028.md#c-46c588a3428db701) · [参数 P-bfb9721d7e9db5ea](../../evidence/parameters-sets-015.md#p-bfb9721d7e9db5ea) · [状态效果 S-80875abca7bbe0c8](../../evidence/state_effects-sets-027.md#s-80875abca7bbe0c8)

### path-034263

```text
(config)# default aaa dnis map enable <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 1 `；EOL ` RVA 0x3419D468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2bc7aed0e14d5b12](../../evidence/conditions-sets-017.md#c-2bc7aed0e14d5b12) · [状态效果 S-50b1fced8dae7d71](../../evidence/state_effects-sets-018.md#s-50b1fced8dae7d71)

### path-044063

```text
(config)# default aaa group server tacacs+ <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 11 `；EOL ` RVA 0x341AAC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Server-group name with max string length 32。

[条件 C-724bb4672860d337](../../evidence/conditions-sets-044.md#c-724bb4672860d337) · [参数 P-bb25f0f3662e2333](../../evidence/parameters-sets-014.md#p-bb25f0f3662e2333) · [状态效果 S-495544a23b1cf674](../../evidence/state_effects-sets-016.md#s-495544a23b1cf674)

### path-044012

```text
(config)# default aaa local authentication attempts max-fail <cr>
```

Handler ` RVA 0xD505370 `；selector ` 1 `；EOL ` RVA 0x33E6FC88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-148303b91acaf5ff](../../evidence/conditions-sets-008.md#c-148303b91acaf5ff) · [状态效果 S-bb1463b67f2d910d](../../evidence/state_effects-sets-039.md#s-bb1463b67f2d910d)

### path-052088

```text
(config)# default aaa local authentication default authorization default <cr>
```

Handler ` RVA 0xD505370 `；selector ` 5 `；EOL ` RVA 0x33E70010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b2f0a854e6e7ca2](../../evidence/conditions-sets-029.md#c-4b2f0a854e6e7ca2) · [状态效果 S-e48b2bfc74382f55](../../evidence/state_effects-sets-048.md#s-e48b2bfc74382f55)

### path-026179

```text
(config)# default aaa new-model <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 0 `；EOL ` RVA 0x3419D068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9ca3d23611b3ebd3](../../evidence/conditions-sets-060.md#c-9ca3d23611b3ebd3) · [状态效果 S-5315a4c5ae8df662](../../evidence/state_effects-sets-018.md#s-5315a4c5ae8df662)

### path-056774

```text
(config)# default aaa tools memleak mode manual count <number:2..64> <cr>
```

Handler ` RVA 0x1371D3C0 `；selector ` 0 `；EOL ` RVA 0x35C0E270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum Sample Count。

[条件 C-bee57da99df13989](../../evidence/conditions-sets-074.md#c-bee57da99df13989) · [参数 P-c896a77975cd77b0](../../evidence/parameters-sets-015.md#p-c896a77975cd77b0) · [状态效果 S-dc352b5145e2ac71](../../evidence/state_effects-sets-047.md#s-dc352b5145e2ac71)

### path-034170

```text
(config)# default aaa user profile <string> <cr>
```

Handler ` RVA 0xDD09450 `；selector ` 62 `；EOL ` RVA 0x341AB2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` AAA user name(max length 63, longer name will be truncated)。

[条件 C-c1044df77e05c547](../../evidence/conditions-sets-075.md#c-c1044df77e05c547) · [参数 P-5fcac73fb916b7fb](../../evidence/parameters-sets-008.md#p-5fcac73fb916b7fb) · [状态效果 S-68d305616850333c](../../evidence/state_effects-sets-022.md#s-68d305616850333c)

### path-026750

```text
(config)# default access-list acl-ace-limit <cr>
```

Handler ` RVA 0xCEE2FE0 `；selector ` 0 `；EOL ` RVA 0x33D54550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6888318978f68193](../../evidence/conditions-sets-040.md#c-6888318978f68193) · [状态效果 S-b339b3ea6392c129](../../evidence/state_effects-sets-038.md#s-b339b3ea6392c129)

### path-026728

```text
(config)# default access-list acl-limit <cr>
```

Handler ` RVA 0xCEE2E30 `；selector ` 0 `；EOL ` RVA 0x33D541B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8d8372447a6876a6](../../evidence/conditions-sets-055.md#c-8d8372447a6876a6) · [状态效果 S-f6d9cf43d4bd9054](../../evidence/state_effects-sets-052.md#s-f6d9cf43d4bd9054)

### path-026668

```text
(config)# default access-list dynamic-extended <cr>
```

Handler ` RVA 0xCEFA1C0 `；selector ` 1 `；EOL ` RVA 0x33D53DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f27fcd8c8da52abe](../../evidence/conditions-sets-094.md#c-f27fcd8c8da52abe) · [状态效果 S-3baf913bf7d1df07](../../evidence/state_effects-sets-013.md#s-3baf913bf7d1df07)

### path-026774

```text
(config)# default access-list global-ace-limit <cr>
```

Handler ` RVA 0xCEE31A0 `；selector ` 0 `；EOL ` RVA 0x33D548C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ff7e823bc1b62626](../../evidence/conditions-sets-098.md#c-ff7e823bc1b62626) · [状态效果 S-4454a9f4471b8213](../../evidence/state_effects-sets-015.md#s-4454a9f4471b8213)

### path-034980

```text
(config)# default access-list rate-limit <number:100..199> <address> <cr>
```

Handler ` RVA 0x10C68030 `；selector ` 0 `；EOL ` RVA 0x34CECFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` MAC address ACL index；` address ` MAC address。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-4a897af35f274644](../../evidence/parameters-sets-006.md#p-4a897af35f274644) · [状态效果 S-3baf913bf7d1df07](../../evidence/state_effects-sets-013.md#s-3baf913bf7d1df07)

### path-026751

```text
(config)# default access-list template <cr>
```

Handler ` RVA 0xEBB9980 `；selector ` 0 `；EOL ` RVA 0x343D1858 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-656eb8ce347bda10](../../evidence/conditions-sets-039.md#c-656eb8ce347bda10) · [状态效果 S-3baf913bf7d1df07](../../evidence/state_effects-sets-013.md#s-3baf913bf7d1df07)

### path-057405

```text
(config)# default access-session accounting attributes filter-spec include list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 14 `；EOL ` RVA 0x33BA3958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` list name。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [参数 P-cb160a75f6835c4b](../../evidence/parameters-sets-015.md#p-cb160a75f6835c4b) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-030004

```text
(config)# default access-session accounting interim-disable <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 25 `；EOL ` RVA 0x33BA3568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [状态效果 S-a344647fa52bc336](../../evidence/state_effects-sets-035.md#s-a344647fa52bc336)

### path-030390

```text
(config)# default access-session acl ack-timer <cr>
```

Handler ` RVA 0xCB45380 `；selector ` 0 `；EOL ` RVA 0x33BDA750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-976e5f04d0520d28](../../evidence/conditions-sets-058.md#c-976e5f04d0520d28) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-036808

```text
(config)# default access-session acl default passthrough <cr>
```

Handler ` RVA 0xCB451F0 `；selector ` 2 `；EOL ` RVA 0x33BDA420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-22163e1f1326ce85](../../evidence/conditions-sets-013.md#c-22163e1f1326ce85) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-045715

```text
(config)# default access-session attributes filter-list list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 12 `；EOL ` RVA 0x33BA2E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` list name。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [参数 P-5ba1cde7f6c0e13e](../../evidence/parameters-sets-007.md#p-5ba1cde7f6c0e13e) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-057361

```text
(config)# default access-session authentication attributes filter-spec include list <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 13 `；EOL ` RVA 0x33BA3250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` list name。

[条件 C-7ce19412fd0a362c](../../evidence/conditions-sets-048.md#c-7ce19412fd0a362c) · [参数 P-d43c8b724db9727a](../../evidence/parameters-sets-016.md#p-d43c8b724db9727a) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-027990

```text
(config)# default access-session bridge-mode vm-policy <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 24 `；EOL ` RVA 0x33BA44F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-606e05f5ec5acf28](../../evidence/conditions-sets-037.md#c-606e05f5ec5acf28) · [状态效果 S-98644ec72e3721cf](../../evidence/state_effects-sets-032.md#s-98644ec72e3721cf)

### path-030230

```text
(config)# default access-session cache limit <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 7 `；EOL ` RVA 0x33BA1E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bab304ae0a5a61db](../../evidence/conditions-sets-072.md#c-bab304ae0a5a61db) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-027138

```text
(config)# default access-session cui-enable <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 23 `；EOL ` RVA 0x33BA40C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7060d85cd77cba2f](../../evidence/conditions-sets-043.md#c-7060d85cd77cba2f) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-027115

```text
(config)# default access-session event-logging <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 16 `；EOL ` RVA 0x33BA0348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b5c1fe2403186a36](../../evidence/conditions-sets-070.md#c-b5c1fe2403186a36) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-030369

```text
(config)# default access-session interface-template sticky <cr>
```

Handler ` RVA 0xCB48060 `；selector ` 0 `；EOL ` RVA 0x33BDD190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-22163e1f1326ce85](../../evidence/conditions-sets-013.md#c-22163e1f1326ce85) · [状态效果 S-c0935f7ef1c15608](../../evidence/state_effects-sets-041.md#s-c0935f7ef1c15608)

### path-045948

```text
(config)# default access-session limit profile name <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 20 `；EOL ` RVA 0x33BA1740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` session limit profile name maximum 32 characters。

[条件 C-d9db9146b1433406](../../evidence/conditions-sets-084.md#c-d9db9146b1433406) · [参数 P-8dcb75c2b8917640](../../evidence/parameters-sets-011.md#p-8dcb75c2b8917640) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-029969

```text
(config)# default access-session mac-move deny <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 2 `；EOL ` RVA 0x33BA0878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8a4b6f81f236ad7c](../../evidence/conditions-sets-053.md#c-8a4b6f81f236ad7c) · [状态效果 S-f7b55950d97cb0ae](../../evidence/state_effects-sets-052.md#s-f7b55950d97cb0ae)

### path-027220

```text
(config)# default access-session monitor <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 1 `；EOL ` RVA 0x33BA3CA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1953bbbd1a40eb74](../../evidence/conditions-sets-010.md#c-1953bbbd1a40eb74) · [状态效果 S-32228eb0c04654a8](../../evidence/state_effects-sets-011.md#s-32228eb0c04654a8)

### path-030293

```text
(config)# default access-session passthru-access-group <string> <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 8 `；EOL ` RVA 0x33BA2228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name of IP access-list。

[条件 C-8baabbe2f46a60d2](../../evidence/conditions-sets-054.md#c-8baabbe2f46a60d2) · [参数 P-3c6c935722325c5c](../../evidence/parameters-sets-005.md#p-3c6c935722325c5c) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-027212

```text
(config)# default access-session pqc-type <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 26 `；EOL ` RVA 0x33BA1230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f4856d6e695d01e](../../evidence/conditions-sets-006.md#c-0f4856d6e695d01e) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-027195

```text
(config)# default access-session tls-version <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 19 `；EOL ` RVA 0x33BA0DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-132eebbe07b342bd](../../evidence/conditions-sets-008.md#c-132eebbe07b342bd) · [状态效果 S-d4cb9e08df8f55f4](../../evidence/state_effects-sets-045.md#s-d4cb9e08df8f55f4)

### path-030237

```text
(config)# default access-session voice skip-data-vlan <cr>
```

Handler ` RVA 0xCAE90D0 `；selector ` 18 `；EOL ` RVA 0x33BA1AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dee2a74085599871](../../evidence/conditions-sets-086.md#c-dee2a74085599871) · [状态效果 S-192dd3cd3ebfe07e](../../evidence/state_effects-sets-006.md#s-192dd3cd3ebfe07e)

### path-027877

```text
(config)# default accounting group <string> <cr>
```

Handler ` RVA 0x10D13C90 `；selector ` 0 `；EOL ` RVA 0x34D11E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Accounting group name。

[条件 C-f52731d492c8b621](../../evidence/conditions-sets-095.md#c-f52731d492c8b621) · [参数 P-08edfb9023a78320](../../evidence/parameters-sets-001.md#p-08edfb9023a78320) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028290

```text
(config)# default alps circuit <string> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 5 `；EOL ` RVA 0x35421EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ASCU ckt name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-d7eaa09ed9c5dfea](../../evidence/parameters-sets-016.md#p-d7eaa09ed9c5dfea) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028266

```text
(config)# default alps enable-alarms peer <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 3 `；EOL ` RVA 0x35421100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-2d2abeb59ee02eab](../../evidence/state_effects-sets-010.md#s-2d2abeb59ee02eab)

### path-026400

```text
(config)# default alps keepalive <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 1 `；EOL ` RVA 0x354209A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-1ea9ec9cba0239f7](../../evidence/state_effects-sets-007.md#s-1ea9ec9cba0239f7)

### path-028185

```text
(config)# default alps local-peer <address> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 0 `；EOL ` RVA 0x354205A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address for local peer。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-53a99e23d8383f0b](../../evidence/parameters-sets-007.md#p-53a99e23d8383f0b) · [状态效果 S-4a7eec0823aaf08e](../../evidence/state_effects-sets-016.md#s-4a7eec0823aaf08e)

### path-026438

```text
(config)# default alps matip-host-emulation <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 6 `；EOL ` RVA 0x35422138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028485

```text
(config)# default alps remote-peer <address> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 4 `；EOL ` RVA 0x35421B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address for remote peer。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-c6c0a71085917c44](../../evidence/parameters-sets-015.md#p-c6c0a71085917c44) · [状态效果 S-fe41072d87125e4b](../../evidence/state_effects-sets-054.md#s-fe41072d87125e4b)

### path-052112

```text
(config)# default alps service-msg-list <number:1..8> number <number:1..8> <string> <cr>
```

Handler ` RVA 0x11213AF0 `；selector ` 2 `；EOL ` RVA 0x35420D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Service message list number；` unsigned_number ` Service message number；` string ` Service message description。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-265dbe293b4e50d3](../../evidence/parameters-sets-003.md#p-265dbe293b4e50d3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028401

```text
(config)# default ancp adjacency timer <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 1 `；EOL ` RVA 0x336DFFB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4cbb7d0757885161](../../evidence/conditions-sets-030.md#c-4cbb7d0757885161) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034419

```text
(config)# default ancp atm shaper percent-factor <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 3 `；EOL ` RVA 0x336DF8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d92f048becdd4002](../../evidence/conditions-sets-084.md#c-d92f048becdd4002) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034420

```text
(config)# default ancp atm shaper percent-factor <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 2 `；EOL ` RVA 0x336DFB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ab128362f960eb3](../../evidence/conditions-sets-017.md#c-2ab128362f960eb3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028397

```text
(config)# default ancp enable test-configuration <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 6 `；EOL ` RVA 0x336E02F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7e7015fb4aa4f49b](../../evidence/conditions-sets-049.md#c-7e7015fb4aa4f49b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-052280

```text
(config)# default ancp neighbor name <string> id <string> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 4 `；EOL ` RVA 0x336E09C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ANCP neighbor name；` string ` ANCP neighbor ID。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-adf739dccc7a9655](../../evidence/parameters-sets-013.md#p-adf739dccc7a9655) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028414

```text
(config)# default ancp source-ip <address> <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 5 `；EOL ` RVA 0x336E0610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` ANCP source IP address。

[条件 C-43b17cd4c6fb8898](../../evidence/conditions-sets-026.md#c-43b17cd4c6fb8898) · [参数 P-df61d1091ab2219d](../../evidence/parameters-sets-017.md#p-df61d1091ab2219d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026393

```text
(config)# default ancp truncate <cr>
```

Handler ` RVA 0xB25E4C0 `；selector ` 7 `；EOL ` RVA 0x336DF488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-be127ddf58be3899](../../evidence/conditions-sets-073.md#c-be127ddf58be3899) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025965

```text
(config)# default archive <cr>
```

Handler ` RVA 0xDEC8E00 `；selector ` 0 `；EOL ` RVA 0x34099E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026804

```text
(config)# default arp <address> <cr>
```

Handler ` RVA 0xCF5BAE0 `；selector ` 0 `；EOL ` RVA 0x33D292C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IP address of ARP entry。

[条件 C-9b4b303308caf43a](../../evidence/conditions-sets-060.md#c-9b4b303308caf43a) · [参数 P-06bf30c5dedbb528](../../evidence/parameters-sets-001.md#p-06bf30c5dedbb528) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028943

```text
(config)# default arp entries interface-limit <cr>
```

Handler ` RVA 0xCF5C9D0 `；selector ` 0 `；EOL ` RVA 0x33D28E70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-284df564c7e848ac](../../evidence/conditions-sets-016.md#c-284df564c7e848ac) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025857

```text
(config)# default async-bootp <cr>
```

Handler ` RVA 0xD344030 `；selector ` 0 `；EOL ` RVA 0x33E1AC30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5ce6138864bf0826](../../evidence/conditions-sets-036.md#c-5ce6138864bf0826) · [状态效果 S-a23e09a1a7374731](../../evidence/state_effects-sets-034.md#s-a23e09a1a7374731)

### path-036289

```text
(config)# default authentication command bounce-port ignore <cr>
```

Handler ` RVA 0xCB0E770 `；selector ` 2 `；EOL ` RVA 0x33BB1730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dc51fcb87e18e11e](../../evidence/conditions-sets-085.md#c-dc51fcb87e18e11e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036355

```text
(config)# default authentication command disable-port ignore <cr>
```

Handler ` RVA 0xCB0E770 `；selector ` 3 `；EOL ` RVA 0x33BB1A60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dc51fcb87e18e11e](../../evidence/conditions-sets-085.md#c-dc51fcb87e18e11e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029855

```text
(config)# default authentication convert-to new-style <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 6 `；EOL ` RVA 0x33B93368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0be4311d10d7daa](../../evidence/conditions-sets-093.md#c-f0be4311d10d7daa) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036007

```text
(config)# default authentication convert-to new-style forced <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 7 `；EOL ` RVA 0x33B93340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f0be4311d10d7daa](../../evidence/conditions-sets-093.md#c-f0be4311d10d7daa) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036322

```text
(config)# default authentication critical recovery delay <cr>
```

Handler ` RVA 0xCAB9CD0 `；selector ` 0 `；EOL ` RVA 0x33B81610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-249763c17ea40f02](../../evidence/conditions-sets-014.md#c-249763c17ea40f02) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027109

```text
(config)# default authentication dis-scale-opt <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 5 `；EOL ` RVA 0x33B92328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41f7ee7f503f70ed](../../evidence/conditions-sets-026.md#c-41f7ee7f503f70ed) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030028

```text
(config)# default authentication logging session-terminate <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 10 `；EOL ` RVA 0x33B92990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-23f1f828624dcb07](../../evidence/conditions-sets-014.md#c-23f1f828624dcb07) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029992

```text
(config)# default authentication logging verbose <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 4 `；EOL ` RVA 0x33B926B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b197d0673015c702](../../evidence/conditions-sets-069.md#c-b197d0673015c702) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029826

```text
(config)# default authentication mac-move permit <cr>
```

Handler ` RVA 0xCAD0250 `；selector ` 1 `；EOL ` RVA 0x33B92030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-41f7ee7f503f70ed](../../evidence/conditions-sets-026.md#c-41f7ee7f503f70ed) · [状态效果 S-b6ac20494d9969ab](../../evidence/state_effects-sets-039.md#s-b6ac20494d9969ab)

### path-026152

```text
(config)# default autoconf enable <cr>
```

Handler ` RVA 0xCAEF6F0 `；selector ` 10 `；EOL ` RVA 0x33BAA4B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025787

```text
(config)# default avc <cr>
```

Handler ` RVA 0x10F24CF0 `；selector ` 45 `；EOL ` RVA 0x35240F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4b80575e83a50d9d](../../evidence/conditions-sets-030.md#c-4b80575e83a50d9d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026968

```text
(config)# default avc sd-service <cr>
```

Handler ` RVA 0x10F26570 `；selector ` 25 `；EOL ` RVA 0x35240CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ee3c9205f596a7f6](../../evidence/conditions-sets-092.md#c-ee3c9205f596a7f6) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027263

```text
(config)# default banner exec <cr>
```

Handler ` RVA 0xDFEC4A0 `；selector ` 0 `；EOL ` RVA 0x340BA1C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ef452e2ce693d97](../../evidence/conditions-sets-018.md#c-2ef452e2ce693d97) · [状态效果 S-b14e0aceecb6f2cb](../../evidence/state_effects-sets-038.md#s-b14e0aceecb6f2cb)

### path-027976

```text
(config)# default bba-group pppoe global <cr>
```

Handler ` RVA 0x112543E0 `；selector ` 0 `；EOL ` RVA 0x35434960 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-e2a1d4339ae58686](../../evidence/state_effects-sets-048.md#s-e2a1d4339ae58686)

### path-028073

```text
(config)# default beep channel limit <cr>
```

Handler ` RVA 0xEF604D0 `；selector ` 3 `；EOL ` RVA 0x3448AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-041ad1f8be4b8641](../../evidence/conditions-sets-002.md#c-041ad1f8be4b8641) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026139

```text
(config)# default bfd fast-timers-on-slow-interface <cr>
```

Handler ` RVA 0x10B1F7C0 `；selector ` 0 `；EOL ` RVA 0x34CAEBB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026145

```text
(config)# default bfd l2cos <cr>
```

Handler ` RVA 0x10B1D4A0 `；selector ` 0 `；EOL ` RVA 0x34CAE590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-750a4dcaa3e5702d](../../evidence/conditions-sets-045.md#c-750a4dcaa3e5702d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027951

```text
(config)# default bfd l3cos ipv6 <cr>
```

Handler ` RVA 0x10B1D370 `；selector ` 0 `；EOL ` RVA 0x34CAE920 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-263a5c78bfbe33ae](../../evidence/conditions-sets-015.md#c-263a5c78bfbe33ae) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-043950

```text
(config)# default bfd neighbor multihop-ipv4 <address> <address> <cr>
```

Handler ` RVA 0x10B4B590 `；selector ` 0 `；EOL ` RVA 0x34CAF4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Destination IP Address；` address ` Source IP Address。

[条件 C-6a1fc372ca36852b](../../evidence/conditions-sets-041.md#c-6a1fc372ca36852b) · [参数 P-e5aa527419715a10](../../evidence/parameters-sets-017.md#p-e5aa527419715a10) · [状态效果 S-1ad02f75a904ab34](../../evidence/state_effects-sets-006.md#s-1ad02f75a904ab34)

### path-026128

```text
(config)# default bfd slow-timers <cr>
```

Handler ` RVA 0x10B1D240 `；selector ` 0 `；EOL ` RVA 0x34CAE240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9acc8bf18350a829](../../evidence/conditions-sets-060.md#c-9acc8bf18350a829) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034031

```text
(config)# default bfd snmp traps more <cr>
```

Handler ` RVA 0x10B1F6D0 `；selector ` 0 `；EOL ` RVA 0x34CAEF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027914

```text
(config)# default bfd-template single-hop <string> <cr>
```

Handler ` RVA 0x10B2F000 `；selector ` 0 `；EOL ` RVA 0x34CB0370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` BFD template name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-70ff01e2ede31908](../../evidence/parameters-sets-009.md#p-70ff01e2ede31908) · [状态效果 S-c3985eacb8093c4d](../../evidence/state_effects-sets-041.md#s-c3985eacb8093c4d)

### path-026072

```text
(config)# default boot bootldr <cr>
```

Handler ` RVA 0xD556020 `；selector ` 0 `；EOL ` RVA 0x33E81818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3bb97630c18d854d](../../evidence/conditions-sets-023.md#c-3bb97630c18d854d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026023

```text
(config)# default boot bootstrap <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x341453C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-60c7429921003534](../../evidence/conditions-sets-038.md#c-60c7429921003534) · [状态效果 S-f3a25664d072b342](../../evidence/state_effects-sets-052.md#s-f3a25664d072b342)

### path-034020

```text
(config)# default boot bootstrap ftp <string> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x33D86D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` System image filename。

[条件 C-922dfa0fbfa41580](../../evidence/conditions-sets-056.md#c-922dfa0fbfa41580) · [参数 P-64b7b29e25e7ff85](../../evidence/parameters-sets-008.md#p-64b7b29e25e7ff85) · [状态效果 S-d871d77dbd7bbd02](../../evidence/state_effects-sets-046.md#s-d871d77dbd7bbd02)

### path-034018

```text
(config)# default boot bootstrap rcp <string> <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 9 `；EOL ` RVA 0x33D7EA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` System image filename。

[条件 C-8033b211b17ecfca](../../evidence/conditions-sets-050.md#c-8033b211b17ecfca) · [参数 P-128ed92b1c40c013](../../evidence/parameters-sets-002.md#p-128ed92b1c40c013) · [状态效果 S-39a958f5e5445ca7](../../evidence/state_effects-sets-013.md#s-39a958f5e5445ca7)

### path-025507

```text
(config)# default boot buffersize <cr>
```

Handler ` RVA 0xDE7F690 `；selector ` 6 `；EOL ` RVA 0x34144CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce97720f76f03f15](../../evidence/conditions-sets-080.md#c-ce97720f76f03f15) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026080

```text
(config)# default boot config <cr>
```

Handler ` RVA 0xE94C290 `；selector ` 0 `；EOL ` RVA 0x343517F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f57cee1619ec1c1e](../../evidence/conditions-sets-095.md#c-f57cee1619ec1c1e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025513

```text
(config)# default boot-end-marker <cr>
```

Handler ` RVA 0xDE7FE20 `；selector ` 0 `；EOL ` RVA 0x341460E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f18f2011c5d14bb](../../evidence/conditions-sets-006.md#c-0f18f2011c5d14bb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025508

```text
(config)# default boot-start-marker <cr>
```

Handler ` RVA 0xDE7FD60 `；selector ` 0 `；EOL ` RVA 0x34144A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f18f2011c5d14bb](../../evidence/conditions-sets-006.md#c-0f18f2011c5d14bb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026288

```text
(config)# default bridge crb <cr>
```

Handler ` RVA 0xF282470 `；selector ` 17 `；EOL ` RVA 0x345E8740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7b718e2fdaf7840](../../evidence/conditions-sets-096.md#c-f7b718e2fdaf7840) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026309

```text
(config)# default bridge irb <cr>
```

Handler ` RVA 0xF282470 `；selector ` 18 `；EOL ` RVA 0x345E89E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f7b718e2fdaf7840](../../evidence/conditions-sets-096.md#c-f7b718e2fdaf7840) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026326

```text
(config)# default bridge mac-address-table limit <cr>
```

Handler ` RVA 0xF285B00 `；selector ` 24 `；EOL ` RVA 0x345E8C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f70593d63fc942a0](../../evidence/conditions-sets-095.md#c-f70593d63fc942a0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028108

```text
(config)# default bridge-domain c-mac aging-time <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 2 `；EOL ` RVA 0x3395A7A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-282e9e07aaf312fd](../../evidence/conditions-sets-016.md#c-282e9e07aaf312fd) · [状态效果 S-9d83812547dabfef](../../evidence/state_effects-sets-033.md#s-9d83812547dabfef)

### path-034208

```text
(config)# default bridge-domain otv default age-time <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 3 `；EOL ` RVA 0x3395AC28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-101a21449ceb8369](../../evidence/conditions-sets-006.md#c-101a21449ceb8369) · [状态效果 S-9d83812547dabfef](../../evidence/state_effects-sets-033.md#s-9d83812547dabfef)

### path-028029

```text
(config)# default bridge-domain parameterized vlan <cr>
```

Handler ` RVA 0xBF84730 `；selector ` 1 `；EOL ` RVA 0x3395A310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-43135ad2f0a46eea](../../evidence/conditions-sets-026.md#c-43135ad2f0a46eea) · [状态效果 S-80ebba0eb8781150](../../evidence/state_effects-sets-027.md#s-80ebba0eb8781150)

### path-028352

```text
(config)# default bstun keepalive-count <number:2..10> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 3 `；EOL ` RVA 0x354BDB90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Number of retries must be between 2 and 10。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [参数 P-d3ed36225ef390ec](../../evidence/parameters-sets-016.md#p-d3ed36225ef390ec) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028226

```text
(config)# default bstun lisnsap <number:0..255> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 4 `；EOL ` RVA 0x354BCEA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` listening SAP。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [参数 P-5e09a37a7c45525f](../../evidence/parameters-sets-008.md#p-5e09a37a7c45525f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026426

```text
(config)# default bstun peer-name <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 0 `；EOL ` RVA 0x354BD1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b82c2dc66f62498](../../evidence/conditions-sets-042.md#c-6b82c2dc66f62498) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034330

```text
(config)# default bstun protocol-group <number:1..255> <string> <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 1 `；EOL ` RVA 0x354BD560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` A BSTUN protocol group number；` string ` Protocol name (max 20 characters)。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [参数 P-13d35ab50d14ac7e](../../evidence/parameters-sets-002.md#p-13d35ab50d14ac7e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026474

```text
(config)# default bstun remote-peer-keepalive <cr>
```

Handler ` RVA 0x113E1540 `；selector ` 2 `；EOL ` RVA 0x354BD890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5193a3f8e96f77f1](../../evidence/conditions-sets-032.md#c-5193a3f8e96f77f1) · [状态效果 S-6b2d63559940f88d](../../evidence/state_effects-sets-023.md#s-6b2d63559940f88d)

### path-028106

```text
(config)# default buffers element permanent <cr>
```

Handler ` RVA 0xE3E08A0 `；selector ` 0 `；EOL ` RVA 0x342BAF18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b2eda43e27382834](../../evidence/conditions-sets-069.md#c-b2eda43e27382834) · [状态效果 S-dcb196d3b84fdfc3](../../evidence/state_effects-sets-047.md#s-dcb196d3b84fdfc3)

### path-028194

```text
(config)# default buffers header permanent <cr>
```

Handler ` RVA 0xE3E06B0 `；selector ` 0 `；EOL ` RVA 0x342BB760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-754dacfe6e986eef](../../evidence/conditions-sets-046.md#c-754dacfe6e986eef) · [状态效果 S-d5fd3057623a8a8a](../../evidence/state_effects-sets-045.md#s-d5fd3057623a8a8a)

### path-026318

```text
(config)# default buffers particle-clone <cr>
```

Handler ` RVA 0xE3E0700 `；selector ` 0 `；EOL ` RVA 0x342BB348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a650ff4bd386b306](../../evidence/conditions-sets-064.md#c-a650ff4bd386b306) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028348

```text
(config)# default buffers tune automatic <cr>
```

Handler ` RVA 0xE3E0AC0 `；selector ` 0 `；EOL ` RVA 0x342BC060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026744

```text
(config)# default busy-message <string> <cr>
```

Handler ` RVA 0xCCF4560 `；selector ` 127 `；EOL ` RVA 0x33C60A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Hostname。

[条件 C-32fb523fb87c4247](../../evidence/conditions-sets-020.md#c-32fb523fb87c4247) · [参数 P-3bd18cae23f559d5](../../evidence/parameters-sets-005.md#p-3bd18cae23f559d5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028936

```text
(config)# default call admission cpu-limit <cr>
```

Handler ` RVA 0xDEB0F40 `；selector ` 0 `；EOL ` RVA 0x3408D738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-33cd2180b78a20fd](../../evidence/conditions-sets-020.md#c-33cd2180b78a20fd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028994

```text
(config)# default call admission cpu-load <cr>
```

Handler ` RVA 0xDEB0FE0 `；selector ` 0 `；EOL ` RVA 0x3408DA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6bc49bb9fd847541](../../evidence/conditions-sets-042.md#c-6bc49bb9fd847541) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044912

```text
(config)# default call admission ike <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 4 `；EOL ` RVA 0x3408EB50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [参数 P-290d5e8e909d7201](../../evidence/parameters-sets-004.md#p-290d5e8e909d7201) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044765

```text
(config)# default call admission ip <number:0..1000> <number:1..31> <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 3 `；EOL ` RVA 0x3408DDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Per-session-charge；` unsigned_number ` Session Lifetime。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [参数 P-0f63ad6b4db446cf](../../evidence/parameters-sets-002.md#p-0f63ad6b4db446cf) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028843

```text
(config)# default call admission limit <cr>
```

Handler ` RVA 0xDEB0D00 `；selector ` 0 `；EOL ` RVA 0x3408D108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9b802c54a5c3d290](../../evidence/conditions-sets-060.md#c-9b802c54a5c3d290) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029287

```text
(config)# default call admission load <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 5 `；EOL ` RVA 0x3408EE68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5f0ac8f13d9a0f46](../../evidence/conditions-sets-037.md#c-5f0ac8f13d9a0f46) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029314

```text
(config)# default call admission new-model <cr>
```

Handler ` RVA 0xDEB11C0 `；selector ` 0 `；EOL ` RVA 0x3408F3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029273

```text
(config)# default call admission padr <cr>
```

Handler ` RVA 0xDEB1160 `；selector ` 0 `；EOL ` RVA 0x3408F138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b09eaec596eb26d0](../../evidence/conditions-sets-068.md#c-b09eaec596eb26d0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029117

```text
(config)# default call admission pppoa <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 2 `；EOL ` RVA 0x3408E470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b32ad2e5623b23c5](../../evidence/conditions-sets-069.md#c-b32ad2e5623b23c5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029080

```text
(config)# default call admission pppoe <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 1 `；EOL ` RVA 0x3408E110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4bc245c8d88c90f0](../../evidence/conditions-sets-030.md#c-4bc245c8d88c90f0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028888

```text
(config)# default call admission session-limit <cr>
```

Handler ` RVA 0xDEB0EA0 `；selector ` 0 `；EOL ` RVA 0x3408D420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9d635f91104585d3](../../evidence/conditions-sets-061.md#c-9d635f91104585d3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029167

```text
(config)# default call admission vpdn <cr>
```

Handler ` RVA 0xDEB1090 `；selector ` 0 `；EOL ` RVA 0x3408E7D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a944279facec644c](../../evidence/conditions-sets-065.md#c-a944279facec644c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029088

```text
(config)# default call filter match-list <cr>
```

Handler ` RVA 0x16988170 `；selector ` 1 `；EOL ` RVA 0x3605B748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0cde5ac269d57fbf](../../evidence/conditions-sets-005.md#c-0cde5ac269d57fbf) · [状态效果 S-56c51545301c5b1c](../../evidence/state_effects-sets-019.md#s-56c51545301c5b1c)

### path-025983

```text
(config)# default call-history-mib max-size <cr>
```

Handler ` RVA 0x1612B140 `；selector ` 0 `；EOL ` RVA 0x35EE00C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-95a5b95e3d90df44](../../evidence/conditions-sets-058.md#c-95a5b95e3d90df44) · [状态效果 S-75a2ca909feae789](../../evidence/state_effects-sets-025.md#s-75a2ca909feae789)

### path-025980

```text
(config)# default call-history-mib retain-timer <cr>
```

Handler ` RVA 0x1612B140 `；selector ` 1 `；EOL ` RVA 0x35EE0068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b79f9cb9af9daf2e](../../evidence/conditions-sets-071.md#c-b79f9cb9af9daf2e) · [状态效果 S-75a2ca909feae789](../../evidence/state_effects-sets-025.md#s-75a2ca909feae789)

### path-025944

```text
(config)# default carrier-id <cr>
```

Handler ` RVA 0x1E3CD110 `；selector ` 14 `；EOL ` RVA 0x37908E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-765482f38a30f333](../../evidence/conditions-sets-046.md#c-765482f38a30f333) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026166

```text
(config)# default cdp advertise-v2 <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 4 `；EOL ` RVA 0x33CE2238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-06df25eb97fd6633](../../evidence/conditions-sets-003.md#c-06df25eb97fd6633) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028157

```text
(config)# default cdp filter-tlv-list <string> <cr>
```

Handler ` RVA 0xCD9E990 `；selector ` 0 `；EOL ` RVA 0x33CE3FF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Filter tlv-list。

[条件 C-5b7d8887077493a1](../../evidence/conditions-sets-036.md#c-5b7d8887077493a1) · [参数 P-c824308fcdb2caee](../../evidence/parameters-sets-015.md#p-c824308fcdb2caee) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025578

```text
(config)# default cdp holdtime <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 2 `；EOL ` RVA 0x33CE24E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ddac59a18b31f560](../../evidence/conditions-sets-085.md#c-ddac59a18b31f560) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034077

```text
(config)# default cdp log mismatch duplex <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 6 `；EOL ` RVA 0x33CE2B08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1a3d3d7ed5c4d4fa](../../evidence/conditions-sets-010.md#c-1a3d3d7ed5c4d4fa) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026268

```text
(config)# default cdp run <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 0 `；EOL ` RVA 0x33CE3250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9bbbf4f0d591d83f](../../evidence/conditions-sets-060.md#c-9bbbf4f0d591d83f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026282

```text
(config)# default cdp source-interface <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 5 `；EOL ` RVA 0x33CE2EA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-705ccbcd73a381c3](../../evidence/conditions-sets-043.md#c-705ccbcd73a381c3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025570

```text
(config)# default cdp timer <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 1 `；EOL ` RVA 0x33CE2260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-671349144ff00636](../../evidence/conditions-sets-040.md#c-671349144ff00636) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028169

```text
(config)# default cdp tlv app <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 8 `；EOL ` RVA 0x33CE38F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3c22a7479591fc0](../../evidence/conditions-sets-076.md#c-c3c22a7479591fc0) · [状态效果 S-39e81a9250e5a955](../../evidence/state_effects-sets-013.md#s-39e81a9250e5a955)

### path-028092

```text
(config)# default cdp tlv location <cr>
```

Handler ` RVA 0xCD9F6D0 `；selector ` 8 `；EOL ` RVA 0x33CE35B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3504ec8090020a69](../../evidence/conditions-sets-021.md#c-3504ec8090020a69) · [状态效果 S-3df8f57349da37c8](../../evidence/state_effects-sets-014.md#s-3df8f57349da37c8)

### path-028124

```text
(config)# default cdp tlv-list <string> <cr>
```

Handler ` RVA 0xCD9DBD0 `；selector ` 0 `；EOL ` RVA 0x33CE3CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Tlv-list。

[条件 C-549e45da6980b349](../../evidence/conditions-sets-033.md#c-549e45da6980b349) · [参数 P-af7cf7003dc8a9d1](../../evidence/parameters-sets-013.md#p-af7cf7003dc8a9d1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026310

```text
(config)# default cef common <cr>
```

Handler ` RVA 0xB5AEF90 `；selector ` 0 `；EOL ` RVA 0x337AE698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-00573d6238a90e3d](../../evidence/conditions-sets-001.md#c-00573d6238a90e3d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034464

```text
(config)# default cef table consistency-check IPv4 <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 1 `；EOL ` RVA 0x337AFCD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-108862e71d524c23](../../evidence/conditions-sets-007.md#c-108862e71d524c23) · [状态效果 S-311c122ba55efa48](../../evidence/state_effects-sets-011.md#s-311c122ba55efa48)

### path-044256

```text
(config)# default cef table consistency-check IPv4 auto-repair <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 3 `；EOL ` RVA 0x337AFD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8ea55380fd002152](../../evidence/conditions-sets-055.md#c-8ea55380fd002152) · [状态效果 S-311c122ba55efa48](../../evidence/state_effects-sets-011.md#s-311c122ba55efa48)

### path-044118

```text
(config)# default cef table consistency-check IPv4 data-checking <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 4 `；EOL ` RVA 0x337AF720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf71e5d6bf7e76f4](../../evidence/conditions-sets-080.md#c-cf71e5d6bf7e76f4) · [状态效果 S-311c122ba55efa48](../../evidence/state_effects-sets-011.md#s-311c122ba55efa48)

### path-044151

```text
(config)# default cef table consistency-check IPv4 error-message <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 2 `；EOL ` RVA 0x337AF9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cf71e5d6bf7e76f4](../../evidence/conditions-sets-080.md#c-cf71e5d6bf7e76f4) · [状态效果 S-311c122ba55efa48](../../evidence/state_effects-sets-011.md#s-311c122ba55efa48)

### path-034497

```text
(config)# default cef table download recursive-dependents <cr>
```

Handler ` RVA 0xB2D7FF0 `；selector ` 0 `；EOL ` RVA 0x33734250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d28c1ff10c20f134](../../evidence/conditions-sets-081.md#c-d28c1ff10c20f134) · [状态效果 S-d02ac7c9824ea864](../../evidence/state_effects-sets-044.md#s-d02ac7c9824ea864)

### path-044192

```text
(config)# default cef table output-chain build favor <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 6 `；EOL ` RVA 0x337B0728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-63c113b1816f81fa](../../evidence/conditions-sets-039.md#c-63c113b1816f81fa) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034297

```text
(config)# default cef table rate-monitor-period <number:1..60> <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 7 `；EOL ` RVA 0x337B0390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Period in minutes。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-8b1a86b9e0c550f0](../../evidence/parameters-sets-011.md#p-8b1a86b9e0c550f0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044105

```text
(config)# default cef table vrf tree ipv4 <cr>
```

Handler ` RVA 0xB5C9DE0 `；selector ` 5 `；EOL ` RVA 0x337AEAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3e92029b77bb12cc](../../evidence/conditions-sets-024.md#c-3e92029b77bb12cc) · [状态效果 S-d0729fbcb2512853](../../evidence/state_effects-sets-044.md#s-d0729fbcb2512853)

### path-027364

```text
(config)# default chat-script <string> <cr>
```

Handler ` RVA 0xF2F26F0 `；selector ` 0 `；EOL ` RVA 0x34603588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of chat script。

[条件 C-6feeaf49f9a4201a](../../evidence/conditions-sets-043.md#c-6feeaf49f9a4201a) · [参数 P-9df78cf9aa95b706](../../evidence/parameters-sets-012.md#p-9df78cf9aa95b706) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026407

```text
(config)# default cisp enable <cr>
```

Handler ` RVA 0xCB250A0 `；selector ` 1 `；EOL ` RVA 0x33BB5180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026369

```text
(config)# default class-map <string> <cr>
```

Handler ` RVA 0xD8806E0 `；selector ` 0 `；EOL ` RVA 0x33F141E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` class-map name。

[条件 C-46ffbf7f816d27a4](../../evidence/conditions-sets-028.md#c-46ffbf7f816d27a4) · [参数 P-2990068f5234917c](../../evidence/parameters-sets-004.md#p-2990068f5234917c) · [状态效果 S-59a119f8212d15a8](../../evidence/state_effects-sets-019.md#s-59a119f8212d15a8)

### path-034688

```text
(config)# default class-map type control <string> <cr>
```

Handler ` RVA 0x10A59FE0 `；selector ` 0 `；EOL ` RVA 0x34C21928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of class-map。

[条件 C-691e8554f9f8451b](../../evidence/conditions-sets-041.md#c-691e8554f9f8451b) · [参数 P-8bacc2b4896dc45c](../../evidence/parameters-sets-011.md#p-8bacc2b4896dc45c) · [状态效果 S-64d3780b1654eefb](../../evidence/state_effects-sets-022.md#s-64d3780b1654eefb)

### path-052291

```text
(config)# default class-map type control subscriber match-all <string> <cr>
```

Handler ` RVA 0xCB630C0 `；selector ` 0 `；EOL ` RVA 0x33BF7BF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of identity class-map。

[条件 C-584eb74e3857a35d](../../evidence/conditions-sets-035.md#c-584eb74e3857a35d) · [参数 P-2b4f16183757da84](../../evidence/parameters-sets-004.md#p-2b4f16183757da84) · [状态效果 S-b9454e8c3cd71629](../../evidence/state_effects-sets-039.md#s-b9454e8c3cd71629)

### path-034195

```text
(config)# default class-map type multicast-flows <string> <cr>
```

Handler ` RVA 0xF6D0ED0 `；selector ` 0 `；EOL ` RVA 0x34738730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of class-map。

[条件 C-1b7b4ab2000998e9](../../evidence/conditions-sets-011.md#c-1b7b4ab2000998e9) · [参数 P-0b0642b12039a44e](../../evidence/parameters-sets-001.md#p-0b0642b12039a44e) · [状态效果 S-67228c51b5288a37](../../evidence/state_effects-sets-022.md#s-67228c51b5288a37)

### path-044071

```text
(config)# default class-map type traffic match-any <string> <cr>
```

Handler ` RVA 0x10A611B0 `；selector ` 0 `；EOL ` RVA 0x34C271A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of traffic class-map。

[条件 C-1b7b4ab2000998e9](../../evidence/conditions-sets-011.md#c-1b7b4ab2000998e9) · [参数 P-798833a87dab9b8e](../../evidence/parameters-sets-009.md#p-798833a87dab9b8e) · [状态效果 S-624f442ed49538f0](../../evidence/state_effects-sets-021.md#s-624f442ed49538f0)

### path-028682

```text
(config)# default classmap-template <string> <string> <cr>
```

Handler ` RVA 0x10564EB0 `；selector ` 0 `；EOL ` RVA 0x34B598C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` base class name；` string ` comma delimited string containingacl entries to be added to filters in parameterized class。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-8ff252b3b27ee04a](../../evidence/parameters-sets-011.md#p-8ff252b3b27ee04a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027017

```text
(config)# default clns cache-invalidate-delay <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 35 `；EOL ` RVA 0x34B84EB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-15484e7c5a2c5245](../../evidence/conditions-sets-008.md#c-15484e7c5a2c5245) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025863

```text
(config)# default clns configuration-time <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 21 `；EOL ` RVA 0x34B924E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b018e5c22bdebeef](../../evidence/conditions-sets-068.md#c-b018e5c22bdebeef) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030462

```text
(config)# default clns filter-expr <string> <cr>
```

Handler ` RVA 0x10583A90 `；selector ` 0 `；EOL ` RVA 0x34B93ED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of filter expression。

[条件 C-67a82f2eda24409a](../../evidence/conditions-sets-040.md#c-67a82f2eda24409a) · [参数 P-22091aedf3a32734](../../evidence/parameters-sets-003.md#p-22091aedf3a32734) · [状态效果 S-62dbc532f2fa97fe](../../evidence/state_effects-sets-021.md#s-62dbc532f2fa97fe)

### path-030437

```text
(config)# default clns filter-set <string> <cr>
```

Handler ` RVA 0x10582270 `；selector ` 0 `；EOL ` RVA 0x34B93A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of filter set。

[条件 C-ecc431517c7ac56f](../../evidence/conditions-sets-091.md#c-ecc431517c7ac56f) · [参数 P-6fbf2ba30783234e](../../evidence/parameters-sets-009.md#p-6fbf2ba30783234e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025871

```text
(config)# default clns holding-time <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 23 `；EOL ` RVA 0x34B92548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8b1472304c03c6d5](../../evidence/conditions-sets-054.md#c-8b1472304c03c6d5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029440

```text
(config)# default clns host <string> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 22 `；EOL ` RVA 0x34B842F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name to give to a NSAP。

[条件 C-02ca263335963e64](../../evidence/conditions-sets-002.md#c-02ca263335963e64) · [参数 P-75e7c10108620ee3](../../evidence/parameters-sets-009.md#p-75e7c10108620ee3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030174

```text
(config)# default clns net <address> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 1 `；EOL ` RVA 0x34B92B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` CLNS address or host name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-385ff22fa02bd36c](../../evidence/parameters-sets-005.md#p-385ff22fa02bd36c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025889

```text
(config)# default clns packet-lifetime <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 24 `；EOL ` RVA 0x34B92DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7db83070181ae7e0](../../evidence/conditions-sets-049.md#c-7db83070181ae7e0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025896

```text
(config)# default clns queue-depth <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 36 `；EOL ` RVA 0x34B92DE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-684f7436c304f745](../../evidence/conditions-sets-040.md#c-684f7436c304f745) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029758

```text
(config)# default clns route <address> <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 25 `；EOL ` RVA 0x34B84990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` NSAP prefix。

[条件 C-df617c3c7aff4e3c](../../evidence/conditions-sets-086.md#c-df617c3c7aff4e3c) · [参数 P-757361b9ee4e7b69](../../evidence/parameters-sets-009.md#p-757361b9ee4e7b69) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027326

```text
(config)# default clns routing <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 27 `；EOL ` RVA 0x34B94AB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eccc7cb2f71a5877](../../evidence/conditions-sets-091.md#c-eccc7cb2f71a5877) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030485

```text
(config)# default clns template-alias <string> <cr>
```

Handler ` RVA 0x10581EE0 `；selector ` 0 `；EOL ` RVA 0x34B94788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Template name。

[条件 C-fb94aa798bc87fe7](../../evidence/conditions-sets-097.md#c-fb94aa798bc87fe7) · [参数 P-41322c6ffc5e959d](../../evidence/parameters-sets-005.md#p-41322c6ffc5e959d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027333

```text
(config)# default clns want-erpdu <cr>
```

Handler ` RVA 0x10590A10 `；selector ` 28 `；EOL ` RVA 0x34B93650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026277

```text
(config)# default clock calendar-valid <cr>
```

Handler ` RVA 0xE039CE0 `；selector ` 0 `；EOL ` RVA 0x34172EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ed34bcb46f1c734a](../../evidence/conditions-sets-092.md#c-ed34bcb46f1c734a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028116

```text
(config)# default clock initialize nvram <cr>
```

Handler ` RVA 0xD70B0E0 `；selector ` 0 `；EOL ` RVA 0x341735A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c7b4effcd8baa15d](../../evidence/conditions-sets-077.md#c-c7b4effcd8baa15d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028172

```text
(config)# default clock save interval <cr>
```

Handler ` RVA 0xE039E60 `；selector ` 0 `；EOL ` RVA 0x341732C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8229a4c9a767c10a](../../evidence/conditions-sets-050.md#c-8229a4c9a767c10a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026281

```text
(config)# default clock summer-time <cr>
```

Handler ` RVA 0xE038CB0 `；selector ` 0 `；EOL ` RVA 0x34172460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a0460a564121a0fb](../../evidence/conditions-sets-062.md#c-a0460a564121a0fb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025607

```text
(config)# default config-register <cr>
```

Handler ` RVA 0xE950C70 `；selector ` 0 `；EOL ` RVA 0x34352370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-396517046a6077d3](../../evidence/conditions-sets-022.md#c-396517046a6077d3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030227

```text
(config)# default configuration mode exclusive <cr>
```

Handler ` RVA 0xDFE8B80 `；selector ` 0 `；EOL ` RVA 0x340BD418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8e11a98e420eb5a5](../../evidence/conditions-sets-055.md#c-8e11a98e420eb5a5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026789

```text
(config)# default connect <string> <cr>
```

Handler ` RVA 0xF43ABC0 `；selector ` 0 `；EOL ` RVA 0x34648398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name for this connection。

[条件 C-592f48400a219a53](../../evidence/conditions-sets-035.md#c-592f48400a219a53) · [参数 P-162edcd88fb53fb2](../../evidence/parameters-sets-002.md#p-162edcd88fb53fb2) · [状态效果 S-e93ecec5f7ad4118](../../evidence/state_effects-sets-049.md#s-e93ecec5f7ad4118)

### path-025856

```text
(config)# default control-plane <cr>
```

Handler ` RVA 0xE47F430 `；selector ` 0 `；EOL ` RVA 0x342C5210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8259f9a4af6fc6d4](../../evidence/conditions-sets-051.md#c-8259f9a4af6fc6d4) · [状态效果 S-ff84ac338ceae66d](../../evidence/state_effects-sets-054.md#s-ff84ac338ceae66d)

### path-034787

```text
(config)# default cops ip dscp ef <cr>
```

Handler ` RVA 0xF446FF0 `；selector ` 0 `；EOL ` RVA 0x3464BDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fc5e34f955776611](../../evidence/conditions-sets-097.md#c-fc5e34f955776611) · [状态效果 S-01d93a1bd21783dd](../../evidence/state_effects-sets-001.md#s-01d93a1bd21783dd)

### path-028665

```text
(config)# default cops listener access-list <cr>
```

Handler ` RVA 0xF446CF0 `；selector ` 0 `；EOL ` RVA 0x3464B5E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2ea3639a89de26ca](../../evidence/conditions-sets-018.md#c-2ea3639a89de26ca) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034742

```text
(config)# default cops tcp window-size <number:516..65535> <cr>
```

Handler ` RVA 0xF4470B0 `；selector ` 0 `；EOL ` RVA 0x3464BA80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Size in bytes。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-7dba7e155c120e9f](../../evidence/parameters-sets-010.md#p-7dba7e155c120e9f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026001

```text
(config)# default coverage history <cr>
```

Handler ` RVA 0xDE877E0 `；selector ` 0 `；EOL ` RVA 0x341478C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-55326ea556244747](../../evidence/conditions-sets-033.md#c-55326ea556244747) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044008

```text
(config)# default crypto RSA-key-pair <string> <number:0..255> <number:0..4294967295> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35838CF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Key pair name；` unsigned_number ` Usage；` unsigned_number ` Generation Timestamp。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-12a1347439a1f629](../../evidence/parameters-sets-002.md#p-12a1347439a1f629) · [状态效果 S-d3ff7be55597781d](../../evidence/state_effects-sets-045.md#s-d3ff7be55597781d)

### path-028107

```text
(config)# default crypto dh lifetime <cr>
```

Handler ` RVA 0x120F3D30 `；selector ` 0 `；EOL ` RVA 0x3579ECD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eefbf4c803275684](../../evidence/conditions-sets-092.md#c-eefbf4c803275684) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028150

```text
(config)# default crypto dh pregen <cr>
```

Handler ` RVA 0x120F3C30 `；selector ` 0 `；EOL ` RVA 0x3579EFF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-19b4bcb19ee411fe](../../evidence/conditions-sets-010.md#c-19b4bcb19ee411fe) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028440

```text
(config)# default crypto engine accelerator <cr>
```

Handler ` RVA 0x120CB850 `；selector ` 0 `；EOL ` RVA 0x3578DFA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-32a577c754b5f541](../../evidence/conditions-sets-020.md#c-32a577c754b5f541) · [状态效果 S-c8c4a014fdceef45](../../evidence/state_effects-sets-043.md#s-c8c4a014fdceef45)

### path-044027

```text
(config)# default crypto engine compliance shield disable <cr>
```

Handler ` RVA 0x1210A590 `；selector ` 0 `；EOL ` RVA 0x357A8190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-329864984b2d7e7b](../../evidence/conditions-sets-020.md#c-329864984b2d7e7b) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034252

```text
(config)# default crypto engine nm <number:0..3> <cr>
```

Handler ` RVA 0x120CB3B0 `；selector ` 0 `；EOL ` RVA 0x3578D7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` NM slot number &lt;0-3&gt;。

[条件 C-ed3286a9813faa7e](../../evidence/conditions-sets-092.md#c-ed3286a9813faa7e) · [参数 P-83ac0da268e733c3](../../evidence/parameters-sets-010.md#p-83ac0da268e733c3) · [状态效果 S-8540c777e3582185](../../evidence/state_effects-sets-028.md#s-8540c777e3582185)

### path-028148

```text
(config)# default crypto engine queue-size <cr>
```

Handler ` RVA 0x12119480 `；selector ` 0 `；EOL ` RVA 0x357A78A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a5c43a4388e0a78a](../../evidence/conditions-sets-064.md#c-a5c43a4388e0a78a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034134

```text
(config)# default crypto engine software ipsec <cr>
```

Handler ` RVA 0x121195B0 `；selector ` 0 `；EOL ` RVA 0x357A7B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034164

```text
(config)# default crypto engine software isakmp <cr>
```

Handler ` RVA 0x121196E0 `；selector ` 0 `；EOL ` RVA 0x357A7E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034506

```text
(config)# default crypto key decrypt rsa <cr>
```

Handler ` RVA 0x123A3E60 `；selector ` 1 `；EOL ` RVA 0x35835120 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-5059040ea021fbf4](../../evidence/state_effects-sets-018.md#s-5059040ea021fbf4)

### path-034460

```text
(config)# default crypto key encrypt rsa <cr>
```

Handler ` RVA 0x123A3E60 `；selector ` 0 `；EOL ` RVA 0x35834C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-15ffb0b188091579](../../evidence/state_effects-sets-005.md#s-15ffb0b188091579)

### path-059627

```text
(config)# default crypto key export ec <string> pem terminal 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35837268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` ec key label；` string ` Passphrase used to protect the private key。

[条件 C-467425c52844b023](../../evidence/conditions-sets-028.md#c-467425c52844b023) · [参数 P-4d8bba577b7ab7b7](../../evidence/parameters-sets-006.md#p-4d8bba577b7ab7b7) · [状态效果 S-875550e016be662c](../../evidence/state_effects-sets-029.md#s-875550e016be662c)

### path-059624

```text
(config)# default crypto key export rsa <string> pem terminal 3des <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` RSA key label；` string ` Passphrase used to protect the private key。

[条件 C-5d5bd329befeaec5](../../evidence/conditions-sets-036.md#c-5d5bd329befeaec5) · [参数 P-5e7b35cad7819108](../../evidence/parameters-sets-008.md#p-5e7b35cad7819108) · [状态效果 S-d2d2d75a4bb9e368](../../evidence/state_effects-sets-045.md#s-d2d2d75a4bb9e368)

### path-052111

```text
(config)# default crypto key generate ec keysize <number:256..256> <cr>
```

Handler ` RVA 0x123A92D0 `；selector ` 3 `；EOL ` RVA 0x358346E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` 256 bit keys。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-343b4cf8bed1ae88](../../evidence/parameters-sets-004.md#p-343b4cf8bed1ae88) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-034326

```text
(config)# default crypto key generate rsa <cr>
```

Handler ` RVA 0x123AA0C0 `；selector ` 15 `；EOL ` RVA 0x358341D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-1be4983520a27cec](../../evidence/conditions-sets-011.md#c-1be4983520a27cec) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-052161

```text
(config)# default crypto key import ec <string> terminal <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x358381B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` EC key label。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-e69a93f63ee3b0a6](../../evidence/parameters-sets-017.md#p-e69a93f63ee3b0a6) · [状态效果 S-6fc4acdca97f1873](../../evidence/state_effects-sets-024.md#s-6fc4acdca97f1873)

### path-052229

```text
(config)# default crypto key import rsa <string> terminal <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35837D20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` RSA key label。

[条件 C-330b9cbc88e262c8](../../evidence/conditions-sets-020.md#c-330b9cbc88e262c8) · [参数 P-b0a9c3bfc80636fc](../../evidence/parameters-sets-013.md#p-b0a9c3bfc80636fc) · [状态效果 S-823be6552aabee02](../../evidence/state_effects-sets-028.md#s-823be6552aabee02)

### path-044054

```text
(config)# default crypto key move rsa <string> <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` RSA key label。

[条件 C-e1f88ae436324afa](../../evidence/conditions-sets-087.md#c-e1f88ae436324afa) · [参数 P-444babfe34822919](../../evidence/parameters-sets-006.md#p-444babfe34822919) · [状态效果 S-f49a1b95a7027dd4](../../evidence/state_effects-sets-052.md#s-f49a1b95a7027dd4)

### path-028211

```text
(config)# default crypto key pubkey-chain <cr>
```

Handler ` RVA 0x123A6B80 `；selector ` 0 `；EOL ` RVA 0x35838568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9791ceb261ababd0](../../evidence/conditions-sets-058.md#c-9791ceb261ababd0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028276

```text
(config)# default crypto key storage <cr>
```

Handler ` RVA 0x121535B0 `；selector ` 17 `；EOL ` RVA 0x35838898 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-54ed9fd49bf4662c](../../evidence/conditions-sets-033.md#c-54ed9fd49bf4662c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028176

```text
(config)# default crypto key zeroize <cr>
```

Handler ` RVA 0x123A44C0 `；selector ` 0 `；EOL ` RVA 0x35836060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-cc29da98009c221e](../../evidence/state_effects-sets-043.md#s-cc29da98009c221e)

### path-037612

```text
(config)# default crypto pki authenticate <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 1 `；EOL ` RVA 0x3574A628 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-a493bd4fde1f6f87](../../evidence/parameters-sets-013.md#p-a493bd4fde1f6f87) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047219

```text
(config)# default crypto pki certificate chain <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 18 `；EOL ` RVA 0x3574D400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-877c0bda626030dd](../../evidence/parameters-sets-010.md#p-877c0bda626030dd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047288

```text
(config)# default crypto pki certificate map <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 23 `；EOL ` RVA 0x3574D080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Certificate attribute map tag。

[条件 C-5d831c6baf3e9b83](../../evidence/conditions-sets-036.md#c-5d831c6baf3e9b83) · [参数 P-f4963e28b36c89f8](../../evidence/parameters-sets-018.md#p-f4963e28b36c89f8) · [状态效果 S-b4a455cbd6ca06e3](../../evidence/state_effects-sets-038.md#s-b4a455cbd6ca06e3)

### path-038005

```text
(config)# default crypto pki certificate pool <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 112 `；EOL ` RVA 0x3574D6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037834

```text
(config)# default crypto pki certificate query <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 3 `；EOL ` RVA 0x3574CC78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047380

```text
(config)# default crypto pki certificate self-signed hash <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 120 `；EOL ` RVA 0x3574E2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-407677f5ad3d5a7a](../../evidence/conditions-sets-025.md#c-407677f5ad3d5a7a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-038112

```text
(config)# default crypto pki certificate storage <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 50 `；EOL ` RVA 0x3574DD10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6ad1c8375b6ab770](../../evidence/conditions-sets-041.md#c-6ad1c8375b6ab770) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047234

```text
(config)# default crypto pki certificate validate <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 36 `；EOL ` RVA 0x3574D9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` trust point。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b01d97b8ece37da7](../../evidence/parameters-sets-013.md#p-b01d97b8ece37da7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047285

```text
(config)# default crypto pki crl cache size <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 31 `；EOL ` RVA 0x3574FEE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-527aa9b9269a7801](../../evidence/conditions-sets-032.md#c-527aa9b9269a7801) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057970

```text
(config)# default crypto pki crl download schedule prepublish <number:0..65535> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 117 `；EOL ` RVA 0x3574EC38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Time interval to Pre-download CRL before CRL expiry。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-5b262c73fd51666f](../../evidence/parameters-sets-007.md#p-5b262c73fd51666f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057978

```text
(config)# default crypto pki crl download schedule retries <number:1..15> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 119 `；EOL ` RVA 0x3574EF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` number of retries。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-d282ece9b775b32f](../../evidence/parameters-sets-016.md#p-d282ece9b775b32f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-054383

```text
(config)# default crypto pki crl download trustpoint <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 116 `；EOL ` RVA 0x3574FB60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of Trustpoint to use for CRL download。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-aa72afc5dc21aaf4](../../evidence/parameters-sets-013.md#p-aa72afc5dc21aaf4) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-054415

```text
(config)# default crypto pki crl download url <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 115 `；EOL ` RVA 0x3574F778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` http or ldap url。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-f7d977c82f857994](../../evidence/parameters-sets-018.md#p-f7d977c82f857994) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047177

```text
(config)# default crypto pki crl request <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 17 `；EOL ` RVA 0x3574E848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b94220b02a9d2fc4](../../evidence/parameters-sets-014.md#p-b94220b02a9d2fc4) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037720

```text
(config)# default crypto pki enroll <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 15 `；EOL ` RVA 0x3574A978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-1f830e14f538908c](../../evidence/parameters-sets-003.md#p-1f830e14f538908c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-054375

```text
(config)# default crypto pki export <string> pem terminal <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 9 `；EOL ` RVA 0x3574C450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with。

[条件 C-f14fc9b7c9d7ff3f](../../evidence/conditions-sets-093.md#c-f14fc9b7c9d7ff3f) · [参数 P-9546f4da27c00d6b](../../evidence/parameters-sets-011.md#p-9546f4da27c00d6b) · [状态效果 S-c57041021a79bdc5](../../evidence/state_effects-sets-042.md#s-c57041021a79bdc5)

### path-057953

```text
(config)# default crypto pki export <string> pem terminal rollover <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 10 `；EOL ` RVA 0x3574C070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-9546f4da27c00d6b](../../evidence/parameters-sets-011.md#p-9546f4da27c00d6b) · [状态效果 S-6a3523b51d41e22c](../../evidence/state_effects-sets-023.md#s-6a3523b51d41e22c)

### path-059340

```text
(config)# default crypto pki export <string> pkcs12 terminal password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 6 `；EOL ` RVA 0x3574BC68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trustpoint label to associate keys and certs with；` string ` Passphrase used to protect the pkcs12 file。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-7ef11695fcfc8786](../../evidence/parameters-sets-010.md#p-7ef11695fcfc8786) · [状态效果 S-5d5b58a82a088040](../../evidence/state_effects-sets-020.md#s-5d5b58a82a088040)

### path-038008

```text
(config)# default crypto pki http max-buffer-size <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 122 `；EOL ` RVA 0x35750280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-736826a90de16fa2](../../evidence/conditions-sets-045.md#c-736826a90de16fa2) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047140

```text
(config)# default crypto pki import <string> certificate <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 16 `；EOL ` RVA 0x3574B7F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-b66c5879120dbef0](../../evidence/parameters-sets-014.md#p-b66c5879120dbef0) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059343

```text
(config)# default crypto pki import <string> pem terminal password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 7 `；EOL ` RVA 0x3574B4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with；` string ` Passphrase used to protect the private key。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-018311bd803f2671](../../evidence/parameters-sets-001.md#p-018311bd803f2671) · [状态效果 S-1af460a6e569dbd8](../../evidence/state_effects-sets-006.md#s-1af460a6e569dbd8)

### path-059341

```text
(config)# default crypto pki import <string> pkcs12 terminal password <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 4 `；EOL ` RVA 0x3574AF50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Trustpoint label to associate certificate or pkcs-12 file with；` string ` Passphrase used to protect the pkcs12 file。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-532840c65e552ec1](../../evidence/parameters-sets-007.md#p-532840c65e552ec1) · [状态效果 S-7b0eabe5e89cd9a0](../../evidence/state_effects-sets-026.md#s-7b0eabe5e89cd9a0)

### path-047163

```text
(config)# default crypto pki profile enrollment <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 27 `；EOL ` RVA 0x3574C980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Certificate enrollment profile tag。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-a2210f57c2ffc457](../../evidence/parameters-sets-012.md#p-a2210f57c2ffc457) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037721

```text
(config)# default crypto pki server <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 33 `；EOL ` RVA 0x33871378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-27be11738d9231ce](../../evidence/conditions-sets-016.md#c-27be11738d9231ce) · [参数 P-1bed6ccbf092ba27](../../evidence/parameters-sets-003.md#p-1bed6ccbf092ba27) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047120

```text
(config)# default crypto pki server <string> rollover <cr>
```

Handler ` RVA 0xBBB8230 `；selector ` 34 `；EOL ` RVA 0x338713E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-081f59a8dd484058](../../evidence/conditions-sets-004.md#c-081f59a8dd484058) · [参数 P-1bed6ccbf092ba27](../../evidence/parameters-sets-003.md#p-1bed6ccbf092ba27) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-054278

```text
(config)# default crypto pki server <string> rollover cancel <cr>
```

Handler ` RVA 0xBBB8230 `；selector ` 35 `；EOL ` RVA 0x338713B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Certificate Server Name。

[条件 C-081f59a8dd484058](../../evidence/conditions-sets-004.md#c-081f59a8dd484058) · [参数 P-1bed6ccbf092ba27](../../evidence/parameters-sets-003.md#p-1bed6ccbf092ba27) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037583

```text
(config)# default crypto pki trustpoint <string> <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 19 `；EOL ` RVA 0x35749928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` CA Server Name。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [参数 P-bd0edbaeffc60831](../../evidence/parameters-sets-014.md#p-bd0edbaeffc60831) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037665

```text
(config)# default crypto pki trustpool clean <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 113 `；EOL ` RVA 0x35749FA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-1f4b3fe2e73d6162](../../evidence/state_effects-sets-007.md#s-1f4b3fe2e73d6162)

### path-037575

```text
(config)# default crypto pki trustpool policy <cr>
```

Handler ` RVA 0x11F19FB0 `；selector ` 111 `；EOL ` RVA 0x35749C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028082

```text
(config)# default crypto provisioning petitioner <cr>
```

Handler ` RVA 0x12E02540 `；selector ` 0 `；EOL ` RVA 0x359E3C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028122

```text
(config)# default crypto provisioning registrar <cr>
```

Handler ` RVA 0x12E02540 `；selector ` 1 `；EOL ` RVA 0x359E3F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-031101

```text
(config)# default cts policy-server device-id <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 3 `；EOL ` RVA 0x359F7A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-119aab07fbb8bf02](../../evidence/conditions-sets-007.md#c-119aab07fbb8bf02) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037987

```text
(config)# default cts policy-server name <string> <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 0 `；EOL ` RVA 0x359F6E50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name for the policy server configuration。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-b4da26b659e349ff](../../evidence/parameters-sets-014.md#p-b4da26b659e349ff) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-038110

```text
(config)# default cts policy-server order random <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 2 `；EOL ` RVA 0x359F7730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-58694a14668c30b4](../../evidence/conditions-sets-035.md#c-58694a14668c30b4) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-031060

```text
(config)# default cts policy-server username <cr>
```

Handler ` RVA 0x12F571F0 `；selector ` 1 `；EOL ` RVA 0x359F7198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-50f3d9f822d1e19d](../../evidence/conditions-sets-032.md#c-50f3d9f822d1e19d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029234

```text
(config)# default cts role-based enforcement <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 0 `；EOL ` RVA 0x35CFA6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3c2a529e2ab1a1fd](../../evidence/conditions-sets-023.md#c-3c2a529e2ab1a1fd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-045012

```text
(config)# default cts role-based enforcement logging-interval <number:5..86400> <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 14 `；EOL ` RVA 0x35CFA6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter logging interval in seconds。

[条件 C-e8be9f72014ed63c](../../evidence/conditions-sets-090.md#c-e8be9f72014ed63c) · [参数 P-ab0334442b8cbc0d](../../evidence/parameters-sets-013.md#p-ab0334442b8cbc0d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028926

```text
(config)# default cts role-based ipv6-copy <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 6 `；EOL ` RVA 0x35CE8948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-32732e14c3f77d59](../../evidence/conditions-sets-020.md#c-32732e14c3f77d59) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035141

```text
(config)# default cts role-based monitor all <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 12 `；EOL ` RVA 0x35CFB810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14caee070928983d](../../evidence/conditions-sets-008.md#c-14caee070928983d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035325

```text
(config)# default cts role-based policy priority-static <cr>
```

Handler ` RVA 0x142093C0 `；selector ` 13 `；EOL ` RVA 0x35CFAC58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e9f606d272b51a89](../../evidence/conditions-sets-090.md#c-e9f606d272b51a89) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029238

```text
(config)# default cts role-based sgt-caching <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 8 `；EOL ` RVA 0x35CF8668 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d1452a1125e391c7](../../evidence/conditions-sets-081.md#c-d1452a1125e391c7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035256

```text
(config)# default cts role-based sgt-caching with-enforcement <cr>
```

Handler ` RVA 0x1413D6C0 `；selector ` 7 `；EOL ` RVA 0x35CF8358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cbaf825484834ab9](../../evidence/conditions-sets-078.md#c-cbaf825484834ab9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-035338

```text
(config)# default cts role-based sgt-map <address> <cr>
```

Handler ` RVA 0x140400F0 `；selector ` 2 `；EOL ` RVA 0x35CE72E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` IPv4 host address。

[条件 C-d5b58e781740419c](../../evidence/conditions-sets-082.md#c-d5b58e781740419c) · [参数 P-4d4a85f27ad2348e](../../evidence/parameters-sets-006.md#p-4d4a85f27ad2348e) · [状态效果 S-5e3bb34c95d6877c](../../evidence/state_effects-sets-020.md#s-5e3bb34c95d6877c)

### path-030824

```text
(config)# default cts server load-balance <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 4 `；EOL ` RVA 0x35A15D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-523c06ce5f2e4fc8](../../evidence/conditions-sets-032.md#c-523c06ce5f2e4fc8) · [状态效果 S-17c9f95e8e9b7bf9](../../evidence/state_effects-sets-005.md#s-17c9f95e8e9b7bf9)

### path-027485

```text
(config)# default cts sgt <cr>
```

Handler ` RVA 0x130492D0 `；selector ` 0 `；EOL ` RVA 0x35A161B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f4f55bf88ca2e48](../../evidence/conditions-sets-049.md#c-7f4f55bf88ca2e48) · [状态效果 S-bae588d473825d87](../../evidence/state_effects-sets-039.md#s-bae588d473825d87)

### path-031017

```text
(config)# default cts sxp enable <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 49 `；EOL ` RVA 0x35A4D6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [状态效果 S-715e4dec1c41c153](../../evidence/state_effects-sets-024.md#s-715e4dec1c41c153)

### path-038023

```text
(config)# default cts sxp import-list <string> <cr>
```

Handler ` RVA 0x1323A190 `；selector ` 50 `；EOL ` RVA 0x35A4DA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Import-list name。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-edc86fdb67e73efe](../../evidence/parameters-sets-018.md#p-edc86fdb67e73efe) · [状态效果 S-ef41a41a615796a7](../../evidence/state_effects-sets-051.md#s-ef41a41a615796a7)

### path-054433

```text
(config)# default cts sxp limit export peer-sequence-nodes <number:2..64> <cr>
```

Handler ` RVA 0x1322A0D0 `；selector ` 0 `；EOL ` RVA 0x35A4E358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Enter number of nodes。

[条件 C-91bd576ce20249b0](../../evidence/conditions-sets-056.md#c-91bd576ce20249b0) · [参数 P-d8786f70be9cbf6b](../../evidence/parameters-sets-016.md#p-d8786f70be9cbf6b) · [状态效果 S-c5be58213bdfa5c8](../../evidence/state_effects-sets-042.md#s-c5be58213bdfa5c8)

### path-027337

```text
(config)# default cwmp agent <cr>
```

Handler ` RVA 0x164722D0 `；selector ` 0 `；EOL ` RVA 0x35F8A868 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b66b6905226f8885](../../evidence/conditions-sets-071.md#c-b66b6905226f8885) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025897

```text
(config)# default default-value data-character-bits <cr>
```

Handler ` RVA 0xE001B50 `；selector ` 1 `；EOL ` RVA 0x3411D2D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-df2e63ece91c6f59](../../evidence/conditions-sets-086.md#c-df2e63ece91c6f59) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025887

```text
(config)# default default-value exec-character-bits <cr>
```

Handler ` RVA 0xE001B50 `；selector ` 3 `；EOL ` RVA 0x3411CFC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ca6d25d9e2b87aa1](../../evidence/conditions-sets-078.md#c-ca6d25d9e2b87aa1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025894

```text
(config)# default default-value special-character-bits <cr>
```

Handler ` RVA 0xE001B50 `；selector ` 2 `；EOL ` RVA 0x3411D038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7bfe861c4bbbbd98](../../evidence/conditions-sets-048.md#c-7bfe861c4bbbbd98) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028054

```text
(config)# default define interface-range <string> <cr>
```

Handler ` RVA 0xE42FB80 `；selector ` 0 `；EOL ` RVA 0x3411B348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` macro definition。

[条件 C-6f9a301beb661d97](../../evidence/conditions-sets-043.md#c-6f9a301beb661d97) · [参数 P-589ed71e5b1ca069](../../evidence/parameters-sets-007.md#p-589ed71e5b1ca069) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-025936

```text
(config)# default device-tracking <cr>
```

Handler ` RVA 0x1368AFF0 `；selector ` 1123 `；EOL ` RVA 0x35BEACB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-3172ce485a803527](../../evidence/conditions-sets-019.md#c-3172ce485a803527) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030589

```text
(config)# default device-tracking export oper-data <cr>
```

Handler ` RVA 0x13686E40 `；selector ` 0 `；EOL ` RVA 0x35BE6BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-864a43724e5421de](../../evidence/conditions-sets-052.md#c-864a43724e5421de) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027400

```text
(config)# default device-tracking full-proxy <cr>
```

Handler ` RVA 0x1367FFE0 `；selector ` 0 `；EOL ` RVA 0x35BE5D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d35b6c53cff2103d](../../evidence/conditions-sets-081.md#c-d35b6c53cff2103d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037290

```text
(config)# default device-tracking history ip disable <cr>
```

Handler ` RVA 0x13687A40 `；selector ` 0 `；EOL ` RVA 0x35BE6558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-78925a6bb9e8a364](../../evidence/conditions-sets-047.md#c-78925a6bb9e8a364) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037331

```text
(config)# default device-tracking history ip length <cr>
```

Handler ` RVA 0x13687950 `；selector ` 0 `；EOL ` RVA 0x35BE6860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-758460cc8758b53c](../../evidence/conditions-sets-046.md#c-758460cc8758b53c) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027422

```text
(config)# default device-tracking logging <cr>
```

Handler ` RVA 0x136800A0 `；selector ` 0 `；EOL ` RVA 0x35BE60D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4dc32716f5ca3606](../../evidence/conditions-sets-030.md#c-4dc32716f5ca3606) · [状态效果 S-91f4093f1f325753](../../evidence/state_effects-sets-031.md#s-91f4093f1f325753)

### path-030554

```text
(config)# default device-tracking policy <string> <cr>
```

Handler ` RVA 0x1368A1D0 `；selector ` 1100 `；EOL ` RVA 0x35BEA990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name of the device-tracking policy。

[条件 C-42d6ea33c1b6ae7c](../../evidence/conditions-sets-026.md#c-42d6ea33c1b6ae7c) · [参数 P-d4137a6cee565ff9](../../evidence/parameters-sets-016.md#p-d4137a6cee565ff9) · [状态效果 S-2d1fe0cbf0aefdb7](../../evidence/state_effects-sets-010.md#s-2d1fe0cbf0aefdb7)

### path-037408

```text
(config)# default device-tracking service-support device-tracking-layer3 <number:0..7> <cr>
```

Handler ` RVA 0x13687B10 `；selector ` 0 `；EOL ` RVA 0x35BE7A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Support (0: none, 1:port, 2:vlan, 4:box, 7: all, ...)。

[条件 C-0eb82648614b7620](../../evidence/conditions-sets-006.md#c-0eb82648614b7620) · [参数 P-144d9d62b7320cef](../../evidence/parameters-sets-002.md#p-144d9d62b7320cef) · [状态效果 S-0184bfeeebe5318b](../../evidence/state_effects-sets-001.md#s-0184bfeeebe5318b)

### path-030610

```text
(config)# default device-tracking tdl dhcp-stats <cr>
```

Handler ` RVA 0x13687530 `；selector ` 0 `；EOL ` RVA 0x35BE6F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4dc32716f5ca3606](../../evidence/conditions-sets-030.md#c-4dc32716f5ca3606) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037405

```text
(config)# default device-tracking tdl disable dhcp-faults <cr>
```

Handler ` RVA 0x13687350 `；selector ` 0 `；EOL ` RVA 0x35BE7338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cd42f332e909ed8d](../../evidence/conditions-sets-079.md#c-cd42f332e909ed8d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027390

```text
(config)# default device-tracking tracking <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1005 `；EOL ` RVA 0x35BE9FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4770cd6da8bbd6fd](../../evidence/conditions-sets-028.md#c-4770cd6da8bbd6fd) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030508

```text
(config)# default device-tracking tracking auto-source <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1010 `；EOL ` RVA 0x35BE9C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d18e87b1ef5cc1d3](../../evidence/conditions-sets-081.md#c-d18e87b1ef5cc1d3) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030539

```text
(config)# default device-tracking tracking retry-interval <cr>
```

Handler ` RVA 0x13680440 `；selector ` 1006 `；EOL ` RVA 0x35BEA050 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9dbea8dd3cf9bac3](../../evidence/conditions-sets-061.md#c-9dbea8dd3cf9bac3) · [状态效果 S-bae1e9aaa7342ae2](../../evidence/state_effects-sets-039.md#s-bae1e9aaa7342ae2)

### path-030477

```text
(config)# default device-tracking unit-test bulk-sync <cr>
```

Handler ` RVA 0x13685F80 `；selector ` 0 `；EOL ` RVA 0x35BDDD68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-054084

```text
(config)# default device-tracking unit-test check-reach vlan <number:0..4096> <address> <cr>
```

Handler ` RVA 0x136868D0 `；selector ` 0 `；EOL ` RVA 0x35BDF0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number；` address ` IPv6 address。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-eda4c24d6d5d3762](../../evidence/parameters-sets-018.md#p-eda4c24d6d5d3762) · [状态效果 S-48adede718d186da](../../evidence/state_effects-sets-016.md#s-48adede718d186da)

### path-030989

```text
(config)# default device-tracking unit-test disable-cli-sync <cr>
```

Handler ` RVA 0x13686B70 `；selector ` 0 `；EOL ` RVA 0x35BE4D98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046932

```text
(config)# default device-tracking unit-test dna vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685460 `；selector ` 0 `；EOL ` RVA 0x35BDFF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-20d6f79d28b3e5cb](../../evidence/parameters-sets-003.md#p-20d6f79d28b3e5cb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-057961

```text
(config)# default device-tracking unit-test ha-sync-msg msg-type bt-entry action enable <cr>
```

Handler ` RVA 0x13686A80 `；selector ` 0 `；EOL ` RVA 0x35BE4560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-ff75631b6ba599ec](../../evidence/state_effects-sets-054.md#s-ff75631b6ba599ec)

### path-046936

```text
(config)# default device-tracking unit-test ip-dhcp-snooping vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13684D10 `；selector ` 0 `；EOL ` RVA 0x35BE1310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-90e7043ba98afd5f](../../evidence/parameters-sets-011.md#p-90e7043ba98afd5f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047001

```text
(config)# default device-tracking unit-test lisp-dt vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13681C10 `；selector ` 0 `；EOL ` RVA 0x35BE16C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-10f24bfd0d125ead](../../evidence/parameters-sets-002.md#p-10f24bfd0d125ead) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030753

```text
(config)# default device-tracking unit-test pgm <cr>
```

Handler ` RVA 0x13680F90 `；selector ` 0 `；EOL ` RVA 0x35BE0538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-046874

```text
(config)# default device-tracking unit-test profile vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13680F50 `；selector ` 0 `；EOL ` RVA 0x35BE0A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-efdb3cde321c553e](../../evidence/parameters-sets-018.md#p-efdb3cde321c553e) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-047196

```text
(config)# default device-tracking unit-test reapply-filters vlan <number:1..4096> <cr>
```

Handler ` RVA 0x13685FF0 `；selector ` 0 `；EOL ` RVA 0x35BE49E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-139592a46b415c0d](../../evidence/parameters-sets-002.md#p-139592a46b415c0d) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-059839

```text
(config)# default device-tracking unit-test replace-policy vlan <number:1..4096> old <string> new <string> <cr>
```

Handler ` RVA 0x13685820 `；selector ` 0 `；EOL ` RVA 0x35BDF9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Vlan number；` string ` old Policy name；` string ` new Policy name。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [参数 P-38fe206d4babd853](../../evidence/parameters-sets-005.md#p-38fe206d4babd853) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030770

```text
(config)# default device-tracking unit-test upgm <cr>
```

Handler ` RVA 0x13680B60 `；selector ` 0 `；EOL ` RVA 0x35BE0EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8eb032aecfb407a9](../../evidence/conditions-sets-055.md#c-8eb032aecfb407a9) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-037384

```text
(config)# default device-tracking unlock policy <string> <cr>
```

Handler ` RVA 0x1368B2C0 `；selector ` 0 `；EOL ` RVA 0x35BE76A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Policy name。

[条件 C-2c4ff5fbef360ca7](../../evidence/conditions-sets-017.md#c-2c4ff5fbef360ca7) · [参数 P-df524c1964bb3064](../../evidence/parameters-sets-017.md#p-df524c1964bb3064) · [状态效果 S-95df98d83bab41af](../../evidence/state_effects-sets-032.md#s-95df98d83bab41af)

### path-027386

```text
(config)# default device-tracking upgrade-cli <cr>
```

Handler ` RVA 0x13689E20 `；selector ` 0 `；EOL ` RVA 0x35BEA5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-4770cd6da8bbd6fd](../../evidence/conditions-sets-028.md#c-4770cd6da8bbd6fd) · [状态效果 S-5893fd312132cb6c](../../evidence/state_effects-sets-019.md#s-5893fd312132cb6c)

### path-031300

```text
(config)# default diagnostic cns publish <cr>
```

Handler ` RVA 0x159C30A0 `；selector ` 1 `；EOL ` RVA 0x35DD3758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8624ead822c08a37](../../evidence/conditions-sets-052.md#c-8624ead822c08a37) · [状态效果 S-6c20490a0c0e71f5](../../evidence/state_effects-sets-023.md#s-6c20490a0c0e71f5)

### path-031157

```text
(config)# default diagnostic event-log size <cr>
```

Handler ` RVA 0xEB6AA60 `；selector ` 0 `；EOL ` RVA 0x343BC1F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7ae26e25be4e5da7](../../evidence/conditions-sets-048.md#c-7ae26e25be4e5da7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027559

```text
(config)# default diagnostic level <cr>
```

Handler ` RVA 0xEB67CD0 `；selector ` 0 `；EOL ` RVA 0x343BC690 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9954bb8bd2034c30](../../evidence/conditions-sets-059.md#c-9954bb8bd2034c30) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-031279

```text
(config)# default diagnostic monitor global <cr>
```

Handler ` RVA 0xEB68B30 `；selector ` 16 `；EOL ` RVA 0x343BCE40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-349bfff1b788f2e1](../../evidence/conditions-sets-020.md#c-349bfff1b788f2e1) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-031217

```text
(config)# default diagnostic monitor syslog <cr>
```

Handler ` RVA 0xEB67E60 `；selector ` 8 `；EOL ` RVA 0x343BCAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-35826832df598b30](../../evidence/conditions-sets-021.md#c-35826832df598b30) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-031138

```text
(config)# default diagnostic soft-error recovery <cr>
```

Handler ` RVA 0xEB6AB70 `；selector ` 0 `；EOL ` RVA 0x343BBD48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0b754a6c1951cc35](../../evidence/conditions-sets-005.md#c-0b754a6c1951cc35) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-036527

```text
(config)# default diameter attribute list <number:0..99> <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 6 `；EOL ` RVA 0x338A66E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` attribute list number。

[条件 C-9a117866ea358fbe](../../evidence/conditions-sets-060.md#c-9a117866ea358fbe) · [参数 P-356573e8ba146437](../../evidence/parameters-sets-005.md#p-356573e8ba146437) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030351

```text
(config)# default diameter gx retransmit <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 32 `；EOL ` RVA 0x338A8160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce5f015119870789](../../evidence/conditions-sets-079.md#c-ce5f015119870789) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030391

```text
(config)# default diameter gx subscription-id-type <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 37 `；EOL ` RVA 0x338A87D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6dadf2b6cf714aae](../../evidence/conditions-sets-042.md#c-6dadf2b6cf714aae) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030368

```text
(config)# default diameter gx tx-timer <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 33 `；EOL ` RVA 0x338A84B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-919a50d1f9dde757](../../evidence/conditions-sets-056.md#c-919a50d1f9dde757) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030267

```text
(config)# default diameter origin host <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 0 `；EOL ` RVA 0x338A7230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd27d90bb143dbfa](../../evidence/conditions-sets-085.md#c-dd27d90bb143dbfa) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030229

```text
(config)# default diameter origin realm <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 1 `；EOL ` RVA 0x338A6F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-20b751ca8723150f](../../evidence/conditions-sets-013.md#c-20b751ca8723150f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030278

```text
(config)# default diameter peer <string> <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 4 `；EOL ` RVA 0x338A7DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` Name for the diameter peer configuration。

[条件 C-79108cf80a05c775](../../evidence/conditions-sets-047.md#c-79108cf80a05c775) · [参数 P-00e60acb19f32338](../../evidence/parameters-sets-001.md#p-00e60acb19f32338) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027205

```text
(config)# default diameter redundancy <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 24 `；EOL ` RVA 0x338A6388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-79108cf80a05c775](../../evidence/conditions-sets-047.md#c-79108cf80a05c775) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-030188

```text
(config)# default diameter timer connection <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 3 `；EOL ` RVA 0x338A6AB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-0f3339f35e31d10f](../../evidence/conditions-sets-006.md#c-0f3339f35e31d10f) · [状态效果 S-f9d91f3e8271d77c](../../evidence/state_effects-sets-053.md#s-f9d91f3e8271d77c)

### path-036727

```text
(config)# default diameter vendor supported vodafone <cr>
```

Handler ` RVA 0xBD07550 `；selector ` 15 `；EOL ` RVA 0x338A79D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-79108cf80a05c775](../../evidence/conditions-sets-047.md#c-79108cf80a05c775) · [状态效果 S-e8d5085e3e911383](../../evidence/state_effects-sets-049.md#s-e8d5085e3e911383)

### path-026917

```text
(config)# default dlsw allroute-netbios <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 6 `；EOL ` RVA 0x354D7A40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026891

```text
(config)# default dlsw allroute-sna <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 5 `；EOL ` RVA 0x354D7798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029320

```text
(config)# default dlsw bridge-group <number:1..255> <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 8 `；EOL ` RVA 0x354D6BE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Assign a Bridge Group to be assigned to DLSw。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [参数 P-69e4dfacabd25d76](../../evidence/parameters-sets-008.md#p-69e4dfacabd25d76) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026784

```text
(config)# default dlsw cache-ignore-netbios-datagram <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 12 `；EOL ` RVA 0x354D49F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026988

```text
(config)# default dlsw circuit-keepalives <cr>
```

Handler ` RVA 0x11453220 `；selector ` 0 `；EOL ` RVA 0x354D92D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026944

```text
(config)# default dlsw disable <cr>
```

Handler ` RVA 0x11421B20 `；selector ` 0 `；EOL ` RVA 0x354D8B78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026617

```text
(config)# default dlsw duplicate-path-bias <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 0 `；EOL ` RVA 0x354D01C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-fae34953773265c8](../../evidence/conditions-sets-097.md#c-fae34953773265c8) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029205

```text
(config)# default dlsw explorerQ-depth <number:10..1000> <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 1 `；EOL ` RVA 0x354D4DB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Maximum Depth of explorer queue in packets。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [参数 P-21aea01164806436](../../evidence/parameters-sets-003.md#p-21aea01164806436) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026514

```text
(config)# default dlsw fast-hpr-support <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 10 `；EOL ` RVA 0x354CDD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029819

```text
(config)# default dlsw group-cache disable <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 8 `；EOL ` RVA 0x354DAE08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029881

```text
(config)# default dlsw group-cache enable <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 9 `；EOL ` RVA 0x354DB0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027158

```text
(config)# default dlsw group-cache max-entries <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 10 `；EOL ` RVA 0x354DB0D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-8aea76509648bd56](../../evidence/conditions-sets-054.md#c-8aea76509648bd56) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027021

```text
(config)# default dlsw history-log <cr>
```

Handler ` RVA 0x11421E20 `；selector ` 0 `；EOL ` RVA 0x354D8EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-14572b19a45b302f](../../evidence/conditions-sets-008.md#c-14572b19a45b302f) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028740

```text
(config)# default dlsw icanreach mac-exclusive <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 3 `；EOL ` RVA 0x354D2E48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-6573039efb55057e](../../evidence/state_effects-sets-022.md#s-6573039efb55057e)

### path-029765

```text
(config)# default dlsw llc2 nornr <cr>
```

Handler ` RVA 0x11421D80 `；selector ` 1 `；EOL ` RVA 0x354DAB10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026661

```text
(config)# default dlsw load-balance <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 0 `；EOL ` RVA 0x354D0530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-448f63092d22b0f7](../../evidence/conditions-sets-027.md#c-448f63092d22b0f7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026446

```text
(config)# default dlsw local-peer <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 0 `；EOL ` RVA 0x354CC830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-bbc7551ef67356d7](../../evidence/conditions-sets-072.md#c-bbc7551ef67356d7) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044931

```text
(config)# default dlsw mac-addr <address> ring <number:0..4095> <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 3 `；EOL ` RVA 0x354D52C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MAC Address；` unsigned_number ` Ring number。

[条件 C-7e7058e191dfb0f0](../../evidence/conditions-sets-049.md#c-7e7058e191dfb0f0) · [参数 P-ea4dae8e32906a28](../../evidence/parameters-sets-018.md#p-ea4dae8e32906a28) · [状态效果 S-2e5a870ae6894b1b](../../evidence/state_effects-sets-010.md#s-2e5a870ae6894b1b)

### path-044932

```text
(config)# default dlsw mac-addr <address> ring <number:0..4095> <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 4 `；EOL ` RVA 0x354D52E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` MAC Address；` unsigned_number ` Ring number。

[条件 C-ecade62fa96a3043](../../evidence/conditions-sets-091.md#c-ecade62fa96a3043) · [参数 P-ea4dae8e32906a28](../../evidence/parameters-sets-018.md#p-ea4dae8e32906a28) · [状态效果 S-2e5a870ae6894b1b](../../evidence/state_effects-sets-010.md#s-2e5a870ae6894b1b)

### path-025732

```text
(config)# default dlsw max-multiple-rifs <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 11 `；EOL ` RVA 0x354D3A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f433582e61a5f755](../../evidence/conditions-sets-094.md#c-f433582e61a5f755) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027125

```text
(config)# default dlsw multicast <cr>
```

Handler ` RVA 0x11418A50 `；selector ` 0 `；EOL ` RVA 0x354DA828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026473

```text
(config)# default dlsw netbios-cache-length <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 11 `；EOL ` RVA 0x354CD710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a379393da2fb9fbb](../../evidence/conditions-sets-063.md#c-a379393da2fb9fbb) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027032

```text
(config)# default dlsw netbios-keepalive-filter <cr>
```

Handler ` RVA 0x11418A90 `；selector ` 1 `；EOL ` RVA 0x354D9820 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026775

```text
(config)# default dlsw peer-log-changes <cr>
```

Handler ` RVA 0x11418C10 `；selector ` 0 `；EOL ` RVA 0x354D41D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ce838a18638bb229](../../evidence/conditions-sets-080.md#c-ce838a18638bb229) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026905

```text
(config)# default dlsw peer-on-demand-defaults <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 5 `；EOL ` RVA 0x354D5C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c20d0a5c2e99ab57](../../evidence/conditions-sets-075.md#c-c20d0a5c2e99ab57) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026971

```text
(config)# default dlsw prom-peer-defaults <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 9 `；EOL ` RVA 0x354D7DB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-887ac8db9ec94a35](../../evidence/conditions-sets-053.md#c-887ac8db9ec94a35) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026732

```text
(config)# default dlsw redundant-rings <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 13 `；EOL ` RVA 0x354D3AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-934b894a2a04a4a5](../../evidence/conditions-sets-057.md#c-934b894a2a04a4a5) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-044551

```text
(config)# default dlsw remote-peer <number:0..4095> tcp <address> <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 1 `；EOL ` RVA 0x354D0A70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Remote peer ring group list；` address ` Remote peer IP address。

[条件 C-66872c1b444661b0](../../evidence/conditions-sets-040.md#c-66872c1b444661b0) · [参数 P-4abb61377bb7ea27](../../evidence/parameters-sets-006.md#p-4abb61377bb7ea27) · [状态效果 S-f1b9fb0ae18b842a](../../evidence/state_effects-sets-051.md#s-f1b9fb0ae18b842a)

### path-026624

```text
(config)# default dlsw rsvp <cr>
```

Handler ` RVA 0x114938E0 `；selector ` 0 `；EOL ` RVA 0x354CFDD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ffdf34825c11851a](../../evidence/conditions-sets-099.md#c-ffdf34825c11851a) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026468

```text
(config)# default dlsw snmp-traps-extended <cr>
```

Handler ` RVA 0x11418F50 `；selector ` 12 `；EOL ` RVA 0x354CDA00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026742

```text
(config)# default dlsw tbridge-maxmtu-4472 <cr>
```

Handler ` RVA 0x11418B90 `；selector ` 0 `；EOL ` RVA 0x354D44A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028531

```text
(config)# default dlsw timer sna-explorer-timeout <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 2 `；EOL ` RVA 0x354CF0D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e2c8bfc22a974d56](../../evidence/conditions-sets-087.md#c-e2c8bfc22a974d56) · [状态效果 S-74446067e669ac04](../../evidence/state_effects-sets-025.md#s-74446067e669ac04)

### path-029628

```text
(config)# default dlsw tos disable <cr>
```

Handler ` RVA 0x11418AD0 `；selector ` 0 `；EOL ` RVA 0x354D9B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-029798

```text
(config)# default dlsw tos map <cr>
```

Handler ` RVA 0x11418AD0 `；selector ` 1 `；EOL ` RVA 0x354D9E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a10dd35e0fe15595](../../evidence/conditions-sets-062.md#c-a10dd35e0fe15595) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027063

```text
(config)# default dlsw tos-disable <cr>
```

Handler ` RVA 0x11418AD0 `；selector ` 2 `；EOL ` RVA 0x354DA4D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-028558

```text
(config)# default dlsw touch-timer touch-nb-cache-timeout <cr>
```

Handler ` RVA 0x114532A0 `；selector ` 7 `；EOL ` RVA 0x354CF9F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dd48f3e4db72a00d](../../evidence/conditions-sets-085.md#c-dd48f3e4db72a00d) · [状态效果 S-f0d7fcc616c5f07d](../../evidence/state_effects-sets-051.md#s-f0d7fcc616c5f07d)

### path-029873

```text
(config)# default dlsw transparent switch-support <cr>
```

Handler ` RVA 0x11418B10 `；selector ` 1 `；EOL ` RVA 0x354DB638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-027009

```text
(config)# default dlsw udp-disable <cr>
```

Handler ` RVA 0x11418B50 `；selector ` 0 `；EOL ` RVA 0x354D9578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)

### path-026765

```text
(config)# default dlsw xid-modify-tws <cr>
```

Handler ` RVA 0x11418BD0 `；selector ` 0 `；EOL ` RVA 0x354D4750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-25454df297d7c169](../../evidence/conditions-sets-015.md#c-25454df297d7c169) · [状态效果 S-9a09e3013796110f](../../evidence/state_effects-sets-033.md#s-9a09e3013796110f)
