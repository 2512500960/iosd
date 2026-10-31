# mode-0007 · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008000

```text
(config-bs-profile)# data-group <string> <cr>
```

Handler ` RVA 0xBC6A0A0 `；selector ` 0 `；EOL ` RVA 0x33884ED0 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` data-group name。

[条件 C-69eb6aaae6d1c98a](../../evidence/conditions-sets-041.md#c-69eb6aaae6d1c98a) · [参数 P-7cf49fd83f483633](../../evidence/parameters-sets-010.md#p-7cf49fd83f483633)

### observed_connections-008009

```text
(config-bs-profile)# data-group <string> polling interval <number:1..120000> <cr>
```

Handler ` RVA 0xBC6A0A0 `；selector ` 0 `；EOL ` RVA 0x33884EA8 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` data-group name；` unsigned_number ` Interval value in seconds。

[条件 C-d1c502d4d0a3cb3c](../../evidence/conditions-sets-081.md#c-d1c502d4d0a3cb3c) · [参数 P-4609986367c72a3e](../../evidence/parameters-sets-006.md#p-4609986367c72a3e)

### observed_connections-008010

```text
(config-bs-profile)# default data-group <string> <cr>
```

Handler ` RVA 0xBC6A0A0 `；selector ` 0 `；EOL ` RVA 0x33884ED0 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` data-group name。

[条件 C-69eb6aaae6d1c98a](../../evidence/conditions-sets-041.md#c-69eb6aaae6d1c98a) · [参数 P-7cf49fd83f483633](../../evidence/parameters-sets-010.md#p-7cf49fd83f483633) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008026

```text
(config-bs-profile)# default data-group <string> polling interval <cr>
```

Handler ` RVA 0xBC6A0A0 `；selector ` 0 `；EOL ` RVA 0x33884EA8 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` data-group name。

[条件 C-73363edc80ca51a0](../../evidence/conditions-sets-045.md#c-73363edc80ca51a0) · [参数 P-7cf49fd83f483633](../../evidence/parameters-sets-010.md#p-7cf49fd83f483633) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008001

```text
(config-bs-profile)# default enable <cr>
```

Handler ` RVA 0xBC69D10 `；selector ` 0 `；EOL ` RVA 0x33885490 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ea69a1666be998cb](../../evidence/conditions-sets-091.md#c-ea69a1666be998cb) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008002

```text
(config-bs-profile)# default exit <cr>
```

Handler ` RVA 0xBC6A910 `；selector ` 0 `；EOL ` RVA 0x33885770 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c3e938249e20310b](../../evidence/conditions-sets-076.md#c-c3e938249e20310b) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008028

```text
(config-bs-profile)# default file format schemaAscii <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 7 `；EOL ` RVA 0x33899320 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6b37f90c1d0c5e9a](../../evidence/conditions-sets-041.md#c-6b37f90c1d0c5e9a) · [状态效果 S-69df4f6ebdda07e1](../../evidence/state_effects-sets-023.md#s-69df4f6ebdda07e1)

### observed_connections-008016

```text
(config-bs-profile)# default file name-prefix <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 9 `；EOL ` RVA 0x33899000 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-eaed3fa6de2afc04](../../evidence/conditions-sets-091.md#c-eaed3fa6de2afc04) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008020

```text
(config-bs-profile)# default file retain <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 6 `；EOL ` RVA 0x33899680 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-cfd1249bf6d6b97a](../../evidence/conditions-sets-080.md#c-cfd1249bf6d6b97a) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-007997

```text
(config-bs-profile)# default file size <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 8 `；EOL ` RVA 0x33898C58 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-d99f7e0fc71b0b99](../../evidence/conditions-sets-084.md#c-d99f7e0fc71b0b99) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008022

```text
(config-bs-profile)# default file transfer retry <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 0 `；EOL ` RVA 0x3389A680 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-e134d079540f3ff1](../../evidence/conditions-sets-087.md#c-e134d079540f3ff1) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008030

```text
(config-bs-profile)# default file transfer source-interface <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 10 `；EOL ` RVA 0x3389A720 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-a137c745c4adbbcb](../../evidence/conditions-sets-062.md#c-a137c745c4adbbcb) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008032

```text
(config-bs-profile)# default file transfer url primary <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 1 `；EOL ` RVA 0x3389A070 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-94571769b854d6e8](../../evidence/conditions-sets-057.md#c-94571769b854d6e8) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008034

```text
(config-bs-profile)# default file transfer url secondary <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 2 `；EOL ` RVA 0x3389A3A8 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5e92abcda35c827b](../../evidence/conditions-sets-037.md#c-5e92abcda35c827b) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008025

```text
(config-bs-profile)# default flow exporter <string> <cr>
```

Handler ` RVA 0xBC101A0 `；selector ` 0 `；EOL ` RVA 0x3387C960 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` string ` the FNF exporter name。

[参数 P-f5d763af3c2197b0](../../evidence/parameters-sets-018.md#p-f5d763af3c2197b0) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008019

```text
(config-bs-profile)# default interval transfer process <cr>
```

Handler ` RVA 0xBC887B0 `；selector ` 0 `；EOL ` RVA 0x33893F68 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-b4b8bda6d0b7beb6](../../evidence/conditions-sets-070.md#c-b4b8bda6d0b7beb6) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-008015

```text
(config-bs-profile)# default interval transfer raw <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 3 `；EOL ` RVA 0x3389AD48 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-498422eb66919bc1](../../evidence/conditions-sets-029.md#c-498422eb66919bc1) · [状态效果 S-141aa8b6197f59bc](../../evidence/state_effects-sets-005.md#s-141aa8b6197f59bc)

### observed_connections-007994

```text
(config-bs-profile)# enable <cr>
```

Handler ` RVA 0xBC69D10 `；selector ` 0 `；EOL ` RVA 0x33885490 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ea69a1666be998cb](../../evidence/conditions-sets-091.md#c-ea69a1666be998cb)

### observed_connections-007995

```text
(config-bs-profile)# exit <cr>
```

Handler ` RVA 0xBC6A910 `；selector ` 0 `；EOL ` RVA 0x33885770 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c3e938249e20310b](../../evidence/conditions-sets-076.md#c-c3e938249e20310b)

### observed_connections-008013

```text
(config-bs-profile)# file format schemaAscii <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 7 `；EOL ` RVA 0x33899320 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b37f90c1d0c5e9a](../../evidence/conditions-sets-041.md#c-6b37f90c1d0c5e9a) · [状态效果 S-48ded0f6f1584c6a](../../evidence/state_effects-sets-016.md#s-48ded0f6f1584c6a)

### observed_connections-008014

```text
(config-bs-profile)# file name-prefix <string> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 9 `；EOL ` RVA 0x33899000 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` prefix name to be used instead of hostname。

[条件 C-dbf565a3dbf06192](../../evidence/conditions-sets-085.md#c-dbf565a3dbf06192) · [参数 P-1c11fc1449b95409](../../evidence/parameters-sets-003.md#p-1c11fc1449b95409)

### observed_connections-008038

```text
(config-bs-profile)# file retain disk <url:dynamic> <number:0..86400> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 4 `；EOL ` RVA 0x33899A20 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Time in seconds to retain the file in the specified location。

[条件 C-ae0b5261f92ebb04](../../evidence/conditions-sets-067.md#c-ae0b5261f92ebb04) · [缺口 G-0cc4f7a4e3669c9b](../../evidence/gaps-sets-001.md#g-0cc4f7a4e3669c9b) · [参数 P-75aea26bb5d4efdb](../../evidence/parameters-sets-009.md#p-75aea26bb5d4efdb)

### observed_connections-008005

```text
(config-bs-profile)# file retain memory <number:0..1200000> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 5 `；EOL ` RVA 0x33899658 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` time in seconds to retain。

[条件 C-2e8e05e4c3b98d7d](../../evidence/conditions-sets-018.md#c-2e8e05e4c3b98d7d) · [参数 P-fd3267b674f48aef](../../evidence/parameters-sets-019.md#p-fd3267b674f48aef)

### observed_connections-007993

```text
(config-bs-profile)# file size <number:1024..2147483647> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 8 `；EOL ` RVA 0x33898C58 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` size in bytes。

[条件 C-55b4ad413b79c2f2](../../evidence/conditions-sets-034.md#c-55b4ad413b79c2f2) · [参数 P-970acbce35584eec](../../evidence/parameters-sets-012.md#p-970acbce35584eec)

### observed_connections-008006

```text
(config-bs-profile)# file transfer retry <number:0..100> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 0 `；EOL ` RVA 0x3389A680 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of retries。

[条件 C-ac9dd462573ef8d8](../../evidence/conditions-sets-067.md#c-ac9dd462573ef8d8) · [参数 P-6fd3e5872d935cfa](../../evidence/parameters-sets-009.md#p-6fd3e5872d935cfa)

### observed_connections-008035

```text
(config-bs-profile)# file transfer source-interface <interface> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 10 `；EOL ` RVA 0x3389A720 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-34bbbeff21caa41e](../../evidence/conditions-sets-020.md#c-34bbbeff21caa41e) · [缺口 G-c4754c6b03b1393c](../../evidence/gaps-sets-007.md#g-c4754c6b03b1393c) · [参数 P-0716900ed0d45bdc](../../evidence/parameters-sets-001.md#p-0716900ed0d45bdc)

### observed_connections-008036

```text
(config-bs-profile)# file transfer url primary <url:dynamic> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 1 `；EOL ` RVA 0x3389A070 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7b1c794c9d436ef9](../../evidence/conditions-sets-048.md#c-7b1c794c9d436ef9) · [缺口 G-881c5a64ff901dbb](../../evidence/gaps-sets-005.md#g-881c5a64ff901dbb) · [参数 P-1efd0ee80db7f3b3](../../evidence/parameters-sets-003.md#p-1efd0ee80db7f3b3)

### observed_connections-008037

```text
(config-bs-profile)# file transfer url secondary <url:dynamic> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 2 `；EOL ` RVA 0x3389A3A8 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9283b647005d7fd4](../../evidence/conditions-sets-057.md#c-9283b647005d7fd4) · [缺口 G-94718890375e8809](../../evidence/gaps-sets-005.md#g-94718890375e8809) · [参数 P-3aab571ebeabb821](../../evidence/parameters-sets-005.md#p-3aab571ebeabb821)

### observed_connections-008008

```text
(config-bs-profile)# flow exporter <string> <cr>
```

Handler ` RVA 0xBC101A0 `；selector ` 0 `；EOL ` RVA 0x3387C960 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` the FNF exporter name。

[参数 P-f5d763af3c2197b0](../../evidence/parameters-sets-018.md#p-f5d763af3c2197b0)

### observed_connections-008004

```text
(config-bs-profile)# interval transfer process <number:1800..604800> <cr>
```

Handler ` RVA 0xBC887B0 `；selector ` 0 `；EOL ` RVA 0x33893F68 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Duration in seconds。

[条件 C-b39a3dd0fdfee6fd](../../evidence/conditions-sets-069.md#c-b39a3dd0fdfee6fd) · [参数 P-ae0f0eb4d610525e](../../evidence/parameters-sets-013.md#p-ae0f0eb4d610525e)

### observed_connections-008003

```text
(config-bs-profile)# interval transfer raw <number:60..4294967> <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 3 `；EOL ` RVA 0x3389AD48 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Duration in seconds。

[条件 C-ebee085a41fbe8d8](../../evidence/conditions-sets-091.md#c-ebee085a41fbe8d8) · [参数 P-0b2c720b6912ef1f](../../evidence/parameters-sets-001.md#p-0b2c720b6912ef1f)

### observed_connections-008007

```text
(config-bs-profile)# no data-group <string> <cr>
```

Handler ` RVA 0xBC6A0A0 `；selector ` 0 `；EOL ` RVA 0x33884ED0 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` data-group name。

[条件 C-69eb6aaae6d1c98a](../../evidence/conditions-sets-041.md#c-69eb6aaae6d1c98a) · [参数 P-7cf49fd83f483633](../../evidence/parameters-sets-010.md#p-7cf49fd83f483633) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008024

```text
(config-bs-profile)# no data-group <string> polling interval <cr>
```

Handler ` RVA 0xBC6A0A0 `；selector ` 0 `；EOL ` RVA 0x33884EA8 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` data-group name。

[条件 C-73363edc80ca51a0](../../evidence/conditions-sets-045.md#c-73363edc80ca51a0) · [参数 P-7cf49fd83f483633](../../evidence/parameters-sets-010.md#p-7cf49fd83f483633) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-007998

```text
(config-bs-profile)# no enable <cr>
```

Handler ` RVA 0xBC69D10 `；selector ` 0 `；EOL ` RVA 0x33885490 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ea69a1666be998cb](../../evidence/conditions-sets-091.md#c-ea69a1666be998cb) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-007999

```text
(config-bs-profile)# no exit <cr>
```

Handler ` RVA 0xBC6A910 `；selector ` 0 `；EOL ` RVA 0x33885770 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-c3e938249e20310b](../../evidence/conditions-sets-076.md#c-c3e938249e20310b) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008027

```text
(config-bs-profile)# no file format schemaAscii <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 7 `；EOL ` RVA 0x33899320 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6b37f90c1d0c5e9a](../../evidence/conditions-sets-041.md#c-6b37f90c1d0c5e9a) · [状态效果 S-ce4ea119897009a0](../../evidence/state_effects-sets-044.md#s-ce4ea119897009a0)

### observed_connections-008012

```text
(config-bs-profile)# no file name-prefix <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 9 `；EOL ` RVA 0x33899000 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-402397e93751d240](../../evidence/conditions-sets-025.md#c-402397e93751d240) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008018

```text
(config-bs-profile)# no file retain <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 6 `；EOL ` RVA 0x33899680 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6246b4d88a73e454](../../evidence/conditions-sets-038.md#c-6246b4d88a73e454) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-007996

```text
(config-bs-profile)# no file size <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 8 `；EOL ` RVA 0x33898C58 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d99f7e0fc71b0b99](../../evidence/conditions-sets-084.md#c-d99f7e0fc71b0b99) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008021

```text
(config-bs-profile)# no file transfer retry <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 0 `；EOL ` RVA 0x3389A680 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-e134d079540f3ff1](../../evidence/conditions-sets-087.md#c-e134d079540f3ff1) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008029

```text
(config-bs-profile)# no file transfer source-interface <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 10 `；EOL ` RVA 0x3389A720 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d4186923b4a27b6e](../../evidence/conditions-sets-082.md#c-d4186923b4a27b6e) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008031

```text
(config-bs-profile)# no file transfer url primary <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 1 `；EOL ` RVA 0x3389A070 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-3a595fa49ef64188](../../evidence/conditions-sets-023.md#c-3a595fa49ef64188) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008033

```text
(config-bs-profile)# no file transfer url secondary <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 2 `；EOL ` RVA 0x3389A3A8 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-8f4875ed650ea315](../../evidence/conditions-sets-055.md#c-8f4875ed650ea315) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008023

```text
(config-bs-profile)# no flow exporter <string> <cr>
```

Handler ` RVA 0xBC101A0 `；selector ` 0 `；EOL ` RVA 0x3387C960 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` string ` the FNF exporter name。

[参数 P-f5d763af3c2197b0](../../evidence/parameters-sets-018.md#p-f5d763af3c2197b0) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008017

```text
(config-bs-profile)# no interval transfer process <cr>
```

Handler ` RVA 0xBC887B0 `；selector ` 0 `；EOL ` RVA 0x33893F68 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-b4b8bda6d0b7beb6](../../evidence/conditions-sets-070.md#c-b4b8bda6d0b7beb6) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)

### observed_connections-008011

```text
(config-bs-profile)# no interval transfer raw <cr>
```

Handler ` RVA 0xBC94490 `；selector ` 3 `；EOL ` RVA 0x3389AD48 `。

模式根 ` RVA 0x3387FBB8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-498422eb66919bc1](../../evidence/conditions-sets-029.md#c-498422eb66919bc1) · [状态效果 S-02978184403c6ccd](../../evidence/state_effects-sets-001.md#s-02978184403c6ccd)
