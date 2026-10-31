# exec · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-019822

```text
(exec)# show bgp * template peer-policy <cr>
```

Handler ` RVA 0xF175000 `；selector ` 0 `；EOL ` RVA 0x344C1B88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54e28e33a72bbe00](../../evidence/conditions-sets-033.md#c-54e28e33a72bbe00) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-c9fb43fa5f61cb12](../../evidence/state_effects-sets-043.md#s-c9fb43fa5f61cb12)

### path-019834

```text
(exec)# show bgp * template peer-session <cr>
```

Handler ` RVA 0xF176160 `；selector ` 0 `；EOL ` RVA 0x344C1F00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-54e28e33a72bbe00](../../evidence/conditions-sets-033.md#c-54e28e33a72bbe00) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-c9fb43fa5f61cb12](../../evidence/state_effects-sets-043.md#s-c9fb43fa5f61cb12)

### path-015231

```text
(exec)# show bgp * update-sources <cr>
```

Handler ` RVA 0xF1D0DF0 `；selector ` 0 `；EOL ` RVA 0x344BD328 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e6c73e6f656b5b4a](../../evidence/conditions-sets-089.md#c-e6c73e6f656b5b4a) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-c9fb43fa5f61cb12](../../evidence/state_effects-sets-043.md#s-c9fb43fa5f61cb12)

### path-015394

```text
(exec)# show bgp * va <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 40 `；EOL ` RVA 0x344C4DD0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ef0ef893681b44c3](../../evidence/conditions-sets-092.md#c-ef0ef893681b44c3) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [状态效果 S-c9fb43fa5f61cb12](../../evidence/state_effects-sets-043.md#s-c9fb43fa5f61cb12)

### path-024368

```text
(exec)# show bgp * ve-id <number:1..65535> block-offset <number:1..65535> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 1 `；EOL ` RVA 0x344CA560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Target VE ID value；` unsigned_number ` Target Block Offset value。

[条件 C-4383efea32434a69](../../evidence/conditions-sets-026.md#c-4383efea32434a69) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-93dc4687e8d08585](../../evidence/parameters-sets-011.md#p-93dc4687e8d08585) · [状态效果 S-cc6d4d3dbee49b1f](../../evidence/state_effects-sets-043.md#s-cc6d4d3dbee49b1f)

### path-019664

```text
(exec)# show bgp * version <number:1..4294967295> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 25 `；EOL ` RVA 0x344BF010 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Version number and above。

[条件 C-4d7032750a0b2481](../../evidence/conditions-sets-030.md#c-4d7032750a0b2481) · [缺口 G-def948e72b71ee7f](../../evidence/gaps-sets-008.md#g-def948e72b71ee7f) · [参数 P-49fbd35dbe8acc86](../../evidence/parameters-sets-006.md#p-49fbd35dbe8acc86) · [状态效果 S-c9fb43fa5f61cb12](../../evidence/state_effects-sets-043.md#s-c9fb43fa5f61cb12)

### path-010050

```text
(exec)# show bgp <address> <address> longer-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 5 `；EOL ` RVA 0x344C3548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network in the BGP routing table to display；` address ` Network mask。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [参数 P-54d2e655ff68d058](../../evidence/parameters-sets-007.md#p-54d2e655ff68d058) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-010059

```text
(exec)# show bgp <address> <address> shorter-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 18 `；EOL ` RVA 0x344C3850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network in the BGP routing table to display；` address ` Network mask。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [参数 P-54d2e655ff68d058](../../evidence/parameters-sets-007.md#p-54d2e655ff68d058) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002874

```text
(exec)# show bgp <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344C6070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Display route-type 2 with specified MAC Address (H.H.H or HH:HH:HH:HH:HH:HH)。

[条件 C-41aa1c57823bb4b1](../../evidence/conditions-sets-026.md#c-41aa1c57823bb4b1) · [参数 P-176896aa62ac74b6](../../evidence/parameters-sets-002.md#p-176896aa62ac74b6) · [状态效果 S-a98d0a6cd106a5b3](../../evidence/state_effects-sets-036.md#s-a98d0a6cd106a5b3)

### path-003331

```text
(exec)# show bgp <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 1 `；EOL ` RVA 0x344C3B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network in the BGP routing table to display。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [参数 P-3d2613e00c71652f](../../evidence/parameters-sets-005.md#p-3d2613e00c71652f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-010078

```text
(exec)# show bgp <address> internal pathext <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 43 `；EOL ` RVA 0x344C3F78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Network in the BGP routing table to display。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [参数 P-3d2613e00c71652f](../../evidence/parameters-sets-005.md#p-3d2613e00c71652f) · [状态效果 S-8798817900de5937](../../evidence/state_effects-sets-029.md#s-8798817900de5937)

### path-000357

```text
(exec)# show bgp <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 0 `；EOL ` RVA 0x344CA860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-03829068a935619f](../../evidence/conditions-sets-002.md#c-03829068a935619f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-000387

```text
(exec)# show bgp <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 13 `；EOL ` RVA 0x34500CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8c0ac19296d57501](../../evidence/conditions-sets-054.md#c-8c0ac19296d57501) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-012648

```text
(exec)# show bgp <prefix:dynamic> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344C6070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Display route-type 2 and 5 routes matching the IP prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-775aaa4af7c58060](../../evidence/conditions-sets-046.md#c-775aaa4af7c58060) · [缺口 G-dcb0e908d13d388d](../../evidence/gaps-sets-008.md#g-dcb0e908d13d388d) · [参数 P-45726d47cb0cf086](../../evidence/parameters-sets-006.md#p-45726d47cb0cf086) · [状态效果 S-98cc5dbb1a06c5bc](../../evidence/state_effects-sets-032.md#s-98cc5dbb1a06c5bc)

### path-012686

```text
(exec)# show bgp <prefix:dynamic> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 1 `；EOL ` RVA 0x3552EBE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-5e1dee0ad0c3c094](../../evidence/conditions-sets-037.md#c-5e1dee0ad0c3c094) · [缺口 G-d3ace05660445e76](../../evidence/gaps-sets-007.md#g-d3ace05660445e76) · [参数 P-1a8383753b78ff02](../../evidence/parameters-sets-002.md#p-1a8383753b78ff02) · [状态效果 S-330adf5789d47f76](../../evidence/state_effects-sets-011.md#s-330adf5789d47f76)

### path-012696

```text
(exec)# show bgp <prefix:dynamic> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 1 `；EOL ` RVA 0x344C3B80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-5716185190993da9](../../evidence/conditions-sets-034.md#c-5716185190993da9) · [缺口 G-9cf11f4dc16e66f0](../../evidence/gaps-sets-006.md#g-9cf11f4dc16e66f0) · [参数 P-bebb1e59b459fbf8](../../evidence/parameters-sets-014.md#p-bebb1e59b459fbf8) · [状态效果 S-9d4b50ea96dde9bc](../../evidence/state_effects-sets-033.md#s-9d4b50ea96dde9bc)

### path-019908

```text
(exec)# show bgp <prefix:dynamic> internal pathext <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 43 `；EOL ` RVA 0x3552EC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-7574b4e3706819a6](../../evidence/conditions-sets-046.md#c-7574b4e3706819a6) · [缺口 G-d3ace05660445e76](../../evidence/gaps-sets-007.md#g-d3ace05660445e76) · [参数 P-1a8383753b78ff02](../../evidence/parameters-sets-002.md#p-1a8383753b78ff02) · [状态效果 S-c42c7e103c1c4895](../../evidence/state_effects-sets-042.md#s-c42c7e103c1c4895)

### path-019958

```text
(exec)# show bgp <prefix:dynamic> internal pathext <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 43 `；EOL ` RVA 0x344C3F78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-5716185190993da9](../../evidence/conditions-sets-034.md#c-5716185190993da9) · [缺口 G-9cf11f4dc16e66f0](../../evidence/gaps-sets-006.md#g-9cf11f4dc16e66f0) · [参数 P-bebb1e59b459fbf8](../../evidence/parameters-sets-014.md#p-bebb1e59b459fbf8) · [状态效果 S-07b73ebb466e71dc](../../evidence/state_effects-sets-002.md#s-07b73ebb466e71dc)

### path-015676

```text
(exec)# show bgp <prefix:dynamic> longer-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 5 `；EOL ` RVA 0x3552E910 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix &lt;network&gt;/&lt;length&gt;。

[条件 C-5e1dee0ad0c3c094](../../evidence/conditions-sets-037.md#c-5e1dee0ad0c3c094) · [缺口 G-d3ace05660445e76](../../evidence/gaps-sets-007.md#g-d3ace05660445e76) · [参数 P-1a8383753b78ff02](../../evidence/parameters-sets-002.md#p-1a8383753b78ff02) · [状态效果 S-330adf5789d47f76](../../evidence/state_effects-sets-011.md#s-330adf5789d47f76)

### path-015701

```text
(exec)# show bgp <prefix:dynamic> longer-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 5 `；EOL ` RVA 0x344C3548 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-5716185190993da9](../../evidence/conditions-sets-034.md#c-5716185190993da9) · [缺口 G-9cf11f4dc16e66f0](../../evidence/gaps-sets-006.md#g-9cf11f4dc16e66f0) · [参数 P-bebb1e59b459fbf8](../../evidence/parameters-sets-014.md#p-bebb1e59b459fbf8) · [状态效果 S-9d4b50ea96dde9bc](../../evidence/state_effects-sets-033.md#s-9d4b50ea96dde9bc)

### path-015719

```text
(exec)# show bgp <prefix:dynamic> shorter-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 18 `；EOL ` RVA 0x344C3850 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-5716185190993da9](../../evidence/conditions-sets-034.md#c-5716185190993da9) · [缺口 G-9cf11f4dc16e66f0](../../evidence/gaps-sets-006.md#g-9cf11f4dc16e66f0) · [参数 P-bebb1e59b459fbf8](../../evidence/parameters-sets-014.md#p-bebb1e59b459fbf8) · [状态效果 S-9d4b50ea96dde9bc](../../evidence/state_effects-sets-033.md#s-9d4b50ea96dde9bc)

### path-011417

```text
(exec)# show bgp all route-type <number:1..7> <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344C8570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Multicast VPN NLRI route-type；` address ` Route-type 1 originator ID。

[条件 C-04d3cdf62bcab54b](../../evidence/conditions-sets-002.md#c-04d3cdf62bcab54b) · [参数 P-1b8a4dec5fa285d3](../../evidence/parameters-sets-003.md#p-1b8a4dec5fa285d3) · [状态效果 S-0137c76cf3126daa](../../evidence/state_effects-sets-001.md#s-0137c76cf3126daa)

### path-011422

```text
(exec)# show bgp all route-type <number:1..7> <address> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 41 `；EOL ` RVA 0x344CB0F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Multicast VPN NLRI route-type；` address ` Route-type 1 originator ID。

[条件 C-0035051f58d911bc](../../evidence/conditions-sets-001.md#c-0035051f58d911bc) · [参数 P-fe3de206dc5b3918](../../evidence/parameters-sets-019.md#p-fe3de206dc5b3918) · [状态效果 S-942c3c5c65c18bb3](../../evidence/state_effects-sets-031.md#s-942c3c5c65c18bb3)

### path-007071

```text
(exec)# show bgp aspath hash <cr>
```

Handler ` RVA 0xF1723F0 `；selector ` 0 `；EOL ` RVA 0x344BE710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cbb55ca8fd1e4105](../../evidence/conditions-sets-078.md#c-cbb55ca8fd1e4105) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007061

```text
(exec)# show bgp attr hash <cr>
```

Handler ` RVA 0xF1729B0 `；selector ` 0 `；EOL ` RVA 0x344BDC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-46b31c9ac896fa77](../../evidence/conditions-sets-028.md#c-46b31c9ac896fa77) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007072

```text
(exec)# show bgp attr nexthop <cr>
```

Handler ` RVA 0xF172000 `；selector ` 0 `；EOL ` RVA 0x344BDF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff0445977d1a7238](../../evidence/conditions-sets-098.md#c-ff0445977d1a7238) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002838

```text
(exec)# show bgp binding-sid <cr>
```

Handler ` RVA 0xF1CFDA0 `；selector ` 0 `；EOL ` RVA 0x344BC410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24f8273a2305d27b](../../evidence/conditions-sets-014.md#c-24f8273a2305d27b) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003212

```text
(exec)# show bgp cidr-only <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 4 `；EOL ` RVA 0x344C25B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7ca23763720e39a](../../evidence/conditions-sets-071.md#c-b7ca23763720e39a) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003103

```text
(exec)# show bgp cluster-ids <cr>
```

Handler ` RVA 0xF185F30 `；selector ` 39 `；EOL ` RVA 0x344C0470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007127

```text
(exec)# show bgp cluster-ids internal <cr>
```

Handler ` RVA 0xF185F30 `；selector ` 38 `；EOL ` RVA 0x344C0448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49b0d0887a2ba64a](../../evidence/conditions-sets-029.md#c-49b0d0887a2ba64a) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003375

```text
(exec)# show bgp community <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 7 `；EOL ` RVA 0x34501500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-40861732d55d8618](../../evidence/conditions-sets-025.md#c-40861732d55d8618) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007273

```text
(exec)# show bgp community-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 8 `；EOL ` RVA 0x34501A18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` community-list number。

[条件 C-af1c7988cbd21973](../../evidence/conditions-sets-068.md#c-af1c7988cbd21973) · [参数 P-a5a54df05ee65623](../../evidence/parameters-sets-013.md#p-a5a54df05ee65623) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003142

```text
(exec)# show bgp dampened-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 12 `；EOL ` RVA 0x344C1470 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aae36500acd2ffaf](../../evidence/conditions-sets-066.md#c-aae36500acd2ffaf) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007145

```text
(exec)# show bgp dampening parameters <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 14 `；EOL ` RVA 0x344C11C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [状态效果 S-52b533c53d96d5eb](../../evidence/state_effects-sets-018.md#s-52b533c53d96d5eb)

### path-002773

```text
(exec)# show bgp default <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 32 `；EOL ` RVA 0x344C5448 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-72cb34b32f940a85](../../evidence/conditions-sets-044.md#c-72cb34b32f940a85) · [状态效果 S-08cf592459df695d](../../evidence/state_effects-sets-002.md#s-08cf592459df695d)

### path-002839

```text
(exec)# show bgp detail <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 44 `；EOL ` RVA 0x344C8F50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3767fe3422e0a81d](../../evidence/conditions-sets-022.md#c-3767fe3422e0a81d) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-006957

```text
(exec)# show bgp detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 52 `；EOL ` RVA 0x344C8F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` L2VPN EVPN Route。

[条件 C-3767fe3422e0a81d](../../evidence/conditions-sets-022.md#c-3767fe3422e0a81d) · [参数 P-faf666212ecfdfb5](../../evidence/parameters-sets-019.md#p-faf666212ecfdfb5) · [状态效果 S-7a467c86140c7431](../../evidence/state_effects-sets-026.md#s-7a467c86140c7431)

### path-006971

```text
(exec)# show bgp detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 53 `；EOL ` RVA 0x344C94F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPv4 MVPN Route。

[条件 C-46e853d2be50886b](../../evidence/conditions-sets-028.md#c-46e853d2be50886b) · [参数 P-f14d7edbc095e8f7](../../evidence/parameters-sets-018.md#p-f14d7edbc095e8f7) · [状态效果 S-70721046bd242174](../../evidence/state_effects-sets-024.md#s-70721046bd242174)

### path-006986

```text
(exec)# show bgp detail <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 54 `；EOL ` RVA 0x344C9810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` IPv6 MVPN Route。

[条件 C-03507b64aa6952fd](../../evidence/conditions-sets-002.md#c-03507b64aa6952fd) · [参数 P-8e299cbbeb9d5d4c](../../evidence/parameters-sets-011.md#p-8e299cbbeb9d5d4c) · [状态效果 S-f9f096a158092686](../../evidence/state_effects-sets-053.md#s-f9f096a158092686)

### path-006867

```text
(exec)# show bgp evi context <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 47 `；EOL ` RVA 0x344C5C70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41aa1c57823bb4b1](../../evidence/conditions-sets-026.md#c-41aa1c57823bb4b1) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007300

```text
(exec)# show bgp extcommunity-list <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 11 `；EOL ` RVA 0x34502620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` extcommunity-list name。

[条件 C-a6332078d356a285](../../evidence/conditions-sets-064.md#c-a6332078d356a285) · [参数 P-16c46cd5a4132de6](../../evidence/parameters-sets-002.md#p-16c46cd5a4132de6) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007197

```text
(exec)# show bgp filter-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 2 `；EOL ` RVA 0x34500058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Regular expression access list number。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [参数 P-2d3e3d354ed0b984](../../evidence/parameters-sets-004.md#p-2d3e3d354ed0b984) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003243

```text
(exec)# show bgp import <cr>
```

Handler ` RVA 0xF171AC0 `；selector ` 0 `；EOL ` RVA 0x344C2260 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f83e23ddfdfda5bb](../../evidence/conditions-sets-096.md#c-f83e23ddfdfda5bb) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007207

```text
(exec)# show bgp inconsistency nexthop-label <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 20 `；EOL ` RVA 0x344C2908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-92c3cc1d4cb6f02f](../../evidence/conditions-sets-057.md#c-92c3cc1d4cb6f02f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007225

```text
(exec)# show bgp inconsistency nexthop-label <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 20 `；EOL ` RVA 0x3552E078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07871a927bf85ec8](../../evidence/conditions-sets-003.md#c-07871a927bf85ec8) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003270

```text
(exec)# show bgp inconsistent-as <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 6 `；EOL ` RVA 0x34500F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-af1c7988cbd21973](../../evidence/conditions-sets-068.md#c-af1c7988cbd21973) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003231

```text
(exec)# show bgp injected-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 17 `；EOL ` RVA 0x344C2BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c98ef1b5d799e490](../../evidence/conditions-sets-078.md#c-c98ef1b5d799e490) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003257

```text
(exec)# show bgp injected-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 17 `；EOL ` RVA 0x3552E308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-07871a927bf85ec8](../../evidence/conditions-sets-003.md#c-07871a927bf85ec8) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003148

```text
(exec)# show bgp internal <cr>
```

Handler ` RVA 0xF184450 `；selector ` 35 `；EOL ` RVA 0x344C0C78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-01d81c5ab91fabc9](../../evidence/conditions-sets-001.md#c-01d81c5ab91fabc9) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007150

```text
(exec)# show bgp internal stat <cr>
```

Handler ` RVA 0xF184450 `；selector ` 36 `；EOL ` RVA 0x344C0C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-053ec67876fa9053](../../evidence/conditions-sets-002.md#c-053ec67876fa9053) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007137

```text
(exec)# show bgp internal task <cr>
```

Handler ` RVA 0xF184450 `；selector ` 37 `；EOL ` RVA 0x344C09A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d42286db0fc82630](../../evidence/conditions-sets-082.md#c-d42286db0fc82630) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002868

```text
(exec)# show bgp labels <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 16 `；EOL ` RVA 0x344C9DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b8b93e038f5ebf9](../../evidence/conditions-sets-054.md#c-8b8b93e038f5ebf9) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002913

```text
(exec)# show bgp labels <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 16 `；EOL ` RVA 0x344CA838 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ee723b356c060cf](../../evidence/conditions-sets-012.md#c-1ee723b356c060cf) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003201

```text
(exec)# show bgp labels <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 16 `；EOL ` RVA 0x344C1810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f83e23ddfdfda5bb](../../evidence/conditions-sets-096.md#c-f83e23ddfdfda5bb) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-015728

```text
(exec)# show bgp large-community <?bgp_lrgcomm_action@555589a55d28> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 9 `；EOL ` RVA 0x34501EF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-af1c7988cbd21973](../../evidence/conditions-sets-068.md#c-af1c7988cbd21973) · [缺口 G-47793e3585bf3f7c](../../evidence/gaps-sets-003.md#g-47793e3585bf3f7c) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007292

```text
(exec)# show bgp largecommunity-list <number:1..500> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 10 `；EOL ` RVA 0x34502278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` community-list number。

[条件 C-af1c7988cbd21973](../../evidence/conditions-sets-068.md#c-af1c7988cbd21973) · [参数 P-73dcc5a2cab3ca61](../../evidence/parameters-sets-009.md#p-73dcc5a2cab3ca61) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002825

```text
(exec)# show bgp local-vtep <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 45 `；EOL ` RVA 0x344C7750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41aa1c57823bb4b1](../../evidence/conditions-sets-026.md#c-41aa1c57823bb4b1) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002585

```text
(exec)# show bgp memory <cr>
```

Handler ` RVA 0xF028050 `；selector ` 0 `；EOL ` RVA 0x344FA0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6ecc7e18221db618](../../evidence/conditions-sets-043.md#c-6ecc7e18221db618) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019740

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> advertised-routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 4 `；EOL ` RVA 0x34502FE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9c05b20c34834ddd](../../evidence/conditions-sets-060.md#c-9c05b20c34834ddd) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019764

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> dampened-routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 1 `；EOL ` RVA 0x34504030 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019749

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> flap-statistics <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 2 `；EOL ` RVA 0x34503D88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019787

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> paths <cr>
```

Handler ` RVA 0xF17ED40 `；selector ` 0 `；EOL ` RVA 0x34504340 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019798

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> policy <cr>
```

Handler ` RVA 0xF186320 `；selector ` 0 `；EOL ` RVA 0x34504600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-022811

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> received extcommunity-filter <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 7 `；EOL ` RVA 0x345037F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-022807

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> received prefix-filter <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 5 `；EOL ` RVA 0x34503550 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-022817

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> received rtfilters <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 6 `；EOL ` RVA 0x34503AE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9edae68eab8887dc](../../evidence/conditions-sets-061.md#c-9edae68eab8887dc) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019711

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> received-routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 3 `；EOL ` RVA 0x34502C28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019699

```text
(exec)# show bgp neighbors <?match_ipv6_addrinfo_action@55558aa83180> routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 0 `；EOL ` RVA 0x34502980 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [缺口 G-ea115753df5fd78f](../../evidence/gaps-sets-008.md#g-ea115753df5fd78f) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009978

```text
(exec)# show bgp neighbors <address> advertised-routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 4 `；EOL ` RVA 0x34502FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-9c05b20c34834ddd](../../evidence/conditions-sets-060.md#c-9c05b20c34834ddd) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-022800

```text
(exec)# show bgp neighbors <address> advertised-routes <prefix:dynamic> <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 8 `；EOL ` RVA 0x34502FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` Neighbor to display information about；` prefix_dynamic ` IP prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-6527c03ff138a903](../../evidence/conditions-sets-039.md#c-6527c03ff138a903) · [缺口 G-29348151589855ec](../../evidence/gaps-sets-002.md#g-29348151589855ec) · [参数 P-c25d8b462ce305e8](../../evidence/parameters-sets-015.md#p-c25d8b462ce305e8) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009984

```text
(exec)# show bgp neighbors <address> dampened-routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 1 `；EOL ` RVA 0x34504030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009980

```text
(exec)# show bgp neighbors <address> flap-statistics <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 2 `；EOL ` RVA 0x34503D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009993

```text
(exec)# show bgp neighbors <address> paths <cr>
```

Handler ` RVA 0xF17ED40 `；selector ` 0 `；EOL ` RVA 0x34504340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009996

```text
(exec)# show bgp neighbors <address> policy <cr>
```

Handler ` RVA 0xF186320 `；selector ` 0 `；EOL ` RVA 0x34504600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-011449

```text
(exec)# show bgp neighbors <address> received extcommunity-filter <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 7 `；EOL ` RVA 0x345037F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-011447

```text
(exec)# show bgp neighbors <address> received prefix-filter <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 5 `；EOL ` RVA 0x34503550 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-011451

```text
(exec)# show bgp neighbors <address> received rtfilters <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 6 `；EOL ` RVA 0x34503AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-9edae68eab8887dc](../../evidence/conditions-sets-061.md#c-9edae68eab8887dc) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009976

```text
(exec)# show bgp neighbors <address> received-routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 3 `；EOL ` RVA 0x34502C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009972

```text
(exec)# show bgp neighbors <address> routes <cr>
```

Handler ` RVA 0xF18F2A0 `；selector ` 0 `；EOL ` RVA 0x34502980 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Neighbor to display information about。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [参数 P-8327aa3c2c0313a2](../../evidence/parameters-sets-010.md#p-8327aa3c2c0313a2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003035

```text
(exec)# show bgp neighbors <cr>
```

Handler ` RVA 0xF18D040 `；selector ` 0 `；EOL ` RVA 0x344BEA20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d56d58befe4a210](../../evidence/conditions-sets-024.md#c-3d56d58befe4a210) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002852

```text
(exec)# show bgp nexthops <cr>
```

Handler ` RVA 0xF1D0550 `；selector ` 0 `；EOL ` RVA 0x344BCD98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c39b803c84eac0fe](../../evidence/conditions-sets-076.md#c-c39b803c84eac0fe) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003241

```text
(exec)# show bgp oer-paths <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 26 `；EOL ` RVA 0x344C3168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002872

```text
(exec)# show bgp overlay-mapping <cr>
```

Handler ` RVA 0xF1CF5B0 `；selector ` 0 `；EOL ` RVA 0x344BCAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2d23ebbae41c8c42](../../evidence/conditions-sets-018.md#c-2d23ebbae41c8c42) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007098

```text
(exec)# show bgp path-attribute discard <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 42 `；EOL ` RVA 0x344C4A88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee49cfe183de4c1f](../../evidence/conditions-sets-092.md#c-ee49cfe183de4c1f) · [状态效果 S-12e6cf8452f437eb](../../evidence/state_effects-sets-004.md#s-12e6cf8452f437eb)

### path-002917

```text
(exec)# show bgp paths <cr>
```

Handler ` RVA 0xF171510 `；selector ` 0 `；EOL ` RVA 0x344BD638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-706899518598eacd](../../evidence/conditions-sets-043.md#c-706899518598eacd) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003055

```text
(exec)# show bgp peer-group <cr>
```

Handler ` RVA 0xF18C360 `；selector ` 0 `；EOL ` RVA 0x344BF3C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-009981

```text
(exec)# show bgp peer-group <string> summary <cr>
```

Handler ` RVA 0xF181410 `；selector ` 0 `；EOL ` RVA 0x344BF478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` peer-group name。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [参数 P-4086bcb5e58a8ba9](../../evidence/parameters-sets-005.md#p-4086bcb5e58a8ba9) · [状态效果 S-f55f078fc9693ac8](../../evidence/state_effects-sets-052.md#s-f55f078fc9693ac8)

### path-003011

```text
(exec)# show bgp pending-prefixes <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 30 `；EOL ` RVA 0x344BED00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002869

```text
(exec)# show bgp per-ce-label-internal <cr>
```

Handler ` RVA 0xF1CF4D0 `；selector ` 0 `；EOL ` RVA 0x344BD040 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a2da556f97fc04b](../../evidence/conditions-sets-016.md#c-2a2da556f97fc04b) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007216

```text
(exec)# show bgp prefix-list <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 19 `；EOL ` RVA 0x3552DD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` An IPv6 prefixlist to match on。

[条件 C-07871a927bf85ec8](../../evidence/conditions-sets-003.md#c-07871a927bf85ec8) · [参数 P-55043fbfe92bc85c](../../evidence/parameters-sets-007.md#p-55043fbfe92bc85c) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007239

```text
(exec)# show bgp prefix-list <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 19 `；EOL ` RVA 0x344C4298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A prefixlist to match on。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [参数 P-ef412fbca0c0c773](../../evidence/parameters-sets-018.md#p-ef412fbca0c0c773) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002914

```text
(exec)# show bgp rcache <cr>
```

Handler ` RVA 0xF1726C0 `；selector ` 0 `；EOL ` RVA 0x344BD8B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-361e1511b3667bfb](../../evidence/conditions-sets-021.md#c-361e1511b3667bfb) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007215

```text
(exec)# show bgp regexp <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 3 `；EOL ` RVA 0x34500970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A regular-expression to match BGP AS paths. Use "ctrl-v ?" to enter "?"。

[条件 C-01069764a4cb228d](../../evidence/conditions-sets-001.md#c-01069764a4cb228d) · [参数 P-299031b797db9159](../../evidence/parameters-sets-004.md#p-299031b797db9159) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003068

```text
(exec)# show bgp replication <cr>
```

Handler ` RVA 0xF186E40 `；selector ` 0 `；EOL ` RVA 0x344BFA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-79ad1cbf1ed259e7](../../evidence/conditions-sets-047.md#c-79ad1cbf1ed259e7) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003012

```text
(exec)# show bgp rib-failure <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 24 `；EOL ` RVA 0x344C4738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cee639592149fa6d](../../evidence/conditions-sets-080.md#c-cee639592149fa6d) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002856

```text
(exec)# show bgp rnh <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 46 `；EOL ` RVA 0x344C7A38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-41aa1c57823bb4b1](../../evidence/conditions-sets-026.md#c-41aa1c57823bb4b1) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007217

```text
(exec)# show bgp route-map <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 21 `；EOL ` RVA 0x344C2EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A route-map to match on。

[条件 C-140b3e253ef2c970](../../evidence/conditions-sets-008.md#c-140b3e253ef2c970) · [参数 P-3cf3c5ecc9709b73](../../evidence/parameters-sets-005.md#p-3cf3c5ecc9709b73) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007238

```text
(exec)# show bgp route-map <string> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 21 `；EOL ` RVA 0x3552E618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` A route-map to match on。

[条件 C-07871a927bf85ec8](../../evidence/conditions-sets-003.md#c-07871a927bf85ec8) · [参数 P-fe99b329b1f65a54](../../evidence/parameters-sets-019.md#p-fe99b329b1f65a54) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007227

```text
(exec)# show bgp rpki servers <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 33 `；EOL ` RVA 0x345003C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-283e400dab2a50ad](../../evidence/conditions-sets-016.md#c-283e400dab2a50ad) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007228

```text
(exec)# show bgp rpki table <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 34 `；EOL ` RVA 0x34500670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aeaf64f3ab8bf8ad](../../evidence/conditions-sets-068.md#c-aeaf64f3ab8bf8ad) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003002

```text
(exec)# show bgp rrinfo <cr>
```

Handler ` RVA 0xF172DB0 `；selector ` 0 `；EOL ` RVA 0x344BE298 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6b264f39b503c657](../../evidence/conditions-sets-041.md#c-6b264f39b503c657) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002871

```text
(exec)# show bgp rt-filter-list <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 31 `；EOL ` RVA 0x344CA140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-98c2ac06304f36e4](../../evidence/conditions-sets-059.md#c-98c2ac06304f36e4) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002588

```text
(exec)# show bgp sr-color <cr>
```

Handler ` RVA 0xF1D04C0 `；selector ` 0 `；EOL ` RVA 0x344FA3A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-898df15e9c172892](../../evidence/conditions-sets-053.md#c-898df15e9c172892) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002855

```text
(exec)# show bgp sr-policy <cr>
```

Handler ` RVA 0xF1D0170 `；selector ` 0 `；EOL ` RVA 0x344BC7B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0df3bda03146b8a5](../../evidence/conditions-sets-006.md#c-0df3bda03146b8a5) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007210

```text
(exec)# show bgp sso internal <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 28 `；EOL ` RVA 0x3372E168 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007198

```text
(exec)# show bgp sso summary <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 27 `；EOL ` RVA 0x3372DEC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002788

```text
(exec)# show bgp state <cr>
```

Handler ` RVA 0xF184320 `；selector ` 0 `；EOL ` RVA 0x344BC098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a353fd5c0fe76a4b](../../evidence/conditions-sets-063.md#c-a353fd5c0fe76a4b) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002790

```text
(exec)# show bgp summary <cr>
```

Handler ` RVA 0xF183AD0 `；selector ` 0 `；EOL ` RVA 0x344BBDF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a353fd5c0fe76a4b](../../evidence/conditions-sets-063.md#c-a353fd5c0fe76a4b) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-002836

```text
(exec)# show bgp tags <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 15 `；EOL ` RVA 0x344C9AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b005184223b2eca2](../../evidence/conditions-sets-068.md#c-b005184223b2eca2) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007221

```text
(exec)# show bgp template peer-policy <cr>
```

Handler ` RVA 0xF175000 `；selector ` 0 `；EOL ` RVA 0x344C1B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f83e23ddfdfda5bb](../../evidence/conditions-sets-096.md#c-f83e23ddfdfda5bb) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007234

```text
(exec)# show bgp template peer-session <cr>
```

Handler ` RVA 0xF176160 `；selector ` 0 `；EOL ` RVA 0x344C1F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f83e23ddfdfda5bb](../../evidence/conditions-sets-096.md#c-f83e23ddfdfda5bb) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-015492

```text
(exec)# show bgp update-group <?match_ipv6_addrinfo_action@555589a14380> <cr>
```

Handler ` RVA 0xF181830 `；selector ` 22 `；EOL ` RVA 0x344BFE50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [缺口 G-b65579c9a136c8d7](../../evidence/gaps-sets-006.md#g-b65579c9a136c8d7) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-019752

```text
(exec)# show bgp update-group <?match_ipv6_addrinfo_action@555589a14380> summary <cr>
```

Handler ` RVA 0xF181830 `；selector ` 23 `；EOL ` RVA 0x344BFE90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [缺口 G-b65579c9a136c8d7](../../evidence/gaps-sets-006.md#g-b65579c9a136c8d7) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-007142

```text
(exec)# show bgp update-group <number:1..4294967295> <cr>
```

Handler ` RVA 0xF181830 `；selector ` 22 `；EOL ` RVA 0x344BFE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` update-group index。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [参数 P-82fb47f8f93fea5b](../../evidence/parameters-sets-010.md#p-82fb47f8f93fea5b) · [状态效果 S-5c8549c2053a32b4](../../evidence/state_effects-sets-020.md#s-5c8549c2053a32b4)

### path-009989

```text
(exec)# show bgp update-group <number:1..4294967295> summary <cr>
```

Handler ` RVA 0xF181830 `；selector ` 23 `；EOL ` RVA 0x344BFE90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` update-group index。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [参数 P-82fb47f8f93fea5b](../../evidence/parameters-sets-010.md#p-82fb47f8f93fea5b) · [状态效果 S-5c8549c2053a32b4](../../evidence/state_effects-sets-020.md#s-5c8549c2053a32b4)

### path-002901

```text
(exec)# show bgp update-sources <cr>
```

Handler ` RVA 0xF1D0DF0 `；selector ` 0 `；EOL ` RVA 0x344BD328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78aacf99bc78a58a](../../evidence/conditions-sets-047.md#c-78aacf99bc78a58a) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-003054

```text
(exec)# show bgp va <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 40 `；EOL ` RVA 0x344C4DD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f95056f73917537](../../evidence/conditions-sets-012.md#c-1f95056f73917537) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-011434

```text
(exec)# show bgp ve-id <number:1..65535> block-offset <number:1..65535> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 1 `；EOL ` RVA 0x344CA560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Target VE ID value；` unsigned_number ` Target Block Offset value。

[条件 C-52db08189363b8e4](../../evidence/conditions-sets-032.md#c-52db08189363b8e4) · [参数 P-93dc4687e8d08585](../../evidence/parameters-sets-011.md#p-93dc4687e8d08585) · [状态效果 S-b55cf44884ee9a0b](../../evidence/state_effects-sets-038.md#s-b55cf44884ee9a0b)

### path-007093

```text
(exec)# show bgp version <number:1..4294967295> <cr>
```

Handler ` RVA 0xF17E380 `；selector ` 25 `；EOL ` RVA 0x344BF010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Version number and above。

[条件 C-b6b7c4925936b3dd](../../evidence/conditions-sets-071.md#c-b6b7c4925936b3dd) · [参数 P-49fbd35dbe8acc86](../../evidence/parameters-sets-006.md#p-49fbd35dbe8acc86) · [状态效果 S-4c2ec37a78ad1edd](../../evidence/state_effects-sets-017.md#s-4c2ec37a78ad1edd)

### path-000230

```text
(exec)# show bootvar <cr>
```

Handler ` RVA 0xD556740 `；selector ` 0 `；EOL ` RVA 0x33E811B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001302

```text
(exec)# show bootvar config-file <cr>
```

Handler ` RVA 0xD556740 `；selector ` 2 `；EOL ` RVA 0x33E80EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001315

```text
(exec)# show bootvar system <cr>
```

Handler ` RVA 0xD556740 `；selector ` 1 `；EOL ` RVA 0x33E81190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000478

```text
(exec)# show bridge <cr>
```

Handler ` RVA 0xF28E620 `；selector ` 0 `；EOL ` RVA 0x345E4198 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beaf129db49b1dc8](../../evidence/conditions-sets-074.md#c-beaf129db49b1dc8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012777

```text
(exec)# show bridge <interface> <cr>
```

Handler ` RVA 0xF28E620 `；selector ` 0 `；EOL ` RVA 0x345E4198 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-24bbcdc30e34b434](../../evidence/conditions-sets-014.md#c-24bbcdc30e34b434) · [缺口 G-bcb05ce553cc2094](../../evidence/gaps-sets-007.md#g-bcb05ce553cc2094) · [参数 P-e198752a8cc2d93f](../../evidence/parameters-sets-017.md#p-e198752a8cc2d93f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003983

```text
(exec)# show bridge circuit-group <cr>
```

Handler ` RVA 0xF27F440 `；selector ` 0 `；EOL ` RVA 0x345E8038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdf5b4c3539f5b86](../../evidence/conditions-sets-079.md#c-cdf5b4c3539f5b86) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003968

```text
(exec)# show bridge group <cr>
```

Handler ` RVA 0xF28F690 `；selector ` 0 `；EOL ` RVA 0x345E7CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdf5b4c3539f5b86](../../evidence/conditions-sets-079.md#c-cdf5b4c3539f5b86) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000268

```text
(exec)# show bridge-domain <cr>
```

Handler ` RVA 0xBF37660 `；selector ` 0 `；EOL ` RVA 0x33952B98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-37f6322a0dc9ce84](../../evidence/conditions-sets-022.md#c-37f6322a0dc9ce84) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001637

```text
(exec)# show bridge-domain c-mac <cr>
```

Handler ` RVA 0xBF38D70 `；selector ` 0 `；EOL ` RVA 0x33953B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f81fb1d8fa8d1c91](../../evidence/conditions-sets-096.md#c-f81fb1d8fa8d1c91) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001604

```text
(exec)# show bridge-domain external-ports <cr>
```

Handler ` RVA 0xBF37390 `；selector ` 0 `；EOL ` RVA 0x33953748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4acb0fa9f37613ec](../../evidence/conditions-sets-029.md#c-4acb0fa9f37613ec) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005337

```text
(exec)# show bridge-domain route stats <cr>
```

Handler ` RVA 0xBF373F0 `；selector ` 0 `；EOL ` RVA 0x33952848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d8ada47583390f6c](../../evidence/conditions-sets-083.md#c-d8ada47583390f6c) · [状态效果 S-658380f59a54d490](../../evidence/state_effects-sets-022.md#s-658380f59a54d490)

### path-000490

```text
(exec)# show bsc <cr>
```

Handler ` RVA 0x113C32F0 `；selector ` 0 `；EOL ` RVA 0x354B5910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000492

```text
(exec)# show bstun <cr>
```

Handler ` RVA 0x113E0EA0 `；selector ` 0 `；EOL ` RVA 0x354BC670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000464

```text
(exec)# show buffers <cr>
```

Handler ` RVA 0xE3DFC30 `；selector ` 0 `；EOL ` RVA 0x342B96A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-a261b3ab32fafcda](../../evidence/state_effects-sets-034.md#s-a261b3ab32fafcda)

### path-003914

```text
(exec)# show buffers failures <cr>
```

Handler ` RVA 0xE3E0BD0 `；selector ` 0 `；EOL ` RVA 0x342B9360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004035

```text
(exec)# show buffers leak <cr>
```

Handler ` RVA 0xE3DED00 `；selector ` 0 `；EOL ` RVA 0x342BA2E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [状态效果 S-a261b3ab32fafcda](../../evidence/state_effects-sets-034.md#s-a261b3ab32fafcda)

### path-010357

```text
(exec)# show buffers leak resource user <cr>
```

Handler ` RVA 0xE3DF2C0 `；selector ` 0 `；EOL ` RVA 0x342BA320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [状态效果 S-a261b3ab32fafcda](../../evidence/state_effects-sets-034.md#s-a261b3ab32fafcda)

### path-004033

```text
(exec)# show buffers tune <cr>
```

Handler ` RVA 0xE3DF810 `；selector ` 0 `；EOL ` RVA 0x342BA800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [状态效果 S-a261b3ab32fafcda](../../evidence/state_effects-sets-034.md#s-a261b3ab32fafcda)

### path-004023

```text
(exec)# show buffers usage <cr>
```

Handler ` RVA 0xE3DE890 `；selector ` 0 `；EOL ` RVA 0x342B9D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [状态效果 S-a261b3ab32fafcda](../../evidence/state_effects-sets-034.md#s-a261b3ab32fafcda)

### path-010355

```text
(exec)# show buffers usage pool <string> <cr>
```

Handler ` RVA 0xE3DE150 `；selector ` 0 `；EOL ` RVA 0x342B9D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of pool to display buffers from。

[条件 C-a4dd4203c52edb14](../../evidence/conditions-sets-064.md#c-a4dd4203c52edb14) · [参数 P-0c1e5d0ea68dc78e](../../evidence/parameters-sets-001.md#p-0c1e5d0ea68dc78e) · [状态效果 S-a261b3ab32fafcda](../../evidence/state_effects-sets-034.md#s-a261b3ab32fafcda)

### path-004186

```text
(exec)# show bulkstat data-group <cr>
```

Handler ` RVA 0xBC6B490 `；selector ` 0 `；EOL ` RVA 0x33884570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010444

```text
(exec)# show bulkstat data-group <string> process <cr>
```

Handler ` RVA 0xBC88BD0 `；selector ` 0 `；EOL ` RVA 0x33894480 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of data-group。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-af5b0e6e47e3ffab](../../evidence/parameters-sets-013.md#p-af5b0e6e47e3ffab) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004192

```text
(exec)# show bulkstat pre-defined <cr>
```

Handler ` RVA 0xBC6C900 `；selector ` 0 `；EOL ` RVA 0x338876A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008022

```text
(exec)# show bulkstat pre-defined data <cr>
```

Handler ` RVA 0xBC6C200 `；selector ` 0 `；EOL ` RVA 0x33887110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008026

```text
(exec)# show bulkstat pre-defined data-group <cr>
```

Handler ` RVA 0xBC6C630 `；selector ` 0 `；EOL ` RVA 0x33887400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008029

```text
(exec)# show bulkstat pre-defined instance <cr>
```

Handler ` RVA 0xBC6BE40 `；selector ` 0 `；EOL ` RVA 0x338876E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004187

```text
(exec)# show bulkstat profile <cr>
```

Handler ` RVA 0xBC6B220 `；selector ` 0 `；EOL ` RVA 0x338848D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000231

```text
(exec)# show calendar <cr>
```

Handler ` RVA 0xE038750 `；selector ` 0 `；EOL ` RVA 0x34171B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae8a8d611186038e](../../evidence/conditions-sets-067.md#c-ae8a8d611186038e) · [状态效果 S-51e3e2090756f514](../../evidence/state_effects-sets-018.md#s-51e3e2090756f514)

### path-003447

```text
(exec)# show call admission <cr>
```

Handler ` RVA 0xDEB05F0 `；selector ` 0 `；EOL ` RVA 0x3408CA08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007400

```text
(exec)# show call filter component <cr>
```

Handler ` RVA 0x16987360 `；selector ` 20 `；EOL ` RVA 0x3605ACB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007405

```text
(exec)# show call filter match-list <cr>
```

Handler ` RVA 0x16987110 `；selector ` 21 `；EOL ` RVA 0x3605A7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010144

```text
(exec)# show call filter match-list <number:1..16> <cr>
```

Handler ` RVA 0x16987360 `；selector ` 21 `；EOL ` RVA 0x3605A7C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` The unique Tag for this filter。

[条件 C-f36fb2d83ce0785a](../../evidence/conditions-sets-094.md#c-f36fb2d83ce0785a) · [参数 P-8da4415909c6b70d](../../evidence/parameters-sets-011.md#p-8da4415909c6b70d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000269

```text
(exec)# show call-home <cr>
```

Handler ` RVA 0xB6D5350 `；selector ` 4 `；EOL ` RVA 0x337EBFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-549ef0f05f705380](../../evidence/conditions-sets-033.md#c-549ef0f05f705380) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001547

```text
(exec)# show call-home alert-group <cr>
```

Handler ` RVA 0xB6D5300 `；selector ` 0 `；EOL ` RVA 0x337EAAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001526

```text
(exec)# show call-home detail <cr>
```

Handler ` RVA 0xB6D5350 `；selector ` 5 `；EOL ` RVA 0x337EA810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001730

```text
(exec)# show call-home diagnostic-signature <cr>
```

Handler ` RVA 0x128FEF40 `；selector ` 0 `；EOL ` RVA 0x337ECD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005547

```text
(exec)# show call-home diagnostic-signature <number:1..99999999> <cr>
```

Handler ` RVA 0x128FEE70 `；selector ` 0 `；EOL ` RVA 0x337ED900 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009061

```text
(exec)# show call-home diagnostic-signature <number:1..99999999> actions <cr>
```

Handler ` RVA 0x128FECD0 `；selector ` 0 `；EOL ` RVA 0x337ED080 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009060

```text
(exec)# show call-home diagnostic-signature <number:1..99999999> events <cr>
```

Handler ` RVA 0x128FEDA0 `；selector ` 0 `；EOL ` RVA 0x337ECDD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009071

```text
(exec)# show call-home diagnostic-signature <number:1..99999999> prerequisite <cr>
```

Handler ` RVA 0x128FEB20 `；selector ` 0 `；EOL ` RVA 0x337ED5D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-3e7f8db3c2a8e863](../../evidence/state_effects-sets-014.md#s-3e7f8db3c2a8e863)

### path-009065

```text
(exec)# show call-home diagnostic-signature <number:1..99999999> prompt <cr>
```

Handler ` RVA 0x128FEC00 `；selector ` 0 `；EOL ` RVA 0x337ED328 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009085

```text
(exec)# show call-home diagnostic-signature <number:1..99999999> variables <cr>
```

Handler ` RVA 0x128FEA50 `；selector ` 0 `；EOL ` RVA 0x337ED8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DS ID。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [参数 P-85d7c83c0ce412b1](../../evidence/parameters-sets-010.md#p-85d7c83c0ce412b1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005443

```text
(exec)# show call-home diagnostic-signature failure <cr>
```

Handler ` RVA 0x128FE5F0 `；selector ` 0 `；EOL ` RVA 0x337EC570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005418

```text
(exec)# show call-home diagnostic-signature info <cr>
```

Handler ` RVA 0x128FE890 `；selector ` 0 `；EOL ` RVA 0x337EC020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005430

```text
(exec)# show call-home diagnostic-signature register <cr>
```

Handler ` RVA 0x128FE7B0 `；selector ` 0 `；EOL ` RVA 0x337EC2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005471

```text
(exec)# show call-home diagnostic-signature statistics <cr>
```

Handler ` RVA 0x128FE6D0 `；selector ` 0 `；EOL ` RVA 0x337EC8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009055

```text
(exec)# show call-home diagnostic-signature statistics download <cr>
```

Handler ` RVA 0x128FE970 `；selector ` 0 `；EOL ` RVA 0x337EC880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-778c74158ba89a40](../../evidence/conditions-sets-046.md#c-778c74158ba89a40) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001567

```text
(exec)# show call-home events <cr>
```

Handler ` RVA 0xB6D6050 `；selector ` 0 `；EOL ` RVA 0x337EAD60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005330

```text
(exec)# show call-home mail-server status <cr>
```

Handler ` RVA 0xB6D5E60 `；selector ` 0 `；EOL ` RVA 0x337EA590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005395

```text
(exec)# show call-home profile <string> <cr>
```

Handler ` RVA 0xB6D4F40 `；selector ` 0 `；EOL ` RVA 0x337EB378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Profile name。

[条件 C-2b3793adec229b1b](../../evidence/conditions-sets-017.md#c-2b3793adec229b1b) · [参数 P-0a89f5cdc2a8ac43](../../evidence/parameters-sets-001.md#p-0a89f5cdc2a8ac43) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005368

```text
(exec)# show call-home profile all <cr>
```

Handler ` RVA 0xB6D4F40 `；selector ` 1 `；EOL ` RVA 0x337EB070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001641

```text
(exec)# show call-home smart-licensing <cr>
```

Handler ` RVA 0xB6D6BB0 `；selector ` 0 `；EOL ` RVA 0x337EBAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eeeeff8298224001](../../evidence/conditions-sets-092.md#c-eeeeff8298224001) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005404

```text
(exec)# show call-home smart-licensing statistics <cr>
```

Handler ` RVA 0xB6D6C40 `；selector ` 0 `；EOL ` RVA 0x337EBA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eeeeff8298224001](../../evidence/conditions-sets-092.md#c-eeeeff8298224001) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001628

```text
(exec)# show call-home statistics <cr>
```

Handler ` RVA 0xB6D6130 `；selector ` 0 `；EOL ` RVA 0x337EB6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d13560265b2422cd](../../evidence/conditions-sets-081.md#c-d13560265b2422cd) · [状态效果 S-fa35c60f99449b88](../../evidence/state_effects-sets-053.md#s-fa35c60f99449b88)

### path-001498

```text
(exec)# show call-home version <cr>
```

Handler ` RVA 0xB6D6CD0 `；selector ` 0 `；EOL ` RVA 0x337EA280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000179

```text
(exec)# show caller <cr>
```

Handler ` RVA 0xE0180D0 `；selector ` 0 `；EOL ` RVA 0x3415FB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001024

```text
(exec)# show caller summary <cr>
```

Handler ` RVA 0xE0179A0 `；selector ` 0 `；EOL ` RVA 0x34160370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-95b56fe6878c0d58](../../evidence/conditions-sets-058.md#c-95b56fe6878c0d58) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004700

```text
(exec)# show capability feature routing <cr>
```

Handler ` RVA 0xD2D7410 `；selector ` 1 `；EOL ` RVA 0x33FDCF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000192

```text
(exec)# show cca <cr>
```

Handler ` RVA 0xD6F1140 `；selector ` 0 `；EOL ` RVA 0x33EDE368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a4415503f550b572](../../evidence/conditions-sets-063.md#c-a4415503f550b572) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012444

```text
(exec)# show cca <interface> <cr>
```

Handler ` RVA 0xD6F1140 `；selector ` 0 `；EOL ` RVA 0x33EDE368 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9eb6776976115a1e](../../evidence/conditions-sets-061.md#c-9eb6776976115a1e) · [缺口 G-4a41c412bd10a961](../../evidence/gaps-sets-003.md#g-4a41c412bd10a961) · [参数 P-f30aea0856b54d98](../../evidence/parameters-sets-018.md#p-f30aea0856b54d98) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005686

```text
(exec)# show cce cp id <cr>
```

Handler ` RVA 0xDCC20C0 `；selector ` 0 `；EOL ` RVA 0x34039708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009130

```text
(exec)# show cce cp id collisions <cr>
```

Handler ` RVA 0xDCC1930 `；selector ` 0 `；EOL ` RVA 0x34039208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011083

```text
(exec)# show cce cp id collisions class-group <cr>
```

Handler ` RVA 0xDCC1D50 `；selector ` 0 `；EOL ` RVA 0x340391E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a83246923aa8127](../../evidence/conditions-sets-035.md#c-5a83246923aa8127) · [状态效果 S-a861a0d97651de03](../../evidence/state_effects-sets-036.md#s-a861a0d97651de03)

### path-009128

```text
(exec)# show cce cp id summary <cr>
```

Handler ` RVA 0xDCC1E40 `；selector ` 0 `；EOL ` RVA 0x340396E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014285

```text
(exec)# show cce cpdp associations <cr>
```

Handler ` RVA 0xDCEF2F0 `；selector ` 0 `；EOL ` RVA 0x3403C1B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-a0db229d144b0445](../../evidence/gaps-sets-006.md#g-a0db229d144b0445) · [状态效果 S-6205d77f283850ef](../../evidence/state_effects-sets-021.md#s-6205d77f283850ef)

### path-014302

```text
(exec)# show cce cpdp bindings <cr>
```

Handler ` RVA 0xDCEF2F0 `；selector ` 1 `；EOL ` RVA 0x3403C560 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-a0db229d144b0445](../../evidence/gaps-sets-006.md#g-a0db229d144b0445) · [状态效果 S-6205d77f283850ef](../../evidence/state_effects-sets-021.md#s-6205d77f283850ef)

### path-001962

```text
(exec)# show cce ha <cr>
```

Handler ` RVA 0xCD853B0 `；selector ` 0 `；EOL ` RVA 0x33CDE210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005734

```text
(exec)# show cce ha collisions <cr>
```

Handler ` RVA 0xCD84E70 `；selector ` 0 `；EOL ` RVA 0x33CDE278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009141

```text
(exec)# show cce ha collisions class-group <cr>
```

Handler ` RVA 0xCD852C0 `；selector ` 0 `；EOL ` RVA 0x33CDE250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1c4b9dfe9382cd8b](../../evidence/conditions-sets-011.md#c-1c4b9dfe9382cd8b) · [状态效果 S-9853de7b2fa9a8ae](../../evidence/state_effects-sets-032.md#s-9853de7b2fa9a8ae)

### path-000427

```text
(exec)# show cdapi <cr>
```

Handler ` RVA 0x161C5B00 `；selector ` 0 `；EOL ` RVA 0x35F0C810 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000280

```text
(exec)# show cdp <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 0 `；EOL ` RVA 0x33CE6DD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca50a594d10b5357](../../evidence/conditions-sets-078.md#c-ca50a594d10b5357) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005601

```text
(exec)# show cdp entry <string> <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 2 `；EOL ` RVA 0x33CE6EE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of CDP neighbor entry。

[条件 C-ca50a594d10b5357](../../evidence/conditions-sets-078.md#c-ca50a594d10b5357) · [参数 P-eda4bc9c9b079a5c](../../evidence/parameters-sets-018.md#p-eda4bc9c9b079a5c) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001688

```text
(exec)# show cdp feature <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 14 `；EOL ` RVA 0x33CE4610 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001771

```text
(exec)# show cdp interface <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 3 `；EOL ` RVA 0x33CE49A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-adb321c4e31075be](../../evidence/conditions-sets-067.md#c-adb321c4e31075be) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014034

```text
(exec)# show cdp interface <interface> <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 3 `；EOL ` RVA 0x33CE49A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-714709b7e6cd2116](../../evidence/conditions-sets-044.md#c-714709b7e6cd2116) · [缺口 G-5acd0daa1943e5ef](../../evidence/gaps-sets-004.md#g-5acd0daa1943e5ef) · [参数 P-79d63ac9c7f5ba88](../../evidence/parameters-sets-009.md#p-79d63ac9c7f5ba88) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001665

```text
(exec)# show cdp mgmt-address <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 15 `；EOL ` RVA 0x33CE4368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001817

```text
(exec)# show cdp neighbors <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 4 `；EOL ` RVA 0x33CE5630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-810111d7a1769c26](../../evidence/conditions-sets-050.md#c-810111d7a1769c26) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014112

```text
(exec)# show cdp neighbors <interface> <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 4 `；EOL ` RVA 0x33CE5630 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dc9f52cfa0445d20](../../evidence/conditions-sets-085.md#c-dc9f52cfa0445d20) · [缺口 G-e614963dd76406ea](../../evidence/gaps-sets-008.md#g-e614963dd76406ea) · [参数 P-4bb6679855382447](../../evidence/parameters-sets-006.md#p-4bb6679855382447) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005603

```text
(exec)# show cdp tlv app <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 6 `；EOL ` RVA 0x33CE5EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-87f4bf28607a4570](../../evidence/conditions-sets-053.md#c-87f4bf28607a4570) · [状态效果 S-3c52233a647971b3](../../evidence/state_effects-sets-013.md#s-3c52233a647971b3)

### path-018066

```text
(exec)# show cdp tlv app <interface> <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 6 `；EOL ` RVA 0x33CE5EE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3dac53d378f54174](../../evidence/conditions-sets-024.md#c-3dac53d378f54174) · [缺口 G-5261c143a3659a63](../../evidence/gaps-sets-003.md#g-5261c143a3659a63) · [参数 P-251d268977eacfaa](../../evidence/parameters-sets-003.md#p-251d268977eacfaa) · [状态效果 S-3c52233a647971b3](../../evidence/state_effects-sets-013.md#s-3c52233a647971b3)

### path-005654

```text
(exec)# show cdp tlv location-server <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 11 `；EOL ` RVA 0x33CE6670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb2525167c5516cb](../../evidence/conditions-sets-072.md#c-bb2525167c5516cb) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005551

```text
(exec)# show cdp tlv-list <string> <cr>
```

Handler ` RVA 0xCDA4900 `；selector ` 0 `；EOL ` RVA 0x33CE6B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of CDP Tlv list。

[条件 C-ce4e234829896151](../../evidence/conditions-sets-079.md#c-ce4e234829896151) · [参数 P-d0760b99dcfebbfd](../../evidence/parameters-sets-016.md#p-d0760b99dcfebbfd) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001740

```text
(exec)# show cdp traffic <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 1 `；EOL ` RVA 0x33CE5238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b0b8185a1bc3f501](../../evidence/conditions-sets-068.md#c-b0b8185a1bc3f501) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005480

```text
(exec)# show cdp vlan <number:1..4094> <cr>
```

Handler ` RVA 0xCDA4AC0 `；selector ` 5 `；EOL ` RVA 0x33CE4FB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` vlan number。

[条件 C-e05d7446190cef50](../../evidence/conditions-sets-086.md#c-e05d7446190cef50) · [参数 P-123f7db6d2d5ae9d](../../evidence/parameters-sets-002.md#p-123f7db6d2d5ae9d) · [状态效果 S-586875d0d8ad3879](../../evidence/state_effects-sets-019.md#s-586875d0d8ad3879)

### path-001749

```text
(exec)# show cef accounting <cr>
```

Handler ` RVA 0xB361DB0 `；selector ` 0 `；EOL ` RVA 0x3374B150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001609

```text
(exec)# show cef background <cr>
```

Handler ` RVA 0xB365420 `；selector ` 0 `；EOL ` RVA 0x33749090 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001909

```text
(exec)# show cef bfd <cr>
```

Handler ` RVA 0xB5B1E50 `；selector ` 0 `；EOL ` RVA 0x337AE350 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014303

```text
(exec)# show cef broker * <cr>
```

Handler ` RVA 0xB2C4830 `；selector ` 0 `；EOL ` RVA 0x33732AD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d4fa849add1dba58](../../evidence/conditions-sets-082.md#c-d4fa849add1dba58) · [缺口 G-1c054291fce371af](../../evidence/gaps-sets-001.md#g-1c054291fce371af) · [状态效果 S-5d294e23e34cd6ea](../../evidence/state_effects-sets-020.md#s-5d294e23e34cd6ea)

### path-005737

```text
(exec)# show cef broker ipv4_p1 <cr>
```

Handler ` RVA 0xB2C4830 `；selector ` 0 `；EOL ` RVA 0x33732AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a78c64637536b19](../../evidence/conditions-sets-041.md#c-6a78c64637536b19) · [状态效果 S-383b79a5409b1f7b](../../evidence/state_effects-sets-012.md#s-383b79a5409b1f7b)

### path-005399

```text
(exec)# show cef collapse-chain loadinfo <cr>
```

Handler ` RVA 0xB406F80 `；selector ` 0 `；EOL ` RVA 0x33748758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-592ee004d043f7a9](../../evidence/conditions-sets-035.md#c-592ee004d043f7a9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-017859

```text
(exec)# show cef collapse-chain loadinfo <interface> <cr>
```

Handler ` RVA 0xB406F80 `；selector ` 0 `；EOL ` RVA 0x33748758 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4eac190e1b6c4a3c](../../evidence/conditions-sets-031.md#c-4eac190e1b6c4a3c) · [缺口 G-834ea4f38eb6d85e](../../evidence/gaps-sets-005.md#g-834ea4f38eb6d85e) · [参数 P-0dd7cb97769ac93a](../../evidence/parameters-sets-002.md#p-0dd7cb97769ac93a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001867

```text
(exec)# show cef drop <cr>
```

Handler ` RVA 0xB5D0BA0 `；selector ` 1 `；EOL ` RVA 0x337ADE00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001768

```text
(exec)# show cef error <cr>
```

Handler ` RVA 0xB37E170 `；selector ` 0 `；EOL ` RVA 0x3374B3F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001772

```text
(exec)# show cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x3374ABA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-2bdc701e9dd500bd](../../evidence/state_effects-sets-010.md#s-2bdc701e9dd500bd)

### path-005420

```text
(exec)# show cef features global <cr>
```

Handler ` RVA 0xB3EB8E0 `；selector ` 0 `；EOL ` RVA 0x33749C88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001588

```text
(exec)# show cef fib <cr>
```

Handler ` RVA 0xB396530 `；selector ` 0 `；EOL ` RVA 0x33748D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001475

```text
(exec)# show cef gr <cr>
```

Handler ` RVA 0xB484AE0 `；selector ` 0 `；EOL ` RVA 0x33746BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005324

```text
(exec)# show cef hardware capabilities <cr>
```

Handler ` RVA 0xB4F1A40 `；selector ` 0 `；EOL ` RVA 0x33747190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-309e4b509921b91f](../../evidence/conditions-sets-019.md#c-309e4b509921b91f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005308

```text
(exec)# show cef hardware vectors <cr>
```

Handler ` RVA 0xB4F1380 `；selector ` 0 `；EOL ` RVA 0x33746EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001623

```text
(exec)# show cef idb <cr>
```

Handler ` RVA 0xB3ED230 `；selector ` 0 `；EOL ` RVA 0x33749978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001701

```text
(exec)# show cef interface <cr>
```

Handler ` RVA 0xB3EB980 `；selector ` 0 `；EOL ` RVA 0x337493D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cc32cd627ad48b7f](../../evidence/conditions-sets-079.md#c-cc32cd627ad48b7f) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014016

```text
(exec)# show cef interface <interface> <cr>
```

Handler ` RVA 0xB3EB980 `；selector ` 0 `；EOL ` RVA 0x337493D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-57e2cfa7bdd86db3](../../evidence/conditions-sets-034.md#c-57e2cfa7bdd86db3) · [缺口 G-99fda5ddcea6b2d5](../../evidence/gaps-sets-006.md#g-99fda5ddcea6b2d5) · [参数 P-a2a43652e391cd2d](../../evidence/parameters-sets-012.md#p-a2a43652e391cd2d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002031

```text
(exec)# show cef linecard <cr>
```

Handler ` RVA 0xB2DE600 `；selector ` 0 `；EOL ` RVA 0x33732308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2ffecb40c0491f80](../../evidence/conditions-sets-019.md#c-2ffecb40c0491f80) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-014361

```text
(exec)# show cef linecard <number:dynamic> <cr>
```

Handler ` RVA 0xB2DE600 `；selector ` 0 `；EOL ` RVA 0x33732308 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` linecard slot number。

[条件 C-ba7213064cfe69e1](../../evidence/conditions-sets-072.md#c-ba7213064cfe69e1) · [缺口 G-d8ce86ed359df42d](../../evidence/gaps-sets-008.md#g-d8ce86ed359df42d) · [参数 P-802a17416dc4fb69](../../evidence/parameters-sets-010.md#p-802a17416dc4fb69) · [状态效果 S-d844173b5807338f](../../evidence/state_effects-sets-046.md#s-d844173b5807338f)

### path-001570

```text
(exec)# show cef loadinfo <cr>
```

Handler ` RVA 0xB3F8EB0 `；selector ` 0 `；EOL ` RVA 0x33748AD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001889

```text
(exec)# show cef loops <cr>
```

Handler ` RVA 0xB40ECD0 `；selector ` 0 `；EOL ` RVA 0x33778150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001783

```text
(exec)# show cef memory <cr>
```

Handler ` RVA 0xB40F9F0 `；selector ` 0 `；EOL ` RVA 0x3374A780 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9ac008dab3f2faee](../../evidence/conditions-sets-060.md#c-9ac008dab3f2faee) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001828

```text
(exec)# show cef non-ip <cr>
```

Handler ` RVA 0xB41F540 `；selector ` 0 `；EOL ` RVA 0x3377C280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001888

```text
(exec)# show cef not-cef-switched <cr>
```

Handler ` RVA 0xB5D0BA0 `；selector ` 0 `；EOL ` RVA 0x337AE0A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001850

```text
(exec)# show cef nsf <cr>
```

Handler ` RVA 0xB32FB60 `；selector ` 0 `；EOL ` RVA 0x33739E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001573

```text
(exec)# show cef path <cr>
```

Handler ` RVA 0xB42B9A0 `；selector ` 0 `；EOL ` RVA 0x33764D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005349

```text
(exec)# show cef path list <cr>
```

Handler ` RVA 0xB43F150 `；selector ` 0 `；EOL ` RVA 0x33748320 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001752

```text
(exec)# show cef state <cr>
```

Handler ` RVA 0xB35DD50 `；selector ` 0 `；EOL ` RVA 0x3374AEB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011052

```text
(exec)# show cef subtree context client all <cr>
```

Handler ` RVA 0xB4534B0 `；selector ` 0 `；EOL ` RVA 0x3374A078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-af505f77d8addfea](../../evidence/state_effects-sets-037.md#s-af505f77d8addfea)

### path-005525

```text
(exec)# show cef switching background <cr>
```

Handler ` RVA 0xB4BFC90 `；selector ` 0 `；EOL ` RVA 0x3374B770 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009084

```text
(exec)# show cef switching reinject handles <cr>
```

Handler ` RVA 0xB4CCC60 `；selector ` 0 `；EOL ` RVA 0x3374BA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001611

```text
(exec)# show cef table <cr>
```

Handler ` RVA 0xB46F530 `；selector ` 0 `；EOL ` RVA 0x33747F58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005331

```text
(exec)# show cef table consistency-check <cr>
```

Handler ` RVA 0xB3702B0 `；selector ` 0 `；EOL ` RVA 0x337478F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-009031

```text
(exec)# show cef table download priority <cr>
```

Handler ` RVA 0xB2D7D00 `；selector ` 0 `；EOL ` RVA 0x337345B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001679

```text
(exec)# show cef timers <cr>
```

Handler ` RVA 0xB484B50 `；selector ` 0 `；EOL ` RVA 0x3374A368 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001911

```text
(exec)# show cef uid <cr>
```

Handler ` RVA 0xB4B7150 `；selector ` 0 `；EOL ` RVA 0x337843B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005585

```text
(exec)# show cef uid client-key <cr>
```

Handler ` RVA 0xB4B7030 `；selector ` 0 `；EOL ` RVA 0x33783B90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005640

```text
(exec)# show cef uid mgr-table <cr>
```

Handler ` RVA 0xB4B70D0 `；selector ` 0 `；EOL ` RVA 0x337840E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005616

```text
(exec)# show cef uid table <cr>
```

Handler ` RVA 0xB4B7080 `；selector ` 0 `；EOL ` RVA 0x33783E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001520

```text
(exec)# show cef vrf <cr>
```

Handler ` RVA 0xB48B9B0 `；selector ` 0 `；EOL ` RVA 0x337474B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001816

```text
(exec)# show cef walks <cr>
```

Handler ` RVA 0xB3584D0 `；selector ` 0 `；EOL ` RVA 0x3374C008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005534

```text
(exec)# show cef walks process <cr>
```

Handler ` RVA 0xB353670 `；selector ` 0 `；EOL ` RVA 0x3374BFE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005517

```text
(exec)# show cef walks queue <cr>
```

Handler ` RVA 0xB3529B0 `；selector ` 0 `；EOL ` RVA 0x3374BD38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002380

```text
(exec)# show cft active <cr>
```

Handler ` RVA 0x12945E00 `；selector ` 2 `；EOL ` RVA 0x358FE2B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c43e200f3ca7c949](../../evidence/conditions-sets-076.md#c-c43e200f3ca7c949) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002314

```text
(exec)# show cft all <cr>
```

Handler ` RVA 0x12945E00 `；selector ` 5 `；EOL ` RVA 0x358FDCD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93001d3a62216da9](../../evidence/conditions-sets-057.md#c-93001d3a62216da9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002394

```text
(exec)# show cft histogram <cr>
```

Handler ` RVA 0x12945E00 `；selector ` 4 `；EOL ` RVA 0x358FE8D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a613e5f356977f87](../../evidence/conditions-sets-064.md#c-a613e5f356977f87) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002373

```text
(exec)# show cft inactive <cr>
```

Handler ` RVA 0x12945E00 `；selector ` 3 `；EOL ` RVA 0x358FE630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9928868213ac8ad1](../../evidence/conditions-sets-059.md#c-9928868213ac8ad1) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002335

```text
(exec)# show cft stats <cr>
```

Handler ` RVA 0x12945E00 `；selector ` 1 `；EOL ` RVA 0x358FDF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31808c11098f6392](../../evidence/conditions-sets-019.md#c-31808c11098f6392) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001379

```text
(exec)# show checkpoint clients <cr>
```

Handler ` RVA 0xCDB5650 `；selector ` 0 `；EOL ` RVA 0x33CED7B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001369

```text
(exec)# show checkpoint entities <cr>
```

Handler ` RVA 0xCDB5AA0 `；selector ` 0 `；EOL ` RVA 0x33CED490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001394

```text
(exec)# show checkpoint statistics <cr>
```

Handler ` RVA 0xCDB5EF0 `；selector ` 0 `；EOL ` RVA 0x33CEDAB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005174

```text
(exec)# show checkpoint statistics buffer-usage <cr>
```

Handler ` RVA 0xCDB6090 `；selector ` 0 `；EOL ` RVA 0x33CEDA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000232

```text
(exec)# show chunk <cr>
```

Handler ` RVA 0xE0374E0 `；selector ` 0 `；EOL ` RVA 0x34171010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001338

```text
(exec)# show chunk brief <cr>
```

Handler ` RVA 0xE037090 `；selector ` 0 `；EOL ` RVA 0x34171570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001322

```text
(exec)# show chunk failures <cr>
```

Handler ` RVA 0xE0383A0 `；selector ` 0 `；EOL ` RVA 0x341712C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000360

```text
(exec)# show class-map <cr>
```

Handler ` RVA 0xD880580 `；selector ` 0 `；EOL ` RVA 0x33F1EDE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ada0a3e734f64ce4](../../evidence/conditions-sets-067.md#c-ada0a3e734f64ce4) · [状态效果 S-e86607253407d588](../../evidence/state_effects-sets-049.md#s-e86607253407d588)

### path-002896

```text
(exec)# show class-map <string> <cr>
```

Handler ` RVA 0xD87DBD0 `；selector ` 0 `；EOL ` RVA 0x33F1EDB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` class-map name。

[条件 C-ada0a3e734f64ce4](../../evidence/conditions-sets-067.md#c-ada0a3e734f64ce4) · [参数 P-dc4e8c7d52022925](../../evidence/parameters-sets-017.md#p-dc4e8c7d52022925) · [状态效果 S-e86607253407d588](../../evidence/state_effects-sets-049.md#s-e86607253407d588)

### path-022783

```text
(exec)# show class-map type control <?option@555589144650> all <cr>
```

Handler ` RVA 0xCB5ADD0 `；selector ` 0 `；EOL ` RVA 0x33BF06F0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e196699bc6ee8e36](../../evidence/conditions-sets-087.md#c-e196699bc6ee8e36) · [缺口 G-68ae461709ba3656](../../evidence/gaps-sets-004.md#g-68ae461709ba3656) · [状态效果 S-abc8595075f138dd](../../evidence/state_effects-sets-036.md#s-abc8595075f138dd)

### path-007049

```text
(exec)# show class-map type control <cr>
```

Handler ` RVA 0x10A5CCE0 `；selector ` 0 `；EOL ` RVA 0x34C76B18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26781530c13403ed](../../evidence/conditions-sets-015.md#c-26781530c13403ed) · [状态效果 S-e86607253407d588](../../evidence/state_effects-sets-049.md#s-e86607253407d588)

### path-007047

```text
(exec)# show class-map type traffic <cr>
```

Handler ` RVA 0x10A62340 `；selector ` 0 `；EOL ` RVA 0x34C27CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26781530c13403ed](../../evidence/conditions-sets-015.md#c-26781530c13403ed) · [状态效果 S-e86607253407d588](../../evidence/state_effects-sets-049.md#s-e86607253407d588)

### path-000386

```text
(exec)# show clns <cr>
```

Handler ` RVA 0x10595620 `；selector ` 5 `；EOL ` RVA 0x34B618A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05a5407df7ae53fb](../../evidence/conditions-sets-003.md#c-05a5407df7ae53fb) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003084

```text
(exec)# show clns cache <cr>
```

Handler ` RVA 0x10595620 `；selector ` 1 `；EOL ` RVA 0x34B5E8A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003244

```text
(exec)# show clns es-neighbors <cr>
```

Handler ` RVA 0x10595620 `；selector ` 2 `；EOL ` RVA 0x34B61128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a235a042e9154087](../../evidence/conditions-sets-063.md#c-a235a042e9154087) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015615

```text
(exec)# show clns es-neighbors <interface> <cr>
```

Handler ` RVA 0x10595620 `；selector ` 2 `；EOL ` RVA 0x34B61128 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-82d208e8df6922b3](../../evidence/conditions-sets-051.md#c-82d208e8df6922b3) · [缺口 G-4b04489f10320f65](../../evidence/gaps-sets-003.md#g-4b04489f10320f65) · [参数 P-38ca496b5546ee3d](../../evidence/parameters-sets-005.md#p-38ca496b5546ee3d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003179

```text
(exec)# show clns filter-expr <cr>
```

Handler ` RVA 0x10595620 `；selector ` 3 `；EOL ` RVA 0x34B5F608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34a69b8a41bf9e98](../../evidence/conditions-sets-020.md#c-34a69b8a41bf9e98) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003160

```text
(exec)# show clns filter-set <cr>
```

Handler ` RVA 0x10595620 `；selector ` 4 `；EOL ` RVA 0x34B5FA38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003069

```text
(exec)# show clns interface <cr>
```

Handler ` RVA 0x10595620 `；selector ` 6 `；EOL ` RVA 0x34B5E580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba6ae4252ff84c85](../../evidence/conditions-sets-072.md#c-ba6ae4252ff84c85) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015411

```text
(exec)# show clns interface <interface> <cr>
```

Handler ` RVA 0x10595620 `；selector ` 6 `；EOL ` RVA 0x34B5E580 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2e507f530c7b3e5a](../../evidence/conditions-sets-018.md#c-2e507f530c7b3e5a) · [缺口 G-a73090ac3518a271](../../evidence/gaps-sets-006.md#g-a73090ac3518a271) · [参数 P-7a86ae6f2863a694](../../evidence/parameters-sets-010.md#p-7a86ae6f2863a694) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003190

```text
(exec)# show clns internal <cr>
```

Handler ` RVA 0x10595620 `；selector ` 11 `；EOL ` RVA 0x34B60020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003260

```text
(exec)# show clns is-neighbors <cr>
```

Handler ` RVA 0x10595620 `；selector ` 7 `；EOL ` RVA 0x34B61530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a432d9249f9516d](../../evidence/conditions-sets-023.md#c-3a432d9249f9516d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015630

```text
(exec)# show clns is-neighbors <interface> <cr>
```

Handler ` RVA 0x10595620 `；selector ` 7 `；EOL ` RVA 0x34B61530 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9395dc8e65f8bda2](../../evidence/conditions-sets-057.md#c-9395dc8e65f8bda2) · [缺口 G-199d78878a3a4046](../../evidence/gaps-sets-001.md#g-199d78878a3a4046) · [参数 P-09fa215a4a2df6ef](../../evidence/parameters-sets-001.md#p-09fa215a4a2df6ef) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003245

```text
(exec)# show clns neighbors <cr>
```

Handler ` RVA 0x10595620 `；selector ` 8 `；EOL ` RVA 0x34B60D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8140e005f190059](../../evidence/conditions-sets-090.md#c-e8140e005f190059) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-015616

```text
(exec)# show clns neighbors <interface> <cr>
```

Handler ` RVA 0x10595620 `；selector ` 8 `；EOL ` RVA 0x34B60D10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e3345c6a2bdbec86](../../evidence/conditions-sets-087.md#c-e3345c6a2bdbec86) · [缺口 G-2a85fb29c906db72](../../evidence/gaps-sets-002.md#g-2a85fb29c906db72) · [参数 P-ea298e7f1b04e0a7](../../evidence/parameters-sets-018.md#p-ea298e7f1b04e0a7) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007222

```text
(exec)# show clns neighbors areas <cr>
```

Handler ` RVA 0x10595620 `；selector ` 9 `；EOL ` RVA 0x34B60970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e7b3322c11c53792](../../evidence/conditions-sets-089.md#c-e7b3322c11c53792) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-019832

```text
(exec)# show clns neighbors areas <interface> <cr>
```

Handler ` RVA 0x10595620 `；selector ` 9 `；EOL ` RVA 0x34B60970 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-65bb55551687ce59](../../evidence/conditions-sets-039.md#c-65bb55551687ce59) · [缺口 G-618a5cc0ff6a1d0d](../../evidence/gaps-sets-004.md#g-618a5cc0ff6a1d0d) · [参数 P-6e694c8eb206aeed](../../evidence/parameters-sets-009.md#p-6e694c8eb206aeed) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003124

```text
(exec)# show clns old-route-display <cr>
```

Handler ` RVA 0x10595620 `；selector ` 13 `；EOL ` RVA 0x34B5F280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003175

```text
(exec)# show clns protocol <cr>
```

Handler ` RVA 0x10595620 `；selector ` 10 `；EOL ` RVA 0x34B5FD30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003062

```text
(exec)# show clns redirects <cr>
```

Handler ` RVA 0x10595620 `；selector ` 12 `；EOL ` RVA 0x34B5EBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003150

```text
(exec)# show clns route <cr>
```

Handler ` RVA 0x10595620 `；selector ` 14 `；EOL ` RVA 0x34B5EF18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d986ee1aea9a133](../../evidence/conditions-sets-024.md#c-3d986ee1aea9a133) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003213

```text
(exec)# show clns traffic <cr>
```

Handler ` RVA 0x10595620 `；selector ` 15 `；EOL ` RVA 0x34B60400 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000373

```text
(exec)# show cls <cr>
```

Handler ` RVA 0x113FD270 `；selector ` 0 `；EOL ` RVA 0x354C2FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007861

```text
(exec)# show cns config connections <cr>
```

Handler ` RVA 0xF31E800 `；selector ` 0 `；EOL ` RVA 0x34607338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007867

```text
(exec)# show cns config outstanding <cr>
```

Handler ` RVA 0xF31EA10 `；selector ` 0 `；EOL ` RVA 0x346075E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007873

```text
(exec)# show cns config stats <cr>
```

Handler ` RVA 0xF31EA90 `；selector ` 0 `；EOL ` RVA 0x34607888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007846

```text
(exec)# show cns event connections <cr>
```

Handler ` RVA 0xF361280 `；selector ` 0 `；EOL ` RVA 0x34616C90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007854

```text
(exec)# show cns event stats <cr>
```

Handler ` RVA 0xF361660 `；selector ` 0 `；EOL ` RVA 0x34616F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007857

```text
(exec)# show cns event subject <cr>
```

Handler ` RVA 0xF3610A0 `；selector ` 0 `；EOL ` RVA 0x34616A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-b22262eb38a795c1](../../evidence/state_effects-sets-038.md#s-b22262eb38a795c1)

### path-007864

```text
(exec)# show cns image connections <cr>
```

Handler ` RVA 0xF36D2D0 `；selector ` 2 `；EOL ` RVA 0x3461B548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007871

```text
(exec)# show cns image inventory <cr>
```

Handler ` RVA 0xF36D2D0 `；selector ` 3 `；EOL ` RVA 0x3461B7F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007878

```text
(exec)# show cns image status <cr>
```

Handler ` RVA 0xF36D2D0 `；selector ` 1 `；EOL ` RVA 0x3461BA98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000205

```text
(exec)# show compress <cr>
```

Handler ` RVA 0xF425840 `；selector ` 0 `；EOL ` RVA 0x34646AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000151

```text
(exec)# show configuration <cr>
```

Handler ` RVA 0xDFF0C60 `；selector ` 0 `；EOL ` RVA 0x340A9848 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000810

```text
(exec)# show configuration ha-sync-lock <cr>
```

Handler ` RVA 0xDF3AC80 `；selector ` 0 `；EOL ` RVA 0x340B5EB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000722

```text
(exec)# show configuration history <cr>
```

Handler ` RVA 0xDFF0C10 `；selector ` 0 `；EOL ` RVA 0x340C6280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000848

```text
(exec)# show configuration id <cr>
```

Handler ` RVA 0xDEDF3F0 `；selector ` 0 `；EOL ` RVA 0x3409DCA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000788

```text
(exec)# show configuration lock <cr>
```

Handler ` RVA 0xDF3ADE0 `；selector ` 0 `；EOL ` RVA 0x340B5C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012273

```text
(exec)# show connection <cr>
```

Handler ` RVA 0xF43B510 `；selector ` 1 `；EOL ` RVA 0x346486B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [缺口 G-b2b2d944c2ba74c6](../../evidence/gaps-sets-006.md#g-b2b2d944c2ba74c6) · [状态效果 S-e7465c417a6c8c88](../../evidence/state_effects-sets-049.md#s-e7465c417a6c8c88)

### path-000167

```text
(exec)# show controllers <cr>
```

Handler ` RVA 0xE006D70 `；selector ` 0 `；EOL ` RVA 0x34162D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-012454

```text
(exec)# show controllers <interface> <cr>
```

Handler ` RVA 0xE006D70 `；selector ` 0 `；EOL ` RVA 0x35F34680 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e01a423c69b66110](../../evidence/conditions-sets-086.md#c-e01a423c69b66110) · [缺口 G-7023c14a9b15b538](../../evidence/gaps-sets-004.md#g-7023c14a9b15b538) · [参数 P-5c63b65693f7c60d](../../evidence/parameters-sets-007.md#p-5c63b65693f7c60d) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025296

```text
(exec)# show controllers E1 <?controller_action@55558b4482b0> <cr>
```

Handler ` RVA 0x16156180 `；selector ` 0 `；EOL ` RVA 0x35EF46B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60b4bc511477c0f4](../../evidence/conditions-sets-038.md#c-60b4bc511477c0f4) · [缺口 G-f094744f7bab3061](../../evidence/gaps-sets-008.md#g-f094744f7bab3061) · [状态效果 S-f5c52c4c7a1bc416](../../evidence/state_effects-sets-052.md#s-f5c52c4c7a1bc416)

### path-025310

```text
(exec)# show controllers E1 <?controller_action@55558b4482b0> errors <cr>
```

Handler ` RVA 0x161596B0 `；selector ` 0 `；EOL ` RVA 0x35EF4358 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-36af7238abcbba44](../../evidence/conditions-sets-021.md#c-36af7238abcbba44) · [缺口 G-f094744f7bab3061](../../evidence/gaps-sets-008.md#g-f094744f7bab3061) · [状态效果 S-20cef277f19f4e7c](../../evidence/state_effects-sets-007.md#s-20cef277f19f4e7c)

### path-013323

```text
(exec)# show controllers SHDSL <?controller_action@55558b4d7180> <cr>
```

Handler ` RVA 0x163CDC00 `；selector ` 0 `；EOL ` RVA 0x35F83210 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c8774190dbaa4eb6](../../evidence/conditions-sets-077.md#c-c8774190dbaa4eb6) · [缺口 G-347e0cb7308c8c57](../../evidence/gaps-sets-002.md#g-347e0cb7308c8c57) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-025295

```text
(exec)# show controllers T1 <?controller_action@55558b444d60> <cr>
```

Handler ` RVA 0x16156180 `；selector ` 0 `；EOL ` RVA 0x35EF1238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a53a4c5ea1d205a4](../../evidence/conditions-sets-064.md#c-a53a4c5ea1d205a4) · [缺口 G-2342bf0422609833](../../evidence/gaps-sets-002.md#g-2342bf0422609833) · [状态效果 S-394232bf9127d0b0](../../evidence/state_effects-sets-013.md#s-394232bf9127d0b0)

### path-025309

```text
(exec)# show controllers T1 <?controller_action@55558b444d60> errors <cr>
```

Handler ` RVA 0x161596B0 `；selector ` 0 `；EOL ` RVA 0x35EF0E08 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-58809a9996eaf281](../../evidence/conditions-sets-035.md#c-58809a9996eaf281) · [缺口 G-2342bf0422609833](../../evidence/gaps-sets-002.md#g-2342bf0422609833) · [状态效果 S-81a6fde4a5248c1a](../../evidence/state_effects-sets-028.md#s-81a6fde4a5248c1a)

### path-013291

```text
(exec)# show controllers VDSL <?controller_action@55558adc38c8> <cr>
```

Handler ` RVA 0x1243F9A0 `；selector ` 0 `；EOL ` RVA 0x3586BA20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3fa072b76241173d](../../evidence/conditions-sets-025.md#c-3fa072b76241173d) · [缺口 G-513ee9f718c2bc66](../../evidence/gaps-sets-003.md#g-513ee9f718c2bc66) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-002905

```text
(exec)# show cops servers <cr>
```

Handler ` RVA 0xF43F4A0 `；selector ` 0 `；EOL ` RVA 0x3464C670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-07309060327c18d6](../../evidence/state_effects-sets-002.md#s-07309060327c18d6)

### path-000598

```text
(exec)# show coverage history <cr>
```

Handler ` RVA 0xDE87B10 `；selector ` 3 `；EOL ` RVA 0x34124C58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83ac4c3b56d3e027](../../evidence/conditions-sets-051.md#c-83ac4c3b56d3e027) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-004307

```text
(exec)# show coverage history all <cr>
```

Handler ` RVA 0xDE87B10 `；selector ` 0 `；EOL ` RVA 0x341243D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-83ac4c3b56d3e027](../../evidence/conditions-sets-051.md#c-83ac4c3b56d3e027) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008082

```text
(exec)# show coverage history first <number:1..100000> <cr>
```

Handler ` RVA 0xDE87B10 `；selector ` 1 `；EOL ` RVA 0x341246E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-83ac4c3b56d3e027](../../evidence/conditions-sets-051.md#c-83ac4c3b56d3e027) · [参数 P-dbaf4cc08bd9072a](../../evidence/parameters-sets-017.md#p-dbaf4cc08bd9072a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-008087

```text
(exec)# show coverage history last <number:1..100000> <cr>
```

Handler ` RVA 0xDE87B10 `；selector ` 2 `；EOL ` RVA 0x341249D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of entries to show。

[条件 C-83ac4c3b56d3e027](../../evidence/conditions-sets-051.md#c-83ac4c3b56d3e027) · [参数 P-f74b23a17eb96ea5](../../evidence/parameters-sets-018.md#p-f74b23a17eb96ea5) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005656

```text
(exec)# show cpl c3pl-info list <cr>
```

Handler ` RVA 0xD8B93E0 `；selector ` 0 `；EOL ` RVA 0x33F3FA90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-307917e49644ca10](../../evidence/conditions-sets-019.md#c-307917e49644ca10) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005605

```text
(exec)# show cpl class-map hash-table <cr>
```

Handler ` RVA 0xD8B9240 `；selector ` 1 `；EOL ` RVA 0x33F3F4A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-275a52bf6e5b00f0](../../evidence/conditions-sets-015.md#c-275a52bf6e5b00f0) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-005629

```text
(exec)# show cpl concurrency history <cr>
```

Handler ` RVA 0xD8B8CF0 `；selector ` 0 `；EOL ` RVA 0x33F3F140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f5422dc3d911bf95](../../evidence/conditions-sets-095.md#c-f5422dc3d911bf95) · [状态效果 S-b020807201af9c22](../../evidence/state_effects-sets-037.md#s-b020807201af9c22)

### path-005630

```text
(exec)# show cpl policy-map hash-table <cr>
```

Handler ` RVA 0xD8B9240 `；selector ` 2 `；EOL ` RVA 0x33F3F798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4dc28931e33e1fa8](../../evidence/conditions-sets-030.md#c-4dc28931e33e1fa8) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-001905

```text
(exec)# show cpl target-c3pl-info <cr>
```

Handler ` RVA 0xD8B98E0 `；selector ` 0 `；EOL ` RVA 0x33F3FD20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-936378a57fc14c18](../../evidence/conditions-sets-057.md#c-936378a57fc14c18) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-000428

```text
(exec)# show crm <cr>
```

Handler ` RVA 0x1E3CBD20 `；selector ` 0 `；EOL ` RVA 0x37908758 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007536

```text
(exec)# show crypto autovpn session <cr>
```

Handler ` RVA 0x165EC2A0 `；selector ` 0 `；EOL ` RVA 0x35FA5C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010227

```text
(exec)# show crypto autovpn session detail <cr>
```

Handler ` RVA 0x165EC2A0 `；selector ` 1 `；EOL ` RVA 0x35FA5C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011567

```text
(exec)# show crypto autovpn session peerno <number:0..2147483647> <cr>
```

Handler ` RVA 0x165EC2A0 `；selector ` 2 `；EOL ` RVA 0x35FA59B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Peerno。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-e203d958bcfef184](../../evidence/parameters-sets-017.md#p-e203d958bcfef184) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007582

```text
(exec)# show crypto ca benchmarks <cr>
```

Handler ` RVA 0x11F3DA70 `；selector ` 0 `；EOL ` RVA 0x357560E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007555

```text
(exec)# show crypto ca certificates <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 0 `；EOL ` RVA 0x35751360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5762d637628c944](../../evidence/conditions-sets-082.md#c-d5762d637628c944) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-010235

```text
(exec)# show crypto ca certificates pem <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 9 `；EOL ` RVA 0x35751068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-010225

```text
(exec)# show crypto ca certificates storage <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 4 `；EOL ` RVA 0x35750D58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007568

```text
(exec)# show crypto ca counters <cr>
```

Handler ` RVA 0x11FC79F0 `；selector ` 0 `；EOL ` RVA 0x35755B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007548

```text
(exec)# show crypto ca crls <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 1 `；EOL ` RVA 0x35751D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007573

```text
(exec)# show crypto ca session <cr>
```

Handler ` RVA 0x11FD6430 `；selector ` 0 `；EOL ` RVA 0x35755E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007562

```text
(exec)# show crypto ca timers <cr>
```

Handler ` RVA 0x11FF3230 `；selector ` 7 `；EOL ` RVA 0x357526A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-010242

```text
(exec)# show crypto ca timers detail <cr>
```

Handler ` RVA 0x11FF3230 `；selector ` 8 `；EOL ` RVA 0x35752678 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007563

```text
(exec)# show crypto ca trustpoints <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 2 `；EOL ` RVA 0x35752340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-df03e2e4931c2db4](../../evidence/conditions-sets-086.md#c-df03e2e4931c2db4) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-010236

```text
(exec)# show crypto ca trustpoints status <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 3 `；EOL ` RVA 0x35752018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-007551

```text
(exec)# show crypto ca trustpool <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 5 `；EOL ` RVA 0x35751948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-010231

```text
(exec)# show crypto ca trustpool policy <cr>
```

Handler ` RVA 0x11F33040 `；selector ` 6 `；EOL ` RVA 0x357516A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-21e76ceaa87ab5c5](../../evidence/state_effects-sets-008.md#s-21e76ceaa87ab5c5)

### path-003635

```text
(exec)# show crypto eli <cr>
```

Handler ` RVA 0x120E67F0 `；selector ` 0 `；EOL ` RVA 0x3579F418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-734c32cda6d0c967](../../evidence/conditions-sets-045.md#c-734c32cda6d0c967) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007546

```text
(exec)# show crypto eli statistics <cr>
```

Handler ` RVA 0x120E8450 `；selector ` 0 `；EOL ` RVA 0x3579F720 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-734c32cda6d0c967](../../evidence/conditions-sets-045.md#c-734c32cda6d0c967) · [状态效果 S-21fe82d7381ca777](../../evidence/state_effects-sets-008.md#s-21fe82d7381ca777)

### path-003614

```text
(exec)# show crypto ha <cr>
```

Handler ` RVA 0x1924CE20 `；selector ` 0 `；EOL ` RVA 0x3697AAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007534

```text
(exec)# show crypto ha statistics <cr>
```

Handler ` RVA 0x1924CE70 `；selector ` 0 `；EOL ` RVA 0x3697AAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ff2f7bc8168f7349](../../evidence/conditions-sets-098.md#c-ff2f7bc8168f7349) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010213

```text
(exec)# show crypto key mypubkey rsa <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x35794EF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-eeaaf03fd4260178](../../evidence/state_effects-sets-050.md#s-eeaaf03fd4260178)

### path-010224

```text
(exec)# show crypto key pubkey-chain rsa <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x35794B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-dece9d70d25ad7d7](../../evidence/state_effects-sets-047.md#s-dece9d70d25ad7d7)

### path-011918

```text
(exec)# show crypto key pubkey-chain rsa address <address> <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x35794548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Peer IP address。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-4f58b1bb520f6f99](../../evidence/parameters-sets-007.md#p-4f58b1bb520f6f99) · [状态效果 S-e863fe5e3fdc5d74](../../evidence/state_effects-sets-049.md#s-e863fe5e3fdc5d74)

### path-011917

```text
(exec)# show crypto key pubkey-chain rsa name <string> <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x35794250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Peer name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-4ab5581401eb1bf1](../../evidence/parameters-sets-006.md#p-4ab5581401eb1bf1) · [状态效果 S-bdda1a792bee9cd9](../../evidence/state_effects-sets-040.md#s-bdda1a792bee9cd9)

### path-011919

```text
(exec)# show crypto key pubkey-chain rsa vrf <string> <cr>
```

Handler ` RVA 0x123A4C00 `；selector ` 0 `；EOL ` RVA 0x357948A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` the VRF name。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [参数 P-3106e7451af1ac7a](../../evidence/parameters-sets-004.md#p-3106e7451af1ac7a) · [状态效果 S-d868736b1d146d59](../../evidence/state_effects-sets-046.md#s-d868736b1d146d59)

### path-007510

```text
(exec)# show crypto key storage <cr>
```

Handler ` RVA 0x121539B0 `；selector ` 0 `；EOL ` RVA 0x35795218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007541

```text
(exec)# show crypto pki server <cr>
```

Handler ` RVA 0xBBBC250 `；selector ` 0 `；EOL ` RVA 0x33870D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-81ec4a802dab777d](../../evidence/state_effects-sets-028.md#s-81ec4a802dab777d)

### path-000445

```text
(exec)# show cts <cr>
```

Handler ` RVA 0x13033940 `；selector ` 0 `；EOL ` RVA 0x35A288F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-631d7c26913618f9](../../evidence/conditions-sets-038.md#c-631d7c26913618f9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010259

```text
(exec)# show cts ap sgt-info <string> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 33 `；EOL ` RVA 0x35A1CB80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show SGT info by AP name。

[条件 C-dd0262a6e26d155e](../../evidence/conditions-sets-085.md#c-dd0262a6e26d155e) · [参数 P-2249494c4998cbf4](../../evidence/parameters-sets-003.md#p-2249494c4998cbf4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007596

```text
(exec)# show cts authorization entries <cr>
```

Handler ` RVA 0x13033940 `；selector ` 15 `；EOL ` RVA 0x35A1B718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5b80759aae321514](../../evidence/conditions-sets-036.md#c-5b80759aae321514) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003632

```text
(exec)# show cts credentials <cr>
```

Handler ` RVA 0x13033940 `；selector ` 6 `；EOL ` RVA 0x35A18060 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8faa9ca9ab637a3a](../../evidence/conditions-sets-056.md#c-8faa9ca9ab637a3a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003669

```text
(exec)# show cts environment-data <cr>
```

Handler ` RVA 0x13033940 `；selector ` 8 `；EOL ` RVA 0x35A19268 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-521ec4596c894423](../../evidence/conditions-sets-032.md#c-521ec4596c894423) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007623

```text
(exec)# show cts ha sync-status <cr>
```

Handler ` RVA 0x13033940 `；selector ` 39 `；EOL ` RVA 0x35A1CE50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-631d7c26913618f9](../../evidence/conditions-sets-038.md#c-631d7c26913618f9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003693

```text
(exec)# show cts interface <cr>
```

Handler ` RVA 0x13033940 `；selector ` 1 `；EOL ` RVA 0x35A18718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d5994a360ac2635](../../evidence/conditions-sets-024.md#c-3d5994a360ac2635) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-016065

```text
(exec)# show cts interface <interface> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 1 `；EOL ` RVA 0x35A18718 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4457c74e0ecd8375](../../evidence/conditions-sets-027.md#c-4457c74e0ecd8375) · [缺口 G-c05a47c21b89d969](../../evidence/gaps-sets-007.md#g-c05a47c21b89d969) · [参数 P-043d9e61c9495761](../../evidence/parameters-sets-001.md#p-043d9e61c9495761) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007571

```text
(exec)# show cts interface brief <cr>
```

Handler ` RVA 0x13033940 `；selector ` 2 `；EOL ` RVA 0x35A189C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d5994a360ac2635](../../evidence/conditions-sets-024.md#c-3d5994a360ac2635) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007576

```text
(exec)# show cts interface summary <cr>
```

Handler ` RVA 0x13033940 `；selector ` 3 `；EOL ` RVA 0x35A18C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d5994a360ac2635](../../evidence/conditions-sets-024.md#c-3d5994a360ac2635) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003644

```text
(exec)# show cts keystore <cr>
```

Handler ` RVA 0x13033940 `；selector ` 4 `；EOL ` RVA 0x35A18348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f6008f2cf1c911cc](../../evidence/conditions-sets-095.md#c-f6008f2cf1c911cc) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-023141

```text
(exec)# show cts macsec counters interface <interface> <cr>
```

Handler ` RVA 0x16071FB0 `；selector ` 0 `；EOL ` RVA 0x35EADA38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-210ce598812a9cd6](../../evidence/conditions-sets-013.md#c-210ce598812a9cd6) · [缺口 G-75c4e3c27564342b](../../evidence/gaps-sets-005.md#g-75c4e3c27564342b) · [参数 P-bce36eccb78ff860](../../evidence/parameters-sets-014.md#p-bce36eccb78ff860) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003619

```text
(exec)# show cts pacs <cr>
```

Handler ` RVA 0x13033940 `；selector ` 5 `；EOL ` RVA 0x35A17D78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4dac7d6ba09eafd2](../../evidence/conditions-sets-030.md#c-4dac7d6ba09eafd2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003744

```text
(exec)# show cts policy <cr>
```

Handler ` RVA 0x13033940 `；selector ` 12 `；EOL ` RVA 0x35A1A170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-327d8089eb969764](../../evidence/conditions-sets-020.md#c-327d8089eb969764) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007599

```text
(exec)# show cts policy peer <cr>
```

Handler ` RVA 0x13033940 `；selector ` 10 `；EOL ` RVA 0x35A199D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f543fa3d39bc1ef9](../../evidence/conditions-sets-095.md#c-f543fa3d39bc1ef9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007647

```text
(exec)# show cts policy sgt <cr>
```

Handler ` RVA 0x13033940 `；selector ` 11 `；EOL ` RVA 0x35A19DC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e4b02b6077879db6](../../evidence/conditions-sets-088.md#c-e4b02b6077879db6) · [状态效果 S-f65b7b07a32f4cf7](../../evidence/state_effects-sets-052.md#s-f65b7b07a32f4cf7)

### path-010249

```text
(exec)# show cts policy-server details active <cr>
```

Handler ` RVA 0x13033940 `；selector ` 43 `；EOL ` RVA 0x35A1AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0164fa2eb0d1fb6e](../../evidence/conditions-sets-001.md#c-0164fa2eb0d1fb6e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010254

```text
(exec)# show cts policy-server details all <cr>
```

Handler ` RVA 0x13033940 `；selector ` 41 `；EOL ` RVA 0x35A1B0C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0164fa2eb0d1fb6e](../../evidence/conditions-sets-001.md#c-0164fa2eb0d1fb6e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011574

```text
(exec)# show cts policy-server details name <string> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 42 `；EOL ` RVA 0x35A1B3B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the server。

[条件 C-0164fa2eb0d1fb6e](../../evidence/conditions-sets-001.md#c-0164fa2eb0d1fb6e) · [参数 P-58c816d50814c6ce](../../evidence/parameters-sets-007.md#p-58c816d50814c6ce) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010246

```text
(exec)# show cts policy-server statistics active <cr>
```

Handler ` RVA 0x13033940 `；selector ` 46 `；EOL ` RVA 0x35A1A5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0164fa2eb0d1fb6e](../../evidence/conditions-sets-001.md#c-0164fa2eb0d1fb6e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010250

```text
(exec)# show cts policy-server statistics all <cr>
```

Handler ` RVA 0x13033940 `；selector ` 44 `；EOL ` RVA 0x35A1A850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0164fa2eb0d1fb6e](../../evidence/conditions-sets-001.md#c-0164fa2eb0d1fb6e) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011572

```text
(exec)# show cts policy-server statistics name <string> <cr>
```

Handler ` RVA 0x13033940 `；selector ` 45 `；EOL ` RVA 0x35A1AB38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the server。

[条件 C-0164fa2eb0d1fb6e](../../evidence/conditions-sets-001.md#c-0164fa2eb0d1fb6e) · [参数 P-a116b3c14ccfdc61](../../evidence/parameters-sets-012.md#p-a116b3c14ccfdc61) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003742

```text
(exec)# show cts provisioning <cr>
```

Handler ` RVA 0x13033940 `；selector ` 13 `；EOL ` RVA 0x35A1BA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43aec3ff669d9c46](../../evidence/conditions-sets-026.md#c-43aec3ff669d9c46) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007603

```text
(exec)# show cts provisioning queue <cr>
```

Handler ` RVA 0x13033940 `；selector ` 14 `；EOL ` RVA 0x35A1BA50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43aec3ff669d9c46](../../evidence/conditions-sets-026.md#c-43aec3ff669d9c46) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003706

```text
(exec)# show cts rbacl <cr>
```

Handler ` RVA 0x13033940 `；selector ` 9 `；EOL ` RVA 0x35A195F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-62fb61bf573908e2](../../evidence/conditions-sets-038.md#c-62fb61bf573908e2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007790

```text
(exec)# show cts role-based counters <cr>
```

Handler ` RVA 0x141F88B0 `；selector ` 2 `；EOL ` RVA 0x35CFC620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dd0541b235be2797](../../evidence/conditions-sets-085.md#c-dd0541b235be2797) · [状态效果 S-9d0c3798ab153054](../../evidence/state_effects-sets-033.md#s-9d0c3798ab153054)

### path-007802

```text
(exec)# show cts role-based permissions <cr>
```

Handler ` RVA 0x141F88B0 `；selector ` 0 `；EOL ` RVA 0x35CFCBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d5a29456eed7d4f6](../../evidence/conditions-sets-082.md#c-d5a29456eed7d4f6) · [状态效果 S-d3aec729134f7d1e](../../evidence/state_effects-sets-045.md#s-d3aec729134f7d1e)

### path-020390

```text
(exec)# show cts role-based sgt-map <prefix:dynamic> <cr>
```

Handler ` RVA 0x1403CDF0 `；selector ` 1 `；EOL ` RVA 0x35CEA118 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Mappings for IPv4 prefix &lt;network&gt;/&lt;length&gt;, e.g., 35.0.0.0/8。

[条件 C-97d5aa5266ec19ca](../../evidence/conditions-sets-059.md#c-97d5aa5266ec19ca) · [缺口 G-577a73092863a6f2](../../evidence/gaps-sets-004.md#g-577a73092863a6f2) · [参数 P-27acb80bb4f9d379](../../evidence/parameters-sets-003.md#p-27acb80bb4f9d379) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010293

```text
(exec)# show cts role-based sgt-map platform <cr>
```

Handler ` RVA 0x1403CDF0 `；selector ` 1 `；EOL ` RVA 0x35CEA118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2a31fa60021cc0c8](../../evidence/conditions-sets-017.md#c-2a31fa60021cc0c8) · [状态效果 S-72454f41440f4873](../../evidence/state_effects-sets-024.md#s-72454f41440f4873)

### path-003660

```text
(exec)# show cts server-list <cr>
```

Handler ` RVA 0x13033940 `；selector ` 7 `；EOL ` RVA 0x35A18F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-959ae2fc3c9026d6](../../evidence/conditions-sets-058.md#c-959ae2fc3c9026d6) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007660

```text
(exec)# show cts sg-epg translations <cr>
```

Handler ` RVA 0x13033940 `；selector ` 20 `；EOL ` RVA 0x35A1C5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13ae14f1a62e50d2](../../evidence/conditions-sets-008.md#c-13ae14f1a62e50d2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010268

```text
(exec)# show cts sg-epg translations all <cr>
```

Handler ` RVA 0x13033940 `；selector ` 23 `；EOL ` RVA 0x35A1C580 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13ae14f1a62e50d2](../../evidence/conditions-sets-008.md#c-13ae14f1a62e50d2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010261

```text
(exec)# show cts sg-epg translations default-epg <cr>
```

Handler ` RVA 0x13033940 `；selector ` 22 `；EOL ` RVA 0x35A1C2D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13ae14f1a62e50d2](../../evidence/conditions-sets-008.md#c-13ae14f1a62e50d2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010255

```text
(exec)# show cts sg-epg translations default-sg <cr>
```

Handler ` RVA 0x13033940 `；selector ` 21 `；EOL ` RVA 0x35A1C030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-13ae14f1a62e50d2](../../evidence/conditions-sets-008.md#c-13ae14f1a62e50d2) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011578

```text
(exec)# show cts sxp ap connections <string> <cr>
```

Handler ` RVA 0x13227830 `；selector ` 34 `；EOL ` RVA 0x35A51B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show SXP connection details by AP name。

[条件 C-356fef1ffabcd302](../../evidence/conditions-sets-021.md#c-356fef1ffabcd302) · [参数 P-69c8548296abda45](../../evidence/parameters-sets-008.md#p-69c8548296abda45) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-011579

```text
(exec)# show cts sxp ap summary <string> <cr>
```

Handler ` RVA 0x13227830 `；selector ` 35 `；EOL ` RVA 0x35A51DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Show SXP summary for the given sxp profile-name。

[条件 C-356fef1ffabcd302](../../evidence/conditions-sets-021.md#c-356fef1ffabcd302) · [参数 P-e2b6b7253722fb32](../../evidence/parameters-sets-017.md#p-e2b6b7253722fb32) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007701

```text
(exec)# show cts sxp connections <cr>
```

Handler ` RVA 0x13227830 `；selector ` 16 `；EOL ` RVA 0x35A50708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a5f1b14f798e455](../../evidence/conditions-sets-041.md#c-6a5f1b14f798e455) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010290

```text
(exec)# show cts sxp connections brief <cr>
```

Handler ` RVA 0x13227830 `；selector ` 17 `；EOL ` RVA 0x35A506E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a5f1b14f798e455](../../evidence/conditions-sets-041.md#c-6a5f1b14f798e455) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007796

```text
(exec)# show cts sxp export-import-group <cr>
```

Handler ` RVA 0x13227830 `；selector ` 49 `；EOL ` RVA 0x35A52718 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1377b5d86c4fb20a](../../evidence/conditions-sets-008.md#c-1377b5d86c4fb20a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007757

```text
(exec)# show cts sxp export-list <cr>
```

Handler ` RVA 0x13227830 `；selector ` 47 `；EOL ` RVA 0x35A520E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1377b5d86c4fb20a](../../evidence/conditions-sets-008.md#c-1377b5d86c4fb20a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007770

```text
(exec)# show cts sxp filter-group <cr>
```

Handler ` RVA 0x13227830 `；selector ` 26 `；EOL ` RVA 0x35A515E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-631d7c26913618f9](../../evidence/conditions-sets-038.md#c-631d7c26913618f9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007715

```text
(exec)# show cts sxp filter-list <cr>
```

Handler ` RVA 0x13227830 `；selector ` 25 `；EOL ` RVA 0x35A51278 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-631d7c26913618f9](../../evidence/conditions-sets-038.md#c-631d7c26913618f9) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007769

```text
(exec)# show cts sxp import-list <cr>
```

Handler ` RVA 0x13227830 `；selector ` 48 `；EOL ` RVA 0x35A523D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1377b5d86c4fb20a](../../evidence/conditions-sets-008.md#c-1377b5d86c4fb20a) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007716

```text
(exec)# show cts sxp sgt-map <cr>
```

Handler ` RVA 0x13227830 `；selector ` 18 `；EOL ` RVA 0x35A50D30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7221598c086721c4](../../evidence/conditions-sets-044.md#c-7221598c086721c4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-010296

```text
(exec)# show cts sxp sgt-map brief <cr>
```

Handler ` RVA 0x13227830 `；selector ` 19 `；EOL ` RVA 0x35A50D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7221598c086721c4](../../evidence/conditions-sets-044.md#c-7221598c086721c4) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-003601

```text
(exec)# show cts transaction-id <cr>
```

Handler ` RVA 0x13033940 `；selector ` 54 `；EOL ` RVA 0x35A17A90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007367

```text
(exec)# show cwmp map hosttable <cr>
```

Handler ` RVA 0x16472800 `；selector ` 13 `；EOL ` RVA 0x35F8CE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007298

```text
(exec)# show cwmp map landevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 6 `；EOL ` RVA 0x35F8BBE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007327

```text
(exec)# show cwmp map lanethernetinterface <cr>
```

Handler ` RVA 0x16472800 `；selector ` 9 `；EOL ` RVA 0x35F8C3D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007349

```text
(exec)# show cwmp map manageddevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 11 `；EOL ` RVA 0x35F8C928 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007337

```text
(exec)# show cwmp map portmapping <cr>
```

Handler ` RVA 0x16472800 `；selector ` 10 `；EOL ` RVA 0x35F8C680 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007357

```text
(exec)# show cwmp map routetable <cr>
```

Handler ` RVA 0x16472800 `；selector ` 12 `；EOL ` RVA 0x35F8CBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

### path-007320

```text
(exec)# show cwmp map wanconnectiondevice <cr>
```

Handler ` RVA 0x16472800 `；selector ` 8 `；EOL ` RVA 0x35F8C130 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-97da42ab13755098](../../evidence/conditions-sets-059.md#c-97da42ab13755098) · [状态效果 S-3b4a970ba630f528](../../evidence/state_effects-sets-013.md#s-3b4a970ba630f528)

