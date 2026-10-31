# pm-delay-profile · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007906

```text
(config-pm-dm-intf)# advertisement <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007911

```text
(config-pm-dm-intf)# advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007929

```text
(config-pm-dm-intf)# advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742)

### observed_connections-007932

```text
(config-pm-dm-intf)# advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef)

### observed_connections-007914

```text
(config-pm-dm-intf)# advertisement periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007924

```text
(config-pm-dm-intf)# advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007936

```text
(config-pm-dm-intf)# advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1)

### observed_connections-007930

```text
(config-pm-dm-intf)# advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7)

### observed_connections-007934

```text
(config-pm-dm-intf)# advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22)

### observed_connections-007907

```text
(config-pm-dm-intf)# default <cr>
```

Handler ` RVA 0x1ACEF410 `；selector ` 0 `；EOL ` RVA 0x36DD4378 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007912

```text
(config-pm-dm-intf)# default advertisement <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007918

```text
(config-pm-dm-intf)# default advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007949

```text
(config-pm-dm-intf)# default advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007953

```text
(config-pm-dm-intf)# default advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007921

```text
(config-pm-dm-intf)# default advertisement periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007944

```text
(config-pm-dm-intf)# default advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007957

```text
(config-pm-dm-intf)# default advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007952

```text
(config-pm-dm-intf)# default advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007955

```text
(config-pm-dm-intf)# default advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007913

```text
(config-pm-dm-intf)# default probe <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007933

```text
(config-pm-dm-intf)# default probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007937

```text
(config-pm-dm-intf)# default probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-d42c022ddeee0d10](../../evidence/conditions-sets-082.md#c-d42c022ddeee0d10) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007941

```text
(config-pm-dm-intf)# default probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6a65f38d35257a86](../../evidence/conditions-sets-041.md#c-6a65f38d35257a86) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007942

```text
(config-pm-dm-intf)# default probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a05f50418cd240f](../../evidence/conditions-sets-035.md#c-5a05f50418cd240f) · [状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007928

```text
(config-pm-dm-intf)# default probe protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007947

```text
(config-pm-dm-intf)# default probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007945

```text
(config-pm-dm-intf)# default probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-39d0fdd365f76f6b](../../evidence/state_effects-sets-013.md#s-39d0fdd365f76f6b)

### observed_connections-007904

```text
(config-pm-dm-intf)# exit <cr>
```

Handler ` RVA 0x1ACF4980 `；selector ` 0 `；EOL ` RVA 0x36DDA5B8 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f299ab713e3a40fa](../../evidence/conditions-sets-094.md#c-f299ab713e3a40fa)

### observed_connections-007905

```text
(config-pm-dm-intf)# no <cr>
```

Handler ` RVA 0x1ACEF410 `；selector ` 0 `；EOL ` RVA 0x36DD4378 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007909

```text
(config-pm-dm-intf)# no advertisement <cr>
```

Handler ` RVA 0x1ACF12B0 `；selector ` 0 `；EOL ` RVA 0x36DD28F0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007916

```text
(config-pm-dm-intf)# no advertisement accelerated <cr>
```

Handler ` RVA 0x1ACF1600 `；selector ` 0 `；EOL ` RVA 0x36DD17A0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007948

```text
(config-pm-dm-intf)# no advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF1BE0 `；selector ` 0 `；EOL ` RVA 0x36DD11F0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-87f9628a76ee7742](../../evidence/parameters-sets-010.md#p-87f9628a76ee7742) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007951

```text
(config-pm-dm-intf)# no advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1AB0 `；selector ` 0 `；EOL ` RVA 0x36DD1508 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-f0ea66ce03e923ef](../../evidence/parameters-sets-018.md#p-f0ea66ce03e923ef) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007919

```text
(config-pm-dm-intf)# no advertisement periodic <cr>
```

Handler ` RVA 0x1ACF1830 `；selector ` 0 `；EOL ` RVA 0x36DD2670 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007940

```text
(config-pm-dm-intf)# no advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACF1D10 `；selector ` 0 `；EOL ` RVA 0x36DD23C8 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007956

```text
(config-pm-dm-intf)# no advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACF1DB0 `；selector ` 0 `；EOL ` RVA 0x36DD2140 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-7083362af6595dd1](../../evidence/parameters-sets-009.md#p-7083362af6595dd1) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007950

```text
(config-pm-dm-intf)# no advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACF2050 `；selector ` 0 `；EOL ` RVA 0x36DD1B10 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-a9f06d097ad720d7](../../evidence/parameters-sets-013.md#p-a9f06d097ad720d7) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007954

```text
(config-pm-dm-intf)# no advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACF1EA0 `；selector ` 0 `；EOL ` RVA 0x36DD1E50 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-870c791c38909c22](../../evidence/parameters-sets-010.md#p-870c791c38909c22) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007910

```text
(config-pm-dm-intf)# no probe <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007931

```text
(config-pm-dm-intf)# no probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007935

```text
(config-pm-dm-intf)# no probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-d42c022ddeee0d10](../../evidence/conditions-sets-082.md#c-d42c022ddeee0d10) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007938

```text
(config-pm-dm-intf)# no probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6a65f38d35257a86](../../evidence/conditions-sets-041.md#c-6a65f38d35257a86) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007939

```text
(config-pm-dm-intf)# no probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5a05f50418cd240f](../../evidence/conditions-sets-035.md#c-5a05f50418cd240f) · [状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007926

```text
(config-pm-dm-intf)# no probe protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007946

```text
(config-pm-dm-intf)# no probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007943

```text
(config-pm-dm-intf)# no probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-d04f25d133cb7468](../../evidence/state_effects-sets-044.md#s-d04f25d133cb7468)

### observed_connections-007908

```text
(config-pm-dm-intf)# probe <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007917

```text
(config-pm-dm-intf)# probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a)

### observed_connections-007920

```text
(config-pm-dm-intf)# probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-d42c022ddeee0d10](../../evidence/conditions-sets-082.md#c-d42c022ddeee0d10) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7)

### observed_connections-007922

```text
(config-pm-dm-intf)# probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a65f38d35257a86](../../evidence/conditions-sets-041.md#c-6a65f38d35257a86)

### observed_connections-007923

```text
(config-pm-dm-intf)# probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a05f50418cd240f](../../evidence/conditions-sets-035.md#c-5a05f50418cd240f)

### observed_connections-007915

```text
(config-pm-dm-intf)# probe protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007927

```text
(config-pm-dm-intf)# probe protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007925

```text
(config-pm-dm-intf)# probe protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007903

```text
(config-pm-dm-intf)# <cr>
```

Handler ` RVA 0x1ACEF410 `；selector ` 0 `；EOL ` RVA 0x36DD4378 `。

模式根 ` RVA 0x36DC18E0 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
