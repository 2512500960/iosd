# eigrp_af_intf_submode · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007614

```text
(config-router-af-interface)# add-paths <number:1..4> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 61 `；EOL ` RVA 0x34689D60 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of add paths to be advertised。

[条件 C-0d4e105e1f233f7b](../../evidence/conditions-sets-005.md#c-0d4e105e1f233f7b) · [参数 P-ebed7c732a63e0ce](../../evidence/parameters-sets-018.md#p-ebed7c732a63e0ce)

### observed_connections-007628

```text
(config-router-af-interface)# authentication key-chain <string> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x34687B88 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name of key-chain。

[条件 C-9e4046b71c6e8915](../../evidence/conditions-sets-061.md#c-9e4046b71c6e8915) · [参数 P-f5fc4ac08c43f476](../../evidence/parameters-sets-018.md#p-f5fc4ac08c43f476)

### observed_connections-007633

```text
(config-router-af-interface)# authentication mode hmac-sha-256 <string> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x346875E0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Authentication key-string used to compute HMAC-SHA-256 hash (maximum 32 characters for clear text, 69 characters for AES encrypted and 66 characters for proprietary)。

[条件 C-970834a62348eb1f](../../evidence/conditions-sets-058.md#c-970834a62348eb1f) · [参数 P-613d723110cccb93](../../evidence/parameters-sets-008.md#p-613d723110cccb93) · [状态效果 S-095fc9d56b5ce123](../../evidence/state_effects-sets-002.md#s-095fc9d56b5ce123)

### observed_connections-007624

```text
(config-router-af-interface)# authentication mode md5 <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x34687468 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fdb4d1b5d30a56cb](../../evidence/conditions-sets-098.md#c-fdb4d1b5d30a56cb) · [状态效果 S-f7b88112fe755896](../../evidence/state_effects-sets-052.md#s-f7b88112fe755896)

### observed_connections-007594

```text
(config-router-af-interface)# bandwidth-percent <number:1..999999> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x34688238 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum bandwidth percentage that EIGRP may use。

[条件 C-51d95e7bcd3c41da](../../evidence/conditions-sets-032.md#c-51d95e7bcd3c41da) · [参数 P-16c5ec63b8ca2af4](../../evidence/parameters-sets-002.md#p-16c5ec63b8ca2af4)

### observed_connections-007582

```text
(config-router-af-interface)# bfd <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x34688568 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6c53bdb75fda365](../../evidence/conditions-sets-071.md#c-b6c53bdb75fda365)

### observed_connections-007583

```text
(config-router-af-interface)# dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x346888F0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d296a613ae2acc1e](../../evidence/conditions-sets-081.md#c-d296a613ae2acc1e) · [状态效果 S-a3391fe53c63087d](../../evidence/state_effects-sets-035.md#s-a3391fe53c63087d)

### observed_connections-007584

```text
(config-router-af-interface)# dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x34688C78 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-89ba94e51c91dff6](../../evidence/conditions-sets-053.md#c-89ba94e51c91dff6) · [状态效果 S-b852b964bb22ae4a](../../evidence/state_effects-sets-039.md#s-b852b964bb22ae4a)

### observed_connections-007617

```text
(config-router-af-interface)# default add-paths <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 61 `；EOL ` RVA 0x34689D60 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-dde8214192e92599](../../evidence/conditions-sets-085.md#c-dde8214192e92599) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007629

```text
(config-router-af-interface)# default authentication key-chain <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x34687B88 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ebe0fb42d51e9c8b](../../evidence/conditions-sets-091.md#c-ebe0fb42d51e9c8b) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007626

```text
(config-router-af-interface)# default authentication mode <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x34687468 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-64f3503dddccde2d](../../evidence/conditions-sets-039.md#c-64f3503dddccde2d) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007596

```text
(config-router-af-interface)# default bandwidth-percent <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x34688238 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-db87956dde2b4ec6](../../evidence/conditions-sets-084.md#c-db87956dde2b4ec6) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007597

```text
(config-router-af-interface)# default bfd <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x34688568 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b6c53bdb75fda365](../../evidence/conditions-sets-071.md#c-b6c53bdb75fda365) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007600

```text
(config-router-af-interface)# default dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x346888F0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-9e7e684b71a3778b](../../evidence/conditions-sets-061.md#c-9e7e684b71a3778b) · [状态效果 S-6fd79b5ce75dbc99](../../evidence/state_effects-sets-024.md#s-6fd79b5ce75dbc99)

### observed_connections-007604

```text
(config-router-af-interface)# default dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x34688C78 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-2bcdaf0fd33b9797](../../evidence/conditions-sets-017.md#c-2bcdaf0fd33b9797) · [状态效果 S-a5f2769490fb82fd](../../evidence/state_effects-sets-035.md#s-a5f2769490fb82fd)

### observed_connections-007606

```text
(config-router-af-interface)# default hello-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x34689328 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7f8c44cc747fe19b](../../evidence/conditions-sets-049.md#c-7f8c44cc747fe19b) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007609

```text
(config-router-af-interface)# default hold-time <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x34689678 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-00bc13a56e2b323f](../../evidence/conditions-sets-001.md#c-00bc13a56e2b323f) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007612

```text
(config-router-af-interface)# default next-hop-self <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 60 `；EOL ` RVA 0x346899A0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007615

```text
(config-router-af-interface)# default passive-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 62 `；EOL ` RVA 0x3468A050 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007618

```text
(config-router-af-interface)# default shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x3468A330 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007620

```text
(config-router-af-interface)# default split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x3468A610 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007632

```text
(config-router-af-interface)# default stub-site wan-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 66 `；EOL ` RVA 0x3468A948 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-88b4e5b6466aac60](../../evidence/conditions-sets-053.md#c-88b4e5b6466aac60) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007635

```text
(config-router-af-interface)# default summary-address <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x346C4F70 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` address ` Summary network address；` address ` Summary network mask。

[条件 C-a5f9c52ba9606409](../../evidence/conditions-sets-064.md#c-a5f9c52ba9606409) · [参数 P-56aae2b2d488e2bd](../../evidence/parameters-sets-007.md#p-56aae2b2d488e2bd) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007592

```text
(config-router-af-interface)# default test-bandwidth <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x34687EE8 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-66e1f29c232288e3](../../evidence/conditions-sets-040.md#c-66e1f29c232288e3) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007602

```text
(config-router-af-interface)# default test-delay <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x34688FC8 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c4f565236529a6f4](../../evidence/conditions-sets-076.md#c-c4f565236529a6f4) · [状态效果 S-68d7dfb6ff79ea36](../../evidence/state_effects-sets-022.md#s-68d7dfb6ff79ea36)

### observed_connections-007625

```text
(config-router-af-interface)# default vnet global <cr>
```

Handler ` RVA 0xF583B80 `；selector ` 110 `；EOL ` RVA 0x3468BF08 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-126907ecd5094097](../../evidence/conditions-sets-007.md#c-126907ecd5094097) · [状态效果 S-c2a259381bfdd336](../../evidence/state_effects-sets-041.md#s-c2a259381bfdd336)

### observed_connections-007581

```text
(config-router-af-interface)# exit-af-interface <cr>
```

Handler ` RVA 0xF574160 `；selector ` 0 `；EOL ` RVA 0x3468AD58 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-deb76985da1c28ae](../../evidence/conditions-sets-086.md#c-deb76985da1c28ae)

### observed_connections-007605

```text
(config-router-af-interface)# hello-interval <number:1..65535> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x34689328 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds between hello transmissions。

[条件 C-73db5e57287f26a9](../../evidence/conditions-sets-045.md#c-73db5e57287f26a9) · [参数 P-2d1d4374d258d852](../../evidence/parameters-sets-004.md#p-2d1d4374d258d852)

### observed_connections-007608

```text
(config-router-af-interface)# hold-time <number:1..65535> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x34689678 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds before neighbor is considered down。

[条件 C-662f499fd270ecb0](../../evidence/conditions-sets-039.md#c-662f499fd270ecb0) · [参数 P-e906540d9909024e](../../evidence/parameters-sets-017.md#p-e906540d9909024e)

### observed_connections-007585

```text
(config-router-af-interface)# next-hop-self <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 60 `；EOL ` RVA 0x346899A0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007613

```text
(config-router-af-interface)# no add-paths <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 61 `；EOL ` RVA 0x34689D60 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-36c6876c72ed0786](../../evidence/conditions-sets-021.md#c-36c6876c72ed0786) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007627

```text
(config-router-af-interface)# no authentication key-chain <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 50 `；EOL ` RVA 0x34687B88 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-25ba0d6193bb4d83](../../evidence/conditions-sets-015.md#c-25ba0d6193bb4d83) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007623

```text
(config-router-af-interface)# no authentication mode <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 51 `；EOL ` RVA 0x34687468 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-a3758a53fb6023d0](../../evidence/conditions-sets-063.md#c-a3758a53fb6023d0) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007593

```text
(config-router-af-interface)# no bandwidth-percent <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 54 `；EOL ` RVA 0x34688238 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-63d25425ea8301d4](../../evidence/conditions-sets-039.md#c-63d25425ea8301d4) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007595

```text
(config-router-af-interface)# no bfd <cr>
```

Handler ` RVA 0xF57A660 `；selector ` 52 `；EOL ` RVA 0x34688568 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b6c53bdb75fda365](../../evidence/conditions-sets-071.md#c-b6c53bdb75fda365) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007598

```text
(config-router-af-interface)# no dampening-change <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 55 `；EOL ` RVA 0x346888F0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-35a87a8607b068d0](../../evidence/conditions-sets-021.md#c-35a87a8607b068d0) · [状态效果 S-38713837f2aaa328](../../evidence/state_effects-sets-012.md#s-38713837f2aaa328)

### observed_connections-007601

```text
(config-router-af-interface)# no dampening-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 56 `；EOL ` RVA 0x34688C78 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-443413283207c9ce](../../evidence/conditions-sets-027.md#c-443413283207c9ce) · [状态效果 S-6c5118ed8e94176f](../../evidence/state_effects-sets-023.md#s-6c5118ed8e94176f)

### observed_connections-007603

```text
(config-router-af-interface)# no hello-interval <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 58 `；EOL ` RVA 0x34689328 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-53039194281b27c5](../../evidence/conditions-sets-032.md#c-53039194281b27c5) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007607

```text
(config-router-af-interface)# no hold-time <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 59 `；EOL ` RVA 0x34689678 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-87618cf1d42b9417](../../evidence/conditions-sets-052.md#c-87618cf1d42b9417) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007610

```text
(config-router-af-interface)# no next-hop-self <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 60 `；EOL ` RVA 0x346899A0 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007611

```text
(config-router-af-interface)# no passive-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 62 `；EOL ` RVA 0x3468A050 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007616

```text
(config-router-af-interface)# no shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x3468A330 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007619

```text
(config-router-af-interface)# no split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x3468A610 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007631

```text
(config-router-af-interface)# no stub-site wan-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 66 `；EOL ` RVA 0x3468A948 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-88b4e5b6466aac60](../../evidence/conditions-sets-053.md#c-88b4e5b6466aac60) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007634

```text
(config-router-af-interface)# no summary-address <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x346C4F70 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` address ` Summary network address；` address ` Summary network mask。

[条件 C-a5f9c52ba9606409](../../evidence/conditions-sets-064.md#c-a5f9c52ba9606409) · [参数 P-56aae2b2d488e2bd](../../evidence/parameters-sets-007.md#p-56aae2b2d488e2bd) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007590

```text
(config-router-af-interface)# no test-bandwidth <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x34687EE8 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c9177574c107dbe2](../../evidence/conditions-sets-077.md#c-c9177574c107dbe2) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007599

```text
(config-router-af-interface)# no test-delay <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x34688FC8 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-606f0080bfdf3397](../../evidence/conditions-sets-037.md#c-606f0080bfdf3397) · [状态效果 S-5ca7f574d389a57d](../../evidence/state_effects-sets-020.md#s-5ca7f574d389a57d)

### observed_connections-007622

```text
(config-router-af-interface)# no vnet global <cr>
```

Handler ` RVA 0xF583B80 `；selector ` 110 `；EOL ` RVA 0x3468BF08 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-126907ecd5094097](../../evidence/conditions-sets-007.md#c-126907ecd5094097) · [状态效果 S-31d2bbcf8879ad80](../../evidence/state_effects-sets-011.md#s-31d2bbcf8879ad80)

### observed_connections-007586

```text
(config-router-af-interface)# passive-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 62 `；EOL ` RVA 0x3468A050 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007587

```text
(config-router-af-interface)# shutdown <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 63 `；EOL ` RVA 0x3468A330 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007588

```text
(config-router-af-interface)# split-horizon <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 64 `；EOL ` RVA 0x3468A610 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007621

```text
(config-router-af-interface)# stub-site wan-interface <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 66 `；EOL ` RVA 0x3468A948 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-88b4e5b6466aac60](../../evidence/conditions-sets-053.md#c-88b4e5b6466aac60)

### observed_connections-007630

```text
(config-router-af-interface)# summary-address <address> <address> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x346C4F70 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Summary network address；` address ` Summary network mask。

[条件 C-a5f9c52ba9606409](../../evidence/conditions-sets-064.md#c-a5f9c52ba9606409) · [参数 P-56aae2b2d488e2bd](../../evidence/parameters-sets-007.md#p-56aae2b2d488e2bd)

### observed_connections-007636

```text
(config-router-af-interface)# summary-address <prefix:dynamic> <cr>
```

Handler ` RVA 0x112E5010 `；selector ` 65 `；EOL ` RVA 0x35460920 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary network prefix。

[条件 C-d0c72fbb596b0f2b](../../evidence/conditions-sets-080.md#c-d0c72fbb596b0f2b) · [缺口 G-3af3a2405911366a](../../evidence/gaps-sets-003.md#g-3af3a2405911366a) · [参数 P-6a50b01d089d1719](../../evidence/parameters-sets-008.md#p-6a50b01d089d1719)

### observed_connections-007638

```text
(config-router-af-interface)# summary-address <prefix:dynamic> <cr>
```

Handler ` RVA 0xF5E07B0 `；selector ` 65 `；EOL ` RVA 0x346C4F70 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Summary &lt;network&gt;/&lt;length&gt;, e.g. 192.168.0.0/16。

[条件 C-cdc8282b8e571c12](../../evidence/conditions-sets-079.md#c-cdc8282b8e571c12) · [缺口 G-7d4a820352deacd3](../../evidence/gaps-sets-005.md#g-7d4a820352deacd3) · [参数 P-31e3bab49483c8d8](../../evidence/parameters-sets-004.md#p-31e3bab49483c8d8) · [状态效果 S-53ef8b45408b4747](../../evidence/state_effects-sets-018.md#s-53ef8b45408b4747)

### observed_connections-007591

```text
(config-router-af-interface)# test-bandwidth <number:1..4294967295> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 53 `；EOL ` RVA 0x34687EE8 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` &lt;1-4294967295&gt; bandwidth in kilobits per second。

[条件 C-ce94e11e15186ee7](../../evidence/conditions-sets-080.md#c-ce94e11e15186ee7) · [参数 P-c2c2b76692921998](../../evidence/parameters-sets-015.md#p-c2c2b76692921998)

### observed_connections-007637

```text
(config-router-af-interface)# test-delay <?general_to_number_action@555589bdcfa0> <cr>
```

Handler ` RVA 0xF586DE0 `；selector ` 57 `；EOL ` RVA 0x34688FC8 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ee812e3b5fbb2b34](../../evidence/conditions-sets-092.md#c-ee812e3b5fbb2b34) · [缺口 G-af86a3cbd04537bb](../../evidence/gaps-sets-006.md#g-af86a3cbd04537bb)

### observed_connections-007589

```text
(config-router-af-interface)# vnet global <cr>
```

Handler ` RVA 0xF583B80 `；selector ` 110 `；EOL ` RVA 0x3468BF08 `。

模式根 ` RVA 0x34686E48 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-126907ecd5094097](../../evidence/conditions-sets-007.md#c-126907ecd5094097) · [状态效果 S-5497eff058f31f76](../../evidence/state_effects-sets-018.md#s-5497eff058f31f76)
