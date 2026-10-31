# pm-delay-profile-probe · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008909

```text
(config-pm-dm-intf-probe)# burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a)

### observed_connections-008910

```text
(config-pm-dm-intf-probe)# computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-d42c022ddeee0d10](../../evidence/conditions-sets-082.md#c-d42c022ddeee0d10) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7)

### observed_connections-008907

```text
(config-pm-dm-intf-probe)# default <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008918

```text
(config-pm-dm-intf-probe)# default burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a) · [状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008920

```text
(config-pm-dm-intf-probe)# default computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-d42c022ddeee0d10](../../evidence/conditions-sets-082.md#c-d42c022ddeee0d10) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7) · [状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008923

```text
(config-pm-dm-intf-probe)# default measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-6a65f38d35257a86](../../evidence/conditions-sets-041.md#c-6a65f38d35257a86) · [状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008924

```text
(config-pm-dm-intf-probe)# default measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-5a05f50418cd240f](../../evidence/conditions-sets-035.md#c-5a05f50418cd240f) · [状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008916

```text
(config-pm-dm-intf-probe)# default protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008928

```text
(config-pm-dm-intf-probe)# default protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008926

```text
(config-pm-dm-intf-probe)# default protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[状态效果 S-62eb1c7669c1bd72](../../evidence/state_effects-sets-021.md#s-62eb1c7669c1bd72)

### observed_connections-008905

```text
(config-pm-dm-intf-probe)# exit <cr>
```

Handler ` RVA 0x1ACF4530 `；selector ` 0 `；EOL ` RVA 0x36DDDE28 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-571c97cd8ac04386](../../evidence/conditions-sets-034.md#c-571c97cd8ac04386)

### observed_connections-008911

```text
(config-pm-dm-intf-probe)# measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6a65f38d35257a86](../../evidence/conditions-sets-041.md#c-6a65f38d35257a86)

### observed_connections-008912

```text
(config-pm-dm-intf-probe)# measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5a05f50418cd240f](../../evidence/conditions-sets-035.md#c-5a05f50418cd240f)

### observed_connections-008906

```text
(config-pm-dm-intf-probe)# no <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008917

```text
(config-pm-dm-intf-probe)# no burst-interval <number:30..15000> <cr>
```

Handler ` RVA 0x1ACF2620 `；selector ` 0 `；EOL ` RVA 0x36DD2CB0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Burst interval (msec)。

[参数 P-03cdf0ceed35889a](../../evidence/parameters-sets-001.md#p-03cdf0ceed35889a) · [状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008919

```text
(config-pm-dm-intf-probe)# no computation-interval <number:3..3600> <cr>
```

Handler ` RVA 0x1ACF2200 `；selector ` 0 `；EOL ` RVA 0x36DD2FE0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

参数提示：` unsigned_number ` Computation interval (seconds)。

[条件 C-d42c022ddeee0d10](../../evidence/conditions-sets-082.md#c-d42c022ddeee0d10) · [参数 P-539c95aaebc2a4a7](../../evidence/parameters-sets-007.md#p-539c95aaebc2a4a7) · [状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008921

```text
(config-pm-dm-intf-probe)# no measurement-mode one-way <cr>
```

Handler ` RVA 0x1ACF23D0 `；selector ` 0 `；EOL ` RVA 0x36DD3358 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-6a65f38d35257a86](../../evidence/conditions-sets-041.md#c-6a65f38d35257a86) · [状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008922

```text
(config-pm-dm-intf-probe)# no measurement-mode two-way <cr>
```

Handler ` RVA 0x1ACF4AA0 `；selector ` 0 `；EOL ` RVA 0x36DD3600 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-5a05f50418cd240f](../../evidence/conditions-sets-035.md#c-5a05f50418cd240f) · [状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008914

```text
(config-pm-dm-intf-probe)# no protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008927

```text
(config-pm-dm-intf-probe)# no protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008925

```text
(config-pm-dm-intf-probe)# no protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[状态效果 S-7761ac8d55e5dd18](../../evidence/state_effects-sets-025.md#s-7761ac8d55e5dd18)

### observed_connections-008908

```text
(config-pm-dm-intf-probe)# protocol <cr>
```

Handler ` RVA 0x1ACF2470 `；selector ` 0 `；EOL ` RVA 0x36DD3E68 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008915

```text
(config-pm-dm-intf-probe)# protocol pm-mpls <cr>
```

Handler ` RVA 0x1ACF46B0 `；selector ` 0 `；EOL ` RVA 0x36DD3BD0 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008913

```text
(config-pm-dm-intf-probe)# protocol twamp-light <cr>
```

Handler ` RVA 0x1ACF45A0 `；selector ` 0 `；EOL ` RVA 0x36DD3928 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。

### observed_connections-008904

```text
(config-pm-dm-intf-probe)# <cr>
```

Handler ` RVA 0x1ACF1390 `；selector ` 0 `；EOL ` RVA 0x36DD4100 `。

模式根 ` RVA 0x36DC1B10 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

该路径记录的参数、条件、状态效果和缺口列表均为空。
