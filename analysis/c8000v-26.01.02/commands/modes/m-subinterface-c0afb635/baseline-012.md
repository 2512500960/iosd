# subinterface · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-069798

```text
(config-subif)# ppp chap matchnames <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 24 `；EOL ` RVA 0x3491C6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e706ab1cc9c5c58b](../../evidence/conditions-sets-089.md#c-e706ab1cc9c5c58b)

### path-071098

```text
(config-subif)# ppp chap password <string> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 12 `；EOL ` RVA 0x3491B8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Default PPP authentication password。

[条件 C-afcc93274bd3ccb6](../../evidence/conditions-sets-068.md#c-afcc93274bd3ccb6) · [参数 P-253b17b811ea9cb9](../../evidence/parameters-sets-003.md#p-253b17b811ea9cb9)

### path-069814

```text
(config-subif)# ppp chap refuse <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 14 `；EOL ` RVA 0x3491BC98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26f6477a32df78f6](../../evidence/conditions-sets-015.md#c-26f6477a32df78f6)

### path-071073

```text
(config-subif)# ppp chap refuse callin <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 15 `；EOL ` RVA 0x3491BCC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-26f6477a32df78f6](../../evidence/conditions-sets-015.md#c-26f6477a32df78f6)

### path-069773

```text
(config-subif)# ppp chap splitnames <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 23 `；EOL ` RVA 0x3491C438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8df8138127f45471](../../evidence/conditions-sets-055.md#c-8df8138127f45471)

### path-069740

```text
(config-subif)# ppp chap wait <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 21 `；EOL ` RVA 0x3491C190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd454823272c21f8](../../evidence/conditions-sets-098.md#c-fd454823272c21f8)

### path-069772

```text
(config-subif)# ppp direction callin <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 20 `；EOL ` RVA 0x3491D9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a3d5445078ce51e](../../evidence/conditions-sets-023.md#c-3a3d5445078ce51e) · [状态效果 S-724169303a0fdafd](../../evidence/state_effects-sets-024.md#s-724169303a0fdafd)

### path-070860

```text
(config-subif)# ppp disconnect-cause keepalive lost-carrier <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 80 `；EOL ` RVA 0x34918200 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d99b2843f88fea2c](../../evidence/conditions-sets-084.md#c-d99b2843f88fea2c) · [状态效果 S-31f1d60337f33658](../../evidence/state_effects-sets-011.md#s-31f1d60337f33658)

### path-069509

```text
(config-subif)# ppp dnis <string> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 78 `；EOL ` RVA 0x34917E78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` DNIS string for this call。

[条件 C-66e99b4627ca9987](../../evidence/conditions-sets-040.md#c-66e99b4627ca9987) · [参数 P-039aeb885dd4cb2a](../../evidence/parameters-sets-001.md#p-039aeb885dd4cb2a)

### path-070957

```text
(config-subif)# ppp eap identity <string> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 33 `；EOL ` RVA 0x34919C28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Alternate EAP Identity。

[条件 C-8d056b146d696f50](../../evidence/conditions-sets-055.md#c-8d056b146d696f50) · [参数 P-43c0dcef2cc9d4cf](../../evidence/parameters-sets-006.md#p-43c0dcef2cc9d4cf)

### path-069676

```text
(config-subif)# ppp eap local <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 31 `；EOL ` RVA 0x3491AAF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071025

```text
(config-subif)# ppp eap password <string> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 34 `；EOL ` RVA 0x34919F70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Default PPP authentication password。

[条件 C-6cd2409e01130911](../../evidence/conditions-sets-042.md#c-6cd2409e01130911) · [参数 P-41a366ad2d54c531](../../evidence/parameters-sets-006.md#p-41a366ad2d54c531)

### path-069725

```text
(config-subif)# ppp eap refuse <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 29 `；EOL ` RVA 0x3491A358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34fc33f59232a301](../../evidence/conditions-sets-021.md#c-34fc33f59232a301)

### path-071000

```text
(config-subif)# ppp eap refuse callin <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 30 `；EOL ` RVA 0x3491A380 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-34fc33f59232a301](../../evidence/conditions-sets-021.md#c-34fc33f59232a301)

### path-069655

```text
(config-subif)# ppp eap wait <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 32 `；EOL ` RVA 0x3491A850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-070970

```text
(config-subif)# ppp encrypt mppe 40 <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 81 `；EOL ` RVA 0x34923A00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ca93f06d23dcc1c1](../../evidence/conditions-sets-078.md#c-ca93f06d23dcc1c1) · [状态效果 S-00bcbf19b949a0dd](../../evidence/state_effects-sets-001.md#s-00bcbf19b949a0dd)

### path-069672

```text
(config-subif)# ppp hostname unique <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 25 `；EOL ` RVA 0x3491D650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-49b29a0bed3a95f2](../../evidence/conditions-sets-029.md#c-49b29a0bed3a95f2)

### path-068461

```text
(config-subif)# ppp ignore-loopback <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 47 `；EOL ` RVA 0x34915958 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f24aa70af8293a94](../../evidence/conditions-sets-094.md#c-f24aa70af8293a94)

### path-069768

```text
(config-subif)# ppp ipcp accept-address <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 58 `；EOL ` RVA 0x3491EAB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071296

```text
(config-subif)# ppp ipcp address accept <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 58 `；EOL ` RVA 0x349218E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071998

```text
(config-subif)# ppp ipcp address no-ip send-ack <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 75 `；EOL ` RVA 0x34921BC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071981

```text
(config-subif)# ppp ipcp address proxy <address> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 61 `；EOL ` RVA 0x349210C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP Address for proxy peer。

[条件 C-67e1ef8e583d1c32](../../evidence/conditions-sets-040.md#c-67e1ef8e583d1c32) · [参数 P-43bb59e311d2d14a](../../evidence/parameters-sets-006.md#p-43bb59e311d2d14a)

### path-071977

```text
(config-subif)# ppp ipcp address request ignore <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 57 `；EOL ` RVA 0x34921650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071232

```text
(config-subif)# ppp ipcp address required <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 74 `；EOL ` RVA 0x34920D50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071254

```text
(config-subif)# ppp ipcp address unique <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 63 `；EOL ` RVA 0x34921340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071158

```text
(config-subif)# ppp ipcp dns reject <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 68 `；EOL ` RVA 0x3491F118 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d6251f1bcbcb8b0](../../evidence/conditions-sets-024.md#c-3d6251f1bcbcb8b0) · [状态效果 S-c34e08c8e40e44b3](../../evidence/state_effects-sets-041.md#s-c34e08c8e40e44b3)

### path-071090

```text
(config-subif)# ppp ipcp header-compression ack <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 70 `；EOL ` RVA 0x3491EDC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-069879

```text
(config-subif)# ppp ipcp ignore-map <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 60 `；EOL ` RVA 0x3491FF00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071187

```text
(config-subif)# ppp ipcp mask request <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 67 `；EOL ` RVA 0x3491FBC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0465da8a8438c2e6](../../evidence/conditions-sets-002.md#c-0465da8a8438c2e6) · [状态效果 S-a0e3aa77622857cf](../../evidence/state_effects-sets-034.md#s-a0e3aa77622857cf)

### path-069987

```text
(config-subif)# ppp ipcp no-renegotiation <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 76 `；EOL ` RVA 0x34921F40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcf02ab73e556676](../../evidence/conditions-sets-098.md#c-fcf02ab73e556676)

### path-069911

```text
(config-subif)# ppp ipcp predictive <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 66 `；EOL ` RVA 0x349204A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071186

```text
(config-subif)# ppp ipcp route default <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 59 `；EOL ` RVA 0x34920210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-069925

```text
(config-subif)# ppp ipcp unique-address <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 63 `；EOL ` RVA 0x34920748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b716b88448fc4a95](../../evidence/conditions-sets-071.md#c-b716b88448fc4a95)

### path-071222

```text
(config-subif)# ppp ipcp username unique <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 65 `；EOL ` RVA 0x34920A58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071175

```text
(config-subif)# ppp ipcp wins reject <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 69 `；EOL ` RVA 0x3491F670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1f856c5e420ed5bc](../../evidence/conditions-sets-012.md#c-1f856c5e420ed5bc) · [状态效果 S-44703e7797039ba6](../../evidence/state_effects-sets-015.md#s-44703e7797039ba6)

### path-070819

```text
(config-subif)# ppp iphc max-header <number:60..168> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 73 `；EOL ` RVA 0x34916F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bytes。

[条件 C-afe1965ef5d3b47d](../../evidence/conditions-sets-068.md#c-afe1965ef5d3b47d) · [参数 P-7cd20fca91b8614e](../../evidence/parameters-sets-010.md#p-7cd20fca91b8614e)

### path-070801

```text
(config-subif)# ppp iphc max-period <number:1..65535> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 71 `；EOL ` RVA 0x349168B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Compressed packets。

[条件 C-70008292228736e7](../../evidence/conditions-sets-043.md#c-70008292228736e7) · [参数 P-4b913d61092da86f](../../evidence/parameters-sets-006.md#p-4b913d61092da86f)

### path-070811

```text
(config-subif)# ppp iphc max-time <number:1..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 72 `；EOL ` RVA 0x34916C08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-c6d6232ce4e04052](../../evidence/conditions-sets-077.md#c-c6d6232ce4e04052) · [参数 P-d1bd46e5053a5408](../../evidence/parameters-sets-016.md#p-d1bd46e5053a5408)

### path-071088

```text
(config-subif)# ppp ipv6cp address unique <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 64 `；EOL ` RVA 0x34922340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-071157

```text
(config-subif)# ppp ipv6cp proxy <address> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 62 `；EOL ` RVA 0x34922670 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IPv6 proxy link-local address。

[条件 C-406d6cf5c135b1ca](../../evidence/conditions-sets-025.md#c-406d6cf5c135b1ca) · [参数 P-2d0f289c0f00407c](../../evidence/parameters-sets-004.md#p-2d0f289c0f00407c)

### path-070797

```text
(config-subif)# ppp lcp delay <number:0..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 40 `；EOL ` RVA 0x34914E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds。

[条件 C-77178d69cdbbb4f2](../../evidence/conditions-sets-046.md#c-77178d69cdbbb4f2) · [参数 P-7fc7d0e921ec9f3c](../../evidence/parameters-sets-010.md#p-7fc7d0e921ec9f3c)

### path-071742

```text
(config-subif)# ppp lcp echo mru verify <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 43 `；EOL ` RVA 0x349152F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-552e1a1a278e3c92](../../evidence/conditions-sets-033.md#c-552e1a1a278e3c92)

### path-069366

```text
(config-subif)# ppp lcp fast-start <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 42 `；EOL ` RVA 0x34914AA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1c369f4f4acc2d9](../../evidence/conditions-sets-062.md#c-a1c369f4f4acc2d9)

### path-069345

```text
(config-subif)# ppp lcp predictive <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 41 `；EOL ` RVA 0x34914800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1c369f4f4acc2d9](../../evidence/conditions-sets-062.md#c-a1c369f4f4acc2d9)

### path-068071

```text
(config-subif)# ppp leased_line_option <number:0..4294967295> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 106 `；EOL ` RVA 0x34911EC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c904839182f1e798](../../evidence/conditions-sets-077.md#c-c904839182f1e798) · [参数 P-05f691280de9c414](../../evidence/parameters-sets-001.md#p-05f691280de9c414)

### path-069840

```text
(config-subif)# ppp link reorders <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 49 `；EOL ` RVA 0x34922D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-069860

```text
(config-subif)# ppp link reset <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 105 `；EOL ` RVA 0x34923028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-069878

```text
(config-subif)# ppp link trap <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 50 `；EOL ` RVA 0x349232D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-069392

```text
(config-subif)# ppp loopback ignore <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 47 `；EOL ` RVA 0x34915C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1c369f4f4acc2d9](../../evidence/conditions-sets-062.md#c-a1c369f4f4acc2d9)

### path-069405

```text
(config-subif)# ppp loopback no-backoff <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 48 `；EOL ` RVA 0x34915F10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1c369f4f4acc2d9](../../evidence/conditions-sets-062.md#c-a1c369f4f4acc2d9)

### path-068078

```text
(config-subif)# ppp max-bad-auth <number:1..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 10 `；EOL ` RVA 0x349129C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of attempts allowed。

[条件 C-b3a414c7001e281d](../../evidence/conditions-sets-069.md#c-b3a414c7001e281d) · [参数 P-dd8fe3506b603707](../../evidence/parameters-sets-017.md#p-dd8fe3506b603707)

### path-068074

```text
(config-subif)# ppp max-configure <number:1..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 2 `；EOL ` RVA 0x34912488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of attempts allowed。

[条件 C-a38347e6e783eb03](../../evidence/conditions-sets-063.md#c-a38347e6e783eb03) · [参数 P-ed0cd11b3eb21abb](../../evidence/parameters-sets-018.md#p-ed0cd11b3eb21abb)

### path-068075

```text
(config-subif)# ppp max-failure <number:1..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 3 `；EOL ` RVA 0x34912728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of attempts allowed。

[条件 C-4c20a0971cbac71f](../../evidence/conditions-sets-030.md#c-4c20a0971cbac71f) · [参数 P-16acfce4096afbb1](../../evidence/parameters-sets-002.md#p-16acfce4096afbb1)

### path-068072

```text
(config-subif)# ppp max-terminate <number:1..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 1 `；EOL ` RVA 0x349121E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of attempts allowed。

[条件 C-63d3d82b0486db5f](../../evidence/conditions-sets-039.md#c-63d3d82b0486db5f) · [参数 P-cb55bcb9e3182ed2](../../evidence/parameters-sets-015.md#p-cb55bcb9e3182ed2)

### path-068475

```text
(config-subif)# ppp microcode <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 104 `；EOL ` RVA 0x34916210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e14a7e5915e8c3dc](../../evidence/conditions-sets-087.md#c-e14a7e5915e8c3dc)

### path-069379

```text
(config-subif)# ppp mru match <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 110 `；EOL ` RVA 0x349156C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ab029a2b0f57032](../../evidence/conditions-sets-004.md#c-0ab029a2b0f57032)

### path-069722

```text
(config-subif)# ppp ms-chap refuse <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 16 `；EOL ` RVA 0x3491CAC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3169a92b6a0ce5bd](../../evidence/conditions-sets-019.md#c-3169a92b6a0ce5bd)

### path-070999

```text
(config-subif)# ppp ms-chap refuse callin <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 17 `；EOL ` RVA 0x3491CAF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3169a92b6a0ce5bd](../../evidence/conditions-sets-019.md#c-3169a92b6a0ce5bd)

### path-069758

```text
(config-subif)# ppp ms-chap-v2 refuse <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 18 `；EOL ` RVA 0x3491D0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-645ac321740c65bf](../../evidence/conditions-sets-039.md#c-645ac321740c65bf)

### path-071024

```text
(config-subif)# ppp ms-chap-v2 refuse callin <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 19 `；EOL ` RVA 0x3491D108 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-645ac321740c65bf](../../evidence/conditions-sets-039.md#c-645ac321740c65bf)

### path-069375

```text
(config-subif)# ppp mtu adaptive <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 44 `；EOL ` RVA 0x34913078 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-09136e7e12055866](../../evidence/conditions-sets-004.md#c-09136e7e12055866)

### path-070651

```text
(config-subif)# ppp mtu pppoe unlimited <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 111 `；EOL ` RVA 0x34913398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8329106527bff5a8](../../evidence/conditions-sets-051.md#c-8329106527bff5a8)

### path-068813

```text
(config-subif)# ppp multilink <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 82 `；EOL ` RVA 0x34936548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fff7872a3df1a2ca](../../evidence/conditions-sets-099.md#c-fff7872a3df1a2ca)

### path-072679

```text
(config-subif)# ppp multilink endpoint mac <interface> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 95 `；EOL ` RVA 0x3493AE38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-746794c9fa64dad2](../../evidence/conditions-sets-045.md#c-746794c9fa64dad2) · [缺口 G-4183057da2826d8f](../../evidence/gaps-sets-003.md#g-4183057da2826d8f) · [参数 P-3ff576775e82e6a8](../../evidence/parameters-sets-005.md#p-3ff576775e82e6a8) · [状态效果 S-135a22e52abeabb1](../../evidence/state_effects-sets-005.md#s-135a22e52abeabb1)

### path-071273

```text
(config-subif)# ppp multilink endpoint none <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 95 `；EOL ` RVA 0x3493AE38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cb4bca522ce7e5a1](../../evidence/conditions-sets-078.md#c-cb4bca522ce7e5a1) · [状态效果 S-5637c9eefefb72a2](../../evidence/state_effects-sets-019.md#s-5637c9eefefb72a2)

### path-072047

```text
(config-subif)# ppp multilink fragment delay <number:0..1000> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 83 `；EOL ` RVA 0x3493D4F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in milliseconds。

[条件 C-e956ddad2dc10db8](../../evidence/conditions-sets-090.md#c-e956ddad2dc10db8) · [参数 P-408ebe26d0408296](../../evidence/parameters-sets-005.md#p-408ebe26d0408296)

### path-071316

```text
(config-subif)# ppp multilink fragment disable <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 94 `；EOL ` RVA 0x3493D1A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f33448aa5852cdab](../../evidence/conditions-sets-094.md#c-f33448aa5852cdab) · [状态效果 S-d9c5063e80f4df04](../../evidence/state_effects-sets-046.md#s-d9c5063e80f4df04)

### path-072021

```text
(config-subif)# ppp multilink fragment maximum 1 <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 94 `；EOL ` RVA 0x3493CEB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-aebd0db6715d5b5d](../../evidence/conditions-sets-068.md#c-aebd0db6715d5b5d) · [状态效果 S-1a4f7b588d8e2c22](../../evidence/state_effects-sets-006.md#s-1a4f7b588d8e2c22)

### path-072001

```text
(config-subif)# ppp multilink fragment size <number:42..65535> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 102 `；EOL ` RVA 0x3493CB28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum fragment size in bytes。

[条件 C-398cba78c6d0cc37](../../evidence/conditions-sets-022.md#c-398cba78c6d0cc37) · [参数 P-dabec36728b0e9a3](../../evidence/parameters-sets-016.md#p-dabec36728b0e9a3)

### path-071294

```text
(config-subif)# ppp multilink fragment-delay <number:1..1000> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 83 `；EOL ` RVA 0x34939348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum delay in milliseconds。

[条件 C-4f2f0f324eb9f2a1](../../evidence/conditions-sets-031.md#c-4f2f0f324eb9f2a1) · [参数 P-40e6f7fb476588f8](../../evidence/parameters-sets-005.md#p-40e6f7fb476588f8)

### path-069965

```text
(config-subif)# ppp multilink fragmentation <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 94 `；EOL ` RVA 0x349395D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d376504d1302cd73](../../evidence/conditions-sets-082.md#c-d376504d1302cd73) · [状态效果 S-e155b3849575953a](../../evidence/state_effects-sets-048.md#s-e155b3849575953a)

### path-072631

```text
(config-subif)# ppp multilink group <number:dynamic> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 99 `；EOL ` RVA 0x3493AAE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Multilink group number。

[条件 C-fa89766555fc9fd7](../../evidence/conditions-sets-097.md#c-fa89766555fc9fd7) · [缺口 G-1880f877b42081f3](../../evidence/gaps-sets-001.md#g-1880f877b42081f3) · [参数 P-32999fcd9f62e0dc](../../evidence/parameters-sets-004.md#p-32999fcd9f62e0dc)

### path-070015

```text
(config-subif)# ppp multilink idle-link <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 87 `；EOL ` RVA 0x3493A490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9dcbd36e6f0cb26](../../evidence/conditions-sets-097.md#c-f9dcbd36e6f0cb26)

### path-070016

```text
(config-subif)# ppp multilink interleave <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 86 `；EOL ` RVA 0x3493A748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9023b0dbadfa200b](../../evidence/conditions-sets-056.md#c-9023b0dbadfa200b)

### path-072678

```text
(config-subif)# ppp multilink links maximum <number:dynamic> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 90 `；EOL ` RVA 0x349399C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Specify maximum desired number of links in a bundle。

[条件 C-5fb8e8320f0f97c1](../../evidence/conditions-sets-037.md#c-5fb8e8320f0f97c1) · [缺口 G-08b4e2d5bcdf8b27](../../evidence/gaps-sets-001.md#g-08b4e2d5bcdf8b27) · [参数 P-14c40c3134303c60](../../evidence/parameters-sets-002.md#p-14c40c3134303c60)

### path-072682

```text
(config-subif)# ppp multilink links minimum <number:dynamic> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 89 `；EOL ` RVA 0x34939CE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Specify minimum desired number of links in a bundle。

[条件 C-271ce42cf4a8abf1](../../evidence/conditions-sets-015.md#c-271ce42cf4a8abf1) · [缺口 G-d07df3666eba5116](../../evidence/gaps-sets-007.md#g-d07df3666eba5116) · [参数 P-588d93860a429414](../../evidence/parameters-sets-007.md#p-588d93860a429414)

### path-071371

```text
(config-subif)# ppp multilink load-threshold <number:1..255> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 88 `；EOL ` RVA 0x3493A0B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Load threshold to add/delete a link。

[条件 C-4719ca06e258bf0d](../../evidence/conditions-sets-028.md#c-4719ca06e258bf0d) · [参数 P-80996adff6a80b67](../../evidence/parameters-sets-010.md#p-80996adff6a80b67)

### path-069964

```text
(config-subif)# ppp multilink mrru local <number:128..16384> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 100 `；EOL ` RVA 0x3493B500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Our MRRU value。

[条件 C-d097d7c86ce7cd44](../../evidence/conditions-sets-080.md#c-d097d7c86ce7cd44) · [参数 P-879783443fc00017](../../evidence/parameters-sets-010.md#p-879783443fc00017)

### path-069982

```text
(config-subif)# ppp multilink mrru remote <number:128..16384> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 101 `；EOL ` RVA 0x3493B568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minimum peer MRRU value。

[条件 C-b6a2a5019f3dd1f5](../../evidence/conditions-sets-071.md#c-b6a2a5019f3dd1f5) · [参数 P-29b11b4343a1ddd5](../../evidence/parameters-sets-004.md#p-29b11b4343a1ddd5)

### path-070054

```text
(config-subif)# ppp multilink multiclass <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 98 `；EOL ` RVA 0x3493BB98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-dedec574334402e2](../../evidence/conditions-sets-086.md#c-dedec574334402e2) · [状态效果 S-7c3bcefa7db43a79](../../evidence/state_effects-sets-026.md#s-7c3bcefa7db43a79)

### path-072683

```text
(config-subif)# ppp multilink multiclass local allow <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 98 `；EOL ` RVA 0x3493BB98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-dedec574334402e2](../../evidence/conditions-sets-086.md#c-dedec574334402e2) · [缺口 G-6c2f42bdc022ce04](../../evidence/gaps-sets-004.md#g-6c2f42bdc022ce04) · [状态效果 S-439cb8c8ef9da978](../../evidence/state_effects-sets-015.md#s-439cb8c8ef9da978)

### path-071969

```text
(config-subif)# ppp multilink ncp sequenced if-needed <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 103 `；EOL ` RVA 0x34938978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-336957520b6be999](../../evidence/conditions-sets-020.md#c-336957520b6be999) · [状态效果 S-9d3e6c0a5b9c4601](../../evidence/state_effects-sets-033.md#s-9d3e6c0a5b9c4601)

### path-071303

```text
(config-subif)# ppp multilink queue depth fifo <number:2..255> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 97 `；EOL ` RVA 0x3493C458 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max queue depth for link。

[条件 C-626ec2a44720ff9d](../../evidence/conditions-sets-038.md#c-626ec2a44720ff9d) · [参数 P-bc19225a5d32d07d](../../evidence/parameters-sets-014.md#p-bc19225a5d32d07d)

### path-071320

```text
(config-subif)# ppp multilink queue depth qos <number:2..255> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 96 `；EOL ` RVA 0x3493C498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max queue depth for link。

[条件 C-5836e91a0ea61f28](../../evidence/conditions-sets-035.md#c-5836e91a0ea61f28) · [参数 P-8728fc87a19a19eb](../../evidence/parameters-sets-010.md#p-8728fc87a19a19eb)

### path-069948

```text
(config-subif)# ppp multilink slippage mru <number:2..32> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 85 `；EOL ` RVA 0x34938CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of units。

[条件 C-ed533bcad24095d9](../../evidence/conditions-sets-092.md#c-ed533bcad24095d9) · [参数 P-a4b2e2d2f3418bf5](../../evidence/parameters-sets-013.md#p-a4b2e2d2f3418bf5)

### path-069957

```text
(config-subif)# ppp multilink slippage msec <number:1..16000> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 84 `；EOL ` RVA 0x34938D48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of milliseconds。

[条件 C-1ca941e36c8efd52](../../evidence/conditions-sets-011.md#c-1ca941e36c8efd52) · [参数 P-36a08252f706169d](../../evidence/parameters-sets-005.md#p-36a08252f706169d)

### path-069907

```text
(config-subif)# ppp ncp passive <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 77 `；EOL ` RVA 0x34922A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-543c8c74a8030f77](../../evidence/conditions-sets-033.md#c-543c8c74a8030f77)

### path-069855

```text
(config-subif)# ppp pap refuse <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 26 `；EOL ` RVA 0x3491E2A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c288fc4952c67326](../../evidence/conditions-sets-075.md#c-c288fc4952c67326)

### path-071116

```text
(config-subif)# ppp pap refuse callin <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 27 `；EOL ` RVA 0x3491E2D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c288fc4952c67326](../../evidence/conditions-sets-075.md#c-c288fc4952c67326)

### path-072323

```text
(config-subif)# ppp pap sent-username <string> password <string> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 11 `；EOL ` RVA 0x3491DE30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Outbound PAP username；` string ` Outbound PAP password。

[条件 C-867d181c2c66e1ec](../../evidence/conditions-sets-052.md#c-867d181c2c66e1ec) · [参数 P-f458bc3633f86f0b](../../evidence/parameters-sets-018.md#p-f458bc3633f86f0b)

### path-069797

```text
(config-subif)# ppp pap wait <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 28 `；EOL ` RVA 0x3491E7A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b9e4ed7df52cf206](../../evidence/conditions-sets-072.md#c-b9e4ed7df52cf206)

### path-070688

```text
(config-subif)# ppp pfc local request <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 54 `；EOL ` RVA 0x349137A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d0d4fed0782e9876](../../evidence/conditions-sets-080.md#c-d0d4fed0782e9876) · [状态效果 S-f563fecd985f4a17](../../evidence/state_effects-sets-052.md#s-f563fecd985f4a17)

### path-070709

```text
(config-subif)# ppp pfc remote apply <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 55 `；EOL ` RVA 0x34913B70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-94811fd504d79379](../../evidence/conditions-sets-057.md#c-94811fd504d79379) · [状态效果 S-03957e763759df28](../../evidence/state_effects-sets-001.md#s-03957e763759df28)

### path-069182

```text
(config-subif)# ppp quality reject <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 0 `；EOL ` RVA 0x34911BA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-868748e7b57927eb](../../evidence/conditions-sets-052.md#c-868748e7b57927eb) · [状态效果 S-827296d227ad90fa](../../evidence/state_effects-sets-028.md#s-827296d227ad90fa)

### path-068481

```text
(config-subif)# ppp reliable-link <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 35 `；EOL ` RVA 0x349164E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c20fd3bac30a830a](../../evidence/conditions-sets-075.md#c-c20fd3bac30a830a)

### path-069960

```text
(config-subif)# ppp timeout aaa <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 39 `；EOL ` RVA 0x34908D60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b4843425e355863](../../evidence/conditions-sets-030.md#c-4b4843425e355863)

### path-068744

```text
(config-subif)# ppp timeout authentication <number:0..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 45 `；EOL ` RVA 0x34908638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-06e2e6d2edbd2dd5](../../evidence/conditions-sets-003.md#c-06e2e6d2edbd2dd5) · [参数 P-9f16c44e8f64d894](../../evidence/parameters-sets-012.md#p-9f16c44e8f64d894)

### path-068806

```text
(config-subif)# ppp timeout bacp <number:1..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 46 `；EOL ` RVA 0x34483DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-394bf2dfabe39c54](../../evidence/conditions-sets-022.md#c-394bf2dfabe39c54) · [参数 P-c8ce10a71921b960](../../evidence/parameters-sets-015.md#p-c8ce10a71921b960)

### path-071311

```text
(config-subif)# ppp timeout idle 0 <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 38 `；EOL ` RVA 0x349090A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1edbafd9055871fd](../../evidence/conditions-sets-012.md#c-1edbafd9055871fd) · [状态效果 S-8ce3f1ac324537b2](../../evidence/state_effects-sets-030.md#s-8ce3f1ac324537b2)

### path-072633

```text
(config-subif)# ppp timeout idle <number:dynamic> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 38 `；EOL ` RVA 0x349090A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Idle timeout value in seconds。

[条件 C-3568105ec94de364](../../evidence/conditions-sets-021.md#c-3568105ec94de364) · [缺口 G-78628df3e2595462](../../evidence/gaps-sets-005.md#g-78628df3e2595462) · [参数 P-bebf77ff390114f9](../../evidence/parameters-sets-014.md#p-bebf77ff390114f9)

### path-071289

```text
(config-subif)# ppp timeout multilink link add <number:1..65535> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 91 `；EOL ` RVA 0x3493D910 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-5f99e78dc83553b9](../../evidence/conditions-sets-037.md#c-5f99e78dc83553b9) · [参数 P-9054b36ed42c27de](../../evidence/parameters-sets-011.md#p-9054b36ed42c27de)

### path-071307

```text
(config-subif)# ppp timeout multilink link remove <number:1..65535> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 92 `；EOL ` RVA 0x3493D978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-faf394a557384243](../../evidence/conditions-sets-097.md#c-faf394a557384243) · [参数 P-364c76959b6ea199](../../evidence/parameters-sets-005.md#p-364c76959b6ea199)

### path-072035

```text
(config-subif)# ppp timeout multilink lost-fragment <number:0..255> <cr>
```

Handler ` RVA 0xFF5C450 `；selector ` 93 `；EOL ` RVA 0x3493DF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeout in seconds。

[条件 C-c30220638c02019c](../../evidence/conditions-sets-075.md#c-c30220638c02019c) · [参数 P-f860c7e0d1cdaacf](../../evidence/parameters-sets-019.md#p-f860c7e0d1cdaacf)

### path-071235

```text
(config-subif)# ppp timeout ncp <number:1..65535> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 5 `；EOL ` RVA 0x349086D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds。

[条件 C-20e6b4bf062a46c3](../../evidence/conditions-sets-013.md#c-20e6b4bf062a46c3) · [参数 P-2a4193f0b33ceb98](../../evidence/parameters-sets-004.md#p-2a4193f0b33ceb98)

### path-071226

```text
(config-subif)# ppp timeout retry <number:0..255> <cr>
```

Handler ` RVA 0xFEAF8B0 `；selector ` 4 `；EOL ` RVA 0x34908340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` seconds。

[条件 C-6d1a148dc5675519](../../evidence/conditions-sets-042.md#c-6d1a148dc5675519) · [参数 P-be4dfacacf1779a8](../../evidence/parameters-sets-014.md#p-be4dfacacf1779a8)

### path-068477

```text
(config-subif)# pppoe enable <cr>
```

Handler ` RVA 0x11C51C40 `；selector ` 1 `；EOL ` RVA 0x356A8AF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5af8e9828b17cfda](../../evidence/conditions-sets-036.md#c-5af8e9828b17cfda)

### path-072570

```text
(config-subif)# pppoe max-sessions <number:dynamic> <cr>
```

Handler ` RVA 0x11C51C40 `；selector ` 4 `；EOL ` RVA 0x356A8F58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum PPPOE sessions。

[条件 C-5e45d4c3f062e660](../../evidence/conditions-sets-037.md#c-5e45d4c3f062e660) · [缺口 G-9a847e3b6a6dfc63](../../evidence/gaps-sets-006.md#g-9a847e3b6a6dfc63) · [参数 P-099bd05fa2450a32](../../evidence/parameters-sets-001.md#p-099bd05fa2450a32)

### path-069723

```text
(config-subif)# pppoe-client dial-pool-number <number:1..255> <cr>
```

Handler ` RVA 0xCBCD230 `；selector ` 3 `；EOL ` RVA 0x33C0B728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Dialer pool number。

[条件 C-21d6d2c3ebe04c45](../../evidence/conditions-sets-013.md#c-21d6d2c3ebe04c45) · [参数 P-62d03db9bcef9b84](../../evidence/parameters-sets-008.md#p-62d03db9bcef9b84) · [状态效果 S-3407c2b3a403ef1f](../../evidence/state_effects-sets-011.md#s-3407c2b3a403ef1f)

### path-072583

```text
(config-subif)# pppoe-client ppp-max-payload <number:dynamic> <cr>
```

Handler ` RVA 0xCBCD230 `；selector ` 12 `；EOL ` RVA 0x33C0BA98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum MRU value to be negotiated during PPP LCP negotiation。

[条件 C-4ed4cf877ed9a56c](../../evidence/conditions-sets-031.md#c-4ed4cf877ed9a56c) · [缺口 G-20d123400eba8218](../../evidence/gaps-sets-002.md#g-20d123400eba8218) · [参数 P-1c7d37fabb043931](../../evidence/parameters-sets-003.md#p-1c7d37fabb043931) · [状态效果 S-3407c2b3a403ef1f](../../evidence/state_effects-sets-011.md#s-3407c2b3a403ef1f)

### path-072569

```text
(config-subif)# pppoe-sessions threshold <number:dynamic> <cr>
```

Handler ` RVA 0x11C51C40 `；selector ` 5 `；EOL ` RVA 0x356A9348 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Per-Interface pppoe session loss threshold。

[条件 C-6a94089ddf7cdebd](../../evidence/conditions-sets-041.md#c-6a94089ddf7cdebd) · [缺口 G-3dbdb0c12b855f30](../../evidence/gaps-sets-003.md#g-3dbdb0c12b855f30) · [参数 P-04aa60fb7674e305](../../evidence/parameters-sets-001.md#p-04aa60fb7674e305)

### path-072253

```text
(config-subif)# pppoe-sessions threshold percent <number:0..100> interval <number:1..65535> <cr>
```

Handler ` RVA 0x11C51C40 `；selector ` 6 `；EOL ` RVA 0x356A9698 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` percentage of sessions to be loss for sending trap；` unsigned_number ` pppoe session loss interval。

[条件 C-8e03261c3d60bc92](../../evidence/conditions-sets-055.md#c-8e03261c3d60bc92) · [参数 P-c894c7b009a216e7](../../evidence/parameters-sets-015.md#p-c894c7b009a216e7)

### path-068632

```text
(config-subif)# pulse-time <number:0..60> <cr>
```

Handler ` RVA 0xED6B800 `；selector ` 0 `；EOL ` RVA 0x3441A790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` DTR low time in seconds。

[条件 C-496ea36e89e45731](../../evidence/conditions-sets-029.md#c-496ea36e89e45731) · [参数 P-602c08df76dcd023](../../evidence/parameters-sets-008.md#p-602c08df76dcd023)

### path-069313

```text
(config-subif)# punt-control cause ipv4-options <cr>
```

Handler ` RVA 0xE751FD0 `；selector ` 0 `；EOL ` RVA 0x34329998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2cc352097deb3d3d](../../evidence/conditions-sets-018.md#c-2cc352097deb3d3d) · [状态效果 S-e76eb4f048c9c4e0](../../evidence/state_effects-sets-049.md#s-e76eb4f048c9c4e0)

### path-068435

```text
(config-subif)# punt-control enable <cr>
```

Handler ` RVA 0xE752430 `；selector ` 0 `；EOL ` RVA 0x34329CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-44724361cd921a8e](../../evidence/conditions-sets-027.md#c-44724361cd921a8e)

### path-068665

```text
(config-subif)# qllc accept-all-calls <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 6 `；EOL ` RVA 0x356C2638 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55ce9376fadb7e09](../../evidence/conditions-sets-034.md#c-55ce9376fadb7e09)

### path-068771

```text
(config-subif)# qllc dlsw <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 8 `；EOL ` RVA 0x356C2D80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-55ce9376fadb7e09](../../evidence/conditions-sets-034.md#c-55ce9376fadb7e09) · [状态效果 S-09863584495f4adf](../../evidence/state_effects-sets-002.md#s-09863584495f4adf)

### path-072700

```text
(config-subif)# qllc dlsw pvc <number:1..4095> <number:1..4095> <?print_action@55558ac17660> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 8 `；EOL ` RVA 0x356C2D80 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Low value for PVC Range；` unsigned_number ` High value for PVC Range。

[条件 C-3a6d2a38b8d35680](../../evidence/conditions-sets-023.md#c-3a6d2a38b8d35680) · [缺口 G-3dd5e7341cf5cc3e](../../evidence/gaps-sets-003.md#g-3dd5e7341cf5cc3e) · [参数 P-c8a37e004d84dab4](../../evidence/parameters-sets-015.md#p-c8a37e004d84dab4) · [状态效果 S-b1fe748013c110e3](../../evidence/state_effects-sets-038.md#s-b1fe748013c110e3)

### path-071077

```text
(config-subif)# qllc largest-packet <address> <number:0..1024> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 4 `；EOL ` RVA 0x356C23D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address mapped to remote x.25 address；` unsigned_number ` largest x.25 packet size accepted on this interface。

[条件 C-c5ee8f59fe09ad1c](../../evidence/conditions-sets-076.md#c-c5ee8f59fe09ad1c) · [参数 P-564b549da65cc47e](../../evidence/parameters-sets-007.md#p-564b549da65cc47e)

### path-069828

```text
(config-subif)# qllc npsi-poll <address> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 7 `；EOL ` RVA 0x356C29C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address mapped to remote x.25 address。

[条件 C-2ceb989570f2464c](../../evidence/conditions-sets-018.md#c-2ceb989570f2464c) · [参数 P-7a7dc9ed815d99ed](../../evidence/parameters-sets-010.md#p-7a7dc9ed815d99ed)

### path-071029

```text
(config-subif)# qllc partner <address> <address> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 1 `；EOL ` RVA 0x356C1CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address mapped to remote x.25 address；` address ` mac address for qllc partner。

[条件 C-54485ded120ee858](../../evidence/conditions-sets-033.md#c-54485ded120ee858) · [参数 P-493d1b50294a49bb](../../evidence/parameters-sets-006.md#p-493d1b50294a49bb)

### path-071838

```text
(config-subif)# qllc sap <address> <number:2..254> <number:2..254> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 5 `；EOL ` RVA 0x356C1930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address mapped to remote x.25 address；` unsigned_number ` Source sap - even value from 0 and FE；` unsigned_number ` Destination sap - even value between 0 and FE。

[条件 C-d157b767b7fc6bd1](../../evidence/conditions-sets-081.md#c-d157b767b7fc6bd1) · [参数 P-0273b9927d3f7396](../../evidence/parameters-sets-001.md#p-0273b9927d3f7396)

### path-071828

```text
(config-subif)# qllc srb <address> <number:1..4095> <number:1..4095> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 0 `；EOL ` RVA 0x356C1558 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address mapped to remote x.25 address；` unsigned_number ` QLLC local ring number - virtual ring number；` unsigned_number ` target ring number - ring group。

[条件 C-a9f65f7bba28d4b7](../../evidence/conditions-sets-066.md#c-a9f65f7bba28d4b7) · [参数 P-23f939c3357763ec](../../evidence/parameters-sets-003.md#p-23f939c3357763ec)

### path-071047

```text
(config-subif)# qllc xid <address> <string> <cr>
```

Handler ` RVA 0x11CBC150 `；selector ` 2 `；EOL ` RVA 0x356C2028 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address mapped to remote x.25 address；` string ` XID (must be 8 digits)。

[条件 C-7f596e28536c2161](../../evidence/conditions-sets-049.md#c-7f596e28536c2161) · [参数 P-8df18ea32c4ead98](../../evidence/parameters-sets-011.md#p-8df18ea32c4ead98)

### path-068703

```text
(config-subif)# qos pre-classify <cr>
```

Handler ` RVA 0x10C407C0 `；selector ` 2 `；EOL ` RVA 0x34CEB308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec1d36f9209cce4f](../../evidence/conditions-sets-091.md#c-ec1d36f9209cce4f)

### path-068704

```text
(config-subif)# qos pre-classify <cr>
```

Handler ` RVA 0x10C407C0 `；selector ` 1 `；EOL ` RVA 0x34CEB588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9dc11e81a1d9f72b](../../evidence/conditions-sets-061.md#c-9dc11e81a1d9f72b)

### path-070278

```text
(config-subif)# radius attribute nas-port-type <number:0..2147483647> <cr>
```

Handler ` RVA 0x11D108B0 `；selector ` 0 `；EOL ` RVA 0x356CEB58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` nas-port-type attribute value。

[条件 C-999218ceed138e63](../../evidence/conditions-sets-059.md#c-999218ceed138e63) · [参数 P-6db53af997106d3a](../../evidence/parameters-sets-009.md#p-6db53af997106d3a)

### path-072513

```text
(config-subif)# rate-limit input <number:8000..2000000000> <number:1000..512000000> <number:2000..1024000000> conform-action drop exceed-action drop <cr>
```

Handler ` RVA 0x10C66C70 `；selector ` 0 `；EOL ` RVA 0x34CED948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bits per second；` unsigned_number ` Normal burst bytes；` unsigned_number ` Maximum burst bytes。

[条件 C-e32c85a3bbb58735](../../evidence/conditions-sets-087.md#c-e32c85a3bbb58735) · [参数 P-c056dca918c1717f](../../evidence/parameters-sets-015.md#p-c056dca918c1717f) · [状态效果 S-e3b30d50cb5d9bce](../../evidence/state_effects-sets-048.md#s-e3b30d50cb5d9bce)

### path-068175

```text
(config-subif)# rbs-zero <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 118 `；EOL ` RVA 0x378BCFF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-643df7e7472f8720](../../evidence/conditions-sets-039.md#c-643df7e7472f8720) · [状态效果 S-8b6eaa235c7fec95](../../evidence/state_effects-sets-030.md#s-8b6eaa235c7fec95)

### path-072593

```text
(config-subif)# rbs-zero nfas-int <number:0..96> <cr>
```

Handler ` RVA 0x1E024080 `；selector ` 118 `；EOL ` RVA 0x378BCFF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` NFAS int value or range。

[条件 C-048dad7fc24d4e43](../../evidence/conditions-sets-002.md#c-048dad7fc24d4e43) · [缺口 G-3e6d653d37adad2e](../../evidence/gaps-sets-003.md#g-3e6d653d37adad2e) · [参数 P-c0c22366c68b03ae](../../evidence/parameters-sets-015.md#p-c0c22366c68b03ae) · [状态效果 S-df60b581825fa122](../../evidence/state_effects-sets-047.md#s-df60b581825fa122)

### path-070749

```text
(config-subif)# redirect to group <string> <cr>
```

Handler ` RVA 0x11AA2550 `；selector ` 0 `；EOL ` RVA 0x355E3508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Server group name。

[条件 C-180aae8d2190a961](../../evidence/conditions-sets-009.md#c-180aae8d2190a961) · [参数 P-4a14dc0562cbc357](../../evidence/parameters-sets-006.md#p-4a14dc0562cbc357) · [状态效果 S-29e40808328c748a](../../evidence/state_effects-sets-009.md#s-29e40808328c748a)

### path-069440

```text
(config-subif)# redundancy asymmetric-routing enable <cr>
```

Handler ` RVA 0xCBE3CE0 `；selector ` 0 `；EOL ` RVA 0x33C164F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d43f5c8449ba90d9](../../evidence/conditions-sets-082.md#c-d43f5c8449ba90d9)

### path-072445

```text
(config-subif)# redundancy gratuitous-arp group <number:1..2> interval sec <number:1..14400> <cr>
```

Handler ` RVA 0xCBE5D40 `；selector ` 0 `；EOL ` RVA 0x33C17228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Redundancy group ID；` unsigned_number ` Gratuitous ARP message interval in seconds。

[条件 C-e48bd03ecf06b331](../../evidence/conditions-sets-088.md#c-e48bd03ecf06b331) · [参数 P-a1b2bce5f350cbbe](../../evidence/parameters-sets-012.md#p-a1b2bce5f350cbbe) · [状态效果 S-fcc7944962ff4822](../../evidence/state_effects-sets-054.md#s-fcc7944962ff4822)

### path-069502

```text
(config-subif)# redundancy group <number:1..2> <cr>
```

Handler ` RVA 0xCBE4C90 `；selector ` 0 `；EOL ` RVA 0x33C16978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RG Group Id。

[条件 C-22dd57987c901a19](../../evidence/conditions-sets-014.md#c-22dd57987c901a19) · [参数 P-78fb8611b342a809](../../evidence/parameters-sets-009.md#p-78fb8611b342a809) · [状态效果 S-93bc89c1b63a2435](../../evidence/state_effects-sets-031.md#s-93bc89c1b63a2435)

### path-072663

```text
(config-subif)# redundancy group <number:1..2> decrement <number:dynamic> <cr>
```

Handler ` RVA 0xCBE4C90 `；selector ` 0 `；EOL ` RVA 0x33C16978 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` RG Group Id；` unsigned_number_dynamic ` decrement value。

[条件 C-c5247b5060079af7](../../evidence/conditions-sets-076.md#c-c5247b5060079af7) · [缺口 G-350f0ec3a59fbc40](../../evidence/gaps-sets-002.md#g-350f0ec3a59fbc40) · [参数 P-1ba4b5b94f2ba1cc](../../evidence/parameters-sets-003.md#p-1ba4b5b94f2ba1cc) · [状态效果 S-9d68296498da600a](../../evidence/state_effects-sets-033.md#s-9d68296498da600a)

### path-069476

```text
(config-subif)# redundancy rii <number:1..65535> <cr>
```

Handler ` RVA 0xCC19140 `；selector ` 0 `；EOL ` RVA 0x33C1E7B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` RII id。

[条件 C-7a75d48eea7315d6](../../evidence/conditions-sets-047.md#c-7a75d48eea7315d6) · [参数 P-699be4e3ad919e1b](../../evidence/parameters-sets-008.md#p-699be4e3ad919e1b)

### path-068383

```text
(config-subif)# ring-speed 4 <cr>
```

Handler ` RVA 0x1240BD40 `；selector ` 0 `；EOL ` RVA 0x35852CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9dc1dcc0863d24e5](../../evidence/conditions-sets-061.md#c-9dc1dcc0863d24e5) · [状态效果 S-637d22c2d78d3e76](../../evidence/state_effects-sets-021.md#s-637d22c2d78d3e76)

### path-068104

```text
(config-subif)# rx-sync-disable <cr>
```

Handler ` RVA 0xED6CD20 `；selector ` 0 `；EOL ` RVA 0x344164A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6158d17a964da9c8](../../evidence/conditions-sets-038.md#c-6158d17a964da9c8)

### path-068047

```text
(config-subif)# sap-priority <number:1..10> <cr>
```

Handler ` RVA 0x1E53CEB0 `；selector ` 0 `；EOL ` RVA 0x355178E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority list number。

[条件 C-2771be7af057184b](../../evidence/conditions-sets-015.md#c-2771be7af057184b) · [参数 P-24b0ee2be0e5bda1](../../evidence/parameters-sets-003.md#p-24b0ee2be0e5bda1)

### path-068069

```text
(config-subif)# scramble <cr>
```

Handler ` RVA 0xED6F530 `；selector ` 1 `；EOL ` RVA 0x344106F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3b051fd8feb6efc0](../../evidence/conditions-sets-023.md#c-3b051fd8feb6efc0)

### path-068176

```text
(config-subif)# sdlc K <number:1..7> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 3 `；EOL ` RVA 0x355037C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Size of local send window。

[条件 C-7ed4be987aefb8d6](../../evidence/conditions-sets-049.md#c-7ed4be987aefb8d6) · [参数 P-c7073276a3ca20f6](../../evidence/parameters-sets-015.md#p-c7073276a3ca20f6)

### path-068170

```text
(config-subif)# sdlc N1 <number:1..4294967295> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 4 `；EOL ` RVA 0x35503280 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Max number of bits for incoming frames。

[条件 C-7fcbaf68ac705cb4](../../evidence/conditions-sets-050.md#c-7fcbaf68ac705cb4) · [参数 P-49c9fdd1c52e0a14](../../evidence/parameters-sets-006.md#p-49c9fdd1c52e0a14)

### path-068172

```text
(config-subif)# sdlc N2 <number:1..255> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 5 `；EOL ` RVA 0x35503520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of times to retry an operation that has timed out。

[条件 C-1bcd458b9326e42c](../../evidence/conditions-sets-011.md#c-1bcd458b9326e42c) · [参数 P-abda68a1e2df2a93](../../evidence/parameters-sets-013.md#p-abda68a1e2df2a93)

### path-068166

```text
(config-subif)# sdlc T1 <number:1..64000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 10 `；EOL ` RVA 0x35502D40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time to wait for a reply to a frame in milliseconds。

[条件 C-1af4365a210e5ab3](../../evidence/conditions-sets-011.md#c-1af4365a210e5ab3) · [参数 P-74e3ff15817955c1](../../evidence/parameters-sets-009.md#p-74e3ff15817955c1)

### path-070019

```text
(config-subif)# sdlc address <number:1..255> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 0 `；EOL ` RVA 0x355043E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC Address in Hex。

[条件 C-eaa57626d5dd0ab3](../../evidence/conditions-sets-091.md#c-eaa57626d5dd0ab3) · [参数 P-7da3518461169434](../../evidence/parameters-sets-010.md#p-7da3518461169434)

### path-068187

```text
(config-subif)# sdlc cts-delay <number:1..64000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 16 `；EOL ` RVA 0x355054D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` delay unit in ucode execution cycles。

[条件 C-dc7ad1f747d15412](../../evidence/conditions-sets-085.md#c-dc7ad1f747d15412) · [参数 P-af43762d9ecdc2da](../../evidence/parameters-sets-013.md#p-af43762d9ecdc2da)

### path-072596

```text
(config-subif)# sdlc dlsw <number:1..254> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 23 `；EOL ` RVA 0x35506B58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` SDLC Address。

[条件 C-e53293a129bc96fb](../../evidence/conditions-sets-088.md#c-e53293a129bc96fb) · [缺口 G-139ac43c3680d9ec](../../evidence/gaps-sets-001.md#g-139ac43c3680d9ec) · [参数 P-b4f3247bd6f8b836](../../evidence/parameters-sets-014.md#p-b4f3247bd6f8b836) · [状态效果 S-5c7dd84c6f79b0ad](../../evidence/state_effects-sets-020.md#s-5c7dd84c6f79b0ad)

### path-070136

```text
(config-subif)# sdlc dlsw default <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 23 `；EOL ` RVA 0x35506B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [状态效果 S-ce2971b75a273434](../../evidence/state_effects-sets-044.md#s-ce2971b75a273434)

### path-068775

```text
(config-subif)# sdlc frmr-disable <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 1 `；EOL ` RVA 0x35504030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e)

### path-070104

```text
(config-subif)# sdlc group-poll <number:1..255> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 25 `；EOL ` RVA 0x35506700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Group Address in Hex。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [参数 P-ebea0dd8584f9d37](../../evidence/parameters-sets-018.md#p-ebea0dd8584f9d37)

### path-068802

```text
(config-subif)# sdlc hdx <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 15 `；EOL ` RVA 0x355054A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e)

### path-070045

```text
(config-subif)# sdlc holdq <number:1..254> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 2 `；EOL ` RVA 0x35504C10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC address for which to specify a queue size。

[条件 C-70a8a5c1076465af](../../evidence/conditions-sets-044.md#c-70a8a5c1076465af) · [参数 P-13fb59d4cca34f05](../../evidence/parameters-sets-002.md#p-13fb59d4cca34f05) · [状态效果 S-cad1034751e513ad](../../evidence/state_effects-sets-043.md#s-cad1034751e513ad)

### path-068184

```text
(config-subif)# sdlc line-speed <number:1200..2000000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 14 `；EOL ` RVA 0x35504B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Clockrate of the interface in bits/sec。

[条件 C-d5b3e57c5b3ee18f](../../evidence/conditions-sets-082.md#c-d5b3e57c5b3ee18f) · [参数 P-d87085d180ae9d6e](../../evidence/parameters-sets-016.md#p-d87085d180ae9d6e)

### path-071451

```text
(config-subif)# sdlc partner <address> <number:1..254> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 27 `；EOL ` RVA 0x355078F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Partners Token Ring MAC address；` unsigned_number ` SDLC address in Hex。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [参数 P-68ae2595f324dd10](../../evidence/parameters-sets-008.md#p-68ae2595f324dd10)

### path-068160

```text
(config-subif)# sdlc poll-limit-value <number:0..10> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 6 `；EOL ` RVA 0x35502800 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Number of times router can poll a secondary station before polling the next station in the poll list。

[条件 C-ff256e8ebe699256](../../evidence/conditions-sets-098.md#c-ff256e8ebe699256) · [参数 P-d73ac7838db7f5c6](../../evidence/parameters-sets-016.md#p-d73ac7838db7f5c6)

### path-068153

```text
(config-subif)# sdlc poll-pause-timer <number:1..10000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 7 `；EOL ` RVA 0x35502240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time between polls for each secondary SDLC station。

[条件 C-5cd0af8c54731f70](../../evidence/conditions-sets-036.md#c-5cd0af8c54731f70) · [参数 P-d7d9a3801eba5f9b](../../evidence/parameters-sets-016.md#p-d7d9a3801eba5f9b)

### path-068168

```text
(config-subif)# sdlc poll-wait-timeout <number:500..64000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 8 `；EOL ` RVA 0x35502FE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Milliseconds。

[条件 C-03add28b99ea3e6b](../../evidence/conditions-sets-002.md#c-03add28b99ea3e6b) · [参数 P-17deee92bd7985bb](../../evidence/parameters-sets-002.md#p-17deee92bd7985bb)

### path-071382

```text
(config-subif)# sdlc qllc-prtnr <address> <number:1..254> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 18 `；EOL ` RVA 0x35505D70 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual mac address mapped to X.121 address；` unsigned_number ` SDLC address in hex。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [参数 P-d08deb892338fca7](../../evidence/parameters-sets-016.md#p-d08deb892338fca7)

### path-068156

```text
(config-subif)# sdlc rnr-limit <number:0..30> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 22 `；EOL ` RVA 0x35502560 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time (in minutes) the router allows its adjacent linkstation to remain in a busy (RNR) state before declaring it inoperative。

[条件 C-e81c50991a5d828a](../../evidence/conditions-sets-090.md#c-e81c50991a5d828a) · [参数 P-2045fa76bb09f254](../../evidence/parameters-sets-003.md#p-2045fa76bb09f254)

### path-069842

```text
(config-subif)# sdlc role primary <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 21 `；EOL ` RVA 0x35501E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0d4930869e03dac0](../../evidence/conditions-sets-005.md#c-0d4930869e03dac0) · [状态效果 S-998a4c4fbcf1d957](../../evidence/state_effects-sets-033.md#s-998a4c4fbcf1d957)

### path-068191

```text
(config-subif)# sdlc rts-timeout <number:1..64000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 17 `；EOL ` RVA 0x35505750 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` timeout unit in ucode execution cycles。

[条件 C-dde0c9a3abda0df0](../../evidence/conditions-sets-085.md#c-dde0c9a3abda0df0) · [参数 P-ca3bccff8c58f3f4](../../evidence/parameters-sets-015.md#p-ca3bccff8c58f3f4)

### path-072069

```text
(config-subif)# sdlc saps <number:1..254> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 28 `；EOL ` RVA 0x35507518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC address in Hex；` unsigned_number ` Source SAP of partner；` unsigned_number ` Destination SAP of partner。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [参数 P-f127c26e5f1c27e3](../../evidence/parameters-sets-018.md#p-f127c26e5f1c27e3)

### path-071454

```text
(config-subif)# sdlc sdlc-largest-frame <number:1..254> <number:0..4294967295> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 29 `；EOL ` RVA 0x35507CD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC station address；` unsigned_number ` Largest I-frame size。

[条件 C-49caa2e7bf71c444](../../evidence/conditions-sets-029.md#c-49caa2e7bf71c444) · [参数 P-4520e46a6f42a643](../../evidence/parameters-sets-006.md#p-4520e46a6f42a643)

### path-070093

```text
(config-subif)# sdlc simultaneous full-datmode <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 19 `；EOL ` RVA 0x355060C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-85c105a07dec0375](../../evidence/conditions-sets-052.md#c-85c105a07dec0375) · [状态效果 S-d62caee3d3730835](../../evidence/state_effects-sets-045.md#s-d62caee3d3730835)

### path-068808

```text
(config-subif)# sdlc slow-poll <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 12 `；EOL ` RVA 0x35505220 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [状态效果 S-cfc2a15ec76c8842](../../evidence/state_effects-sets-044.md#s-cfc2a15ec76c8842)

### path-068163

```text
(config-subif)# sdlc snrm-timer <number:1..64000> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 11 `；EOL ` RVA 0x35502AA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time to wait for a reply to a SNRM frame in milliseconds。

[条件 C-753864f4ae181658](../../evidence/conditions-sets-045.md#c-753864f4ae181658) · [参数 P-1b86187a4a86ce66](../../evidence/parameters-sets-003.md#p-1b86187a4a86ce66)

### path-068832

```text
(config-subif)# sdlc virtual-multidrop <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 20 `；EOL ` RVA 0x355063B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e)

### path-069861

```text
(config-subif)# sdlc vmac <address> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 24 `；EOL ` RVA 0x355022E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual IEEE MAC address。

[条件 C-249504e73f37e464](../../evidence/conditions-sets-014.md#c-249504e73f37e464) · [参数 P-cd9f7cc4afd15d68](../../evidence/parameters-sets-016.md#p-cd9f7cc4afd15d68)

### path-071447

```text
(config-subif)# sdlc xid <number:1..254> <string> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 26 `；EOL ` RVA 0x355070D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC address in Hex；` string ` XID (must be 8 digits)。

[条件 C-48e5e5be5b37f4b1](../../evidence/conditions-sets-029.md#c-48e5e5be5b37f4b1) · [参数 P-660051aa6d42b739](../../evidence/parameters-sets-008.md#p-660051aa6d42b739)

### path-069963

```text
(config-subif)# sdlc xid-pause-timer <number:10..300> <cr>
```

Handler ` RVA 0x114D7430 `；selector ` 9 `；EOL ` RVA 0x35503DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Time in seconds。

[条件 C-a6ec0388f5fdd99e](../../evidence/conditions-sets-064.md#c-a6ec0388f5fdd99e) · [参数 P-61d5d02a157d5973](../../evidence/parameters-sets-008.md#p-61d5d02a157d5973)

### path-071056

```text
(config-subif)# sdllc partner <address> <number:1..254> <cr>
```

Handler ` RVA 0x113C1BF0 `；selector ` 34 `；EOL ` RVA 0x354AEA98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Partners Token Ring MAC address；` unsigned_number ` SDLC address in Hex。

[条件 C-647a97be1510b4a1](../../evidence/conditions-sets-039.md#c-647a97be1510b4a1) · [参数 P-6157022597b517c1](../../evidence/parameters-sets-008.md#p-6157022597b517c1)

### path-069634

```text
(config-subif)# sdllc ring-largest-frame 516 <cr>
```

Handler ` RVA 0x113C1BF0 `；selector ` 32 `；EOL ` RVA 0x354AD9C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19017d21bf160ec4](../../evidence/conditions-sets-010.md#c-19017d21bf160ec4) · [状态效果 S-5cf0064df2bce15e](../../evidence/state_effects-sets-020.md#s-5cf0064df2bce15e)

### path-071833

```text
(config-subif)# sdllc saps <number:1..254> <number:1..255> <number:1..255> <cr>
```

Handler ` RVA 0x113C1BF0 `；selector ` 35 `；EOL ` RVA 0x354AE6E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC address in Hex；` unsigned_number ` Source SAP；` unsigned_number ` Destination SAP。

[条件 C-647a97be1510b4a1](../../evidence/conditions-sets-039.md#c-647a97be1510b4a1) · [参数 P-ca2e6d557e078f6e](../../evidence/parameters-sets-015.md#p-ca2e6d557e078f6e)

### path-070976

```text
(config-subif)# sdllc sdlc-largest-frame <number:1..254> <number:0..4294967295> <cr>
```

Handler ` RVA 0x113C1BF0 `；selector ` 33 `；EOL ` RVA 0x354ADFA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC station address；` unsigned_number ` Largest I-frame size。

[条件 C-62342d09fed34e73](../../evidence/conditions-sets-038.md#c-62342d09fed34e73) · [参数 P-b3c0f4f838895a18](../../evidence/parameters-sets-014.md#p-b3c0f4f838895a18)

### path-072285

```text
(config-subif)# sdllc traddr <address> <number:0..4095> <number:0..15> <number:0..4095> <cr>
```

Handler ` RVA 0x113C1BF0 `；selector ` 30 `；EOL ` RVA 0x354AD5A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Virtual Token Ring MAC address (must end with 00)；` unsigned_number ` SDLLC virtual ring number；` unsigned_number ` SDLLC bridge number；` unsigned_number ` SDLLC target ring number。

[条件 C-49b1a0acac9f0474](../../evidence/conditions-sets-029.md#c-49b1a0acac9f0474) · [参数 P-c5e5fd3029a77229](../../evidence/parameters-sets-015.md#p-c5e5fd3029a77229)

### path-070996

```text
(config-subif)# sdllc xid <number:1..254> <string> <cr>
```

Handler ` RVA 0x113C1BF0 `；selector ` 31 `；EOL ` RVA 0x354AE338 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SDLC address in Hex；` string ` XID (must be 8 digits)。

[条件 C-d39b6e9cc499dbf5](../../evidence/conditions-sets-082.md#c-d39b6e9cc499dbf5) · [参数 P-859e456122dd8329](../../evidence/parameters-sets-010.md#p-859e456122dd8329)

### path-068108

```text
(config-subif)# serial restart-delay <number:0..900> <cr>
```

Handler ` RVA 0xED6CB60 `；selector ` 0 `；EOL ` RVA 0x34416798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Restart delay (seconds)。

[条件 C-f02f618666680f35](../../evidence/conditions-sets-093.md#c-f02f618666680f35) · [参数 P-58abc4f1e5935ade](../../evidence/parameters-sets-007.md#p-58abc4f1e5935ade)

### path-072564

```text
(config-subif)# service instance <number:dynamic> <cr>
```

Handler ` RVA 0xC00B6A0 `；selector ` 1 `；EOL ` RVA 0x33969600 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Service Instance Identifier。

[条件 C-6beb1397d84d7ee7](../../evidence/conditions-sets-042.md#c-6beb1397d84d7ee7) · [缺口 G-8a00a9e1fb96bc3f](../../evidence/gaps-sets-005.md#g-8a00a9e1fb96bc3f) · [参数 P-b404e03066889489](../../evidence/parameters-sets-014.md#p-b404e03066889489)

### path-069697

```text
(config-subif)# service-overlay encap cmd <cr>
```

Handler ` RVA 0x108F3230 `；selector ` 1 `；EOL ` RVA 0x34BF4F00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8805901d6c3cdd2b](../../evidence/conditions-sets-053.md#c-8805901d6c3cdd2b) · [状态效果 S-bbbed3535a3955a0](../../evidence/state_effects-sets-040.md#s-bbbed3535a3955a0)

### path-069208

```text
(config-subif)# service-policy inline input <cr>
```

Handler ` RVA 0xD896300 `；selector ` 0 `；EOL ` RVA 0x33F27748 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b13c836666e8bad](../../evidence/conditions-sets-029.md#c-4b13c836666e8bad) · [状态效果 S-0f6647348b78a532](../../evidence/state_effects-sets-004.md#s-0f6647348b78a532)

### path-069239

```text
(config-subif)# service-policy inline output <cr>
```

Handler ` RVA 0xD896300 `；selector ` 1 `；EOL ` RVA 0x33F279F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b13c836666e8bad](../../evidence/conditions-sets-029.md#c-4b13c836666e8bad) · [状态效果 S-0f6647348b78a532](../../evidence/state_effects-sets-004.md#s-0f6647348b78a532)

### path-072561

```text
(config-subif)# service-policy input <string> <cr>
```

Handler ` RVA 0xD88E820 `；selector ` 0 `；EOL ` RVA 0x33F12CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` policy-map name。

[条件 C-5b2ae002039a9d64](../../evidence/conditions-sets-036.md#c-5b2ae002039a9d64) · [缺口 G-13151bbed42cbef0](../../evidence/gaps-sets-001.md#g-13151bbed42cbef0) · [参数 P-b6f37faf1563c4dc](../../evidence/parameters-sets-014.md#p-b6f37faf1563c4dc) · [状态效果 S-87b24e7a845357a9](../../evidence/state_effects-sets-029.md#s-87b24e7a845357a9)

### path-069174

```text
(config-subif)# service-policy output <string> <cr>
```

Handler ` RVA 0xD88E820 `；selector ` 1 `；EOL ` RVA 0x33F12F68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` policy-map name。

[条件 C-5b2ae002039a9d64](../../evidence/conditions-sets-036.md#c-5b2ae002039a9d64) · [参数 P-f610c8a7327067c8](../../evidence/parameters-sets-018.md#p-f610c8a7327067c8) · [状态效果 S-0f6647348b78a532](../../evidence/state_effects-sets-004.md#s-0f6647348b78a532)

### path-069417

```text
(config-subif)# service-policy type control <cr>
```

Handler ` RVA 0x10A7F1D0 `；selector ` 1 `；EOL ` RVA 0x34C761F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ef5bcfd79eefc4e0](../../evidence/conditions-sets-092.md#c-ef5bcfd79eefc4e0) · [状态效果 S-d9794a9dfa0de016](../../evidence/state_effects-sets-046.md#s-d9794a9dfa0de016)

### path-070715

```text
(config-subif)# service-policy type control default <cr>
```

Handler ` RVA 0x10A7F1D0 `；selector ` 0 `；EOL ` RVA 0x34C75C60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8c2eb6f73991be08](../../evidence/conditions-sets-054.md#c-8c2eb6f73991be08) · [状态效果 S-d9794a9dfa0de016](../../evidence/state_effects-sets-046.md#s-d9794a9dfa0de016)

### path-071674

```text
(config-subif)# service-policy type control default <string> <cr>
```

Handler ` RVA 0x10A7F4F0 `；selector ` 0 `；EOL ` RVA 0x34C75C38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of default control service-policy。

[条件 C-8c2eb6f73991be08](../../evidence/conditions-sets-054.md#c-8c2eb6f73991be08) · [参数 P-4afc259a999b2249](../../evidence/parameters-sets-006.md#p-4afc259a999b2249) · [状态效果 S-d9794a9dfa0de016](../../evidence/state_effects-sets-046.md#s-d9794a9dfa0de016)

### path-072660

```text
(config-subif)# service-policy type control subscriber <?option@5555890f3358> <cr>
```

Handler ` RVA 0xCAE2F10 `；selector ` 1 `；EOL ` RVA 0x33B9F380 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ffe0f9530cff3b04](../../evidence/conditions-sets-099.md#c-ffe0f9530cff3b04) · [缺口 G-c071812ccf4827f9](../../evidence/gaps-sets-007.md#g-c071812ccf4827f9) · [状态效果 S-8bfc182910790e6d](../../evidence/state_effects-sets-030.md#s-8bfc182910790e6d)

### path-068515

```text
(config-subif)# service-routing mdns-sd <cr>
```

Handler ` RVA 0x14308EA0 `；selector ` 2 `；EOL ` RVA 0x35D20590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0bbc7f77129bbfad](../../evidence/conditions-sets-005.md#c-0bbc7f77129bbfad)

### path-068060

```text
(config-subif)# shutdown <cr>
```

Handler ` RVA 0xE40CF20 `；selector ` 0 `；EOL ` RVA 0x34141190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-831bf9460eb13eab](../../evidence/conditions-sets-051.md#c-831bf9460eb13eab)

### path-068114

```text
(config-subif)# site-local-redundancy <cr>
```

Handler ` RVA 0xC64D730 `；selector ` 0 `；EOL ` RVA 0x33AC9B20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a705884f2c49f773](../../evidence/conditions-sets-064.md#c-a705884f2c49f773)

### path-069331

```text
(config-subif)# smds address <address> <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 0 `；EOL ` RVA 0x34B4D630 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` An SMDS address。

[条件 C-c8c0d45e92164bfc](../../evidence/conditions-sets-077.md#c-c8c0d45e92164bfc) · [参数 P-786376b2e947dd81](../../evidence/parameters-sets-009.md#p-786376b2e947dd81)

### path-068414

```text
(config-subif)# smds dxi-mode <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 6 `；EOL ` RVA 0x34B4D8B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1fcfc8fe3edc1bdb](../../evidence/conditions-sets-012.md#c-1fcfc8fe3edc1bdb)

### path-068466

```text
(config-subif)# smds enable-arp <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 1 `；EOL ` RVA 0x34B4ECF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1fcfc8fe3edc1bdb](../../evidence/conditions-sets-012.md#c-1fcfc8fe3edc1bdb)

### path-072566

```text
(config-subif)# smds glean-mode <?protoname_action@55558a0a1bc0> <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 8 `；EOL ` RVA 0x34B4DC58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-74e3aad163bbc1a8](../../evidence/conditions-sets-045.md#c-74e3aad163bbc1a8) · [缺口 G-e6b132afeaed3641](../../evidence/gaps-sets-008.md#g-e6b132afeaed3641)

### path-072819

```text
(config-subif)# smds multicast <?protoname_action@55558a0a26a0> <?protoname_action@55558a0a2700> <address> <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 4 `；EOL ` RVA 0x34B4EA58 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` SMDS address。

[条件 C-1fcfc8fe3edc1bdb](../../evidence/conditions-sets-012.md#c-1fcfc8fe3edc1bdb) · [缺口 G-419bee681ab2746a](../../evidence/gaps-sets-003.md#g-419bee681ab2746a) · [参数 P-3afa0782616c985a](../../evidence/parameters-sets-005.md#p-3afa0782616c985a)

### path-072614

```text
(config-subif)# smds multicast <?protoname_action@55558a0a26a0> <address> <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 4 `；EOL ` RVA 0x34B4E738 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` SMDS address。

[条件 C-1fcfc8fe3edc1bdb](../../evidence/conditions-sets-012.md#c-1fcfc8fe3edc1bdb) · [缺口 G-8fbbad10d2c18a56](../../evidence/gaps-sets-005.md#g-8fbbad10d2c18a56) · [参数 P-0efe21ad68031fef](../../evidence/parameters-sets-002.md#p-0efe21ad68031fef)

### path-068442

```text
(config-subif)# smds nec-mode <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 5 `；EOL ` RVA 0x34B4DF40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1fcfc8fe3edc1bdb](../../evidence/conditions-sets-012.md#c-1fcfc8fe3edc1bdb)

### path-072617

```text
(config-subif)# smds static-map <?protoaddr_action@55558a0a2250> <address> <cr>
```

Handler ` RVA 0x1050F860 `；selector ` 3 `；EOL ` RVA 0x34B4E398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` address ` SMDS address。

[条件 C-194d81f19ef54496](../../evidence/conditions-sets-010.md#c-194d81f19ef54496) · [缺口 G-66ad016ceb672eac](../../evidence/gaps-sets-004.md#g-66ad016ceb672eac) · [参数 P-7cc39ba3345655c5](../../evidence/parameters-sets-010.md#p-7cc39ba3345655c5)

### path-068429

```text
(config-subif)# sna enable-host <cr>
```

Handler ` RVA 0x114FAAD0 `；selector ` 19 `；EOL ` RVA 0x35514940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d42fd2578887d518](../../evidence/conditions-sets-082.md#c-d42fd2578887d518) · [状态效果 S-bba59f9a981c067a](../../evidence/state_effects-sets-040.md#s-bba59f9a981c067a)

### path-069213

```text
(config-subif)# sna start <string> <cr>
```

Handler ` RVA 0x114FAAD0 `；selector ` 18 `；EOL ` RVA 0x35514D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` SNA START Pu Name。

[条件 C-d42fd2578887d518](../../evidence/conditions-sets-082.md#c-d42fd2578887d518) · [参数 P-23ee3aed7870039e](../../evidence/parameters-sets-003.md#p-23ee3aed7870039e)

### path-069949

```text
(config-subif)# snapshot server <number:5..1000> <cr>
```

Handler ` RVA 0x10517960 `；selector ` 0 `；EOL ` RVA 0x34B50510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` duration, in minutes, of each active period。

[条件 C-7073d2f51659b4cb](../../evidence/conditions-sets-043.md#c-7073d2f51659b4cb) · [参数 P-a1fdb05f47359b30](../../evidence/parameters-sets-012.md#p-a1fdb05f47359b30) · [状态效果 S-94b3fea09fac47f5](../../evidence/state_effects-sets-032.md#s-94b3fea09fac47f5)

### path-069573

```text
(config-subif)# snmp ifindex clear <cr>
```

Handler ` RVA 0x104C3B90 `；selector ` 16 `；EOL ` RVA 0x33C3C170 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e0c85ef2433b9c84](../../evidence/conditions-sets-087.md#c-e0c85ef2433b9c84)

### path-069576

```text
(config-subif)# snmp ifindex persist <cr>
```

Handler ` RVA 0x104C3B90 `；selector ` 14 `；EOL ` RVA 0x33C3BF08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec54de05356c7ec7](../../evidence/conditions-sets-091.md#c-ec54de05356c7ec7)

### path-071806

```text
(config-subif)# snmp trap ip verify drop-rate <cr>
```

Handler ` RVA 0xB625B80 `；selector ` 0 `；EOL ` RVA 0x337CA2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c487e962c56d5b20](../../evidence/conditions-sets-076.md#c-c487e962c56d5b20)

### path-069602

```text
(config-subif)# snmp trap isdn-calls <cr>
```

Handler ` RVA 0x161389A0 `；selector ` 2 `；EOL ` RVA 0x35EE21F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-530dfcff0b6edc14](../../evidence/conditions-sets-032.md#c-530dfcff0b6edc14)

### path-069537

```text
(config-subif)# snmp trap link-status <cr>
```

Handler ` RVA 0x104C3B90 `；selector ` 0 `；EOL ` RVA 0x33C3D110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682)

### path-071766

```text
(config-subif)# snmp trap link-status permit duplicates <cr>
```

Handler ` RVA 0x104C3B90 `；selector ` 27 `；EOL ` RVA 0x33C3D150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682)

### path-068625

```text
(config-subif)# source template <cr>
```

Handler ` RVA 0xD6D5B20 `；selector ` 3 `；EOL ` RVA 0x33ED06D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a287947516098c0f](../../evidence/conditions-sets-063.md#c-a287947516098c0f) · [状态效果 S-5a6a2453dfe9835e](../../evidence/state_effects-sets-019.md#s-5a6a2453dfe9835e)

### path-072847

```text
(config-subif)# source-bridge <?params_action_alist@55558a9ff7e0> <?params_action_alist@55558a9ffb88> <?params_action_alist@55558a9ffe30> <?params_action_alist@55558aa000d8> <?params_action_alist@55558aa00380> <?params_action_alist@55558aa00628> max-rd <number:2..8> <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 12 `；EOL ` RVA 0x354AC8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Number of routing descriptors in RIF。

[条件 C-60cb003985976393](../../evidence/conditions-sets-038.md#c-60cb003985976393) · [缺口 G-11b91aa0033c52e9](../../evidence/gaps-sets-001.md#g-11b91aa0033c52e9) · [参数 P-c4c0e7ecb30090da](../../evidence/parameters-sets-015.md#p-c4c0e7ecb30090da)

### path-071059

```text
(config-subif)# source-bridge <number:1..4095> <number:1..15> <number:1..4095> <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 1 `；EOL ` RVA 0x354AD140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Ring number of local interface；` unsigned_number ` Bridge number；` unsigned_number ` Target ring number。

[条件 C-ea44866bab793a6a](../../evidence/conditions-sets-090.md#c-ea44866bab793a6a) · [参数 P-02aea9536d69dd46](../../evidence/parameters-sets-001.md#p-02aea9536d69dd46)

### path-068147

```text
(config-subif)# source-bridge max-hops <number:1..7> <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 11 `；EOL ` RVA 0x354AA940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Hop count。

[条件 C-101a8af2e966a1f3](../../evidence/conditions-sets-006.md#c-101a8af2e966a1f3) · [参数 P-9fa5a1fcf43b05fb](../../evidence/parameters-sets-012.md#p-9fa5a1fcf43b05fb)

### path-068137

```text
(config-subif)# source-bridge max-in-hops <number:1..7> <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 40 `；EOL ` RVA 0x354AA308 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Span input hop count。

[条件 C-eddb24d87af93fd4](../../evidence/conditions-sets-092.md#c-eddb24d87af93fd4) · [参数 P-7914cfe8a996b357](../../evidence/parameters-sets-009.md#p-7914cfe8a996b357)

### path-068143

```text
(config-subif)# source-bridge max-out-hops <number:1..7> <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 39 `；EOL ` RVA 0x354AA6A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Span output hop count。

[条件 C-56c387ab30e525f1](../../evidence/conditions-sets-034.md#c-56c387ab30e525f1) · [参数 P-b8d3b61e2acfcb61](../../evidence/parameters-sets-014.md#p-b8d3b61e2acfcb61)

### path-068688

```text
(config-subif)# source-bridge proxy-explorer <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 16 `；EOL ` RVA 0x354AB518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2fc1b3b93b7a8f15](../../evidence/conditions-sets-019.md#c-2fc1b3b93b7a8f15)

### path-068715

```text
(config-subif)# source-bridge route-cache <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 25 `；EOL ` RVA 0x354AB890 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab0739f115d1674d](../../evidence/conditions-sets-066.md#c-ab0739f115d1674d)

### path-068682

```text
(config-subif)# source-bridge spanning <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 29 `；EOL ` RVA 0x354AAF48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2fc1b3b93b7a8f15](../../evidence/conditions-sets-019.md#c-2fc1b3b93b7a8f15)

### path-072665

```text
(config-subif)# source-bridge trcrf-vlan <number:dynamic> ring-group <number:1..4095> <cr>
```

Handler ` RVA 0x113ACC80 `；selector ` 45 `；EOL ` RVA 0x354AA408 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` CRF Vlan id；` unsigned_number ` CRF Ring number。

[条件 C-caad1c466fc4ae3d](../../evidence/conditions-sets-078.md#c-caad1c466fc4ae3d) · [缺口 G-74f8cee744e4831f](../../evidence/gaps-sets-004.md#g-74f8cee744e4831f) · [参数 P-afb0b8d6c21f513d](../../evidence/parameters-sets-013.md#p-afb0b8d6c21f513d)

### path-068294

```text
(config-subif)# speed 10 <cr>
```

Handler ` RVA 0xE40CD40 `；selector ` 18 `；EOL ` RVA 0x34133BB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-15d74305be3e7307](../../evidence/conditions-sets-009.md#c-15d74305be3e7307) · [状态效果 S-e689d6d6d4b6d62d](../../evidence/state_effects-sets-049.md#s-e689d6d6d4b6d62d)

### path-072528

```text
(config-subif)# standby <number:dynamic> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 255 `；EOL ` RVA 0x33E15F18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-c775199d3ca02cee](../../evidence/conditions-sets-077.md#c-c775199d3ca02cee) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072548

```text
(config-subif)# standby <number:dynamic> authentication <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 22 `；EOL ` RVA 0x33E0F640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-3bbeb98fb42656ef](../../evidence/conditions-sets-023.md#c-3bbeb98fb42656ef) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072552

```text
(config-subif)# standby <number:dynamic> follow <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 29 `；EOL ` RVA 0x33E105D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-339f2a89ef475641](../../evidence/conditions-sets-020.md#c-339f2a89ef475641) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072556

```text
(config-subif)# standby <number:dynamic> ip <cr>
```

Handler ` RVA 0xD33A6E0 `；selector ` 20 `；EOL ` RVA 0x33E19F90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-1a9db35b6f73062b](../../evidence/conditions-sets-010.md#c-1a9db35b6f73062b) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072557

```text
(config-subif)# standby <number:dynamic> ipv6 <cr>
```

Handler ` RVA 0x11397820 `；selector ` 21 `；EOL ` RVA 0x354A2A78 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-ec744f6410e02da2](../../evidence/conditions-sets-091.md#c-ec744f6410e02da2) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072550

```text
(config-subif)# standby <number:dynamic> mac-address <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 28 `；EOL ` RVA 0x33E0FFA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-3a58eb0ab6750eea](../../evidence/conditions-sets-023.md#c-3a58eb0ab6750eea) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072549

```text
(config-subif)# standby <number:dynamic> name <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 27 `；EOL ` RVA 0x33E102C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-43941fe8e832bb2a](../../evidence/conditions-sets-026.md#c-43941fe8e832bb2a) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072554

```text
(config-subif)# standby <number:dynamic> preempt <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 24 `；EOL ` RVA 0x33E11000 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-1f2727cbb39b6bc8](../../evidence/conditions-sets-012.md#c-1f2727cbb39b6bc8) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072553

```text
(config-subif)# standby <number:dynamic> priority <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 23 `；EOL ` RVA 0x33E108E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-53c0408c820cca97](../../evidence/conditions-sets-033.md#c-53c0408c820cca97) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072544

```text
(config-subif)# standby <number:dynamic> timers <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 25 `；EOL ` RVA 0x33E0ECB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number。

[条件 C-1e097356381ca109](../../evidence/conditions-sets-012.md#c-1e097356381ca109) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-34dd22494c43b8ed](../../evidence/parameters-sets-004.md#p-34dd22494c43b8ed) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-072604

```text
(config-subif)# standby <number:dynamic> track <number:1..32767> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 26 `；EOL ` RVA 0x33E0F270 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number；` unsigned_number ` Tracked object number。

[条件 C-f030e5cb950dd898](../../evidence/conditions-sets-093.md#c-f030e5cb950dd898) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-f9dc0c19804abc0d](../../evidence/parameters-sets-019.md#p-f9dc0c19804abc0d) · [状态效果 S-d939cb405db3610c](../../evidence/state_effects-sets-046.md#s-d939cb405db3610c)

### path-072647

```text
(config-subif)# standby <number:dynamic> unicast destination <address> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 30 `；EOL ` RVA 0x33E10CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` group number；` address ` Destination IP address。

[条件 C-b9c0c4cdbabc939c](../../evidence/conditions-sets-072.md#c-b9c0c4cdbabc939c) · [缺口 G-1a6f6eaa4992a50d](../../evidence/gaps-sets-001.md#g-1a6f6eaa4992a50d) · [参数 P-0744de49f28b80e3](../../evidence/parameters-sets-001.md#p-0744de49f28b80e3) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-069037

```text
(config-subif)# standby authentication <string> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 22 `；EOL ` RVA 0x33E0F640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Plain text or Type 6 authentication string。

[条件 C-74549759a94ae307](../../evidence/conditions-sets-045.md#c-74549759a94ae307) · [参数 P-cf61d170f857d36a](../../evidence/parameters-sets-016.md#p-cf61d170f857d36a) · [状态效果 S-2c2e7bd9485a6de4](../../evidence/state_effects-sets-010.md#s-2c2e7bd9485a6de4)

### path-068245

```text
(config-subif)# standby bfd <cr>
```

Handler ` RVA 0xD318790 `；selector ` 13 `；EOL ` RVA 0x33E0E918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3961701b0d0fa3ad](../../evidence/conditions-sets-022.md#c-3961701b0d0fa3ad)

### path-070295

```text
(config-subif)# standby delay minimum <number:0..10000> <cr>
```

Handler ` RVA 0xD318790 `；selector ` 12 `；EOL ` RVA 0x33E0D500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Delay in seconds。

[条件 C-da667c74fe40519a](../../evidence/conditions-sets-084.md#c-da667c74fe40519a) · [参数 P-d333cdc7f19690ff](../../evidence/parameters-sets-016.md#p-d333cdc7f19690ff) · [状态效果 S-e3c548ba8c8fda7f](../../evidence/state_effects-sets-048.md#s-e3c548ba8c8fda7f)

### path-069013

```text
(config-subif)# standby follow <string> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 29 `；EOL ` RVA 0x33E105D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name string (25 chars. max)。

[条件 C-25d7e250cfec8569](../../evidence/conditions-sets-015.md#c-25d7e250cfec8569) · [参数 P-30cdc444452d6b86](../../evidence/parameters-sets-004.md#p-30cdc444452d6b86) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-068309

```text
(config-subif)# standby ip <cr>
```

Handler ` RVA 0xD33A6E0 `；selector ` 20 `；EOL ` RVA 0x33E19F90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3874b5e0afe6a5f9](../../evidence/conditions-sets-022.md#c-3874b5e0afe6a5f9) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-068312

```text
(config-subif)# standby ipv6 <cr>
```

Handler ` RVA 0x11397820 `；selector ` 21 `；EOL ` RVA 0x354A2A78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0f99b4a78ec5b8a1](../../evidence/conditions-sets-006.md#c-0f99b4a78ec5b8a1) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-069003

```text
(config-subif)# standby mac-address <address> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 28 `；EOL ` RVA 0x33E0FFA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` MAC address。

[条件 C-6e62d823186fb604](../../evidence/conditions-sets-043.md#c-6e62d823186fb604) · [参数 P-c2d1c2c0ed3d20d5](../../evidence/parameters-sets-015.md#p-c2d1c2c0ed3d20d5) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-068935

```text
(config-subif)# standby mac-refresh <number:0..255> <cr>
```

Handler ` RVA 0xD3181E0 `；selector ` 1 `；EOL ` RVA 0x33E0DD58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Interval to refresh MAC cache。

[条件 C-191a008774929a0c](../../evidence/conditions-sets-010.md#c-191a008774929a0c) · [参数 P-e5a0d2e60eb341e5](../../evidence/parameters-sets-017.md#p-e5a0d2e60eb341e5)

### path-069002

```text
(config-subif)# standby name <string> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 27 `；EOL ` RVA 0x33E102C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` name string (25 chars. max)。

[条件 C-f6262e0a7240e33d](../../evidence/conditions-sets-095.md#c-f6262e0a7240e33d) · [参数 P-4caa6446e0d437e8](../../evidence/parameters-sets-006.md#p-4caa6446e0d437e8) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-068289

```text
(config-subif)# standby preempt <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 24 `；EOL ` RVA 0x33E11000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-da7480c9a5ba71d7](../../evidence/conditions-sets-084.md#c-da7480c9a5ba71d7) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-068255

```text
(config-subif)# standby redirect <cr>
```

Handler ` RVA 0xD318790 `；selector ` 11 `；EOL ` RVA 0x33E0E0E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b7b0bce3a1a56437](../../evidence/conditions-sets-071.md#c-b7b0bce3a1a56437) · [状态效果 S-c5737636b73387ae](../../evidence/state_effects-sets-042.md#s-c5737636b73387ae)

### path-072815

```text
(config-subif)# standby redirect timers <number:dynamic> <number:dynamic> <cr>
```

Handler ` RVA 0xD318790 `；selector ` 11 `；EOL ` RVA 0x33E0E0E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Passive router advertisement interval in seconds；` unsigned_number_dynamic ` Passive router holddown interval in seconds。

[条件 C-17ba77a688628504](../../evidence/conditions-sets-009.md#c-17ba77a688628504) · [缺口 G-0ee97092da057ef3](../../evidence/gaps-sets-001.md#g-0ee97092da057ef3) · [参数 P-09f213cb3ec169b9](../../evidence/parameters-sets-001.md#p-09f213cb3ec169b9) · [状态效果 S-f6cbd81905452cf1](../../evidence/state_effects-sets-052.md#s-f6cbd81905452cf1)

### path-069017

```text
(config-subif)# standby track <number:1..32767> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 26 `；EOL ` RVA 0x33E0F270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tracked object number。

[条件 C-8893db6f44238f3e](../../evidence/conditions-sets-053.md#c-8893db6f44238f3e) · [参数 P-64958ec2989447dd](../../evidence/parameters-sets-008.md#p-64958ec2989447dd) · [状态效果 S-d939cb405db3610c](../../evidence/state_effects-sets-046.md#s-d939cb405db3610c)

### path-070381

```text
(config-subif)# standby unicast destination <address> <cr>
```

Handler ` RVA 0xD31A220 `；selector ` 30 `；EOL ` RVA 0x33E10CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Destination IP address。

[条件 C-41bc97e8a9cf388e](../../evidence/conditions-sets-026.md#c-41bc97e8a9cf388e) · [参数 P-3fd250f6ac020065](../../evidence/parameters-sets-005.md#p-3fd250f6ac020065) · [状态效果 S-be369793d459601a](../../evidence/state_effects-sets-040.md#s-be369793d459601a)

### path-068231

```text
(config-subif)# standby use-bia <cr>
```

Handler ` RVA 0xD3181E0 `；selector ` 0 `；EOL ` RVA 0x33E0CF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64bb629a6d75997b](../../evidence/conditions-sets-039.md#c-64bb629a6d75997b)

### path-070285

```text
(config-subif)# standby use-bia scope interface <cr>
```

Handler ` RVA 0xD318790 `；selector ` 10 `；EOL ` RVA 0x33E0CF78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-64bb629a6d75997b](../../evidence/conditions-sets-039.md#c-64bb629a6d75997b) · [状态效果 S-174ed375143bca03](../../evidence/state_effects-sets-005.md#s-174ed375143bca03)

### path-068936

```text
(config-subif)# standby version <number:1..2> <cr>
```

Handler ` RVA 0xD318790 `；selector ` 14 `；EOL ` RVA 0x33E0DA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Version number。

[条件 C-07e97c7dac6c98ce](../../evidence/conditions-sets-003.md#c-07e97c7dac6c98ce) · [参数 P-6530fea0ba64c64d](../../evidence/parameters-sets-008.md#p-6530fea0ba64c64d)

### path-068149

```text
(config-subif)# stun group <number:1..255> <cr>
```

Handler ` RVA 0x11535000 `；selector ` 1 `；EOL ` RVA 0x35501398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` A STUN group number。

[条件 C-b8d377a91ea69566](../../evidence/conditions-sets-071.md#c-b8d377a91ea69566) · [参数 P-a6ea9835fbc2c927](../../evidence/parameters-sets-013.md#p-a6ea9835fbc2c927)

### path-071926

```text
(config-subif)# stun proxy-poll address <address> discovery <cr>
```

Handler ` RVA 0x11535000 `；selector ` 0 `；EOL ` RVA 0x35508CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` STUN address。

[条件 C-dd19dac5a6ea36b5](../../evidence/conditions-sets-085.md#c-dd19dac5a6ea36b5) · [参数 P-4f66ccf9e8f7812f](../../evidence/parameters-sets-007.md#p-4f66ccf9e8f7812f) · [状态效果 S-97c6c482d6ecbafc](../../evidence/state_effects-sets-032.md#s-97c6c482d6ecbafc)

### path-072674

```text
(config-subif)# stun route all interface <interface> <cr>
```

Handler ` RVA 0x11535000 `；selector ` 2 `；EOL ` RVA 0x35508388 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-97af859eebb1be90](../../evidence/conditions-sets-059.md#c-97af859eebb1be90) · [缺口 G-4e790a4e347faa5d](../../evidence/gaps-sets-003.md#g-4e790a4e347faa5d) · [参数 P-e82e1229c2b09386](../../evidence/parameters-sets-017.md#p-e82e1229c2b09386) · [状态效果 S-6eb544f2a389f461](../../evidence/state_effects-sets-024.md#s-6eb544f2a389f461)

### path-071927

```text
(config-subif)# stun route all tcp <address> <cr>
```

Handler ` RVA 0x11535000 `；selector ` 2 `；EOL ` RVA 0x35508388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Remote STUN peer's IP address。

[条件 C-1943374b4db8327f](../../evidence/conditions-sets-010.md#c-1943374b4db8327f) · [参数 P-5537d40f9bf710c4](../../evidence/parameters-sets-007.md#p-5537d40f9bf710c4) · [状态效果 S-4a25e50791ab20fb](../../evidence/state_effects-sets-016.md#s-4a25e50791ab20fb)

### path-069843

```text
(config-subif)# stun sdlc-role primary <cr>
```

Handler ` RVA 0x11535000 `；selector ` 4 `；EOL ` RVA 0x35501740 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-167c2b72add59770](../../evidence/conditions-sets-009.md#c-167c2b72add59770) · [状态效果 S-df9e7488d0d96fbb](../../evidence/state_effects-sets-047.md#s-df9e7488d0d96fbb)

### path-068878

```text
(config-subif)# subscriber aging probe <cr>
```

Handler ` RVA 0xCB474C0 `；selector ` 0 `；EOL ` RVA 0x33BDCA30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-93ab66dd3774477c](../../evidence/conditions-sets-057.md#c-93ab66dd3774477c) · [状态效果 S-9baf860a6485e459](../../evidence/state_effects-sets-033.md#s-9baf860a6485e459)

### path-068054

```text
(config-subif)# switchport <cr>
```

Handler ` RVA 0x15DC8870 `；selector ` 0 `；EOL ` RVA 0x35E301C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bbf229d144b0cb74](../../evidence/conditions-sets-073.md#c-bbf229d144b0cb74) · [状态效果 S-8ea34eac77856de5](../../evidence/state_effects-sets-030.md#s-8ea34eac77856de5)

### path-070510

```text
(config-subif)# switchport access vlan <number:1..2349> <cr>
```

Handler ` RVA 0x15C36700 `；selector ` 1 `；EOL ` RVA 0x35DF2218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan Id Range 1。

[条件 C-fa95f2ea5167d399](../../evidence/conditions-sets-097.md#c-fa95f2ea5167d399) · [参数 P-a1a129201cd8d442](../../evidence/parameters-sets-012.md#p-a1a129201cd8d442)

### path-072597

```text
(config-subif)# switchport access vlan <number:dynamic> <cr>
```

Handler ` RVA 0x15DC8870 `；selector ` 0 `；EOL ` RVA 0x35E301C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` VLAN ID of the VLAN when this port is in access mode。

[条件 C-7c36edaf23560cd1](../../evidence/conditions-sets-048.md#c-7c36edaf23560cd1) · [缺口 G-54f7f94a07879219](../../evidence/gaps-sets-003.md#g-54f7f94a07879219) · [参数 P-3495ef6390505e77](../../evidence/parameters-sets-004.md#p-3495ef6390505e77) · [状态效果 S-ac907e1e63c30f43](../../evidence/state_effects-sets-036.md#s-ac907e1e63c30f43)

### path-069121

```text
(config-subif)# switchport mode access <cr>
```

Handler ` RVA 0x15C36700 `；selector ` 0 `；EOL ` RVA 0x35DF1E68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c8280c0ca66157ce](../../evidence/conditions-sets-077.md#c-c8280c0ca66157ce) · [状态效果 S-f011e4579380e2d9](../../evidence/state_effects-sets-051.md#s-f011e4579380e2d9)

### path-068228

```text
(config-subif)# switchport port-security <cr>
```

Handler ` RVA 0x15F4FE70 `；selector ` 0 `；EOL ` RVA 0x35E70500 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-42d9696fbe679cfc](../../evidence/conditions-sets-026.md#c-42d9696fbe679cfc) · [状态效果 S-a34624bbf44d5827](../../evidence/state_effects-sets-035.md#s-a34624bbf44d5827)

### path-068898

```text
(config-subif)# switchport port-security allowlist <cr>
```

Handler ` RVA 0x15F50BE0 `；selector ` 0 `；EOL ` RVA 0x35E70710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-66fed996db8e510b](../../evidence/conditions-sets-040.md#c-66fed996db8e510b) · [状态效果 S-ce6451783d492c20](../../evidence/state_effects-sets-044.md#s-ce6451783d492c20)

### path-072684

```text
(config-subif)# switchport port-security limit rate invalid-source-mac <number:dynamic> <cr>
```

Handler ` RVA 0x15F50BE0 `；selector ` 0 `；EOL ` RVA 0x35E70710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Packets per second。

[条件 C-d7362530bb25cbf0](../../evidence/conditions-sets-083.md#c-d7362530bb25cbf0) · [缺口 G-627826acfe89043c](../../evidence/gaps-sets-004.md#g-627826acfe89043c) · [参数 P-3da26c4882da5a6a](../../evidence/parameters-sets-005.md#p-3da26c4882da5a6a) · [状态效果 S-d4a4d8a65aff11ef](../../evidence/state_effects-sets-045.md#s-d4a4d8a65aff11ef)

### path-072598

```text
(config-subif)# switchport port-security maximum <number:dynamic> <cr>
```

Handler ` RVA 0x15F4FE70 `；selector ` 0 `；EOL ` RVA 0x35E70500 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Maximum addresses。

[条件 C-5530a3f012b1faa9](../../evidence/conditions-sets-033.md#c-5530a3f012b1faa9) · [缺口 G-d4f30bcd310ec49a](../../evidence/gaps-sets-007.md#g-d4f30bcd310ec49a) · [参数 P-53668943729136a6](../../evidence/parameters-sets-007.md#p-53668943729136a6) · [状态效果 S-e68d58e7b1068bd2](../../evidence/state_effects-sets-049.md#s-e68d58e7b1068bd2)

### path-071488

```text
(config-subif)# switchport priority extend cos <number:0..7> <cr>
```

Handler ` RVA 0x15D9E050 `；selector ` 0 `；EOL ` RVA 0x35E359B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Priority for devices on appliance。

[条件 C-58b074de9f8984b6](../../evidence/conditions-sets-035.md#c-58b074de9f8984b6) · [参数 P-debca7d4d138aabb](../../evidence/parameters-sets-017.md#p-debca7d4d138aabb)

### path-070293

```text
(config-subif)# switchport priority extend trust <cr>
```

Handler ` RVA 0x15D9E050 `；selector ` 1 `；EOL ` RVA 0x35E356D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-58b074de9f8984b6](../../evidence/conditions-sets-035.md#c-58b074de9f8984b6)

### path-071649

```text
(config-subif)# switchport trunk allowed vlan all <cr>
```

Handler ` RVA 0x15C36700 `；selector ` 3 `；EOL ` RVA 0x35DF2A10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-50d9b5197eb73f93](../../evidence/conditions-sets-032.md#c-50d9b5197eb73f93) · [状态效果 S-4a8b462b033e81ac](../../evidence/state_effects-sets-016.md#s-4a8b462b033e81ac)

### path-071570

```text
(config-subif)# switchport trunk native vlan <number:1..2349> <cr>
```

Handler ` RVA 0x15C36700 `；selector ` 2 `；EOL ` RVA 0x35DF2640 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Vlan Id Range 1。

[条件 C-bba7dbecfabd427f](../../evidence/conditions-sets-072.md#c-bba7dbecfabd427f) · [参数 P-632f88a8086d7835](../../evidence/parameters-sets-008.md#p-632f88a8086d7835)

### path-070847

```text
(config-subif)# template global inheritance disable <cr>
```

Handler ` RVA 0xD6D9000 `；selector ` 1 `；EOL ` RVA 0x33ED0CF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05fdc74b4ea7e682](../../evidence/conditions-sets-003.md#c-05fdc74b4ea7e682)

### path-069044

```text
(config-subif)# timeout absolute <number:0..518399> <cr>
```

Handler ` RVA 0xDEC3710 `；selector ` 0 `；EOL ` RVA 0x34139EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Session lifetime (in minutes)。

[条件 C-701d66ed3f3a1e96](../../evidence/conditions-sets-043.md#c-701d66ed3f3a1e96) · [参数 P-6fc91786907ba9a2](../../evidence/parameters-sets-009.md#p-6fc91786907ba9a2)

### path-070787

```text
(config-subif)# timeslot <number:0..31> - <number:0..31> <cr>
```

Handler ` RVA 0xED6BE00 `；selector ` 0 `；EOL ` RVA 0x344156E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Timeslots for the G.703 interface；` unsigned_number ` Timeslots for the G.703 interface。

[条件 C-02c3dd9e072f74fa](../../evidence/conditions-sets-002.md#c-02c3dd9e072f74fa) · [参数 P-0de91ee2a743350f](../../evidence/parameters-sets-002.md#p-0de91ee2a743350f)

### path-072535

```text
(config-subif)# topology <?option@5555895340b0> <cr>
```

Handler ` RVA 0xDB71B50 `；selector ` 0 `；EOL ` RVA 0x33FE0218 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a5433032cf45039d](../../evidence/conditions-sets-064.md#c-a5433032cf45039d) · [缺口 G-53ea6b192c9d1094](../../evidence/gaps-sets-003.md#g-53ea6b192c9d1094)

### path-072525

```text
(config-subif)# transmit-interface <interface> <cr>
```

Handler ` RVA 0xE40C8A0 `；selector ` 0 `；EOL ` RVA 0x34131688 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-501082516304e906](../../evidence/conditions-sets-031.md#c-501082516304e906) · [缺口 G-c75dd7404d5412e1](../../evidence/gaps-sets-007.md#g-c75dd7404d5412e1) · [参数 P-e58cb5ebe23b57a5](../../evidence/parameters-sets-017.md#p-e58cb5ebe23b57a5)

### path-068261

```text
(config-subif)# transport-mode lan <cr>
```

Handler ` RVA 0xDFF1980 `；selector ` 0 `；EOL ` RVA 0x34142218 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f71bf64051ad8e60](../../evidence/conditions-sets-095.md#c-f71bf64051ad8e60) · [状态效果 S-a41f19f07247651f](../../evidence/state_effects-sets-035.md#s-a41f19f07247651f)

### path-068181

```text
(config-subif)# trunk-group <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 1 `；EOL ` RVA 0x37904098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-43b3f8e63c9724d9](../../evidence/conditions-sets-026.md#c-43b3f8e63c9724d9)

### path-072844

```text
(config-subif)# trunk-group <string> timeslots <?number_func_nows_action@55558ce58140> <cr>
```

Handler ` RVA 0x1E3BBF00 `；selector ` 1 `；EOL ` RVA 0x37904098 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` Trunk group label。

[条件 C-2a18c5bd9d095fce](../../evidence/conditions-sets-016.md#c-2a18c5bd9d095fce) · [缺口 G-c237e0aa78450ffc](../../evidence/gaps-sets-007.md#g-c237e0aa78450ffc) · [参数 P-c499a03ecdbae284](../../evidence/parameters-sets-015.md#p-c499a03ecdbae284) · [状态效果 S-c7b3d6353e65a581](../../evidence/state_effects-sets-042.md#s-c7b3d6353e65a581)

### path-068099

```text
(config-subif)# ts16 <cr>
```

Handler ` RVA 0xED6BC70 `；selector ` 0 `；EOL ` RVA 0x344161B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3fdaf18f1219327c](../../evidence/conditions-sets-025.md#c-3fdaf18f1219327c)

### path-072627

```text
(config-subif)# tunnel 6rd prefix <prefix:dynamic> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 24 `；EOL ` RVA 0x3482D708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` IPv6 prefix &lt;prefix&gt;/&lt;length&gt;。

[条件 C-59effcf747d6f429](../../evidence/conditions-sets-035.md#c-59effcf747d6f429) · [缺口 G-26abefea172b05cf](../../evidence/gaps-sets-002.md#g-26abefea172b05cf) · [参数 P-2dcd8327c1140084](../../evidence/parameters-sets-004.md#p-2dcd8327c1140084) · [状态效果 S-0f2f7fd0c8fb6524](../../evidence/state_effects-sets-004.md#s-0f2f7fd0c8fb6524)

### path-069802

```text
(config-subif)# tunnel 6rd reverse-map-check <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 24 `；EOL ` RVA 0x3482D708 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8eaa90c3b876c9e0](../../evidence/conditions-sets-055.md#c-8eaa90c3b876c9e0) · [状态效果 S-f9b807df1bad760f](../../evidence/state_effects-sets-053.md#s-f9b807df1bad760f)

### path-070789

```text
(config-subif)# tunnel bandwidth transmit <number:1..10000000> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 3 `；EOL ` RVA 0x3483F450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bandwidth in kilobits。

[条件 C-86d83260fc546010](../../evidence/conditions-sets-052.md#c-86d83260fc546010) · [参数 P-33d6a1fc6060c19e](../../evidence/parameters-sets-004.md#p-33d6a1fc6060c19e) · [状态效果 S-be5eea7400036abb](../../evidence/state_effects-sets-040.md#s-be5eea7400036abb)

### path-068532

```text
(config-subif)# tunnel checksum <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 7 `；EOL ` RVA 0x3482A990 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78acd616c69eab30](../../evidence/conditions-sets-047.md#c-78acd616c69eab30)

### path-069910

```text
(config-subif)# tunnel delete-timer <number:10..60> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 40 `；EOL ` RVA 0x3482FF60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel Endpoint delete timer value in sec。

[条件 C-84e7848071e6e4db](../../evidence/conditions-sets-051.md#c-84e7848071e6e4db) · [参数 P-124998570808d69c](../../evidence/parameters-sets-002.md#p-124998570808d69c)

### path-069472

```text
(config-subif)# tunnel destination dynamic <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 9 `；EOL ` RVA 0x34829CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ad1942a6bf998fe8](../../evidence/conditions-sets-067.md#c-ad1942a6bf998fe8) · [状态效果 S-73fc66bc647bc029](../../evidence/state_effects-sets-025.md#s-73fc66bc647bc029)

### path-069877

```text
(config-subif)# tunnel dst-port <number:0..65535> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 30 `；EOL ` RVA 0x3482F000 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` tunnel destination port number。

[条件 C-3b1bd05455160ab0](../../evidence/conditions-sets-023.md#c-3b1bd05455160ab0) · [参数 P-9e9ae74cd3fedf19](../../evidence/parameters-sets-012.md#p-9e9ae74cd3fedf19)

### path-071901

```text
(config-subif)# tunnel endpoint service-policy output <string> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 28 `；EOL ` RVA 0x3482E8C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` QoS policy-map name。

[条件 C-e8604fe880c35824](../../evidence/conditions-sets-090.md#c-e8604fe880c35824) · [参数 P-7513367b0506a506](../../evidence/parameters-sets-009.md#p-7513367b0506a506)

### path-068492

```text
(config-subif)# tunnel entropy <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 27 `；EOL ` RVA 0x3482A0E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f9c4c8a09979d6ed](../../evidence/conditions-sets-096.md#c-f9c4c8a09979d6ed)

### path-069612

```text
(config-subif)# tunnel flow egress-records <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 17 `；EOL ` RVA 0x3482C7C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4270341e15bb64de](../../evidence/conditions-sets-026.md#c-4270341e15bb64de) · [状态效果 S-2b92ae70b41d7603](../../evidence/state_effects-sets-010.md#s-2b92ae70b41d7603)

### path-068101

```text
(config-subif)# tunnel key <number:0..16777215> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 8 `；EOL ` RVA 0x3482A388 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` key。

[条件 C-793ef74f774c901d](../../evidence/conditions-sets-047.md#c-793ef74f774c901d) · [参数 P-a63f032b3dd1874f](../../evidence/parameters-sets-013.md#p-a63f032b3dd1874f)

### path-068102

```text
(config-subif)# tunnel key <number:0..4294967295> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 8 `；EOL ` RVA 0x348305B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` key。

[条件 C-0eeef786b6cb5c57](../../evidence/conditions-sets-006.md#c-0eeef786b6cb5c57) · [参数 P-57aae4da9d0a5b98](../../evidence/parameters-sets-007.md#p-57aae4da9d0a5b98)

### path-069590

```text
(config-subif)# tunnel metadata src_vpn <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 19 `；EOL ` RVA 0x3482C420 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-51293d00a3209c75](../../evidence/conditions-sets-032.md#c-51293d00a3209c75) · [状态效果 S-6c539e355334c706](../../evidence/state_effects-sets-023.md#s-6c539e355334c706)

### path-072662

```text
(config-subif)# tunnel mode gre <?test_subsys_action@555589d7c780> ipv6 <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 1 `；EOL ` RVA 0x348284C8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-143641e6b39c2c3f](../../evidence/conditions-sets-008.md#c-143641e6b39c2c3f) · [缺口 G-c08448a506032d0e](../../evidence/gaps-sets-007.md#g-c08448a506032d0e) · [状态效果 S-69f8989872049025](../../evidence/state_effects-sets-023.md#s-69f8989872049025)

### path-069456

```text
(config-subif)# tunnel mode ipv6 <cr>
```

Handler ` RVA 0x118CD310 `；selector ` 1 `；EOL ` RVA 0x355A1B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78f9314eccedf3d4](../../evidence/conditions-sets-047.md#c-78f9314eccedf3d4) · [状态效果 S-cb002539241b6649](../../evidence/state_effects-sets-043.md#s-cb002539241b6649)

### path-069568

```text
(config-subif)# tunnel mode ipv6ip <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 1 `；EOL ` RVA 0x355A1FC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd62f1068922b6fe](../../evidence/conditions-sets-098.md#c-fd62f1068922b6fe) · [状态效果 S-d2e6a4c87cb593f9](../../evidence/state_effects-sets-045.md#s-d2e6a4c87cb593f9)

### path-069446

```text
(config-subif)# tunnel mode nos <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 1 `；EOL ` RVA 0x348284C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8248a641359f8c31](../../evidence/conditions-sets-050.md#c-8248a641359f8c31) · [状态效果 S-1f2de2e72e6daebd](../../evidence/state_effects-sets-007.md#s-1f2de2e72e6daebd)

### path-069447

```text
(config-subif)# tunnel mode rbscp <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 1 `；EOL ` RVA 0x3483F070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-78f9314eccedf3d4](../../evidence/conditions-sets-047.md#c-78f9314eccedf3d4) · [状态效果 S-030b70bb2c3dfa44](../../evidence/state_effects-sets-001.md#s-030b70bb2c3dfa44)

### path-068738

```text
(config-subif)# tunnel mpls-ip-only <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 42 `；EOL ` RVA 0x34830230 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d04b9197b6da7bd5](../../evidence/conditions-sets-080.md#c-d04b9197b6da7bd5)

### path-071763

```text
(config-subif)# tunnel network-id <number:1..65535> nexthop <address> <cr>
```

Handler ` RVA 0x1436B860 `；selector ` 0 `；EOL ` RVA 0x35D492E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` network id；` address ` Next Hop Address。

[条件 C-57ae9102c499ed69](../../evidence/conditions-sets-034.md#c-57ae9102c499ed69) · [参数 P-f9085a199401abf6](../../evidence/parameters-sets-019.md#p-f9085a199401abf6)

### path-068599

```text
(config-subif)# tunnel path-mtu-discovery <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 11 `；EOL ` RVA 0x3482B530 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-18c43189de3c0578](../../evidence/conditions-sets-010.md#c-18c43189de3c0578)

### path-070905

```text
(config-subif)# tunnel path-mtu-discovery age-timer <number:10..30> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 12 `；EOL ` RVA 0x3482B248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Aging time。

[条件 C-d258b5f8a7cfa99c](../../evidence/conditions-sets-081.md#c-d258b5f8a7cfa99c) · [参数 P-741a42fd86ee76c0](../../evidence/parameters-sets-009.md#p-741a42fd86ee76c0)

### path-068591

```text
(config-subif)# tunnel path-mtu-discovery min-mtu <number:92..65535> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 13 `；EOL ` RVA 0x3482B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Bytes。

[条件 C-8556ff51c6571390](../../evidence/conditions-sets-052.md#c-8556ff51c6571390) · [参数 P-7dacd93a3166be79](../../evidence/parameters-sets-010.md#p-7dacd93a3166be79)

### path-072577

```text
(config-subif)# tunnel raw-packet-interface <interface> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 15 `；EOL ` RVA 0x3482C0C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4ef1f79ba016115e](../../evidence/conditions-sets-031.md#c-4ef1f79ba016115e) · [缺口 G-ada4c2f16ca15509](../../evidence/gaps-sets-006.md#g-ada4c2f16ca15509) · [参数 P-e9b0c5c37960ded9](../../evidence/parameters-sets-017.md#p-e9b0c5c37960ded9)

### path-069427

```text
(config-subif)# tunnel rbscp delay <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 4 `；EOL ` RVA 0x3483F790 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12aa578f31a1794c](../../evidence/conditions-sets-007.md#c-12aa578f31a1794c) · [状态效果 S-62730a0fb7ff1e57](../../evidence/state_effects-sets-021.md#s-62730a0fb7ff1e57)

### path-072623

```text
(config-subif)# tunnel route-via <interface> preferred <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 22 `；EOL ` RVA 0x3482AD40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-824beb9c0c2f2288](../../evidence/conditions-sets-050.md#c-824beb9c0c2f2288) · [缺口 G-57567797a5b0f6e0](../../evidence/gaps-sets-004.md#g-57567797a5b0f6e0) · [参数 P-5b8d0b5dae63a985](../../evidence/parameters-sets-007.md#p-5b8d0b5dae63a985) · [状态效果 S-54581f4b43f93b1b](../../evidence/state_effects-sets-018.md#s-54581f4b43f93b1b)

### path-068522

```text
(config-subif)# tunnel sequence-datagrams <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 6 `；EOL ` RVA 0x3482A6A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9a4a4f40974cbf9b](../../evidence/conditions-sets-060.md#c-9a4a4f40974cbf9b)

### path-069870

```text
(config-subif)# tunnel snooping enable <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 29 `；EOL ` RVA 0x3482EC80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f62514de0048d84c](../../evidence/conditions-sets-095.md#c-f62514de0048d84c)

### path-072571

```text
(config-subif)# tunnel source <interface> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 10 `；EOL ` RVA 0x34827FD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-c2d91a57be47a099](../../evidence/conditions-sets-075.md#c-c2d91a57be47a099) · [缺口 G-16cb61e64c96e9b7](../../evidence/gaps-sets-001.md#g-16cb61e64c96e9b7) · [参数 P-17f4c15d65d560e6](../../evidence/parameters-sets-002.md#p-17f4c15d65d560e6)

### path-069430

```text
(config-subif)# tunnel source dynamic <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 10 `；EOL ` RVA 0x34827FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-03ec6622ce27f72f](../../evidence/conditions-sets-002.md#c-03ec6622ce27f72f) · [状态效果 S-ecaaed7d25678885](../../evidence/state_effects-sets-050.md#s-ecaaed7d25678885)

### path-069822

```text
(config-subif)# tunnel src-mac-address <address> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 26 `；EOL ` RVA 0x3482E4E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` Mac address。

[条件 C-93ca2ad27bab412f](../../evidence/conditions-sets-057.md#c-93ca2ad27bab412f) · [参数 P-2190f7d1691cef58](../../evidence/parameters-sets-003.md#p-2190f7d1691cef58)

### path-069894

```text
(config-subif)# tunnel src-port <number:0..65535> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 31 `；EOL ` RVA 0x3482F430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel Source port number。

[条件 C-4bb3cc41e2ffdf72](../../evidence/conditions-sets-030.md#c-4bb3cc41e2ffdf72) · [参数 P-2141f1c6e59011d6](../../evidence/parameters-sets-003.md#p-2141f1c6e59011d6)

### path-068140

```text
(config-subif)# tunnel tos <number:0..255> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 20 `；EOL ` RVA 0x3482CA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` tos。

[条件 C-0de917aa6e21e2a2](../../evidence/conditions-sets-006.md#c-0de917aa6e21e2a2) · [参数 P-700b2721d882b42f](../../evidence/parameters-sets-009.md#p-700b2721d882b42f)

### path-068145

```text
(config-subif)# tunnel ttl <number:1..255> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 18 `；EOL ` RVA 0x3482CD40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` ttl。

[条件 C-84f0fa36f627fbea](../../evidence/conditions-sets-051.md#c-84f0fa36f627fbea) · [参数 P-096655996def9448](../../evidence/parameters-sets-001.md#p-096655996def9448)

### path-069617

```text
(config-subif)# tunnel udlr address-resolution <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 14 `；EOL ` RVA 0x3482BC00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d7b7643f419b846b](../../evidence/conditions-sets-083.md#c-d7b7643f419b846b) · [状态效果 S-0197fc3e730e659a](../../evidence/state_effects-sets-001.md#s-0197fc3e730e659a)

### path-072625

```text
(config-subif)# tunnel udlr send-only <interface> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 14 `；EOL ` RVA 0x3482BC00 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e869b9f7a101438d](../../evidence/conditions-sets-090.md#c-e869b9f7a101438d) · [缺口 G-513ad4388bd918f4](../../evidence/gaps-sets-003.md#g-513ad4388bd918f4) · [参数 P-3bf92a11a6b1d1de](../../evidence/parameters-sets-005.md#p-3bf92a11a6b1d1de) · [状态效果 S-2612145086ef834a](../../evidence/state_effects-sets-009.md#s-2612145086ef834a)

### path-071920

```text
(config-subif)# tunnel vlan <number:1..4094> - <number:1..4094> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 25 `；EOL ` RVA 0x3482DED0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` vlan-id；` unsigned_number ` vlan id。

[条件 C-4e18979b24f8666e](../../evidence/conditions-sets-031.md#c-4e18979b24f8666e) · [参数 P-08ec5241fb7d9490](../../evidence/parameters-sets-001.md#p-08ec5241fb7d9490) · [状态效果 S-4910984817153ce6](../../evidence/state_effects-sets-016.md#s-4910984817153ce6)

### path-072592

```text
(config-subif)# tunnel vlan <number:1..4094> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 25 `；EOL ` RVA 0x3482DED0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` vlan-id。

[条件 C-fa0bb1c7b1113ab4](../../evidence/conditions-sets-097.md#c-fa0bb1c7b1113ab4) · [缺口 G-e57456554a76f7f2](../../evidence/gaps-sets-008.md#g-e57456554a76f7f2) · [参数 P-625148c77a64a74f](../../evidence/parameters-sets-008.md#p-625148c77a64a74f) · [状态效果 S-194726f8ec1098da](../../evidence/state_effects-sets-006.md#s-194726f8ec1098da)

### path-069700

```text
(config-subif)# tunnel vrf multiplexing <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 21 `；EOL ` RVA 0x3482D100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-023394b820932175](../../evidence/conditions-sets-001.md#c-023394b820932175) · [状态效果 S-15850ad94f3407aa](../../evidence/state_effects-sets-005.md#s-15850ad94f3407aa)

### path-071948

```text
(config-subif)# tunnel vxlan source-port-range <number:1..65535> <number:1..65535> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 41 `；EOL ` RVA 0x3482FBB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel vxlan source port number start；` unsigned_number ` Tunnel vxlan source port number end。

[条件 C-4da01a18129c6e9b](../../evidence/conditions-sets-030.md#c-4da01a18129c6e9b) · [参数 P-0725b843606366e5](../../evidence/parameters-sets-001.md#p-0725b843606366e5)

### path-071197

```text
(config-subif)# tunnel vxlan vni <number:1..16777215> <cr>
```

Handler ` RVA 0xFB8B1A0 `；selector ` 32 `；EOL ` RVA 0x3482F888 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Tunnel vxlan network identifier number。

[条件 C-8ff59e359f9cb95c](../../evidence/conditions-sets-056.md#c-8ff59e359f9cb95c) · [参数 P-573eb5901c48d899](../../evidence/parameters-sets-007.md#p-573eb5901c48d899)

### path-072527

```text
(config-subif)# tx-queue-limit <number:dynamic> <cr>
```

Handler ` RVA 0xE408D30 `；selector ` 0 `；EOL ` RVA 0x341432D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number (queue limit)。

[条件 C-a59b94ed349b265d](../../evidence/conditions-sets-064.md#c-a59b94ed349b265d) · [缺口 G-1df186d21e2abc9e](../../evidence/gaps-sets-002.md#g-1df186d21e2abc9e) · [参数 P-3c9efa37850eafbe](../../evidence/parameters-sets-005.md#p-3c9efa37850eafbe)

### path-068061

```text
(config-subif)# tx-ring-limit <cr>
```

Handler ` RVA 0xE408D80 `；selector ` 0 `；EOL ` RVA 0x34143728 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-146527d5c757d04d](../../evidence/conditions-sets-008.md#c-146527d5c757d04d)

### path-072526

```text
(config-subif)# tx-ring-limit <number:dynamic> <cr>
```

Handler ` RVA 0xE408D80 `；selector ` 0 `；EOL ` RVA 0x34143728 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Number (ring limit)。

[条件 C-b5a512ec50eace7d](../../evidence/conditions-sets-070.md#c-b5a512ec50eace7d) · [缺口 G-088091411cea6911](../../evidence/gaps-sets-001.md#g-088091411cea6911) · [参数 P-c254e12c08af3cc4](../../evidence/parameters-sets-015.md#p-c254e12c08af3cc4)

### path-068089

```text
(config-subif)# vlan-autoconfig <cr>
```

Handler ` RVA 0x112B68E0 `；selector ` 15 `；EOL ` RVA 0x3544DAE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63ab743f834d9602](../../evidence/conditions-sets-039.md#c-63ab743f834d9602)

### path-069343

```text
(config-subif)# vlan-autoconfig protocol any <cr>
```

Handler ` RVA 0x112B68E0 `；selector ` 13 `；EOL ` RVA 0x3544DB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63ab743f834d9602](../../evidence/conditions-sets-039.md#c-63ab743f834d9602)

### path-069365

```text
(config-subif)# vlan-autoconfig protocol dhcpv6iapd <cr>
```

Handler ` RVA 0x112B68E0 `；selector ` 14 `；EOL ` RVA 0x3544DDC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-63ab743f834d9602](../../evidence/conditions-sets-039.md#c-63ab743f834d9602)

### path-069429

```text
(config-subif)# vlan-id dot1q <number:1..4094> <cr>
```

Handler ` RVA 0x11D3A4F0 `；selector ` 4 `；EOL ` RVA 0x356D3C50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` VLAN ID。

[条件 C-2806199de3b15088](../../evidence/conditions-sets-016.md#c-2806199de3b15088) · [参数 P-fbc9c065375e7fa2](../../evidence/parameters-sets-019.md#p-fbc9c065375e7fa2)

### path-072618

```text
(config-subif)# vlan-range dot1q <number:1..4094> <number:dynamic> <cr>
```

Handler ` RVA 0x11D3A4F0 `；selector ` 1 `；EOL ` RVA 0x356D38A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` First VLAN ID in range；` unsigned_number_dynamic ` Last VLAN ID in range。

[条件 C-e106ca97a1bc2c32](../../evidence/conditions-sets-087.md#c-e106ca97a1bc2c32) · [缺口 G-6112de7c8c6c883d](../../evidence/gaps-sets-004.md#g-6112de7c8c6c883d) · [参数 P-4f96934543fd9490](../../evidence/parameters-sets-007.md#p-4f96934543fd9490)

### path-068416

```text
(config-subif)# vnet global <cr>
```

Handler ` RVA 0x124676B0 `；selector ` 0 `；EOL ` RVA 0x358750C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5915076baa417510](../../evidence/conditions-sets-035.md#c-5915076baa417510) · [状态效果 S-9ed1b8b65af87eb9](../../evidence/state_effects-sets-034.md#s-9ed1b8b65af87eb9)

### path-072565

```text
(config-subif)# vnet name <string> <cr>
```

Handler ` RVA 0x124676B0 `；selector ` 0 `；EOL ` RVA 0x358750C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-cd687b2819f02598](../../evidence/conditions-sets-079.md#c-cd687b2819f02598) · [缺口 G-abb7442f06d41e1f](../../evidence/gaps-sets-006.md#g-abb7442f06d41e1f) · [参数 P-9b785f9b3c8a015e](../../evidence/parameters-sets-012.md#p-9b785f9b3c8a015e) · [状态效果 S-439db06df411fa59](../../evidence/state_effects-sets-015.md#s-439db06df411fa59)

### path-068226

```text
(config-subif)# vnet trunk <cr>
```

Handler ` RVA 0x124666E0 `；selector ` 0 `；EOL ` RVA 0x358749C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1e949dc24ca49059](../../evidence/conditions-sets-012.md#c-1e949dc24ca49059)

### path-072600

```text
(config-subif)# vnet trunk list <string> <cr>
```

Handler ` RVA 0x124666E0 `；selector ` 0 `；EOL ` RVA 0x358749C0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF list name。

[条件 C-6a4fa9968d32a270](../../evidence/conditions-sets-041.md#c-6a4fa9968d32a270) · [缺口 G-40be24e3fe927d07](../../evidence/gaps-sets-003.md#g-40be24e3fe927d07) · [参数 P-665cfe39c68927c7](../../evidence/parameters-sets-008.md#p-665cfe39c68927c7) · [状态效果 S-63621f01836a19af](../../evidence/state_effects-sets-021.md#s-63621f01836a19af)

### path-072723

```text
(config-subif)# vpdn authorization <cr>
```

Handler ` RVA 0x11DBA550 `；selector ` 0 `；EOL ` RVA 0x356FAA18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e2c9753faaa40037](../../evidence/conditions-sets-087.md#c-e2c9753faaa40037) · [缺口 G-de89506b318a71ad](../../evidence/gaps-sets-008.md#g-de89506b318a71ad) · [状态效果 S-c2ad5e519dff6f16](../../evidence/state_effects-sets-041.md#s-c2ad5e519dff6f16)

### path-068915

```text
(config-subif)# vpdn template <string> <cr>
```

Handler ` RVA 0x11DBA550 `；selector ` 1 `；EOL ` RVA 0x356FAE78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VPDN template name.。

[条件 C-4db9b5645b5ab31d](../../evidence/conditions-sets-030.md#c-4db9b5645b5ab31d) · [参数 P-814b9029693cd884](../../evidence/parameters-sets-010.md#p-814b9029693cd884)

### path-068925

```text
(config-subif)# vrf autoclassify source <cr>
```

Handler ` RVA 0xCFD7910 `；selector ` 0 `；EOL ` RVA 0x33D77620 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e25317a5c051faaa](../../evidence/conditions-sets-087.md#c-e25317a5c051faaa) · [状态效果 S-bc38510d57dc114f](../../evidence/state_effects-sets-040.md#s-bc38510d57dc114f)

### path-072541

```text
(config-subif)# vrf forwarding <string> <cr>
```

Handler ` RVA 0xDC46EA0 `；selector ` 0 `；EOL ` RVA 0x34013398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-44a9f45d95f8bbe8](../../evidence/conditions-sets-027.md#c-44a9f45d95f8bbe8) · [缺口 G-01d4b7803ba3e918](../../evidence/gaps-sets-001.md#g-01d4b7803ba3e918) · [参数 P-0433dd3edc314881](../../evidence/parameters-sets-001.md#p-0433dd3edc314881) · [状态效果 S-82774f1d43f35167](../../evidence/state_effects-sets-028.md#s-82774f1d43f35167)

### path-068937

```text
(config-subif)# vrf receive <string> <cr>
```

Handler ` RVA 0xFADE850 `；selector ` 1 `；EOL ` RVA 0x34807A30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Table name。

[条件 C-e25317a5c051faaa](../../evidence/conditions-sets-087.md#c-e25317a5c051faaa) · [参数 P-461a4dfaf2c49eb5](../../evidence/parameters-sets-006.md#p-461a4dfaf2c49eb5) · [状态效果 S-ec0d813e95b29a40](../../evidence/state_effects-sets-050.md#s-ec0d813e95b29a40)

### path-068928

```text
(config-subif)# vrf select source <cr>
```

Handler ` RVA 0xFADE850 `；selector ` 0 `；EOL ` RVA 0x34807730 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e25317a5c051faaa](../../evidence/conditions-sets-087.md#c-e25317a5c051faaa) · [状态效果 S-ec0d813e95b29a40](../../evidence/state_effects-sets-050.md#s-ec0d813e95b29a40)

### path-068916

```text
(config-subif)# vrf sitemap <string> <cr>
```

Handler ` RVA 0xDC2A990 `；selector ` 1 `；EOL ` RVA 0x34013BE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the route-map。

[条件 C-9c7fd36e1b27c635](../../evidence/conditions-sets-060.md#c-9c7fd36e1b27c635) · [参数 P-481002911548a307](../../evidence/parameters-sets-006.md#p-481002911548a307) · [状态效果 S-ec0d813e95b29a40](../../evidence/state_effects-sets-050.md#s-ec0d813e95b29a40)

### path-072724

```text
(config-subif)# vrrp <number:1..255> <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 9 `；EOL ` RVA 0x3429B668 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-abdb761146228515](../../evidence/conditions-sets-066.md#c-abdb761146228515) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-070678

```text
(config-subif)# vrrp <number:1..255> address-family ipv4 <cr>
```

Handler ` RVA 0x133C8130 `；selector ` 0 `；EOL ` RVA 0x35A7EE58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Group number for this VRRP context。

[条件 C-efcb46d32ab11380](../../evidence/conditions-sets-093.md#c-efcb46d32ab11380) · [参数 P-ccb711003e1599e2](../../evidence/parameters-sets-016.md#p-ccb711003e1599e2) · [状态效果 S-b5da9b5384376156](../../evidence/state_effects-sets-038.md#s-b5da9b5384376156)

### path-072744

```text
(config-subif)# vrrp <number:1..255> authentication <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 2 `；EOL ` RVA 0x34299708 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-98380049f90f530d](../../evidence/conditions-sets-059.md#c-98380049f90f530d) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072745

```text
(config-subif)# vrrp <number:1..255> description <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 10 `；EOL ` RVA 0x3429A1F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-e8262dca95c66d5e](../../evidence/conditions-sets-090.md#c-e8262dca95c66d5e) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072785

```text
(config-subif)# vrrp <number:1..255> ip <address> <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 3 `；EOL ` RVA 0x34299BA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number；` address ` VRRP group IP address。

[条件 C-ec9a68fb3a344190](../../evidence/conditions-sets-091.md#c-ec9a68fb3a344190) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-dca4766efe7a1d89](../../evidence/parameters-sets-017.md#p-dca4766efe7a1d89) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072746

```text
(config-subif)# vrrp <number:1..255> name <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 13 `；EOL ` RVA 0x34299EA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-61b9c93f42512b9b](../../evidence/conditions-sets-038.md#c-61b9c93f42512b9b) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072748

```text
(config-subif)# vrrp <number:1..255> preempt <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 5 `；EOL ` RVA 0x3429A508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-ec9a68fb3a344190](../../evidence/conditions-sets-091.md#c-ec9a68fb3a344190) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072749

```text
(config-subif)# vrrp <number:1..255> priority <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 6 `；EOL ` RVA 0x3429A8E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-7dfc7dfcb83d552c](../../evidence/conditions-sets-049.md#c-7dfc7dfcb83d552c) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072750

```text
(config-subif)# vrrp <number:1..255> shutdown <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 12 `；EOL ` RVA 0x3429B390 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-ec9a68fb3a344190](../../evidence/conditions-sets-091.md#c-ec9a68fb3a344190) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072786

```text
(config-subif)# vrrp <number:1..255> timers advertise <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 8 `；EOL ` RVA 0x3429AC70 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number。

[条件 C-c321831e12638671](../../evidence/conditions-sets-075.md#c-c321831e12638671) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-6a79a7e83d00f153](../../evidence/parameters-sets-008.md#p-6a79a7e83d00f153) · [状态效果 S-34eb14c77bda1ec7](../../evidence/state_effects-sets-012.md#s-34eb14c77bda1ec7)

### path-072787

```text
(config-subif)# vrrp <number:1..255> track <number:1..32767> <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 11 `；EOL ` RVA 0x3429B0E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Group number；` unsigned_number ` Tracked object。

[条件 C-ec9a68fb3a344190](../../evidence/conditions-sets-091.md#c-ec9a68fb3a344190) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [参数 P-3073f9542adafc88](../../evidence/parameters-sets-004.md#p-3073f9542adafc88) · [状态效果 S-328cfa80a98b3ca3](../../evidence/state_effects-sets-011.md#s-328cfa80a98b3ca3)

### path-072747

```text
(config-subif)# vrrp delay minimum <cr>
```

Handler ` RVA 0xE2E2FA0 `；selector ` 101 `；EOL ` RVA 0x3429BA90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-19f29840830a60ee](../../evidence/conditions-sets-010.md#c-19f29840830a60ee) · [缺口 G-d249188beeda3871](../../evidence/gaps-sets-007.md#g-d249188beeda3871) · [状态效果 S-73fd54f1c5ae45c5](../../evidence/state_effects-sets-025.md#s-73fd54f1c5ae45c5)

### path-072532

```text
(config-subif)# vrrs follow <cr>
```

Handler ` RVA 0xE2FEE60 `；selector ` 2 `；EOL ` RVA 0x342A5640 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a1a6c7ef56b4af69](../../evidence/conditions-sets-062.md#c-a1a6c7ef56b4af69) · [缺口 G-738487019e268c27](../../evidence/gaps-sets-004.md#g-738487019e268c27) · [状态效果 S-56e14fe982a051e9](../../evidence/state_effects-sets-019.md#s-56e14fe982a051e9)

### path-072531

```text
(config-subif)# vrrs interface-state <cr>
```

Handler ` RVA 0xE2FEE60 `；selector ` 4 `；EOL ` RVA 0x342A5968 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-79fc2caa6d33bbe1](../../evidence/conditions-sets-047.md#c-79fc2caa6d33bbe1) · [缺口 G-738487019e268c27](../../evidence/gaps-sets-004.md#g-738487019e268c27) · [状态效果 S-56e14fe982a051e9](../../evidence/state_effects-sets-019.md#s-56e14fe982a051e9)

### path-072533

```text
(config-subif)# vrrs mac-address <cr>
```

Handler ` RVA 0xE2FEE60 `；selector ` 3 `；EOL ` RVA 0x342A5C38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-38952ac3283f871d](../../evidence/conditions-sets-022.md#c-38952ac3283f871d) · [缺口 G-738487019e268c27](../../evidence/gaps-sets-004.md#g-738487019e268c27) · [状态效果 S-56e14fe982a051e9](../../evidence/state_effects-sets-019.md#s-56e14fe982a051e9)

### path-069364

```text
(config-subif)# vrrs pathway <string> <cr>
```

Handler ` RVA 0x133F8C30 `；selector ` 0 `；EOL ` RVA 0x35A89158 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of the VRRS tag to associate with pathway。

[条件 C-680d5d0fe7dba923](../../evidence/conditions-sets-040.md#c-680d5d0fe7dba923) · [参数 P-4d144c07c34ee5b2](../../evidence/parameters-sets-006.md#p-4d144c07c34ee5b2) · [状态效果 S-84d49f3a047aa944](../../evidence/state_effects-sets-028.md#s-84d49f3a047aa944)

### path-068088

```text
(config-subif)# vtp <cr>
```

Handler ` RVA 0x15C7B9D0 `；selector ` 0 `；EOL ` RVA 0x35E02FD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-02227243c538d1df](../../evidence/conditions-sets-001.md#c-02227243c538d1df)

### path-068636

```text
(config-subif)# x25 accept-reverse <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 21 `；EOL ` RVA 0x34BB8228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-069406

```text
(config-subif)# x25 address <address> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 0 `；EOL ` RVA 0x34BB5438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` X.121 address。

[条件 C-6c84f40d97d052ce](../../evidence/conditions-sets-042.md#c-6c84f40d97d052ce) · [参数 P-e17b43eb334e7804](../../evidence/parameters-sets-017.md#p-e17b43eb334e7804)

### path-069421

```text
(config-subif)# x25 alias <string> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 1 `；EOL ` RVA 0x34BB57C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` address pattern to alias。

[条件 C-c889b62659345a03](../../evidence/conditions-sets-077.md#c-c889b62659345a03) · [参数 P-b680586de65312e7](../../evidence/parameters-sets-014.md#p-b680586de65312e7)

### path-068781

```text
(config-subif)# x25 aodi <cr>
```

Handler ` RVA 0x1061D610 `；selector ` 7 `；EOL ` RVA 0x34BD3438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b184afabc59e2c77](../../evidence/conditions-sets-069.md#c-b184afabc59e2c77)

### path-070037

```text
(config-subif)# x25 bfe-decision yes <cr>
```

Handler ` RVA 0x1061DDE0 `；selector ` 4 `；EOL ` RVA 0x34BD3E38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5c34aae893b82cce](../../evidence/conditions-sets-036.md#c-5c34aae893b82cce) · [状态效果 S-0a3623f6cbb9ac5e](../../evidence/state_effects-sets-003.md#s-0a3623f6cbb9ac5e)

### path-070027

```text
(config-subif)# x25 bfe-emergency never <cr>
```

Handler ` RVA 0x1061DDE0 `；selector ` 3 `；EOL ` RVA 0x34BD3A50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5e45c0e8bf5d1030](../../evidence/conditions-sets-037.md#c-5e45c0e8bf5d1030) · [状态效果 S-ac62fa662a900c95](../../evidence/state_effects-sets-036.md#s-ac62fa662a900c95)

### path-072590

```text
(config-subif)# x25 default <?protoname_action@55558a10cd68> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 2 `；EOL ` RVA 0x34BB8D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-48935b442b022a67](../../evidence/conditions-sets-028.md#c-48935b442b022a67) · [缺口 G-2234afd04ea1b24f](../../evidence/gaps-sets-002.md#g-2234afd04ea1b24f)

### path-072628

```text
(config-subif)# x25 facility cug <number:dynamic> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 3 `；EOL ` RVA 0x34BB9148 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` CUG number。

[条件 C-facf65454275c96f](../../evidence/conditions-sets-097.md#c-facf65454275c96f) · [缺口 G-337b9604c5e5eef1](../../evidence/gaps-sets-002.md#g-337b9604c5e5eef1) · [参数 P-ee8d17c5a5a3e4f2](../../evidence/parameters-sets-018.md#p-ee8d17c5a5a3e4f2) · [状态效果 S-807588c514f418e0](../../evidence/state_effects-sets-027.md#s-807588c514f418e0)

### path-069863

```text
(config-subif)# x25 facility reverse <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 3 `；EOL ` RVA 0x34BB9148 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa) · [状态效果 S-4f00e5511223c572](../../evidence/state_effects-sets-017.md#s-4f00e5511223c572)

### path-072677

```text
(config-subif)# x25 fail-over <number:0..65565> interface <interface> <cr>
```

Handler ` RVA 0x10631F70 `；selector ` 0 `；EOL ` RVA 0x34BD7078 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` delay time。

[条件 C-d610eda89b079a74](../../evidence/conditions-sets-083.md#c-d610eda89b079a74) · [缺口 G-d60c52f45eb576d5](../../evidence/gaps-sets-007.md#g-d60c52f45eb576d5) · [参数 P-cb739af3272e0f59](../../evidence/parameters-sets-015.md#p-cb739af3272e0f59)

### path-068095

```text
(config-subif)# x25 hic <number:0..4095> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 4 `；EOL ` RVA 0x34BB5A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Circuit number。

[条件 C-5d1288dbf95a55c5](../../evidence/conditions-sets-036.md#c-5d1288dbf95a55c5) · [参数 P-7dcb4f475fe8ad41](../../evidence/parameters-sets-010.md#p-7dcb4f475fe8ad41)

### path-068106

```text
(config-subif)# x25 hoc <number:0..4095> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 8 `；EOL ` RVA 0x34BB64E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Circuit number。

[条件 C-d9f3989fa637220f](../../evidence/conditions-sets-084.md#c-d9f3989fa637220f) · [参数 P-0da50e006e1d9179](../../evidence/parameters-sets-001.md#p-0da50e006e1d9179)

### path-068174

```text
(config-subif)# x25 hold-queue <number:0..9999> <cr>
```

Handler ` RVA 0x1061D610 `；selector ` 6 `；EOL ` RVA 0x34BD27B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Maximum packets to queue before dropping。

[条件 C-ccd62008da0fcfbb](../../evidence/conditions-sets-079.md#c-ccd62008da0fcfbb) · [参数 P-2baa8ab10fb60068](../../evidence/parameters-sets-004.md#p-2baa8ab10fb60068)

### path-068180

```text
(config-subif)# x25 hold-vc-timer <number:0..1000> <cr>
```

Handler ` RVA 0x1061D610 `；selector ` 0 `；EOL ` RVA 0x34BD2AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minutes; 0 to always try calls。

[条件 C-bda7124731026008](../../evidence/conditions-sets-073.md#c-bda7124731026008) · [参数 P-62aebe3aebd8743d](../../evidence/parameters-sets-008.md#p-62aebe3aebd8743d)

### path-068098

```text
(config-subif)# x25 htc <number:0..4095> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 6 `；EOL ` RVA 0x34BB5FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Circuit number。

[条件 C-7e426db1f0ae6aa5](../../evidence/conditions-sets-049.md#c-7e426db1f0ae6aa5) · [参数 P-7bde3fcabbc7f634](../../evidence/parameters-sets-010.md#p-7bde3fcabbc7f634)

### path-069927

```text
(config-subif)# x25 idle <number:0..255> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 7 `；EOL ` RVA 0x34BBA2B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Minutes; 0 to never clear。

[条件 C-66161127b7679984](../../evidence/conditions-sets-039.md#c-66161127b7679984) · [参数 P-e4e9321959bf95f4](../../evidence/parameters-sets-017.md#p-e4e9321959bf95f4)

### path-068776

```text
(config-subif)# x25 ip-precedence <cr>
```

Handler ` RVA 0x1061D610 `；selector ` 1 `；EOL ` RVA 0x34BD3190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b184afabc59e2c77](../../evidence/conditions-sets-069.md#c-b184afabc59e2c77)

### path-072582

```text
(config-subif)# x25 ips <number:dynamic> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 19 `；EOL ` RVA 0x34BB7C50 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bytes (power of 2)。

[条件 C-60c29c6e3e881a10](../../evidence/conditions-sets-038.md#c-60c29c6e3e881a10) · [缺口 G-2ab670dc5a635079](../../evidence/gaps-sets-002.md#g-2ab670dc5a635079) · [参数 P-abd3a7e13268a6bb](../../evidence/parameters-sets-013.md#p-abd3a7e13268a6bb)

### path-068094

```text
(config-subif)# x25 lic <number:0..4095> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 3 `；EOL ` RVA 0x34BB56E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Circuit number。

[条件 C-11fcd51392f7201a](../../evidence/conditions-sets-007.md#c-11fcd51392f7201a) · [参数 P-b12fc8b1ef88f26f](../../evidence/parameters-sets-013.md#p-b12fc8b1ef88f26f)

### path-068669

```text
(config-subif)# x25 linkrestart <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 22 `；EOL ` RVA 0x34BB8A20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-068103

```text
(config-subif)# x25 loc <number:0..4095> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 7 `；EOL ` RVA 0x34BB6248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Circuit number。

[条件 C-8fb10dbb5ccb29db](../../evidence/conditions-sets-056.md#c-8fb10dbb5ccb29db) · [参数 P-ea5f119c8ca291fd](../../evidence/parameters-sets-018.md#p-ea5f119c8ca291fd)

### path-068096

```text
(config-subif)# x25 ltc <number:0..4095> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 5 `；EOL ` RVA 0x34BB5D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Virtual Circuit number。

[条件 C-30124efa0e09ed30](../../evidence/conditions-sets-019.md#c-30124efa0e09ed30) · [参数 P-4fd195c3778e4877](../../evidence/parameters-sets-007.md#p-4fd195c3778e4877)

### path-072595

```text
(config-subif)# x25 map <?protoaddr_action@555589e57540> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 10 `；EOL ` RVA 0x34BBD928 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7d7dbd2ad20c48ce](../../evidence/conditions-sets-049.md#c-7d7dbd2ad20c48ce) · [缺口 G-a6594d49bf7480f4](../../evidence/gaps-sets-006.md#g-a6594d49bf7480f4) · [状态效果 S-3c2c8a60db2e8202](../../evidence/state_effects-sets-013.md#s-3c2c8a60db2e8202)

### path-072638

```text
(config-subif)# x25 map svc <string> <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 11 `；EOL ` RVA 0x34BBECE8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` X.121 Address pattern。

[条件 C-a8981bc765928c2c](../../evidence/conditions-sets-065.md#c-a8981bc765928c2c) · [缺口 G-191af87c3f2e237a](../../evidence/gaps-sets-001.md#g-191af87c3f2e237a) · [参数 P-37d1f7240976abfc](../../evidence/parameters-sets-005.md#p-37d1f7240976abfc) · [状态效果 S-b1d33d5f744ec88c](../../evidence/state_effects-sets-038.md#s-b1d33d5f744ec88c)

### path-069407

```text
(config-subif)# x25 modulo 8 <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 2 `；EOL ` RVA 0x34BB5068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec9c511fa775f23a](../../evidence/conditions-sets-091.md#c-ec9c511fa775f23a) · [状态效果 S-a3239d0d9049ac64](../../evidence/state_effects-sets-035.md#s-a3239d0d9049ac64)

### path-068650

```text
(config-subif)# x25 nonzero-dte-cause <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 24 `；EOL ` RVA 0x34BB84D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-068183

```text
(config-subif)# x25 nvc <number:1..8> <cr>
```

Handler ` RVA 0x1061D610 `；selector ` 2 `；EOL ` RVA 0x34BD3460 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` SVCs。

[条件 C-6500ef2424a69945](../../evidence/conditions-sets-039.md#c-6500ef2424a69945) · [参数 P-ef79d593e83a15ab](../../evidence/parameters-sets-018.md#p-ef79d593e83a15ab)

### path-072584

```text
(config-subif)# x25 ops <number:dynamic> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 20 `；EOL ` RVA 0x34BB7FA0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Bytes (power of 2)。

[条件 C-3e632c0ac2c044cb](../../evidence/conditions-sets-024.md#c-3e632c0ac2c044cb) · [缺口 G-fa89195477ba8c87](../../evidence/gaps-sets-009.md#g-fa89195477ba8c87) · [参数 P-3cb882359209fead](../../evidence/parameters-sets-005.md#p-3cb882359209fead)

### path-068678

```text
(config-subif)# x25 pad-access <cr>
```

Handler ` RVA 0xFE61240 `；selector ` 0 `；EOL ` RVA 0x34903250 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a1e6fe6d97c5ebb2](../../evidence/conditions-sets-063.md#c-a1e6fe6d97c5ebb2)

### path-068660

```text
(config-subif)# x25 relay-vc-number <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 34 `；EOL ` RVA 0x34BB8778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-072043

```text
(config-subif)# x25 remote-red <address> remote-black <address> <cr>
```

Handler ` RVA 0x1061DDE0 `；selector ` 5 `；EOL ` RVA 0x34BD4270 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address of host；` address ` IP address of remote BFE。

[条件 C-462dee200a8b198b](../../evidence/conditions-sets-027.md#c-462dee200a8b198b) · [参数 P-c03e127fb25872ce](../../evidence/parameters-sets-015.md#p-c03e127fb25872ce)

### path-072349

```text
(config-subif)# x25 retry interval <number:5..3600> attempts <number:1..100> <cr>
```

Handler ` RVA 0x1061D610 `；selector ` 8 `；EOL ` RVA 0x34BD2BC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Retry interval in seconds；` unsigned_number ` Number of retry attempts。

[条件 C-19cb61347b95ed87](../../evidence/conditions-sets-010.md#c-19cb61347b95ed87) · [参数 P-f11ded7e9555fe94](../../evidence/parameters-sets-018.md#p-f11ded7e9555fe94)

### path-069344

```text
(config-subif)# x25 security crcdn <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 31 `；EOL ` RVA 0x34BB4798 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c889b62659345a03](../../evidence/conditions-sets-077.md#c-c889b62659345a03) · [状态效果 S-52d2559b2078d82a](../../evidence/state_effects-sets-018.md#s-52d2559b2078d82a)

### path-070046

```text
(config-subif)# x25 subscribe cug-service <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 26 `；EOL ` RVA 0x34BBBF58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-12ef06c2074c4fba](../../evidence/conditions-sets-007.md#c-12ef06c2074c4fba)

### path-071233

```text
(config-subif)# x25 subscribe flow-control always <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 23 `；EOL ` RVA 0x34BBACF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0a02b824a994626](../../evidence/conditions-sets-093.md#c-f0a02b824a994626) · [状态效果 S-d72e38b6548f15ab](../../evidence/state_effects-sets-046.md#s-d72e38b6548f15ab)

### path-071274

```text
(config-subif)# x25 subscribe lc0 incoming-only <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 25 `；EOL ` RVA 0x34BBB9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc9b9b6c5222cad3](../../evidence/conditions-sets-097.md#c-fc9b9b6c5222cad3) · [状态效果 S-1992ce78711f3db5](../../evidence/state_effects-sets-006.md#s-1992ce78711f3db5)

### path-072632

```text
(config-subif)# x25 subscribe local-cug <number:dynamic> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 27 `；EOL ` RVA 0x34BBC388 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Local CUG number。

[条件 C-21198bb67e654d9e](../../evidence/conditions-sets-013.md#c-21198bb67e654d9e) · [缺口 G-14a7116e8fde30df](../../evidence/gaps-sets-001.md#g-14a7116e8fde30df) · [参数 P-5572468e1731c58f](../../evidence/parameters-sets-007.md#p-5572468e1731c58f)

### path-069959

```text
(config-subif)# x25 subscribe packetsize <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 29 `；EOL ` RVA 0x34BBB180 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-071223

```text
(config-subif)# x25 subscribe throughput never <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 32 `；EOL ` RVA 0x34BBA930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4154087191aee251](../../evidence/conditions-sets-026.md#c-4154087191aee251) · [状态效果 S-5ec6194be20a013b](../../evidence/state_effects-sets-020.md#s-5ec6194be20a013b)

### path-069972

```text
(config-subif)# x25 subscribe windowsize <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 28 `；EOL ` RVA 0x34BBB618 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-068694

```text
(config-subif)# x25 suppress-called-address <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 4 `；EOL ` RVA 0x34BB99F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-068702

```text
(config-subif)# x25 suppress-calling-address <cr>
```

Handler ` RVA 0x105E9A10 `；selector ` 5 `；EOL ` RVA 0x34BB9CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8f279cf63b17daaa](../../evidence/conditions-sets-055.md#c-8f279cf63b17daaa)

### path-068111

```text
(config-subif)# x25 t10 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 9 `；EOL ` RVA 0x34BB6A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-ee3b578b5522a9ad](../../evidence/conditions-sets-092.md#c-ee3b578b5522a9ad) · [参数 P-81c7bef2a29a5ad4](../../evidence/parameters-sets-010.md#p-81c7bef2a29a5ad4)

### path-068118

```text
(config-subif)# x25 t11 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 11 `；EOL ` RVA 0x34BB6A68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-34c2f15025ffbacd](../../evidence/conditions-sets-021.md#c-34c2f15025ffbacd) · [参数 P-24827c88155c9dc0](../../evidence/parameters-sets-003.md#p-24827c88155c9dc0)

### path-068123

```text
(config-subif)# x25 t12 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 13 `；EOL ` RVA 0x34BB6D08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-217acc50fa7c89ac](../../evidence/conditions-sets-013.md#c-217acc50fa7c89ac) · [参数 P-bda2cfb38f4ca2d2](../../evidence/parameters-sets-014.md#p-bda2cfb38f4ca2d2)

### path-068128

```text
(config-subif)# x25 t13 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 15 `；EOL ` RVA 0x34BB6FA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-a1ea4c483a83e93e](../../evidence/conditions-sets-063.md#c-a1ea4c483a83e93e) · [参数 P-4511326732d0072d](../../evidence/parameters-sets-006.md#p-4511326732d0072d)

### path-068112

```text
(config-subif)# x25 t20 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 10 `；EOL ` RVA 0x34BBC8E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-9f96be6986cc17de](../../evidence/conditions-sets-062.md#c-9f96be6986cc17de) · [参数 P-1d6bb9f789bfb809](../../evidence/parameters-sets-003.md#p-1d6bb9f789bfb809)

### path-068119

```text
(config-subif)# x25 t21 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 12 `；EOL ` RVA 0x34BBC908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-e57a7d3be4066031](../../evidence/conditions-sets-088.md#c-e57a7d3be4066031) · [参数 P-3d8464d26d0925f4](../../evidence/parameters-sets-005.md#p-3d8464d26d0925f4)

### path-068124

```text
(config-subif)# x25 t22 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 14 `；EOL ` RVA 0x34BBCBA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-cecbf02e01624431](../../evidence/conditions-sets-080.md#c-cecbf02e01624431) · [参数 P-019de3cc1d0e605c](../../evidence/parameters-sets-001.md#p-019de3cc1d0e605c)

### path-068129

```text
(config-subif)# x25 t23 <number:1..1000> <cr>
```

Handler ` RVA 0x105E7C30 `；selector ` 16 `；EOL ` RVA 0x34BBCE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Seconds。

[条件 C-fa99b15f5df0c264](../../evidence/conditions-sets-097.md#c-fa99b15f5df0c264) · [参数 P-a034c23d60cf24b9](../../evidence/parameters-sets-012.md#p-a034c23d60cf24b9)

