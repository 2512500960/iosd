# ecfm · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-008983

```text
(config-ecfm)# default id <cr>
```

Handler ` RVA 0xBDC8C10 `；selector ` 0 `；EOL ` RVA 0x338EC018 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-f669cca3b17ec3f2](../../evidence/conditions-sets-095.md#c-f669cca3b17ec3f2) · [状态效果 S-8f12b474cc1dcfeb](../../evidence/state_effects-sets-030.md#s-8f12b474cc1dcfeb)

### observed_connections-008988

```text
(config-ecfm)# default mep archive-hold-time <cr>
```

Handler ` RVA 0xBDC8830 `；selector ` 0 `；EOL ` RVA 0x338EAFB8 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-311cb5e2ffcf1bca](../../evidence/conditions-sets-019.md#c-311cb5e2ffcf1bca) · [状态效果 S-8f12b474cc1dcfeb](../../evidence/state_effects-sets-030.md#s-8f12b474cc1dcfeb)

### observed_connections-008994

```text
(config-ecfm)# default mep ccm-fastage <cr>
```

Handler ` RVA 0xBDC8AC0 `；selector ` 0 `；EOL ` RVA 0x338EB5C0 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-c370baf3775d4372](../../evidence/conditions-sets-075.md#c-c370baf3775d4372) · [状态效果 S-8f12b474cc1dcfeb](../../evidence/state_effects-sets-030.md#s-8f12b474cc1dcfeb)

### observed_connections-008991

```text
(config-ecfm)# default mep ccm-hold-time <cr>
```

Handler ` RVA 0xBDC8980 `；selector ` 0 `；EOL ` RVA 0x338EB2D0 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-84273096e008cb90](../../evidence/conditions-sets-051.md#c-84273096e008cb90) · [状态效果 S-8f12b474cc1dcfeb](../../evidence/state_effects-sets-030.md#s-8f12b474cc1dcfeb)

### observed_connections-008996

```text
(config-ecfm)# default mip auto-create <cr>
```

Handler ` RVA 0xBDC9360 `；selector ` 0 `；EOL ` RVA 0x338EBD08 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-ecc51b45d1086d78](../../evidence/conditions-sets-091.md#c-ecc51b45d1086d78) · [状态效果 S-5bf2b4c72b365294](../../evidence/state_effects-sets-020.md#s-5bf2b4c72b365294)

### observed_connections-008980

```text
(config-ecfm)# default sender-id <cr>
```

Handler ` RVA 0xBDC9210 `；selector ` 0 `；EOL ` RVA 0x338EB908 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-7a052aefc1eed369](../../evidence/conditions-sets-047.md#c-7a052aefc1eed369) · [状态效果 S-8f12b474cc1dcfeb](../../evidence/state_effects-sets-030.md#s-8f12b474cc1dcfeb)

### observed_connections-008998

```text
(config-ecfm)# default service port <cr>
```

Handler ` RVA 0xBDC70A0 `；selector ` 0 `；EOL ` RVA 0x338EA290 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-335b517933916c94](../../evidence/conditions-sets-020.md#c-335b517933916c94) · [状态效果 S-6da56a34555aa09d](../../evidence/state_effects-sets-023.md#s-6da56a34555aa09d)

### observed_connections-008977

```text
(config-ecfm)# exit <cr>
```

Handler ` RVA 0xBDBE570 `；selector ` 0 `；EOL ` RVA 0x338CA218 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-39cd7244555f8184](../../evidence/conditions-sets-022.md#c-39cd7244555f8184)

### observed_connections-008982

```text
(config-ecfm)# id null <cr>
```

Handler ` RVA 0xBDC8C10 `；selector ` 0 `；EOL ` RVA 0x338EC018 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f57512c49982b6f8](../../evidence/conditions-sets-095.md#c-f57512c49982b6f8) · [状态效果 S-7a20ea4b93fc045c](../../evidence/state_effects-sets-026.md#s-7a20ea4b93fc045c)

### observed_connections-008987

```text
(config-ecfm)# mep archive-hold-time <number:1..65535> <cr>
```

Handler ` RVA 0xBDC8830 `；selector ` 0 `；EOL ` RVA 0x338EAFB8 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` minutes (default 100)。

[条件 C-13f556cc7b27aabb](../../evidence/conditions-sets-008.md#c-13f556cc7b27aabb) · [参数 P-41a0a554417bbc92](../../evidence/parameters-sets-006.md#p-41a0a554417bbc92)

### observed_connections-008993

```text
(config-ecfm)# mep ccm-fastage enable <cr>
```

Handler ` RVA 0xBDC8AC0 `；selector ` 0 `；EOL ` RVA 0x338EB5C0 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c799057a476d09b4](../../evidence/conditions-sets-077.md#c-c799057a476d09b4)

### observed_connections-008990

```text
(config-ecfm)# mep ccm-hold-time <number:1..48> <cr>
```

Handler ` RVA 0xBDC8980 `；selector ` 0 `；EOL ` RVA 0x338EB2D0 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` hour(s) (default 24)。

[条件 C-816938713f07a3f0](../../evidence/conditions-sets-050.md#c-816938713f07a3f0) · [参数 P-972b2f5eade8fa1b](../../evidence/parameters-sets-012.md#p-972b2f5eade8fa1b)

### observed_connections-008984

```text
(config-ecfm)# mip auto-create <cr>
```

Handler ` RVA 0xBDC9360 `；selector ` 0 `；EOL ` RVA 0x338EBD08 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ecc51b45d1086d78](../../evidence/conditions-sets-091.md#c-ecc51b45d1086d78) · [状态效果 S-c74dcb0e046ee290](../../evidence/state_effects-sets-042.md#s-c74dcb0e046ee290)

### observed_connections-008981

```text
(config-ecfm)# no id <cr>
```

Handler ` RVA 0xBDC8C10 `；selector ` 0 `；EOL ` RVA 0x338EC018 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-62d4c2b8e99453ae](../../evidence/conditions-sets-038.md#c-62d4c2b8e99453ae) · [状态效果 S-7deba8c62a140627](../../evidence/state_effects-sets-027.md#s-7deba8c62a140627)

### observed_connections-008986

```text
(config-ecfm)# no mep archive-hold-time <cr>
```

Handler ` RVA 0xBDC8830 `；selector ` 0 `；EOL ` RVA 0x338EAFB8 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-d5e729389eba3451](../../evidence/conditions-sets-083.md#c-d5e729389eba3451) · [状态效果 S-7deba8c62a140627](../../evidence/state_effects-sets-027.md#s-7deba8c62a140627)

### observed_connections-008992

```text
(config-ecfm)# no mep ccm-fastage <cr>
```

Handler ` RVA 0xBDC8AC0 `；selector ` 0 `；EOL ` RVA 0x338EB5C0 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-297b97646790726b](../../evidence/conditions-sets-016.md#c-297b97646790726b) · [状态效果 S-7deba8c62a140627](../../evidence/state_effects-sets-027.md#s-7deba8c62a140627)

### observed_connections-008989

```text
(config-ecfm)# no mep ccm-hold-time <cr>
```

Handler ` RVA 0xBDC8980 `；selector ` 0 `；EOL ` RVA 0x338EB2D0 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0ee816254d5b477c](../../evidence/conditions-sets-006.md#c-0ee816254d5b477c) · [状态效果 S-7deba8c62a140627](../../evidence/state_effects-sets-027.md#s-7deba8c62a140627)

### observed_connections-008995

```text
(config-ecfm)# no mip auto-create <cr>
```

Handler ` RVA 0xBDC9360 `；selector ` 0 `；EOL ` RVA 0x338EBD08 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-ecc51b45d1086d78](../../evidence/conditions-sets-091.md#c-ecc51b45d1086d78) · [状态效果 S-87160df09b72e0e4](../../evidence/state_effects-sets-029.md#s-87160df09b72e0e4)

### observed_connections-008978

```text
(config-ecfm)# no sender-id <cr>
```

Handler ` RVA 0xBDC9210 `；selector ` 0 `；EOL ` RVA 0x338EB908 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-0d232f1e21871cb9](../../evidence/conditions-sets-005.md#c-0d232f1e21871cb9) · [状态效果 S-7deba8c62a140627](../../evidence/state_effects-sets-027.md#s-7deba8c62a140627)

### observed_connections-008997

```text
(config-ecfm)# no service port <cr>
```

Handler ` RVA 0xBDC70A0 `；selector ` 0 `；EOL ` RVA 0x338EA290 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-335b517933916c94](../../evidence/conditions-sets-020.md#c-335b517933916c94) · [状态效果 S-ad82b25e9b7f37ce](../../evidence/state_effects-sets-037.md#s-ad82b25e9b7f37ce)

### observed_connections-008979

```text
(config-ecfm)# sender-id chassis <cr>
```

Handler ` RVA 0xBDC9210 `；selector ` 0 `；EOL ` RVA 0x338EB908 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6e2938e7214b69e6](../../evidence/conditions-sets-043.md#c-6e2938e7214b69e6) · [状态效果 S-354e87712c42d5ff](../../evidence/state_effects-sets-012.md#s-354e87712c42d5ff)

### observed_connections-008985

```text
(config-ecfm)# service port <cr>
```

Handler ` RVA 0xBDC70A0 `；selector ` 0 `；EOL ` RVA 0x338EA290 `。

模式根 ` RVA 0x338CA080 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-335b517933916c94](../../evidence/conditions-sets-020.md#c-335b517933916c94) · [状态效果 S-8ab8a3f6d7c974ad](../../evidence/state_effects-sets-029.md#s-8ab8a3f6d7c974ad)

