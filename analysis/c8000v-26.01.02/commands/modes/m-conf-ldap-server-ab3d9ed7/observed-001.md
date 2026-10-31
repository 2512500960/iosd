# conf-ldap-server · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007981

```text
(config-ldap-server)# attribute map <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 2 `；EOL ` RVA 0x35610858 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Attribute map name。

[参数 P-f779b386f345c6c1](../../evidence/parameters-sets-018.md#p-f779b386f345c6c1)

### observed_connections-007967

```text
(config-ldap-server)# authentication bind-first <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 9 `；EOL ` RVA 0x3560FEB8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007969

```text
(config-ldap-server)# authentication compare <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 10 `；EOL ` RVA 0x356101A8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007990

```text
(config-ldap-server)# automate-tester username <string> probe-on <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 27 `；EOL ` RVA 0x35610F58 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Enter the username。

[参数 P-19f6886a94535ee2](../../evidence/parameters-sets-002.md#p-19f6886a94535ee2)

### observed_connections-007966

```text
(config-ldap-server)# base-dn <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 11 `；EOL ` RVA 0x3560FB40 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Base DN String。

[条件 C-0bcd0866876a70c2](../../evidence/conditions-sets-005.md#c-0bcd0866876a70c2) · [参数 P-5dd25fc2a04496d2](../../evidence/parameters-sets-008.md#p-5dd25fc2a04496d2)

### observed_connections-007992

```text
(config-ldap-server)# bind authenticate root-dn <string> password <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 8 `；EOL ` RVA 0x3560DAB8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Username string；` string ` The UNENCRYPTED (cleartext) password。

[条件 C-d473a97ccb7028d4](../../evidence/conditions-sets-082.md#c-d473a97ccb7028d4) · [参数 P-10686a3b5d1eb92c](../../evidence/parameters-sets-002.md#p-10686a3b5d1eb92c)

### observed_connections-007970

```text
(config-ldap-server)# deadtime <number:1..1440> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 28 `；EOL ` RVA 0x35610BB0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Deadtime in mins。

[条件 C-e2cc95993190cef3](../../evidence/conditions-sets-087.md#c-e2cc95993190cef3) · [参数 P-35ca4131a2818169](../../evidence/parameters-sets-005.md#p-35ca4131a2818169)

### observed_connections-007958

```text
(config-ldap-server)# exit <cr>
```

Handler ` RVA 0x11ABCD10 `；selector ` 0 `；EOL ` RVA 0x355E9BE0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-36f0c9deb0ffa88f](../../evidence/conditions-sets-021.md#c-36f0c9deb0ffa88f)

### observed_connections-007964

```text
(config-ldap-server)# fqdn <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 34 `；EOL ` RVA 0x3560F458 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Fully Qualified Domain name。

[条件 C-3bf4e9328295b674](../../evidence/conditions-sets-023.md#c-3bf4e9328295b674) · [参数 P-dc5488c150138b67](../../evidence/parameters-sets-017.md#p-dc5488c150138b67)

### observed_connections-007960

```text
(config-ldap-server)# ipv4 <address> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 15 `；EOL ` RVA 0x3560EDC8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv4 Address of LDAP Server。

[条件 C-172cf48d8d83e259](../../evidence/conditions-sets-009.md#c-172cf48d8d83e259) · [参数 P-e22e8db12e6c1dfb](../../evidence/parameters-sets-017.md#p-e22e8db12e6c1dfb)

### observed_connections-007962

```text
(config-ldap-server)# ipv6 <address> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 16 `；EOL ` RVA 0x3560F110 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 Address of LDAP Server。

[条件 C-a422131c5b427955](../../evidence/conditions-sets-063.md#c-a422131c5b427955) · [参数 P-b1f358f7ed095435](../../evidence/parameters-sets-013.md#p-b1f358f7ed095435)

### observed_connections-007959

```text
(config-ldap-server)# mode secure <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 5 `；EOL ` RVA 0x3560E1A0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[状态效果 S-267ff5e8fb6201d1](../../evidence/state_effects-sets-009.md#s-267ff5e8fb6201d1)

### observed_connections-007988

```text
(config-ldap-server)# no attribute map <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 2 `；EOL ` RVA 0x35610858 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Attribute map name。

[参数 P-f779b386f345c6c1](../../evidence/parameters-sets-018.md#p-f779b386f345c6c1) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007980

```text
(config-ldap-server)# no authentication bind-first <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 9 `；EOL ` RVA 0x3560FEB8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007983

```text
(config-ldap-server)# no authentication compare <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 10 `；EOL ` RVA 0x356101A8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007991

```text
(config-ldap-server)# no automate-tester username <string> probe-on <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 27 `；EOL ` RVA 0x35610F58 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Enter the username。

[参数 P-19f6886a94535ee2](../../evidence/parameters-sets-002.md#p-19f6886a94535ee2) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007968

```text
(config-ldap-server)# no base-dn <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 11 `；EOL ` RVA 0x3560FB40 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a0f66122732f4375](../../evidence/conditions-sets-062.md#c-a0f66122732f4375) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007973

```text
(config-ldap-server)# no bind authenticate <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 8 `；EOL ` RVA 0x3560DAB8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a94f321fcf51769b](../../evidence/conditions-sets-065.md#c-a94f321fcf51769b) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007971

```text
(config-ldap-server)# no deadtime <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 28 `；EOL ` RVA 0x35610BB0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fa3ca58c95d789b4](../../evidence/conditions-sets-097.md#c-fa3ca58c95d789b4) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007965

```text
(config-ldap-server)# no fqdn <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 34 `；EOL ` RVA 0x3560F458 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-75efc4f0f1f3aec6](../../evidence/conditions-sets-046.md#c-75efc4f0f1f3aec6) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007961

```text
(config-ldap-server)# no ipv4 <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 15 `；EOL ` RVA 0x3560EDC8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-797d8a395f2e5496](../../evidence/conditions-sets-047.md#c-797d8a395f2e5496) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007963

```text
(config-ldap-server)# no ipv6 <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 16 `；EOL ` RVA 0x3560F110 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-832e4daf02dd888f](../../evidence/conditions-sets-051.md#c-832e4daf02dd888f) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007974

```text
(config-ldap-server)# no mode secure <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 5 `；EOL ` RVA 0x3560E1A0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-cdec21f158e29d80](../../evidence/state_effects-sets-044.md#s-cdec21f158e29d80)

### observed_connections-007989

```text
(config-ldap-server)# no search-filter user-object-type <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 17 `；EOL ` RVA 0x35610520 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` Object Class attribute name。

[参数 P-0ccd38986214fcdb](../../evidence/parameters-sets-001.md#p-0ccd38986214fcdb) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007984

```text
(config-ldap-server)# no search-type nested <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 26 `；EOL ` RVA 0x35611610 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007987

```text
(config-ldap-server)# no secure cipher rc4-128-md5 <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 7 `；EOL ` RVA 0x3560E5F0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ac317507ab7585e1](../../evidence/conditions-sets-067.md#c-ac317507ab7585e1) · [状态效果 S-36f46a732642af7c](../../evidence/state_effects-sets-012.md#s-36f46a732642af7c)

### observed_connections-007977

```text
(config-ldap-server)# no secure trustpoint <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 6 `；EOL ` RVA 0x3560EA68 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-788e9f95ce2869bc](../../evidence/conditions-sets-047.md#c-788e9f95ce2869bc) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007986

```text
(config-ldap-server)# no timeout retransmit <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 13 `；EOL ` RVA 0x356112F8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-74bf2e0f9efa0194](../../evidence/conditions-sets-045.md#c-74bf2e0f9efa0194) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007979

```text
(config-ldap-server)# no transport port <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 12 `；EOL ` RVA 0x3560F7E0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-cb036748ac2a7fac](../../evidence/conditions-sets-078.md#c-cb036748ac2a7fac) · [状态效果 S-c7008cafe60e17c3](../../evidence/state_effects-sets-042.md#s-c7008cafe60e17c3)

### observed_connections-007982

```text
(config-ldap-server)# search-filter user-object-type <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 17 `；EOL ` RVA 0x35610520 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Object Class attribute name。

[参数 P-0ccd38986214fcdb](../../evidence/parameters-sets-001.md#p-0ccd38986214fcdb)

### observed_connections-007972

```text
(config-ldap-server)# search-type nested <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 26 `；EOL ` RVA 0x35611610 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007976

```text
(config-ldap-server)# secure cipher rc4-128-md5 <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 7 `；EOL ` RVA 0x3560E5F0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ac317507ab7585e1](../../evidence/conditions-sets-067.md#c-ac317507ab7585e1) · [状态效果 S-a0ea7a3681c22469](../../evidence/state_effects-sets-034.md#s-a0ea7a3681c22469)

### observed_connections-007975

```text
(config-ldap-server)# secure trustpoint <string> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 6 `；EOL ` RVA 0x3560EA68 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Trustpoint name. Default: primary trustpoint。

[条件 C-097456262b551611](../../evidence/conditions-sets-004.md#c-097456262b551611) · [参数 P-5c7bb2f25740cf7b](../../evidence/parameters-sets-007.md#p-5c7bb2f25740cf7b)

### observed_connections-007985

```text
(config-ldap-server)# timeout retransmit <number:1..65535> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 13 `；EOL ` RVA 0x356112F8 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in secs。

[条件 C-cac1765a4069dce2](../../evidence/conditions-sets-078.md#c-cac1765a4069dce2) · [参数 P-1e6cf7f42bf5d876](../../evidence/parameters-sets-003.md#p-1e6cf7f42bf5d876)

### observed_connections-007978

```text
(config-ldap-server)# transport port <number:1..65535> <cr>
```

Handler ` RVA 0x11ABE670 `；selector ` 12 `；EOL ` RVA 0x3560F7E0 `。

模式根 ` RVA 0x355E9A10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Port Number。

[条件 C-0a6418a509827bf5](../../evidence/conditions-sets-004.md#c-0a6418a509827bf5) · [参数 P-4c9cf543aa0087f1](../../evidence/parameters-sets-006.md#p-4c9cf543aa0087f1)

