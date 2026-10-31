# pm-delay-profile-ep · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-007290

```text
(config-pm-dm-ep)# advertisement <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007300

```text
(config-pm-dm-ep)# advertisement accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007326

```text
(config-pm-dm-ep)# advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9)

### observed_connections-007332

```text
(config-pm-dm-ep)# advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7)

### observed_connections-007302

```text
(config-pm-dm-ep)# advertisement periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007318

```text
(config-pm-dm-ep)# advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007340

```text
(config-pm-dm-ep)# advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a)

### observed_connections-007329

```text
(config-pm-dm-ep)# advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004)

### observed_connections-007336

```text
(config-pm-dm-ep)# advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2)

### observed_connections-007298

```text
(config-pm-dm-ep)# advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007303

```text
(config-pm-dm-ep)# advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007304

```text
(config-pm-dm-ep)# advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007305

```text
(config-pm-dm-ep)# advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007291

```text
(config-pm-dm-ep)# default <cr>
```

Handler ` RVA 0x1ACF9DE0 `；selector ` 0 `；EOL ` RVA 0x36DCB5B0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007296

```text
(config-pm-dm-ep)# default advertisement <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007313

```text
(config-pm-dm-ep)# default advertisement accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007351

```text
(config-pm-dm-ep)# default advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007355

```text
(config-pm-dm-ep)# default advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007316

```text
(config-pm-dm-ep)# default advertisement periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007346

```text
(config-pm-dm-ep)# default advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007359

```text
(config-pm-dm-ep)# default advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007353

```text
(config-pm-dm-ep)# default advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007357

```text
(config-pm-dm-ep)# default advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007309

```text
(config-pm-dm-ep)# default advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007322

```text
(config-pm-dm-ep)# default advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007324

```text
(config-pm-dm-ep)# default advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007328

```text
(config-pm-dm-ep)# default advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007301

```text
(config-pm-dm-ep)# default liveness-detection <cr>
```

Handler ` RVA 0x1ACFB2C0 `；selector ` 0 `；EOL ` RVA 0x36DCB330 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f85c029387138a43](../../evidence/conditions-sets-096.md#c-f85c029387138a43) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007335

```text
(config-pm-dm-ep)# default liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACFCEA0 `；selector ` 0 `；EOL ` RVA 0x36DCB098 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-f85c029387138a43](../../evidence/conditions-sets-096.md#c-f85c029387138a43) · [参数 P-832a3c41773baa51](../../evidence/parameters-sets-010.md#p-832a3c41773baa51) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007297

```text
(config-pm-dm-ep)# default probe <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007330

```text
(config-pm-dm-ep)# default probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007339

```text
(config-pm-dm-ep)# default probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-a62e985afdf91068](../../evidence/conditions-sets-064.md#c-a62e985afdf91068) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007349

```text
(config-pm-dm-ep)# default probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007344

```text
(config-pm-dm-ep)# default probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007347

```text
(config-pm-dm-ep)# default probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007337

```text
(config-pm-dm-ep)# default probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007341

```text
(config-pm-dm-ep)# default probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7) · [状态效果 S-89daa2e58f674d08](../../evidence/state_effects-sets-029.md#s-89daa2e58f674d08)

### observed_connections-007288

```text
(config-pm-dm-ep)# exit <cr>
```

Handler ` RVA 0x1ACFC930 `；selector ` 0 `；EOL ` RVA 0x36DDADC8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0298c48db0d35aab](../../evidence/conditions-sets-001.md#c-0298c48db0d35aab)

### observed_connections-007293

```text
(config-pm-dm-ep)# liveness-detection <cr>
```

Handler ` RVA 0x1ACFB2C0 `；selector ` 0 `；EOL ` RVA 0x36DCB330 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f85c029387138a43](../../evidence/conditions-sets-096.md#c-f85c029387138a43)

### observed_connections-007310

```text
(config-pm-dm-ep)# liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACFCEA0 `；selector ` 0 `；EOL ` RVA 0x36DCB098 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-f85c029387138a43](../../evidence/conditions-sets-096.md#c-f85c029387138a43) · [参数 P-832a3c41773baa51](../../evidence/parameters-sets-010.md#p-832a3c41773baa51)

### observed_connections-007289

```text
(config-pm-dm-ep)# no <cr>
```

Handler ` RVA 0x1ACF9DE0 `；selector ` 0 `；EOL ` RVA 0x36DCB5B0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007294

```text
(config-pm-dm-ep)# no advertisement <cr>
```

Handler ` RVA 0x1ACFAE10 `；selector ` 0 `；EOL ` RVA 0x36DC94E8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007308

```text
(config-pm-dm-ep)# no advertisement accelerated <cr>
```

Handler ` RVA 0x1ACFB3D0 `；selector ` 0 `；EOL ` RVA 0x36DC83D8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007350

```text
(config-pm-dm-ep)# no advertisement accelerated minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFB890 `；selector ` 0 `；EOL ` RVA 0x36DC7E28 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement minimum change (uSec)。

[参数 P-9f6f6ba2d130deb9](../../evidence/parameters-sets-012.md#p-9f6f6ba2d130deb9) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007354

```text
(config-pm-dm-ep)# no advertisement accelerated threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFB760 `；selector ` 0 `；EOL ` RVA 0x36DC8140 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Accelerated advertisement threshold percentage change。

[参数 P-2bf284102dc3b5f7](../../evidence/parameters-sets-004.md#p-2bf284102dc3b5f7) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007314

```text
(config-pm-dm-ep)# no advertisement periodic <cr>
```

Handler ` RVA 0x1ACFB520 `；selector ` 0 `；EOL ` RVA 0x36DC9258 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007343

```text
(config-pm-dm-ep)# no advertisement periodic disabled <cr>
```

Handler ` RVA 0x1ACFB9C0 `；selector ` 0 `；EOL ` RVA 0x36DC8FB0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007358

```text
(config-pm-dm-ep)# no advertisement periodic interval <number:30..3600> <cr>
```

Handler ` RVA 0x1ACFBA60 `；selector ` 0 `；EOL ` RVA 0x36DC8D28 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number `  Periodic advertisement interval (seconds)。

[参数 P-9239b3dae0fed22a](../../evidence/parameters-sets-011.md#p-9239b3dae0fed22a) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007352

```text
(config-pm-dm-ep)# no advertisement periodic minimum-change <number:0..1000000> <cr>
```

Handler ` RVA 0x1ACFBD00 `；selector ` 0 `；EOL ` RVA 0x36DC86F8 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement minimum change (uSec)。

[参数 P-ca7c92d34181e004](../../evidence/parameters-sets-015.md#p-ca7c92d34181e004) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007356

```text
(config-pm-dm-ep)# no advertisement periodic threshold <number:0..100> <cr>
```

Handler ` RVA 0x1ACFBB50 `；selector ` 0 `；EOL ` RVA 0x36DC8A38 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Periodic advertisement threshold percentage change。

[参数 P-0f8747ef381467d2](../../evidence/parameters-sets-002.md#p-0f8747ef381467d2) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007307

```text
(config-pm-dm-ep)# no advertisement threshold-check <cr>
```

Handler ` RVA 0x1ACFB6B0 `；selector ` 0 `；EOL ` RVA 0x36DC7A78 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007321

```text
(config-pm-dm-ep)# no advertisement threshold-check average-delay <cr>
```

Handler ` RVA 0x1ACFCC80 `；selector ` 0 `；EOL ` RVA 0x36DC7280 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007323

```text
(config-pm-dm-ep)# no advertisement threshold-check maximum-delay <cr>
```

Handler ` RVA 0x1ACFCB30 `；selector ` 0 `；EOL ` RVA 0x36DC7528 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007325

```text
(config-pm-dm-ep)# no advertisement threshold-check minimum-delay <cr>
```

Handler ` RVA 0x1ACFC9E0 `；selector ` 0 `；EOL ` RVA 0x36DC77D0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007299

```text
(config-pm-dm-ep)# no liveness-detection <cr>
```

Handler ` RVA 0x1ACFB2C0 `；selector ` 0 `；EOL ` RVA 0x36DCB330 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-f85c029387138a43](../../evidence/conditions-sets-096.md#c-f85c029387138a43) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007331

```text
(config-pm-dm-ep)# no liveness-detection multiplier <number:2..10> <cr>
```

Handler ` RVA 0x1ACFCEA0 `；selector ` 0 `；EOL ` RVA 0x36DCB098 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Detect Multiplier。

[条件 C-f85c029387138a43](../../evidence/conditions-sets-096.md#c-f85c029387138a43) · [参数 P-832a3c41773baa51](../../evidence/parameters-sets-010.md#p-832a3c41773baa51) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007295

```text
(config-pm-dm-ep)# no probe <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007327

```text
(config-pm-dm-ep)# no probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007334

```text
(config-pm-dm-ep)# no probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-a62e985afdf91068](../../evidence/conditions-sets-064.md#c-a62e985afdf91068) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007348

```text
(config-pm-dm-ep)# no probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007342

```text
(config-pm-dm-ep)# no probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007345

```text
(config-pm-dm-ep)# no probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007333

```text
(config-pm-dm-ep)# no probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007338

```text
(config-pm-dm-ep)# no probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7) · [状态效果 S-1760abe834733e25](../../evidence/state_effects-sets-005.md#s-1760abe834733e25)

### observed_connections-007292

```text
(config-pm-dm-ep)# probe <cr>
```

Handler ` RVA 0x1ACFB040 `；selector ` 0 `；EOL ` RVA 0x36DCAD20 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007306

```text
(config-pm-dm-ep)# probe burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACFC440 `；selector ` 0 `；EOL ` RVA 0x36DC98D0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-f4437d88dc812964](../../evidence/parameters-sets-018.md#p-f4437d88dc812964)

### observed_connections-007312

```text
(config-pm-dm-ep)# probe computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACFC0E0 `；selector ` 0 `；EOL ` RVA 0x36DC9C00 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-a62e985afdf91068](../../evidence/conditions-sets-064.md#c-a62e985afdf91068) · [参数 P-d09a80bed29e4458](../../evidence/parameters-sets-016.md#p-d09a80bed29e4458)

### observed_connections-007320

```text
(config-pm-dm-ep)# probe measurement-mode loopback <cr>
```

Handler ` RVA 0x1ACFC2A0 `；selector ` 0 `；EOL ` RVA 0x36DCAA40 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007317

```text
(config-pm-dm-ep)# probe measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACFC370 `；selector ` 0 `；EOL ` RVA 0x36DCA4F0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007319

```text
(config-pm-dm-ep)# probe measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACFCDE0 `；selector ` 0 `；EOL ` RVA 0x36DCA798 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-007311

```text
(config-pm-dm-ep)# probe padding-size <number:0..8000> <cr>
```

Handler ` RVA 0x1ACFBEC0 `；selector ` 0 `；EOL ` RVA 0x36DC9F38 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Padding (bytes) to add to probes。

[参数 P-0f90b03d9cc18eae](../../evidence/parameters-sets-002.md#p-0f90b03d9cc18eae)

### observed_connections-007315

```text
(config-pm-dm-ep)# probe tos-dscp <number:0..63> <cr>
```

Handler ` RVA 0x1ACFBFE0 `；selector ` 0 `；EOL ` RVA 0x36DCA228 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` TOS DSCP。

[参数 P-1395f8a7ed87e3f7](../../evidence/parameters-sets-002.md#p-1395f8a7ed87e3f7)

### observed_connections-007287

```text
(config-pm-dm-ep)# <cr>
```

Handler ` RVA 0x1ACF9DE0 `；selector ` 0 `；EOL ` RVA 0x36DCB5B0 `。

模式根 ` RVA 0x36DC1930 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

