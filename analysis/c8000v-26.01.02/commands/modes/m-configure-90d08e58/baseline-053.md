# configure · 六个基础模式的历史连接

[模式索引](README.md) · [总索引](../../README.md)

### path-052008

```text
(config)# do-exec show event manager history traps <cr>
```

Handler ` RVA 0x1106B990 `；selector ` 0 `；EOL ` RVA 0x35383850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-fcf91542de83b9d1](../../evidence/state_effects-sets-054.md#s-fcf91542de83b9d1)

### path-051996

```text
(config)# do-exec show event manager policy pending <cr>
```

Handler ` RVA 0xC0CC560 `；selector ` 0 `；EOL ` RVA 0x339A0CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4c8c21a147cb6df2](../../evidence/state_effects-sets-017.md#s-4c8c21a147cb6df2)

### path-063001

```text
(config)# do-exec show event manager policy pending class range A - A <cr>
```

Handler ` RVA 0xC0CC560 `；selector ` 0 `；EOL ` RVA 0x339A0CC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a5efd93998130a9d](../../evidence/conditions-sets-064.md#c-a5efd93998130a9d) · [缺口 G-0f6b8aa25a96cb72](../../evidence/gaps-sets-001.md#g-0f6b8aa25a96cb72) · [状态效果 S-58fb51147e3af3e8](../../evidence/state_effects-sets-019.md#s-58fb51147e3af3e8)

### path-052010

```text
(config)# do-exec show event manager scheduler thread <cr>
```

Handler ` RVA 0xC0CC8E0 `；selector ` 0 `；EOL ` RVA 0x339A55C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056731

```text
(config)# do-exec show event manager session cli username <cr>
```

Handler ` RVA 0xC0CC870 `；selector ` 0 `；EOL ` RVA 0x339A42D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-052005

```text
(config)# do-exec show event manager statistics server <cr>
```

Handler ` RVA 0xC0CC480 `；selector ` 0 `；EOL ` RVA 0x339A58F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-39da89a72ab607fb](../../evidence/state_effects-sets-013.md#s-39da89a72ab607fb)

### path-043727

```text
(config)# do-exec show event manager trace <cr>
```

Handler ` RVA 0xC0CC790 `；selector ` 0 `；EOL ` RVA 0x339A4CA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-043722

```text
(config)# do-exec show event manager version <cr>
```

Handler ` RVA 0xC0CC720 `；selector ` 0 `；EOL ` RVA 0x339A49F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032863

```text
(config)# do-exec show event-manager consumers <cr>
```

Handler ` RVA 0xD2C5AE0 `；selector ` 0 `；EOL ` RVA 0x33DF80A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026365

```text
(config)# do-exec show exception <cr>
```

Handler ` RVA 0xE8D9080 `；selector ` 3 `；EOL ` RVA 0x341240A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eaa78769c8f7581a](../../evidence/conditions-sets-091.md#c-eaa78769c8f7581a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028156

```text
(config)# do-exec show exception dumpfile <cr>
```

Handler ` RVA 0xE8D9080 `；selector ` 0 `；EOL ` RVA 0x34123E00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eaa78769c8f7581a](../../evidence/conditions-sets-091.md#c-eaa78769c8f7581a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028117

```text
(config)# do-exec show exception dumphost <cr>
```

Handler ` RVA 0xE8D9080 `；selector ` 3 `；EOL ` RVA 0x34123B58 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-eaa78769c8f7581a](../../evidence/conditions-sets-091.md#c-eaa78769c8f7581a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029197

```text
(config)# do-exec show facility-ains card <cr>
```

Handler ` RVA 0xC29A530 `；selector ` 0 `；EOL ` RVA 0x33A27088 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7b9ab4a299d1ed0](../../evidence/conditions-sets-077.md#c-c7b9ab4a299d1ed0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029264

```text
(config)# do-exec show facility-ains ports <cr>
```

Handler ` RVA 0xC29A650 `；selector ` 0 `；EOL ` RVA 0x33A27330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7b9ab4a299d1ed0](../../evidence/conditions-sets-077.md#c-c7b9ab4a299d1ed0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029142

```text
(config)# do-exec show facility-ains status <cr>
```

Handler ` RVA 0xC29A6E0 `；selector ` 0 `；EOL ` RVA 0x33A26DE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7b9ab4a299d1ed0](../../evidence/conditions-sets-077.md#c-c7b9ab4a299d1ed0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029306

```text
(config)# do-exec show facility-ains transceiver <cr>
```

Handler ` RVA 0xC29A5C0 `；selector ` 0 `；EOL ` RVA 0x33A275D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c7b9ab4a299d1ed0](../../evidence/conditions-sets-077.md#c-c7b9ab4a299d1ed0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-035305

```text
(config)# do-exec show facility-alarm relay minor <cr>
```

Handler ` RVA 0xC29ADB0 `；selector ` 0 `；EOL ` RVA 0x33A269E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8cef438a5c87be4f](../../evidence/conditions-sets-055.md#c-8cef438a5c87be4f) · [状态效果 S-b65ca7ab441789b9](../../evidence/state_effects-sets-039.md#s-b65ca7ab441789b9)

### path-029176

```text
(config)# do-exec show facility-alarm status <cr>
```

Handler ` RVA 0xC29A7B0 `；selector ` 0 `；EOL ` RVA 0x33A265A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6107f5cb54a5fa96](../../evidence/state_effects-sets-021.md#s-6107f5cb54a5fa96)

### path-029251

```text
(config)# do-exec show facility-condition status <cr>
```

Handler ` RVA 0xC29A250 `；selector ` 0 `；EOL ` RVA 0x33A27930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ab69cdcc7eb4a969](../../evidence/conditions-sets-066.md#c-ab69cdcc7eb4a969) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-029332

```text
(config)# do-exec show facility-protocols status <cr>
```

Handler ` RVA 0xC29B170 `；selector ` 0 `；EOL ` RVA 0x33A27C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-31ae46631da6eef6](../../evidence/conditions-sets-019.md#c-31ae46631da6eef6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033256

```text
(config)# do-exec show fallback profile <cr>
```

Handler ` RVA 0xCB4B8A0 `；selector ` 0 `；EOL ` RVA 0x33BE2CC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-bf4453e684cfa970](../../evidence/state_effects-sets-040.md#s-bf4453e684cfa970)

### path-031919

```text
(config)# do-exec show fast-reroute database <cr>
```

Handler ` RVA 0xB585600 `；selector ` 0 `；EOL ` RVA 0x337A56A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-36476b197182c666](../../evidence/conditions-sets-021.md#c-36476b197182c666) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027719

```text
(config)# do-exec show fastblk <cr>
```

Handler ` RVA 0x1133B470 `；selector ` 0 `；EOL ` RVA 0x3549D6C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027617

```text
(config)# do-exec show fhrp <cr>
```

Handler ` RVA 0x13387130 `；selector ` 0 `；EOL ` RVA 0x35A78DF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d0c32ac3d2b0414b](../../evidence/conditions-sets-080.md#c-d0c32ac3d2b0414b) · [状态效果 S-a289250bd86f6bd8](../../evidence/state_effects-sets-034.md#s-a289250bd86f6bd8)

### path-060714

```text
(config)# do-exec show fhrp <interface> <cr>
```

Handler ` RVA 0x13387130 `；selector ` 0 `；EOL ` RVA 0x35A78DF0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fde2afbad824f09c](../../evidence/conditions-sets-098.md#c-fde2afbad824f09c) · [缺口 G-2a96f16db596c0e6](../../evidence/gaps-sets-002.md#g-2a96f16db596c0e6) · [参数 P-bcfff0df67583ca6](../../evidence/parameters-sets-014.md#p-bcfff0df67583ca6) · [状态效果 S-a289250bd86f6bd8](../../evidence/state_effects-sets-034.md#s-a289250bd86f6bd8)

### path-033310

```text
(config)# do-exec show file descriptors <cr>
```

Handler ` RVA 0xD6506F0 `；selector ` 0 `；EOL ` RVA 0x33EBA978 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-4189475e824249c5](../../evidence/state_effects-sets-014.md#s-4189475e824249c5)

### path-061171

```text
(config)# do-exec show file information <url:dynamic> <cr>
```

Handler ` RVA 0xD650B00 `；selector ` 0 `；EOL ` RVA 0x33EBACB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a510eef822c770c0](../../evidence/conditions-sets-064.md#c-a510eef822c770c0) · [缺口 G-81de65c8d9815fbe](../../evidence/gaps-sets-005.md#g-81de65c8d9815fbe) · [参数 P-c4d91dda3ad9f9c6](../../evidence/parameters-sets-015.md#p-c4d91dda3ad9f9c6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033280

```text
(config)# do-exec show file systems <cr>
```

Handler ` RVA 0xD64FEB0 `；selector ` 0 `；EOL ` RVA 0x33EBA658 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027688

```text
(config)# do-exec show flooding-suppression <cr>
```

Handler ` RVA 0x136B3070 `；selector ` 1 `；EOL ` RVA 0x35C05C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037880

```text
(config)# do-exec show flow config log <cr>
```

Handler ` RVA 0xC1FE8A0 `；selector ` 0 `；EOL ` RVA 0x33A07AC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f31f38c12ec1db19](../../evidence/conditions-sets-094.md#c-f31f38c12ec1db19) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060938

```text
(config)# do-exec show flow config state <cr>
```

Handler ` RVA 0xC1FE010 `；selector ` 0 `；EOL ` RVA 0x33A077D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad390dd9aeaa985c](../../evidence/conditions-sets-067.md#c-ad390dd9aeaa985c) · [缺口 G-a5be4ed6063c6650](../../evidence/gaps-sets-006.md#g-a5be4ed6063c6650) · [状态效果 S-c7cb9ffd33f1ead2](../../evidence/state_effects-sets-042.md#s-c7cb9ffd33f1ead2)

### path-037787

```text
(config)# do-exec show flow config transactions <cr>
```

Handler ` RVA 0xC1FDB10 `；selector ` 0 `；EOL ` RVA 0x33A07490 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cd9804c1be05ff03](../../evidence/conditions-sets-079.md#c-cd9804c1be05ff03) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060948

```text
(config)# do-exec show flow exporter <?option@555588f39878> <cr>
```

Handler ` RVA 0xC154980 `；selector ` 0 `；EOL ` RVA 0x339E50A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1615965a25a49c3c](../../evidence/conditions-sets-009.md#c-1615965a25a49c3c) · [缺口 G-9e0456b87760e736](../../evidence/gaps-sets-006.md#g-9e0456b87760e736) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061459

```text
(config)# do-exec show flow exporter <?option@555588f39878> statistics <cr>
```

Handler ` RVA 0xC154900 `；selector ` 0 `；EOL ` RVA 0x339E4DD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-27a7d9f7ebc34403](../../evidence/conditions-sets-016.md#c-27a7d9f7ebc34403) · [缺口 G-9e0456b87760e736](../../evidence/gaps-sets-006.md#g-9e0456b87760e736) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061462

```text
(config)# do-exec show flow exporter <?option@555588f39878> templates <cr>
```

Handler ` RVA 0xC154880 `；selector ` 0 `；EOL ` RVA 0x339E5110 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1615965a25a49c3c](../../evidence/conditions-sets-009.md#c-1615965a25a49c3c) · [缺口 G-9e0456b87760e736](../../evidence/gaps-sets-006.md#g-9e0456b87760e736) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062027

```text
(config)# do-exec show flow exporter <?option@555588f39878> templates details <cr>
```

Handler ` RVA 0xC154800 `；selector ` 0 `；EOL ` RVA 0x339E50E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1615965a25a49c3c](../../evidence/conditions-sets-009.md#c-1615965a25a49c3c) · [缺口 G-9e0456b87760e736](../../evidence/gaps-sets-006.md#g-9e0456b87760e736) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030969

```text
(config)# do-exec show flow exporter <cr>
```

Handler ` RVA 0xC154980 `；selector ` 0 `；EOL ` RVA 0x339E50A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67e88299d2bec772](../../evidence/conditions-sets-040.md#c-67e88299d2bec772) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037823

```text
(config)# do-exec show flow exporter broker <cr>
```

Handler ` RVA 0xC216310 `；selector ` 0 `；EOL ` RVA 0x33A0F3E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061442

```text
(config)# do-exec show flow exporter export-ids <?option@555588f38100> <cr>
```

Handler ` RVA 0xC154750 `；selector ` 0 `；EOL ` RVA 0x339E4168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7656b868a2bec319](../../evidence/conditions-sets-046.md#c-7656b868a2bec319) · [缺口 G-9f583096fe6f2287](../../evidence/gaps-sets-006.md#g-9f583096fe6f2287) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054322

```text
(config)# do-exec show flow exporter option application engines <cr>
```

Handler ` RVA 0xC154660 `；selector ` 0 `；EOL ` RVA 0x339FD9E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfd5e7ef26a8ef4e](../../evidence/conditions-sets-080.md#c-cfd5e7ef26a8ef4e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054303

```text
(config)# do-exec show flow exporter option application table <cr>
```

Handler ` RVA 0xC154500 `；selector ` 0 `；EOL ` RVA 0x339FD738 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cfd5e7ef26a8ef4e](../../evidence/conditions-sets-080.md#c-cfd5e7ef26a8ef4e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037753

```text
(config)# do-exec show flow exporter statistics <cr>
```

Handler ` RVA 0xC154900 `；selector ` 0 `；EOL ` RVA 0x339E4450 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b5d58dd6b571ce9](../../evidence/conditions-sets-030.md#c-4b5d58dd6b571ce9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037864

```text
(config)# do-exec show flow exporter templates <cr>
```

Handler ` RVA 0xC154880 `；selector ` 0 `；EOL ` RVA 0x339E4788 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b5d58dd6b571ce9](../../evidence/conditions-sets-030.md#c-4b5d58dd6b571ce9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047131

```text
(config)# do-exec show flow exporter templates details <cr>
```

Handler ` RVA 0xC154800 `；selector ` 0 `；EOL ` RVA 0x339E4760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4b5d58dd6b571ce9](../../evidence/conditions-sets-030.md#c-4b5d58dd6b571ce9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030874

```text
(config)# do-exec show flow interface <cr>
```

Handler ` RVA 0xC18EB40 `；selector ` 0 `；EOL ` RVA 0x339EAB20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8186e4b1d503d7cc](../../evidence/conditions-sets-050.md#c-8186e4b1d503d7cc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060927

```text
(config)# do-exec show flow interface <interface> <cr>
```

Handler ` RVA 0xC18EB40 `；selector ` 0 `；EOL ` RVA 0x339EAB20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bb012c791a916b2f](../../evidence/conditions-sets-072.md#c-bb012c791a916b2f) · [缺口 G-9ecc33c93143aaf2](../../evidence/gaps-sets-006.md#g-9ecc33c93143aaf2) · [参数 P-822084f7d6d22061](../../evidence/parameters-sets-010.md#p-822084f7d6d22061) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030783

```text
(config)# do-exec show flow internal <cr>
```

Handler ` RVA 0xC14B000 `；selector ` 0 `；EOL ` RVA 0x339E2C18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061428

```text
(config)# do-exec show flow internal field <?option@555588f36bf0> <cr>
```

Handler ` RVA 0xC14B000 `；selector ` 0 `；EOL ` RVA 0x339E2C18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-65b9d517153bc784](../../evidence/conditions-sets-039.md#c-65b9d517153bc784) · [缺口 G-7df69c8b1d5eb5e3](../../evidence/gaps-sets-005.md#g-7df69c8b1d5eb5e3) · [状态效果 S-c4ad16b14de5e941](../../evidence/state_effects-sets-042.md#s-c4ad16b14de5e941)

### path-062807

```text
(config)# do-exec show flow monitor <?option@555588f3f338> <cr>
```

Handler ` RVA 0xC18F560 `；selector ` 0 `；EOL ` RVA 0x339ED650 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5b08740b5e20b776](../../evidence/conditions-sets-036.md#c-5b08740b5e20b776) · [缺口 G-c7dcc10a2809e8d4](../../evidence/gaps-sets-007.md#g-c7dcc10a2809e8d4) · [状态效果 S-eb9bf5cd2b7c6ed1](../../evidence/state_effects-sets-050.md#s-eb9bf5cd2b7c6ed1)

### path-031045

```text
(config)# do-exec show flow monitor <cr>
```

Handler ` RVA 0xC18F560 `；selector ` 0 `；EOL ` RVA 0x339ED650 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5bb68754b97d02b7](../../evidence/conditions-sets-036.md#c-5bb68754b97d02b7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037735

```text
(config)# do-exec show flow monitor all <cr>
```

Handler ` RVA 0xC18F560 `；selector ` 0 `；EOL ` RVA 0x339E97C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-955c117c98936d1a](../../evidence/conditions-sets-058.md#c-955c117c98936d1a) · [状态效果 S-d6a4191ae333274c](../../evidence/state_effects-sets-045.md#s-d6a4191ae333274c)

### path-038076

```text
(config)# do-exec show flow monitor broker <cr>
```

Handler ` RVA 0xC22A520 `；selector ` 0 `；EOL ` RVA 0x33A11430 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e58703f6ee26dada](../../evidence/conditions-sets-089.md#c-e58703f6ee26dada) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030951

```text
(config)# do-exec show flow record <cr>
```

Handler ` RVA 0xC1D8180 `；selector ` 0 `；EOL ` RVA 0x339F9880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-19ece40e31ca854f](../../evidence/conditions-sets-010.md#c-19ece40e31ca854f) · [状态效果 S-6ff06c21afd69914](../../evidence/state_effects-sets-024.md#s-6ff06c21afd69914)

### path-060686

```text
(config)# do-exec show flow record <cr>
```

Handler ` RVA 0xC1D8180 `；selector ` 0 `；EOL ` RVA 0x339F9880 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-373481d54eca880f](../../evidence/conditions-sets-021.md#c-373481d54eca880f) · [缺口 G-f529cafa9f6c2a74](../../evidence/gaps-sets-008.md#g-f529cafa9f6c2a74) · [状态效果 S-f70ebb1173e4418a](../../evidence/state_effects-sets-052.md#s-f70ebb1173e4418a)

### path-037774

```text
(config)# do-exec show flow record broker <cr>
```

Handler ` RVA 0xC21C800 `；selector ` 0 `；EOL ` RVA 0x33A0FC10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062526

```text
(config)# do-exec show flow service instance id <number:1..16384> interface <interface> <cr>
```

Handler ` RVA 0xC18EC20 `；selector ` 0 `；EOL ` RVA 0x339EAFE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` Identifier。

[条件 C-61f3ac9f9bdfd8c6](../../evidence/conditions-sets-038.md#c-61f3ac9f9bdfd8c6) · [缺口 G-b6cf0a29f1ecaa4d](../../evidence/gaps-sets-006.md#g-b6cf0a29f1ecaa4d) · [参数 P-2047b6e03f25c1ec](../../evidence/parameters-sets-003.md#p-2047b6e03f25c1ec) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027810

```text
(config)# do-exec show flowcontrol <cr>
```

Handler ` RVA 0x15E61FD0 `；selector ` 0 `；EOL ` RVA 0x35E29930 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a179bc921e7013de](../../evidence/conditions-sets-062.md#c-a179bc921e7013de) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061195

```text
(config)# do-exec show flowcontrol interface <interface> <cr>
```

Handler ` RVA 0x15E61FD0 `；selector ` 2 `；EOL ` RVA 0x35E29608 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa90fbd70fa4853c](../../evidence/conditions-sets-066.md#c-aa90fbd70fa4853c) · [缺口 G-de2e8c0291969162](../../evidence/gaps-sets-008.md#g-de2e8c0291969162) · [参数 P-bf7a9765dc38820b](../../evidence/parameters-sets-015.md#p-bf7a9765dc38820b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061197

```text
(config)# do-exec show flowcontrol module <number:dynamic> <cr>
```

Handler ` RVA 0x15E61FD0 `；selector ` 1 `；EOL ` RVA 0x35E29A38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Module number。

[条件 C-b0248730725b3401](../../evidence/conditions-sets-068.md#c-b0248730725b3401) · [缺口 G-b0ccd2b8fcdbc931](../../evidence/gaps-sets-006.md#g-b0ccd2b8fcdbc931) · [参数 P-ca62c826aa47522a](../../evidence/parameters-sets-015.md#p-ca62c826aa47522a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061198

```text
(config)# do-exec show flowcontrol switch <number:dynamic> <cr>
```

Handler ` RVA 0x15E61FD0 `；selector ` 0 `；EOL ` RVA 0x35E29930 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` Switch Number。

[条件 C-9fbed78b24782f29](../../evidence/conditions-sets-062.md#c-9fbed78b24782f29) · [缺口 G-bc56ee6a57031a0e](../../evidence/gaps-sets-007.md#g-bc56ee6a57031a0e) · [参数 P-c1e4858905f5052b](../../evidence/parameters-sets-015.md#p-c1e4858905f5052b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033883

```text
(config)# do-exec show flowspec afi-all <cr>
```

Handler ` RVA 0x13448E20 `；selector ` 0 `；EOL ` RVA 0x35A942B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bae01448879552dc](../../evidence/conditions-sets-072.md#c-bae01448879552dc) · [状态效果 S-d87f8e13777f6695](../../evidence/state_effects-sets-046.md#s-d87f8e13777f6695)

### path-061803

```text
(config)# do-exec show flowspec afi-all nlri <hex-data> <cr>
```

Handler ` RVA 0x13448E20 `；selector ` 0 `；EOL ` RVA 0x35A942B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexdata ` Enter NLRI hex string。

[条件 C-c21e8fe217e5b395](../../evidence/conditions-sets-075.md#c-c21e8fe217e5b395) · [缺口 G-dbafa8455ab46bc3](../../evidence/gaps-sets-008.md#g-dbafa8455ab46bc3) · [参数 P-70b8a336002e4c18](../../evidence/parameters-sets-009.md#p-70b8a336002e4c18) · [状态效果 S-e10e52ee3ede7b52](../../evidence/state_effects-sets-048.md#s-e10e52ee3ede7b52)

### path-033848

```text
(config)# do-exec show flowspec client <cr>
```

Handler ` RVA 0x13448CA0 `；selector ` 2 `；EOL ` RVA 0x35A93970 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f530e9027a0bd1f7](../../evidence/state_effects-sets-052.md#s-f530e9027a0bd1f7)

### path-033854

```text
(config)# do-exec show flowspec summary <cr>
```

Handler ` RVA 0x13448CA0 `；selector ` 0 `；EOL ` RVA 0x35A93CE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-bb33a5c74448cf51](../../evidence/state_effects-sets-040.md#s-bb33a5c74448cf51)

### path-036602

```text
(config)# do-exec show fmm db alarm <cr>
```

Handler ` RVA 0x1695FBF0 `；selector ` 0 `；EOL ` RVA 0x3602D058 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045898

```text
(config)# do-exec show fmm db condition conditions <cr>
```

Handler ` RVA 0x1695FAB0 `；selector ` 0 `；EOL ` RVA 0x3602C570 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045841

```text
(config)# do-exec show fmm db condition profiles <cr>
```

Handler ` RVA 0x1695FA60 `；selector ` 0 `；EOL ` RVA 0x3602C2C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053229

```text
(config)# do-exec show fmm db flow data basic <cr>
```

Handler ` RVA 0x1695F600 `；selector ` 0 `；EOL ` RVA 0x36029C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053331

```text
(config)# do-exec show fmm db flow data ip <cr>
```

Handler ` RVA 0x1695F6A0 `；selector ` 0 `；EOL ` RVA 0x3602A190 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053284

```text
(config)# do-exec show fmm db flow data l2vlan <cr>
```

Handler ` RVA 0x1695F650 `；selector ` 0 `；EOL ` RVA 0x36029EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053464

```text
(config)# do-exec show fmm db flow data rtp <cr>
```

Handler ` RVA 0x1695F790 `；selector ` 0 `；EOL ` RVA 0x3602A988 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053420

```text
(config)# do-exec show fmm db flow data tcp <cr>
```

Handler ` RVA 0x1695F740 `；selector ` 0 `；EOL ` RVA 0x3602A6E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053374

```text
(config)# do-exec show fmm db flow data udp <cr>
```

Handler ` RVA 0x1695F6F0 `；selector ` 0 `；EOL ` RVA 0x3602A438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053275

```text
(config)# do-exec show fmm db flow metrics common <cr>
```

Handler ` RVA 0x1695F7E0 `；selector ` 0 `；EOL ` RVA 0x3602AC90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053416

```text
(config)# do-exec show fmm db flow metrics ipcbr <cr>
```

Handler ` RVA 0x1695F8D0 `；selector ` 0 `；EOL ` RVA 0x3602B488 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053324

```text
(config)# do-exec show fmm db flow metrics mdi <cr>
```

Handler ` RVA 0x1695F830 `；selector ` 0 `；EOL ` RVA 0x3602AF38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053369

```text
(config)# do-exec show fmm db flow metrics rtp <cr>
```

Handler ` RVA 0x1695F880 `；selector ` 0 `；EOL ` RVA 0x3602B1E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036485

```text
(config)# do-exec show fmm db groups <cr>
```

Handler ` RVA 0x1695FB00 `；selector ` 0 `；EOL ` RVA 0x3602C808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045784

```text
(config)# do-exec show fmm db interval common <cr>
```

Handler ` RVA 0x1695F920 `；selector ` 0 `；EOL ` RVA 0x3602B7B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045961

```text
(config)# do-exec show fmm db interval ipcbr <cr>
```

Handler ` RVA 0x1695FA10 `；selector ` 0 `；EOL ` RVA 0x3602BFB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045855

```text
(config)# do-exec show fmm db interval mdi <cr>
```

Handler ` RVA 0x1695F970 `；selector ` 0 `；EOL ` RVA 0x3602BA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045907

```text
(config)# do-exec show fmm db interval rtp <cr>
```

Handler ` RVA 0x1695F9C0 `；selector ` 0 `；EOL ` RVA 0x3602BD08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-036216

```text
(config)# do-exec show fmm db monitor <cr>
```

Handler ` RVA 0x1695F5B0 `；selector ` 0 `；EOL ` RVA 0x360298C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045995

```text
(config)# do-exec show fmm db set flows <cr>
```

Handler ` RVA 0x1695FBA0 `；selector ` 0 `；EOL ` RVA 0x3602CDC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-045940

```text
(config)# do-exec show fmm db set sets <cr>
```

Handler ` RVA 0x1695FB50 `；selector ` 0 `；EOL ` RVA 0x3602CB18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027784

```text
(config)# do-exec show format <cr>
```

Handler ` RVA 0xF414BC0 `；selector ` 0 `；EOL ` RVA 0x34641FC0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1ec6f2749cfa0af4](../../evidence/conditions-sets-012.md#c-1ec6f2749cfa0af4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060747

```text
(config)# do-exec show format <url:dynamic> <cr>
```

Handler ` RVA 0xF414BC0 `；selector ` 0 `；EOL ` RVA 0x34641FC0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c427f96c4e1db99](../../evidence/conditions-sets-030.md#c-4c427f96c4e1db99) · [缺口 G-7d541839e0aa7ce1](../../evidence/gaps-sets-005.md#g-7d541839e0aa7ce1) · [参数 P-5e7267f44e4f728c](../../evidence/parameters-sets-008.md#p-5e7267f44e4f728c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061184

```text
(config)# do-exec show format <url:dynamic> validate <cr>
```

Handler ` RVA 0xF414A60 `；selector ` 0 `；EOL ` RVA 0x34642240 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4c427f96c4e1db99](../../evidence/conditions-sets-030.md#c-4c427f96c4e1db99) · [缺口 G-7d541839e0aa7ce1](../../evidence/gaps-sets-005.md#g-7d541839e0aa7ce1) · [参数 P-5e7267f44e4f728c](../../evidence/parameters-sets-008.md#p-5e7267f44e4f728c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033632

```text
(config)# do-exec show format validate <cr>
```

Handler ` RVA 0xF414A60 `；selector ` 0 `；EOL ` RVA 0x34642240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb535702d0316d4b](../../evidence/conditions-sets-072.md#c-bb535702d0316d4b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027699

```text
(config)# do-exec show fqdn <cr>
```

Handler ` RVA 0xC2E0FF0 `；selector ` 0 `；EOL ` RVA 0x33A3C390 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041006

```text
(config)# do-exec show frame-relay end-to-end keepalive <cr>
```

Handler ` RVA 0xF630D90 `；selector ` 0 `；EOL ` RVA 0x34710498 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2fd6c0cc827db6fb](../../evidence/conditions-sets-019.md#c-2fd6c0cc827db6fb) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062152

```text
(config)# do-exec show frame-relay end-to-end keepalive interface <interface> <cr>
```

Handler ` RVA 0xF630D90 `；selector ` 0 `；EOL ` RVA 0x34710498 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-36ab5cc68694f44f](../../evidence/conditions-sets-021.md#c-36ab5cc68694f44f) · [缺口 G-87d7cefcb7c45795](../../evidence/gaps-sets-005.md#g-87d7cefcb7c45795) · [参数 P-0c0967de6785c4ba](../../evidence/parameters-sets-001.md#p-0c0967de6785c4ba) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032365

```text
(config)# do-exec show frame-relay fragment <cr>
```

Handler ` RVA 0xD2EE7F0 `；selector ` 99 `；EOL ` RVA 0x33E09DA8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0b109b6dfd434da2](../../evidence/conditions-sets-005.md#c-0b109b6dfd434da2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061057

```text
(config)# do-exec show frame-relay fragment <interface> <cr>
```

Handler ` RVA 0xD2EE7F0 `；selector ` 99 `；EOL ` RVA 0x33E09DA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-986b1ec13af85729](../../evidence/conditions-sets-059.md#c-986b1ec13af85729) · [缺口 G-c272ab721f882f4f](../../evidence/gaps-sets-007.md#g-c272ab721f882f4f) · [参数 P-27022a69d7a0347e](../../evidence/parameters-sets-003.md#p-27022a69d7a0347e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050177

```text
(config)# do-exec show frame-relay ip rtp header-compression <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x347068B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-29a18ffbaa6041ba](../../evidence/conditions-sets-016.md#c-29a18ffbaa6041ba) · [状态效果 S-6a941b96d6997c36](../../evidence/state_effects-sets-023.md#s-6a941b96d6997c36)

### path-062151

```text
(config)# do-exec show frame-relay ip rtp header-compression <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x347068B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1db547ccf916280d](../../evidence/conditions-sets-012.md#c-1db547ccf916280d) · [缺口 G-84a12cf35f00a9a4](../../evidence/gaps-sets-005.md#g-84a12cf35f00a9a4) · [参数 P-e0598c6cf328ed48](../../evidence/parameters-sets-017.md#p-e0598c6cf328ed48) · [状态效果 S-6a941b96d6997c36](../../evidence/state_effects-sets-023.md#s-6a941b96d6997c36)

### path-050144

```text
(config)# do-exec show frame-relay ip tcp header-compression <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x34706468 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8970f7c096235e5c](../../evidence/conditions-sets-053.md#c-8970f7c096235e5c) · [状态效果 S-714fbcd3c51a898b](../../evidence/state_effects-sets-024.md#s-714fbcd3c51a898b)

### path-062149

```text
(config)# do-exec show frame-relay ip tcp header-compression <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 8 `；EOL ` RVA 0x34706468 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4a0d7985c5bb7475](../../evidence/conditions-sets-029.md#c-4a0d7985c5bb7475) · [缺口 G-36572982cea49168](../../evidence/gaps-sets-002.md#g-36572982cea49168) · [参数 P-c21e71008274daa9](../../evidence/parameters-sets-015.md#p-c21e71008274daa9) · [状态效果 S-714fbcd3c51a898b](../../evidence/state_effects-sets-024.md#s-714fbcd3c51a898b)

### path-032193

```text
(config)# do-exec show frame-relay lmi <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 5 `；EOL ` RVA 0x346FDE90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8bcae7a7d1063aaf](../../evidence/conditions-sets-054.md#c-8bcae7a7d1063aaf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061022

```text
(config)# do-exec show frame-relay lmi <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 5 `；EOL ` RVA 0x346FDE90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f96ec4179330e7c2](../../evidence/conditions-sets-096.md#c-f96ec4179330e7c2) · [缺口 G-1e6372393f355bdf](../../evidence/gaps-sets-002.md#g-1e6372393f355bdf) · [参数 P-6bbeb00abf3c76ed](../../evidence/parameters-sets-008.md#p-6bbeb00abf3c76ed) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032153

```text
(config)# do-exec show frame-relay map <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 0 `；EOL ` RVA 0x346FCE48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0ed55f4dfcca5394](../../evidence/conditions-sets-006.md#c-0ed55f4dfcca5394) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061016

```text
(config)# do-exec show frame-relay map <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 0 `；EOL ` RVA 0x346FCE48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-29e22d6973a45de4](../../evidence/conditions-sets-016.md#c-29e22d6973a45de4) · [缺口 G-f6404e06abfde94a](../../evidence/gaps-sets-008.md#g-f6404e06abfde94a) · [参数 P-a0d2c8da41af61d6](../../evidence/parameters-sets-012.md#p-a0d2c8da41af61d6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032379

```text
(config)# do-exec show frame-relay multilink <cr>
```

Handler ` RVA 0xC4BF980 `；selector ` 129 `；EOL ` RVA 0x33AA5228 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-cdfbd3e8ef193715](../../evidence/conditions-sets-079.md#c-cdfbd3e8ef193715) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061063

```text
(config)# do-exec show frame-relay multilink <interface> <cr>
```

Handler ` RVA 0xC4BF980 `；selector ` 129 `；EOL ` RVA 0x33AA5228 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fe18749242d1ba73](../../evidence/conditions-sets-098.md#c-fe18749242d1ba73) · [缺口 G-e7ac503f935d64fe](../../evidence/gaps-sets-008.md#g-e7ac503f935d64fe) · [参数 P-b2885959629d0317](../../evidence/parameters-sets-014.md#p-b2885959629d0317) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032209

```text
(config)# do-exec show frame-relay pvc <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 2 `；EOL ` RVA 0x346FD508 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-99edcadf1eb73b6a](../../evidence/conditions-sets-059.md#c-99edcadf1eb73b6a) · [状态效果 S-2d32454652ecf155](../../evidence/state_effects-sets-010.md#s-2d32454652ecf155)

### path-061029

```text
(config)# do-exec show frame-relay pvc <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 2 `；EOL ` RVA 0x346FD508 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-fa8539011cf9d382](../../evidence/conditions-sets-097.md#c-fa8539011cf9d382) · [缺口 G-9bd5779da4972ad3](../../evidence/gaps-sets-006.md#g-9bd5779da4972ad3) · [参数 P-2e0459c18d51caf3](../../evidence/parameters-sets-004.md#p-2e0459c18d51caf3) · [状态效果 S-2d32454652ecf155](../../evidence/state_effects-sets-010.md#s-2d32454652ecf155)

### path-032207

```text
(config)# do-exec show frame-relay qos-autosense <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 6 `；EOL ` RVA 0x346FE238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-892d68be0fd66d7c](../../evidence/conditions-sets-053.md#c-892d68be0fd66d7c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061027

```text
(config)# do-exec show frame-relay qos-autosense <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 6 `；EOL ` RVA 0x346FE238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-771f4bde333fbe75](../../evidence/conditions-sets-046.md#c-771f4bde333fbe75) · [缺口 G-4877c555659f710a](../../evidence/gaps-sets-003.md#g-4877c555659f710a) · [参数 P-82085a31f3bdf5d2](../../evidence/parameters-sets-010.md#p-82085a31f3bdf5d2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032203

```text
(config)# do-exec show frame-relay route <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 7 `；EOL ` RVA 0x346FE538 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1543bfb0ea2126ac](../../evidence/conditions-sets-008.md#c-1543bfb0ea2126ac) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032113

```text
(config)# do-exec show frame-relay traffic <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 1 `；EOL ` RVA 0x346FD110 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032176

```text
(config)# do-exec show frame-relay vofr <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 3 `；EOL ` RVA 0x346FDA48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e120d584ab7570a4](../../evidence/conditions-sets-087.md#c-e120d584ab7570a4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061024

```text
(config)# do-exec show frame-relay vofr <interface> <cr>
```

Handler ` RVA 0xF601B80 `；selector ` 3 `；EOL ` RVA 0x346FDA48 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3be11087dbeabb0d](../../evidence/conditions-sets-023.md#c-3be11087dbeabb0d) · [缺口 G-9e08199d7b868b69](../../evidence/gaps-sets-006.md#g-9e08199d7b868b69) · [参数 P-d318f6ca22964952](../../evidence/parameters-sets-016.md#p-d318f6ca22964952) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027814

```text
(config)# do-exec show fras <cr>
```

Handler ` RVA 0x1140B8D0 `；selector ` 0 `；EOL ` RVA 0x354C4D00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027682

```text
(config)# do-exec show fras-host <cr>
```

Handler ` RVA 0x11388CD0 `；selector ` 0 `；EOL ` RVA 0x3549F568 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-571a3fc10b026932](../../evidence/conditions-sets-034.md#c-571a3fc10b026932) · [状态效果 S-9644fb56c48716eb](../../evidence/state_effects-sets-032.md#s-9644fb56c48716eb)

### path-060730

```text
(config)# do-exec show fras-host <interface> <cr>
```

Handler ` RVA 0x11388CD0 `；selector ` 0 `；EOL ` RVA 0x3549F568 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5c0a392fcd71eb2d](../../evidence/conditions-sets-036.md#c-5c0a392fcd71eb2d) · [缺口 G-12e0c1051580010b](../../evidence/gaps-sets-001.md#g-12e0c1051580010b) · [参数 P-9c6d7a3c7390aae3](../../evidence/parameters-sets-012.md#p-9c6d7a3c7390aae3) · [状态效果 S-9644fb56c48716eb](../../evidence/state_effects-sets-032.md#s-9644fb56c48716eb)

### path-027668

```text
(config)# do-exec show glbp <cr>
```

Handler ` RVA 0xE166D30 `；selector ` 0 `；EOL ` RVA 0x34224068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-883650aac8a2dbcc](../../evidence/conditions-sets-053.md#c-883650aac8a2dbcc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032364

```text
(config)# do-exec show glbp capability <cr>
```

Handler ` RVA 0xE166970 `；selector ` 0 `；EOL ` RVA 0x34223BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-24460cedbb23ba30](../../evidence/conditions-sets-014.md#c-24460cedbb23ba30) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061054

```text
(config)# do-exec show glbp capability <interface> <cr>
```

Handler ` RVA 0xE166970 `；selector ` 0 `；EOL ` RVA 0x34223BD8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b17e0fbebe834cfc](../../evidence/conditions-sets-069.md#c-b17e0fbebe834cfc) · [缺口 G-f38835cfab48a756](../../evidence/gaps-sets-008.md#g-f38835cfab48a756) · [参数 P-8f5e1c323fae0d94](../../evidence/parameters-sets-011.md#p-8f5e1c323fae0d94) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032347

```text
(config)# do-exec show glbp internal <cr>
```

Handler ` RVA 0xE166CA0 `；selector ` 0 `；EOL ` RVA 0x342237D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ec257e02fae798a6](../../evidence/conditions-sets-091.md#c-ec257e02fae798a6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061056

```text
(config)# do-exec show glbp internal <interface> <cr>
```

Handler ` RVA 0xE166CA0 `；selector ` 0 `；EOL ` RVA 0x342237D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e5a7f5c05b5c224b](../../evidence/conditions-sets-089.md#c-e5a7f5c05b5c224b) · [缺口 G-2a5a778008b1d554](../../evidence/gaps-sets-002.md#g-2a5a778008b1d554) · [参数 P-ac0ba157b887c9b3](../../evidence/parameters-sets-013.md#p-ac0ba157b887c9b3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060728

```text
(config)# do-exec show glbp network <cr>
```

Handler ` RVA 0xE166D30 `；selector ` 0 `；EOL ` RVA 0x34224068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a35f6d5159def04c](../../evidence/conditions-sets-063.md#c-a35f6d5159def04c) · [缺口 G-e5a757d73b0537f1](../../evidence/gaps-sets-008.md#g-e5a757d73b0537f1) · [状态效果 S-313f565d3701e3d1](../../evidence/state_effects-sets-011.md#s-313f565d3701e3d1)

### path-026803

```text
(config)# do-exec show hardware <cr>
```

Handler ` RVA 0xE0065E0 `；selector ` 0 `；EOL ` RVA 0x34165E18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-f0aca990aed40166](../../evidence/conditions-sets-093.md#c-f0aca990aed40166) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033869

```text
(config)# do-exec show hdd-devices summary <cr>
```

Handler ` RVA 0x1581A210 `；selector ` 0 `；EOL ` RVA 0x3435DBA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-026626

```text
(config)# do-exec show history <cr>
```

Handler ` RVA 0xE2D2A30 `；selector ` 0 `；EOL ` RVA 0x340C59A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-beaab1d147b09124](../../evidence/conditions-sets-074.md#c-beaab1d147b09124) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028516

```text
(config)# do-exec show history all <cr>
```

Handler ` RVA 0xE2D2B30 `；selector ` 0 `；EOL ` RVA 0x340C5700 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060499

```text
(config)# do-exec show hosts <cr>
```

Handler ` RVA 0xD12D240 `；selector ` 0 `；EOL ` RVA 0x33D94D18 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-96b2f3bad6254f25](../../evidence/conditions-sets-058.md#c-96b2f3bad6254f25) · [缺口 G-1b07875653eb7371](../../evidence/gaps-sets-001.md#g-1b07875653eb7371) · [状态效果 S-6b0fef706bebe2aa](../../evidence/state_effects-sets-023.md#s-6b0fef706bebe2aa)

### path-032285

```text
(config)# do-exec show hosts summary <cr>
```

Handler ` RVA 0xD12D240 `；selector ` 0 `；EOL ` RVA 0x33D94D18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8517998c52793596](../../evidence/conditions-sets-051.md#c-8517998c52793596) · [状态效果 S-4dc73785f0622af5](../../evidence/state_effects-sets-017.md#s-4dc73785f0622af5)

### path-032603

```text
(config)# do-exec show hqf full-qos <cr>
```

Handler ` RVA 0x10CE5200 `；selector ` 2 `；EOL ` RVA 0x34D0D9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fde821cb9057892a](../../evidence/conditions-sets-098.md#c-fde821cb9057892a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032619

```text
(config)# do-exec show hqf interface <cr>
```

Handler ` RVA 0x10CE4BA0 `；selector ` 0 `；EOL ` RVA 0x34D0CBD0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-265038e8cc9f4727](../../evidence/conditions-sets-015.md#c-265038e8cc9f4727) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061086

```text
(config)# do-exec show hqf interface <interface> <cr>
```

Handler ` RVA 0x10CE4750 `；selector ` 0 `；EOL ` RVA 0x34D0CBA8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-d9057831e230ae76](../../evidence/conditions-sets-084.md#c-d9057831e230ae76) · [缺口 G-32f74396c131a590](../../evidence/gaps-sets-002.md#g-32f74396c131a590) · [参数 P-fa46588795320b19](../../evidence/parameters-sets-019.md#p-fa46588795320b19) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032546

```text
(config)# do-exec show hqf size <cr>
```

Handler ` RVA 0x10CE8DC0 `；selector ` 0 `；EOL ` RVA 0x34D0C818 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fde821cb9057892a](../../evidence/conditions-sets-098.md#c-fde821cb9057892a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032613

```text
(config)# do-exec show hqf sub-interface <cr>
```

Handler ` RVA 0x10CE4DD0 `；selector ` 2 `；EOL ` RVA 0x34D0D160 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fde821cb9057892a](../../evidence/conditions-sets-098.md#c-fde821cb9057892a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056008

```text
(config)# do-exec show hqf sub-interface <string> dlci <number:16..1007> <cr>
```

Handler ` RVA 0x10CE4DD0 `；selector ` 3 `；EOL ` RVA 0x34D0D208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Namestring of subinterface；` unsigned_number ` DLCI value。

[条件 C-fde821cb9057892a](../../evidence/conditions-sets-098.md#c-fde821cb9057892a) · [参数 P-b25e912a1f765fbf](../../evidence/parameters-sets-014.md#p-b25e912a1f765fbf) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-056017

```text
(config)# do-exec show hqf sub-interface <string> vcd <number:0..8191> <cr>
```

Handler ` RVA 0x10CE4DD0 `；selector ` 6 `；EOL ` RVA 0x34D0D4D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Namestring of subinterface；` unsigned_number ` ATM vcd value。

[条件 C-fde821cb9057892a](../../evidence/conditions-sets-098.md#c-fde821cb9057892a) · [参数 P-fc9a4861b06efba4](../../evidence/parameters-sets-019.md#p-fc9a4861b06efba4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050129

```text
(config)# do-exec show html module command <string> <cr>
```

Handler ` RVA 0xD223470 `；selector ` 4 `；EOL ` RVA 0x33DC6E10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The command to execute over modules。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-d9e4f37aa80a5bc6](../../evidence/parameters-sets-016.md#p-d9e4f37aa80a5bc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040982

```text
(config)# do-exec show html module count <cr>
```

Handler ` RVA 0xD223470 `；selector ` 0 `；EOL ` RVA 0x33DC6B28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040947

```text
(config)# do-exec show html module names <cr>
```

Handler ` RVA 0xD223470 `；selector ` 3 `；EOL ` RVA 0x33DC6880 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040878

```text
(config)# do-exec show html module options <cr>
```

Handler ` RVA 0xD223470 `；selector ` 2 `；EOL ` RVA 0x33DC62D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040959

```text
(config)# do-exec show html module ports <cr>
```

Handler ` RVA 0xD223470 `；selector ` 1 `；EOL ` RVA 0x33DC65E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050205

```text
(config)# do-exec show html port command <string> <cr>
```

Handler ` RVA 0xD223730 `；selector ` 4 `；EOL ` RVA 0x33DC5ED8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` The command to execute over ports。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-6ee3a3ffd6d25ffc](../../evidence/parameters-sets-009.md#p-6ee3a3ffd6d25ffc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041101

```text
(config)# do-exec show html port count <cr>
```

Handler ` RVA 0xD223730 `；selector ` 0 `；EOL ` RVA 0x33DC5BF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041027

```text
(config)# do-exec show html port names <cr>
```

Handler ` RVA 0xD223730 `；selector ` 2 `；EOL ` RVA 0x33DC56A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040984

```text
(config)# do-exec show html port options <cr>
```

Handler ` RVA 0xD223730 `；selector ` 3 `；EOL ` RVA 0x33DC53F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041068

```text
(config)# do-exec show html port shortnames <cr>
```

Handler ` RVA 0xD223730 `；selector ` 1 `；EOL ` RVA 0x33DC5948 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037457

```text
(config)# do-exec show hw-module all attribute <cr>
```

Handler ` RVA 0x159B8210 `；selector ` 0 `；EOL ` RVA 0x35DD11A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd7b2129d0ec8d1e](../../evidence/conditions-sets-098.md#c-fd7b2129d0ec8d1e) · [状态效果 S-878f867272750727](../../evidence/state_effects-sets-029.md#s-878f867272750727)

### path-037538

```text
(config)# do-exec show hw-module all entity <cr>
```

Handler ` RVA 0xEED4AF0 `；selector ` 0 `；EOL ` RVA 0x34461B60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fd7b2129d0ec8d1e](../../evidence/conditions-sets-098.md#c-fd7b2129d0ec8d1e) · [状态效果 S-878f867272750727](../../evidence/state_effects-sets-029.md#s-878f867272750727)

### path-037537

```text
(config)# do-exec show hw-module all module <cr>
```

Handler ` RVA 0x159BE350 `；selector ` 0 `；EOL ` RVA 0x35DD3020 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a795cdced38b7eda](../../evidence/conditions-sets-065.md#c-a795cdced38b7eda) · [状态效果 S-878f867272750727](../../evidence/state_effects-sets-029.md#s-878f867272750727)

### path-037686

```text
(config)# do-exec show hw-module all oir <cr>
```

Handler ` RVA 0xEEDF390 `；selector ` 0 `；EOL ` RVA 0x34465A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8df62e3fa810589](../../evidence/conditions-sets-065.md#c-a8df62e3fa810589) · [状态效果 S-f066895b71252197](../../evidence/state_effects-sets-051.md#s-f066895b71252197)

### path-037770

```text
(config)# do-exec show hw-module all sensors <cr>
```

Handler ` RVA 0xEEDAD70 `；selector ` 0 `；EOL ` RVA 0x34463300 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6807b559cef754b5](../../evidence/conditions-sets-040.md#c-6807b559cef754b5) · [状态效果 S-aa21ac1bea7f7269](../../evidence/state_effects-sets-036.md#s-aa21ac1bea7f7269)

### path-037595

```text
(config)# do-exec show hw-module all subblock <cr>
```

Handler ` RVA 0xEEE18D0 `；selector ` 0 `；EOL ` RVA 0x344667D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-037d7c89825ca5fc](../../evidence/conditions-sets-002.md#c-037d7c89825ca5fc) · [状态效果 S-878f867272750727](../../evidence/state_effects-sets-029.md#s-878f867272750727)

### path-037680

```text
(config)# do-exec show hw-module all tech-support <cr>
```

Handler ` RVA 0xEEDBE30 `；selector ` 0 `；EOL ` RVA 0x34465D38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-a8df62e3fa810589](../../evidence/conditions-sets-065.md#c-a8df62e3fa810589) · [状态效果 S-878f867272750727](../../evidence/state_effects-sets-029.md#s-878f867272750727)

### path-062007

```text
(config)# do-exec show hw-module all transceiver <number:dynamic> status <cr>
```

Handler ` RVA 0xEEE1B10 `；selector ` 0 `；EOL ` RVA 0x34466C88 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` transceiver port number。

[条件 C-0fb90ed5e2319a60](../../evidence/conditions-sets-006.md#c-0fb90ed5e2319a60) · [缺口 G-0b1ac8f46e7627af](../../evidence/gaps-sets-001.md#g-0b1ac8f46e7627af) · [参数 P-5cc20972785a59b2](../../evidence/parameters-sets-007.md#p-5cc20972785a59b2) · [状态效果 S-2cd080effc3efaa7](../../evidence/state_effects-sets-010.md#s-2cd080effc3efaa7)

### path-062006

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all attribute <cr>
```

Handler ` RVA 0x159B8210 `；selector ` 0 `；EOL ` RVA 0x35DD11A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-defd4d2decd336a7](../../evidence/conditions-sets-086.md#c-defd4d2decd336a7) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-9f6f552c6405a7b2](../../evidence/state_effects-sets-034.md#s-9f6f552c6405a7b2)

### path-062012

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all entity <cr>
```

Handler ` RVA 0xEED4AF0 `；selector ` 0 `；EOL ` RVA 0x34461B60 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-defd4d2decd336a7](../../evidence/conditions-sets-086.md#c-defd4d2decd336a7) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-9f6f552c6405a7b2](../../evidence/state_effects-sets-034.md#s-9f6f552c6405a7b2)

### path-062011

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all module <cr>
```

Handler ` RVA 0x159BE350 `；selector ` 0 `；EOL ` RVA 0x35DD3020 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3059437766595442](../../evidence/conditions-sets-019.md#c-3059437766595442) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-9f6f552c6405a7b2](../../evidence/state_effects-sets-034.md#s-9f6f552c6405a7b2)

### path-062022

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all oir <cr>
```

Handler ` RVA 0xEEDF390 `；selector ` 0 `；EOL ` RVA 0x34465A98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a59e34405a36b641](../../evidence/conditions-sets-064.md#c-a59e34405a36b641) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-fbabfd6f95756fa7](../../evidence/state_effects-sets-053.md#s-fbabfd6f95756fa7)

### path-062030

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all sensors <cr>
```

Handler ` RVA 0xEEDAD70 `；selector ` 0 `；EOL ` RVA 0x34463300 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-127d810136650faa](../../evidence/conditions-sets-007.md#c-127d810136650faa) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-5b07f73c51ea42ef](../../evidence/state_effects-sets-020.md#s-5b07f73c51ea42ef)

### path-062015

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all subblock <cr>
```

Handler ` RVA 0xEEE18D0 `；selector ` 0 `；EOL ` RVA 0x344667D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-bfdf48b56ced963a](../../evidence/conditions-sets-074.md#c-bfdf48b56ced963a) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-9f6f552c6405a7b2](../../evidence/state_effects-sets-034.md#s-9f6f552c6405a7b2)

### path-062021

```text
(config)# do-exec show hw-module subslot <?slotcard_func_action@5555899c0dc8> all tech-support <cr>
```

Handler ` RVA 0xEEDBE30 `；selector ` 0 `；EOL ` RVA 0x34465D38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a59e34405a36b641](../../evidence/conditions-sets-064.md#c-a59e34405a36b641) · [缺口 G-349b908215b16b46](../../evidence/gaps-sets-002.md#g-349b908215b16b46) · [状态效果 S-9f6f552c6405a7b2](../../evidence/state_effects-sets-034.md#s-9f6f552c6405a7b2)

### path-032073

```text
(config)# do-exec show icm stats <cr>
```

Handler ` RVA 0xC2FAF60 `；selector ` 0 `；EOL ` RVA 0x33A40208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c96b4c6b9be8bcad](../../evidence/state_effects-sets-043.md#s-c96b4c6b9be8bcad)

### path-033511

```text
(config)# do-exec show id-manager traceback <cr>
```

Handler ` RVA 0xE115ED0 `；selector ` 0 `；EOL ` RVA 0x342097B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b9a9a65675880bc9](../../evidence/state_effects-sets-039.md#s-b9a9a65675880bc9)

### path-027757

```text
(config)# do-exec show idb <cr>
```

Handler ` RVA 0xE3EEB50 `；selector ` 0 `；EOL ` RVA 0x341CF3B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-76cb17bf52c7d006](../../evidence/conditions-sets-046.md#c-76cb17bf52c7d006) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060745

```text
(config)# do-exec show idb <interface> <cr>
```

Handler ` RVA 0xE3EEB50 `；selector ` 0 `；EOL ` RVA 0x341CF3B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7718a5e6b83d9906](../../evidence/conditions-sets-046.md#c-7718a5e6b83d9906) · [缺口 G-675a2c85f8f6bd59](../../evidence/gaps-sets-004.md#g-675a2c85f8f6bd59) · [参数 P-9d24ce7442dc7462](../../evidence/parameters-sets-012.md#p-9d24ce7442dc7462) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061174

```text
(config)# do-exec show idb <interface> bits <cr>
```

Handler ` RVA 0xE3EFF80 `；selector ` 0 `；EOL ` RVA 0x341D1330 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-110bbd77919f7f5c](../../evidence/conditions-sets-007.md#c-110bbd77919f7f5c) · [缺口 G-675a2c85f8f6bd59](../../evidence/gaps-sets-004.md#g-675a2c85f8f6bd59) · [参数 P-9d24ce7442dc7462](../../evidence/parameters-sets-012.md#p-9d24ce7442dc7462) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033586

```text
(config)# do-exec show idb bits <cr>
```

Handler ` RVA 0xE3EFF80 `；selector ` 0 `；EOL ` RVA 0x341D1330 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-831183d34fa7861f](../../evidence/conditions-sets-051.md#c-831183d34fa7861f) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033524

```text
(config)# do-exec show idb ifnum <cr>
```

Handler ` RVA 0xED1CEC0 `；selector ` 0 `；EOL ` RVA 0x34406B00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7dfcabb49abcce2c](../../evidence/conditions-sets-049.md#c-7dfcabb49abcce2c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033527

```text
(config)# do-exec show idb pointers <cr>
```

Handler ` RVA 0xE3EFC20 `；selector ` 0 `；EOL ` RVA 0x341D0F30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7ea4291ce0170e4b](../../evidence/conditions-sets-049.md#c-7ea4291ce0170e4b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033257

```text
(config)# do-exec show identity policy <cr>
```

Handler ` RVA 0xCB518F0 `；selector ` 0 `；EOL ` RVA 0x33BE2038 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c61179f13e1fd720](../../evidence/state_effects-sets-042.md#s-c61179f13e1fd720)

### path-033259

```text
(config)# do-exec show identity profile <cr>
```

Handler ` RVA 0xCB50300 `；selector ` 0 `；EOL ` RVA 0x33BE1C68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2c43afc728a15176](../../evidence/state_effects-sets-010.md#s-2c43afc728a15176)

### path-033013

```text
(config)# do-exec show idmgr memory <cr>
```

Handler ` RVA 0xE186C50 `；selector ` 0 `；EOL ` RVA 0x3422A9B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-d53248505657c8f6](../../evidence/state_effects-sets-045.md#s-d53248505657c8f6)

### path-062205

```text
(config)# do-exec show idmgr session key session-handle <hex-data> <cr>
```

Handler ` RVA 0xE186C50 `；selector ` 0 `；EOL ` RVA 0x34229E40 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexdata ` string of hex characters。

[条件 C-ca4cbac2b3eca919](../../evidence/conditions-sets-078.md#c-ca4cbac2b3eca919) · [缺口 G-da167bc7726fe6ae](../../evidence/gaps-sets-008.md#g-da167bc7726fe6ae) · [参数 P-2e6c61ea35613a54](../../evidence/parameters-sets-004.md#p-2e6c61ea35613a54) · [状态效果 S-6ff3bc34c97ae7b4](../../evidence/state_effects-sets-024.md#s-6ff3bc34c97ae7b4)

### path-032955

```text
(config)# do-exec show idmgr statistics <cr>
```

Handler ` RVA 0xE186C50 `；selector ` 0 `；EOL ` RVA 0x34229E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-2d545908799b4ca2](../../evidence/state_effects-sets-010.md#s-2d545908799b4ca2)

### path-027356

```text
(config)# do-exec show if-mgr <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 0 `；EOL ` RVA 0x33A35908 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037014

```text
(config)# do-exec show if-mgr db ifStack <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 6 `；EOL ` RVA 0x33A350E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046371

```text
(config)# do-exec show if-mgr db interface brief <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 2 `；EOL ` RVA 0x33A34348 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053867

```text
(config)# do-exec show if-mgr db interface ifIndex <number:0..4294967295> <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 1 `；EOL ` RVA 0x33A346C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interface's ifIndex。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-ed37c063ae2f72f0](../../evidence/parameters-sets-018.md#p-ed37c063ae2f72f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-057652

```text
(config)# do-exec show if-mgr db interface ifIndex <number:0..4294967295> ifStack <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 5 `；EOL ` RVA 0x33A346A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` interface's ifIndex。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-ed37c063ae2f72f0](../../evidence/parameters-sets-018.md#p-ed37c063ae2f72f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-046557

```text
(config)# do-exec show if-mgr db interface ifName <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 4 `；EOL ` RVA 0x33A34C00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-053841

```text
(config)# do-exec show if-mgr db interface ifName <string> <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 3 `；EOL ` RVA 0x33A34BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` interface's ifName。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-5e93dbc60763e120](../../evidence/parameters-sets-008.md#p-5e93dbc60763e120) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-030465

```text
(config)# do-exec show if-mgr hash <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 7 `；EOL ` RVA 0x33A35438 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-037008

```text
(config)# do-exec show if-mgr hash brief <cr>
```

Handler ` RVA 0xC2C7E10 `；selector ` 8 `；EOL ` RVA 0x33A35410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028378

```text
(config)# do-exec show ifnum list <cr>
```

Handler ` RVA 0xED27C20 `；selector ` 0 `；EOL ` RVA 0x34406588 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028416

```text
(config)# do-exec show ifnum statistics <cr>
```

Handler ` RVA 0xED27C20 `；selector ` 1 `；EOL ` RVA 0x34406830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060390

```text
(config)# do-exec show interfaces <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 0 `；EOL ` RVA 0x34125150 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-b51dd26dc8ae56d3](../../evidence/conditions-sets-070.md#c-b51dd26dc8ae56d3) · [缺口 G-38b0b5be34db5940](../../evidence/gaps-sets-002.md#g-38b0b5be34db5940) · [状态效果 S-efda9e0a0ebd752c](../../evidence/state_effects-sets-051.md#s-efda9e0a0ebd752c)

### path-061869

```text
(config)# do-exec show interfaces <interface> counters protocol status <cr>
```

Handler ` RVA 0xE4456B0 `；selector ` 0 `；EOL ` RVA 0x342C20E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60e3fc54b263113b](../../evidence/conditions-sets-038.md#c-60e3fc54b263113b) · [缺口 G-fafd5741871f1eb9](../../evidence/gaps-sets-009.md#g-fafd5741871f1eb9) · [参数 P-abfa956765e3a60b](../../evidence/parameters-sets-013.md#p-abfa956765e3a60b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060787

```text
(config)# do-exec show interfaces <interface> flowcontrol <cr>
```

Handler ` RVA 0x15DB0A30 `；selector ` 0 `；EOL ` RVA 0x35E1F540 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4ca62fc392778bb2](../../evidence/conditions-sets-030.md#c-4ca62fc392778bb2) · [缺口 G-fafd5741871f1eb9](../../evidence/gaps-sets-009.md#g-fafd5741871f1eb9) · [参数 P-abfa956765e3a60b](../../evidence/parameters-sets-013.md#p-abfa956765e3a60b) · [状态效果 S-265d9f64fb44ea2b](../../evidence/state_effects-sets-009.md#s-265d9f64fb44ea2b)

### path-060810

```text
(config)# do-exec show interfaces <interface> history <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 21 `；EOL ` RVA 0x34125AE0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-60e3fc54b263113b](../../evidence/conditions-sets-038.md#c-60e3fc54b263113b) · [缺口 G-fafd5741871f1eb9](../../evidence/gaps-sets-009.md#g-fafd5741871f1eb9) · [参数 P-abfa956765e3a60b](../../evidence/parameters-sets-013.md#p-abfa956765e3a60b) · [状态效果 S-bc4b81a08717b0ef](../../evidence/state_effects-sets-040.md#s-bc4b81a08717b0ef)

### path-060769

```text
(config)# do-exec show interfaces <interface> switchport <cr>
```

Handler ` RVA 0x15C36D40 `；selector ` 1 `；EOL ` RVA 0x35DF3070 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-1dc077650c03ca7a](../../evidence/conditions-sets-012.md#c-1dc077650c03ca7a) · [缺口 G-fafd5741871f1eb9](../../evidence/gaps-sets-009.md#g-fafd5741871f1eb9) · [参数 P-abfa956765e3a60b](../../evidence/parameters-sets-013.md#p-abfa956765e3a60b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-044595

```text
(config)# do-exec show interfaces counters protocol status <cr>
```

Handler ` RVA 0xE4456B0 `；selector ` 0 `；EOL ` RVA 0x342C20E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9cf70dc8c91efd7a](../../evidence/conditions-sets-061.md#c-9cf70dc8c91efd7a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-028297

```text
(config)# do-exec show interfaces dampening <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 0 `；EOL ` RVA 0x34125150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3316cec7d3c3e310](../../evidence/conditions-sets-020.md#c-3316cec7d3c3e310) · [状态效果 S-ddf306635e108fba](../../evidence/state_effects-sets-047.md#s-ddf306635e108fba)

### path-028640

```text
(config)# do-exec show interfaces flowcontrol <cr>
```

Handler ` RVA 0x15DB0A30 `；selector ` 0 `；EOL ` RVA 0x35E1F540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-552b668f43f08c69](../../evidence/conditions-sets-033.md#c-552b668f43f08c69) · [状态效果 S-265d9f64fb44ea2b](../../evidence/state_effects-sets-009.md#s-265d9f64fb44ea2b)

### path-028960

```text
(config)# do-exec show interfaces history <cr>
```

Handler ` RVA 0xE43B080 `；selector ` 21 `；EOL ` RVA 0x34125AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-9cf70dc8c91efd7a](../../evidence/conditions-sets-061.md#c-9cf70dc8c91efd7a) · [状态效果 S-bc4b81a08717b0ef](../../evidence/state_effects-sets-040.md#s-bc4b81a08717b0ef)

### path-027754

```text
(config)# do-exec show inventory <cr>
```

Handler ` RVA 0xE01BD20 `；selector ` 0 `；EOL ` RVA 0x3416E5D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3bd120b3ae4e6370](../../evidence/conditions-sets-023.md#c-3bd120b3ae4e6370) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033145

```text
(config)# do-exec show iosp-server status <cr>
```

Handler ` RVA 0xE8C47B0 `；selector ` 0 `；EOL ` RVA 0x3433C288 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-027811

```text
(config)# do-exec show iox-service <cr>
```

Handler ` RVA 0xE9E9380 `；selector ` 1 `；EOL ` RVA 0x34384010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-033895

```text
(config)# do-exec show iox-service detail <cr>
```

Handler ` RVA 0xE9E9380 `；selector ` 3 `；EOL ` RVA 0x34383FE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031435

```text
(config)# do-exec show ip access-lists <cr>
```

Handler ` RVA 0xCEED5F0 `；selector ` 0 `；EOL ` RVA 0x33D54CE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e8b459f558708fef](../../evidence/conditions-sets-090.md#c-e8b459f558708fef) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047840

```text
(config)# do-exec show ip access-lists <number:1..199> dump-og-database <cr>
```

Handler ` RVA 0xCEED520 `；selector ` 0 `；EOL ` RVA 0x33D558A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-2ea6b31dd9df267c](../../evidence/conditions-sets-018.md#c-2ea6b31dd9df267c) · [参数 P-8145ab0f3d0aa67b](../../evidence/parameters-sets-010.md#p-8145ab0f3d0aa67b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047923

```text
(config)# do-exec show ip access-lists <number:1..199> dump-reflexive <cr>
```

Handler ` RVA 0xCEED210 `；selector ` 0 `；EOL ` RVA 0x33D55B88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-8c40a1a6dbb1e46a](../../evidence/conditions-sets-054.md#c-8c40a1a6dbb1e46a) · [参数 P-8145ab0f3d0aa67b](../../evidence/parameters-sets-010.md#p-8145ab0f3d0aa67b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-047764

```text
(config)# do-exec show ip access-lists <number:1..199> expanded <cr>
```

Handler ` RVA 0xCEED760 `；selector ` 0 `；EOL ` RVA 0x33D55578 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Access list number。

[条件 C-a5ef4cd44829758d](../../evidence/conditions-sets-064.md#c-a5ef4cd44829758d) · [参数 P-8145ab0f3d0aa67b](../../evidence/parameters-sets-010.md#p-8145ab0f3d0aa67b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061500

```text
(config)# do-exec show ip access-lists interface <interface> <cr>
```

Handler ` RVA 0xCEED960 `；selector ` 0 `；EOL ` RVA 0x33D55168 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f4cdb718ba11296f](../../evidence/conditions-sets-094.md#c-f4cdb718ba11296f) · [缺口 G-fa7f9ae50c0a9ba8](../../evidence/gaps-sets-009.md#g-fa7f9ae50c0a9ba8) · [参数 P-66b42d6f3c85068c](../../evidence/parameters-sets-008.md#p-66b42d6f3c85068c) · [状态效果 S-bd307f3975c3189d](../../evidence/state_effects-sets-040.md#s-bd307f3975c3189d)

### path-032177

```text
(config)# do-exec show ip accounting <cr>
```

Handler ` RVA 0xD17A1A0 `；selector ` 0 `；EOL ` RVA 0x33DA7150 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bb5231a2120f2ff4](../../evidence/conditions-sets-072.md#c-bb5231a2120f2ff4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031848

```text
(config)# do-exec show ip aliases <cr>
```

Handler ` RVA 0xD17BFF0 `；selector ` 0 `；EOL ` RVA 0x33DA83B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039565

```text
(config)# do-exec show ip amt tunnel <cr>
```

Handler ` RVA 0xBB7D800 `；selector ` 0 `；EOL ` RVA 0x3386C998 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c39448146a1b3b1](../../evidence/conditions-sets-042.md#c-6c39448146a1b3b1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038263

```text
(config)# do-exec show ip arp <address> <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 3 `；EOL ` RVA 0x33D1F210 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` 48-bit hardware address of ARP entry。

[条件 C-5792fd917ec6ec78](../../evidence/conditions-sets-034.md#c-5792fd917ec6ec78) · [参数 P-271dd2dbc889757e](../../evidence/parameters-sets-003.md#p-271dd2dbc889757e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038366

```text
(config)# do-exec show ip arp <address> <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 2 `；EOL ` RVA 0x33D1F778 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address or hostname of ARP entry。

[条件 C-81e873f91ef65f15](../../evidence/conditions-sets-050.md#c-81e873f91ef65f15) · [参数 P-eac77c0fd9a82cc9](../../evidence/parameters-sets-018.md#p-eac77c0fd9a82cc9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031214

```text
(config)# do-exec show ip arp <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 0 `；EOL ` RVA 0x33D1F4B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-5792fd917ec6ec78](../../evidence/conditions-sets-034.md#c-5792fd917ec6ec78) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060959

```text
(config)# do-exec show ip arp <interface> <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 1 `；EOL ` RVA 0x33D1EF68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-aa883a0bf9d3778b](../../evidence/conditions-sets-066.md#c-aa883a0bf9d3778b) · [缺口 G-f761f1beb1dd7250](../../evidence/gaps-sets-009.md#g-f761f1beb1dd7250) · [参数 P-4e1b23c080c06fe5](../../evidence/parameters-sets-006.md#p-4e1b23c080c06fe5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038175

```text
(config)# do-exec show ip arp garpretry <cr>
```

Handler ` RVA 0xCF704B0 `；selector ` 0 `；EOL ` RVA 0x33D1FA60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-be8c62c1c0d063c5](../../evidence/conditions-sets-074.md#c-be8c62c1c0d063c5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038135

```text
(config)# do-exec show ip arp incomplete <cr>
```

Handler ` RVA 0xCF6DDD0 `；selector ` 0 `；EOL ` RVA 0x33D1FD18 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-afdf6ab04c41b9f3](../../evidence/conditions-sets-068.md#c-afdf6ab04c41b9f3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038041

```text
(config)# do-exec show ip arp poll <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 5 `；EOL ` RVA 0x33D1E860 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038029

```text
(config)# do-exec show ip arp summary <cr>
```

Handler ` RVA 0xCF5FD60 `；selector ` 4 `；EOL ` RVA 0x33D1EB00 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031671

```text
(config)# do-exec show ip as-path-access-list <cr>
```

Handler ` RVA 0xF24D440 `；selector ` 0 `；EOL ` RVA 0x344BB918 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031506

```text
(config)# do-exec show ip cache <cr>
```

Handler ` RVA 0xD49E9E0 `；selector ` 0 `；EOL ` RVA 0x33E55378 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ecd3a44f65f9f843](../../evidence/conditions-sets-091.md#c-ecd3a44f65f9f843) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060982

```text
(config)# do-exec show ip cache <interface> <cr>
```

Handler ` RVA 0xD49E9E0 `；selector ` 0 `；EOL ` RVA 0x33E55378 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ec2978d6133630e4](../../evidence/conditions-sets-091.md#c-ec2978d6133630e4) · [缺口 G-6b31f0b012fe1896](../../evidence/gaps-sets-004.md#g-6b31f0b012fe1896) · [参数 P-0061b1ed422a21f0](../../evidence/parameters-sets-001.md#p-0061b1ed422a21f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061504

```text
(config)# do-exec show ip cache <interface> flow <cr>
```

Handler ` RVA 0x10BB3E20 `；selector ` 0 `；EOL ` RVA 0x34CCC258 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-41dafcfc19066e8a](../../evidence/conditions-sets-026.md#c-41dafcfc19066e8a) · [缺口 G-6b31f0b012fe1896](../../evidence/gaps-sets-004.md#g-6b31f0b012fe1896) · [参数 P-0061b1ed422a21f0](../../evidence/parameters-sets-001.md#p-0061b1ed422a21f0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039137

```text
(config)# do-exec show ip cache flow <cr>
```

Handler ` RVA 0x10BB3E20 `；selector ` 0 `；EOL ` RVA 0x34CCC258 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-1d31465d89ad7a04](../../evidence/conditions-sets-011.md#c-1d31465d89ad7a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038820

```text
(config)# do-exec show ip cache policy <cr>
```

Handler ` RVA 0xD49E9E0 `；selector ` 0 `；EOL ` RVA 0x34804F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-394712fa75e3f0cd](../../evidence/state_effects-sets-013.md#s-394712fa75e3f0cd)

### path-040322

```text
(config)# do-exec show ip casa oper <cr>
```

Handler ` RVA 0x11266710 `；selector ` 0 `；EOL ` RVA 0x354406C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-bee5a7abe969eca4](../../evidence/state_effects-sets-040.md#s-bee5a7abe969eca4)

### path-040545

```text
(config)# do-exec show ip casa wildcard <cr>
```

Handler ` RVA 0x1132CDC0 `；selector ` 0 `；EOL ` RVA 0x35498E80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-c3cced9b6c4de07c](../../evidence/state_effects-sets-041.md#s-c3cced9b6c4de07c)

### path-032624

```text
(config)# do-exec show ip cef <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 0 `；EOL ` RVA 0x337B5CB8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-288378b871be8ccf](../../evidence/conditions-sets-016.md#c-288378b871be8ccf) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-061085

```text
(config)# do-exec show ip cef <interface> <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 0 `；EOL ` RVA 0x337B5CB8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f855e72d1d4a95ff](../../evidence/conditions-sets-096.md#c-f855e72d1d4a95ff) · [缺口 G-a4eb6b2c27b9e40c](../../evidence/gaps-sets-006.md#g-a4eb6b2c27b9e40c) · [参数 P-5bf33fa929e3f371](../../evidence/parameters-sets-007.md#p-5bf33fa929e3f371) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-041168

```text
(config)# do-exec show ip cef events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337B67B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f116a8929305056](../../evidence/conditions-sets-031.md#c-4f116a8929305056) · [状态效果 S-ef4837270df52d31](../../evidence/state_effects-sets-051.md#s-ef4837270df52d31)

### path-041000

```text
(config)# do-exec show ip cef inconsistency <cr>
```

Handler ` RVA 0xB5FCCD0 `；selector ` 0 `；EOL ` RVA 0x337B6D28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f116a8929305056](../../evidence/conditions-sets-031.md#c-4f116a8929305056) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-041045

```text
(config)# do-exec show ip cef label-table <cr>
```

Handler ` RVA 0xB5FBF00 `；selector ` 0 `；EOL ` RVA 0x337B6370 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f116a8929305056](../../evidence/conditions-sets-031.md#c-4f116a8929305056) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-040678

```text
(config)# do-exec show ip cef protocol-discard <cr>
```

Handler ` RVA 0xB5C2EB0 `；selector ` 74 `；EOL ` RVA 0x337C4AF0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040738

```text
(config)# do-exec show ip cef summary <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 1 `；EOL ` RVA 0x337B5518 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c48b06dbecdebb9](../../evidence/conditions-sets-042.md#c-6c48b06dbecdebb9) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-050027

```text
(config)# do-exec show ip cef switching statistics <cr>
```

Handler ` RVA 0xB5F8C90 `；selector ` 0 `；EOL ` RVA 0x337B6018 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f116a8929305056](../../evidence/conditions-sets-031.md#c-4f116a8929305056) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-050094

```text
(config)# do-exec show ip cef traffic prefix-length <cr>
```

Handler ` RVA 0xB5FCBD0 `；selector ` 0 `；EOL ` RVA 0x337B7068 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4f116a8929305056](../../evidence/conditions-sets-031.md#c-4f116a8929305056) · [状态效果 S-0afd165f21936db8](../../evidence/state_effects-sets-003.md#s-0afd165f21936db8)

### path-040872

```text
(config)# do-exec show ip cef tree <cr>
```

Handler ` RVA 0xB5FC9E0 `；selector ` 0 `；EOL ` RVA 0x337B5828 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-6c48b06dbecdebb9](../../evidence/conditions-sets-042.md#c-6c48b06dbecdebb9) · [状态效果 S-2186d28fa8259dd5](../../evidence/state_effects-sets-008.md#s-2186d28fa8259dd5)

### path-062158

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> events <cr>
```

Handler ` RVA 0xD2CF860 `；selector ` 0 `；EOL ` RVA 0x337B67B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e4aff2cf03d8e2b](../../evidence/conditions-sets-043.md#c-6e4aff2cf03d8e2b) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-4a66e2c9efd7985e](../../evidence/state_effects-sets-016.md#s-4a66e2c9efd7985e)

### path-062150

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> inconsistency <cr>
```

Handler ` RVA 0xB5FCCD0 `；selector ` 0 `；EOL ` RVA 0x337B6D28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e4aff2cf03d8e2b](../../evidence/conditions-sets-043.md#c-6e4aff2cf03d8e2b) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-5348da40e7323670](../../evidence/state_effects-sets-018.md#s-5348da40e7323670)

### path-062153

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> label-table <cr>
```

Handler ` RVA 0xB5FBF00 `；selector ` 0 `；EOL ` RVA 0x337B6370 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e4aff2cf03d8e2b](../../evidence/conditions-sets-043.md#c-6e4aff2cf03d8e2b) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-5348da40e7323670](../../evidence/state_effects-sets-018.md#s-5348da40e7323670)

### path-062140

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> summary <cr>
```

Handler ` RVA 0xB5FBFC0 `；selector ` 1 `；EOL ` RVA 0x337B5518 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f8351302a5894d7](../../evidence/conditions-sets-025.md#c-3f8351302a5894d7) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-5348da40e7323670](../../evidence/state_effects-sets-018.md#s-5348da40e7323670)

### path-062431

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> switching statistics <cr>
```

Handler ` RVA 0xB5F8C90 `；selector ` 0 `；EOL ` RVA 0x337B6018 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e4aff2cf03d8e2b](../../evidence/conditions-sets-043.md#c-6e4aff2cf03d8e2b) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-5348da40e7323670](../../evidence/state_effects-sets-018.md#s-5348da40e7323670)

### path-062440

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> traffic prefix-length <cr>
```

Handler ` RVA 0xB5FCBD0 `；selector ` 0 `；EOL ` RVA 0x337B7068 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-6e4aff2cf03d8e2b](../../evidence/conditions-sets-043.md#c-6e4aff2cf03d8e2b) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-bc981c2a8409356b](../../evidence/state_effects-sets-040.md#s-bc981c2a8409356b)

### path-062144

```text
(config)# do-exec show ip cef vrf <?option@555588d09300> tree <cr>
```

Handler ` RVA 0xB5FC9E0 `；selector ` 0 `；EOL ` RVA 0x337B5828 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-3f8351302a5894d7](../../evidence/conditions-sets-025.md#c-3f8351302a5894d7) · [缺口 G-9cd8812443ef89da](../../evidence/gaps-sets-006.md#g-9cd8812443ef89da) · [状态效果 S-5348da40e7323670](../../evidence/state_effects-sets-018.md#s-5348da40e7323670)

### path-031692

```text
(config)# do-exec show ip community-list <cr>
```

Handler ` RVA 0xF248DA0 `；selector ` 0 `；EOL ` RVA 0x344BB590 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-260e7b7ef6825b50](../../evidence/conditions-sets-015.md#c-260e7b7ef6825b50) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040629

```text
(config)# do-exec show ip ddns update <cr>
```

Handler ` RVA 0xF4811F0 `；selector ` 0 `；EOL ` RVA 0x3465B360 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-03ee89c6d4ea2f47](../../evidence/conditions-sets-002.md#c-03ee89c6d4ea2f47) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061620

```text
(config)# do-exec show ip ddns update <interface> <cr>
```

Handler ` RVA 0xF4811F0 `；selector ` 0 `；EOL ` RVA 0x3465B360 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-84902ff74f972809](../../evidence/conditions-sets-051.md#c-84902ff74f972809) · [缺口 G-cd0a7da60ce72d65](../../evidence/gaps-sets-007.md#g-cd0a7da60ce72d65) · [参数 P-dd8c8ede646185fc](../../evidence/parameters-sets-017.md#p-dd8c8ede646185fc) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049719

```text
(config)# do-exec show ip ddns update method <cr>
```

Handler ` RVA 0xF480EE0 `；selector ` 0 `；EOL ` RVA 0x3465B008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031153

```text
(config)# do-exec show ip default-gateway <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 1 `；EOL ` RVA 0x33D32B80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032046

```text
(config)# do-exec show ip dfp <cr>
```

Handler ` RVA 0x11285090 `；selector ` 0 `；EOL ` RVA 0x354459E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050141

```text
(config)# do-exec show ip dhcp binding <address> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 1 `；EOL ` RVA 0x33DE0540 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` IP address in dotted-decimal notation。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-b433863fc480c7af](../../evidence/parameters-sets-014.md#p-b433863fc480c7af) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041047

```text
(config)# do-exec show ip dhcp binding <cr>
```

Handler ` RVA 0xD298440 `；selector ` 0 `；EOL ` RVA 0x33DE0128 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040962

```text
(config)# do-exec show ip dhcp conflict <cr>
```

Handler ` RVA 0xD298440 `；selector ` 2 `；EOL ` RVA 0x33DE0F80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040782

```text
(config)# do-exec show ip dhcp database <cr>
```

Handler ` RVA 0xD251DB0 `；selector ` 3 `；EOL ` RVA 0x33DD6410 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049903

```text
(config)# do-exec show ip dhcp database <string> <cr>
```

Handler ` RVA 0xD251DB0 `；selector ` 4 `；EOL ` RVA 0x33DD63E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Uniform Resource Locator (URL)。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-faf497cd99c246ca](../../evidence/parameters-sets-019.md#p-faf497cd99c246ca) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049878

```text
(config)# do-exec show ip dhcp excluded-addresses all <cr>
```

Handler ` RVA 0xD29AF20 `；selector ` 15 `；EOL ` RVA 0x33DD5B30 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055752

```text
(config)# do-exec show ip dhcp excluded-addresses pool <string> <cr>
```

Handler ` RVA 0xD29AF20 `；selector ` 14 `；EOL ` RVA 0x33DD6100 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Pool name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-39a02f901b7b7a04](../../evidence/parameters-sets-005.md#p-39a02f901b7b7a04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055742

```text
(config)# do-exec show ip dhcp excluded-addresses vrf <string> <cr>
```

Handler ` RVA 0xD29AF20 `；selector ` 16 `；EOL ` RVA 0x33DD5E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-3fc957922bee21ab](../../evidence/parameters-sets-005.md#p-3fc957922bee21ab) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062442

```text
(config)# do-exec show ip dhcp hash find-index <number:0..65535> <hex-string> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 20 `；EOL ` RVA 0x33DE30E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number ` htype value；` hexstring ` haddr value (Hexstring)。

[条件 C-14c1245604f651f0](../../evidence/conditions-sets-008.md#c-14c1245604f651f0) · [缺口 G-80c79e6647736ce2](../../evidence/gaps-sets-005.md#g-80c79e6647736ce2) · [参数 P-084e89d8230e234e](../../evidence/parameters-sets-001.md#p-084e89d8230e234e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062579

```text
(config)# do-exec show ip dhcp hash global client-id <hex-string> dump <cr>
```

Handler ` RVA 0xD298440 `；selector ` 19 `；EOL ` RVA 0x33DE2D10 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Client Id value (hexstring)。

[条件 C-99f05afb51521c04](../../evidence/conditions-sets-059.md#c-99f05afb51521c04) · [缺口 G-14cbe2a5b7b6353d](../../evidence/gaps-sets-001.md#g-14cbe2a5b7b6353d) · [参数 P-6e618f32c5f3e8e0](../../evidence/parameters-sets-009.md#p-6e618f32c5f3e8e0) · [状态效果 S-94120dbdc440fc2e](../../evidence/state_effects-sets-031.md#s-94120dbdc440fc2e)

### path-062578

```text
(config)# do-exec show ip dhcp hash global client-id <hex-string> statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 18 `；EOL ` RVA 0x33DE2A28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` hexstring ` Client Id value (hexstring)。

[条件 C-99f05afb51521c04](../../evidence/conditions-sets-059.md#c-99f05afb51521c04) · [缺口 G-14cbe2a5b7b6353d](../../evidence/gaps-sets-001.md#g-14cbe2a5b7b6353d) · [参数 P-6e618f32c5f3e8e0](../../evidence/parameters-sets-009.md#p-6e618f32c5f3e8e0) · [状态效果 S-94120dbdc440fc2e](../../evidence/state_effects-sets-031.md#s-94120dbdc440fc2e)

### path-055983

```text
(config)# do-exec show ip dhcp hash global dump <cr>
```

Handler ` RVA 0xD298440 `；selector ` 19 `；EOL ` RVA 0x33DE2D10 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba8867d415c7bfcd](../../evidence/conditions-sets-072.md#c-ba8867d415c7bfcd) · [状态效果 S-b84ef6b88b1484a2](../../evidence/state_effects-sets-039.md#s-b84ef6b88b1484a2)

### path-055974

```text
(config)# do-exec show ip dhcp hash global statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 18 `；EOL ` RVA 0x33DE2A28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ba8867d415c7bfcd](../../evidence/conditions-sets-072.md#c-ba8867d415c7bfcd) · [状态效果 S-b84ef6b88b1484a2](../../evidence/state_effects-sets-039.md#s-b84ef6b88b1484a2)

### path-040991

```text
(config)# do-exec show ip dhcp import <cr>
```

Handler ` RVA 0xD298440 `；selector ` 6 `；EOL ` RVA 0x33DE1520 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050237

```text
(config)# do-exec show ip dhcp limit lease <cr>
```

Handler ` RVA 0xD298440 `；selector ` 10 `；EOL ` RVA 0x33DE24E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-259b545834b91947](../../evidence/conditions-sets-015.md#c-259b545834b91947) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062156

```text
(config)# do-exec show ip dhcp limit lease <interface> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 10 `；EOL ` RVA 0x33DE24E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-ad96ca82737d1201](../../evidence/conditions-sets-067.md#c-ad96ca82737d1201) · [缺口 G-0977f4ecd41c659f](../../evidence/gaps-sets-001.md#g-0977f4ecd41c659f) · [参数 P-7938f911247cd3c1](../../evidence/parameters-sets-009.md#p-7938f911247cd3c1) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050062

```text
(config)# do-exec show ip dhcp packet statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 17 `；EOL ` RVA 0x33DE1290 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041108

```text
(config)# do-exec show ip dhcp pool <cr>
```

Handler ` RVA 0xD298440 `；selector ` 7 `；EOL ` RVA 0x33DE2140 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055725

```text
(config)# do-exec show ip dhcp relay information trusted-sources <cr>
```

Handler ` RVA 0xD24E100 `；selector ` 0 `；EOL ` RVA 0x33DD5830 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050158

```text
(config)# do-exec show ip dhcp server odap-statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 12 `；EOL ` RVA 0x33DE1E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050197

```text
(config)# do-exec show ip dhcp server statistics <cr>
```

Handler ` RVA 0xD298440 `；selector ` 5 `；EOL ` RVA 0x33DE1940 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ee83d1a26447fa84](../../evidence/conditions-sets-092.md#c-ee83d1a26447fa84) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062154

```text
(config)# do-exec show ip dhcp server statistics <interface> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 11 `；EOL ` RVA 0x33DE1918 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-03aa367f06303525](../../evidence/conditions-sets-002.md#c-03aa367f06303525) · [缺口 G-5de8a475d9cee600](../../evidence/gaps-sets-004.md#g-5de8a475d9cee600) · [参数 P-b533da34b300ad73](../../evidence/parameters-sets-014.md#p-b533da34b300ad73) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050116

```text
(config)# do-exec show ip dhcp sip session <cr>
```

Handler ` RVA 0x1128DD50 `；selector ` 0 `；EOL ` RVA 0x354479F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-07f922278f1487cc](../../evidence/state_effects-sets-002.md#s-07f922278f1487cc)

### path-050143

```text
(config)# do-exec show ip dhcp sip statistics <cr>
```

Handler ` RVA 0x1128D470 `；selector ` 0 `；EOL ` RVA 0x35447E40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-041009

```text
(config)# do-exec show ip dhcp snooping <cr>
```

Handler ` RVA 0x15FA8760 `；selector ` 0 `；EOL ` RVA 0x35E812A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57e2b32a5e9aa365](../../evidence/conditions-sets-034.md#c-57e2b32a5e9aa365) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050243

```text
(config)# do-exec show ip dhcp snooping binding <cr>
```

Handler ` RVA 0x15FA9210 `；selector ` 0 `；EOL ` RVA 0x35E80808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0685e120ec15d920](../../evidence/conditions-sets-003.md#c-0685e120ec15d920) · [状态效果 S-b73345115eb62009](../../evidence/state_effects-sets-039.md#s-b73345115eb62009)

### path-062159

```text
(config)# do-exec show ip dhcp snooping binding <interface> <cr>
```

Handler ` RVA 0x15FA9210 `；selector ` 0 `；EOL ` RVA 0x35E80808 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f423aff57ac569ec](../../evidence/conditions-sets-094.md#c-f423aff57ac569ec) · [缺口 G-4ae8bcff98042fc0](../../evidence/gaps-sets-003.md#g-4ae8bcff98042fc0) · [参数 P-414176b6509a1716](../../evidence/parameters-sets-005.md#p-414176b6509a1716) · [状态效果 S-1ea633f8de534f48](../../evidence/state_effects-sets-007.md#s-1ea633f8de534f48)

### path-050113

```text
(config)# do-exec show ip dhcp snooping database <cr>
```

Handler ` RVA 0x15FAA370 `；selector ` 0 `；EOL ` RVA 0x35E80FD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3d0680b18a1c54be](../../evidence/conditions-sets-024.md#c-3d0680b18a1c54be) · [状态效果 S-870a4b096c986d16](../../evidence/state_effects-sets-029.md#s-870a4b096c986d16)

### path-050074

```text
(config)# do-exec show ip dhcp snooping multi-chassis <cr>
```

Handler ` RVA 0x15FAAA70 `；selector ` 0 `；EOL ` RVA 0x35E801F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0e0f9f86235fa280](../../evidence/conditions-sets-006.md#c-0e0f9f86235fa280) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-050114

```text
(config)# do-exec show ip dhcp snooping statistics <cr>
```

Handler ` RVA 0x15FA9710 `；selector ` 0 `；EOL ` RVA 0x35E812F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-57e2b32a5e9aa365](../../evidence/conditions-sets-034.md#c-57e2b32a5e9aa365) · [状态效果 S-c11125b4704b5416](../../evidence/state_effects-sets-041.md#s-c11125b4704b5416)

### path-055826

```text
(config)# do-exec show ip dhcp snooping track host <cr>
```

Handler ` RVA 0x15FA2CD0 `；selector ` 0 `；EOL ` RVA 0x35E7FF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fcad73cf3f2fc176](../../evidence/conditions-sets-097.md#c-fcad73cf3f2fc176) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062434

```text
(config)# do-exec show ip dhcp vrf <string> binding * <cr>
```

Handler ` RVA 0xD298440 `；selector ` 8 `；EOL ` RVA 0x33DE08F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` string ` VRF name。

[条件 C-033c18ec013f25fc](../../evidence/conditions-sets-002.md#c-033c18ec013f25fc) · [缺口 G-9e1b18fdc4821f49](../../evidence/gaps-sets-006.md#g-9e1b18fdc4821f49) · [参数 P-29398c16343455a3](../../evidence/parameters-sets-004.md#p-29398c16343455a3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058638

```text
(config)# do-exec show ip dhcp vrf <string> binding <address> <cr>
```

Handler ` RVA 0xD298440 `；selector ` 9 `；EOL ` RVA 0x33DE0C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name；` address ` Show a specific binding in a VRF。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-2b5d8d8b934943db](../../evidence/parameters-sets-004.md#p-2b5d8d8b934943db) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058605

```text
(config)# do-exec show ip dhcp vrf <string> binding assigned <cr>
```

Handler ` RVA 0xD298440 `；selector ` 8 `；EOL ` RVA 0x33DE08F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` VRF name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-29398c16343455a3](../../evidence/parameters-sets-004.md#p-29398c16343455a3) · [状态效果 S-0d4c4c7f3078e8cc](../../evidence/state_effects-sets-003.md#s-0d4c4c7f3078e8cc)

### path-039866

```text
(config)# do-exec show ip dns name-list <cr>
```

Handler ` RVA 0xD16CAF0 `；selector ` 0 `；EOL ` RVA 0x33D9AAA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039922

```text
(config)# do-exec show ip dns primary <cr>
```

Handler ` RVA 0xD134080 `；selector ` 1 `；EOL ` RVA 0x33D9AD90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039958

```text
(config)# do-exec show ip dns servers <cr>
```

Handler ` RVA 0xD1337C0 `；selector ` 0 `；EOL ` RVA 0x33D9B2B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039901

```text
(config)# do-exec show ip dns statistics <cr>
```

Handler ` RVA 0xD134080 `；selector ` 2 `；EOL ` RVA 0x33D9B010 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039933

```text
(config)# do-exec show ip dns view <cr>
```

Handler ` RVA 0xD132740 `；selector ` 0 `；EOL ` RVA 0x33D9A408 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ebb1802116352cc3](../../evidence/conditions-sets-091.md#c-ebb1802116352cc3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039815

```text
(config)# do-exec show ip dns view-list <cr>
```

Handler ` RVA 0xD16E690 `；selector ` 0 `；EOL ` RVA 0x33D9A7B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031176

```text
(config)# do-exec show ip domain-name <cr>
```

Handler ` RVA 0xCF2CF20 `；selector ` 0 `；EOL ` RVA 0x33D32E28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031386

```text
(config)# do-exec show ip drp <cr>
```

Handler ` RVA 0xF4F09B0 `；selector ` 0 `；EOL ` RVA 0x34679008 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040337

```text
(config)# do-exec show ip eigrp accounting <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 98 `；EOL ` RVA 0x346DBEF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-459016105323cbf3](../../evidence/conditions-sets-027.md#c-459016105323cbf3) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-040317

```text
(config)# do-exec show ip eigrp interfaces <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x346DADC8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-28a5728966043987](../../evidence/conditions-sets-016.md#c-28a5728966043987) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-061576

```text
(config)# do-exec show ip eigrp interfaces <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 89 `；EOL ` RVA 0x346DADC8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-94eb612f59666c6d](../../evidence/conditions-sets-058.md#c-94eb612f59666c6d) · [缺口 G-1d76c37cdf9433ef](../../evidence/gaps-sets-002.md#g-1d76c37cdf9433ef) · [参数 P-e9c8852ddbde1b77](../../evidence/parameters-sets-017.md#p-e9c8852ddbde1b77) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-040363

```text
(config)# do-exec show ip eigrp neighbors <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x346DA8D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-075c66f1681fd627](../../evidence/conditions-sets-003.md#c-075c66f1681fd627) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-061579

```text
(config)# do-exec show ip eigrp neighbors <interface> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 90 `；EOL ` RVA 0x346DA8D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-a5096d229c7c27f8](../../evidence/conditions-sets-064.md#c-a5096d229c7c27f8) · [缺口 G-ea2bc9caefcb8e78](../../evidence/gaps-sets-008.md#g-ea2bc9caefcb8e78) · [参数 P-cfe916be7650cb18](../../evidence/parameters-sets-016.md#p-cfe916be7650cb18) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-040422

```text
(config)# do-exec show ip eigrp sia-event <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x346DC240 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-459016105323cbf3](../../evidence/conditions-sets-027.md#c-459016105323cbf3) · [状态效果 S-e3e68bec47b96b73](../../evidence/state_effects-sets-048.md#s-e3e68bec47b96b73)

### path-040483

```text
(config)# do-exec show ip eigrp sia-statistics <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 99 `；EOL ` RVA 0x346DC5C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-459016105323cbf3](../../evidence/conditions-sets-027.md#c-459016105323cbf3) · [状态效果 S-024bef6925bc2529](../../evidence/state_effects-sets-001.md#s-024bef6925bc2529)

### path-040223

```text
(config)# do-exec show ip eigrp timers <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 95 `；EOL ` RVA 0x346DB098 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-459016105323cbf3](../../evidence/conditions-sets-027.md#c-459016105323cbf3) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-040658

```text
(config)# do-exec show ip eigrp topology <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x346DB6F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-69035e8b22b344c1](../../evidence/conditions-sets-041.md#c-69035e8b22b344c1) · [状态效果 S-1359048dd8bde631](../../evidence/state_effects-sets-005.md#s-1359048dd8bde631)

### path-061600

```text
(config)# do-exec show ip eigrp topology <prefix:dynamic> <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 97 `；EOL ` RVA 0x346DB6F8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Prefix &lt;network&gt;/&lt;length&gt;, e.g., 192.168.0.0/16。

[条件 C-405c93034eec15b0](../../evidence/conditions-sets-025.md#c-405c93034eec15b0) · [缺口 G-293d570fc1b9fc60](../../evidence/gaps-sets-002.md#g-293d570fc1b9fc60) · [参数 P-7d6f9034aaa5c9b0](../../evidence/parameters-sets-010.md#p-7d6f9034aaa5c9b0) · [状态效果 S-993aa277ef302343](../../evidence/state_effects-sets-033.md#s-993aa277ef302343)

### path-040266

```text
(config)# do-exec show ip eigrp traffic <cr>
```

Handler ` RVA 0xF573CD0 `；selector ` 96 `；EOL ` RVA 0x346DB340 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-459016105323cbf3](../../evidence/conditions-sets-027.md#c-459016105323cbf3) · [状态效果 S-a2b290e2609071c5](../../evidence/state_effects-sets-034.md#s-a2b290e2609071c5)

### path-031626

```text
(config)# do-exec show ip extcommunity-list <cr>
```

Handler ` RVA 0xE246790 `；selector ` 0 `；EOL ` RVA 0x344BAF20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ebdc4828df6eb2a9](../../evidence/conditions-sets-091.md#c-ebdc4828df6eb2a9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031765

```text
(config)# do-exec show ip ftp-password <cr>
```

Handler ` RVA 0xD018280 `；selector ` 4 `；EOL ` RVA 0x33D856C0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031745

```text
(config)# do-exec show ip ftp-username <cr>
```

Handler ` RVA 0xD018280 `；selector ` 3 `；EOL ` RVA 0x33D85418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031257

```text
(config)# do-exec show ip helper-address <cr>
```

Handler ` RVA 0xCF36E40 `；selector ` 0 `；EOL ` RVA 0x33D331B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d974ccae2de28e60](../../evidence/conditions-sets-084.md#c-d974ccae2de28e60) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060965

```text
(config)# do-exec show ip helper-address <interface> <cr>
```

Handler ` RVA 0xCF36E40 `；selector ` 0 `；EOL ` RVA 0x33D331B8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-4192ba71d1835909](../../evidence/conditions-sets-026.md#c-4192ba71d1835909) · [缺口 G-23c1e3a3b9f23f38](../../evidence/gaps-sets-002.md#g-23c1e3a3b9f23f38) · [参数 P-d68acf3c1ecbff1a](../../evidence/parameters-sets-016.md#p-d68acf3c1ecbff1a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032091

```text
(config)# do-exec show ip host-list <cr>
```

Handler ` RVA 0xF4878A0 `；selector ` 0 `；EOL ` RVA 0x3465B6B8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048656

```text
(config)# do-exec show ip http client all <cr>
```

Handler ` RVA 0xD1D40C0 `；selector ` 14 `；EOL ` RVA 0x33DB4600 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048942

```text
(config)# do-exec show ip http client cache <cr>
```

Handler ` RVA 0xD1D3BD0 `；selector ` 16 `；EOL ` RVA 0x33DB4E88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055106

```text
(config)# do-exec show ip http client cache brief <cr>
```

Handler ` RVA 0xD1D3BD0 `；selector ` 17 `；EOL ` RVA 0x33DB4E60 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048784

```text
(config)# do-exec show ip http client connection <cr>
```

Handler ` RVA 0xD1D3570 `；selector ` 20 `；EOL ` RVA 0x33DB4B50 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055283

```text
(config)# do-exec show ip http client cookie summary <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 23 `；EOL ` RVA 0x33DB5A08 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-b8f0fae70fe26fb8](../../evidence/state_effects-sets-039.md#s-b8f0fae70fe26fb8)

### path-059474

```text
(config)# do-exec show ip http client cookie summary domain <string> <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 25 `；EOL ` RVA 0x33DB5760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client cookie domain (or) host name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-5d48c863bc7d385e](../../evidence/parameters-sets-007.md#p-5d48c863bc7d385e) · [状态效果 S-b8f0fae70fe26fb8](../../evidence/state_effects-sets-039.md#s-b8f0fae70fe26fb8)

### path-059476

```text
(config)# do-exec show ip http client cookie summary name <string> <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 26 `；EOL ` RVA 0x33DB5A48 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client cookie name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-acf97ba8b51a0b28](../../evidence/parameters-sets-013.md#p-acf97ba8b51a0b28) · [状态效果 S-b8f0fae70fe26fb8](../../evidence/state_effects-sets-039.md#s-b8f0fae70fe26fb8)

### path-059471

```text
(config)# do-exec show ip http client cookie summary session <string> <cr>
```

Handler ` RVA 0xD1D41F0 `；selector ` 24 `；EOL ` RVA 0x33DB5478 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Client session name。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-64ac1130dd55272a](../../evidence/parameters-sets-008.md#p-64ac1130dd55272a) · [状态效果 S-b8f0fae70fe26fb8](../../evidence/state_effects-sets-039.md#s-b8f0fae70fe26fb8)

### path-048597

```text
(config)# do-exec show ip http client history <cr>
```

Handler ` RVA 0xD1D39C0 `；selector ` 19 `；EOL ` RVA 0x33DB4358 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055259

```text
(config)# do-exec show ip http client secure status <cr>
```

Handler ` RVA 0xC49F370 `；selector ` 22 `；EOL ` RVA 0x33A9AA78 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048526

```text
(config)# do-exec show ip http client session-module <cr>
```

Handler ` RVA 0xD1D3DD0 `；selector ` 15 `；EOL ` RVA 0x33DB40B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048712

```text
(config)# do-exec show ip http client statistics <cr>
```

Handler ` RVA 0xD1D3930 `；selector ` 18 `；EOL ` RVA 0x33DB48A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048470

```text
(config)# do-exec show ip http server all <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 1 `；EOL ` RVA 0x33DB1C40 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048716

```text
(config)# do-exec show ip http server connection <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 10 `；EOL ` RVA 0x33DB3598 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055088

```text
(config)# do-exec show ip http server external registration <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 5 `；EOL ` RVA 0x33DB2AE0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-db6b8eb1765de98b](../../evidence/conditions-sets-084.md#c-db6b8eb1765de98b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058253

```text
(config)# do-exec show ip http server external registration <string> <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 6 `；EOL ` RVA 0x33DB2808 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of registered url。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-fb0953dfbba3d052](../../evidence/parameters-sets-019.md#p-fb0953dfbba3d052) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058312

```text
(config)# do-exec show ip http server external statistics data <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 9 `；EOL ` RVA 0x33DB32D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058289

```text
(config)# do-exec show ip http server external statistics registration <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 8 `；EOL ` RVA 0x33DB3030 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058271

```text
(config)# do-exec show ip http server external statistics summary <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 7 `；EOL ` RVA 0x33DB2D88 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048925

```text
(config)# do-exec show ip http server help-path <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 13 `；EOL ` RVA 0x33DB3D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048852

```text
(config)# do-exec show ip http server history <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 12 `；EOL ` RVA 0x33DB3AE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055261

```text
(config)# do-exec show ip http server secure status <cr>
```

Handler ` RVA 0xC49E900 `；selector ` 21 `；EOL ` RVA 0x33A9A070 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048748

```text
(config)# do-exec show ip http server session-module <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 3 `；EOL ` RVA 0x33DB24D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-ae207b016ffbb75b](../../evidence/conditions-sets-067.md#c-ae207b016ffbb75b) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-054961

```text
(config)# do-exec show ip http server session-module <string> <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 4 `；EOL ` RVA 0x33DB21F8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` string ` Name of a session module。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [参数 P-c24c9205b4226549](../../evidence/parameters-sets-015.md#p-c24c9205b4226549) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048786

```text
(config)# do-exec show ip http server statistics <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 11 `；EOL ` RVA 0x33DB3840 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048538

```text
(config)# do-exec show ip http server status <cr>
```

Handler ` RVA 0xD1D4580 `；selector ` 2 `；EOL ` RVA 0x33DB1EE8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038109

```text
(config)# do-exec show ip icmp rate-limit <cr>
```

Handler ` RVA 0xCFE5270 `；selector ` 0 `；EOL ` RVA 0x33D31238 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-c63d682b2df6a176](../../evidence/conditions-sets-076.md#c-c63d682b2df6a176) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061465

```text
(config)# do-exec show ip icmp rate-limit <interface> <cr>
```

Handler ` RVA 0xCFE5270 `；selector ` 0 `；EOL ` RVA 0x33D31238 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-9cf029990246ee68](../../evidence/conditions-sets-061.md#c-9cf029990246ee68) · [缺口 G-ed14de01b6abefba](../../evidence/gaps-sets-008.md#g-ed14de01b6abefba) · [参数 P-48a213035c927ce5](../../evidence/parameters-sets-006.md#p-48a213035c927ce5) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040019

```text
(config)# do-exec show ip igmp filter <cr>
```

Handler ` RVA 0xE7AFD20 `；selector ` 0 `；EOL ` RVA 0x343394C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0810e3d3bb81feb9](../../evidence/conditions-sets-003.md#c-0810e3d3bb81feb9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039804

```text
(config)# do-exec show ip igmp gir <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 42 `；EOL ` RVA 0x3472C608 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-68a09ad1e03566e6](../../evidence/conditions-sets-040.md#c-68a09ad1e03566e6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039714

```text
(config)# do-exec show ip igmp groups <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 4 `；EOL ` RVA 0x3472AE20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-230fc2240c05eb04](../../evidence/conditions-sets-014.md#c-230fc2240c05eb04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061523

```text
(config)# do-exec show ip igmp groups <interface> <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 4 `；EOL ` RVA 0x3472AE20 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5f77020d680c9936](../../evidence/conditions-sets-037.md#c-5f77020d680c9936) · [缺口 G-d7ae899b084ec470](../../evidence/gaps-sets-007.md#g-d7ae899b084ec470) · [参数 P-40db9dd45ed1ddcd](../../evidence/parameters-sets-005.md#p-40db9dd45ed1ddcd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062054

```text
(config)# do-exec show ip igmp groups <interface> detail <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 28 `；EOL ` RVA 0x3472ADF8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-5f77020d680c9936](../../evidence/conditions-sets-037.md#c-5f77020d680c9936) · [缺口 G-d7ae899b084ec470](../../evidence/gaps-sets-007.md#g-d7ae899b084ec470) · [参数 P-40db9dd45ed1ddcd](../../evidence/parameters-sets-005.md#p-40db9dd45ed1ddcd) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048610

```text
(config)# do-exec show ip igmp groups detail <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 28 `；EOL ` RVA 0x3472ADF8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-230fc2240c05eb04](../../evidence/conditions-sets-014.md#c-230fc2240c05eb04) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039486

```text
(config)# do-exec show ip igmp interface <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 5 `；EOL ` RVA 0x3472A9A8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-bca2cd6f6d4303db](../../evidence/conditions-sets-073.md#c-bca2cd6f6d4303db) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-061512

```text
(config)# do-exec show ip igmp interface <interface> <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 5 `；EOL ` RVA 0x3472A9A8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-33fcdf8bcdc3b09c](../../evidence/conditions-sets-020.md#c-33fcdf8bcdc3b09c) · [缺口 G-db75ed2e13a7b533](../../evidence/gaps-sets-008.md#g-db75ed2e13a7b533) · [参数 P-52e579f658d4dd94](../../evidence/parameters-sets-007.md#p-52e579f658d4dd94) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039823

```text
(config)# do-exec show ip igmp membership <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 31 `；EOL ` RVA 0x3472BE80 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040025

```text
(config)# do-exec show ip igmp profile <cr>
```

Handler ` RVA 0xE7B30A0 `；selector ` 2 `；EOL ` RVA 0x3433A878 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-0810e3d3bb81feb9](../../evidence/conditions-sets-003.md#c-0810e3d3bb81feb9) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048970

```text
(config)# do-exec show ip igmp profile <number:1..4294967295> <cr>
```

Handler ` RVA 0xE7B30A0 `；selector ` 1 `；EOL ` RVA 0x3433A850 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` Profile number。

[条件 C-0810e3d3bb81feb9](../../evidence/conditions-sets-003.md#c-0810e3d3bb81feb9) · [参数 P-6dcf44850ec5b755](../../evidence/parameters-sets-009.md#p-6dcf44850ec5b755) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040247

```text
(config)# do-exec show ip igmp snooping <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 10 `；EOL ` RVA 0x33A54C20 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055275

```text
(config)# do-exec show ip igmp snooping bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 11 `；EOL ` RVA 0x33A47310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-2c8a704b385be8b5](../../evidence/conditions-sets-017.md#c-2c8a704b385be8b5) · [参数 P-62a440c0a1746977](../../evidence/parameters-sets-008.md#p-62a440c0a1746977) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058373

```text
(config)# do-exec show ip igmp snooping bd <number:1006..4094> forced <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 29 `；EOL ` RVA 0x33A472E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-9aa98306783ea6fa](../../evidence/conditions-sets-060.md#c-9aa98306783ea6fa) · [参数 P-62a440c0a1746977](../../evidence/parameters-sets-008.md#p-62a440c0a1746977) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062076

```text
(config)# do-exec show ip igmp snooping bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 11 `；EOL ` RVA 0x33A47310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-26b6da9c676349d9](../../evidence/conditions-sets-015.md#c-26b6da9c676349d9) · [缺口 G-4b0d124b1701eada](../../evidence/gaps-sets-003.md#g-4b0d124b1701eada) · [参数 P-5cad3408e6aed164](../../evidence/parameters-sets-007.md#p-5cad3408e6aed164) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062376

```text
(config)# do-exec show ip igmp snooping bd <number:dynamic> forced <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 29 `；EOL ` RVA 0x33A472E8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-5780cf975a239614](../../evidence/conditions-sets-034.md#c-5780cf975a239614) · [缺口 G-4b0d124b1701eada](../../evidence/gaps-sets-003.md#g-4b0d124b1701eada) · [参数 P-5cad3408e6aed164](../../evidence/parameters-sets-007.md#p-5cad3408e6aed164) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049144

```text
(config)# do-exec show ip igmp snooping counters <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 77 `；EOL ` RVA 0x33A490A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058405

```text
(config)# do-exec show ip igmp snooping counters bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 78 `；EOL ` RVA 0x33A490E0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-391c5d656160a31f](../../evidence/conditions-sets-022.md#c-391c5d656160a31f) · [参数 P-14d525f738305481](../../evidence/parameters-sets-002.md#p-14d525f738305481) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062383

```text
(config)# do-exec show ip igmp snooping counters bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 78 `；EOL ` RVA 0x33A490E0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-51f95d81ddca475a](../../evidence/conditions-sets-032.md#c-51f95d81ddca475a) · [缺口 G-14ec10243bfe0091](../../evidence/gaps-sets-001.md#g-14ec10243bfe0091) · [参数 P-bab0e90ae4e41e57](../../evidence/parameters-sets-014.md#p-bab0e90ae4e41e57) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058390

```text
(config)# do-exec show ip igmp snooping filter BD <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 51 `；EOL ` RVA 0x33A47950 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-c22c8f7988646117](../../evidence/conditions-sets-075.md#c-c22c8f7988646117) · [参数 P-dae9d46e28f0594c](../../evidence/parameters-sets-016.md#p-dae9d46e28f0594c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062379

```text
(config)# do-exec show ip igmp snooping filter BD <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 51 `；EOL ` RVA 0x33A47950 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-e082d569e6d54190](../../evidence/conditions-sets-086.md#c-e082d569e6d54190) · [缺口 G-ca1533759929be84](../../evidence/gaps-sets-007.md#g-ca1533759929be84) · [参数 P-e71149ed3d713055](../../evidence/parameters-sets-017.md#p-e71149ed3d713055) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-055351

```text
(config)# do-exec show ip igmp snooping filter et <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 54 `；EOL ` RVA 0x33A47D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8b49632dfa559c43](../../evidence/conditions-sets-054.md#c-8b49632dfa559c43) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062539

```text
(config)# do-exec show ip igmp snooping filter et BD <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 54 `；EOL ` RVA 0x33A47D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-e26a5f997555700b](../../evidence/conditions-sets-087.md#c-e26a5f997555700b) · [缺口 G-6c072b28847e26af](../../evidence/gaps-sets-004.md#g-6c072b28847e26af) · [参数 P-cf9b0f93e60d04b2](../../evidence/parameters-sets-016.md#p-cf9b0f93e60d04b2) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062396

```text
(config)# do-exec show ip igmp snooping filter interface <interface> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 52 `；EOL ` RVA 0x33A484D8 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2a3d6d01e585afdd](../../evidence/conditions-sets-017.md#c-2a3d6d01e585afdd) · [缺口 G-08340c3d9423f65b](../../evidence/gaps-sets-001.md#g-08340c3d9423f65b) · [参数 P-f8df29fc34a51391](../../evidence/parameters-sets-019.md#p-f8df29fc34a51391) · [状态效果 S-f7712b6595c50cb4](../../evidence/state_effects-sets-052.md#s-f7712b6595c50cb4)

### path-062542

```text
(config)# do-exec show ip igmp snooping filter interface <interface> statistics <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 53 `；EOL ` RVA 0x33A488A0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-2a3d6d01e585afdd](../../evidence/conditions-sets-017.md#c-2a3d6d01e585afdd) · [缺口 G-08340c3d9423f65b](../../evidence/gaps-sets-001.md#g-08340c3d9423f65b) · [参数 P-f8df29fc34a51391](../../evidence/parameters-sets-019.md#p-f8df29fc34a51391) · [状态效果 S-f7712b6595c50cb4](../../evidence/state_effects-sets-052.md#s-f7712b6595c50cb4)

### path-049369

```text
(config)# do-exec show ip igmp snooping groups <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 17 `；EOL ` RVA 0x33A4A138 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d88fbc692e48435d](../../evidence/conditions-sets-083.md#c-d88fbc692e48435d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062398

```text
(config)# do-exec show ip igmp snooping groups bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 17 `；EOL ` RVA 0x33A4A138 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-5c4fe45c871ff46a](../../evidence/conditions-sets-036.md#c-5c4fe45c871ff46a) · [缺口 G-253009b156d6d3f2](../../evidence/gaps-sets-002.md#g-253009b156d6d3f2) · [参数 P-4435c17702c3672a](../../evidence/parameters-sets-006.md#p-4435c17702c3672a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062541

```text
(config)# do-exec show ip igmp snooping groups bd <number:dynamic> count <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 18 `；EOL ` RVA 0x33A49CB0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-c5705fd4b8eb26cd](../../evidence/conditions-sets-076.md#c-c5705fd4b8eb26cd) · [缺口 G-253009b156d6d3f2](../../evidence/gaps-sets-002.md#g-253009b156d6d3f2) · [参数 P-4435c17702c3672a](../../evidence/parameters-sets-006.md#p-4435c17702c3672a) · [状态效果 S-a19d17072c4d416f](../../evidence/state_effects-sets-034.md#s-a19d17072c4d416f)

### path-055329

```text
(config)# do-exec show ip igmp snooping groups count <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 18 `；EOL ` RVA 0x33A49CB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-4b7230eb2be6030f](../../evidence/state_effects-sets-017.md#s-4b7230eb2be6030f)

### path-049565

```text
(config)# do-exec show ip igmp snooping membership <cr>
```

Handler ` RVA 0xC31D110 `；selector ` 26 `；EOL ` RVA 0x33A5A510 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062406

```text
(config)# do-exec show ip igmp snooping membership interface <interface> <cr>
```

Handler ` RVA 0xC31D110 `；selector ` 26 `；EOL ` RVA 0x33A5A510 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-7d60bc38be427e57](../../evidence/conditions-sets-049.md#c-7d60bc38be427e57) · [缺口 G-81a662e2ea891482](../../evidence/gaps-sets-005.md#g-81a662e2ea891482) · [参数 P-a74b2fd3b966693e](../../evidence/parameters-sets-013.md#p-a74b2fd3b966693e) · [状态效果 S-f3283c12b5c44a7e](../../evidence/state_effects-sets-051.md#s-f3283c12b5c44a7e)

### path-049191

```text
(config)# do-exec show ip igmp snooping mrouter <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 12 `；EOL ` RVA 0x33A496D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c8d5e7b99f6d2b0](../../evidence/conditions-sets-048.md#c-7c8d5e7b99f6d2b0) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-058416

```text
(config)# do-exec show ip igmp snooping mrouter bd <number:1006..4094> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 13 `；EOL ` RVA 0x33A49710 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` unsigned_number ` BD number。

[条件 C-f944dfdd52c0910f](../../evidence/conditions-sets-096.md#c-f944dfdd52c0910f) · [参数 P-2f4b396e2c97b79a](../../evidence/parameters-sets-004.md#p-2f4b396e2c97b79a) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062389

```text
(config)# do-exec show ip igmp snooping mrouter bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 13 `；EOL ` RVA 0x33A49710 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-588155c208528fbc](../../evidence/conditions-sets-035.md#c-588155c208528fbc) · [缺口 G-0aefb1ced3d0cc86](../../evidence/gaps-sets-001.md#g-0aefb1ced3d0cc86) · [参数 P-4253578c0de1914e](../../evidence/parameters-sets-006.md#p-4253578c0de1914e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-049152

```text
(config)# do-exec show ip igmp snooping querier <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 14 `；EOL ` RVA 0x33A48D68 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-14f695302ab8cef3](../../evidence/conditions-sets-008.md#c-14f695302ab8cef3) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062387

```text
(config)# do-exec show ip igmp snooping querier bd <number:dynamic> <cr>
```

Handler ` RVA 0xC30A7F0 `；selector ` 14 `；EOL ` RVA 0x33A48D68 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` unsigned_number_dynamic ` BD number。

[条件 C-4d2b0c39f8118c9a](../../evidence/conditions-sets-030.md#c-4d2b0c39f8118c9a) · [缺口 G-b412d30a4995240d](../../evidence/gaps-sets-006.md#g-b412d30a4995240d) · [参数 P-05d7c715cf866bc4](../../evidence/parameters-sets-001.md#p-05d7c715cf866bc4) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039588

```text
(config)# do-exec show ip igmp ssm-mapping <cr>
```

Handler ` RVA 0xF6C18D0 `；selector ` 0 `；EOL ` RVA 0x3472B6D8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-048733

```text
(config)# do-exec show ip igmp static-group class-map <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 14 `；EOL ` RVA 0x3472C248 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062364

```text
(config)# do-exec show ip igmp static-group class-map interface <interface> <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 14 `；EOL ` RVA 0x3472C248 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-80b79a7b475b55a8](../../evidence/conditions-sets-050.md#c-80b79a7b475b55a8) · [缺口 G-dbed45866ae6de0f](../../evidence/gaps-sets-008.md#g-dbed45866ae6de0f) · [参数 P-32588745a6f60ae8](../../evidence/parameters-sets-004.md#p-32588745a6f60ae8) · [状态效果 S-ec3f232d4df057ec](../../evidence/state_effects-sets-050.md#s-ec3f232d4df057ec)

### path-039706

```text
(config)# do-exec show ip igmp udlr <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 6 `；EOL ` RVA 0x3472BA28 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-062060

```text
(config)# do-exec show ip igmp udlr interface <interface> <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 6 `；EOL ` RVA 0x3472BA28 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f3c2fedd1e20ff49](../../evidence/conditions-sets-094.md#c-f3c2fedd1e20ff49) · [缺口 G-bb33393ed523faaf](../../evidence/gaps-sets-007.md#g-bb33393ed523faaf) · [参数 P-a845eb219496b710](../../evidence/parameters-sets-013.md#p-a845eb219496b710) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-039530

```text
(config)# do-exec show ip igmp virtual-group-cache <cr>
```

Handler ` RVA 0xF6AC4F0 `；selector ` 41 `；EOL ` RVA 0x3472B3D0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038114

```text
(config)# do-exec show ip interface address <cr>
```

Handler ` RVA 0xCF36F30 `；selector ` 0 `；EOL ` RVA 0x33D30310 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-fc7d353b58500d65](../../evidence/conditions-sets-097.md#c-fc7d353b58500d65) · [状态效果 S-253204288e18f047](../../evidence/state_effects-sets-008.md#s-253204288e18f047)

### path-061476

```text
(config)# do-exec show ip interface address <interface> <cr>
```

Handler ` RVA 0xCF36F30 `；selector ` 0 `；EOL ` RVA 0x33D30310 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cb452c5783a3a57f](../../evidence/conditions-sets-078.md#c-cb452c5783a3a57f) · [缺口 G-a283d3503a383560](../../evidence/gaps-sets-006.md#g-a283d3503a383560) · [参数 P-eb983603e1fd151a](../../evidence/parameters-sets-018.md#p-eb983603e1fd151a) · [状态效果 S-253204288e18f047](../../evidence/state_effects-sets-008.md#s-253204288e18f047)

### path-062039

```text
(config)# do-exec show ip interface address <interface> stats <cr>
```

Handler ` RVA 0xCF38EA0 `；selector ` 0 `；EOL ` RVA 0x33D308D0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-cb452c5783a3a57f](../../evidence/conditions-sets-078.md#c-cb452c5783a3a57f) · [缺口 G-a283d3503a383560](../../evidence/gaps-sets-006.md#g-a283d3503a383560) · [参数 P-eb983603e1fd151a](../../evidence/parameters-sets-018.md#p-eb983603e1fd151a) · [状态效果 S-253204288e18f047](../../evidence/state_effects-sets-008.md#s-253204288e18f047)

### path-062533

```text
(config)# do-exec show ip interface address <interface> topology base stats <cr>
```

Handler ` RVA 0xCF38E30 `；selector ` 0 `；EOL ` RVA 0x33D30438 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-00ff64b7151e128c](../../evidence/conditions-sets-001.md#c-00ff64b7151e128c) · [缺口 G-a283d3503a383560](../../evidence/gaps-sets-006.md#g-a283d3503a383560) · [参数 P-eb983603e1fd151a](../../evidence/parameters-sets-018.md#p-eb983603e1fd151a) · [状态效果 S-ea0ecaf8c35682c9](../../evidence/state_effects-sets-050.md#s-ea0ecaf8c35682c9)

### path-031482

```text
(config)# do-exec show ip irdp <cr>
```

Handler ` RVA 0xE242F00 `；selector ` 0 `；EOL ` RVA 0x34285418 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3a2f6e9a1324f340](../../evidence/conditions-sets-022.md#c-3a2f6e9a1324f340) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-060979

```text
(config)# do-exec show ip irdp <interface> <cr>
```

Handler ` RVA 0xE242F00 `；selector ` 0 `；EOL ` RVA 0x34285418 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-e81ef15d397d15ce](../../evidence/conditions-sets-090.md#c-e81ef15d397d15ce) · [缺口 G-c8021c976e6b312d](../../evidence/gaps-sets-007.md#g-c8021c976e6b312d) · [参数 P-21e7ece8580a1d7c](../../evidence/parameters-sets-003.md#p-21e7ece8580a1d7c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031672

```text
(config)# do-exec show ip largecommunity-list <cr>
```

Handler ` RVA 0xF24B100 `；selector ` 0 `；EOL ` RVA 0x344BB208 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-2346960aeb93f3c7](../../evidence/conditions-sets-014.md#c-2346960aeb93f3c7) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038483

```text
(config)# do-exec show ip local policy <cr>
```

Handler ` RVA 0xFAD8CE0 `；selector ` 0 `；EOL ` RVA 0x34804760 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-038700

```text
(config)# do-exec show ip local pool <cr>
```

Handler ` RVA 0xCEB0290 `；selector ` 0 `；EOL ` RVA 0x33D18188 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-079064ca986a3a49](../../evidence/conditions-sets-003.md#c-079064ca986a3a49) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031523

```text
(config)# do-exec show ip masks <cr>
```

Handler ` RVA 0xE1D6200 `；selector ` 0 `；EOL ` RVA 0x3422EDA0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-d310395f1ac60a7d](../../evidence/conditions-sets-081.md#c-d310395f1ac60a7d) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-031731

```text
(config)# do-exec show ip mcache <cr>
```

Handler ` RVA 0xF6D6320 `；selector ` 0 `；EOL ` RVA 0x3474EDB0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-e85d0302d7ba3e1e](../../evidence/conditions-sets-090.md#c-e85d0302d7ba3e1e) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-032332

```text
(config)# do-exec show ip mfib <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5A98 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-67a3bfa8448891e3](../../evidence/conditions-sets-040.md#c-67a3bfa8448891e3) · [状态效果 S-1abafb0ce6023fe0](../../evidence/state_effects-sets-006.md#s-1abafb0ce6023fe0)

### path-061061

```text
(config)# do-exec show ip mfib <prefix:dynamic> <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5A98 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` Group IP address/prefix length。

[条件 C-11d63fd473301aa6](../../evidence/conditions-sets-007.md#c-11d63fd473301aa6) · [缺口 G-dc7d5cbf119053c2](../../evidence/gaps-sets-008.md#g-dc7d5cbf119053c2) · [参数 P-ded4f8c38fd20e36](../../evidence/parameters-sets-017.md#p-ded4f8c38fd20e36) · [状态效果 S-1abafb0ce6023fe0](../../evidence/state_effects-sets-006.md#s-1abafb0ce6023fe0)

### path-040516

```text
(config)# do-exec show ip mfib cable <cr>
```

Handler ` RVA 0x1197DD40 `；selector ` 0 `；EOL ` RVA 0x355B4548 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-a833d21703888db7](../../evidence/state_effects-sets-036.md#s-a833d21703888db7)

### path-062117

```text
(config)# do-exec show ip mfib instance <?option@55558ab098e8> rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5D90 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-298109b96d6b9495](../../evidence/conditions-sets-016.md#c-298109b96d6b9495) · [缺口 G-ad18df5efeec1d53](../../evidence/gaps-sets-006.md#g-ad18df5efeec1d53) · [状态效果 S-80d377d5f0b1b47c](../../evidence/state_effects-sets-027.md#s-80d377d5f0b1b47c)

### path-040573

```text
(config)# do-exec show ip mfib interface <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B54B0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-05d6f91ab27ef51f](../../evidence/conditions-sets-003.md#c-05d6f91ab27ef51f) · [状态效果 S-02ceef1c26987e62](../../evidence/state_effects-sets-001.md#s-02ceef1c26987e62)

### path-061621

```text
(config)# do-exec show ip mfib interface <interface> <cr>
```

Handler ` RVA 0x1197DBC0 `；selector ` 0 `；EOL ` RVA 0x355B54B0 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-f35b6854ec41a23b](../../evidence/conditions-sets-094.md#c-f35b6854ec41a23b) · [缺口 G-88d44b23760aaa1d](../../evidence/gaps-sets-005.md#g-88d44b23760aaa1d) · [参数 P-e548cae555bd5cdc](../../evidence/parameters-sets-017.md#p-e548cae555bd5cdc) · [状态效果 S-02ceef1c26987e62](../../evidence/state_effects-sets-001.md#s-02ceef1c26987e62)

### path-049487

```text
(config)# do-exec show ip mfib internal fibidb <cr>
```

Handler ` RVA 0x1197DE80 `；selector ` 0 `；EOL ` RVA 0x355B49A0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6cc7295b80f30cbd](../../evidence/state_effects-sets-023.md#s-6cc7295b80f30cbd)

### path-049793

```text
(config)# do-exec show ip mfib internal mem <cr>
```

Handler ` RVA 0x1197DF50 `；selector ` 0 `；EOL ` RVA 0x355B4CD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-f58ef08855c2513b](../../evidence/state_effects-sets-052.md#s-f58ef08855c2513b)

### path-040620

```text
(config)# do-exec show ip mfib rate-list <cr>
```

Handler ` RVA 0x1197C6E0 `；selector ` 0 `；EOL ` RVA 0x355B5D90 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-b52a3045f630d0b8](../../evidence/conditions-sets-070.md#c-b52a3045f630d0b8) · [状态效果 S-f2c91bbb18add8d2](../../evidence/state_effects-sets-051.md#s-f2c91bbb18add8d2)

### path-040403

```text
(config)# do-exec show ip mfib status <cr>
```

Handler ` RVA 0x1197C470 `；selector ` 0 `；EOL ` RVA 0x355B50E8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-6cc7295b80f30cbd](../../evidence/state_effects-sets-023.md#s-6cc7295b80f30cbd)

### path-031813

```text
(config)# do-exec show ip mpacket <cr>
```

Handler ` RVA 0xF70B090 `；selector ` 0 `；EOL ` RVA 0x347508C8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-3362a984c2c73b4c](../../evidence/conditions-sets-020.md#c-3362a984c2c73b4c) · [状态效果 S-0fbef734423d15b1](../../evidence/state_effects-sets-004.md#s-0fbef734423d15b1)

### path-040456

```text
(config)# do-exec show ip mrib client <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 1 `；EOL ` RVA 0x3537A9F0 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-019989db96fefde6](../../evidence/state_effects-sets-001.md#s-019989db96fefde6)

### path-061623

```text
(config)# do-exec show ip mrib route * <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x35379F38 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-194eb47d0d2a75b3](../../evidence/conditions-sets-010.md#c-194eb47d0d2a75b3) · [缺口 G-9f5d435a596140f8](../../evidence/gaps-sets-006.md#g-9f5d435a596140f8) · [状态效果 S-e20c509d2541756d](../../evidence/state_effects-sets-048.md#s-e20c509d2541756d)

### path-055664

```text
(config)# do-exec show ip mrib route <address> <address> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3537A398 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

参数提示：` address ` source IP address；` address ` source IP address。

[条件 C-ab93dc5ba85837d8](../../evidence/conditions-sets-066.md#c-ab93dc5ba85837d8) · [参数 P-d7ab31900369f8e6](../../evidence/parameters-sets-016.md#p-d7ab31900369f8e6) · [状态效果 S-39c38a03bba25f74](../../evidence/state_effects-sets-013.md#s-39c38a03bba25f74)

### path-040579

```text
(config)# do-exec show ip mrib route <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 0 `；EOL ` RVA 0x35379F38 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-4730806389d24414](../../evidence/conditions-sets-028.md#c-4730806389d24414) · [状态效果 S-019989db96fefde6](../../evidence/state_effects-sets-001.md#s-019989db96fefde6)

### path-061616

```text
(config)# do-exec show ip mrib route <prefix:dynamic> <cr>
```

Handler ` RVA 0x119BD650 `；selector ` 0 `；EOL ` RVA 0x3537A398 `。

语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

参数提示：` prefix_dynamic ` group IP address/prefix length。

[条件 C-277a870a126108fc](../../evidence/conditions-sets-015.md#c-277a870a126108fc) · [缺口 G-12174f1388aa4471](../../evidence/gaps-sets-001.md#g-12174f1388aa4471) · [参数 P-bd5aaf12b2b81081](../../evidence/parameters-sets-014.md#p-bd5aaf12b2b81081) · [状态效果 S-019989db96fefde6](../../evidence/state_effects-sets-001.md#s-019989db96fefde6)

### path-049433

```text
(config)# do-exec show ip mrib route summary <cr>
```

Handler ` RVA 0x119BB9A0 `；selector ` 3 `；EOL ` RVA 0x35379BD8 `。

语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-8246f8b85ee07dc6](../../evidence/conditions-sets-050.md#c-8246f8b85ee07dc6) · [状态效果 S-019989db96fefde6](../../evidence/state_effects-sets-001.md#s-019989db96fefde6)

