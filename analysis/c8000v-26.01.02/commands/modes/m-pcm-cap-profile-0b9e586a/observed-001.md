# pcm-cap-profile · 补充模式入口与历史连接

[模式索引](README.md) · [总索引](../../README.md)

### observed_connections-009772

```text
(config-pcmt-profile)# capture-tdm <?controller_action@55558b4bf970> analog-voice-port <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 8 `；EOL ` RVA 0x35F6B8F0 `。

模式根 ` RVA 0x35F68BF8 `；语法状态 ` partial_syntax_candidate `；跟踪状态 ` [null,null,0] `。

[条件 C-8a6d32c10dd11821](../../evidence/conditions-sets-054.md#c-8a6d32c10dd11821) · [缺口 G-ffb92afe32c4bd9e](../../evidence/gaps-sets-009.md#g-ffb92afe32c4bd9e) · [状态效果 S-aac65b562bb810a6](../../evidence/state_effects-sets-036.md#s-aac65b562bb810a6)

### observed_connections-009771

```text
(config-pcmt-profile)# default capture-tdm <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 8 `；EOL ` RVA 0x35F6B8F0 `。

模式根 ` RVA 0x35F68BF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,1,0] `。

[条件 C-04a542f5a3b8242b](../../evidence/conditions-sets-002.md#c-04a542f5a3b8242b) · [状态效果 S-1d69ea4d539cb736](../../evidence/state_effects-sets-007.md#s-1d69ea4d539cb736)

### observed_connections-009769

```text
(config-pcmt-profile)# exit <cr>
```

Handler ` RVA 0xDEE92A0 `；selector ` 0 `；EOL ` RVA 0x35F6C048 `。

模式根 ` RVA 0x35F68BF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [1,0,0] `。

[条件 C-7c9e29d1d49418c7](../../evidence/conditions-sets-048.md#c-7c9e29d1d49418c7)

### observed_connections-009770

```text
(config-pcmt-profile)# no capture-tdm <cr>
```

Handler ` RVA 0x1629F110 `；selector ` 8 `；EOL ` RVA 0x35F6B8F0 `。

模式根 ` RVA 0x35F68BF8 `；语法状态 ` syntax_candidate `；跟踪状态 ` [0,0,0] `。

[条件 C-fe5958d59c50b613](../../evidence/conditions-sets-098.md#c-fe5958d59c50b613) · [状态效果 S-a5f2b9061fbd5929](../../evidence/state_effects-sets-035.md#s-a5f2b9061fbd5929)
